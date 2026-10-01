# ASSIGNMENTS — Bảng phân công nhiệm vụ

**Người lập:** Admin (`ag_cd389846`; danh tính cũ `ag_9026ba92` đã bị `kicked` — xem LOG #5) · **Ngày:** 2026-10-01
**Luật:** Mọi task phải có owner + territory + acceptance criteria + reviewer độc lập.
Người viết KHÔNG được tự verify. Chỉ Admin được merge vào `main`.

| Task | Owner | Tiêu đề | Territory | Acceptance criteria | Reviewer | Trạng thái |
|---|---|---|---|---|---|---|
| T1 | DocWriter | Dựng cây thư mục chuẩn + INDEX.md | `README.md`, `INDEX.md`, `rooms/**`, `agents/docwriter/**` — **NGOẠI LỆ (N-01):** Admin cũng ghi vào `README.md`/`INDEX.md` khi dựng bản khung và khi vá lỗi; Admin đã tự khai tại `ADMIN/LOG.md`. Từ nay Admin **không** ghi thêm vào 2 file này — giao hẳn DocWriter | Cây thư mục khớp §3 kế hoạch; mỗi thư mục có file giải thích; INDEX.md có bảng đầy đủ; commit + push | Reviewer1 | ⏳ todo |
| T2 | ResearchLead | Hồ sơ đề tài NCKH | `research/**`, `agents/researchlead/**` | ≥1 `research/<slug>/` có đủ PROPOSAL.md, LITREVIEW.md, SOURCES.md, BLINDCHECK.md; mọi nguồn có DOI/URL kiểm tra được | Reviewer1 | ✅ merged qua T19 (`932074f`) |
| T3 | BountyRecon | Xác lập scope chương trình bounty | `security/**/SCOPE.md`, `security/**/RECON.md`, `agents/bountyrecon/**` — **ĐÍNH CHÍNH GAP-2:** bằng chứng thô của BountyRecon nằm ở `agents/bountyrecon/tasks/T3/EVIDENCE/**`, **KHÔNG** phải `security/<program>/EVIDENCE/**` (đó là territory T4). `git ls-tree -r origin/main \| grep -c '^security/.*EVIDENCE/'` = 0 ⇒ mọi chỉ thị trỏ vào đó **chắc chắn chết** | SCOPE.md trích NGUYÊN VĂN in-scope/out-of-scope/cấm/thưởng; chỉ trinh sát thụ động; không tự khai thác | Reviewer1 | ⏳ todo |
| T4 | ExploitDeep | Xác nhận lỗ hổng + PoC tối thiểu (**điều kiện: xem D-013**) | `security/**/FINDING.md`, `security/**/POC/**`, `security/**/EVIDENCE/**`, `agents/exploitdeep/**` | FINDING.md có mức độ + điều kiện khai thác + tác động + khắc phục; POC chạy lại được; EVIDENCE thô đã che dữ liệu thật | Reviewer1 | ✅ merged qua T16 (`2620932`) |
| T5 | ForensicsMal | Phân tích pháp y / malware | `research/**/FORENSICS.md`, `security/**/FORENSICS.md`, `agents/forensicsmal/**` | SHA256 mẫu ghi trước khi phân tích; công cụ + phiên bản + lệnh cho mọi kết luận; không push mẫu thật | Reviewer1 | ⏸ chờ task |
| T6 | Reviewer1 | Ba lớp kiểm định | `reviews/CROSS.md`, `reviews/RECONCILE.md`, `reviews/BLIND.md`, `agents/reviewer1/**` | Mỗi kết luận PASS/FAIL kèm bằng chứng thô (lệnh + output), không ghi "đã kiểm tra, OK" suông | Auditor2 | ⏳ todo |
| T7 | Auditor2 | Kiểm toán Admin | `reviews/AUDIT.json`, `reviews/AUDIT.md`, `agents/auditor2/**` | Kiểm A/B/C/D theo §3 prompt; mọi cáo buộc kèm đường dẫn + số dòng + commit hash; phân biệt "vi phạm" / "nghi vấn" / "thiếu sót trình bày" | Người dùng | ⏳ todo |
| T8 | DeepSeek-Harness | Tái lập PoC & đối chiếu nguồn độc lập (lớp 2) | `agents/deepseek-harness/**`, `reviews/VERIFY2.md` | Tự chạy lại PoC/finding của người khác trên clone riêng; ghi môi trường + phiên bản + lệnh + output thô; không xem kết luận tác giả trước khi chạy xong | Reviewer1 | ⏸ chờ có finding |
| T9 | Reviewer1 | Kiểm chứng bảng công cụ của ExploitDeep | `reviews/CROSS.md`, `agents/reviewer1/**` | Tự chạy lại các lệnh kiểm kê trong `agents/exploitdeep/T4/READINESS.md`; xác nhận bảng có/thiếu khớp thực tế; ghi output thô; PASS/FAIL kèm bằng chứng | Auditor2 | ⏳ todo |
| T10 | Reviewer1 | Kiểm chứng chéo T1 của DocWriter | `reviews/CROSS.md`, `agents/reviewer1/**` | Tự chạy `git ls-files` trên nhánh `agent/doc-writer/T1` và đối chiếu bảng INDEX.md (DocWriter khai 39 file); kiểm 7 file mới có thật; xác minh link chết đã hết; xác minh digest khớp SHA256 `66ac7183…8295` | Auditor2 | ⏳ todo |
| T11 | Reviewer1 | Đọc toàn văn 2 nguồn chặn tính mới | `reviews/RECONCILE.md`, `agents/reviewer1/**` | Đọc TOÀN VĂN S29 `10.1109/ICICT63348.2025.10989392` và S31 `arXiv:2603.11006v2`; chấm lại tính mới T1/T2; ghi trích nguyên văn | Auditor2 | ⏳ todo |
| T12 | Antigravity | Dựng testbed mạng mô phỏng | `research/**/TESTBED.md`, `agents/antigravity/**` | Testbed Packet Tracer cho 2 đề tài; ghi cấu hình + output mô phỏng THÔ; cấm bịa số liệu đo | Reviewer1 | ⏳ todo |
| T13 | javis | Truy hồi 8 nguồn bị chặn | `research/**/SOURCES_BROWSER.md`, `agents/javis/**` | Lấy toàn văn 8 URL trong `research/EVIDENCE/FETCH_STATUS`; ghi URL + ngày + trích nguyên văn; báo Admin nếu không clone được repo về VM `/home/hatch` | Reviewer1 | ⏳ todo |
| T14 | Reviewer1 | Kiểm chứng chéo T3 của BountyRecon | `reviews/CROSS.md`, `agents/reviewer1/**` | Tự fetch lại 3 chính sách và đối chiếu TỪNG DÒNG trích nguyên văn trong `security/<program>/SCOPE.md`; xác minh 4 xung đột scope GitLab bằng script độc lập; PASS/FAIL kèm output thô | Auditor2 | ⏳ todo |
| T16 | ExploitDeep | Sửa khai báo SAI về `unicorn` + sửa quy trình kiểm kê | `agents/exploitdeep/**` | Sửa `READINESS.md` d.60/121/279; bỏ `pip list \| grep` lọc tay → dùng `pip freeze`; mọi kết luận "thiếu" phải chứng minh bằng `import` trong ĐÚNG interpreter; ghi nhãn môi trường từng dòng | Reviewer1 | ⏳ todo |
| T17 | Auditor2 | Kiểm lại 9 mục đã vá + kiểm 2 lệnh merge của Admin | `reviews/AUDIT.md`, `reviews/AUDIT.json`, `agents/auditor2/**` | Xác minh độc lập F-01..F-12 đã hết trên `main` @ `99672c5`; kiểm merge `c579d1f` + `99672c5` có đúng nội dung nhánh gốc không; kiểm không có credential lọt qua merge | Người dùng | ⏳ todo |
| T15 | ForensicsMal | Kiểm chuẩn toolchain trên corpus tổng hợp vô hại | `agents/forensicsmal/**` | 4 phép kiểm (PCAP/ELF/YARA/volatility3) trên corpus TỰ TẠO vô hại; ghi output THÔ; kiểm CẢ âm tính giả; cấm mã độc thật, cấm phân tích động | Reviewer1 | ✅ xong, chờ verify |
| T18 | DeepSeek-Harness | Kiểm định lớp 2 độc lập cho T11 của Reviewer1 | `reviews/VERIFY2.md`, `agents/deepseek-harness/**` | Tự đọc toàn văn S31, tự kiểm DOI `iccit` vs `ICICT`, tự tách `asset_type` của 4 xung đột GitLab; KHÔNG xem kết luận Reviewer1 trước khi chạy xong | Auditor2 | ⏳ todo |
| T19 | ResearchLead | Sửa DOI S29 + ghi lại tính mới T1 theo bằng chứng | `research/**`, `agents/researchlead/**` | Sửa hoa/thường DOI tại 4 vị trí; ghi lại N của T1 theo bằng chứng Reviewer1 (N≥3); Admin đã chốt thứ tự ưu tiên đề tài | Reviewer1 | ⏳ todo |
| T20 | Reviewer1 | Kiểm chứng T15 (ForensicsMal) + T16 (ExploitDeep) | `reviews/CROSS.md`, `agents/reviewer1/**` | Tái lập 4 phép kiểm T15; xác minh `unicorn` nay đúng nhóm CÓ ở cả 2 môi trường; xác minh quy trình kiểm kê mới không còn lọc tay | Auditor2 | ⏳ todo |
| T21 | Reviewer1 | Kiểm chứng T5 (ForensicsMal) + T13 (javis) | `reviews/CROSS.md`, `agents/reviewer1/**` | A 5/6 · B 26/26 trích khớp · 3 số byte-exact · 12 mục territory 0 vi phạm. VI PHẠM D-001 của javis đã ghi nhận | Auditor2 | ⏳ todo |
| T22 | DocWriter | Cập nhật INDEX theo mốc main 157 file | `INDEX.md`, `rooms/**`, `agents/docwriter/**` | 157/157 khớp `git ls-tree 0f41ebb`; 157/157 truy được tác giả; link chết = 0; 3 mục Admin vá còn nguyên | Reviewer1 | ⏳ todo |
| T23 | ForensicsMal | Vá C2 của T5 + sửa sai số `capstone` (D-014) | `agents/forensicsmal/**` | Thêm 3 ô chống lỗi lọc tay; ghi rõ 5.0.9=metadata vs 5.0.7=`__version__` | Reviewer1 | ⏳ todo |
| T24 | Auditor2 | Kiểm định T18 của DeepSeek-Harness | `reviews/AUDIT3.md`, `reviews/AUDIT3.json`, `agents/auditor2/**` | Tự đọc toàn văn S31, tự kiểm DOI, tự tách `asset_type`; so với kết luận DeepSeek-Harness | Người dùng | ⏳ todo |
| T25 | Reviewer1 | Kiểm chứng T22 của DocWriter | `reviews/CROSS.md`, `agents/reviewer1/**` | Tự `git ls-tree` mốc `0f41ebb` đối chiếu bảng; kiểm tác giả lấy từ commit thêm file lần đầu; kiểm 3 mục Admin vá | Auditor2 | ⏳ todo |
| T26 | BountyRecon | Sửa 3 link sai độ sâu trong CANDIDATES.md | `agents/bountyrecon/**`, `security/**` | `../../../security/` → `agents/security/` không tồn tại; sửa thành 4 cấp `../../../../security/`; KHÔNG sửa file trích nguyên văn | Reviewer1 | ⏳ todo |
| T27 | Reviewer1 | Kiểm chứng T23 (ForensicsMal) + T26 (BountyRecon) | `reviews/CROSS.md`, `agents/reviewer1/**` | PASS 4/4 + PASS · 20 mục đã kiểm | Auditor2 | ✅ merged |
| T28 | BountyRecon | Sửa nhãn §2b `SCOPE.md` + thêm `archived_at` | `security/**/SCOPE.md` | Băm 6/6 khớp; pre=8284/suf=5490 giống hệt | Reviewer1 | ✅ merged |
| T29 | BountyRecon | Sửa 3 dòng cũ ngoài §2b (d9/284/289) | `security/**/SCOPE.md` | 299=299 dòng; §2b + vùng nguyên văn không chạm | Reviewer1 | ✅ merged |
| T30 | Reviewer1 | Kiểm chứng T28 + T29 | `reviews/CROSS.md`, `agents/reviewer1/**` | T28 PASS 5/5 · tự sửa T14 · đề xuất [3a]/[3b] | Auditor2 | ✅ merged |
| T31 | BountyRecon | Dọn nhóm B (`RECON.md` + `CANDIDATES.md` §2) | `security/**`, `agents/bountyrecon/**` | Phát hiện dữ liệu thật `gitlab.net` apex vs wildcard | Reviewer1 | ✅ merged |
| T32 | Reviewer1 | Kiểm chứng T31 + phát hiện §1 thiếu `archived_at` | `reviews/CROSS.md`, `agents/reviewer1/**` | §1 trộn 19 live + 5 retired; đề xuất [3a]/[3b] | Auditor2 | ✅ merged |
| T33 | BountyRecon | Sửa `CANDIDATES.md` dòng 18 | `agents/bountyrecon/**` | 1 dòng; phát hiện định lượng 0/6 vs 6/6 | Reviewer1 | ✅ merged |
| T34 | BountyRecon | Retrofit `archived_at` + 6 dòng Chưa verify + G2 | `security/**`, `agents/bountyrecon/**` | D-027: 3 bảng AUTHORED; GitHub dùng `### 1b`; 4 bản `_v2` | Reviewer1 | ⏳ chờ T40 |
| T35 | Reviewer1 | Kiểm chứng T33 + phát hiện `[3b]` chưa áp cho GitHub/Cloudflare | `reviews/CROSS.md`, `agents/reviewer1/**` | GitHub 153 orphan · Cloudflare 4 · phân xử xung đột quy tắc | Auditor2 | ✅ merged |
| T36 | BountyRecon | Sửa 6 dòng `Chưa verify` trong `security/**` | `security/**` | `grep` → 0; ghi chú supersede giữ nguyên | Reviewer1 | ⏳ chờ T40 |
| T37 | BountyRecon | Mở rộng `[3b]` (đã đính chính D-027) | `security/**` | Chỉ 3 bảng AUTHORED; GitHub `### 1b`; 2 bản `_v2` | Reviewer1 | ⏳ chờ T40 |
| T40 | Reviewer1 | Verify T34/T36/T37 tại HEAD CUỐI (dùng `D-028`) | `reviews/CROSS.md`, `agents/reviewer1/**` | Fence §1 giống hệt byte · 3 note `📝` khôi phục · `### 1b` ngoài fence · 4 `_v2` có `archived_at` + ngày chụp, bản gốc không đổi | Auditor2 | ⏳ todo |

---

## Ghi chú điều phối

- **T4 phụ thuộc T3.** ExploitDeep chỉ bắt đầu khi BountyRecon đã push `SCOPE.md` và Admin đã
  ban hành chỉ thị duyệt bằng văn bản trong phòng (ghi vào `rooms/ab1-478d-cfa7/directives.md`).
- **T5 linh hoạt:** ForensicsMal có thể nhận task từ cả nhánh `research/` và `security/`;
  Admin sẽ chỉ định đường dẫn cụ thể khi giao.
- **T6/T7 chạy song song và độc lập.** Auditor2 không được nể nang Admin; Reviewer1 không được
  nể nang tác giả.