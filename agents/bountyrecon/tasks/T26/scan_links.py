#!/usr/bin/env python3
"""scan_links.py (v2.1) — T26 (BountyRecon)

Quét TOÀN BỘ territory (`agents/bountyrecon/**`, `security/**`) tìm link
Markdown/HTML dạng TƯƠNG ĐỐI, giải theo đúng ngữ nghĩa Markdown (tương đối với
THƯ MỤC CHỨA FILE), rồi kiểm file đích có tồn tại thật không.

v2 sửa 2 lỗi phân loại của v1 (đã phát hiện khi tự chạy lại):
  * v1 coi `/css/site.css` trong HTML ĐÃ CAPTURE là link repo -> báo nhầm 127 "lỗi".
    Thực chất đó là đường dẫn của MÁY CHỦ GỐC, không phải của repo này.
  * v1 coi `lgtm-com.pentesting.semmle.net` là đường dẫn tương đối (vì có dấu `.`)
    -> phải là BARE HOST (không có scheme), tức trích nguyên văn.

Phân loại theo NGỮ CẢNH:
  AUTHORED  — file do người/agent viết (CANDIDATES.md, SCOPE.md, RECON.md...)
  CAPTURE   — file bằng chứng thô (trong EVIDENCE/, .html, .txt): nội dung là
              bản ghi từ nguồn ngoài => link trong đó KHÔNG thuộc repo này.

Kết quả:
  DEFECT    — link tương đối trong file AUTHORED, giải ra file KHÔNG tồn tại
              => ĐÂY là lỗi sai độ sâu cần sửa
  CAPTURED  — đường dẫn gốc-máy-chủ trong file CAPTURE => KHÔNG sửa
  BARE_HOST — target không scheme, trông như tên miền => trích nguyên văn, KHÔNG sửa

Chỉ ĐỌC. Không sửa file. Không dùng mạng.
"""
import os
import re
import subprocess
import sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
TERRITORIES = ("agents/bountyrecon", "security")

MD_LINK = re.compile(r"\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
HTML_LINK = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.I)
FENCE = re.compile(r"^\s*(```|~~~)")

SKIP_PREFIX = ("http://", "https://", "//", "mailto:", "tel:", "ftp://",
               "data:", "javascript:", "#")
# ten mien: nhan[.nhan]+  voi TLD chu >=2 ky tu, KHONG co dau /
HOSTNAME = re.compile(r"^[a-z0-9]([a-z0-9\-]*[a-z0-9])?"
                      r"(\.[a-z0-9]([a-z0-9\-]*[a-z0-9])?)*\.[a-z]{2,}$", re.I)


def git_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                         text=True, check=True).stdout
    return [p for p in out.splitlines() if p.strip()]


def iter_targets():
    for terr in TERRITORIES:
        base = os.path.join(ROOT, terr)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d != ".git"]
            for fn in filenames:
                if fn.endswith((".md", ".markdown", ".txt", ".html")):
                    yield os.path.join(dirpath, fn)


def is_capture(rel):
    return ("/EVIDENCE/" in rel) or rel.endswith((".html", ".txt"))


def classify(target):
    t = target.strip()
    if not t:
        return "SKIPPED", t
    low = t.lower()
    for p in SKIP_PREFIX:
        if low.startswith(p):
            return "SKIPPED", t
    path = unquote(t.split("#", 1)[0].split("?", 1)[0]).strip()
    if not path:
        return "SKIPPED", t
    if path.startswith("/"):
        return "ROOT_REL", path
    if path.startswith(("./", "../")):
        return "RELATIVE", path
    if "/" in path and not path.startswith("/"):
        return "RELATIVE", path
    # không có / : hoặc là bare host, hoặc là tên file trần
    if HOSTNAME.match(path) and not path.endswith((".md", ".html", ".txt", ".json")):
        return "BARE_HOST", path
    return "RELATIVE", path


def suggest(path, filedir, repo_files):
    """Tìm file repo có ĐUÔI khớp `path` (sau khi bỏ các ../), trả về đường dẫn đúng."""
    tail = re.sub(r"^(\.\./)+", "", path)
    tail = tail.lstrip("./")
    cands = []
    for f in repo_files:
        if f == tail or f.endswith("/" + tail):
            cands.append(f)
    if not cands:
        return None
    # ưu tiên đường dẫn khớp sâu nhất (đuôi dài nhất)
    cands.sort(key=lambda f: (len(tail), len(f)))
    best = cands[0]
    return os.path.relpath(os.path.join(ROOT, best), filedir), best


def main():
    repo_files = git_files()
    defects, captured, bare, fenced_defects = [], [], [], []
    ok = skipped = scanned = 0

    for abspath in sorted(iter_targets()):
        rel = os.path.relpath(abspath, ROOT)
        try:
            with open(abspath, encoding="utf-8", errors="replace") as fh:
                lines = fh.read().splitlines()
        except OSError:
            continue
        scanned += 1
        filedir = os.path.dirname(abspath)
        capture = is_capture(rel)
        in_fence = False
        for lineno, line in enumerate(lines, 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            # v2.1: bo inline-code span (`...`) truoc khi tim link, neu khong se
            # bat nham cac mau mo ta nhu `](…)` trong van xuoi -> bao dong gia.
            scanline = re.sub(r"`[^`]*`", "", line)
            for rx in (MD_LINK, HTML_LINK):
                for m in rx.finditer(scanline):
                    raw = m.group(1)
                    kind, path = classify(raw)
                    if kind == "SKIPPED":
                        skipped += 1
                        continue
                    if kind == "BARE_HOST":
                        # trong file CAPTURE thi day la ban ghi nguon ngoai, khong phai link ta
                        (captured if capture else bare).append((rel, lineno, raw))
                        continue
                    if kind == "ROOT_REL":
                        captured.append((rel, lineno, raw))
                        continue
                    cand = os.path.normpath(os.path.join(filedir, path))
                    if os.path.exists(cand):
                        ok += 1
                        continue
                    if capture:
                        captured.append((rel, lineno, raw))
                        continue
                    rec = (rel, lineno, raw, os.path.relpath(cand, ROOT),
                           suggest(path, filedir, repo_files))
                    (fenced_defects if in_fence else defects).append(rec)

    print("# scan_links.py v2.1 — T26 (BountyRecon)")
    print(f"# territory : {', '.join(TERRITORIES)}")
    print(f"# root      : {ROOT}")
    print(f"# file quet : {scanned}")
    print()

    print("=" * 72)
    print("## A. DEFECT — link tuong doi trong file AUTHORED, giai ra KHONG ton tai")
    print("=" * 72)
    if not defects:
        print("(khong co)")
    for rel, lineno, raw, resolved, sug in defects:
        print(f"\n{rel}:{lineno}")
        print(f"    target  : {raw}")
        print(f"    giai ra : {resolved}   -> KHONG TON TAI")
        if sug:
            print(f"    DE XUAT : {sug[0]}")
            print(f"              (file that: {sug[1]})")
        else:
            print("    DE XUAT : (khong tim thay file co duoi khop)")
    print()

    if fenced_defects:
        print("## A2. Trong code fence (khong duoc render) — hạ mức ưu tiên")
        for rel, lineno, raw, resolved, sug in fenced_defects:
            print(f"  {rel}:{lineno}  {raw} -> {resolved} (KHONG TON TAI)")
        print()

    print("=" * 72)
    print("## B. BARE HOST — target khong scheme, trong nhu ten mien")
    print("     => thuong la TRICH NGUYEN VAN. KHONG SUA.")
    print("=" * 72)
    if not bare:
        print("(khong co)")
    for rel, lineno, raw in bare:
        print(f"  {rel}:{lineno}  {raw}")
    print()

    print("=" * 72)
    print("## C. ROOT-RELATIVE trong file CAPTURE — duong dan cua MAY CHU GOC")
    print("     => khong phai link repo, KHONG SUA. (chi liet ke 5 vi du dau)")
    print("=" * 72)
    print(f"  tong so: {len(captured)}")
    for rel, lineno, raw in captured[:5]:
        print(f"  {rel}:{lineno}  {raw}")
    print()

    print("=" * 72)
    print("## TONG KET")
    print("=" * 72)
    print(f"  file da quet                        : {scanned}")
    print(f"  link tương đối OK                   : {ok}")
    print(f"  ** DEFECT (sai độ sâu, cần sửa)     : {len(defects)} **")
    print(f"  DEFECT trong code fence (không render): {len(fenced_defects)}")
    print(f"  BARE_HOST (trích nguyên văn)        : {len(bare)}")
    print(f"  ROOT_REL trong file CAPTURE (bỏ qua): {len(captured)}")
    print(f"  SKIPPED (http/https/anchor...)      : {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
