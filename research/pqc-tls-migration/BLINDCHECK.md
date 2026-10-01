# BLINDCHECK — Phiếu kiểm định mù (Đề tài `RL-T1-PQC-TLS`)

> ## ⚠️ QUY TẮC SỬ DỤNG
> File này **để TRỐNG phần kết quả**. Chỉ **Reviewer1** được điền.
> **ResearchLead (`ag_d85dde8d`) — tác giả — KHÔNG được điền bất kỳ ô kết luận nào.**
> Mọi ô kết luận hiện đang là `⛔ CHƯA ĐIỀN`. Nếu thấy ô nào đã có nội dung do tác giả viết,
> hãy coi đó là **vi phạm quy trình** và báo Admin.

| Trường | Giá trị |
|---|---|
| Đề tài | `RL-T1-PQC-TLS` — Di trú PQC cho TLS 1.3 tại hạ tầng biên |
| Tác giả hồ sơ | ResearchLead (`ag_d85dde8d`) |
| Nhánh | `agent/research-lead/T2` |
| Ngày tạo phiếu | 2026-10-01 |
| **Người kiểm định** | ⛔ CHƯA ĐIỀN |
| **Ngày kiểm định** | ⛔ CHƯA ĐIỀN |
| **Commit hash được kiểm** | ⛔ CHƯA ĐIỀN |

---

## PHẦN A — KHAI BÁO CỦA TÁC GIẢ (tác giả điền — phần này hợp lệ)

Tác giả khai báo trước những điểm mà bản thân **biết là yếu**, để Reviewer1 tập trung soi:

| # | Điểm yếu tác giả tự khai | Vị trí trong hồ sơ |
|---|---|---|
| A1 | Khẳng định "chưa có mô hình quyết định ưu tiên di trú nào tồn tại" dựa trên **không tìm thấy**, không phải tìm kiếm có hệ thống | `PROPOSAL.md` §1.3; `LITREVIEW.md` §6.4 |
| A2 | Chỉ **6/29 nguồn** đọc được toàn văn; phần còn lại chỉ ở mức metadata | `SOURCES.md` §A–§C |
| A3 | **Không có sơ đồ PRISMA**, không khử trùng lặp hai người → tài liệu này KHÔNG phải systematic review | `LITREVIEW.md` §4, §9 |
| A4 | Hai truy vấn tìm kiếm (Q5, Q6) **thất bại** do lỗi cú pháp của tác giả | `LITREVIEW.md` §3 |
| A5 | Một URL tác giả **tự suy đoán sai** (`cic.iacr.org/p/1/3/22`) đã bị loại | `SOURCES.md` §D mục X5 |
| A6 | **Không có thực nghiệm nào được chạy.** Toàn bộ §3 của PROPOSAL là thiết kế | `PROPOSAL.md` §10 |
| A7 | Chi phí tiền tệ để ở mức `chưa xác minh` — tác giả cố ý không quy đổi | `PROPOSAL.md` §8 |
| A8 | Tính mới là tính mới của **tổ hợp**, không phải của từng mảnh | `LITREVIEW.md` §7 mẫu hình 4 |

---

## PHẦN B — KẾT QUẢ KIỂM ĐỊNH (CHỈ REVIEWER1 ĐIỀN)

### B1. Kiểm tra tính xác thực của nguồn (bắt buộc)

| # | Việc phải làm | Reviewer1 ghi kết quả thô (lệnh + output) | Kết luận PASS/FAIL |
|---|---|---|---|
| B1.1 | Chạy lại `curl -s https://api.crossref.org/works/10.6028/NIST.FIPS.203` — DOI có tồn tại? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.2 | Tải lại `https://www.ndss-symposium.org/wp-content/uploads/2020/02/24203-paper.pdf` — có tải được không? Kích thước bao nhiêu byte? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.3 | Chạy `pdftotext -layout` trên PDF đó. **Dòng 622, 667, 673, 678 có khớp nguyên văn** với `../EVIDENCE/quote_extracts.txt` mục A không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.4 | Tải `https://lirias.kuleuven.be/retrieve/14e501bd-e6bb-41d6-bf72-360c4850443a`. Trích xuất. **Dòng 46–48 có chứa câu "negligible performance overhead"** như đã trích không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.5 | Tải RFC 8446 và RFC 9370 từ `rfc-editor.org`. Kích thước có khớp 337.736 và 81.487 bytes? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.6 | Kiểm 5 mục ở `SOURCES.md` §D (X1–X5): các mục đó có **thực sự không xác minh được** không, hay tác giả đã bỏ sót nguồn xác minh được? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B2. Kiểm tra tính mới (bắt buộc — đây là chỗ dễ sai nhất)

| # | Việc phải làm | Reviewer1 ghi kết quả thô | Kết luận |
|---|---|---|---|
| B2.1 | Tự chạy một tìm kiếm **độc lập** (khác truy vấn của tác giả) cho: *hybrid ML-KEM TLS 1.3 measurement edge MTU middlebox dataset* | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.2 | Tự chạy một tìm kiếm độc lập cho: *post-quantum migration priority model traffic class HNDL* — **có tồn tại mô hình tương tự không?** | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.3 | Kiểm tra S7 (khảo sát PQC TLS, Alnahawi et al.) — **tìm cách đọc được toàn văn**. Trong đó có mô hình ưu tiên di trú không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.4 | Nếu B2.2 hoặc B2.3 tìm ra công trình trùng ý tưởng → **tính mới phải bị hạ cấp**. Ghi rõ mức hạ cấp. | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B3. Kiểm tra phương pháp

| # | Việc phải làm | Kết quả | Kết luận |
|---|---|---|---|
| B3.1 | §3 P2 có mô tả đủ để **người khác chạy lại** không? Thiếu gì? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.2 | Cách chọn cỡ mẫu có hợp lệ không? Có nên bắt buộc tính `statistical-power` trước? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.3 | Chọn kiểm định thống kê (Mann–Whitney U, bootstrap CI) có phù hợp với dữ liệu độ trễ không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.4 | Có **tự mâu thuẫn** giữa các phần không? (PROPOSAL ↔ LITREVIEW ↔ SOURCES) | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B4. Kiểm tra đạo đức & an toàn

| # | Việc phải làm | Kết quả | Kết luận |
|---|---|---|---|
| B4.1 | §3 P2 có nêu rõ **chỉ chạy trên testbed có uỷ quyền** không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B4.2 | Có nguy cơ dữ liệu cá nhân/thật bị đưa vào repo không (§4 D5)? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B4.3 | Có token/credential nào bị lộ trong nhánh này không? (kiểm `git log -p` và mọi file) | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B4.4 | §6 R6 (rủi ro kết quả bị dùng để biện minh trì hoãn di trú) đã được xử lý thoả đáng chưa? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B5. Kiểm tra tuân thủ luật phòng

| # | Việc phải làm | Kết quả | Kết luận |
|---|---|---|---|
| B5.1 | Mọi file trong nhánh có nằm trong territory `research/**` hoặc `agents/researchlead/**`? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B5.2 | Tác giả có **tự verify** việc mình làm ở bất kỳ đâu không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B5.3 | Có file nào tên `FORENSICS.md` bị tạo nhầm (đụng territory T5) không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

---

## PHẦN C — TỔNG KẾT CỦA REVIEWER1

| Trường | Giá trị |
|---|---|
| **Kết quả tổng thể** | ⛔ CHƯA ĐIỀN — `PASS` / `PASS CÓ ĐIỀU KIỆN` / `FAIL` |
| **Số lỗi mức nghiêm trọng (blocker)** | ⛔ CHƯA ĐIỀN |
| **Số lỗi mức trung bình** | ⛔ CHƯA ĐIỀN |
| **Số lỗi mức nhỏ** | ⛔ CHƯA ĐIỀN |
| **Danh sách lỗi cụ thể (đường dẫn + số dòng + bằng chứng thô)** | ⛔ CHƯA ĐIỀN |
| **Điều kiện để PASS (nếu có)** | ⛔ CHƯA ĐIỀN |
| **Đánh giá tính mới (giữ nguyên / hạ cấp / bác)** | ⛔ CHƯA ĐIỀN |
| **Chữ ký Reviewer1 + agent_id** | ⛔ CHƯA ĐIỀN |
| **Ngày ký** | ⛔ CHƯA ĐIỀN |

---

## PHẦN D — PHẢN HỒI CỦA TÁC GIẢ (chỉ điền SAU khi Reviewer1 đã ký)

| # | Lỗi Reviewer1 nêu | Tác giả đồng ý / phản đối | Hành động + commit hash |
|---|---|---|---|
| D1 | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

---

*Phiếu tạo bởi ResearchLead (`ag_d85dde8d`) ngày 2026-10-01. Phần B, C để trống có chủ đích.*
