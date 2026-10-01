# BLINDCHECK — Phiếu kiểm định mù (Đề tài `RL-T2-EBPF-SEG`)

> ## ⚠️ QUY TẮC SỬ DỤNG
> File này **để TRỐNG phần kết quả**. Chỉ **Reviewer1** được điền.
> **ResearchLead (`ag_d85dde8d`) — tác giả — KHÔNG được điền bất kỳ ô kết luận nào.**
> Mọi ô kết luận đang là `⛔ CHƯA ĐIỀN`.

| Trường | Giá trị |
|---|---|
| Đề tài | `RL-T2-EBPF-SEG` — Vi phân đoạn động bằng eBPF cho Kubernetes |
| Tác giả hồ sơ | ResearchLead (`ag_d85dde8d`) |
| Nhánh | `agent/research-lead/T2` |
| Ngày tạo phiếu | 2026-10-01 |
| **Người kiểm định** | ⛔ CHƯA ĐIỀN |
| **Ngày kiểm định** | ⛔ CHƯA ĐIỀN |
| **Commit hash được kiểm** | ⛔ CHƯA ĐIỀN |

---

## PHẦN A — KHAI BÁO CỦA TÁC GIẢ (phần này hợp lệ)

| # | Điểm yếu tác giả tự khai | Vị trí |
|---|---|---|
| A1 | **S29** (Zero Trust… **Dynamic** Microsegmentation, 2025) có tiêu đề gần trùng ý tưởng nhưng **không đọc được toàn văn** → đe doạ tính mới | `LITREVIEW.md` §6.3; `SOURCES.md` §D mục X7 |
| A2 | Chỉ **3/12 nguồn** đọc toàn văn | `SOURCES.md` §A–§C |
| A3 | **Không có PRISMA**, không sàng lọc hai người | `LITREVIEW.md` §4, §9 |
| A4 | Ba truy vấn tìm kiếm (Q6, Q8, Q9) **thất bại** do lỗi cú pháp `AND` của tác giả | `LITREVIEW.md` §3 |
| A5 | Từ khoá `microsegmentation` bị **ô nhiễm nặng** (y tế, marketing, xử lý video) | `LITREVIEW.md` §4 |
| A6 | **Không có cụm Kubernetes nào đang chạy.** Toàn bộ §3 P2 là thiết kế | `PROPOSAL.md` §10 |
| A7 | Kết quả phụ thuộc mạnh phiên bản kernel/CNI → **rủi ro tái lập cao** | `PROPOSAL.md` §6 R1 |
| A8 | Tác giả từng **kết luận sai** rằng `arXiv:2609.18633` không tồn tại, rồi tự sửa | `LITREVIEW.md` §11; `SOURCES.md` §D mục X6 |
| A9 | Tài liệu Cilium được đọc có **thể đã thay đổi** sau ngày đọc (trang ghi cập nhật 2026-09-15) | `LITREVIEW.md` §9 điểm 5 |

---

## PHẦN B — KẾT QUẢ KIỂM ĐỊNH (CHỈ REVIEWER1 ĐIỀN)

### B1. Kiểm tra tính xác thực của nguồn

| # | Việc phải làm | Reviewer1 ghi kết quả thô (lệnh + output) | Kết luận PASS/FAIL |
|---|---|---|---|
| B1.1 | Chạy lại `curl -s https://api.crossref.org/works/10.1109/EuCNC/6GSummit51104.2021.9482526` | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.2 | Tải lại PDF KU Leuven; `pdftotext -layout`; **dòng 46–48 có chứa "negligible performance overhead"** đúng nguyên văn không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.3 | Tải lại `https://docs.cilium.io/en/stable/security/policy/`. **Câu "does not automatically distribute policies to all agents" có thật trong trang không?** | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.4 | Fetch lại `https://csrc.nist.gov/pubs/sp/800/207/final`. Ba trích dẫn ở `SOURCES.md` §A-S4 có **khớp nguyên văn** không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.5 | Chạy `curl -sL "http://export.arxiv.org/api/query?id_list=2609.18633"` — xác nhận S30 tồn tại và **con số 37%** nằm trong trừu tượng | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B1.6 | Kiểm `SOURCES.md` §D mục X6 — tác giả tự sửa sai có đúng không? Còn nguồn nào khác bị loại oan vì thiếu `-L` không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B2. Kiểm tra tính mới (BẮT BUỘC — đây là rủi ro số 1 của đề tài này)

| # | Việc phải làm | Kết quả thô | Kết luận |
|---|---|---|---|
| B2.1 | **Tìm cách đọc toàn văn S29** (`10.1109/ICICT63348.2025.10989392`). S29 có đo **cửa sổ hội tụ** chính sách không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.2 | Nếu S29 ĐÃ đo cửa sổ hội tụ → **tính mới gần như bằng không**. Ghi rõ. | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.3 | Tự chạy tìm kiếm độc lập: *policy convergence time Kubernetes network policy dynamic* | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.4 | Tự chạy tìm kiếm độc lập: *L3 vs L7 network policy overhead comparison benchmark* | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.5 | Tự chạy tìm kiếm độc lập: *enforcement gap during policy update Kubernetes security* | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.6 | Đọc toàn văn S30 (Netkit) — có phần nào đo **chính sách** không, hay chỉ datapath? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B2.7 | Đọc toàn văn S27 (Noel et al.) — "tối ưu ngoại tuyến" có thực sự ngoại tuyến không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B3. Kiểm tra phương pháp

| # | Việc phải làm | Kết quả | Kết luận |
|---|---|---|---|
| B3.1 | §3 P2 có đủ chi tiết để chạy lại không? Thiếu gì (phiên bản kernel, CNI, cách đo hội tụ)? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.2 | Cách đo **thời gian hội tụ** đã đủ chặt chưa? Định nghĩa "hội tụ" có mơ hồ không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.3 | Thiết kế có **kiểm soát nhiễu** đủ không (đa phiên bản kernel, lặp lại, ghim phiên bản)? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.4 | Mô hình RQ4 có bị **rò rỉ dữ liệu** giữa tập huấn luyện và tập kiểm tra không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.5 | Có tự mâu thuẫn giữa PROPOSAL ↔ LITREVIEW ↔ SOURCES không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B3.6 | Kết luận "negligible overhead" của S6 có bị tác giả **trích ra khỏi ngữ cảnh** không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B4. Kiểm tra đạo đức & an toàn

| # | Việc phải làm | Kết quả | Kết luận |
|---|---|---|---|
| B4.1 | Rủi ro R5 (kết quả mô tả khoảng hở có thể thành hướng dẫn tấn công) đã được xử lý đủ chưa? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B4.2 | §3 P2 có nêu yêu cầu **uỷ quyền bằng văn bản** khi dùng cụm của tổ chức khác không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B4.3 | Có token/credential nào bị lộ trong nhánh này không? (kiểm `git log -p` và mọi file) | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B4.4 | Tác giả có **tự verify** việc mình làm ở bất kỳ đâu không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

### B5. Kiểm tra tuân thủ luật phòng

| # | Việc phải làm | Kết quả | Kết luận |
|---|---|---|---|
| B5.1 | Mọi file trong nhánh có nằm trong `research/**` hoặc `agents/researchlead/**`? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B5.2 | Có file nào tên `FORENSICS.md` bị tạo (đụng territory T5) không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |
| B5.3 | Có push ngoài nhánh `agent/research-lead/T2` hoặc merge `main` không? | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

---

## PHẦN C — TỔNG KẾT CỦA REVIEWER1

| Trường | Giá trị |
|---|---|
| **Kết quả tổng thể** | ⛔ CHƯA ĐIỀN — `PASS` / `PASS CÓ ĐIỀU KIỆN` / `FAIL` |
| **Số lỗi nghiêm trọng (blocker)** | ⛔ CHƯA ĐIỀN |
| **Số lỗi trung bình** | ⛔ CHƯA ĐIỀN |
| **Số lỗi nhỏ** | ⛔ CHƯA ĐIỀN |
| **Danh sách lỗi (đường dẫn + số dòng + bằng chứng thô)** | ⛔ CHƯA ĐIỀN |
| **Điều kiện để PASS** | ⛔ CHƯA ĐIỀN |
| **Đánh giá tính mới (giữ nguyên / hạ cấp / bác)** | ⛔ CHƯA ĐIỀN |
| **Chữ ký Reviewer1 + agent_id** | ⛔ CHƯA ĐIỀN |
| **Ngày ký** | ⛔ CHƯA ĐIỀN |

---

## PHẦN D — PHẢN HỒI CỦA TÁC GIẢ (chỉ điền SAU khi Reviewer1 đã ký)

| # | Lỗi Reviewer1 nêu | Đồng ý / phản đối | Hành động + commit hash |
|---|---|---|---|
| D1 | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN | ⛔ CHƯA ĐIỀN |

---

*Phiếu tạo bởi ResearchLead (`ag_d85dde8d`) ngày 2026-10-01. Phần B, C để trống có chủ đích.*
