#!/usr/bin/env python3
"""verify_t33.py — T33 (BountyRecon)

Gồm 4 phần:
  [1] BĂM TỪNG PHẦN — cô lập thay đổi CỦA RIÊNG T33 (base = nhánh T31, vì T33 xếp chồng)
  [2] BĂM TỪNG PHẦN — đối chiếu merge-base (main) -> work, cho CẢ 2 file
  [3] KIỂM THEO LỊCH SỬ (D-023 phép kiểm [2]) — mọi commit merge-base..HEAD
  [4] blob scope_github.md

QUY ƯỚC RANH GIỚI (ghi rõ; Reviewer1 từng lệch 1 ký tự vì quy ước khác):
  * dòng = str.splitlines()            -> BỎ ký tự kết thúc dòng (\\n, \\r\\n)
  * vùng = "\\n".join(dòng_a..dòng_b), 1-based, HAI ĐẦU ĐÓNG, KHÔNG có \\n ở cuối vùng
  * vùng "đã sửa" xác định bằng difflib.SequenceMatcher — KHÔNG đoán số dòng tay
  * mỗi vùng được băm theo CẢ HAI quy ước: (A) KHÔNG \\n cuối   (B) CÓ \\n cuối
    => nếu cả A và B khớp trước/sau thì kết luận KHÔNG phụ thuộc quy ước
"""
import difflib
import hashlib
import subprocess
import sys

CAND = "agents/bountyrecon/tasks/T3/CANDIDATES.md"
RECON = "security/gitlab/RECON.md"
SCOPE = "security/gitlab/SCOPE.md"
ALLOWED_PREFIX = "agents/bountyrecon/tasks/T33/"
# T33 XEP CHONG tren T31 => file cua T31 trong khoang merge-base..HEAD la HOP LE.
ALLOWED_PREFIXES = ("agents/bountyrecon/tasks/T31/", "agents/bountyrecon/tasks/T33/")
FIXED = (CAND, RECON)


def is_allowed(f):
    return f in FIXED or f.startswith(ALLOWED_PREFIXES)


def is_excluded(f):
    """Ban ghi LICH SU / bang chung cua task KHAC => khong duoc chạm."""
    if f.startswith(ALLOWED_PREFIXES):
        return False                      # T31/T33 la chinh minh
    if "FIX_2B" in f:
        return True
    if any(x in f for x in ("/T28/", "/T29/", "/T30/", "/T32/")):
        return True
    if "/EVIDENCE/" in f:
        return True
    return False


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout


def lines_at(ref, f):
    out = subprocess.run(["git", "show", f"{ref}:{f}"], capture_output=True, text=True)
    return None if out.returncode != 0 else out.stdout.splitlines()


def work(f):
    return open(f, encoding="utf-8").read().splitlines()


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def segments(before, after, label):
    sm = difflib.SequenceMatcher(a=before, b=after, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
    print(f"  {label}: dong TRUOC={len(before)} SAU={len(after)}")
    print(f"    opcodes khac: {[(o[0],o[1]+1,o[2],o[3]+1,o[4]) for o in ops]}")
    n = 0
    for tag, i1, i2, j1, j2 in ops:
        n += (i2 - i1)
        for k in range(i1, i2):
            print(f"      - {before[k][:110]}")
        for k in range(j1, j2):
            print(f"      + {after[k][:110]}")
    print(f"    DONG DA SUA: {n}")
    print("    VUNG KHONG DOI (A/B deu phai GIONG HET):")
    ok = True
    for bi, blk in enumerate(sm.get_matching_blocks()):
        if blk.size == 0:
            continue
        sa = "\n".join(before[blk.a:blk.a + blk.size])
        sb = "\n".join(after[blk.b:blk.b + blk.size])
        oa = h(sa) == h(sb)
        ob = h(sa + "\n") == h(sb + "\n")
        ok &= oa and ob
        print(f"      V{bi}: TRUOC {blk.a+1}..{blk.a+blk.size} (SAU {blk.b+1}..{blk.b+blk.size}) "
              f"n={blk.size}  (A){h(sa)}/{h(sb)} {'OK' if oa else 'KHAC!!'}  "
              f"(B){h(sa+chr(10))}/{h(sb+chr(10))} {'OK' if ob else 'KHAC!!'}")
    print(f"    => MOI VUNG KHONG DOI GIONG HET theo CA HAI quy uoc: {ok}")
    print()
    return ok, n


def verbatim(ls):
    def idx(p):
        for i, l in enumerate(ls):
            if p(l):
                return i
    i1, i2b = idx(lambda l: l.startswith("## 1.")), idx(lambda l: l.startswith("## 2b."))
    i3, i5 = idx(lambda l: l.startswith("## 3.")), idx(lambda l: l.startswith("## 5."))
    if None in (i1, i2b, i3, i5):
        return None
    return "\n".join(ls[i1:i2b] + ls[i3:i5])


def main():
    t33base = git("rev-parse", "origin/agent/bounty-recon/T31").strip()
    base = git("merge-base", "main", "HEAD").strip()
    head = git("rev-parse", "HEAD").strip()
    print("# verify_t33.py — T33 (BountyRecon)")
    print(f"# T33 xep chong tren T31: base cua T33 = {t33base[:12]} (origin/agent/bounty-recon/T31)")
    print(f"# merge-base main = {base[:12]}   head = {head[:12]}  (chua commit -> HEAD = T31)")
    print("# QUY UOC RANH GIOI: dong=splitlines(); vung='\\n'.join(...); hai dau DONG; khong \\n cuoi")
    print()

    print("=" * 78)
    print("[1] CO LAP THAY DOI CUA RIENG T33 (T31 -> cay lam viec)")
    print("=" * 78)
    ok1, n1 = segments(lines_at(t33base, CAND), work(CAND), CAND)
    ok2, n2 = segments(lines_at(t33base, RECON), work(RECON), RECON)

    print("=" * 78)
    print("[2] DOI CHIEU MERGE-BASE (main) -> CAY LAM VIEC, ca 2 file")
    print("=" * 78)
    ok3, n3 = segments(lines_at(base, CAND), work(CAND), CAND)
    ok4, n4 = segments(lines_at(base, RECON), work(RECON), RECON)

    print("=" * 78)
    print("[3] KIEM THEO LICH SU (D-023 phep kiem [2]) — moi commit merge-base..HEAD")
    print("=" * 78)
    commits = [c for c in git("rev-list", f"{base}..{head}").split() if c]
    print(f"  so commit: {len(commits)}")
    ok_allowed = True
    for c in commits:
        subj = git("log", "-1", "--format=%s", c).strip()
        files = [f for f in git("diff-tree", "--no-commit-id", "--name-only", "-r", c).split() if f]
        print(f"    {c[:12]}  {subj[:70]}")
        for f in files:
            allowed = is_allowed(f)
            ok_allowed &= allowed
            print(f"      {'OK        ' if allowed else '!!KHONG PHEP'}  {f}")
    print(f"  => moi file bi cham nam trong danh sach CHO PHEP: {ok_allowed}")
    print(f"     CHO PHEP = {CAND}, {RECON}, hoac thuoc {ALLOWED_PREFIXES}")
    # file bi loai tru
    touched = git("diff", "--name-only", f"{base}..{head}").split()
    bad = [f for f in touched if is_excluded(f)]
    print(f"  => file bi LOAI TRU bi cham: {len(bad)}  {bad if bad else ''}")
    print("     LOAI TRU = T28/FIX_2B.md, T28|T29|T30|T32/**, va moi EVIDENCE/** ngoai T31/T33")
    print()
    # vung nguyen van SCOPE.md qua MOI commit
    logc = [c for c in git("log", "--format=%H", "--", SCOPE).split() if c]
    print(f"  VUNG TRICH NGUYEN VAN cua {SCOPE} qua tung commit (tu merge-base tro di):")
    print(f"    {'commit':<14}{'parent':<14}{'cha':<18}{'commit':<18}KET QUA")
    okv = True
    checked = 0
    for c in logc:
        if subprocess.run(["git", "merge-base", "--is-ancestor", c, base]).returncode == 0:
            continue  # truoc merge-base
        parents = git("rev-list", "--parents", "-n", "1", c).split()
        if len(parents) < 2:
            continue
        p = parents[1]
        vc, vp = verbatim(lines_at(c, SCOPE)), verbatim(lines_at(p, SCOPE))
        if vc is None or vp is None:
            continue
        same = vc == vp
        okv &= same
        checked += 1
        print(f"    {c[:12]:<14}{p[:12]:<14}{h(vp):<18}{h(vc):<18}{'GIONG HET' if same else 'KHAC !!'}")
    print(f"    => so commit kiem: {checked}; VUNG NGUYEN VAN KHONG DOI: {okv}")
    if checked == 0:
        print(f"    GHI CHU: KHONG commit nao trong khoang {base[:12]}..{head[:12]} cham {SCOPE}")
        print("             => vung trich nguyen van duong nhien khong doi (T28/T29 da o trong main)")
    print()

    print("=" * 78)
    print("[4] blob scope_github.md")
    print("=" * 78)
    G = "agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md"
    want = "15c946ff956a3fdb466f7f9768081af29b812088"
    got, gotm = git("rev-parse", f"HEAD:{G}").strip(), git("rev-parse", f"main:{G}").strip()
    print(f"  HEAD -> {got}\n  main -> {gotm}\n  mong doi -> {want}")
    print(f"  => {'KHOP CA HAI' if got == gotm == want else 'LECH !!'}")
    print()
    print("=" * 78)
    print(f"TONG: [1] ok={ok1 and ok2} (sua {n1+n2} dong) | [2] ok={ok3 and ok4} (sua {n3+n4} dong) | "
          f"lich su ok={ok_allowed and okv} | blob={got == want}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
