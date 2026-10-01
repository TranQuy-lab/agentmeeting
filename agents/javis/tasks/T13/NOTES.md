# T13 — Nhật ký phương pháp & bằng chứng truy hồi (javis)

**Task:** T13 theo D-012 (msg #43) + assignment msg #48 · **Nhánh:** `agent/javis/T13`
**Ngày:** 2026-10-01 · **Clone:** `~/workspace/agentmeeting` trên VM của javis (clone bằng HTTPS — đã xác minh đủ khung D-001: `README.md`, `INDEX.md`, `ADMIN/`, `agents/`, `research/`, `security/`, `reviews/`, `rooms/`).

## Sản phẩm

- `research/pqc-tls-migration/SOURCES_BROWSER.md` — S16, S15, S17, S7, X4 (RFC 9954).
- `research/ebpf-microsegmentation/SOURCES_BROWSER.md` — S24, ebpf.io.

## Nhật ký thử truy hồi (mọi dòng là kết quả lệnh/công cụ thật trên VM này)

| # | URL | curl -L (UA trình duyệt) | Fetch nội dung trang | Trình duyệt thật | Kết luận |
|---|---|---|---|---|---|
| 1 | mdpi.com/2413-4155/7/3/91 | 403 · 396 B | 200 · toàn văn 1.187 dòng | — | ✅ Toàn văn |
| 2 | mdpi.com/1099-4300/27/12/1242 | 403 · 400 B | 200 · toàn văn 1.451 dòng | — | ✅ Toàn văn |
| 3 | mdpi.com/2413-4155/7/3/91/pdf | 403 · 404 B | 403 | Chưa kiểm chứng được riêng (trình duyệt bận ở thử thách ACM) | ⚠️ Riêng PDF chưa xác minh; nội dung bài đã có qua #1 |
| 4 | dl.acm.org/doi/pdf/10.1145/3620678.3624652 | 000 · 0 B | 403 | Cloudflare "xác minh bạn là con người" — không bypass | ❌ Chưa xác minh |
| 5 | dergipark.org.tr/en/download/article-file/5763310 | **200 · PDF 1.108.312 B** | — | — | ✅ Toàn văn PDF (`pdftotext` OK) |
| 6 | doi.org/10.62056/ahee0iuc | **200 · đích cic.iacr.org/p/1/2/6 · 168.296 B** | — | — | ✅ Trang đích + abstract |
| 7 | datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/ | **200 · đích /doc/rfc9954/ · 79.550 B** | — | — | ✅ Đã thành RFC 9954 |
| 8 | ebpf.io/what-is-ebpf/ | **200 · 340.219 B** | — | — | ✅ Toàn văn |

## Ghi chú trung thực

- Không kênh nào được dùng để lách kiểm soát truy cập: 403 giữ nguyên là 403 ở kênh đó; thử thách Cloudflare ở ACM **không** được tự vượt qua. Kết quả "lấy được" đến từ kênh hợp lệ khác (fetch nội dung trang của MDPI, chuyển hướng công khai của DOI/datatracker, kết nối trực tiếp tới DergiPark/ebpf.io từ mạng của VM này).
- Metadata tác giả/venue đối chiếu qua Crossref API ngày 2026-10-01; abstract S15/S16 trích từ Crossref khớp với toàn văn đã đọc.
- File bằng chứng thô (HTML/PDF đã tải) lưu tại máy của javis ngoài repo: `~/.agentmeet/sessions/ab1-478d-cfa7/javis/T13-evidence/` — sẵn sàng cung cấp cho Reviewer1 khi kiểm chứng.
- Người viết không tự verify (D-004). Đề nghị Reviewer1 kiểm chứng độc lập.
