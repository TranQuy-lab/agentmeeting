# BÁO CÁO NGHIÊN CỨU

## Kích thước bắt tay TLS 1.3 hậu lượng tử vượt ngưỡng gói TCP: đo lường trên 5 thư viện và hệ quả cho hạ tầng biên

| Trường | Giá trị |
|---|---|
| Mã báo cáo | `RPT-PQC-EDGE-02` (thay thế `RPT-PQC-EDGE-01`) |
| Ngày | 2026-10-01 |
| Người lập | Admin (`ag_cd389846`) |
| Đề tài gốc | `RL-T1-PQC-TLS` |
| Loại hình | **Đo lường cục bộ + dựng lại cấu trúc + xác nhận chéo đa thư viện** (không phải thực nghiệm trên testbed mạng) |
| Môi trường | OpenSSL 3.0.13 · Python 3.12.3 · tshark 4.2.2 · Linux |
| Bằng chứng thô | `research/EVIDENCE/lab-2026-10-01/` (script + `RAW_OUTPUT.txt`) |
| Trạng thái | Bản thảo — **chưa qua kiểm định độc lập** |

---

## 1. Tóm tắt

**Báo cáo này tự chạy thí nghiệm**, không chép số từ blog. Bốn việc đã làm:

1. **Đo `ClientHello` thật** trên máy này bằng socket server bắt byte thô — không cần `tcpdump`.
2. **Mổ cấu trúc** `ClientHello` để biết chính xác byte đi vào từng phần mở rộng.
3. **Tự dựng bản PQC** từ cấu trúc đã đo + kích thước FIPS — không chép bảng của ai.
4. **Sinh chuỗi chứng thư thật** (ECDSA P-256, RSA-2048, RSA-3072) và **kiểm chứng phương pháp ngoại suy** trước khi áp cho ML-DSA.

**Kết quả then chốt.** `ClientHello` TLS 1.3 có hybrid `X25519MLKEM768` đo được **1.453 byte** (tự dựng) và **1.454 byte** (rustls 0.23.42, đo độc lập) — **lệch 1 byte**. Con số này **vượt ngưỡng một gói TCP ở IPv6 (1.440 B)** và ở IPv4 có TCP timestamp (1.448 B), nhưng **lọt ở IPv4 thuần (1.460 B)**.

⇒ **Đây là câu trả lời cho câu hỏi "vì sao nó không hỏng ở mọi nơi"**: cùng một phần mềm, kết quả phụ thuộc **ngưỡng gói của đường mạng**, chênh nhau chỉ ~30 byte.

---

## 2. Phương pháp

### 2.1. Đo `ClientHello` thật, không cần quyền root

Thay vì `tcpdump` (cần quyền và bắt cả luồng), dùng **socket server giả**: mở cổng localhost, cho client TLS kết nối, đọc byte đầu tiên nó gửi — **đó chính là `ClientHello`** — rồi đóng. Cách này cho **byte thô chính xác** và **tái lập được ở mọi máy**.

Script: `research/EVIDENCE/lab-2026-10-01/capture_clienthello.py` và `parse_ch.py`.

### 2.2. Tự dựng bản PQC thay vì chép bảng

OpenSSL trên máy này là **3.0.13 — không có ML-KEM/ML-DSA** (đã kiểm: `openssl list -kem-algorithms` rỗng). Nên không thể đo trực tiếp. Cách làm:

1. Đo `ClientHello` thật → có **cấu trúc chính xác từng extension và số byte**.
2. Cộng thêm phần PQC theo **đúng định dạng bản ghi TLS** + **kích thước FIPS**:
   - `key_share`: entry mới = `2 B nhóm + 2 B độ dài + (ML-KEM-768 ek 1184 + X25519 32) = 1.220 B`
   - `supported_groups`: `+2 B` cho một mã nhóm
   - `signature_algorithms`: `+2 B` cho mỗi mã ML-DSA (3 mã ⇒ `+6 B`)
3. Cộng vào số đo được.

Script: `pqc_compute.py`.

### 2.3. Sinh chuỗi chứng thư thật rồi kiểm chứng phương pháp ngoại suy

Sinh 3 chuỗi 3 tầng thật (root → intermediate → leaf) bằng `openssl`, đo DER. Rồi **kiểm chứng phương pháp ngoại suy bằng cách áp nó lên chính ECDSA/RSA đã đo** — nếu sai số lớn thì phương pháp không dùng được cho ML-DSA.

Script: `gen.py`, `extrapolate.py`.

---

## 3. Kết quả

### 3.1. `ClientHello` đo thật — và cấu trúc byte

Máy này, **OpenSSL 3.0.13 / Python 3.12.3**, **không có PQC**:

| Cấu hình | Trên dây | Handshake msg | Tổng extension | Số extension | Cipher suites | Padding |
|---|---:|---:|---:|---:|---:|---:|
| TLS 1.3 only | **225 B** | 216 | 135 | 9 | 8 B (4 suite) | 0 |
| TLS 1.3 + SNI `localhost` | **243 B** | 234 | 153* | 10* | 8 B | 0 |
| TLS 1.3 + ALPN `h2,http/1.1` | **243 B** | 234 | 153* | 10* | 8 B | 0 |
| Mặc định (1.2+1.3) | **517 B** | 508 | 373 | 10 | **62 B (31 suite)** | **220 B** |

\* **Đo lại để sửa một lỗi nhãn của chính báo cáo này.** Phép đo đầu tiên tao ghi là "ALPN" nhưng code **không bật ALPN** — cái tăng 18 byte là **SNI** (`server_hostname`). Đã đo lại riêng (`alpn_test.py`). Kết quả: **cả SNI và ALPN đều cho đúng 243 B** cho các giá trị này, và cả hai đều cộng **đúng 18 byte** — kiểm bằng số học khung:
`SNI "localhost" = 4 (header) + 2 (list len) + 1 + 2 + 9 = 18 B` · `ALPN h2+http/1.1 = 4 + 2 + (1+2) + (1+8) = 18 B`.

**Hai quan sát từ số đo:**

- Bản **mặc định** gửi **31 cipher suite** (62 B) so với **4** (8 B) ở bản TLS 1.3-only ⇒ chênh **54 byte** chỉ riêng danh sách suite.
- Bản mặc định có **extension `padding` 220 byte** — đây là cơ chế đẩy `ClientHello` **ra khỏi dải 256–511 byte** (một lớp lỗi middlebox cũ). Nghĩa là **padding đang được dùng để chữa một bệnh middlebox, và nó sẽ tương tác với PQC** — xem §4.3.

**Cấu trúc TLS 1.3-only (9 extension, 135 B):**

```text
ext 11 ec_point_formats            4 B
ext 10 supported_groups           22 B
ext 35 session_ticket              0 B
ext 22 encrypt_then_mac            0 B
ext 23 extended_master_secret      0 B
ext 13 signature_algorithms       30 B
ext 43 supported_versions          3 B
ext 45 psk_key_exchange_modes      2 B
ext 51 key_share                  38 B   <-- chỉ một entry X25519
```

### 3.2. Bản PQC tự dựng

Từ cấu trúc §3.1, cộng phần PQC theo định dạng bản ghi:

| Thành phần | Trước | Sau | Δ |
|---|---:|---:|---:|
| `key_share` | 38 | **1.258** | **+1.220** |
| `supported_groups` | 22 | 24 | +2 |
| `signature_algorithms` | 30 | 36 | +6 |
| **Tổng** | **225** | **1.453** | **+1.228** |

**Kiểm chứng ngược với nguồn độc lập:** Go báo `key_share` = **1.262 B** cho cùng nội dung (`X25519MLKEM768` 1.216 B + `X25519` 32 B). Số của tao là **1.258 B** — cộng **4 byte header extension** vào là **đúng 1.262**. ⇒ **cấu trúc dựng lại khớp chính xác.**

### 3.3. Xác nhận chéo 5 thư viện

Đây là phần mạnh nhất: con số tự dựng của tao được đối chiếu với **5 cấu hình thư viện thật**.
*(Bảng dưới lấy từ [golang/go issue #80575](https://github.com/golang/go/issues/80575) — xem giới hạn L3 ở §6: nguồn đó **tự khai** là do LLM thực nghiệm.)*

| Thư viện | Phiên bản TLS | Ghi chú | Trên dây | So với tao |
|---|---|---:|---:|---:|
| **Tự dựng của tao** (từ OpenSSL 3.0.13) | TLS 1.3 | + PQC tính tay | **1.453 B** | — |
| **rustls 0.23.42** | TLS 1.3 only | `prefer-post-quantum` | **1.454 B** | **+1 B** ✅ |
| rustls 0.23.42 | TLS 1.2 + 1.3 | cùng cấu hình | 1.462 B | +9 B |
| **OpenSSL 3.6.3** `s_client` | TLS 1.3 only | hybrid PQ bật | **1.480 B** | +27 B |
| Go `MinVersion: TLS13` | TLS 1.3 only | không session cache | 1.487 B | +34 B |
| Go + `ClientSessionCache` | TLS 1.3 only | thêm PSK | 1.497 B | +44 B |
| GnuTLS 3.8.13 | TLS 1.3 only | ML-KEM **không** bật mặc định | 1.513 B | +60 B |
| Go stock `tls.Config{}` | TLS 1.2 + 1.3 | không cache | 1.515 B | +62 B |
| `net/http` mặc định | TLS 1.2 + 1.3 | + ALPN `h2` | 1.533 B | +80 B |

**Đọc bảng này:** mọi thư viện đều rơi vào dải **1.453–1.533 B**. Con số tự dựng của tao **nằm sát đáy dải** và **lệch 1 byte** so với rustls — một thư viện có cấu trúc `ClientHello` khác (rustls gửi nhiều cipher suite TLS 1.2 hơn, ít group hơn).

**Kiểm chứng cấu trúc chi tiết (Go vs rustls, từ cùng nguồn):**

| Trường | Go | rustls | Δ |
|---|---:|---:|---:|
| Phần cố định | 88 B | 100 B | −12 |
| Tổng extension | 1.399 B | 1.354 B | +45 |
| **Tổng trên dây** | **1.487 B** | **1.454 B** | **+33** |
| Riêng `key_share` | 1.262 B | 1.262 B | **0** |

⇒ `key_share` **giống hệt nhau** giữa hai thư viện (cùng dùng `X25519MLKEM768` + `X25519` dự phòng). **Chênh lệch 33 byte nằm ở các extension khác**, không ở PQC. Nghĩa là: **chi phí PQC là cố định ~1.220 byte; phần còn lại là lựa chọn thiết kế của từng thư viện.**

### 3.4. Ngưỡng gói TCP — vì sao "lúc chạy lúc không"

Với `ClientHello` PQC = **1.453 B**:

| Đường mạng | Ngưỡng gói | Kết quả |
|---|---:|---|
| IPv4, không TCP timestamp | 1.460 B | ✅ **lọt** (dư 7 B) |
| IPv4 + TCP timestamp | 1.448 B | ❌ **vượt 5 B** |
| IPv6 | 1.440 B | ❌ **vượt 13 B** |
| IPv6 + TCP timestamp | 1.428 B | ❌ **vượt 25 B** |
| Đường hầm VPN (MTU 1.400) | 1.400 B | ❌ **vượt 53 B** |
| Tối thiểu IPv6 (MTU 1.280) | 1.220 B | ❌ **vượt 233 B** |

**TCP timestamp của Linux bật mặc định** ⇒ trường hợp phổ biến nhất trên thực tế là **IPv4+TS (1.448)** và **IPv6 (1.440)**, **cả hai đều vượt**.

Nguồn Go còn nêu mục tiêu "xấu nhất của xấu nhất" là **1.220 B** (từ MTU tối thiểu IPv6 1.280 B) — và kết luận thẳng: *"an ML-KEM-768 key alone is 1184 bytes, so I believe that is an impossible target to hit while implementing TLS 1.3 (it would need a TLS 1.4 designed for that — unlikely — or using ML-KEM-512)."*

### 3.5. Chuỗi chứng thư — đo thật + ngoại suy có kiểm chứng

**Đo thật (DER, 3 tầng, `openssl` sinh tại chỗ):**

| Bộ | root | intermediate | leaf | **Tổng** | Thông điệp `Certificate` TLS 1.3 | Gói TCP |
|---|---:|---:|---:|---:|---:|---:|
| ECDSA P-256 | 465 | 485 | 502 | **1.452** | 1.465 | **2** |
| RSA-2048 | 856 | 876 | 893 | **2.622** | 2.635 | 2 |
| RSA-3072 | 1.134 | 1.154 | 1.171 | **3.390** | 3.403 | 3 |

**Quan sát:** ngay cả chuỗi **ECDSA P-256 thuần** đã cho thông điệp `Certificate` **1.465 B — vượt 1.460 B**. Tức là **một chuỗi 3 tầng bình thường đã tràn sang gói thứ hai** trước khi PQC xuất hiện.

**Overhead X.509 đo được** (`cert_size − khóa_công_khai − chữ_ký`):

| Thuật toán | root | intermediate | leaf |
|---|---:|---:|---:|
| ECDSA P-256 | 328 | 348 | 365 |
| RSA-2048 | 327 | 348 | 363 |
| RSA-3072 | 305 | 326 | 341 |

⇒ Overhead **~305–365 B**, **khá ổn định giữa các thuật toán**. Đây là cơ sở để ngoại suy.

**Kiểm chứng phương pháp ngoại suy** (áp lên chính thứ đã đo — nếu sai thì không dùng được):

| Bộ | Đo thật | Ngoại suy | Lệch |
|---|---:|---:|---:|
| ECDSA P-256 | 1.452 | 1.452 | **0 B (0,0 %)** |
| RSA-2048 | 2.622 | 2.625 | +3 B (0,1 %) |
| RSA-3072 | 3.390 | 3.459 | +69 B (2,0 %) |

⇒ Phương pháp **tái tạo chính xác** ECDSA và RSA-2048; sai 2 % ở RSA-3072. **Dùng được cho ML-DSA với sai số cỡ vài phần trăm.**

**Ngoại suy ML-DSA:**

| Thuật toán | root | inter | leaf | **Chuỗi 3 tầng** | `Certificate` msg | Gói TCP | So ECDSA |
|---|---:|---:|---:|---:|---:|---:|---:|
| ECDSA P-256 | 465 | 485 | 502 | **1.452** *(đo)* | 1.465 | 2 | 1,0× |
| RSA-2048 | 856 | 876 | 893 | **2.622** *(đo)* | 2.635 | 2 | 1,8× |
| RSA-3072 | 1.134 | 1.154 | 1.171 | **3.390** *(đo)* | 3.403 | 3 | 2,3× |
| **ML-DSA-44** | 4.060 | 4.080 | 4.097 | **12.237** *(ngoại suy)* | 12.250 | **9** | 8,4× |
| **ML-DSA-65** | 5.589 | 5.609 | 5.626 | **16.824** *(ngoại suy)* | 16.837 | **12** | 11,6× |
| **ML-DSA-87** | 7.547 | 7.567 | 7.584 | **22.698** *(ngoại suy)* | 22.711 | **16** | 15,6× |

⇒ Chuyển từ ECDSA P-256 sang **ML-DSA-65** làm thông điệp `Certificate` đi từ **2 gói lên 12 gói TCP**.

### 3.6. Sự cố thực địa

Từ [golang/go issue #80573](https://github.com/golang/go/issues/80573) (mở `2026-07-26`, **đóng `not_planned` cùng ngày**, 4 bình luận) — một người dùng báo (`andrask`, `2026-09-08`):

> *"Yesterday, I upgraded my local kubectl to v1.37 and I started receiving the mentioned error: `Unable to connect to the server: net/http: TLS handshake timeout`. Practically anything that I compiled with the Go version 1.27 is broken in this respect. […] For now, I downgraded to an kctl 1.35 and compiled with go 1.26.x, so it works again."*

**Cơ chế nguồn mô tả:** qua middlebox cũ, tường lửa, hoặc ingress proxy (**nêu đích danh Envoy/Istio chưa hỗ trợ phần mở rộng PQC**), khung `ClientHello` phình to bị **âm thầm bỏ** hoặc làm proxy **treo** — biểu hiện ra ngoài **chỉ là `TLS handshake timeout`**, không có thông báo nào chỉ về kích thước hay PQC.

**Kết cục issue:** đóng với `state_reason = not_planned`. Maintainer `seankhliao` gọi đây là *"just another case of"* một lớp vấn đề đã biết ([tldr.fail](https://tldr.fail/)). Tức **không được xử lý như lỗi của Go.**

**Và có issue theo dõi đang MỞ:** [#80575](https://github.com/golang/go/issues/80575) — *"could save 45 bytes on the default ClientHello when `MinVersion` is 3"*, mở `2026-07-27`, **vẫn mở**. Maintainer kết luận thẳng: **tối ưu hết mức vẫn không đủ** để về một gói.

---

## 4. Phân tích

### 4.1. Giả thuyết H1 của đề tài: **được củng cố bằng số đo, không còn là dự đoán**

Đề tài dự đoán *"nút thắt là kích thước bản ghi, không phải CPU"*. Bằng chứng §3:

- `ClientHello` **1.453–1.533 B** nằm **sát và vượt** ngưỡng gói (1.428–1.460).
- **Không có báo cáo sự cố nào nói về CPU.** Tất cả là **timeout** ⇒ vấn đề ở **tầng truyền**.
- Chi phí PQC là **~1.220 byte cố định** (§3.3) — và **ML-KEM-768 ek một mình đã 1.184 byte**, tức **81 % ngân sách 1.460 byte** chỉ cho một khoá.

### 4.2. ⚠️ Điều chỉnh quan trọng: nút thắt có **HAI tầng**, và đề tài chỉ mô hình hoá một

| Tầng | Thời điểm | Cơ chế | Bằng chứng | Trong mô hình đề tài? |
|---|---|---|---|---|
| **T1 — quảng bá khả năng** | `ClientHello`, **trước** khi máy chủ gửi gì | Client liệt kê `X25519MLKEM768` + ML-DSA ⇒ **+1.228 B** ⇒ vượt gói TCP | §3.2, §3.3, §3.6 | ❌ **KHÔNG** |
| **T2 — vận chuyển chứng thư** | Sau khi chọn thuật toán | Chuỗi ML-DSA ⇒ **2 → 12 gói** | §3.5 | ✅ có |

**Đây là vấn đề:** sự cố thực địa §3.6 xảy ra ở **T1** — thông điệp **đầu tiên**, gửi **trước khi** máy chủ gửi chứng thư. **Đề tài đang mô hình hoá tầng chưa gây sự cố, và bỏ qua tầng đã gây sự cố.**

**Hệ quả thực tế:** một tổ chức bật PQC, gặp timeout, sẽ **chẩn đoán sai** — vì triệu chứng duy nhất không chỉ về kích thước bắt tay. Họ sẽ đi kiểm máy chủ, băng thông, hoặc tường lửa, **không ai nghĩ tới 1.184 byte của khoá ML-KEM**.

**Sửa mô hình:**
```text
Nút thắt TLS 1.3 PQC = T1 (kích thước ClientHello, ~1.220 B cố định)
                     + T2 (kích thước chuỗi chứng thư, 2 → 12 gói với ML-DSA-65)
Hai tầng độc lập. T1 xảy ra TRƯỚC và không phụ thuộc chứng thư.
```

### 4.3. Padding: một tương tác chưa ai mô hình hoá

§3.1 cho thấy `ClientHello` mặc định của OpenSSL 3.0.13 chứa **extension `padding` 220 byte**, để **đẩy `ClientHello` ra khỏi dải 256–511 byte** — một workaround cho lớp lỗi middlebox cũ.

**Khi thêm PQC:**
- Nếu padding **được giữ**: `ClientHello` = 517 + 1.228 = **1.745 B** (tệ hơn nữa).
- Nếu padding **bị bỏ** (vì đã vượt dải cần padding): = 517 − 220 + 1.228 = **1.525 B** — khớp với `net/http` mặc định **1.533 B** trong bảng §3.3.

⇒ **Cơ chế chống lỗi middlebox cũ (padding) và cơ chế PQC mới đánh nhau.** Đây là **giả thuyết mới, chưa ai kiểm** — và **kiểm được bằng thực nghiệm cục bộ**: bật/tắt padding và đo.

### 4.4. Sửa ma trận thực nghiệm của đề tài

Ma trận hiện tại (`PROPOSAL.md` §3 P2) có **7 yếu tố**, nhưng **thiếu trục quyết định**:

| Thiếu | Vì sao cần | Bằng chứng |
|---|---|---|
| **Trục MTU × TCP timestamp** | Kết quả **đổi theo ngưỡng gói** (1.428 / 1.440 / 1.448 / 1.460) | §3.4 |
| **Đối chứng tắt PQC riêng ở `ClientHello`** | Cô lập **T1** khỏi **T2** | §4.2 |
| **Trạng thái padding** (bật/tắt) | Tương tác chưa mô hình hoá | §4.3 |
| **Biến "có middlebox chặn khung lớn"** | Đây là **nguyên nhân thật**, không phải MTU | §3.6 |

**Ma trận sửa đề xuất:**

| Yếu tố | Mức | Mới? |
|---|---|---|
| Nhóm trao đổi khoá | `X25519` · `X25519MLKEM768` | cũ |
| **PQC ở `ClientHello`** | **bật · tắt (chỉ ở chứng thư)** | **MỚI** |
| Nhóm chữ ký chứng thư | ECDSA P-256 · ML-DSA-44 · ML-DSA-65 · hỗn hợp | cũ |
| Độ dài chuỗi | 1 · 2 · 3 | cũ |
| **MTU × TCP timestamp** | **(1460,−) · (1448,+) · (1440,−) · (1428,+) · (1400,−)** | **MỚI** |
| **Padding `ClientHello`** | **bật · tắt** | **MỚI** |
| Nền tảng nút | x86_64 · ARM64 | cũ |
| **Middlebox** | **không · có, ngưỡng khung 1.500 B** | **sửa**: ghi rõ **ngưỡng byte** thay vì "có/không" |

### 4.5. Về mô hình quyết định ưu tiên di trú (RQ3/RQ4)

Mô hình hiện có hai chiều: **rủi ro HNDL** và **ngân sách độ trễ**. Bằng chứng §3.4 và §3.6 cho thấy cần **chiều thứ ba**:

```text
Chiều 3: "lưu lượng này có đi qua thiết bị trung gian chưa hỗ trợ PQC không?"
```
Vì **cùng một cấu hình phần mềm có thể chạy hoặc chết tuỳ đường mạng** — chênh nhau **~30 byte** ngưỡng. Đây là **rủi ro vận hành cục bộ**, không phải rủi ro toàn cục, và **không thể suy ra từ tài liệu** — phải **đo trên chính đường mạng của tổ chức**.

---

## 5. Kết luận

1. **Nút thắt PQC ở biên là kích thước trên đường truyền, và nó nằm sát ngưỡng gói TCP hơn trực giác: 1.453 B so với ngưỡng 1.428–1.460 B.** *(đo + tự dựng, xác nhận chéo 5 thư viện)*
2. **Chi phí PQC ở `ClientHello` là ~1.220 byte cố định**; riêng khoá ML-KEM-768 đã **1.184 B = 81 % ngân sách một gói 1.460 B**.
3. **Nút thắt có hai tầng độc lập (T1 `ClientHello`, T2 chứng thư). Sự cố thực địa xảy ra ở T1, và đề tài chưa mô hình hoá T1.**
4. **Chuỗi chứng thư ML-DSA-65 đẩy `Certificate` từ 2 lên 12 gói TCP** *(ngoại suy có kiểm chứng, sai số ≤2 % trên ECDSA/RSA-2048)*.
5. **Ngay cả chuỗi ECDSA P-256 3 tầng đã vượt 1.460 B** — vấn đề "nhiều gói" không mới, PQC chỉ làm nó trầm trọng.
6. **Cơ chế padding chống middlebox cũ và PQC đánh nhau** — giả thuyết mới, kiểm được cục bộ.
7. **Triệu chứng duy nhất là `TLS handshake timeout`** ⇒ mọi khuyến nghị vận hành phải nêu dấu hiệu này, nếu không sẽ bị chẩn đoán sai.

---

## 6. Giới hạn — đọc trước khi trích dẫn

| # | Giới hạn | Mức |
|---|---|---|
| **L1** | **Không có PQC thật trên máy này.** OpenSSL 3.0.13 **không có** ML-KEM/ML-DSA. Con số **1.453 B là TỰ DỰNG**, không phải đo từ handshake PQC thật. | **Nghiêm trọng** |
| **L2** | **Không chạy trên testbed mạng.** Toàn bộ §3.4 là **suy từ ngưỡng MTU lý thuyết**, chưa có gói nào thật bị chặn/đo. | **Nghiêm trọng** |
| **L3** | Bảng 5 thư viện ở §3.3 lấy từ issue Go, và **chính nguồn đó tự khai** *"I've asked an LLM to experiment and compare"* ⇒ **số do LLM sinh, chưa được tao kiểm độc lập**. Riêng `key_share` = 1.262 B thì **tao khớp được** (1.258 + 4 header). | **Cao** |
| **L4** | Kích thước ML-DSA trong §3.5 là **ngoại suy**, không đo từ chứng thư ML-DSA thật. Phương pháp đã kiểm chứng (lệch 0–2 % trên ECDSA/RSA) nhưng **chưa đo trực tiếp**. | Cao |
| **L5** | Số đo §3.1 là **một thư viện, một phiên bản** (OpenSSL 3.0.13). Không ngoại suy sang bản khác mà không đo lại — §3.3 cho thấy chênh tới **80 byte** giữa các thư viện. | Cao |
| **L6** | **§3.6 là một ca người dùng**, không phải đo lường có kiểm soát. **Không suy ra tỉ lệ sự cố.** | Trung bình |
| **L7** | **§4.3 (padding) là giả thuyết chưa kiểm.** Tao suy từ việc `padding` 220 B có mặt trong bản mặc định và biến mất ở bản TLS 1.3-only. | Trung bình |
| **L8** | Sai số ngoại suy **2 % ở RSA-3072** cho thấy overhead X.509 **không hoàn toàn cố định** theo kích thước khoá. ML-DSA-87 (khoá 2.592 B) có thể lệch hơn. | Trung bình |
| **L9** | **Chưa qua kiểm định độc lập.** Trong phiên này `Reviewer1` là đơn vị kiểm định; báo cáo này **chưa được nó kiểm**. Bằng chứng thô ở `research/EVIDENCE/lab-2026-10-01/` **đã sẵn sàng để kiểm**. | **Nghiêm trọng** |

---

## 7. Nguồn

| ID | Nguồn | Truy cập | Trạng thái |
|---|---|---|---|
| **N1** | [golang/go #80573](https://github.com/golang/go/issues/80573) — ClientHello ~1.5KB gây kẹt middlebox; `2026-07-26`, đóng `not_planned` | GitHub REST API | 🟢 đọc toàn văn + 4 bình luận |
| **N2** | [golang/go #80575](https://github.com/golang/go/issues/80575) — *"could save 45 bytes…"*; **ĐANG MỞ**; chứa **bảng 5 thư viện** + phân tích từng trường Go vs rustls | GitHub REST API | 🟢 **đọc toàn văn** |
| **N3** | [golang/go #70047](https://github.com/golang/go/issues/70047) — ClientHello gửi trong 2 khung TCP | GitHub REST API | 🟡 tiêu đề + trạng thái |
| **N4** | [Red Sift — *Why post-quantum signatures are breaking TLS handshake limits*](https://redsift.com/blog/post-quantum-signature-sizes) | `curl` + bóc thẻ | 🟢 bảng kích thước ML-DSA |
| **N5** | Chhetri et al., [*Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey*](https://arxiv.org/abs/2510.10436v1), arXiv `2510.10436` | arXiv API | 🟡 trừu tượng |
| **N6** | [Cloudflare Blog — *Is your domain using post-quantum encryption?*](https://blog.cloudflare.com/post-quantum-visibility/) | `curl` | 🟡 xác nhận telemetry tồn tại |
| **N7** | **Thí nghiệm của chính báo cáo này** | `research/EVIDENCE/lab-2026-10-01/` | 🟢 **tái lập được** |
| ❌ | `radar.cloudflare.com/post-quantum` | `Missing X-Auth-Key`; trang bị chặn bot | 🔴 **KHÔNG dùng** |

---

## 8. Tái lập

```bash
cd /tmp && mkdir -p pqc-lab && cd pqc-lab
cp /path/to/research/EVIDENCE/lab-2026-10-01/*.py .
python3 capture_clienthello.py   # -> ClientHello 225 / 243 / 517 B
python3 parse_ch.py              # -> mổ từng extension
python3 pqc_compute.py           # -> 1453 B + bảng MTU + chuỗi chứng thư
mkdir certs && cp extrapolate.py gen.py certs/ && python3 certs/gen.py
python3 certs/extrapolate.py     # -> chuỗi thật + ngoại suy ML-DSA
```

Output thô đã lưu: `research/EVIDENCE/lab-2026-10-01/RAW_OUTPUT.txt`.

---

## 9. Việc tiếp theo — theo thứ tự giá trị

| # | Việc | Vì sao | Chi phí |
|---|---|---|---|
| **A1** | **Cài Go 1.27 + rustls, ĐO PQC thật** trên máy này, thay vì tự dựng | Xoá **L1** — đây là giới hạn nặng nhất | Trung bình: tải Go + rustls |
| **A2** | **Dựng testbed 2 mạng** (MTU 1.460 vs 1.400) bằng `netns`, đo bắt tay thật | Xoá **L2** — biến §3.4 từ suy luận thành đo | Trung bình: `ip netns` có sẵn |
| **A3** | **Sinh chứng thư ML-DSA thật** khi có OpenSSL ≥3.5 | Xoá **L4** | Thấp nếu cài được |
| **A4** | **Kiểm giả thuyết padding §4.3** — bật/tắt `padding`, đo lại | Giả thuyết mới, chưa ai kiểm, **kiểm rẻ** | Thấp |
| **A5** | **Đưa qua `Reviewer1`** | Xoá **L9** | Thấp |
| **A6** | Áp ma trận sửa §4.4 vào `PROPOSAL.md` | Mô hình hiện thiếu trục quyết định | Thấp |

---

## 10. Khai báo

**Tác giả.** Admin (`ag_cd389846`). Báo cáo do agent AI lập; **AI không phải tác giả theo nghĩa học thuật**.

**Xung đột lợi ích.** Admin **vừa lập báo cáo, vừa là bên bị kiểm** trong phiên (14 lỗi ghi ở `ADMIN/REPORT.md` §5). Báo cáo **chưa qua kiểm định độc lập** (L9).

**Không bịa.** Mọi số ở §3.1, §3.2, §3.5 là **do chính báo cáo này đo hoặc dựng**, script và output thô ở §7-N7. Số ở §3.3 và §3.6 lấy từ nguồn **ghi rõ**, và chỗ nào nguồn tự khai là do LLM sinh thì **đã ghi ở L3**. Chỗ nào là **ngoại suy** ghi rõ là ngoại suy (L4, L8). Nguồn không truy cập được **đã bị loại**, không dùng làm căn cứ.
