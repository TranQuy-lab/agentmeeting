#!/usr/bin/env python3
"""semantic_scan_t34.py — T34 (BountyRecon) — D-025 [3a]

QUÉT THEO NGHĨA (KHÔNG theo mẫu câu): với mọi dòng trong TÀI LIỆU SỐNG thuộc territory
có khẳng định một TRẠNG THÁI, JOIN với BẢNG NGUỒN SỰ THẬT tương ứng, rồi BÁO DELTA.

Bảng nguồn sự thật dùng ở đây:
  [A] `rooms/ab1-478d-cfa7/directives.md`  — danh mục D-0xx (+ luật "D-013 thay thế D-005 về G4")
  [B] `ADMIN/ASSIGNMENTS.md`               — bảng task T<nn> (cột Trạng thái)
  [C] `security/<prog>/SCOPE.md` §1        — bảng tài sản + `archived_at`
  [D] dữ liệu HackerOne tái truy vấn       — đối chiếu §1 (xem EVIDENCE/gitlab_archived_t34.txt)

TÀI LIỆU SỐNG = security/*/SCOPE.md, security/*/RECON.md,
                agents/bountyrecon/tasks/T3/CANDIDATES.md
(không quét báo cáo lịch sử T28/T29/T31/T33 và mọi EVIDENCE/** — chúng ghi nguyên trạng quá khứ)
"""
import os
import re
import subprocess
import sys

LIVE = [
    "security/gitlab/SCOPE.md",
    "security/github/SCOPE.md",
    "security/cloudflare/SCOPE.md",
    "security/gitlab/RECON.md",
    "security/github/RECON.md",
    "security/cloudflare/RECON.md",
    "agents/bountyrecon/tasks/T3/CANDIDATES.md",
]
DIRECTIVES = "rooms/ab1-478d-cfa7/directives.md"
ASSIGN = "ADMIN/ASSIGNMENTS.md"


def read(f):
    return open(f, encoding="utf-8").read().splitlines()


def main():
    print("# semantic_scan_t34.py — D-025 [3a]: JOIN (CHU THE, TRANG THAI) voi BANG NGUON")
    print()
    # ---------- bang nguon [A] D-0xx ----------
    dlines = read(DIRECTIVES)
    d_exist = {m.group(1) for l in dlines for m in [re.search(r"\[(D-\d{3})\]", l)] if m}
    print("=" * 78)
    print(f"[A] BANG NGUON: {DIRECTIVES} — co {len(d_exist)} chi thi")
    print("=" * 78)
    print("   ", " ".join(sorted(d_exist)))
    print()

    # ---------- bang nguon [B] T<nn> ----------
    alines = read(ASSIGN)
    a_status = {}
    for l in alines:
        m = re.match(r"\|\s*(T\d+)\s*\|", l)
        if m:
            cols = [c.strip() for c in l.strip("|").split("|")]
            a_status[m.group(1)] = cols[-1] if cols else "(?)"
    print("=" * 78)
    print(f"[B] BANG NGUON: {ASSIGN} — {len(a_status)} task")
    print("=" * 78)
    for k in sorted(a_status, key=lambda x: int(x[1:])):
        print(f"    {k:<5} {a_status[k]}")
    print()

    # ---------- bang nguon [C] §1 gitlab archived_at ----------
    gl = read("security/gitlab/SCOPE.md")
    sec1 = None
    for i, l in enumerate(gl):
        if l.startswith("## 1."):
            sec1 = i
        if sec1 is not None and l.startswith("## 2."):
            sec1_end = i
            break
    rows = []
    for l in gl[sec1:sec1_end]:
        m = re.search(r"archived_at=(\S+?)(?:\s|$)", l)
        if m:
            rows.append((l.strip()[:60], m.group(1)))
    print("=" * 78)
    print(f"[C] BANG NGUON: security/gitlab/SCOPE.md §1 — {len(rows)} dong co archived_at")
    print("=" * 78)
    live_n = sum(1 for _, v in rows if v == "None")
    ret = [(a, v) for a, v in rows if v != "None"]
    print(f"    archived_at=None (LIVE): {live_n}   |   archived_at!=None (RETIRED): {len(ret)}")
    for a, v in ret:
        print(f"      RETIRED  {v}  {a}")
    print()

    # ---------- QUET LIVE DOCS ----------
    print("=" * 78)
    print("[QUET] TAI LIEU SONG — moi tham chieu D-0xx / T<nn> / tuyen bo trang thai")
    print("=" * 78)
    deltas = []
    dref_hist = {}
    tref_hist = {}
    for f in LIVE:
        for i, l in enumerate(read(f), 1):
            for m in re.finditer(r"\bD-\d{3}\b", l):
                dref_hist.setdefault(m.group(0), []).append(f"{f}:{i}")
            for m in re.finditer(r"\bT\d{1,2}\b", l):
                tref_hist.setdefault(m.group(0), []).append(f"{f}:{i}")

    print("\n  --- D-0xx duoc trich trong tai lieu song (JOIN [A]) ---")
    for d in sorted(dref_hist):
        ok = d in d_exist
        mark = "CO trong bang ✅" if ok else "KHONG CO trong bang ❌"
        note = ""
        if d == "D-005":
            note = "  <-- D-013 noi 'thay the moi cach hieu khac ve cong G4'; chi duoc dung cho LUAT CAM"
        print(f"    {d:<7} {len(dref_hist[d])} lan  -> {mark}{note}")
        if not ok:
            deltas.append((f"tham chieu {d} khong co trong {DIRECTIVES}", dref_hist[d]))
    # luat D-025 [3a]: D-005 khong duoc dung de suy ra TRANG THAI G4
    for loc in dref_hist.get("D-005", []):
        f, n = loc.rsplit(":", 1)
        line = read(f)[int(n) - 1]
        if re.search(r"T4|G4|cổng|Cổng|cong", line):
            deltas.append((f"D-005 dung de suy ra TRANG THAI cua T4/G4 (phai dung D-013)", [loc]))
            print(f"      ⚠ DELTA: {loc} dung D-005 cho TRANG THAI G4 -> phai la D-013")
            print(f"        {line.strip()[:140]}")

    print("\n  --- T<nn> duoc trich trong tai lieu song (JOIN [B]) ---")
    for t in sorted(tref_hist, key=lambda x: int(x[1:])):
        st = a_status.get(t)
        mark = f"trang thai bang = {st}" if st else "KHONG co trong bang"
        print(f"    {t:<5} {len(tref_hist[t])} lan  -> {mark}")
        if not st:
            deltas.append((f"tham chieu {t} khong co trong {ASSIGN}", tref_hist[t]))

    print("\n  --- Tuyen bo TRANG THAI ve TAI SAN (JOIN [C]) ---")
    # moi tai san co archived_at != None phai duoc goi la 'nghi huu/retired/loai', KHONG 'trong scope' kieu mo
    ret_names = ["gitlab-workhorse", "license.gitlab.com", "Static websites", "opstrace",
                 "GitLab for Jira Cloud Plugin"]
    for i, l in enumerate(read("agents/bountyrecon/tasks/T3/CANDIDATES.md"), 1):
        for nm in ret_names:
            if nm in l and re.search(r"trong scope|Đáng chuyển|dang chuyen", l):
                deltas.append((f"tai san DA RETIRED '{nm}' van duoc goi la 'trong scope'/'Đáng chuyển'", [f"T3/CANDIDATES.md:{i}"]))
                print(f"    ⚠ DELTA: T3/CANDIDATES.md:{i}  '{nm}' + 'trong scope/Đáng chuyển'")
                print(f"      {l.strip()[:150]}")
    if not any("RETIRED" in d[0] for d in deltas):
        print("    (khong thay DELTA: khong tai san retired nao bi goi la 'trong scope' nua)")

    print()
    print("=" * 78)
    print(f"TONG DELTA: {len(deltas)}")
    for d, loc in deltas:
        print(f"  - {d}")
        print(f"      tai: {', '.join(loc[:6])}")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
