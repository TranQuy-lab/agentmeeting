# ASSIGNMENTS — Bảng phân công nhiệm vụ

**Người lập:** Admin (`ag_cd389846`; danh tính cũ `ag_9026ba92` đã bị `kicked` — xem LOG #5) · **Ngày:** 2026-10-01
**Luật:** Mọi task phải có owner + territory + acceptance criteria + reviewer độc lập.
Người viết KHÔNG được tự verify. Chỉ Admin được merge vào `main`.

| Task | Owner | Tiêu đề | Territory | Acceptance criteria | Reviewer | Trạng thái |
|---|---|---|---|---|---|---|
| T1 | DocWriter | Dựng cây thư mục chuẩn + INDEX.md | `README.md`, `INDEX.md`, `rooms/**`, `agents/docwriter/**` | Cây thư mục khớp §3 kế hoạch; mỗi thư mục có file giải thích; INDEX.md có bảng đầy đủ; commit + push | Reviewer1 | ⏳ todo |
| T2 | ResearchLead | Hồ sơ đề tài NCKH | `research/**`, `agents/researchlead/**` | ≥1 `research/<slug>/` có đủ PROPOSAL.md, LITREVIEW.md, SOURCES.md, BLINDCHECK.md; mọi nguồn có DOI/URL kiểm tra được | Reviewer1 | ⏳ todo |
| T3 | BountyRecon | Xác lập scope chương trình bounty | `security/**/SCOPE.md`, `security/**/RECON.md`, `agents/bountyrecon/**` | SCOPE.md trích NGUYÊN VĂN in-scope/out-of-scope/cấm/thưởng; chỉ trinh sát thụ động; không tự khai thác | Reviewer1 | ⏳ todo |
| T4 | ExploitDeep | Xác nhận lỗ hổng + PoC tối thiểu | `security/**/FINDING.md`, `security/**/POC/**`, `security/**/EVIDENCE/**`, `agents/exploitdeep/**` | FINDING.md có mức độ + điều kiện khai thác + tác động + khắc phục; POC chạy lại được; EVIDENCE thô đã che dữ liệu thật | Reviewer1 | ⏸ chờ T3 |
| T5 | ForensicsMal | Phân tích pháp y / malware | `research/**/FORENSICS.md`, `security/**/FORENSICS.md`, `agents/forensicsmal/**` | SHA256 mẫu ghi trước khi phân tích; công cụ + phiên bản + lệnh cho mọi kết luận; không push mẫu thật | Reviewer1 | ⏸ chờ task |
| T6 | Reviewer1 | Ba lớp kiểm định | `reviews/CROSS.md`, `reviews/RECONCILE.md`, `reviews/BLIND.md`, `agents/reviewer1/**` | Mỗi kết luận PASS/FAIL kèm bằng chứng thô (lệnh + output), không ghi "đã kiểm tra, OK" suông | Auditor2 | ⏳ todo |
| T7 | Auditor2 | Kiểm toán Admin | `reviews/AUDIT.json`, `reviews/AUDIT.md`, `agents/auditor2/**` | Kiểm A/B/C/D theo §3 prompt; mọi cáo buộc kèm đường dẫn + số dòng + commit hash; phân biệt "vi phạm" / "nghi vấn" / "thiếu sót trình bày" | Người dùng | ⏳ todo |

---

## Ghi chú điều phối

- **T4 phụ thuộc T3.** ExploitDeep chỉ bắt đầu khi BountyRecon đã push `SCOPE.md` và Admin đã
  ban hành chỉ thị duyệt bằng văn bản trong phòng (ghi vào `rooms/ab1-478d-cfa7/directives.md`).
- **T5 linh hoạt:** ForensicsMal có thể nhận task từ cả nhánh `research/` và `security/`;
  Admin sẽ chỉ định đường dẫn cụ thể khi giao.
- **T6/T7 chạy song song và độc lập.** Auditor2 không được nể nang Admin; Reviewer1 không được
  nể nang tác giả.
| T8 | DeepSeek-Harness | Tái lập PoC & đối chiếu nguồn độc lập (lớp 2) | `agents/deepseek-harness/**`, `reviews/VERIFY2.md` | Tự chạy lại PoC/finding của người khác trên clone riêng; ghi môi trường + phiên bản + lệnh + output thô; không xem kết luận tác giả trước khi chạy xong | Reviewer1 | ⏸ chờ có finding |
| T9 | Reviewer1 | Kiểm chứng bảng công cụ của ExploitDeep | `reviews/CROSS.md`, `agents/reviewer1/**` | Tự chạy lại các lệnh kiểm kê trong `agents/exploitdeep/T4/READINESS.md`; xác nhận bảng có/thiếu khớp thực tế; ghi output thô; PASS/FAIL kèm bằng chứng | Auditor2 | ⏳ todo |
| T10 | Reviewer1 | Kiểm chứng chéo T1 của DocWriter | `reviews/CROSS.md`, `agents/reviewer1/**` | Tự chạy `git ls-files` trên nhánh `agent/doc-writer/T1` và đối chiếu bảng INDEX.md (DocWriter khai 39 file); kiểm 7 file mới có thật; xác minh link chết đã hết; xác minh digest khớp SHA256 `66ac7183…8295` | Auditor2 | ⏳ todo |
