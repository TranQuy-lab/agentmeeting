# SUMMARY — Tổng kết phiên

**Người lập:** Admin · **Ngày:** 2026-10-01 · **Trạng thái:** ĐANG CHẠY

> ⚠️ **Chưa có kết luận nào.** File này cố ý để trống phần kết quả cho tới khi có artifact
> đã qua kiểm định 3 lớp. Mọi kết luận đưa vào đây PHẢI trỏ tới đường dẫn bằng chứng cụ thể
> trong repo. Kết luận không có bằng chứng = Auditor2 đánh dấu vi phạm.

## 1. Kết quả đã nghiệm thu

**Đã merge vào `main`:** `reviews/{CROSS,RECONCILE,BLIND}.md` (T6, `c579d1f`) và
`reviews/AUDIT.md`+`AUDIT.json` (T7, `99672c5`). Đây là **hạ tầng kiểm định và bản kiểm toán**,
**không phải kết quả nghiên cứu hay lỗ hổng** — mục này vẫn **chưa có kết quả kỹ thuật nào
được nghiệm thu**. Đính chính N-07 của Auditor2.

**Chưa merge** (đang chờ kiểm định): T1, T2, T3, T4, T5, T11, T13, T15, T16, T17.

## 2. Việc chưa làm được / thất bại

*Chưa có.* — Mục này KHÔNG được lược bỏ khỏi báo cáo cuối.

## 3. Rủi ro đang mở

> **ĐÍNH CHÍNH DEF-6 (Reviewer1 phát hiện):** bảng này trước đây **thiếu cột Bằng chứng**,
> tự vi phạm luật ở dòng 6-7 của chính file này. Đã thêm cột.

| # | Rủi ro | Mức | Đối phó | Bằng chứng |
|---|---|---|---|---|
| 1 | Phòng giới hạn 500 tin; 8+ agent poll liên tục sẽ đầy nhanh | Cao | Nội dung dài ghi file trong repo, tin nhắn chỉ giữ điều phối | `admin_cli.py status` → 500 max; HTTP 422 khi Admin gửi tin 4892 ký tự (`ADMIN/LOG.md` #8) |
| 2 | Worker tự bịa cấu trúc nếu clone repo trước khi có khung | Đã xử lý | Đã push khung ở commit đầu tiên | commit `abe0c3e`; `DeepSeek-Harness` msg_id=8 §1 xác nhận cây thư mục đủ |
| 3 | HTTPS credential helper hỏng, agent clone sai giao thức | Trung bình | Mọi prompt ghi rõ SSH, cấm HTTPS | `ssh -T git@github.com` → `Hi TranQuy-lab!` OK; Reviewer1 từ chối kiểm mục này vì D-001 cấm HTTPS |
| 4 | **`pip` không tồn tại + `sudo` cần mật khẩu ⇒ nhiều agent không cài được thư viện** | **Cao** | Dùng `uv` (không cần sudo). Script tái lập đã push | `agents/forensicsmal/T5/EVIDENCE/tooling_bootstrap_raw.txt`; `agents/forensicsmal/T5/scripts/bootstrap_tools.sh` |
| 5 | **Bằng chứng bảo mật chỉ do MỘT người chạy được ⇒ không đạt lớp 2** | Cao | Cấp slot 8 (DeepSeek-Harness) làm Verifier lớp 2 | `ADMIN/LOG.md` #12; D-006 |
| 6 | **Thiếu testbed mạng và cụm K8s ⇒ 2 hồ sơ NCKH chỉ là thiết kế, không có số liệu** | **Cao** | Cấp slot 9 (Antigravity, MCP Packet Tracer thật) | `ADMIN/LOG.md` #24; báo cáo T2 ResearchLead |
| 7 | **8 nguồn không fetch được (MDPI 403, ACM DL 403…) ⇒ mất nguồn đối chiếu lớp 2** | Trung bình | Cấp slot 10 (javis, trình duyệt thật) | `research/EVIDENCE/FETCH_STATUS`; `ADMIN/LOG.md` #25 |
| 8 | **4 tài sản GitLab có xung đột scope trong dữ liệu công bố của chính GitLab** | Trung bình | Loại khỏi T4; cấm khai thác tới khi GitLab làm rõ | D-013; báo cáo T3 BountyRecon |
| 9 | **Máy không có môi trường cô lập đã xác minh ⇒ phân tích động malware bị đình chỉ** | Trung bình | Đình chỉ phân tích động; chỉ làm tĩnh | `agents/forensicsmal/T5/FORENSICS_PROCEDURE.md`; `ADMIN/LOG.md` |
| 10 | **Hai đề tài NCKH HOÀ điểm 48–48 sau khi Reviewer1 chấm lại tính mới** | Trung bình | Admin chốt thứ tự ưu tiên; xem `ADMIN/LOG.md` #35 | `ADMIN/LOG.md` #35; `reviews/CROSS.md` T11 |
| 11 | **DOI S29 ghi sai hoa/thường ở 4 tài liệu (ICICT vs iccit) ⇒ 404** | Trung bình | Giao ResearchLead T19 sửa; **không phải bịa nguồn**, metadata đã xác minh thật | DISSENT-6; `reviews/CROSS.md` T11 |
| 12 | **`capstone` khai báo phiên bản KHÔNG nhất quán: metadata 5.0.9 vs `__version__` 5.0.7** | Thấp | Agent nào trích version capstone phải ghi rõ dùng nguồn nào | `agents/forensicsmal/T15/T15_REPORT.md` |
| 13 | **Bẫy đối chiếu chéo: so CHUỖI THÔ giữa 2 công cụ báo lệch sai** (`4660` vs `0x1234`, `0` vs `False`) | Trung bình | Phải chuẩn hoá về **giá trị** (`int(x,0)`, `bool`) trước khi so | `agents/forensicsmal/T15/T15_REPORT.md` T15-1 |
| 14 | **Nguy cơ mất nội dung khi merge T1: bản vá `INDEX.md:10` của Admin sẽ bị ghi đè** | **Cao** | KHÔNG merge T1 kiểu "lấy bản worker"; phải rebase và giữ `INDEX.md:10` | N-03 của Auditor2; Reviewer1 xác nhận độc lập |
