#!/usr/bin/env python3
"""insert_archived_blocks.py — T37 (BountyRecon) — D-026 [3b]

Chèn khối `[3b] CHIỀU archived_at` vào MỌI bảng AUTHORED (bảng do người viết),
ngay sau bảng tương ứng. KHÔNG sửa bảng CAPTURE nào trong EVIDENCE/**.

Chèn tại ANCHOR xác định (dòng đầu tiên khớp), idempotent: nếu khối đã có thì bỏ qua.
"""
import sys

MARK = "🧭 **[3b] CHIỀU `archived_at`"
STAMP = "2026-10-01T15:28Z"

STATS = {
    "gitlab": dict(name="GitLab", live=44, live_sub=19, arch=19, arch_sub=5, total=63,
                   v2="scope_gitlab_v2.md", orig="scope_gitlab.md",
                   orphans=[("gitlab-workhorse", "2021-12-28T13:36:15.653Z"),
                            ("license.gitlab.com", "2022-03-21T22:30:03.041Z"),
                            ("Static websites", "2022-07-21T16:00:50.221Z"),
                            ("opstrace/", "2023-06-04T21:02:31.693Z"),
                            ("GitLab for Jira Cloud Plugin", "2023-12-07T13:38:09.687Z")]),
    "github": dict(name="GitHub", live=39, live_sub=27, arch=158, arch_sub=156, total=197,
                   v2="scope_github_v2.md", orig="scope_github.md",
                   orphans=[("gist.github.com", "2017-06-22T23:23:44.719Z"),
                            ("http://GitHub.com/CSP", "2017-06-22T23:29:38.991Z"),
                            ("Atom", "2017-06-22T23:35:22.423Z"),
                            ("Other Applications", "2019-02-19T19:29:54.119Z"),
                            ("semmle.net / semmle.com / LGTM", "2022-08-31T18:46:1x–33xZ"),
                            ("jobs.github.com / lab.github.com", "2022-08-31T18:48–20:36Z"),
                            ("Copilot · Code Search · GitHub Enterprise Importer", "2022-09-13T02:27:1xZ"),
                            ("Codespaces", "2022-09-13T02:27:1x–19xZ"),
                            ("GHES", "2022-09-13T02:27:19.5–9xZ"),
                            ("All Other Scope (placeholder, ~150 dòng trùng)", "2022-09-13T02:27:19–21Z")]),
    "cloudflare": dict(name="Cloudflare", live=78, live_sub=51, arch=5, arch_sub=4, total=83,
                       v2="scope_cloudflare_v2.md", orig="scope_cloudflare.md",
                       orphans=[("http://cloudflare.com/apps/", "2023-03-01T17:47:43.944Z"),
                                ("dash.teams.cloudflare.com", "2023-05-08T10:11:33.083Z"),
                                ("Argo Tunnel", "2023-10-26T15:25:05.200Z"),
                                ("Durable Objects", "2023-10-26T15:40:54.533Z")]),
}


def block(prog):
    s = STATS[prog]
    out = [f"> {MARK} (D-026) — bảng này TRƯỚC ĐÂY THIẾU chiều này.**"]
    out.append(f"> Tự truy vấn lại `{STAMP}` (`archived:false` / `archived:true`, GraphQL công khai):")
    out.append(f"> **{s['name']}** — `archived:false` **{s['live']}** scope (sub=True **{s['live_sub']}**) · "
               f"`archived:true` **{s['arch']}** (sub=True **{s['arch_sub']}**) · TỔNG **{s['total']}**.")
    out.append(f"> **{s['arch_sub']} bản ghi `archived_at != None` MÀ VẪN `eligible_for_submission=true`** "
               f"(tạm gọi *orphan*) — bảng gốc không phân biệt được chúng với bản còn hiệu lực:")
    for nm, dt in s["orphans"]:
        out.append(f">   - `{nm}` — `{dt}`")
    out.append(f"> Bản chụp lại **có cột `archived_at`** đầy đủ: "
               f"`agents/bountyrecon/tasks/T3/EVIDENCE/{s['v2']}` (bản gốc "
               f"`{s['orig']}` **giữ nguyên**, không sửa/xoá — D-026 (a)).")
    out.append(">")
    out.append("> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** **KHÔNG** suy ra *\"ngoài scope\"* cho các bản ghi này.")
    out.append("> Chỉ được khẳng định: bảng **THIẾU chiều `archived_at`** ⇒ **KHÔNG PHÂN BIỆT ĐƯỢC**"
               " bản ghi còn hiệu lực hay đã nghỉ hưu.")
    out.append("> Việc **loại khỏi T4** chỉ áp cho **4 tài sản GitLab** đã có phán quyết (`D-021`).")
    out.append(">")
    out.append("> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên một bản ghi "
               "`archived_at != None` **CHƯA có định nghĩa chính thức** (introspection `description` RỖNG;")
    out.append("> tài liệu công khai không có). **Ghi hiện tượng, KHÔNG kết luận ngữ nghĩa.**")
    out.append("")
    return "\n".join(out)


# (file, prog, anchor-regex mở đầu dòng để chèn TRƯỚC)
JOBS = [
    ("security/gitlab/SCOPE.md", "gitlab", "Prose out-of-scope (không nằm trong bảng structured)"),
    ("security/github/SCOPE.md", "github", "> 📝 **Quan sát của tôi (KHÔNG phải nguyên văn):**"),
    ("security/cloudflare/SCOPE.md", "cloudflare", "### 1b. Sản phẩm / dịch vụ trong scope"),
    ("security/gitlab/RECON.md", "gitlab", "### 1.1 DMARC (nguyên văn)"),
    ("security/github/RECON.md", "github", "### 1.1 CAA (ai được phép phát hành chứng chỉ)"),
    ("security/cloudflare/RECON.md", "cloudflare", "### 1.1 TXT đáng chú ý (nguyên văn)"),
]


def main():
    for path, prog, anchor in JOBS:
        lines = open(path, encoding="utf-8").read().splitlines()
        if any(MARK in l for l in lines):
            print(f"  {path}: da co khoi [3b] -> bo qua")
            continue
        idx = next((i for i, l in enumerate(lines) if l.startswith(anchor)), None)
        if idx is None:
            print(f"  {path}: KHONG tim thay anchor {anchor!r} -> BO QUA")
            continue
        new = lines[:idx] + block(prog).splitlines() + lines[idx:]
        open(path, "w", encoding="utf-8").write("\n".join(new) + "\n")
        print(f"  {path}: chen khoi [3b] tai dong {idx+1} (prog={prog})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
