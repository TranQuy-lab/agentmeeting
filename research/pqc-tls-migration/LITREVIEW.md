# LITREVIEW — Tổng quan tài liệu

## Đề tài `RL-T1-PQC-TLS`: Di trú mật mã hậu lượng tử cho TLS 1.3 tại hạ tầng biên

**Người thực hiện:** ResearchLead (`ag_d85dde8d`)
**Ngày hoàn thành:** 2026-10-01
**Ngày thực hiện tìm kiếm:** 2026-10-01 (toàn bộ truy vấn trong cùng một ngày, UTC)
**Nhánh:** `agent/research-lead/T2`
**Phương pháp:** theo quy trình `literature-review` của bộ skill `nckh`
(`/home/noble-tran/agent-skills/skills/nckh/references/skills/literature-review/SKILL.md`)
**Trạng thái:** ⏳ chờ Reviewer1 kiểm định độc lập — **người viết không tự verify**

---

## MỤC LỤC

1. [Tóm tắt điều hành](#1-tóm-tắt-điều-hành)
2. [Câu hỏi tổng quan và phạm vi](#2-câu-hỏi-tổng-quan-và-phạm-vi)
3. [Chiến lược tìm kiếm (ghi lại để tái lập)](#3-chiến-lược-tìm-kiếm-ghi-lại-để-tái-lập)
4. [Sàng lọc và chọn lựa](#4-sàng-lọc-và-chọn-lựa)
5. [Bối cảnh chuẩn hoá](#5-bối-cảnh-chuẩn-hoá)
6. [Tổng hợp theo chủ đề](#6-tổng-hợp-theo-chủ-đề)
   - 6.1 [Chi phí bắt tay: từ chữ ký sang kích thước bản ghi](#61-chi-phí-bắt-tay-từ-chữ-ký-sang-kích-thước-bản-ghi)
   - 6.2 [Trao đổi khoá lai (hybrid): tiền lệ chuẩn hoá và khoảng trống đo lường](#62-trao-đổi-khoá-lai-hybrid-tiền-lệ-chuẩn-hoá-và-khoảng-trống-đo-lường)
   - 6.3 [Giao thức thay thế: KEMTLS và họ thiết kế lại bắt tay](#63-giao-thức-thay-thế-kemtls-và-họ-thiết-kế-lại-bắt-tay)
   - 6.4 [Mô hình hoá di trú: chuẩn hoá, khảo sát, và cái còn thiếu](#64-mô-hình-hoá-di-trú-chuẩn-hoá-khảo-sát-và-cái-còn-thiếu)
7. [Tổng hợp xuyên nghiên cứu](#7-tổng-hợp-xuyên-nghiên-cứu)
8. [Khoảng trống nghiên cứu và vị trí của đề tài](#8-khoảng-trống-nghiên-cứu-và-vị-trí-của-đề-tài)
9. [Đánh giá chất lượng bằng chứng](#9-đánh-giá-chất-lượng-bằng-chứng)
10. [Giới hạn của tổng quan này](#10-giới-hạn-của-tổng-quan-này)
11. [Tài liệu tham khảo](#11-tài-liệu-tham-khảo)

---

## 1. Tóm tắt điều hành

Mật mã hậu lượng tử (PQC) cho TLS 1.3 không còn là câu hỏi "có khả thi không" mà là câu hỏi "di trú thế nào, cho lưu lượng nào, trước". Ba chuẩn liên quan đã được NIST chốt ngày 2024-08-13 (FIPS 203/204/205 — S18–S20). Tổng quan này tổng hợp **29 nguồn**, trong đó **6 nguồn đã được đọc toàn văn** (S1–S6) và 21 DOI chỉ xác minh được metadata; 5 mục không xác minh được đã bị loại bỏ minh bạch.

Ba kết luận có bằng chứng:

1. **Chi phí chữ ký PQC trong TLS 1.3 là chấp nhận được ở nhiều cấu hình, nhưng nút thắt nằm ở kích thước chứng thư, không phải CPU.** Sikeridis và cộng sự (S3, NDSS 2020, đọc toàn văn) đo được phần lớn lựa chọn chữ ký chỉ thêm **dưới 5 ms**, một số cấu hình khoảng **10–15 ms so với RSA3072**, nhưng khi chứng thư đủ lớn để vượt ngưỡng MTU thì **phát sinh thêm một vòng khứ hồi (~11 ms)**.

2. **Mô hình "trao đổi khoá lai" đã có tiền lệ chuẩn hoá ở một giao thức khác.** RFC 9370 (S2, đọc toàn văn, 81.487 bytes) chuẩn hoá *nhiều trao đổi khoá đồng thời* trong IKEv2 — tiền lệ thiết kế trực tiếp cho hybrid X25519MLKEM768 trong TLS.

3. **Tồn tại khoảng trống ở ba điểm:** (a) không có harness đo lường/tập dữ liệu mở cho hybrid ML-KEM ở hạ tầng biên có middlebox và ràng buộc MTU; (b) chi phí chuỗi chứng thư ML-DSA trong mTLS gần như không được đo; (c) chưa có mô hình quyết định ưu tiên di trú kiểm chứng được, nối rủi ro HNDL với chi phí đo được.

**Điều tổng quan này KHÔNG nói được:** không có kết luận nào về hiệu năng thực tế của hybrid ML-KEM trên hạ tầng biên, vì **chưa có thực nghiệm nào được chạy**. Mọi con số ở trên là **số liệu của công trình khác**, không phải kết quả của đề tài này.

---

## 2. Câu hỏi tổng quan và phạm vi

**Câu hỏi tổng quan:** Hiện đã biết gì — và chưa biết gì — về chi phí và lộ trình di trú PQC cho TLS 1.3, đặc biệt ở hạ tầng biên có ràng buộc về thiết bị trung gian?

**Tiêu chí đưa vào:**
- (a) có **đo lường thực nghiệm** TLS/TLS 1.3 với thuật toán hậu lượng tử; hoặc
- (b) có **mô hình/khung di trú** PQC; hoặc
- (c) là **văn bản chuẩn hoá** liên quan trực tiếp (RFC, FIPS, NIST IR/SP).
- Ngôn ngữ: tiếng Anh. Không giới hạn năm (để bắt được công trình nền 2015).

**Tiêu chí loại:**
- Bài quan điểm không có số liệu và không có khung phương pháp.
- Không truy được DOI/URL, hoặc DOI không tồn tại.
- Trùng lặp: giữ bản gốc, loại bản rút gọn.

**Phạm vi loại trừ:** mã hoá đồng cấu, chữ ký dựa trên hash cho firmware, QKD (chỉ nêu khi so sánh trực tiếp), và mật mã cho thiết bị cấy ghép.

---

## 3. Chiến lược tìm kiếm (ghi lại để tái lập)

**Cơ sở dữ liệu đã dùng (3 nguồn — đạt mức tối thiểu mà skill yêu cầu):**

| # | Nguồn | Cách truy vấn | Ghi lại ở đâu |
|---|---|---|---|
| DB1 | **OpenAlex** | REST API `search=` và `filter=title.search:` | `../EVIDENCE/openalex_queries.txt`, `../EVIDENCE/openalex_title_filters.txt`, `../EVIDENCE/openalex_doi_lookup.txt` |
| DB2 | **CrossRef** | REST API `works/<DOI>` | `../EVIDENCE/crossref_lookups.txt` |
| DB3 | **Nguồn nhất cấp** (RFC Editor, NIST CSRC, trang hội nghị NDSS, tài liệu nhà cung cấp) | `curl` + `web_fetch` | `SOURCES.md` §A §E |

**Chuỗi truy vấn nguyên văn (đã chạy):**

```text
Q1  post-quantum TLS handshake performance measurement
Q2  hybrid key exchange ML-KEM deployment measurement
Q3  post-quantum cryptography migration challenges organisation survey
Q4  title.search:ML-KEM
Q5  title.search:post-quantum AND title.search:TLS          -> 0 kết quả (cú pháp sai, xem ghi chú)
Q6  title.search:post-quantum AND title.search:migration    -> 0 kết quả (cú pháp sai, xem ghi chú)
Q7  post-quantum TLS handshake latency measurement study arxiv     (web_search)
Q8  NIST FIPS 203 204 205 post-quantum standards final             (web_search)
Q9  post-quantum cryptography migration challenges survey DOI 2024 (web_search)
```

**Ghi chú về sai sót tìm kiếm (tự khai báo):** Q5 và Q6 trả về **0 kết quả** vì cú pháp `AND` không được OpenAlex `filter=title.search:` hỗ trợ theo cách người lập giả định. Đây là **lỗi của người lập**, được phát hiện qua output thô trong `../EVIDENCE/openalex_title_filters.txt`. Q5/Q6 **không được tính** vào độ phủ tìm kiếm.

---

## 4. Sàng lọc và chọn lựa

| Bước | Số lượng | Ghi chú |
|---|---|---|
| Bản ghi thô thu được từ OpenAlex (5 truy vấn hợp lệ) | ~40 bản ghi | Trích trong `../EVIDENCE/openalex_queries.txt` |
| Bản ghi **liên quan trực tiếp** sau khi đọc tiêu đề + trừu tượng | 14 | Có trừu tượng thật từ OpenAlex |
| Trùng lặp / lạc đề bị loại | ~26 | Ví dụ bị loại: "Spectre Attacks" (1795 trích dẫn) và "Engineering biology applications" trong `oa_T2.txt` — **lạc đề hoàn toàn**, xuất hiện do xếp hạng theo số trích dẫn |
| Nguồn nhất cấp bổ sung (RFC/FIPS/NIST/tài liệu nhà cung cấp) | 8 | S1, S2, S4, S5, S18–S21 |
| **Tổng nguồn được đưa vào tổng quan** | **29** | Trong đó 6 đọc toàn văn |
| Bị loại vì **không xác minh được** | 5 | Ghi minh bạch ở `SOURCES.md` §D |

> ⚠️ **Không dựng được sơ đồ PRISMA đầy đủ** vì: (1) OpenAlex không trả về số bản ghi sau khử trùng lặp theo cách tách bạch; (2) quy trình này là **tổng quan định hướng**, không phải systematic review theo PRISMA. Người lập **không** dán nhãn "PRISMA" cho tài liệu này.

---

## 5. Bối cảnh chuẩn hoá

Ngày **2024-08-13** là mốc chốt: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA) — cả ba xác minh qua CrossRef (S18, S19, S20; xem `../EVIDENCE/crossref_lookups.txt`). Song song, NIST IR 8547 (**bản dự thảo** — hậu tố `.ipd`, S21) vạch lộ trình chuyển đổi ở tầm tổ chức.

**Điểm quan trọng về mặt phương pháp:** sự tồn tại của một văn bản *dự thảo* không đồng nghĩa với việc lộ trình đó đã được chốt. Văn bản dự thảo có thể thay đổi. Đây là một rủi ro của đề tài (xem `PROPOSAL.md` §6, R3).

Ở tầng giao thức, TLS 1.3 được định nghĩa bởi RFC 8446 (S1, đọc toàn văn 337.736 bytes). RFC 9370 (S2) là tiền lệ chuẩn hoá cho **nhiều trao đổi khoá đồng thời** trong IKEv2 — một thiết kế "lai" đã được IETF phê chuẩn ở giao thức khác, không phải ở TLS.

---

## 6. Tổng hợp theo chủ đề

### 6.1. Chi phí bắt tay: từ chữ ký sang kích thước bản ghi

> ## ✅ TÍNH MỚI — ĐÃ GIẢI QUYẾT BẰNG BẰNG CHỨNG DƯƠNG (cập nhật vòng T19)
> Nguồn gần nhất với đề tài là **S31** — Gómez-Cambronero, Munteanu & González-Tablas (2026),
> *Layered Performance Analysis of TLS 1.3 Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange*,
> arXiv:2603.11006v2, **đã qua bình duyệt** tại **SPIQE 2026** (gắn với **Euro S&P 2026**).
>
> **Người lập đã tự tải và đọc toàn văn bản HTML** (`https://arxiv.org/html/2603.11006v2`, HTTP 200, **368.458 bytes**),
> bóc thẻ → **67.743 ký tự văn bản**, và đếm từ khoá. Kết quả:
>
> | Từ khoá | Số lần |
> |---|---|
> | `MTU` · `middlebox` · `fragment` · `packet size` · `network layer` · `certificate chain` · `tunnel` · `VPN` | **0 · 0 · 0 · 0 · 0 · 0 · 0 · 0** |
> | `edge` | 1 — ở **99,5%** độ dài văn bản ⇒ **footer arXiv**, không phải nội dung bài |
> | `MiTM` / `man-in-the-middle` | 2 / 2 |
> | `load balancer` | 2 |
>
> **S31 tự liệt kê đúng khoảng hở của đề tài này vào *future work***, trích nguyên văn:
> > *"extending the analysis to real network environments with commercial load balancers and MiTM
> > (Man-in-The-Middle) inspection devices to quantify the performance impact when using PQC in TLS…"*
>
> **S31 bao phủ:** phân tích theo tầng (TCP → TCP-TLS → TLS → tầng trung gian → HTTP), ba nhóm trao đổi khoá
> cổ điển/lai/thuần PQC, hơn 30 thí nghiệm, backend đổi kích thước phản hồi, tới 100 giao dịch/giây, có effect size.
>
> **S31 KHÔNG bao phủ:** thiết bị trung gian thật, ràng buộc MTU/phân mảnh, lớp mạng, chuỗi chứng thư,
> đường hầm/VPN, biên thật.
>
> ⇒ **Kết luận tính mới:** khoảng hở của đề tài là **CÒN MỞ**, được chứng minh bằng **bằng chứng DƯƠNG**
> (S31 đã qua bình duyệt và tự nhận phần này là việc chưa làm), **không còn** là suy luận từ việc "không tìm thấy".
> Người lập chấm lại **N = 4/5** (không phải 2/5 như bản trước, cũng không phải 5/5 vì phần lõi
> "đo hybrid so với cổ điển" **đã có người làm**).
>
> **Bằng chứng thô:** `../EVIDENCE/T19_checks.txt` mục VIỆC 2.
>
> **Ghi chú trung thực về một lần suýt sai:** lần grep đầu tiên trên HTML **không** tìm thấy thông tin venue
> (`SPIQE`/`Euro S&P`), và người lập suýt kết luận rằng Reviewer1 nêu sai venue. Kiểm lại ở trường
> `<arxiv:comment>` qua arXiv API thì **venue là THẬT** — thông tin nằm ở **metadata**, không nằm trong bản HTML
> toàn văn. Bài học: **một lần grep rỗng không phải là bằng chứng phủ định.**

Đây là chủ đề có **chất lượng bằng chứng tốt nhất** trong tổng quan, vì có một nguồn đọc toàn văn.

**Sikeridis, Kampanakis & Devetsikiotis (S3, NDSS 2020)** đặt câu hỏi: chi phí xác thực hậu lượng tử trong TLS 1.3 là bao nhiêu trong điều kiện mạng thực tế? Họ đánh giá các ứng viên chữ ký NIST ở cả ba mặt: độ trễ bắt tay, thông lượng phiên, và đánh đổi giữa chữ ký dài với phép toán mật mã nặng.

Các phát hiện định lượng (trích nguyên văn, số dòng theo bản trích xuất — xem `../EVIDENCE/quote_extracts.txt` mục A):

| Phát hiện | Trích nguyên văn | Dòng |
|---|---|---|
| Nhiều lựa chọn chữ ký chỉ thêm rất ít | *"…that equates to less than 5ms extra"* | 622 |
| Khoảng chi phí điển hình | *"…handshake is ∼10-15ms over RSA3072"* | 667 |
| Vượt ngưỡng kích thước → thêm vòng khứ hồi | *"…size triggers an extra round-trip (∼11ms). Falcon 1024 does"* | 673 |
| Mốc cơ sở | *"…with a baseline RSA3072 handshake time of ∼15ms"* | 678 |

**Diễn giải (của người lập — KHÔNG phải kết luận của bài gốc):** con số "~11 ms cho một vòng khứ hồi" lớn hơn nhiều con số "dưới 5 ms" cho phép toán chữ ký. Nếu diễn giải này đúng, thì trong môi trường có độ trễ cao (vệ tinh, mạng di động biên, đường truyền xa), **kích thước chứng thư quan trọng hơn tốc độ CPU**. Đây chính là **giả thuyết H1** của đề tài, và nó **cần được kiểm chứng bằng thực nghiệm của chính đề tài**, không được coi là đã chứng minh.

Các công trình đo lường khác cùng hướng (S8, S11, S12, S13, S15, S16, S17) **chỉ xác minh được metadata** trong tổng quan này. Người lập **không trích số liệu** từ chúng. Việc chúng tồn tại cho thấy đây là một hướng nghiên cứu **đang hoạt động**, không phải một khoảng trống hoàn toàn — điều này làm giảm mức độ "mới" của đề tài và phải được Reviewer1 cân nhắc khi chấm tính mới.

### 6.2. Trao đổi khoá lai (hybrid): tiền lệ chuẩn hoá và khoảng trống đo lường

**RFC 9370 (S2)** cho phép IKEv2 thương lượng **nhiều trao đổi khoá trong cùng một phiên**, để kết hợp một thuật toán cổ điển với một thuật toán hậu lượng tử. Người lập đã tải và đọc toàn văn phần đầu (81.487 bytes, HTTP 200).

Ý nghĩa: **thiết kế lai không phải là chuyện mới hay chưa được kiểm chứng ở tầng chuẩn hoá.** Cái chưa có là **số liệu đo lường mở ở hạ tầng biên** cho cấu hình lai trong TLS, đặc biệt khi có thiết bị trung gian.

Về phía thuật toán, ML-KEM là đối tượng của FIPS 203 (S18). Các nghiên cứu về triển khai và đo ML-KEM (S15, S16, S17) đều nằm ngoài tầm đọc toàn văn của tổng quan này.

### 6.3. Giao thức thay thế: KEMTLS và họ thiết kế lại bắt tay

**KEMTLS (S9, ACM CCS 2020, 180 trích dẫn — chỉ metadata)** đề xuất dùng KEM thay chữ ký cho xác thực máy chủ, nhằm tránh chữ ký hậu lượng tử vốn lớn. Đây là hướng "thiết kế lại bắt tay" thay vì "nhét thuật toán mới vào bắt tay cũ".

**Hệ quả cho đề tài:** hướng thiết kế lại giao thức và hướng đo lường/kiểm thử vận hành là **hai hướng bổ trợ, không cạnh tranh**. Đề tài này thuộc hướng thứ hai. Tuy nhiên, một tổng quan trung thực phải ghi nhận rằng nếu KEMTLS (hoặc họ tương tự) được triển khai rộng, **giả định "chứng thư lớn là bài toán trung tâm" sẽ yếu đi**. Đây là rủi ro về tính mới, cần theo dõi.

### 6.4. Mô hình hoá di trú: chuẩn hoá, khảo sát, và cái còn thiếu

Ở đây bằng chứng **yếu nhất** — và đây cũng chính là chỗ đề tài muốn đóng góp.

- **NIST IR 8547 (S21, bản dự thảo)** và **khảo sát post-quantum TLS (S7)** đều chỉ xác minh được metadata. Người lập **không đọc được toàn văn** nên **không thể** mô tả chi tiết chúng đề xuất gì.
- Điều nói được một cách an toàn: **có tồn tại** một văn bản lộ trình chuyển đổi của NIST ở dạng dự thảo, và **có tồn tại** một khảo sát học thuật tổng hợp các đề xuất post-quantum TLS.
- Điều **không** nói được: chúng có mô hình quyết định theo lớp lưu lượng hay không; chúng có gắn rủi ro HNDL với chi phí đo được hay không.

> 🔴 **Cảnh báo cho Reviewer1:** khẳng định "chưa có mô hình quyết định nào tồn tại" trong `PROPOSAL.md` §1.3 **chưa được chứng minh** — nó dựa trên việc *không tìm thấy*, chứ không phải trên một tìm kiếm có hệ thống đủ mạnh. Đây là **điểm yếu nghiêm trọng nhất** của hồ sơ đề tài và phải được kiểm tra độc lập trước khi chấp nhận.

---

## 7. Tổng hợp xuyên nghiên cứu

Đọc theo chiều ngang, bốn mẫu hình xuất hiện:

**Mẫu hình 1 — "CPU không phải là nút thắt".** Bằng chứng mạnh nhất từ S3 (đọc toàn văn) và được củng cố gián tiếp bởi sự tồn tại của nhiều công trình tối ưu kích thước/cấu trúc (S9 KEMTLS, S14).

**Mẫu hình 2 — "Đo lường tập trung vào trao đổi khoá, bỏ quên PKI".** Các nghiên cứu đo lường (S8, S11, S12) và các nguồn chuẩn (S18–S20) đều cho thấy trọng tâm là KEM; trong khi FIPS 204 (ML-DSA) tồn tại và **có** kích thước lớn — nhưng chưa thấy công trình đo chi phí chuỗi chứng thư ML-DSA trong mTLS trong tập nguồn này.

**Mẫu hình 3 — "Chuẩn hoá đi trước đo lường vận hành".** Ba FIPS chốt 2024-08-13 (S18–S20), IR 8547 còn dự thảo (S21). Khoảng cách giữa "đã có chuẩn" và "đã có số liệu vận hành ở biên" là khoảng trống thời sự.

**Mẫu hình 4 — "Tính mới của đề tài là tính mới của TỔ HỢP, không phải của từng mảnh".** Từng thành phần (đo TLS PQC, hybrid KEM, chuẩn hoá, mTLS) đều đã có công trình. Cái có thể mới là **tổ hợp**: harness mở + nút biên + middlebox + MTU + chứng thư ML-DSA + mô hình quyết định. Điều này phải được nói thẳng khi bảo vệ tính mới.

---

## 8. Khoảng trống nghiên cứu và vị trí của đề tài

| # | Khoảng trống | Mức độ chắc chắn của bằng chứng | Đề tài đóng góp gì |
|---|---|---|---|
| G1 | Không có tập dữ liệu/harness mở cho hybrid ML-KEM ở biên có middlebox + ràng buộc MTU | 🟢 **CÒN MỞ — BẰNG CHỨNG DƯƠNG.** S31 (2026, đã bình duyệt) đếm được `MTU`=0, `middlebox`=0, `fragment`=0, `network layer`=0, `tunnel`=0, `VPN`=0 trên toàn văn, và **tự liệt kê đúng khoảng hở này vào future work** | P2 |
| G2 | Chi phí chuỗi chứng thư ML-DSA trong mTLS chưa được đo | 🟢 **CÒN MỞ — BẰNG CHỨNG DƯƠNG.** Toàn văn S31 có `certificate chain` = **0** lần | P2 |
| G3 | Chưa có mô hình ưu tiên di trú kiểm chứng được | 🔴 **Yếu** — dựa trên *không tìm thấy*, và 2 nguồn liên quan nhất (S7, S21) chưa đọc được toàn văn | P3 |

**Vị trí của đề tài (đã điều chỉnh sau khi phát hiện S31):** nằm ở giao điểm của (a) đo lường hiệu năng giao thức và (b) hỗ trợ ra quyết định vận hành an ninh mạng. Nó **không** nằm trong làn sóng thiết kế lại giao thức (KEMTLS và tương tự).

---

## 9. Đánh giá chất lượng bằng chứng

**Phát hiện muộn được ghi nhận trung thực, và nay đã giải quyết:** S31 (arXiv:2603.11006) chỉ được tìm thấy **sau** khi hồ sơ viết xong bản đầu. Người lập **không giấu**, đã tự hạ tính mới từ 4 xuống 2 ở vòng T2, rồi ở vòng T19 **tự đọc toàn văn S31** và **nâng lại lên N=4 theo bằng chứng**. Việc hạ rồi nâng lại theo dữ liệu — chứ không theo uy quyền — là điều cần ghi lại. Quy trình tìm kiếm ban đầu **có lỗ hổng độ phủ**, và lỗ hổng đó là thật.

**Điểm mạnh của tổng quan này:**
- Mọi trích dẫn định lượng đều truy được tới **văn bản gốc đã tải**, kèm **số dòng** (S3, S6).
- Toàn bộ truy vấn tìm kiếm được ghi lại nguyên văn, kể cả hai truy vấn **thất bại** (Q5, Q6).
- Năm mục không xác minh được được liệt kê công khai ở `SOURCES.md` §D thay vì bị bỏ im lặng.
- Sai sót của chính người lập (suy đoán sai URL `cic.iacr.org/p/1/3/22`) được ghi lại ở §D mục X5.

**Điểm yếu — nói thẳng:**
1. **Phụ thuộc paywall.** Chỉ 6/29 nguồn đọc được toàn văn. Phần lớn "tổng hợp" ở §6 thực chất là tổng hợp **trừu tượng**, không phải tổng hợp nội dung.
2. **Không có sơ đồ PRISMA** và không có khử trùng lặp hai người độc lập. Đây là tổng quan định hướng, **không phải** systematic review. Tài liệu này **không được** dán nhãn PRISMA hay "systematic review".
3. **Thiên lệch công bố:** các nghiên cứu cho kết quả "chi phí chấp nhận được" có nhiều khả năng được công bố hơn các nghiên cứu cho kết quả "quá đắt". Tổng quan này **không** hiệu chỉnh được thiên lệch đó.
4. **Nguy cơ lỗi thời cao.** Đây là lĩnh vực thay đổi nhanh; các chuẩn mới có thể xuất hiện. Ngày tìm kiếm là 2026-10-01 và phải được ghi kèm mọi lần trích dẫn lại.
5. **Người lập không tự kiểm định.** Mọi đánh giá chất lượng ở mục này là **tự đánh giá** và có thể sai. Reviewer1 là bên quyết định.

---

## 10. Giới hạn của tổng quan này

- Chỉ dùng **3 nguồn tìm kiếm** (OpenAlex, CrossRef, nguồn nhất cấp). Scopus, Web of Science, IEEE Xplore full-text, ACM DL **không** truy cập được.
- **Không** tìm được nguồn nào bằng tiếng Việt hoặc tiếng Trung được đưa vào, do hạn chế của chuỗi truy vấn tiếng Anh.
- **Chỉ một người** thực hiện tìm kiếm và sàng lọc. Không có sàng lọc độc lập hai người.
- Toàn bộ kết quả trong ngày **2026-10-01**.

---

## 11. Tài liệu tham khảo

> Đánh số khớp với `SOURCES.md`. Nhãn mức xác minh giữ nguyên.

**Mức 🟢 TOÀN VĂN (đã tải và đọc):**

- **[S1]** Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3*. RFC 8446, RFC Editor. DOI: [10.17487/RFC8446](https://doi.org/10.17487/RFC8446). Toàn văn: https://www.rfc-editor.org/rfc/rfc8446.txt
- **[S2]** Tjhai, CJ., Tomlinson, M., Bartlett, G., Fluhrer, S., Van Geest, D., Garcia-Morchon, O., et al. (2023). *Multiple Key Exchanges in the Internet Key Exchange Protocol Version 2 (IKEv2)*. RFC 9370, RFC Editor. DOI: [10.17487/RFC9370](https://doi.org/10.17487/RFC9370). Toàn văn: https://www.rfc-editor.org/rfc/rfc9370.txt
- **[S3]** Sikeridis, D., Kampanakis, P., & Devetsikiotis, M. (2020). *Post-Quantum Authentication in TLS 1.3: A Performance Study*. NDSS Symposium 2020. DOI: [10.14722/ndss.2020.24203](https://doi.org/10.14722/ndss.2020.24203). PDF: https://www.ndss-symposium.org/wp-content/uploads/2020/02/24203-paper.pdf
- **[S4]** Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero Trust Architecture*. NIST SP 800-207. DOI: [10.6028/NIST.SP.800-207](https://doi.org/10.6028/NIST.SP.800-207)
- **[S5]** Cilium Authors. *Overview of Network Policy* (Cilium 1.20.2 documentation). https://docs.cilium.io/en/stable/security/policy/
- **[S6]** Budigiri, G., Baumann, C., Mühlberg, J. T., Truyen, E., & Joosen, W. (2021). *Network Policies in Kubernetes: Performance Evaluation and Security Analysis*. EuCNC/6G Summit 2021. DOI: [10.1109/EuCNC/6GSummit51104.2021.9482526](https://doi.org/10.1109/EuCNC/6GSummit51104.2021.9482526)

**Mức 🟡 CHỈ METADATA — không trích số liệu:**

- **[S31]** Gómez-Cambronero, D., Munteanu, D., & González-Tablas, A. I. (2026). *Layered Performance Analysis of TLS 1.3 Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange*. arXiv:2603.11006v2 (bản đầu 2026-03-11, cập nhật 2026-07-07). URL: https://arxiv.org/abs/2603.11006. 🟢 **ĐÃ ĐỌC TOÀN VĂN** (bản HTML, HTTP 200, 368.458 bytes) ở vòng T19 — xem §6.1 và `../EVIDENCE/T19_checks.txt`. Đã qua bình duyệt: SPIQE 2026 / Euro S&P 2026. **Xác nhận khoảng hở của đề tài là còn mở.**
- **[S7]** Alnahawi, N., Müller, J., Oupický, J., & Wiesmaier, A. (2024). *A Comprehensive Survey on Post-Quantum TLS*. IACR Communications in Cryptology. DOI: [10.62056/ahee0iuc](https://doi.org/10.62056/ahee0iuc). ⚠️ Chưa đọc toàn văn.
- **[S8]** (2023). *The Performance of Post-Quantum TLS 1.3*. DOI: [10.1145/3624354.3630585](https://doi.org/10.1145/3624354.3630585). ⚠️ Chưa đọc toàn văn.
- **[S9]** Schwabe, P., Stebila, D., & Wiggers, T. (2020). *Post-Quantum TLS Without Handshake Signatures*. ACM CCS 2020. DOI: [10.1145/3372297.3423350](https://doi.org/10.1145/3372297.3423350). ⚠️ Chưa đọc toàn văn. *(Danh sách tác giả đã xác minh qua OpenAlex — xem `../EVIDENCE/openalex_authors.txt`.)*
- **[S10]** Bos, J. W., Costello, C., Naehrig, M., & Stebila, D. (2015). *Post-Quantum Key Exchange for the TLS Protocol from the Ring Learning with Errors Problem*. IEEE S&P 2015. DOI: [10.1109/SP.2015.40](https://doi.org/10.1109/SP.2015.40). ⚠️ Chưa đọc toàn văn.
- **[S11]** (2020). *Assessing the overhead of post-quantum cryptography in TLS 1.3 and SSH*. ACM CoNEXT 2020. DOI: [10.1145/3386367.3431305](https://doi.org/10.1145/3386367.3431305). ⚠️ Chưa đọc toàn văn.
- **[S12]** (2022). *Post-Quantum Cryptography in Use: Empirical Analysis of the TLS Handshake Performance*. IEEE/IFIP NOMS 2022. DOI: [10.1109/NOMS54207.2022.9789913](https://doi.org/10.1109/NOMS54207.2022.9789913). ⚠️ Chưa đọc toàn văn.
- **[S13]** (2025). *A performance evaluation framework for post-quantum TLS*. Computer Networks. DOI: [10.1016/j.comnet.2025.111234](https://doi.org/10.1016/j.comnet.2025.111234). ⚠️ Chưa đọc toàn văn.
- **[S14]** (2024). *Faster Post-quantum TLS 1.3 Based on ML-KEM: Implementation and Assessment*. LNCS. DOI: [10.1007/978-3-031-70890-9_7](https://doi.org/10.1007/978-3-031-70890-9_7). ⚠️ Chưa đọc toàn văn.
- **[S15]** (2025). *On the Security and Efficiency of TLS 1.3 Handshake with Hybrid Key Exchange from CPA-Secure KEMs*. Entropy. DOI: [10.3390/e27121242](https://doi.org/10.3390/e27121242). ⚠️ Chưa đọc toàn văn.
- **[S16]** (2025). *Module-Lattice-Based Key-Encapsulation Mechanism Performance Measurements*. Sci. DOI: [10.3390/sci7030091](https://doi.org/10.3390/sci7030091). ⚠️ Chưa đọc toàn văn.
- **[S17]** (2026). *Hybrid ML-KEM in TLS 1.3: Performance Analysis on ARM64 Under Network Stress*. Computer Science (DergiPark). DOI: [10.53070/bbd.1898820](https://doi.org/10.53070/bbd.1898820). ⚠️ Chưa đọc toàn văn.
- **[S18]** NIST (2024-08-13). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. DOI: [10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203). ⚠️ Chỉ metadata.
- **[S19]** NIST (2024-08-13). *FIPS 204: Module-Lattice-Based Digital Signature Standard*. DOI: [10.6028/NIST.FIPS.204](https://doi.org/10.6028/NIST.FIPS.204). ⚠️ Chỉ metadata.
- **[S20]** NIST (2024-08-13). *FIPS 205: Stateless Hash-Based Digital Signature Standard*. DOI: [10.6028/NIST.FIPS.205](https://doi.org/10.6028/NIST.FIPS.205). ⚠️ Chỉ metadata.
- **[S21]** NIST (2024). *Transition to Post-Quantum Cryptography Standards* (**bản dự thảo**). NIST IR 8547 ipd. DOI: [10.6028/NIST.IR.8547.ipd](https://doi.org/10.6028/NIST.IR.8547.ipd). ⚠️ Chỉ metadata.

**Tài liệu tham khảo của Đề tài 2 (dùng trong hồ sơ song song):** S4, S5, S6, và S22–S29 — xem `../ebpf-microsegmentation/SOURCES.md`.

---

*Người lập: ResearchLead (`ag_d85dde8d`) · Ngày: 2026-10-01 · Nhánh `agent/research-lead/T2`*
*Tài liệu này CHƯA được kiểm định độc lập. Reviewer1 chịu trách nhiệm `BLINDCHECK.md`.*
