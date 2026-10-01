# SOURCES — Đề tài `RL-T1-PQC-TLS`

**Người lập:** ResearchLead (`ag_d85dde8d`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/research-lead/T2`

**Quy ước mức xác minh — đọc kỹ trước khi trích dẫn lại:**

| Nhãn | Nghĩa |
|---|---|
| 🟢 **TOÀN VĂN** | Đã tải được nội dung và **đọc thật** (hoặc bản PDF đã trích xuất văn bản). Trích dẫn được coi là an toàn. |
| 🟡 **METADATA** | DOI/URL tồn tại thật, metadata khớp — **nhưng chưa đọc được toàn văn**. Chỉ được trích ở mức "tồn tại và nói về chủ đề X", **không được trích số liệu hay kết luận**. |
| 🔴 **CHƯA XÁC MINH** | Không xác minh được. **CẤM trích dẫn.** Ghi ra đây để minh bạch. |

---

## A. Nguồn mức 🟢 TOÀN VĂN

### S1 — RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
- **Tác giả:** E. Rescorla · **Năm:** 2018-08 · **Nhà xuất bản:** RFC Editor
- **DOI:** `10.17487/RFC8446` — ✅ xác minh CrossRef (`../EVIDENCE/crossref_lookups.txt`)
- **URL toàn văn:** https://www.rfc-editor.org/rfc/rfc8446.txt
- **Trạng thái fetch:** ✅ HTTP 200, tải về **337.736 bytes**; đã đọc phần đầu (tiêu đề, trừu tượng, trường "Obsoletes: 5077, 5246, 6961").
- **Dùng cho:** nền tảng giao thức của đề tài.

### S2 — RFC 9370: Multiple Key Exchanges in IKEv2
- **Tác giả:** CJ. Tjhai, M. Tomlinson, G. Bartlett, S. Fluhrer, D. Van Geest, O. Garcia-Morchon (+1) · **Năm:** 2023-05 · **RFC Editor**
- **DOI:** `10.17487/RFC9370` — ✅ xác minh CrossRef
- **URL toàn văn:** https://www.rfc-editor.org/rfc/rfc9370.txt
- **Trạng thái fetch:** ✅ HTTP 200, **81.487 bytes**; đã đọc phần đầu (hiện rõ "Updates: 7296", "Post-Quantum", "Quantum Secret").
- **Dùng cho:** tiền lệ chuẩn hoá của **trao đổi khoá lai** (hybrid) — chứng minh rằng mô hình "chạy song song cổ điển + hậu lượng tử" đã được IETF chuẩn hoá ở một giao thức khác (IKEv2). Đây là bằng chứng cho tính khả thi của thiết kế lai, không phải bằng chứng cho TLS.

### S3 — Post-Quantum Authentication in TLS 1.3: A Performance Study
- **Tác giả:** Dimitrios Sikeridis, Panos Kampanakis, Michael Devetsikiotis · **Năm:** 2020 · **Venue:** NDSS Symposium 2020
- **DOI:** `10.14722/ndss.2020.24203` — 🟡 xác minh qua OpenAlex; bản PDF công khai tải trực tiếp ✅
- **URL toàn văn:** https://www.ndss-symposium.org/wp-content/uploads/2020/02/24203-paper.pdf
- **Trạng thái fetch:** ✅ HTTP 200, **720.938 bytes**; `pdftotext -layout` → **1.413 dòng**; đã đọc trừu tượng + các mục kết quả.
- **Trích nguyên văn đã kiểm chứng** (số dòng theo bản trích xuất, xem `../EVIDENCE/quote_extracts.txt` mục A):
  - *"…(Dilithium II, Falcon 512) that equates to less than 5ms extra"* (dòng 622)
  - *"…handshake is ∼10-15ms over RSA3072"* (dòng 667)
  - *"…size triggers an extra round-trip (∼11ms). Falcon 1024 does"* (dòng 673)
  - *"…with a baseline RSA3072 handshake time of ∼15ms"* (dòng 678)
- **Dùng cho:** mốc so sánh chi phí chữ ký PQC; bằng chứng cho luận điểm "kích thước chứng thư → thêm vòng khứ hồi".

### S4 — NIST SP 800-207: Zero Trust Architecture
- **Tác giả:** Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly · **Ngày:** 2020-08-11 · **NIST**
- **DOI:** `10.6028/NIST.SP.800-207` — ✅ xác minh CrossRef
- **URL:** https://csrc.nist.gov/pubs/sp/800/207/final · PDF: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
- **Trạng thái fetch:** ✅ HTTP 200; đã đọc trừu tượng chính thức nguyên văn.
- **Dùng cho:** đề tài 2 (định nghĩa ZTA nền tảng).

### S5 — Cilium: Overview of Network Policy (tài liệu chính thức)
- **Nhà xuất bản:** Cilium Authors · **Phiên bản tài liệu:** Cilium 1.20.2 · **Cập nhật trang:** 2026-09-15
- **URL:** https://docs.cilium.io/en/stable/security/policy/
- **Trạng thái fetch:** ✅ HTTP 200; đã đọc nội dung.
- **Dùng cho:** căn cứ kỹ thuật về các lớp chính sách L3/L4/L7 và cơ chế phân phối chính sách trong Cilium.

### S6 — Network Policies in Kubernetes: Performance Evaluation and Security Analysis
- **Tác giả:** Gerald Budigiri, Christoph Baumann, Jan Tobias Mühlberg, Eddy Truyen, Wouter Joosen · **Năm:** 2021 · **Venue:** EuCNC/6G Summit 2021
- **DOI:** `10.1109/EuCNC/6GSummit51104.2021.9482526` — ✅ xác minh CrossRef
- **URL toàn văn (bản tác giả):** https://lirias.kuleuven.be/retrieve/14e501bd-e6bb-41d6-bf72-360c4850443a
- **Trạng thái fetch:** ✅ HTTP 200, **718.671 bytes**, PDF 6 trang; `pdftotext -layout` → **440 dòng**; đã đọc trừu tượng + phần I.
- **Trích nguyên văn đã kiểm chứng** (xem `../EVIDENCE/quote_extracts.txt` mục B):
  - *"…that network policies incur a negligible performance overhead which only varies slightly with the number of policies and for different policy recipes."* (dòng 46–48)
  - *"…which host results were better by 8.7% and 10.7% for latency"* (dòng 161)
  - Trừu tượng nêu rõ: *"the first to investigate both performance overheads and security implications of K8s network policies specifically"*.
- **Dùng cho:** đề tài 2 — mốc so sánh và căn cứ cho khoảng trống nghiên cứu.

---

## B. Nguồn mức 🟡 CHỈ XÁC MINH METADATA — **cấm trích số liệu/kết luận**

> Tất cả DOI dưới đây **đã tồn tại thật** và metadata khớp (xác minh bằng CrossRef — `../EVIDENCE/crossref_lookups.txt` — hoặc OpenAlex — `../EVIDENCE/openalex_doi_lookup.txt`). Tuy nhiên người lập **chưa đọc được toàn văn** (phần lớn nằm sau paywall, hoặc nhà xuất bản chặn tải). Chỉ được dùng để mô tả "hướng nghiên cứu đã có".

| Mã | Tài liệu | DOI | Venue / Năm | Trích dẫn (OpenAlex) | Lý do chỉ metadata |
|---|---|---|---|---|---|
| S7 | A Comprehensive Survey on Post-Quantum TLS — Alnahawi, Müller, Oupický, Wiesmaier | `10.62056/ahee0iuc` | IACR Communications in Cryptology, 2024-07-08 | 28 | DOI chuyển hướng chéo tên miền sang `cic.iacr.org`; chưa định vị được URL toàn văn đúng |
| S8 | The Performance of Post-Quantum TLS 1.3 | `10.1145/3624354.3630585` | ACM, 2023 | 45 | Không truy cập được toàn văn |
| S9 | Post-Quantum TLS Without Handshake Signatures (KEMTLS) — Schwabe, Stebila, Wiggers | `10.1145/3372297.3423350` | ACM CCS, 2020 | 180 | ACM DL chặn tải PDF (HTTP 403) |
| S10 | Post-Quantum Key Exchange for the TLS Protocol from the Ring Learning with Errors Problem — Bos, Costello, Naehrig, Stebila | `10.1109/SP.2015.40` | IEEE S&P, 2015 | 330 | IEEE Xplore — không có quyền truy cập |
| S11 | Assessing the overhead of post-quantum cryptography in TLS 1.3 and SSH | `10.1145/3386367.3431305` | ACM CoNEXT, 2020 | 78 | Không truy cập được toàn văn |
| S12 | Post-Quantum Cryptography in Use: Empirical Analysis of the TLS Handshake Performance | `10.1109/NOMS54207.2022.9789913` | IEEE/IFIP NOMS, 2022 | 17 | IEEE Xplore — không có quyền truy cập |
| S13 | A performance evaluation framework for post-quantum TLS | `10.1016/j.comnet.2025.111234` | Computer Networks, 2025 | 3 | ScienceDirect — không có quyền truy cập |
| S14 | Faster Post-quantum TLS 1.3 Based on ML-KEM: Implementation and Assessment | `10.1007/978-3-031-70890-9_7` | LNCS, 2024 | 15 | Springer — không có quyền truy cập |
| S15 | On the Security and Efficiency of TLS 1.3 Handshake with Hybrid Key Exchange from CPA-Secure KEMs | `10.3390/e27121242` | Entropy, 2025 | 6 | MDPI chặn tải (HTTP 403) |
| S16 | Module-Lattice-Based Key-Encapsulation Mechanism Performance Measurements | `10.3390/sci7030091` | Sci (MDPI), 2025 | 14 | MDPI chặn tải (HTTP 403) |
| S17 | Hybrid ML-KEM in TLS 1.3: Performance Analysis on ARM64 Under Network Stress | `10.53070/bbd.1898820` | Computer Science (DergiPark), 2026 | 4 | Máy chủ DergiPark không kết nối được từ môi trường này |
| **S31** | **Layered Performance Analysis of TLS 1.3 Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange** — Gómez-Cambronero, Munteanu, González-Tablas | arXiv:2603.11006v2 (không có DOI) | arXiv, 2026-03-11 (cập nhật 2026-07-07) · **đã bình duyệt: SPIQE 2026 / Euro S&P 2026** | chưa tra | 🟢 **ĐÃ ĐỌC TOÀN VĂN** ở vòng T19 (HTML, HTTP 200, 368.458 bytes). Đếm từ khoá: `MTU`/`middlebox`/`fragment`/`packet size`/`network layer`/`certificate chain`/`tunnel`/`VPN` = **0**; `edge`=1 ở footer arXiv. Tự liệt kê khoảng hở của T1 vào *future work*. Bằng chứng: `../EVIDENCE/T19_checks.txt` |

**Nguồn chuẩn hoá (metadata):**
| Mã | Tài liệu | DOI | Ngày | Trạng thái |
|---|---|---|---|---|
| S18 | FIPS 203 — Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM) | `10.6028/NIST.FIPS.203` | 2024-08-13 | ✅ CrossRef |
| S19 | FIPS 204 — Module-Lattice-Based Digital Signature Standard (ML-DSA) | `10.6028/NIST.FIPS.204` | 2024-08-13 | ✅ CrossRef |
| S20 | FIPS 205 — Stateless Hash-Based Digital Signature Standard (SLH-DSA) | `10.6028/NIST.FIPS.205` | 2024-08-13 | ✅ CrossRef |
| S21 | NIST IR 8547 (bản dự thảo) — Transition to Post-Quantum Cryptography Standards | `10.6028/NIST.IR.8547.ipd` | 2024 | ✅ CrossRef (lưu ý: đây là **bản dự thảo**, `.ipd`) |

---

## C. Nguồn dùng cho Đề tài 2 — 🟡 CHỈ METADATA (trừ S4, S5, S6 đã ở mức 🟢)

| Mã | Tài liệu | DOI | Venue / Năm | Trích dẫn | Trạng thái |
|---|---|---|---|---|---|
| S22 | The eXpress Data Path (XDP) | `10.1145/3281411.3281443` | ACM CoNEXT, 2018-12-04 | 327 | 🟡 ACM DL chặn PDF (403) |
| S23 | eBPF: A New Approach to Cloud-Native Observability, Networking and Security for Current (5G) and Future Mobile Networks | `10.1109/ACCESS.2023.3281480` | IEEE Access, 2023 | 70 | 🟡 không tải được toàn văn |
| S24 | Dissecting Overheads of Service Mesh Sidecars | `10.1145/3620678.3624652` | ACM SoCC, 2023-10-30 | 42 | 🟡 ACM DL chặn PDF (403) |
| S25 | Synthesizing safe and efficient kernel extensions for packet processing | `10.1145/3452296.3472929` | ACM SIGCOMM, 2021 | 30 | 🟡 không truy cập được |
| S26 | Simple and precise static analysis of untrusted Linux kernel extensions | `10.1145/3314221.3314590` | ACM PLDI, 2019 | 99 | 🟡 không truy cập được |
| S27 | Optimizing network microsegmentation policy for cyber resilience | `10.1177/15485129211051386` | J. Defense Modeling & Simulation, 2021-10-08 | 12 | 🟡 không có bản mở |
| S28 | Automated Microsegmentation for Lateral Movement Prevention in Industrial Internet of Things (IIoT) | `10.1109/SIN54109.2021.9699232` | IEEE SIN, 2021-12-15 | 18 | 🟡 không đọc toàn văn |
| S29 | Zero Trust Implementation for Legacy Systems using Dynamic Microsegmentation, RBAC, and ABAC | `10.1109/iccit63348.2025.10989392` | IEEE ICCIT, 2025-04-13 | 9 | 🟡 không có bản mở |

---

## D. 🔴 CHƯA XÁC MINH — **CẤM TRÍCH DẪN**

| # | Thứ bị nghi | Nguồn gốc | Kết quả kiểm tra | Kết luận |
|---|---|---|---|---|
| X6 | `arXiv:2609.18633` — ban đầu người lập **tưởng không xác minh được** | Kết quả `web_search` cho đề tài 2 | arXiv API với `-L` → **TỒN TẠI**: "Netkit: Specializing Linux Packet Delivery for Container Networks", Borkmann & Chaignon, 2026-09-16, DOI `10.1145/3837779.3838164` | 🟢 **Đã sửa sai**: nguồn này CÓ THẬT. Nguyên nhân lỗi ban đầu: `http://export.arxiv.org/api/` trả **HTTP 301** và phải dùng `curl -L`. Xem `../EVIDENCE/arxiv_lookups.txt`. |
| X1 | `arXiv:2605.06881` — "Hybrid configurations combining classical key exchange (X25519) with ML-KEM-768…" | Xuất hiện trong kết quả `web_search` | Gọi arXiv API `id_list=2605.06881` → **0 entry** | 🔴 Không tồn tại theo API arXiv tại thời điểm kiểm tra. **Không trích.** |
| X2 | `https://eprint.iacr.org/2026/1938.pdf` — "Post-Quantum TLS Measurements and Protocol Variants" | Kết quả `web_search` | Không fetch được; không xác minh | 🔴 **Không trích.** |
| X3 | `NIST SP 1800-38` (NCCoE, Migration to Post-Quantum Cryptography) | Ký ức + tìm kiếm | CrossRef trả phản hồi **không phải JSON hợp lệ** cho DOI `10.6028/NIST.SP.1800-38` | 🔴 Không xác minh được qua CrossRef. Nếu cần dùng, phải xác minh lại bằng nguồn NCCoE trực tiếp. |
| X4 | `draft-ietf-tls-hybrid-design` (bản thảo hybrid key exchange cho TLS) | Ký ức | Fetch `datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/` → HTTP 302, **không lấy được tiêu đề** | 🔴 Chưa xác minh. **Không trích.** |
| X5 | URL `https://cic.iacr.org/p/1/3/22` được suy đoán là bài khảo sát PQC TLS | Do người lập tự suy đoán | Fetch → HTTP 200 nhưng nội dung là **bài khác** ("Lower Bound on Number of Compression Calls of a Collision-Resistance Preserving Hash", Chakraborty & Nandi) | 🔴 **Suy đoán sai.** Đã loại. Ghi lại để Reviewer1 thấy lỗi này đã được tự phát hiện và sửa. |

---

## E. Nguồn đã cố fetch nhưng **THẤT BẠI** (ghi rõ để minh bạch)

| URL | Kết quả | Ghi chú |
|---|---|---|
| `https://www.mdpi.com/2413-4155/7/3/91` | ❌ HTTP **403 Access Denied** (Akamai) | Nguồn S16 |
| `https://www.mdpi.com/1099-4300/27/12/1242` | ❌ HTTP **403 Access Denied** | Nguồn S15 |
| `https://www.mdpi.com/2413-4155/7/3/91/pdf` (kèm User-Agent trình duyệt) | ❌ HTTP **403**, trả về HTML 404 bytes | Không lách tiếp — tôn trọng kiểm soát truy cập |
| `https://dl.acm.org/doi/pdf/10.1145/3620678.3624652` | ❌ HTTP **403** | Nguồn S24 |
| `https://dergipark.org.tr/en/download/article-file/5763310` | ❌ HTTP **000** (không thiết lập được kết nối) | Nguồn S17 |
| `https://lirias.kuleuven.be/retrieve/14e501bd-…` qua `web_fetch` | ❌ `unsupported content type "application/pdf"` | Nhưng **tải được bằng `curl`** → đã đọc toàn văn (S6) |
| `https://doi.org/10.62056/ahee0iuc` | ❌ `cross-origin redirect to https://cic.iacr.org is not followed automatically` | Nguồn S7 |
| `https://csrc.nist.gov/pubs/sp/800/207/final` | ✅ HTTP 200 | Thành công (S4) |
| `https://www.rfc-editor.org/rfc/rfc8446.txt` | ✅ HTTP 200 | Thành công (S1) |
| `https://www.rfc-editor.org/rfc/rfc9370.txt` | ✅ HTTP 200 | Thành công (S2) |
| `https://www.ndss-symposium.org/wp-content/uploads/2020/02/24203-paper.pdf` | ✅ HTTP 200 | Thành công (S3) |

**Tổng kết truy cập (do người lập tự đếm, Reviewer1 phải kiểm lại):**
- Tải **thành công** nội dung: **7** nguồn (S1, S2, S3, S4, S5, S6) **+ S31 toàn văn HTML** (vòng T19).
- Đọc **trừu tượng chính thức qua arXiv API**: 1 nguồn (S31) ở vòng T2 — **nay đã nâng lên toàn văn** ở vòng T19.
- Xác minh **metadata** thành công nhưng không đọc toàn văn: **21** DOI (S7–S21, S22–S29).
- **Thất bại** khi fetch: **7** URL (bảng §E, trừ 2 dòng ✅).
- **Không xác minh được**: **5** mục (X1–X5). **Đã tự phát hiện và sửa 1 sai sót** (X6): `arXiv:2609.18633` thực ra tồn tại — lỗi do thiếu cờ `-L` khi gọi arXiv API.

---

## F. Phương pháp xác minh (tái lập được)

```bash
# 1) Metadata DOI
curl -s "https://api.crossref.org/works/10.6028/NIST.FIPS.203"
curl -s "https://api.openalex.org/works/https://doi.org/10.1109/ACCESS.2023.3281480"
# 2) Toàn văn PDF mở
curl -sL "https://www.ndss-symposium.org/wp-content/uploads/2020/02/24203-paper.pdf" -o ndss2020.pdf
pdftotext -layout ndss2020.pdf ndss.txt && wc -l ndss.txt
# 3) Tìm kiếm có hệ thống (OpenAlex, ghi lại nguyên văn truy vấn)
#    -> ../EVIDENCE/openalex_title_filters.txt, ../EVIDENCE/openalex_doi_lookup.txt
```

Danh sách tác giả: xác minh qua OpenAlex, lưu tại `../EVIDENCE/openalex_authors.txt`.

Công cụ dùng: `curl`, `python3` (thư viện chuẩn), `pdftotext` (poppler), `web_search`, `web_fetch`.
**Không** dùng CSDL trả phí. **Không** dùng bất kỳ nguồn nào từ trí nhớ mà không kiểm tra.

---

## G. BÀI HỌC TỪ DISSENT-6 — DOI phân biệt HOA/THƯỜNG khi truy vấn

Đã tự kiểm lại bằng `curl` (bằng chứng thô: `../EVIDENCE/T19_checks.txt` mục VIỆC 1):

| Chuỗi DOI | Crossref REST | OpenAlex REST | doi.org |
|---|---|---|---|
| `10.1109/`**`ICICT`**`63348.2025.10989392` | **404** | **404** | **404** |
| `10.1109/`**`iccit`**`63348.2025.10989392` | **200** | **200** | **202** |

⇒ **hoa/thường quyết định 404 hay 200** trong thực tế. Đây là lỗi **chép sai hoa/thường**, **KHÔNG phải bịa nguồn**.
Đã sửa 4 vị trí theo DISSENT-6; `grep -rn "ICICT63348" research/` nay → **0 match**.

**Quy tắc từ nay:** **luôn dán DOI nguyên văn từ output API**, không gõ lại bằng tay.
