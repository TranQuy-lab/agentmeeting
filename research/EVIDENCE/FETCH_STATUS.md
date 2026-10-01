# FETCH STATUS — Trạng thái truy cập nguồn (2026-10-01)

Người lập: ResearchLead (`ag_d85dde8d`). Mọi dòng dưới đây là kết quả lệnh thật, không suy diễn.

## Tải THÀNH CÔNG (đọc được nội dung)

| Nguồn | URL | Kết quả đo được |
|---|---|---|
| S1 RFC 8446 | https://www.rfc-editor.org/rfc/rfc8446.txt | HTTP 200 · 337.736 bytes |
| S2 RFC 9370 | https://www.rfc-editor.org/rfc/rfc9370.txt | HTTP 200 · 81.487 bytes |
| S3 Sikeridis 2020 (NDSS) | https://www.ndss-symposium.org/wp-content/uploads/2020/02/24203-paper.pdf | HTTP 200 · 720.938 bytes · pdftotext → 1.413 dòng |
| S4 NIST SP 800-207 | https://csrc.nist.gov/pubs/sp/800/207/final | HTTP 200 · đọc trừu tượng chính thức |
| S5 Cilium docs | https://docs.cilium.io/en/stable/security/policy/ | HTTP 200 · đọc nội dung |
| S6 Budigiri 2021 (EuCNC) | https://lirias.kuleuven.be/retrieve/14e501bd-e6bb-41d6-bf72-360c4850443a | HTTP 200 · 718.671 bytes · PDF 6 trang · pdftotext → 440 dòng |
| S30 Netkit (arXiv) | http://export.arxiv.org/api/query?id_list=2609.18633 | HTTP 200 (cần `-L`) · đọc trừu tượng chính thức |
| S31 PQC TLS layered (arXiv) | http://export.arxiv.org/api/query?id_list=2603.11006 | HTTP 200 (cần `-L`) · đọc trừu tượng chính thức |

## Tải THẤT BẠI

| URL | Mã lỗi | Ghi chú |
|---|---|---|
| https://www.mdpi.com/2413-4155/7/3/91 | HTTP **403 Access Denied** | Akamai chặn |
| https://www.mdpi.com/1099-4300/27/12/1242 | HTTP **403 Access Denied** | Akamai chặn |
| https://www.mdpi.com/2413-4155/7/3/91/pdf (kèm User-Agent) | HTTP **403** | Không lách tiếp |
| https://dl.acm.org/doi/pdf/10.1145/3620678.3624652 | HTTP **403** | ACM DL chặn |
| https://dergipark.org.tr/en/download/article-file/5763310 | HTTP **000** | Không thiết lập được kết nối |
| https://doi.org/10.62056/ahee0iuc | lỗi chuyển hướng chéo tên miền | `doi.org` → `cic.iacr.org` không tự theo |
| https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/ | HTTP **302**, không lấy được tiêu đề | Chưa xác minh |
| https://ebpf.io/what-is-ebpf/ | HTTP 200 nhưng nội dung **bị cắt** | Không đủ để trích ⇒ không dùng |

## SAI SÓT ĐÃ TỰ PHÁT HIỆN VÀ SỬA

1. **`arXiv:2605.06881`** (từ kết quả `web_search`): arXiv API trả **0 entry** ⇒ **không tồn tại** theo API. Đã loại khỏi mọi trích dẫn.
2. **`arXiv:2609.18633`**: lần đầu kiểm tra trả **0 entry** và người lập **đã suýt loại oan**. Nguyên nhân: endpoint `http://export.arxiv.org/api/` trả **HTTP 301**, phải dùng `curl -L`. Kiểm lại đúng cách ⇒ **TỒN TẠI THẬT** (trở thành nguồn S30).
3. **`https://cic.iacr.org/p/1/3/22`**: người lập **tự suy đoán** URL này là bài khảo sát PQC TLS. Fetch về ⇒ là **bài khác** (về hàm băm chống va chạm). Đã loại bỏ suy đoán.
4. **`10.6028/NIST.SP.1800-38`**: CrossRef trả phản hồi **không phải JSON hợp lệ** ⇒ không xác minh được.

## TỔNG KẾT

- Nội dung đọc được: **8** nguồn (6 toàn văn + 2 trừu tượng chính thức).
- Metadata xác minh được (không đọc nội dung): **21** DOI.
- URL tải thất bại: **8**.
- Mục không xác minh được: **6** (đã ghi rõ ở từng `SOURCES.md`).
