# Kho làm việc đội AgentMeet — phòng `ab1-478d-cfa7`

**Chủ sở hữu:** Admin (`ag_cd389846`; danh tính cũ `ag_9026ba92` đã bị `kicked` — xem `ADMIN/LOG.md` #5) — điều hành theo uỷ quyền của người dùng.
**Repo:** `git@github.com:TranQuy-lab/agentmeeting.git` (SSH — HTTPS đang hỏng credential helper).
**Ngày khởi tạo khung:** 2026-10-01 (commit đầu tiên do Admin).

---

## Mục tiêu phiên

Thành lập đội đa agent để (1) truy tìm đề tài nghiên cứu khoa học về mạng / an ninh mạng /
thiết kế hệ thống, và (2) săn lỗ hổng trong các chương trình bug bounty **công khai có scope**.
Mọi kết quả phải qua kiểm chứng chéo → đối chiếu → kiểm tra mù trước khi nghiệm thu.

---

## Cây thư mục

| Đường dẫn | Mục đích | Ai được ghi |
|---|---|---|
| `ADMIN/` | Hồ sơ điều hành: roster, phân công, log quyết định, bất đồng, tổng kết | Chỉ Admin |
| `agents/<slug>/tasks/<task_id>/` | Artifact riêng của từng agent | Chính agent đó |
| `research/<topic_slug>/` | Hồ sơ đề tài NCKH | ResearchLead, ForensicsMal (FORENSICS.md) |
| `security/<program_slug>/<finding_id>/` | Hồ sơ lỗ hổng theo chương trình | BountyRecon, ExploitDeep, ForensicsMal |
| `reviews/` | Ba lớp kiểm định độc lập | Reviewer1, Auditor2 |
| `rooms/ab1-478d-cfa7/` | Dữ liệu thô + digest của phòng họp | DocWriter, Admin |

---

## Thứ tự đọc kho

1. [`ADMIN/ROSTER.md`](ADMIN/ROSTER.md) — đội hình và năng lực đã khai báo.
2. [`ADMIN/ASSIGNMENTS.md`](ADMIN/ASSIGNMENTS.md) — ai làm gì, territory nào, ai review.
3. [`ADMIN/LOG.md`](ADMIN/LOG.md) — nhật ký quyết định của Admin kèm lý do.
4. [`INDEX.md`](INDEX.md) — mục lục toàn kho: đường dẫn · tác giả · trạng thái · reviewer.
5. [`reviews/CROSS.md`](reviews/CROSS.md) — kiểm chứng chéo lớp 1.

---

## Luật bất biến của kho này

1. **CẤM BỊA.** URL, DOI, CVE, số liệu, output lệnh, tên bài báo — không chắc thì ghi `chưa xác minh`.
2. **Mỗi khẳng định kỹ thuật phải trỏ tới bằng chứng thô trong repo** (đường dẫn tương đối).
3. **Người viết KHÔNG BAO GIỜ tự verify việc mình làm.** Reviewer1 làm. Không ngoại lệ.
4. **CẤM push** token, credential, API key, dữ liệu cá nhân thật, mẫu malware, dump khai thác.
5. **CẤM merge vào `main`** — chỉ Admin được merge. Mọi agent push nhánh riêng `agent/<slug>/<task_id>`.
6. **Hoạt động an ninh chỉ trong scope công khai đã trích nguyên văn.** Ngoài scope = dừng, báo Admin.

---

## Trạng thái cổng duyệt (gate)

| Cổng | Điều kiện | Trạng thái |
|---|---|---|
| G0 — Khung repo | Admin push commit đầu tiên | ✅ |
| G1 — Cơ chế kiểm định | Reviewer1 + Auditor2 vào phòng | ⏳ |
| G2 — Nhánh nghiên cứu | ResearchLead có ≥1 PROPOSAL.md | ⏳ |
| G3 — Nhánh bounty | BountyRecon có SCOPE.md trích nguyên văn | ⏳ |
| G4 — Khai thác sâu | G3 **và** chỉ thị Admin nêu `target` + `finding_id` (bản ghi uỷ quyền, ban hành ngay khi G3 đạt — xem D-013) | ⛔ CHƯA MỞ (chưa có `SCOPE.md`) |
