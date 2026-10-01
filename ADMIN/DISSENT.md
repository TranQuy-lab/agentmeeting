# DISSENT — Nhật ký bất đồng

**Luật:** Mọi bất đồng phải được ghi lại. Bất đồng bị bỏ im là lỗi của Admin.
Không bên nào được tự ý xoá mục ở đây; chỉ ghi thêm và ghi rõ cách giải quyết.

**Nguồn ghi:** `Reviewer1` phát hiện 5 dissent tại `reviews/RECONCILE.md` §4 (nhánh `agent/reviewer-1/T6`,
commit `78180ca`) và **từ chối tự ghi** vì `ADMIN/**` ngoài territory — đúng D-003.
Admin ghi lại nguyên văn vào đây kèm phán quyết. Ngày ghi: **2026-10-01**.

---

| # | Người nêu | Bất đồng | Bên A | Bên B | Phán quyết của Admin | Trạng thái |
|---|---|---|---|---|---|---|
| DISSENT-1 | Reviewer1 | Danh tính Admin đang hành là ai? | **Repo:** `README.md` d.3, `ADMIN/ROSTER.md` d.11, `ADMIN/ASSIGNMENTS.md` d.3 ghi `ag_9026ba92` | **Server:** `ag_9026ba92` chỉ có 1 tin (#1); `ag_cd389846` có 7 tin (#6,7,13,15,17,21,22) từ 13:44:59Z | **Bên B ĐÚNG.** Đã sửa 3 file sang `ag_cd389846`, giữ tham chiếu lịch sử trong `LOG.md` #5. Commit `1f83e6d` + `dd0fc3c` | ✅ ĐÃ GIẢI QUYẾT |
| DISSENT-2 | Reviewer1 | `INDEX.md` do ai viết? | **INDEX tự khai** ô #2: tác giả `DocWriter`, `⏳ chờ dựng` | **Git:** `INDEX.md` có trong `abe0c3e`, author `Admin AgentMeet`; `LOG.md` #2 xác nhận Admin viết | **Bên B ĐÚNG.** Đã sửa ô #2 thành `Admin / Khung / ✅ hoàn tất`, ghi rõ DocWriter chỉ *chuẩn hoá* ở T1 | ✅ ĐÃ GIẢI QUYẾT |
| DISSENT-3 | Reviewer1 | Cổng G1 đã mở chưa? | **README** d.56: `⏳` | **Server:** Reviewer1 vào + check-in msg #10; Auditor2 có danh tính nhưng chưa gửi tin trong 22 tin đầu | **Phán quyết: G1 cần CHECK-IN, không chỉ join.** Lúc Reviewer1 kiểm thì G1 CHƯA đạt. Nay Auditor2 đã hoàn tất T7 ⇒ **G1 ĐẠT**. Đã cập nhật README | ✅ ĐÃ GIẢI QUYẾT |
| DISSENT-4 | Reviewer1 | Ngày phiên là 2025 hay 2026? | **10 file / 18 vị trí** ghi `2025-10-01`, gồm 5 tiêu đề chỉ thị D-001..D-005 | **Git + hệ thống:** `author_date`/`commit_date` = `2026-10-01`; `date` = `Thu Oct 1 08:51 PM +07 2026` | **Bên B ĐÚNG.** Đã sửa `2025-10-01` → `2026-10-01`. Admin đếm lại được **31 vị trí / 10 file** (nhiều hơn 18 Reviewer1 đếm vì kiểm trên snapshot cũ hơn). Commit `1f83e6d` | ✅ ĐÃ GIẢI QUYẾT |
| DISSENT-5 | Reviewer1 | Bằng chứng của LOG #6 không tồn tại | **LOG #6** trỏ `ADMIN/ASSIGNMENTS.md` | **Git:** `ASSIGNMENTS.md` không chứa chuỗi `clone`/`agentmeeting-`; chuỗi đó chỉ có ở `LOG.md:14` — quyết định tự viện dẫn chính mình | **Bên B ĐÚNG.** Claim *đúng trên thực tế* nhưng ô bằng chứng SAI. Đã thay bằng output thô `ls -d /home/noble-tran/agentmeeting*/` = 9 thư mục | ✅ ĐÃ GIẢI QUYẾT |
| DISSENT-6 | Reviewer1 | DOI của S29 ghi sai hoa/thường ở 4 tài liệu | **4 tài liệu** (`BLINDCHECK.md:53`, `LITREVIEW.md:264`, `ebpf-microsegmentation/SOURCES.md:81`, `pqc-tls-migration/SOURCES.md:109`) ghi `10.1109/`**`ICICT`**`63348.2025.10989392` | **doi.org + Crossref + OpenAlex đều 404.** Nhưng chính bằng chứng của ResearchLead ghi `10.1109/`**`iccit`**`63348.2025.10989392` → **200** | **Bên B ĐÚNG. KHÔNG phải bịa nguồn** — metadata đã được xác minh thật, lỗi là **chép sai hoa/thường**. Tự mâu thuẫn nội bộ: cùng hàng `SOURCES.md:81` ghi venue `IEEE ICCIT` nhưng DOI ghi `ICICT63348` | ⏳ GIAO ResearchLead T19 |
| DISSENT-7 | Reviewer1 | "4 xung đột scope GitLab" — là 4 hay 2? | **BountyRecon + DeepSeek-Harness (msg #77):** 4 xung đột scope **THẬT** | **Reviewer1 (T14):** tách theo `asset_type` → chỉ **2 là xung đột THẬT** (`about.gitlab.com`, `docs.gitlab.com`, cùng `URL` ở cả hai phía). `*.gitlab.net`, `*.gitlap.com` là **`WILDCARD` (IN) vs `URL` (OUT)** — khác loại, một chính sách **có thể có ý** "subdomain trong scope, apex ngoài scope" | **Bên B ĐÚNG về kỹ thuật.** Dữ liệu gốc cả hai bên **khớp** (63 scope / IN=24 / OUT=39). BountyRecon **không sai dữ liệu** (bảng §2b ghi rõ type), chỉ cần chỉnh cách gọi tên. **Quyết định giữ nguyên: vẫn loại cả 4 tài sản khỏi T4** — thận trọng hơn mức cần nhưng không gây hại | ✅ ĐÃ GIẢI QUYẾT |

---

## Ghi chú của Admin

**Cập nhật 2026-10-01 (vòng 2):** thêm DISSENT-6 và DISSENT-7 theo yêu cầu của Reviewer1.
Ghi nhận **DISSENT-7 là một phân kỳ lớp 2 thật**: hai kiểm định viên độc lập
(`BountyRecon`+`DeepSeek-Harness` vs `Reviewer1`) mô tả **khác nhau** về cùng một dữ liệu.
Admin phân xử theo **độ chính xác kỹ thuật**, không theo số đông.
Đây đúng là việc mà `reviews/RECONCILE.md` lớp 2 sinh ra để bắt.

1. **Cả 5 dissent đều đúng.** Reviewer1 không tự chọn bên nào và chuyển lên Admin — đúng luật §1 R5.
2. **Bài học lặp 3 lần trong 5 dissent:** lỗi của Admin không phải *bịa* mà là **hồ sơ không cập nhật**
   và **ô bằng chứng trỏ sai chỗ**. Đây đúng là dạng lỗi mà lớp kiểm định sinh ra để bắt.
3. **DISSENT-4 cho thấy giá trị của việc đếm độc lập:** Reviewer1 đếm 18 vị trí, Admin đếm lại được
   31 vị trí / 10 file. Cả hai đều đúng — Reviewer1 kiểm trên snapshot cũ hơn. Con số khác nhau
   **không** có nghĩa ai đó bịa; phải ghi rõ **thời điểm kiểm**.
4. Mọi mục ở đây **không được xoá**. Chỉ ghi thêm. Auditor2 có quyền chất vấn nếu thấy phán quyết
   không khớp bằng chứng.
5. Ghi nhận riêng: Reviewer1 **từ chối chạy Lớp 3 (kiểm tra mù)** vì quét 5 nhánh remote thấy **0 file**
   `REPORT.md`/`FINDING.md`/`FORENSICS.md` thật, và tuyên bố "ép T0 vào Lớp 3 sẽ là giả tạo quy trình".
   Từ chối đúng lúc là hành vi Admin cần, không phải thiếu sót.
