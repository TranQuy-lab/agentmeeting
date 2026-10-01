#!/usr/bin/env python3
"""verify_t34.py — T34+T36 (BountyRecon)

[1] BĂM TỪNG PHẦN — mọi vùng KHÔNG đổi phải GIỐNG HỆT TỪNG BYTE, băm theo CẢ HAI quy ước
[2] VÙNG NGUYÊN VĂN BẢO VỆ — băm riêng các khối trích dẫn (phải giống hệt trước/sau)
[3] KIỂM THEO LỊCH SỬ (D-023 [2])
[4] blob scope_github.md

QUY ƯỚC RANH GIỚI (ghi rõ; Reviewer1 từng lệch 1 ký tự vì quy ước khác):
  * dòng = str.splitlines()            -> BỎ ký tự kết thúc dòng (\\n, \\r\\n)
  * vùng = "\\n".join(dòng_a..dòng_b), 1-based, HAI ĐẦU ĐÓNG, KHÔNG có \\n ở cuối vùng
  * vùng "đã sửa" xác định bằng difflib.SequenceMatcher — KHÔNG đoán số dòng tay
  * mỗi vùng băm theo CẢ HAI quy ước: (A) KHÔNG \\n cuối   (B) CÓ \\n cuối
"""
import difflib
import hashlib
import re
import subprocess
import sys

FILES = [
    "security/gitlab/SCOPE.md",
    "security/github/SCOPE.md",
    "security/cloudflare/SCOPE.md",
    "security/gitlab/RECON.md",
    "security/github/RECON.md",
    "security/cloudflare/RECON.md",
    "agents/bountyrecon/tasks/T3/CANDIDATES.md",
    "agents/bountyrecon/tasks/T31/FIX_GROUP_B.md",
    "agents/bountyrecon/tasks/T31/history_check_t31.py",
    "agents/bountyrecon/tasks/T31/verify_t31.py",
]
# vùng NGUYÊN VĂN phải bảo vệ: (file, mô tả, regex TIÊU ĐỀ mục)
# Vùng = KHỐI FENCE ```...``` ĐẦU TIÊN sau tiêu đề đó.
# (Dùng khối fence, KHÔNG dùng "từ tiêu đề tới tiêu đề sau", vì T37 chèn khối [3b]
#  KHÔNG-nguyên-văn vào TRONG các mục đó — lấy cả mục sẽ báo KHÁC sai.)
PROTECTED = [
    ("security/gitlab/SCOPE.md", "§1 khoi POLICY PROSE (fence, KHONG doi)", r'^Policy prose bổ sung'),
    ("security/gitlab/SCOPE.md", "§2a out-of-scope (fence)", r'^### 2a\.'),
    ("security/gitlab/SCOPE.md", "§3 quy dinh cam (fence)", r'^## 3\.'),
    ("security/gitlab/SCOPE.md", "§4 muc thuong (fence)", r'^## 4\.'),
    ("security/github/SCOPE.md", "§1 in-scope (fence)", r'^## 1\.'),
    ("security/github/SCOPE.md", "§4b ineligible (fence)", r'^## 4b\.'),
    ("security/cloudflare/SCOPE.md", "§1 in-scope (fence)", r'^## 1\.'),
    ("security/cloudflare/SCOPE.md", "§3 quy dinh cam (fence)", r'^## 3\.'),
    ("security/github/RECON.md", "§1 bang DNS (fence)", r'^## 1\.'),
    ("security/cloudflare/RECON.md", "§1 bang DNS (fence)", r'^## 1\.'),
    ("security/gitlab/RECON.md", "§1 bang DNS (fence)", r'^## 1\.'),
]
ALLOWED_PREFIX = "agents/bountyrecon/tasks/T34/"
FIXED = tuple(FILES)
EXCLUDED_HINT = ("FIX_2B", "/T28/", "/T29/", "/T30/", "/T32/", "/T33/")


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout


def lines_at(ref, f):
    out = subprocess.run(["git", "show", f"{ref}:{f}"], capture_output=True, text=True)
    return None if out.returncode != 0 else out.stdout.splitlines()


def work(f):
    return open(f, encoding="utf-8").read().splitlines()


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def region(ls, heading_rx):
    """Vùng = KHỐI FENCE ```...``` ĐẦU TIÊN sau dòng khớp heading_rx.
    Trả về (i_mở_fence, i_đóng_fence) — bao gồm cả 2 dòng fence. None nếu không thấy."""
    hi = next((i for i, l in enumerate(ls) if re.search(heading_rx, l)), None)
    if hi is None:
        return None
    a = next((i for i in range(hi, len(ls)) if re.match(r'^\s*```', ls[i])), None)
    if a is None:
        return None
    b = next((i for i in range(a + 1, len(ls)) if re.match(r'^\s*```\s*$', ls[i])), None)
    if b is None:
        return None
    return a, b + 1


def main():
    base = git("merge-base", "main", "HEAD").strip()
    head = git("rev-parse", "HEAD").strip()
    print("# verify_t34.py — T34 + T36 (BountyRecon)")
    print(f"# merge-base main = {base[:12]}   head = {head[:12]}")
    print("# QUY UOC RANH GIOI: dong=splitlines(); vung='\\n'.join(...); hai dau DONG; khong \\n cuoi")
    print("#   Moi vung bam theo CA HAI quy uoc: (A) khong \\n cuoi (B) co \\n cuoi")
    print()
    all_ok = True
    total = 0
    print("=" * 78)
    print("[1] BAM TUNG PHAN — moi vung KHONG DOI phai GIONG HET (ca 2 quy uoc)")
    print("=" * 78)
    for f in FILES:
        before, after = lines_at(base, f), work(f)
        if before is None:
            print(f"  {f}: KHONG co o merge-base (file moi) -> bo qua")
            continue
        sm = difflib.SequenceMatcher(a=before, b=after, autojunk=False)
        ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
        n = sum(o[2] - o[1] for o in ops)
        total += n
        fileok = True
        for blk in sm.get_matching_blocks():
            if blk.size == 0:
                continue
            sa = "\n".join(before[blk.a:blk.a + blk.size])
            sb = "\n".join(after[blk.b:blk.b + blk.size])
            fileok &= (h(sa) == h(sb)) and (h(sa + "\n") == h(sb + "\n"))
        all_ok &= fileok
        print(f"  {f}")
        print(f"    dong {len(before)} -> {len(after)} | dong sua: {n} | "
              f"opcodes: {[(o[0],o[1]+1,o[2],o[3]+1,o[4]) for o in ops]}")
        print(f"    moi vung khong doi GIONG HET (ca A va B): {fileok}")
    print(f"\n  => TONG dong sua (10 file): {total} | tat ca vung khong doi OK: {all_ok}")
    print()

    print("=" * 78)
    print("[2] VUNG NGUYEN VAN BAO VE — phai GIONG HET truoc/sau")
    print("=" * 78)
    for f, label, hrx in PROTECTED:
        b, a = lines_at(base, f), work(f)
        rb, ra = region(b, hrx), region(a, hrx)
        if rb is None or ra is None:
            print(f"  {f} :: {label}: KHONG tim thay vung -> CANH BAO")
            all_ok = False
            continue
        sb = "\n".join(b[rb[0]:rb[1]])
        sa = "\n".join(a[ra[0]:ra[1]])
        ok = (sb == sa)
        all_ok &= ok
        print(f"  {f} :: {label}")
        print(f"    dong {rb[0]+1}..{rb[1]} (n={rb[1]-rb[0]})  A:{h(sb)}/{h(sa)}  "
              f"B:{h(sb+chr(10))}/{h(sa+chr(10))}  -> {'GIONG HET' if ok else 'KHAC !!'}")
    print()

    print("=" * 78)
    print("[3] KIEM THEO LICH SU (D-023 phep kiem [2])")
    print("=" * 78)
    commits = [c for c in git("rev-list", f"{base}..{head}").split() if c]
    print(f"  so commit trong merge-base..HEAD: {len(commits)}  (chua commit -> 0 la dung)")
    touched = git("diff", "--name-only", f"{base}..{head}").split()
    bad = [f for f in touched if not f.startswith(ALLOWED_PREFIX)
           and not f.startswith("agents/bountyrecon/tasks/T31/")
           and any(x in f for x in EXCLUDED_HINT)]
    print(f"  => file bi LOAI TRU bi cham: {len(bad)}  {bad if bad else ''}")
    print("     LOAI TRU = T28/FIX_2B.md, T28|T29|T30|T32|T33/**, moi EVIDENCE/** khac")
    print()

    print("=" * 78)
    print("[4] blob scope_github.md")
    print("=" * 78)
    G = "agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md"
    want = "15c946ff956a3fdb466f7f9768081af29b812088"
    got, gotm = git("rev-parse", f"HEAD:{G}").strip(), git("rev-parse", f"main:{G}").strip()
    print(f"  HEAD -> {got}\n  main -> {gotm}\n  mong doi -> {want}")
    ok4 = (got == gotm == want)
    print(f"  => {'KHOP CA HAI' if ok4 else 'LECH !!'}")
    print()
    print("=" * 78)
    print(f"TONG KET: vung khong doi + vung nguyen van OK={all_ok} | blob={ok4}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
