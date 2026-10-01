#!/usr/bin/env python3
"""verify_t41.py — T41 (BountyRecon)

[1] BĂM TỪNG PHẦN (CẢ HAI quy ước) — chỉ 2 dòng đổi, mọi vùng khác GIỐNG HỆT
[2] KIỂM THEO LỊCH SỬ (D-023 [2])
[3] QUÉT THEO NGHĨA (D-025 [3a]) — tìm dòng nói tài sản "bị loại/ngoài scope/không còn hiệu lực"
    MÀ CĂN CỨ là `archived_at` (bị cấm) — phân biệt với căn cứ CHÍNH SÁCH/LUẬT CẤM/QUYẾT ĐỊNH ADMIN (đúng).

QUY ƯỚC RANH GIỚI: dòng = splitlines() (bỏ \\n cuối dòng); vùng = "\\n".join(a..b), 1-based,
hai đầu ĐÓNG, không \\n ở cuối; vùng đổi xác định bằng difflib; băm theo CẢ (A) không \\n cuối
và (B) có \\n cuối.
"""
import difflib
import hashlib
import os
import re
import subprocess
import sys

FILES = ["agents/bountyrecon/tasks/T3/CANDIDATES.md", "security/gitlab/RECON.md"]
BASE_REF = "origin/agent/bounty-recon/T34"
ALLOWED_PREFIX = "agents/bountyrecon/tasks/T41/"
EXCLUDED_HINT = ("FIX_2B", "/T28/", "/T29/", "/T30/", "/T32/", "/T33/", "/T34/EVIDENCE/")

LIVE = ["security/gitlab/SCOPE.md", "security/github/SCOPE.md",
        "security/cloudflare/SCOPE.md", "security/gitlab/RECON.md",
        "security/github/RECON.md", "security/cloudflare/RECON.md",
        "agents/bountyrecon/tasks/T3/CANDIDATES.md"]
# các chỗ ĐÚNG (Reviewer1 liệt kê) — căn cứ chính sách/luật cấm/quyết định Admin -> ĐỪNG sửa
LEGIT = ["CANDIDATES.md G4/G5/G6", "gitlab/RECON.md:179-181", "cloudflare/RECON.md:158",
         "github/SCOPE.md:511", "4 khoi GIOI HAN (D-026)", "_TEMPLATE/SCOPE.md:46"]


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout


def lines_at(ref, f):
    o = subprocess.run(["git", "show", f"{ref}:{f}"], capture_output=True, text=True)
    return None if o.returncode != 0 else o.stdout.splitlines()


def work(f):
    return open(f, encoding="utf-8").read().splitlines()


def h(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def main():
    base = git("rev-parse", BASE_REF).strip()
    head = git("rev-parse", "HEAD").strip()
    print("# verify_t41.py — T41 (BountyRecon)")
    print(f"# T41 xep chong tren T34: base = {base[:12]} ({BASE_REF}) | HEAD = {head[:12]}")
    print("# QUY UOC: dong=splitlines(); vung='\\n'.join(a..b); hai dau DONG; khong \\n cuoi")
    print()
    ok = True
    print("=" * 78)
    print("[1] BAM TUNG PHAN — moi vung KHONG DOI phai GIONG HET (ca A va B)")
    print("=" * 78)
    for f in FILES:
        b, a = lines_at(base, f), work(f)
        sm = difflib.SequenceMatcher(a=b, b=a, autojunk=False)
        ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
        n = sum(o[2] - o[1] for o in ops)
        fok = True
        for blk in sm.get_matching_blocks():
            if blk.size == 0:
                continue
            sa = "\n".join(b[blk.a:blk.a + blk.size])
            sb = "\n".join(a[blk.b:blk.b + blk.size])
            fok &= (h(sa) == h(sb)) and (h(sa + "\n") == h(sb + "\n"))
        ok &= fok
        print(f"  {f}: dong {len(b)}->{len(a)} | dong sua: {n} | "
              f"opcodes {[(o[0],o[1]+1,o[2],o[3]+1,o[4]) for o in ops]}")
        for tag, i1, i2, j1, j2 in ops:
            for k in range(i1, i2):
                print(f"    - {b[k][:120]}")
            for k in range(j1, j2):
                print(f"    + {a[k][:120]}")
        print(f"    moi vung khong doi GIONG HET (ca A va B): {fok}")
    print(f"\n  => TAT CA VUNG KHONG DOI OK: {ok}")
    print()

    print("=" * 78)
    print("[2] KIEM THEO LICH SU (D-023 [2])")
    print("=" * 78)
    commits = [c for c in git("rev-list", f"{base}..{head}").split() if c]
    print(f"  so commit {base[:8]}..{head[:8]}: {len(commits)} (chua commit -> 0 la dung)")
    touched = git("diff", "--name-only", f"{base}..{head}").split()
    bad = [f for f in touched if not f.startswith(ALLOWED_PREFIX)
           and not f.startswith("agents/bountyrecon/tasks/T34/")
           and any(x in f for x in EXCLUDED_HINT)]
    print(f"  => file bi LOAI TRU bi cham: {len(bad)}  {bad if bad else ''}")
    print("     LOAI TRU = T28/FIX_2B.md, T28|T29|T30|T32|T33/**, T34/EVIDENCE/**")
    print()

    print("=" * 78)
    print("[3] QUET THEO NGHIA (D-025 [3a]) — can cu 'archived_at' cho ket luan loai/ngoai scope")
    print("=" * 78)
    print("  (cho DUNG da biet, can cu la chinh sach/luat cam/quyet dinh Admin -> KHONG vi pham:)")
    for x in LEGIT:
        print(f"    OK  {x}")
    print()
    BAD = re.compile(r"(bị loại|BỊ LOẠI|ngoài scope|NGOÀI scope|không còn hiệu lực|đã bị loại)")
    BASIS = re.compile(r"archived_at|nghỉ hưu|retired|đã retired")
    POLICY = re.compile(r"SCOPE\.md|chính sách|chinh sach|policy|D-0\d\d|luật cấm|ineligible|out-of-scope")
    viol = []
    for f in LIVE:
        for i, l in enumerate(work(f), 1):
            if BAD.search(l) and BASIS.search(l) and not POLICY.search(l):
                viol.append((f, i, l.strip()[:150]))
    if not viol:
        print("  => KHONG con dong nao ket luan 'loai/ngoai scope' ma can cu CHI la archived_at ✅")
    else:
        print(f"  => {len(viol)} DONG NGHI VI PHAM (can cu archived_at, khong co chinh sach):")
        for f, i, l in viol:
            print(f"    ⚠ {f}:{i}")
            print(f"       {l}")
    print()
    print("=" * 78)
    print(f"TONG: vung khong doi OK={ok} | file bi cam cham={len(bad)} | nghi vi pham={len(viol)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
