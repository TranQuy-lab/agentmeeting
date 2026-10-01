# SUMMARY — Tổng kết phiên

**Người lập:** Admin · **Ngày:** 2026-10-01 · **Trạng thái:** ĐANG CHẠY

> ⚠️ **Chưa có kết luận nào.** File này cố ý để trống phần kết quả cho tới khi có artifact
> đã qua kiểm định 3 lớp. Mọi kết luận đưa vào đây PHẢI trỏ tới đường dẫn bằng chứng cụ thể
> trong repo. Kết luận không có bằng chứng = Auditor2 đánh dấu vi phạm.

## 1. Kết quả đã nghiệm thu

*Chưa có.*

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
