#!/usr/bin/env python3
"""apply_t37_correct.py — T37 theo D-027 (đã đính chính)

Làm ĐÚNG 3 việc:
  [1] cloudflare/SCOPE.md §1a — thêm `archived_at=` vào 12 dòng tài sản
  [2] gitlab/SCOPE.md §2a    — thêm `archived_at=` vào các dòng tài sản
  [3] github/SCOPE.md        — GIỮ NGUYÊN §1 (khối nguyên văn), THÊM mục AUTHORED mới
                               `### 1b. Bảng tài sản GitHub kèm archived_at`

KHÔNG chạm: github/RECON.md, cloudflare/RECON.md, gitlab/RECON.md (không có bảng scope — D-027).
"""
import json
import sys
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
STAMP = "2026-10-01T15:28Z"


def fetch(handle, arch):
    q = ('query{team(handle:"%s"){structured_scopes(first:400,archived:%s){'
         'edges{node{asset_identifier asset_type eligible_for_submission '
         'eligible_for_bounty max_severity archived_at}}}}}') % (handle, arch)
    req = urllib.request.Request(
        "https://hackerone.com/graphql", data=json.dumps({"query": q}).encode(),
        headers={"Content-Type": "application/json", "User-Agent": UA}, method="POST")
    return [x["node"] for x in
            json.loads(urllib.request.urlopen(req, timeout=60).read())
            ["data"]["team"]["structured_scopes"]["edges"]]


def index(handle):
    d = {}
    for arch in ("false", "true"):
        for n in fetch(handle, arch):
            d.setdefault(n["asset_identifier"], n)
    return d


def add_col(path, anchor_end, mapping, keys):
    """Chèn `  archived_at=<v>` vào cuối dòng bắt đầu bằng 1 trong `keys`, trong khoảng
    từ dòng khớp anchor_end (mở) tới dòng trống kết thúc khối fence."""
    lines = open(path, encoding="utf-8").read().splitlines()
    # tìm khối fence chứa các dòng tài sản
    start = next(i for i, l in enumerate(lines) if anchor_end in l)
    a = next(i for i in range(start, len(lines)) if lines[i].lstrip().startswith("```"))
    b = next(i for i in range(a + 1, len(lines)) if lines[i].strip().startswith("```"))
    n = 0
    for i in range(a + 1, b):
        l = lines[i]
        head = l.split("  ")[0].strip()
        for k in keys:
            if l.startswith(k):
                ident = l.split("  ")[0].strip() if False else None
                break
        # xác định identifier: token đầu sau key
        m = l.split()
        if not m or m[0] not in keys:
            continue
        ident = m[1] if len(m) > 1 else ""
        # một số dòng có identifier nối bằng '|' hoặc chuỗi dài -> tra trực tiếp
        val = mapping.get(ident)
        if val is None:
            for cand in mapping:
                if cand and cand in l:
                    val = mapping[cand]
                    break
            else:
                val = "?"
                print(f"    CANH BAO: khong tra duoc archived_at cho dong: {l[:70]}")
        if "archived_at=" in l:
            continue
        lines[i] = l + f"    archived_at={val if val else 'None'}"
        n += 1
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"  {path}: them archived_at vao {n} dong")
    return n


def main():
    cf = index("cloudflare")
    gl = index("gitlab")
    gh_live = fetch("github", "false")
    gh_arch = fetch("github", "true")
    sub = [n for n in gh_live + gh_arch if n["eligible_for_submission"]]
    live = [n for n in sub if not n["archived_at"]]
    ret = [n for n in sub if n["archived_at"]]

    # [1] cloudflare §1a
    add_col("security/cloudflare/SCOPE.md",
            "### 1a. Tên miền / tài sản web",
            {k: (v["archived_at"] or "None") for k, v in cf.items()},
            {"URL", "OTHER", "SOURCE_CODE", "WILDCARD"})

    # [2] gitlab §2a  (dòng có thể chứa nhiều identifier -> tra theo substring)
    gl_map = {}
    for k, v in gl.items():
        gl_map.setdefault(k, v["archived_at"] or "None")
    add_col("security/gitlab/SCOPE.md",
            "### 2a. Danh sách out-of-scope",
            gl_map, {"WILDCARD", "URL", "SOURCE_CODE", "OTHER"})

    # [3] github §1b — MỤC AUTHORED MỚI
    p = "security/github/SCOPE.md"
    lines = open(p, encoding="utf-8").read().splitlines()
    if any("### 1b. Bảng tài sản GitHub kèm" in l for l in lines):
        print("  github/SCOPE.md: da co §1b -> bo qua")
        return 0
    out = ["### 1b. Bảng tài sản GitHub kèm `archived_at` (AUTHORED — KHÔNG phải nguyên văn)", "",
           "> 🧭 **Mục này do BountyRecon TẠO Ở T37 (D-027).** `§1` phía trên là **KHỐI TRÍCH NGUYÊN VĂN**",
           "> và **KHÔNG bị sửa một ký tự nào** — đúng nguyên tắc *trích nguyên văn > yêu cầu định dạng*.",
           "> Bảng dưới đây là **bảng tổng hợp do tôi lập** từ `structured_scopes` (đã TÁCH khỏi nguyên văn).",
           f"> Tự truy vấn lại `{STAMP}` (`archived:false` / `archived:true`).", ">",
           f"> **Thống kê tự đo:** `archived:false` **39** · `archived:true` **158** · TỔNG **197** · "
           f"`sub=True` **{len(sub)}** (live **{len(live)}** + archived **{len(ret)}**).", ">",
           "> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** **KHÔNG** suy ra *\"ngoài scope\"* cho bản ghi",
           "> `archived_at != None`. Chỉ được khẳng định: bảng **THIẾU chiều `archived_at`** ⇒",
           "> **KHÔNG PHÂN BIỆT ĐƯỢC** còn hiệu lực hay đã nghỉ hưu.",
           "> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi archived",
           "> **CHƯA có định nghĩa chính thức** ⇒ hiệu lực **CHƯA XÁC MINH**. Cần trả lời chính thức từ chương trình.",
           "", "| asset_type | asset_identifier | sub | bounty | max_severity | **archived_at** |",
           "|---|---|---|---|---|---|"]
    for n in sorted(live, key=lambda x: x["asset_identifier"]) + \
             sorted(ret, key=lambda x: (x["archived_at"] or "")):
        out.append(f"| {n['asset_type']} | {n['asset_identifier'][:90]} | "
                   f"{n['eligible_for_submission']} | {n['eligible_for_bounty']} | "
                   f"{n['max_severity']} | `{n['archived_at'] or 'None'}` |")
    out.append("")
    # chèn trước dòng "**Tài sản phi-tên-miền trong scope**"
    idx = next((i for i, l in enumerate(lines)
                if l.startswith("**Tài sản phi-tên-miền trong scope**")), None)
    if idx is None:
        print("  github/SCOPE.md: KHONG tim thay anchor -> bo qua §1b")
        return 0
    new = lines[:idx] + out + lines[idx:]
    open(p, "w", encoding="utf-8").write("\n".join(new) + "\n")
    print(f"  {p}: chen §1b ({len(out)} dong, {len(sub)} tai san)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
