#!/usr/bin/env python3
"""gen_v2_captures.py — T37 (BountyRecon) — D-026 phương án (a)

CHỤP LẠI 4 bảng CAPTURE thành `<tên>_v2.md` CÓ kèm cột `archived_at`.
BẢN GỐC `scope_<prog>.md` KHÔNG bị sửa, KHÔNG bị xoá (bằng chứng pháp lý).

Vì sao `_v2` là bảng MÁY sinh (khác bản gốc): bản gốc T3 cũng là bảng máy sinh nhưng
THIẾU chiều `archived_at`. Bản `_v2` bổ sung đúng chiều đó, giữ nguyên mọi trường cũ.

Chỉ ĐỌC mạng (GraphQL công khai), chỉ GHI file mới `_v2`.
"""
import datetime
import json
import os
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
OUTDIR = "agents/bountyrecon/tasks/T3/EVIDENCE"
Q = """query{team(handle:"%s"){name handle offers_bounties
 structured_scopes(first:400,archived:%s){
  edges{node{asset_identifier asset_type eligible_for_submission eligible_for_bounty
             max_severity archived_at instruction}}}}}"""


def gq(handle, arch):
    body = json.dumps({"query": Q % (handle, arch)}).encode()
    req = urllib.request.Request(
        "https://hackerone.com/graphql", data=body,
        headers={"Content-Type": "application/json", "User-Agent": UA}, method="POST")
    d = json.loads(urllib.request.urlopen(req, timeout=60).read())
    if "data" not in d or d.get("data", {}).get("team") is None:
        raise SystemExit(f"GraphQL loi cho handle={handle} arch={arch}: {json.dumps(d)[:400]}")
    t = d["data"]["team"]
    return t, [x["node"] for x in t["structured_scopes"]["edges"]]


def esc(s):
    return (s or "").replace("\n", " ").replace("|", "\\|")[:400]


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    for handle, slug in (("github", "github"), ("cloudflare", "cloudflare"),
                         ("gitlab", "gitlab"), ("security", "security")):
        t, live = gq(handle, "false")
        _, arch = gq(handle, "true")
        path = os.path.join(OUTDIR, f"scope_{slug}_v2.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# STRUCTURED SCOPE v2 (có `archived_at`) — {t['name']} "
                    f"(handle `{t['handle']}`)\n\n")
            f.write(f"**Ngày chụp:** `{stamp}` (UTC) · **Nguồn:** "
                    f"`POST https://hackerone.com/graphql` (công khai, không auth)\n")
            f.write("**Quan hệ với bản gốc:** đây là **BẢN CHỤP LẠI** theo `D-026` phương án (a).\n")
            f.write(f"Bản gốc `scope_{slug}.md` **KHÔNG bị sửa, KHÔNG bị xoá** — vẫn là bằng chứng "
                    f"pháp lý cho thời điểm chụp gốc `2026-10-01`.\n\n")
            f.write("> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** cột `archived_at` cho biết bản ghi "
                    "**đã nghỉ hưu hay chưa**. **KHÔNG** được suy ra 'ngoài scope'. "
                    "Chỉ được khẳng định: bảng thiếu chiều này thì **KHÔNG PHÂN BIỆT ĐƯỢC**.\n")
            f.write("> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi "
                    "`archived_at != None` **chưa có định nghĩa chính thức**. Ghi hiện tượng, "
                    "KHÔNG kết luận ngữ nghĩa.\n\n")
            sub_live = [n for n in live if n["eligible_for_submission"]]
            sub_arch = [n for n in arch if n["eligible_for_submission"]]
            f.write(f"**Thống kê tự đo:** `archived:false` = **{len(live)}** scope "
                    f"(sub=True **{len(sub_live)}**) · `archived:true` = **{len(arch)}** scope "
                    f"(sub=True **{len(sub_arch)}**) · TỔNG **{len(live)+len(arch)}**\n\n")
            for label, rows, arch_flag in (("archived=false (đang hiệu lực)", live, False),
                                           ("archived=true (đã nghỉ hưu)", arch, True)):
                f.write(f"## {label} — n={len(rows)}\n\n")
                f.write("| asset_type | asset_identifier | eligible_submission | eligible_bounty "
                        "| max_severity | **archived_at** | instruction |\n")
                f.write("|---|---|---|---|---|---|---|\n")
                for n in rows:
                    f.write(f"| {n['asset_type']} | {esc(n['asset_identifier'])} "
                            f"| {n['eligible_for_submission']} | {n['eligible_for_bounty']} "
                            f"| {n['max_severity']} | `{n['archived_at'] or 'None'}` "
                            f"| {esc(n['instruction'])} |\n")
                f.write("\n")
        print(f"  ghi {path}: live={len(live)} arch={len(arch)} "
              f"orphan(arch&sub)={len(sub_arch)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
