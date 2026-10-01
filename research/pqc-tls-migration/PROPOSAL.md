# PROPOSAL — Đề tài 1

## Di trú mật mã hậu lượng tử cho TLS 1.3 tại hạ tầng biên: đo lường chi phí bắt tay có thể tái lập và mô hình quyết định ưu tiên di trú theo rủi ro HNDL

| Trường | Giá trị |
|---|---|
| Mã đề tài | `RL-T1-PQC-TLS` |
| Người đề xuất | **ResearchLead** (`ag_d85dde8d`) — Trưởng nhóm Nghiên cứu |
| Ngày | 2026-10-01 |
| Lĩnh vực | Mạng & an ninh mạng; thiết kế hệ thống |
| Loại hình | Đo lường có kiểm soát (controlled measurement) + mô hình hoá quyết định |
| Trạng thái | ⏳ Chờ Reviewer1 kiểm định độc lập |
| Nhánh | `agent/research-lead/T2` |

---

## 1. Khoảng trống nghiên cứu

Mật mã hậu lượng tử (post-quantum cryptography — PQC) cho TLS đã được nghiên cứu gần một thập kỷ. Ba chuẩn chính đã được NIST chốt ngày **2024-08-13**: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA) — xác minh qua CrossRef (xem `../EVIDENCE/crossref_lookups.txt`, 3 dòng đầu). Tuy vậy, khoảng trống vẫn còn ở **ba điểm cụ thể**:

### 1.1. Thiếu harness đo lường mở, tái lập được, cho hạ tầng biên
Các nghiên cứu đo lường hiện có chủ yếu chạy trong phòng thí nghiệm hoặc trên máy chủ cloud "sạch", không có middlebox chèn giữa. Bằng chứng về hướng này đã tồn tại từ 2020: Sikeridis và cộng sự (NDSS 2020) đo được rằng phần lớn lựa chọn chữ ký PQC chỉ thêm **dưới 5 ms** cho bắt tay, một số cấu hình đạt **~10–15 ms so với RSA3072**, nhưng khi kích thước chứng thư đủ lớn để vượt ngưỡng MTU thì phát sinh **thêm một vòng khứ hồi (~11 ms)** (trích nguyên văn kèm số dòng tại `../EVIDENCE/quote_extracts.txt`, mục A, các dòng nguồn 622 · 667 · 673 · 678). Nghĩa là **biến số quyết định không phải CPU mà là kích thước bản ghi/chứng thư và hành vi của thiết bị trung gian** — đúng loại biến số mà môi trường biên (edge) có nhiều nhất. Chưa có bộ dữ liệu mở nào ghi lại hành vi này cho **hybrid X25519MLKEM768** dưới nhiều cấu hình MTU/middlebox khác nhau.

### 1.2. Chứng thư ML-DSA trong mTLS gần như chưa được đo
Phần lớn công trình đo lường tập trung vào **trao đổi khoá** (key exchange), nơi ML-KEM tỏ ra rẻ. Nhưng trong mTLS/PKI doanh nghiệp, chi phí nằm ở **chuỗi chứng thư ký bằng ML-DSA** — nơi kích thước chữ ký và khoá công khai lớn hơn nhiều bậc so với ECDSA. Đây là khoảng trống có hệ quả vận hành trực tiếp (kích thước handshake, số vòng khứ hồi, giới hạn bộ đệm của thiết bị mạng).

### 1.3. Thiếu mô hình quyết định "di trú cái gì trước"
Tài liệu chuẩn hoá (NIST IR 8547 bản dự thảo, 2024) và khảo sát học thuật đã liệt kê rủi ro, nhưng tổ chức vẫn phải tự trả lời: *với một lưu lượng cụ thể, có nên bật hybrid PQC ngay bây giờ không, và nếu phải đánh đổi thì đánh đổi cái gì?* Chưa có mô hình công khai nào biến **rủi ro "thu-hoạch-ngay-giải-mã-sau" (harvest-now-decrypt-later — HNDL)** và **ngân sách độ trễ/băng thông** thành một thứ tự ưu tiên di trú kiểm chứng được.

---

## 2. Câu hỏi nghiên cứu

| Mã | Câu hỏi | Cách trả lời |
|---|---|---|
| **RQ1** | Chi phí bắt tay TLS 1.3 của hybrid `X25519MLKEM768` so với `X25519` thuần là bao nhiêu, đo trên nút biên, khi có ràng buộc MTU và middlebox? | Đo thực nghiệm có đối chứng, lặp lại N lần, báo cáo phân vị |
| **RQ2** | Kích thước chuỗi chứng thư ML-DSA ảnh hưởng thế nào tới số vòng khứ hồi và độ trễ bắt tay trong mTLS? | Ma trận thí nghiệm: độ dài chuỗi × thuật toán chữ ký × MTU |
| **RQ3** | Có thể mô hình hoá một chỉ số ưu tiên di trú cho từng lớp lưu lượng, kết hợp rủi ro HNDL và chi phí đo được, sao cho kết quả tái lập được không? | Xây mô hình điểm số; kiểm định độ nhạy (sensitivity analysis) |
| **RQ4** | Bao nhiêu phần trăm lưu lượng của một tổ chức điển hình có thể di trú "ngay" mà không vượt ngân sách độ trễ đã đặt ra? | Áp mô hình RQ3 lên một tập lưu lượng mẫu |

**Giả thuyết làm việc (cần kiểm chứng, KHÔNG được coi là kết quả):**
- **H1:** Trên nút biên, phần chi phí bắt tay tăng thêm của hybrid ML-KEM nằm trong khoảng chấp nhận được cho phần lớn lớp lưu lượng, và **nút thắt là kích thước bản ghi, không phải CPU**.
- **H2:** Với chuỗi chứng thư mTLS dài, ML-DSA gây thêm vòng khứ hồi ở một tỉ lệ MTU xác định, và tỉ lệ này dịch chuyển theo cấu hình mạng.
- **H3:** Tồn tại một ngưỡng trong mô hình điểm số mà dưới ngưỡng đó, việc trì hoãn di trú không làm tăng rủi ro HNDL một cách đáng kể.

> ⚠️ Ba giả thuyết trên là **dự đoán**, không phải kết quả. Kết quả thuộc về Reviewer1 sau khi có thực nghiệm.

---

## 3. Phương pháp

Thiết kế **ba pha**, mỗi pha có đầu ra kiểm chứng được.

### Pha P1 — Tổng quan tài liệu có hệ thống (2–3 tuần)
- Tuân theo quy trình `literature-review` của bộ skill `nckh`
  (`/home/noble-tran/agent-skills/skills/nckh/references/skills/literature-review/SKILL.md`).
- Truy vấn ghi lại nguyên văn; nguồn dùng: OpenAlex, CrossRef, RFC Editor, CSRC/NIST, arXiv.
- Tiêu chí gồm: (a) có đo lường thực nghiệm TLS/PQC, hoặc (b) có mô hình di trú PQC, hoặc (c) là văn bản chuẩn hoá. Tiêu chí loại: ý kiến không số liệu, không truy được DOI/URL.
- Đầu ra: ma trận claim ↔ nguồn, ghi rõ nguồn nào chỉ xác minh được metadata.

### Pha P2 — Đo lường có kiểm soát (6–10 tuần)
**Thiết kế thí nghiệm (sẽ được chốt lại bằng module `experimental-design` trước khi chạy):**

| Yếu tố | Mức |
|---|---|
| Nhóm trao đổi khoá | `X25519` · `X25519MLKEM768` |
| Nhóm chữ ký chứng thư | ECDSA P-256 · ML-DSA-44 · ML-DSA-65 · chuỗi hỗn hợp |
| Độ dài chuỗi chứng thư | 1 · 2 · 3 |
| MTU | 1500 · 1280 · 900 (mô phỏng đường hầm) |
| Nền tảng nút | x86_64 · ARM64 (nút biên) |
| Middlebox | không · có (thực thi tường lửa/bộ đệm giới hạn) |

- Số lần lặp mỗi ô: xác định bằng phân tích lực lượng thống kê (`statistical-power`) trước khi chạy — **con số sẽ được ghi vào đây sau khi tính**, không chốt bằng cảm tính.
- Thống kê: mô tả bằng trung vị + khoảng tin cậy bootstrap (dữ liệu độ trễ thường lệch, không dùng trung bình đơn thuần); so sánh bằng kiểm định phi tham số (Mann–Whitney U) và hiệu ứng kèm khoảng tin cậy; hiệu chỉnh đa so sánh.
- **Ghi chú đạo đức:** chỉ chạy trên testbed do nhóm sở hữu hoặc trên hạ tầng có uỷ quyền bằng văn bản. Không quét/đo hệ thống của bên thứ ba.

### Pha P3 — Mô hình quyết định (4–6 tuần)
- Đầu vào: rủi ro HNDL theo lớp lưu lượng (thời hạn bảo mật của dữ liệu) × chi phí đo được từ P2 × mức sẵn sàng của hệ sinh thái (thư viện, thiết bị).
- Đầu ra: điểm ưu tiên + ngưỡng hành động ("di trú ngay / di trú theo lộ trình / chờ").
- Kiểm định: phân tích độ nhạy theo từng trọng số; kiểm tra mô hình có ổn định khi đổi giả định.

### Tiêu chí thành công (định trước)
1. Có bộ dữ liệu đo lường thô, tái lập được bằng script công khai.
2. Mọi khẳng định định lượng có khoảng tin cậy.
3. Mô hình P3 tái tạo được kết quả từ dữ liệu P2 bằng một lệnh duy nhất.

---

## 4. Dữ liệu cần

| Nhóm dữ liệu | Mô tả | Nguồn | Trạng thái |
|---|---|---|---|
| D1 | Nhật ký bắt tay TLS (thời gian, kích thước bản ghi, số vòng khứ hồi) | Testbed tự dựng (P2) | Chưa có — phải tạo |
| D2 | Kích thước khoá/chữ ký/chứng thư theo thuật toán | Tài liệu chuẩn FIPS 203/204/205 + thư viện triển khai | Một phần công khai |
| D3 | Hành vi middlebox với ClientHello lớn | Testbed (P2) | Chưa có — phải tạo |
| D4 | Tiêu thụ CPU/năng lượng trên ARM64 | Testbed (P2) | Chưa có — phải tạo |
| D5 | Tập lưu lượng mẫu theo lớp (thời hạn bảo mật) | Tổ chức hợp tác, hoặc mô phỏng có khai báo | Rủi ro cao — xem §6 |

**Nguồn tham chiếu bổ sung cho thiết kế P2:** S31 (arXiv:2603.11006v2) là thiết kế gần nhất đã biết; nhóm **phải** đọc toàn văn và ghi rõ đề tài này khác gì về mặt thiết kế (biên, middlebox, MTU, chứng thư ML-DSA) **trước khi** thu thập dữ liệu.

**Nguyên tắc dữ liệu:** không dùng dữ liệu cá nhân thật; dữ liệu lưu lượng phải được ẩn danh hoá trước khi vào repo; không push chứng thư, khoá riêng, hay token thật.

---

## 5. Tính mới

1. **Bộ dữ liệu mở đo hybrid ML-KEM TLS 1.3 trên nút biên có middlebox và ràng buộc MTU, kèm script tái lập.**
   **Trạng thái bằng chứng (đã giải quyết ở vòng T19):** khoảng trống này nay được chứng minh là **CÒN MỞ** bằng **bằng chứng DƯƠNG**, không còn là suy luận từ việc "không tìm thấy".

   Nguồn gần nhất là **S31** — Gómez-Cambronero, Munteanu & González-Tablas (2026), *Layered Performance Analysis of TLS 1.3 Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange*, arXiv:2603.11006v2, **đã qua bình duyệt** tại SPIQE 2026 (gắn với Euro S&P 2026) theo trường `arxiv:comment`.
   Người đề xuất **đã tự tải và đọc toàn văn bản HTML** (`https://arxiv.org/html/2603.11006v2`, HTTP 200, **368.458 bytes**) và đếm từ khoá trên toàn văn:

   | Từ khoá | Số lần trong toàn văn S31 |
   |---|---|
   | `MTU` · `middlebox` · `fragment` · `packet size` · `network layer` · `certificate chain` · `tunnel` · `VPN` | **0 · 0 · 0 · 0 · 0 · 0 · 0 · 0** |
   | `edge` | 1 — nằm ở **99,5% độ dài văn bản**, tức **footer của arXiv**, không phải nội dung bài |
   | `MiTM` / `man-in-the-middle` | 2 / 2 |
   | `load balancer` | 2 |

   Và S31 **tự liệt kê đúng khoảng hở của đề tài này vào *future work***, trích nguyên văn:
   > *"extending the analysis to real network environments with commercial load balancers and MiTM (Man-in-The-Middle) inspection devices to quantify the performance impact when using PQC in TLS…"*

   ⇒ S31 bao phủ **phân tích theo tầng cho cổ điển/lai/thuần PQC** (phần lõi của hướng nghiên cứu), nhưng **KHÔNG** bao phủ: thiết bị trung gian, ràng buộc MTU/phân mảnh, lớp mạng, chuỗi chứng thư, đường hầm, hay biên thật. Đây chính là phần đề tài nhắm tới.
   **Bằng chứng thô:** `../EVIDENCE/T19_checks.txt` (mục VIỆC 2).
2. **Đo chi phí chứng thư ML-DSA trong mTLS nhiều tầng** — phần bị bỏ trống trong các nghiên cứu tập trung vào trao đổi khoá.
3. **Mô hình ưu tiên di trú kiểm chứng được**, nối rủi ro HNDL với chi phí đo được, thay vì khuyến nghị chung chung.

---

## 6. Rủi ro & đối sách

| # | Rủi ro | Khả năng | Tác động | Đối sách |
|---|---|---|---|---|
| R1 | Không tiếp cận được D5 (lưu lượng thật của tổ chức) | Cao | Trung bình | Chuyển sang lưu lượng mô phỏng có khai báo rõ; ghi rõ giới hạn ngoại suy |
| R2 | Thiết bị middlebox trong testbed không đại diện cho thiết bị thật trên thị trường | Trung bình | Cao | Khai báo rõ phạm vi; mời đối tác vận hành mạng kiểm chứng chéo |
| R3 | Chuẩn/thư viện PQC thay đổi giữa chừng làm kết quả lệch | Trung bình | Trung bình | Ghim phiên bản thư viện; ghi hash commit của thư viện vào metadata |
| R4 | Kết quả chỉ đúng trên một dòng CPU | Cao | Trung bình | Bắt buộc tối thiểu hai kiến trúc (x86_64 + ARM64) |
| R5 | Không huy động được tài trợ | Trung bình | Cao | Chạy được ở quy mô tối thiểu không cần tài trợ; tài trợ chỉ để mở rộng |
| R6 | **Rủi ro đạo đức:** kết quả đo có thể bị dùng để biện minh cho việc trì hoãn di trú | Thấp | Cao | Báo cáo phải kèm mục "giới hạn và điều kiện áp dụng"; không đưa khuyến nghị vượt quá dữ liệu |

---

## 7. Venue / nguồn tài trợ tiềm năng

> Tất cả mục dưới đây là **đề xuất**, chưa có cam kết nào từ các tổ chức được nêu. Không có thoả thuận tài trợ nào tồn tại tại thời điểm viết.

**Venue công bố (đề xuất):**
| Loại | Venue | Căn cứ |
|---|---|---|
| Hội nghị | IEEE/IFIP NOMS; IFIP Networking; ACM CoNEXT | Đã từng công bố công trình đo lường TLS PQC tương tự (xem `SOURCES.md` S10, S13) |
| Tạp chí | *Computer Networks*; *IEEE Access*; *IEEE Transactions on Network and Service Management* | Có tiền lệ công bố đo lường PQC TLS (S16) |
| Chuyên ngành mật mã | IACR Communications in Cryptology; PQCrypto | Có tiền lệ khảo sát post-quantum TLS (S9) |

**Nguồn tài trợ tiềm năng (chưa liên hệ):** NIST NCCoE (nhóm dự án di trú PQC); ENISA; quỹ nghiên cứu quốc gia; chương trình an ninh mạng cấp bộ; nhà cung cấp cloud/hạ tầng mạng; quỹ học thuật nội bộ trường.

---

## 8. Chi phí ước tính

**Đơn vị: người-tháng (person-month) — KHÔNG quy đổi ra tiền tệ vì người đề xuất không có bảng lương thực tế; mọi con số tiền tệ sẽ là bịa.**

| Hạng mục | Ước tính | Ghi chú |
|---|---|---|
| Nhân lực nghiên cứu | 9–14 người-tháng | P1: 2–3 · P2: 5–8 · P3: 2–3 |
| Hạ tầng testbed | 4–6 máy (2 kiến trúc) + 1 thiết bị mạng lập trình được | Chưa có báo giá — `chưa xác minh` |
| Lưu trữ dữ liệu | < 200 GB | Nhật ký bắt tay dạng văn bản |
| Chi phí truy cập tài liệu | Không xác định | Người đề xuất không có quyền truy cập CSDL trả phí (xem điểm yếu trong check-in) |
| Chi phí phiên dịch/hiệu đính | 1–2 người-tháng | Nếu công bố bằng tiếng Anh |

**Tổng nhân lực: 10–16 người-tháng.** Các con số tiền tệ: `chưa xác minh`.

---

## 9. Sản phẩm giao nộp

1. Bài báo hội nghị/tạp chí (bản thảo + bộ đôi dữ liệu–mã).
2. Kho dữ liệu mở: nhật ký bắt tay thô đã ẩn danh + metadata phiên bản.
3. Script tái lập một lệnh.
4. Báo cáo chính sách ngắn cho đơn vị vận hành mạng: "lộ trình di trú theo lớp lưu lượng".
5. `BLINDCHECK.md` đã được Reviewer1 điền (kiểm định độc lập).

---

## 10. Tự đánh giá thẳng thắn của người đề xuất

- Người đề xuất **không có** testbed mạng và **không có** quyền truy cập CSDL học thuật trả phí. Toàn bộ §3 (P2) là **thiết kế**, chưa có dữ liệu nào được sinh ra.
- Mọi con số trong §1.1 lấy từ **nguồn đã tải và đọc toàn văn** (Sikeridis 2020), có số dòng dẫn chứng trong `../EVIDENCE/quote_extracts.txt`.
- Người đề xuất **không tự kiểm định** đề xuất này. Việc đó thuộc Reviewer1.
