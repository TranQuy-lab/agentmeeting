#!/usr/bin/env python3
"""history_check_t31.py — T31 (BountyRecon)

D-023 phép kiểm [2]: KIỂM TOÀN VẸN VÙNG TRÍCH NGUYÊN VĂN **THEO LỊCH SỬ**,
không chỉ so 2 điểm. Mục đích: bịt kẽ hở K1 — một commit trung gian "sửa rồi revert"
sẽ LỌT qua phép so 2 điểm (trước/head) nhưng bị bắt ở đây.

Hai phần:
  (A) Mọi commit của nhánh T31 (merge-base..HEAD): liệt kê file bị chạm, đối chiếu
      danh sách CHO PHÉP, và băm vùng trích nguyên văn của 2 file SỬA so với CHA.
  (B) Toàn bộ chuỗi commit đã chạm `security/gitlab/SCOPE.md` (T28 -> T29 -> ...):
      tại MỖI commit, băm vùng trích nguyên văn và so với CHA.

QUY ƯỚC RANH GIỚI (như verify_t31.py):
  * dòng = splitlines() (bỏ \\n cuối dòng)
  * vùng = "\\n".join(...), 1-based, hai đầu ĐÓNG, KHÔNG có \\n ở cuối
  * VÙNG TRÍCH NGUYÊN VĂN của SCOPE.md =
        [từ dòng '## 1.'  .. trước dòng '## 2b.')   (§1 + §2 + §2a)
      + [từ dòng '## 3.'  .. trước dòng '## 5.')   (§3 + §4)
    => CỐ Ý loại §2b (đã sửa ở T28), §0, §5 — đó là phần tổng hợp, không phải nguyên văn.
"""
import hashlib
import subprocess
import sys

SCOPE = "security/gitlab/SCOPE.md"
FIXED = ["security/gitlab/RECON.md", "agents/bountyrecon/tasks/T3/CANDIDATES.md"]
ALLOWED_PREFIX = "agents/bountyrecon/tasks/T31/"


def git(*a):
    r = subprocess.run(["git"] + list(a), capture_output=True, text=True)
    return r.stdout


def lines_at(rev, f):
    out = subprocess.run(["git", "show", f"{rev}:{f}"], capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return out.stdout.splitlines()


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def verbatim(ls):
    """Vùng trích nguyên văn của SCOPE.md (loại §2b, §0, §5)."""
    def idx(pred):
        for i, l in enumerate(ls):
            if pred(l):
                return i
        return None
    i1 = idx(lambda l: l.startswith("## 1."))
    i2b = idx(lambda l: l.startswith("## 2b."))
    i3 = idx(lambda l: l.startswith("## 3."))
    i5 = idx(lambda l: l.startswith("## 5."))
    if None in (i1, i2b, i3, i5):
        return None
    return "\n".join(ls[i1:i2b] + ls[i3:i5])


def main():
    print("# history_check_t31.py — T31 (BountyRecon) — D-023 phep kiem [2]")
    print("# QUY UOC RANH GIOI: dong=splitlines(); vung='\\n'.join(...); hai dau DONG; khong \\n cuoi")
    print()
    branch = git("rev-parse", "--abbrev-ref", "HEAD").strip()
    base = git("merge-base", "main", "HEAD").strip()
    head = git("rev-parse", "HEAD").strip()
    print(f"branch     : {branch}")
    print(f"merge-base : {base[:12]}  (main)")
    print(f"head       : {head[:12]}")
    print()

    # ---------- (A) commit cua nhanh T31 ----------
    print("=" * 78)
    print("(A) MOI COMMIT CUA NHANH T31 — file bi cham + doi chieu danh sach CHO PHEP")
    print("=" * 78)
    commits = [c for c in git("rev-list", f"{base}..{head}").split() if c]
    print(f"so commit: {len(commits)}")
    ok_allowed = True
    for c in commits:
        subject = git("log", "-1", "--format=%s", c).strip()
        files = [f for f in git("diff-tree", "--no-commit-id", "--name-only", "-r", c).split() if f]
        print(f"\n  commit {c[:12]}  {subject[:80]}")
        for f in files:
            allowed = (f in FIXED) or f.startswith(ALLOWED_PREFIX)
            if not allowed:
                ok_allowed = False
            print(f"    {'OK  ' if allowed else '!!VI PHAM'}  {f}")
    print(f"\n  => moi file bi cham nam trong danh sach CHO PHEP: {ok_allowed}")
    print("  CHO PHEP = 2 file sua + moi thu trong agents/bountyrecon/tasks/T31/")
    print("  DANH SACH LOAI TRU (khong duoc xuat hien): T28/FIX_2B.md, T29/*, moi EVIDENCE/**")
    forbidden = git("diff", "--name-only", f"{base}..{head}")
    # v2: loai chinh T31/ khoi phep thu "bi cam" (bang chung cua T31 la HOP LE).
    #     Chi coi la vi pham neu cham ban ghi lich su cua T28/T29 hoac EVIDENCE khac.
    bad = [f for f in forbidden.split()
           if not f.startswith(ALLOWED_PREFIX)
           and ("FIX_2B" in f or "/T28/" in f or "/T29/" in f or "/EVIDENCE/" in f)]
    print(f"  => file bi LOAI TRU bi cham: {len(bad)}  {bad if bad else ''}")
    print("     (T31/EVIDENCE/** la bang chung cua chinh T31 => HOP LE, da loai khoi phep thu)")
    print()

    # ---------- (B) chuoi commit cham SCOPE.md ----------
    print("=" * 78)
    print("(B) CHUOI COMMIT DA CHAM security/gitlab/SCOPE.md — bam vung NGUYEN VAN moi commit")
    print("=" * 78)
    # lay moi commit trong lich su cua file, gioi han tu commit T28 tro di
    logc = [c for c in git("log", "--format=%H", "--", SCOPE).split() if c]
    print(f"so commit cham {SCOPE}: {len(logc)}")
    print()
    print(f"  {'commit':<14}{'parent':<14}{'nguyen van (cha)':<20}{'nguyen van (commit)':<21}KET QUA")
    ok_verbatim = True
    checked = 0
    for c in logc:
        parents = git("rev-list", "--parents", "-n", "1", c).split()
        if len(parents) < 2:
            continue
        p = parents[1]
        lc = lines_at(c, SCOPE)
        lp = lines_at(p, SCOPE)
        if lc is None or lp is None:
            continue
        vc, vp = verbatim(lc), verbatim(lp)
        if vc is None or vp is None:
            print(f"  {c[:12]:<14}{p[:12]:<14}{'(khong tim thay heading)':<20}")
            continue
        same = vc == vp
        ok_verbatim &= same
        checked += 1
        print(f"  {c[:12]:<14}{p[:12]:<14}{h(vp):<20}{h(vc):<21}{'GIONG HET' if same else 'KHAC !!'}")
    print()
    print(f"  => so commit da kiem: {checked}")
    print(f"  => VUNG TRICH NGUYEN VAN cua SCOPE.md KHONG DOI qua MOI commit: {ok_verbatim}")
    print("     (neu co commit trung gian 'sua roi revert', dong nay se la KHAC !!)")
    print()

    # ---------- (C) blob scope_github.md ----------
    print("=" * 78)
    print("(C) scope_github.md — phai van la 15c946ff956a3fdb466f7f9768081af29b812088")
    print("=" * 78)
    G = "agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md"
    want = "15c946ff956a3fdb466f7f9768081af29b812088"
    got = git("rev-parse", f"HEAD:{G}").strip()
    gotm = git("rev-parse", f"main:{G}").strip()
    print(f"  HEAD:{G}  -> {got}")
    print(f"  main:{G}  -> {gotm}")
    print(f"  mong doi          -> {want}")
    print(f"  => {'KHOP CA HAI' if got == gotm == want else 'LECH !!'}")
    print()
    print("=" * 78)
    print(f"TONG KET: cho phep={ok_allowed}  nguyen van khong doi={ok_verbatim}  "
          f"scope_github={got == want}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
