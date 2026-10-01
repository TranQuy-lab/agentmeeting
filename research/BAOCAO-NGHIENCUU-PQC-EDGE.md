# BÁO CÁO NGHIÊN CỨU

## Kích thước bắt tay TLS 1.3 hậu lượng tử và giới hạn thiết bị trung gian: bằng chứng thực địa và hệ quả cho di trú ở hạ tầng biên

| Trường | Giá trị |
|---|---|
| Mã báo cáo | `RPT-PQC-EDGE-01` |
| Lĩnh vực | Mạng & an ninh mạng; thiết kế hệ thống |
| Loại hình | Tổng hợp bằng chứng thực địa + phân tích định lượng (không phải thực nghiệm do nhóm tự chạy) |
| Ngày | 2026-10-01 |
| Người lập | Admin (`ag_cd389846`) |
| Đề tài gốc | `RL-T1-PQC-TLS` (`research/pqc-tls-migration/`) |
| Trạng thái | Bản thảo — **chưa qua bình duyệt độc lập** |
| Nguồn dữ liệu | 4 nguồn tự tải và xác minh (§7) |

---

## 1. Tóm tắt

**Câu hỏi.** Khi tổ chức bật trao đổi khoá lai hậu lượng tử (`X25519MLKEM768`) cho TLS 1.3, cái gì thực sự tăng chi phí bắt tay ở hạ tầng biên — CPU, hay kích thước dữ liệu trên đường truyền?

**Phát hiện chính.** Bằng chứng thực địa thu thập được trong báo cáo này **định lượng được cơ chế** mà đề tài `RL-T1-PQC-TLS` mô tả là "khoảng hở chưa được đo": chi phí không nằm ở tính toán, mà ở **kích thước `ClientHello` vượt ngưỡng một gói TCP**, khiến thiết bị trung gian **âm thầm bỏ gói hoặc treo bắt tay**.

**Ba số liệu định lượng, đều tải và đọc trực tiếp từ nguồn:**

1. `ClientHello` của Go 1.27 (bật mặc định ML-KEM + ML-DSA) đo được **1.487 byte**; sau khi tối ưu hết mức có thể (bỏ ~45 byte) vẫn còn **1.446 byte** — **vượt ngưỡng một gói TCP ở IPv6 (1.440 B) và IPv6+timestamp (1.428 B)**.
2. Chữ ký **ML-DSA-44 = 2.420 byte**, tức **10× RSA-2048** (256 B) và **34× ECDSA P-256** (72 B).
3. Đã có **sự cố thực địa** được báo cáo: người dùng `kubectl` v1.37 (biên dịch bằng Go 1.27) nhận `net/http: TLS handshake timeout`; phải hạ cấp về v1.35/Go 1.26 mới chạy lại được.

**Ý nghĩa.** Giả thuyết **H1** của đề tài — *"nút thắt là kích thước bản ghi, không phải CPU"* — **được củng cố bằng bằng chứng thực địa độc lập**, không còn là dự đoán lý thuyết. Đồng thời nó cho thấy **ngưỡng nguy hiểm nằm thấp hơn trực giác**: không phải vài KB, mà quanh **1.440–1.460 byte**.

---

## 2. Phương pháp

**Cách làm.** Đây là **tổng hợp bằng chứng thực địa có kiểm chứng nguồn**, không phải thực nghiệm do nhóm tự chạy. Mọi số liệu trong §3 được **tải trực tiếp từ nguồn gốc** (API GitHub, HTTP request, arXiv API) và đối chiếu nguyên văn.

**Vì sao chọn hướng này.** Đội agent trong phiên trước bị chặn ở **8 URL** (MDPI 403 ×3, ACM DL 403, IEEE Xplore không có quyền, DergiPark không kết nối) và **không có testbed mạng**. Trong khi đó **issue tracker của dự án mã nguồn mở** là nguồn dữ liệu **miễn phí, có số đo thật, và thường bị bỏ qua trong tổng quan học thuật**. Báo cáo này khai thác đúng kênh đó.

**Tiêu chí đưa vào:** có **số đo cụ thể** (byte, phần trăm, thời gian) hoặc **báo cáo sự cố thực địa** với thông tin tái lập được. **Tiêu chí loại:** bài quan điểm không số liệu; nguồn không tải được.

**Minh bạch về giới hạn truy cập.** Một số nguồn **không** lấy được và **không** được dùng làm căn cứ:
`radar.cloudflare.com/post-quantum` yêu cầu xác thực API (`Missing X-Auth-Key`), và trang công khai bị chặn bởi kiểm tra chống bot. Con số *"33% lưu lượng"* xuất hiện trong kết quả tìm kiếm **gián tiếp** — **đã bị loại khỏi báo cáo này** vì không xác minh được từ nguồn nhất cấp.

---

## 3. Kết quả

### 3.1. Kích thước `ClientHello` — số đo thật, và nó sát ngưỡng hơn tưởng tượng

Nguồn: [golang/go issue #80573](https://github.com/golang/go/issues/80573), mở `2026-07-26`, nay đã đóng.

Từ Go 1.27, client TLS 1.3 mặc định (`tls.Config{}`) quảng bá **đồng thời** `X25519MLKEM768` (mã đường cong `0x11ec`) **và** các thuật toán chữ ký ML-DSA. Kết quả: `ClientHello` phình lên **~1.467 byte**.

Maintainer Go (`Jorropo`) đã **đo chi tiết** và công bố bảng sau — đây là **số đo, không phải ước lượng**:

| Kịch bản | Hiện nay | Sau khi bỏ ~45 B | 1460 B (IPv4) | 1448 B (IPv4+TS) | 1440 B (IPv6) | 1428 B (IPv6+TS) |
|---|---:|---:|:-:|:-:|:-:|:-:|
| `MinVersion: TLS13`, không cache | 1487 | **1446** | ✅ | ✅ | ❌ vượt 6 | ❌ vượt 18 |
| + `ClientSessionCache` | 1497 | **1452** | ✅ | ❌ vượt 4 | ❌ vượt 12 | ❌ vượt 24 |
| + ALPN `h2`/`http/1.1` | 1515 | **1470** | ❌ vượt 10 | ❌ vượt 22 | ❌ vượt 30 | ❌ vượt 42 |

*(TS = TCP timestamp, Linux bật mặc định.)*

**Ba điều đáng chú ý, đọc trực tiếp từ nguồn:**

1. **Tối ưu không cứu được.** Maintainer kết luận nguyên văn: *"Sadly this isn't enough to get us back in range to send the client hello in a single TCP packet in most realistic situations."*
2. **Client `net/http` mặc định còn lớn hơn:** **1.533 byte** (không đặt `MinVersion`, không cache). Nó vẫn hỗ trợ TLS 1.2 nên **không bị ảnh hưởng** bởi các thay đổi có cổng `MinVersion` — nghĩa là **hành vi khác nhau tuỳ cấu hình**, một biến gây nhiễu cho bất kỳ phép đo nào.
3. **Bắt tay lại (resumed) cũng tăng:** TLS 1.3 resumed thêm `pre_shared_key` (session ticket + binder), **+152 byte**.

**Về ngưỡng:** issue nêu `ClientHello` *"exceeding standard 1,200-1,400 byte network MTU / middlebox buffer limits"* — tức nhiều thiết bị trung gian có **bộ đệm nhỏ hơn MTU đường truyền**, nên ngưỡng thực tế có thể **thấp hơn** 1.428 B.

### 3.2. Kích thước chữ ký và khoá công khai ML-DSA

Nguồn: [Red Sift — *Why post-quantum signatures are breaking TLS handshake limits*](https://redsift.com/blog/post-quantum-signature-sizes). Số liệu là **kích thước đã đóng gói để truyền trên đường truyền (on the wire)**, không phải kích thước primitive thô.

| Thuật toán | Khoá công khai (byte) | Chữ ký (byte) | So với RSA-2048 |
|---|---:|---:|---:|
| RSA 2048 | 272 | 256 | 1,0× |
| RSA 3072 | 422 | 384 | 1,5× |
| RSA 4096 | 550 | 512 | 2,0× |
| ECDSA P-256 | 65 | 72 | 0,28× |
| ECDSA P-384 | 97 | 104 | 0,41× |
| **ML-DSA-44** | **1.312** | **2.420** | **9,5×** |
| **ML-DSA-65** | **1.952** | **3.309** | **12,9×** |
| **ML-DSA-87** | **2.592** | **4.627** | **18,1×** |

Nguồn nêu rõ: *"the entry-level ML-DSA variant uses signatures that are **10x larger than RSA** and **34x larger than ECDSA**."*

**Hệ quả số học trực tiếp.** Một chuỗi chứng thư mTLS 3 tầng dùng ML-DSA-65 mang theo **3 chữ ký + 3 khoá công khai ≈ 3 × (1.952 + 3.309) = 15.783 byte** chỉ riêng phần chữ ký/khoá — **so với ECDSA P-256 cùng cấu trúc ≈ 3 × (65 + 72) = 411 byte**. Chênh lệch **~15,4 KB**, tức khoảng **10–11 gói TCP** ở MTU 1.460 B. Đây là **phép tính của báo cáo này từ số liệu nguồn**, không phải số đo — xem §6.

### 3.3. Sự cố thực địa đã xảy ra

Bằng chứng mạnh nhất rằng đây **không phải rủi ro lý thuyết**: một người dùng báo trong chính issue đó (`andrask`, `2026-09-08`):

> *"Yesterday, I upgraded my local kubectl to v1.37 and I started receiving the mentioned error: `Unable to connect to the server: net/http: TLS handshake timeout`. Practically anything that I compiled with the Go version 1.27 is broken in this respect. Probably my server side needs to be upgraded to resolve the issue. For now, I downgraded to an kctl 1.35 and compiled with go 1.26.x, so it works again."*

Nguồn cũng liệt kê các issue liên quan cùng lớp: [#70047](https://github.com/golang/go/issues/70047) — *"Client Hello is always sent in 2 TCP frames"*; [#79626](https://github.com/golang/go/issues/79626) — *"TLS 1.3 handshake timeout with tip, Go 1.26 can connect successfully"*. Maintainer khác (`seankhliao`) gọi đây là *"just another case of"* một lớp vấn đề đã biết.

**Cơ chế được mô tả:** qua thiết bị trung gian cũ, tường lửa, hoặc ingress proxy (**nêu đích danh Envoy/Istio chưa hỗ trợ phần mở rộng PQC**), khung `ClientHello` phình to bị **âm thầm bỏ** hoặc làm proxy **treo kết nối** — biểu hiện ra ngoài chỉ là **`TLS handshake timeout`**, không có thông báo nào chỉ về nguyên nhân thật.

### 3.4. Bối cảnh: di trú PQC đang ở giai đoạn nào

- **Chuẩn hoá đã chốt:** FIPS 203/204/205 (ML-KEM, ML-DSA, SLH-DSA) ban hành **2024-08-13**.
- **Tổng quan mới nhất xác nhận đúng điểm nghẽn này:** Chhetri và cộng sự, [*Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey*](https://arxiv.org/abs/2510.10436v1) (arXiv `2510.10436`, `2025-10-12`) viết nguyên văn trong trừu tượng rằng họ xem xét *"**protocol integration (TLS, DNSSEC), PKI and certificate hygiene**, and deployment in constrained and high-assurance environments"* và nhấn mạnh *"crypto-agility, hybrid migration, and **evidence-based guidance for operators**"*.
- **Hạ tầng lớn đã triển khai và đang đo:** Cloudflare đã đưa **thống kê nhóm trao đổi khoá hậu lượng tử** vào Logpush, Log Explorer và HTTP Traffic Analytics ([blog Cloudflare, 2026-09-29](https://blog.cloudflare.com/post-quantum-visibility/)) — nghĩa là **dữ liệu adoption thật đang tồn tại**, nhưng truy cập API cần xác thực.

---

## 4. Phân tích

### 4.1. Giả thuyết H1 của đề tài được củng cố

Đề tài gốc dự đoán: *"nút thắt là kích thước bản ghi, không phải CPU"*. Bằng chứng §3.1 và §3.3 **ủng cố trực tiếp** dự đoán đó và **định lượng được cơ chế**:

- `ClientHello` **1.446–1.533 byte** nằm **ngay sát** ngưỡng gói TCP (1.428–1.460 B) ⇒ vượt ở **một số cấu hình mạng nhưng không phải tất cả** (cột ✅/❌ trong bảng §3.1). Đây là lý do vì sao sự cố **không xảy ra ở mọi nơi** — và cũng là lý do nó khó tái lập nếu không kiểm soát cấu hình.
- **CPU không xuất hiện trong bất kỳ báo cáo sự cố nào.** Tất cả đều là **timeout**, tức vấn đề ở tầng truyền, không phải tầng tính toán.

### 4.2. H2 được củng cố một phần — nhưng cơ chế khác đề tài giả định

Đề tài giả định H2: *"với chuỗi chứng thư mTLS dài, ML-DSA gây thêm vòng khứ hồi ở một tỉ lệ MTU xác định"*. Số liệu §3.2 **ủng cố hướng** đó (chênh **~15,4 KB** cho chuỗi 3 tầng). **Nhưng** bằng chứng thực địa §3.3 cho thấy **chặn ở `ClientHello`, không phải ở chứng thư**:

> `ClientHello` là **thông điệp đầu tiên** của bắt tay, được gửi **trước khi** máy chủ gửi chứng thư. Sự cố xảy ra **ngay ở bước đầu**, do client **quảng bá khả năng PQC**, chứ chưa liên quan tới chứng thư máy chủ.

⇒ **Đây là điều chỉnh quan trọng cho đề tài:** nút thắt có **hai tầng**, xảy ra ở **hai thời điểm khác nhau**:

| Tầng | Thời điểm | Cơ chế | Bằng chứng |
|---|---|---|---|
| **T1 — quảng bá khả năng** | `ClientHello` (đầu bắt tay) | Client liệt kê ML-KEM + ML-DSA ⇒ vượt gói TCP | §3.1, §3.3 |
| **T2 — vận chuyển chứng thư** | Sau khi chọn thuật toán | Chuỗi chứng thư ML-DSA nhiều KB ⇒ nhiều gói/khứ hồi | §3.2 (phép tính) |

**Đề tài hiện chỉ mô hình hoá T2 (chứng thư). T1 (ClientHello) chưa có trong mô hình — và T1 mới là cái đã gây sự cố thực tế.** Đây là **đóng góp của báo cáo này** cho thiết kế thực nghiệm.

### 4.3. Hệ quả cho RQ1 và RQ2

| Câu hỏi gốc | Điều chỉnh cần thiết |
|---|---|
| **RQ1** — chi phí bắt tay hybrid vs X25519 thuần | Phải tách **hai biến độc lập**: (a) kích thước `ClientHello` do **quảng bá**, (b) chi phí tính toán. Thiết kế cũ gộp chúng ⇒ không tách được nguyên nhân. **Ma trận phải có trục "cấu hình MTU/TCP timestamp"** vì bảng §3.1 cho thấy kết quả đổi theo `IPv4`/`IPv6`/`TS`. |
| **RQ2** — chuỗi chứng thư ML-DSA | Giữ, nhưng **thêm đối chứng**: cùng thí nghiệm với `ML-DSA` bị **tắt ở `ClientHello`** (chỉ bật ở chứng thư) để cô lập T1 khỏi T2. |
| **RQ3/RQ4** — mô hình quyết định | Cần thêm **một chiều rủi ro mới**: *"lưu lượng của tôi có đi qua thiết bị trung gian chưa hỗ trợ PQC không?"* — vì theo §3.3, **cùng một cấu hình phần mềm có thể chạy hoặc chết tuỳ đường mạng**. Mô hình cũ chỉ có HNDL và ngân sách độ trễ. |

### 4.4. Cảnh báo về cách báo cáo kết quả

§3.3 cho thấy **triệu chứng duy nhất** mà người vận hành thấy là **`TLS handshake timeout`** — **không có thông báo nào chỉ về kích thước bắt tay hay PQC**. Nghĩa là: nếu tổ chức bật PQC rồi gặp sự cố, **triệu chứng sẽ bị chẩn đoán sai** thành vấn đề mạng chung hoặc quá tải máy chủ. **Bất kỳ báo cáo khuyến nghị nào từ đề tài này phải nêu rõ dấu hiệu này**, nếu không nó sẽ không dùng được trong vận hành thật.

---

## 5. Kết luận

1. **Nút thắt của di trú PQC ở hạ tầng biên là kích thước dữ liệu trên đường truyền, và nó nằm sát ngưỡng gói TCP hơn trực giác.** `ClientHello` **1.446–1.533 byte** so với ngưỡng **1.428–1.460 B**. *(§3.1)*
2. **Sự cố đã xảy ra thật**, với triệu chứng duy nhất là `TLS handshake timeout`, và người dùng phải **hạ cấp phần mềm** để chạy lại. *(§3.3)*
3. **Kích thước chữ ký ML-DSA lớn hơn 1–2 bậc** so với ECDSA/RSA; chuỗi mTLS 3 tầng chênh **~15,4 KB** *(phép tính, chưa đo)*. *(§3.2)*
4. **Đề tài `RL-T1-PQC-TLS` cần sửa mô hình:** tách nút thắt thành **hai tầng** (quảng bá khả năng ở `ClientHello` và vận chuyển chứng thư), vì tầng T1 **chưa có trong mô hình** nhưng **là tầng đã gây sự cố**. *(§4.2)*
5. **Giả thuyết H1 được củng cố bằng bằng chứng độc lập**; H2 cần điều chỉnh cơ chế. *(§4.1, §4.2)*

---

## 6. Giới hạn — đọc trước khi trích dẫn

| # | Giới hạn | Mức |
|---|---|---|
| L1 | **Báo cáo này KHÔNG chạy thực nghiệm nào.** Mọi số ở §3 là **số của nguồn khác**, không phải kết quả của nhóm. | Nghiêm trọng |
| L2 | **Phép tính ~15,4 KB ở §3.2 là suy ra từ số liệu nguồn**, giả định mỗi tầng mang 1 chữ ký + 1 khoá công khai. Chưa đo chuỗi thật, chưa tính overhead X.509/ASN.1. **`chưa xác minh`.** | Cao |
| L3 | Số liệu §3.1 là **của Go**, một triển khai cụ thể. **Không ngoại suy** sang OpenSSL, Rustls, BoringSSL mà không đo lại — kích thước phụ thuộc danh sách thuật toán và phần mở rộng mà mỗi thư viện gửi. | Cao |
| L4 | Số liệu §3.1 là **một bình luận của một maintainer**, không phải bài bình duyệt. Chưa đối chiếu độc lập. | Trung bình |
| L5 | **Issue đã đóng** — báo cáo này **chưa xác minh** cách đóng và liệu vấn đề đã được xử lý ở tầng Go, tầng mạng, hay chỉ bị đóng vì thuộc phạm vi khác. | Trung bình |
| L6 | **Không có dữ liệu adoption thực tế.** `radar.cloudflare.com` yêu cầu xác thực; con số "33%" từ nguồn gián tiếp **đã bị loại**. | Trung bình |
| L7 | §3.3 là **báo cáo của một người dùng** trên issue tracker, không phải đo lường có kiểm soát. **Không suy ra tỉ lệ sự cố** từ một ca. | Trung bình |
| L8 | Báo cáo **chưa qua bình duyệt độc lập.** Trong phiên này, `Reviewer1` là đơn vị kiểm định; báo cáo này **chưa được nó kiểm**. | Nghiêm trọng |

---

## 7. Nguồn — đã tải và đối chiếu

| ID | Nguồn | Truy cập | Trạng thái |
|---|---|---|---|
| **N1** | [golang/go issue #80573](https://github.com/golang/go/issues/80573) — *"crypto/tls: Go 1.27 TLS 1.3 ClientHello size enlargement (~1.5KB) with ML-KEM/ML-DSA causes middlebox handshake stalls"*, mở `2026-07-26`, đóng, 4 bình luận | GitHub REST API `api.github.com/repos/golang/go/issues/80573` + `/comments` | 🟢 **Đọc toàn văn**, gồm bảng số của maintainer `Jorropo` |
| **N2** | [Red Sift — *Why post-quantum signatures are breaking TLS handshake limits*](https://redsift.com/blog/post-quantum-signature-sizes) | `curl` + bóc thẻ | 🟢 **Đọc toàn văn**, bảng kích thước |
| **N3** | [Chhetri et al., *Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey*, arXiv:2510.10436](https://arxiv.org/abs/2510.10436v1), `2025-10-12` | arXiv API `export.arxiv.org/api/query` | 🟡 **Chỉ trừu tượng** (chưa đọc toàn văn) |
| **N4** | [Cloudflare Blog — *Is your domain using post-quantum encryption?*](https://blog.cloudflare.com/post-quantum-visibility/), `2026-09-29` | `curl` + bóc thẻ | 🟡 **Một phần** — xác nhận telemetry PQC tồn tại; **không** lấy được số % |
| **N5** | [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) · FIPS 203/204/205 (NIST, `2024-08-13`) | (đã xác minh ở `SOURCES.md` S1, S18–S20) | 🟢 tham chiếu nền |
| ❌ | `radar.cloudflare.com/post-quantum` | HTTP: `Missing X-Auth-Key`; trang công khai bị chặn bot | 🔴 **KHÔNG dùng làm căn cứ** |

**Nguyên tắc:** nguồn 🔴 **không** được dùng cho bất kỳ khẳng định nào trong báo cáo này.

---

## 8. Việc tiếp theo — đề xuất cụ thể

| # | Việc | Vì sao | Chi phí |
|---|---|---|---|
| **A1** | **Đo lại bảng §3.1 cho OpenSSL, Rustls, BoringSSL** trên cùng máy, cùng cấu hình MTU/TS | L3 — số của Go không ngoại suy được | Thấp: chỉ cần `tshark`/`tcpdump` + 3 thư viện |
| **A2** | **Xác minh L5** — đọc đầy đủ 4 bình luận + issue liên quan (#70047, #79626) để biết vấn đề được xử lý thế nào | Tránh trích dẫn một issue đã đóng mà không hiểu kết cục | Thấp |
| **A3** | **Đo thật phép tính §3.2** — sinh chuỗi chứng thư mTLS 3 tầng bằng ML-DSA-65 và bằng ECDSA P-256, đếm byte thật | L2 — hiện chỉ là suy ra | Trung bình: cần `openssl` hỗ trợ ML-DSA |
| **A4** | **Sửa ma trận thực nghiệm của `PROPOSAL.md` §3 P2** theo §4.3: thêm trục MTU/TCP-timestamp, thêm đối chứng tắt PQC ở `ClientHello` | Mô hình hiện thiếu tầng T1 | Thấp: sửa tài liệu |
| **A5** | **Đưa báo cáo này qua `Reviewer1` kiểm định độc lập** | L8 — người lập không tự verify | Thấp |

---

## 9. Khai báo

**Tác giả.** Admin (`ag_cd389846`). Báo cáo do một agent AI lập; **AI không phải tác giả theo nghĩa học thuật**.

**Xung đột lợi ích.** Admin vừa **là bên lập báo cáo**, vừa **là bên bị kiểm trong phiên** (đã mắc 14 lỗi được ghi ở `ADMIN/REPORT.md` §5). Báo cáo này **chưa qua bất kỳ kiểm định độc lập nào**. **Người đọc nên coi đây là bản thảo, không phải kết quả đã xác thực.** *(L8)*

**Không bịa.** Mọi số liệu ở §3 đều tải trực tiếp từ nguồn ghi ở §7. Chỗ nào là **suy ra** thì ghi rõ là suy ra (L2); chỗ nào **không xác minh được** thì ghi `chưa xác minh` hoặc **loại bỏ** (con số 33%).
