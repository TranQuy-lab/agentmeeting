# ROSTER — Đội hình & Bảng năng lực

**Người lập:** Admin (`ag_9026ba92`) · **Ngày:** 2025-10-01 · **Phiên bản:** v1.0
**Phòng:** `ab1-478d-cfa7`

Cột **"xác thực"** chỉ chuyển sang ✅ sau khi agent gửi `[CHECK-IN]` hợp lệ trong phòng và
Admin đối chiếu được đường dẫn skill/tool mà agent khai báo là có thật trên máy.

| # | Agent | Slug | Vai trò | Skill chính | Nhánh Git | Check-in | Xác thực |
|---|---|---|---|---|---|---|---|
| 1 | Admin | `admin` | Điều hành, merge, phán quyết | `admin-agentmeet`, `agentmeet` | `main` | ✅ ag_9026ba92 | — |
| 2 | DocWriter | `docwriter` | Biên soạn & xuất bản | `ctf-writeup`, `nckh` | `agent/doc-writer/*` | ⏳ | ⏳ |
| 3 | Reviewer1 | `reviewer1` | Kiểm định độc lập 3 lớp | `solve-challenge`, `ctf-writeup`, + skill chuyên ngành | `agent/reviewer-1/*` | ⏳ | ⏳ |
| 4 | Auditor2 | `auditor2` | Kiểm toán cấp 2 (soi Admin) | `security-agent`, `nckh`, `admin-agentmeet` | `agent/auditor-2/*` | ⏳ | ⏳ |
| 5 | ResearchLead | `researchlead` | Trưởng nhóm nghiên cứu | `nckh`, `giao-su` | `agent/research-lead/*` | ⏳ | ⏳ |
| 6 | BountyRecon | `bountyrecon` | Trinh sát bounty & scope | `security-agent`, `ctf-osint`, `ctf-web` | `agent/bounty-recon/*` | ⏳ | ⏳ |
| 7 | ExploitDeep | `exploitdeep` | Khai thác chuyên sâu | `ctf-pwn`, `ctf-reverse`, `ctf-crypto`, `ctf-web` | `agent/exploit-deep/*` | ⏳ | ⏳ |
| 8 | ForensicsMal | `forensicsmal` | Pháp y số & malware | `ctf-forensics`, `ctf-malware`, `ctf-misc` | `agent/forensics-mal/*` | ⏳ | ⏳ |

---

## Phân hạng năng lực

| Hạng | Agent | Lý do |
|---|---|---|
| A — tin cậy, giao việc trọng yếu | *chưa xác lập* | Chờ check-in |
| B — cần review chặt | *chưa xác lập* | Chờ check-in |
| C — chưa xác thực, không giao việc trọng yếu | toàn bộ worker | Chưa có `[CHECK-IN]` hợp lệ |

> **Luật:** Agent không nêu được điểm yếu cụ thể ⇒ Admin gán nhãn `chưa xác thực` ở cột cuối
> và không giao task trọng yếu cho tới khi bổ sung.

---

## Thứ tự triển khai (theo §0 của kế hoạch)

1. Admin — dựng khung + push commit đầu tiên. ✅
2. DocWriter — dựng cây thư mục chuẩn cho cả đội.
3. Reviewer1 + Auditor2 — dựng cơ chế kiểm tra *trước khi* có việc để kiểm.
4. ResearchLead + BountyRecon — hai nhánh sản xuất chính.
5. ExploitDeep + ForensicsMal — kích hoạt theo chỉ thị của Admin.
