# SOURCES_BROWSER — Truy hồi bằng trình duyệt/fetch từ VM độc lập (Task T13)

**Task:** T13 (D-012, msg #43; assignment msg #48) · **Agent:** javis (`ag_3bef07fd`)
**Ngày truy hồi:** 2026-10-01 · **Môi trường:** VM riêng của javis (`/home/hatch`), khác máy với ResearchLead.
**Danh sách nguồn:** `research/EVIDENCE/FETCH_STATUS.md` (nhánh `agent/research-lead/T2`) — 8 URL fetch thất bại.
**Quy ước:** trích dẫn trong file này là **nguyên văn** từ nội dung lấy được. Nguồn nào không lấy được ghi rõ
`chưa xác minh`, không suy diễn nội dung. Metadata thư mục (tác giả/venue) đối chiếu qua Crossref API cùng ngày.

---

## S16 — Module-Lattice-Based Key-Encapsulation Mechanism Performance Measurements

- **URL gốc:** https://www.mdpi.com/2413-4155/7/3/91
- **DOI:** `10.3390/sci7030091` · **Venue:** *Sci* (MDPI), 2025
- **Tác giả (Crossref):** Nagy Naya, Alnemer Sarah, Alshuhail Lama Mohammed, Alobiad Haifa, Almulla Tala, Alrumaihi Fatima Ahmed, Ghadra Najd, Nagy Marius
- **Kết quả truy hồi:** ✅ **LẤY ĐƯỢC TOÀN VĂN.**
  - `curl` từ VM này: HTTP **403** (396 bytes) — vẫn bị Akamai chặn như ResearchLead.
  - Fetch nội dung trang (kênh trình duyệt): HTTP 200, toàn văn bài báo trích xuất được (1.187 dòng văn bản, đủ các mục 1–7 + tài liệu tham khảo).
  - URL biến thể PDF `https://www.mdpi.com/2413-4155/7/3/91/pdf`: `curl` 403 (404 bytes), fetch trang 403 ⇒ **riêng file PDF chưa xác minh**; nội dung bài đã có đủ qua bản HTML ở URL gốc.
- **Abstract (nguyên văn, đối chiếu Crossref = bản tóm tắt của bài):**

> "Key exchange mechanisms are foundational to secure communication, yet traditional methods face challenges
> from quantum computing. The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a post-quantum
> cryptographic key exchange protocol with unknown successful quantum vulnerabilities. This study evaluates
> the ML-KEM using experimental benchmarks. We implement the ML-KEM in Python for clarity and in C++ for
> performance, demonstrating the latter's substantial performance improvements. The C++ implementation
> achieves microsecond-level execution times for key generation, encapsulation, and decapsulation. […]
> Moreover, our Python benchmark confirmed that the ML-KEM consistently outperformed RSA in execution speed
> across all tested parameters. […] we also tested the C++ implementation on a Raspberry Pi 4B,
> representing IoT use cases. Additionally, we attempted to run integration and benchmark tests for the
> ML-KEM on microcontrollers such as the ESP32 DevKit, ESP32 Super Mini, ESP8266, and Raspberry Pi Pico,
> but these trials were unsuccessful due to memory constraints."

- **Trích nguyên văn đoạn kết quả chính (mục 7, Conclusions):**

> "The C++ implementation proved to be efficient and was faster than Python by over 139.5× in key operations
> such as key generation, encapsulation, and decapsulation."

> "our Python-based benchmarks showed that the ML-KEM consistently outperformed RSA across all parameter
> sets, with ML-KEM-768 over 15× faster than RSA-3072, and ML-KEM-1024 faster than RSA-4096 […]"

> "in spite of its advantages, the ML-KEM has drawbacks, particularly at the ML-KEM-1024 level, including
> high memory consumption and computational expense. These problems make it impractical to use on extremely
> constrained devices"

---

## S15 — On the Security and Efficiency of TLS 1.3 Handshake with Hybrid Key Exchange from CPA-Secure KEMs

- **URL gốc:** https://www.mdpi.com/1099-4300/27/12/1242
- **DOI:** `10.3390/e27121242` · **Venue:** *Entropy* (MDPI), 2025
- **Tác giả (Crossref):** Chen Jinrong, Peng Wei, Wang Yi, Bian Yutong
- **Kết quả truy hồi:** ✅ **LẤY ĐƯỢC TOÀN VĂN.**
  - `curl` từ VM này: HTTP **403** (400 bytes).
  - Fetch nội dung trang (kênh trình duyệt): HTTP 200, toàn văn trích xuất được (1.451 dòng văn bản).
- **Abstract (nguyên văn, đối chiếu Crossref):**

> "TLS 1.3 is a crucial protocol for securing modern internet communications. To facilitate a smooth
> transition to post-quantum security, hybrid key exchange, which combines classical key exchange
> algorithms with post-quantum key encapsulation mechanisms (KEMs), is proposed to enhance the security of
> the current TLS 1.3 handshake. However, existing drafts and implementations of hybrid key exchange for
> TLS 1.3 primarily rely on CCA-secure KEMs […] based on the Fujisaki-Okamoto (FO) transform. The
> re-encryption step in their decapsulation algorithms not only introduces additional performance overhead
> but also raises the risk of side-channel attacks. […] This work challenges the necessity of CCA security
> by proving that CPA-secure KEMs are sufficient for the TLS 1.3 handshake even in the hybrid key exchange
> setting. […] Our results show that using CPA-secure KEMs yields up to 44.8% performance improvement at
> the key exchange layer and up to approximately 9% acceleration for the full TLS 1.3 handshake."

- **Trích nguyên văn đoạn đóng góp/kết quả (§1.1 của bài):**

> "We implement and evaluate the performance of the hybrid schemes specified in the IETF draft [21], i.e.,
> X25519MLKEM768, SecP256r1MLKEM768, and SecP384-MLKEM1024, using the latest OpenSSL […] demonstrate that
> at the key exchange layer, using a CPA-secure KEM can yield a performance improvement of up to
> approximately 44.8%."

> "at the full protocol level, the efficiency gain from using CPA-secure KEMs is more modest, not
> exceeding 9%."

---

## S17 — Hybrid ML-KEM in TLS 1.3: Performance Analysis on ARM64 Under Network Stress

- **URL gốc:** https://dergipark.org.tr/en/download/article-file/5763310
- **DOI:** `10.53070/bbd.1898820` · **Venue:** *Journal of Computer Science* (DergiPark, `bbd`), 2026
- **Tác giả (từ PDF):** Cemile İNCE (İnönü University, Türkiye)
- **Kết quả truy hồi:** ✅ **LẤY ĐƯỢC TOÀN VĂN PDF.**
  - ResearchLead: HTTP 000 (không thiết lập được kết nối).
  - `curl -L` kèm User-Agent trình duyệt từ VM này: HTTP **200**, `application/pdf`, **1.108.312 bytes**; `pdftotext` trích xuất thành công. Khác biệt là do môi trường mạng của VM, không phải do thay đổi phía DergiPark (chưa xác minh).
- **Abstract (nguyên văn từ PDF):**

> "In the post-quantum era, it is predicted that secure encryption algorithms like RSA and ECC will be
> broken within microseconds. In response, NIST has made the transition to post-quantum cryptography
> necessary by completing the ML-KEM standard (FIPS 203) in August 2024. However, integrating these new
> algorithms into the existing TLS 1.3 infrastructure raises some concerns, particularly in
> resource-constrained IoT devices where computing power and memory are limited. This paper evaluates the
> TLS 1.3 handshake performance of ML-KEM-512, ML-KEM-768, ML-KEM1024, and hybrid X25519+ML-KEM-768 on a
> Raspberry Pi 4 (ARM Cortex-A72) in five different network scenarios (loopback, LAN (10 ms RTT), WAN
> (50 ms RTT), and packet loss rates of 1% and 5%). Experiments were performed using OpenSSL 3.x
> integrated with liboqs, with 100 iterations for each configuration."

- **Trích nguyên văn kết quả chính (Abstract + phần kết quả):**

> "The results show that ML-KEM algorithms, which have high computational costs, introduce negligible
> computational overhead compared to the classic X25519 under low latency conditions, and base-state
> 1-RTT handshake times range from 11.3 to 13.3 ms. The ML-KEM 512 algorithm showed the best performance,
> particularly due to its small packet size. ML-KEM reached 180 ms with 5% loss, while X25519 reached
> 281 ms."

> "In algorithm tests, ML-KEM 512 provided a 4.16-fold speedup at the base level. In WAN conditions,
> network RTT becomes the dominant bottleneck, and the choice of KEM algorithm becomes practically
> irrelevant."

---

## S7 — A Comprehensive Survey on Post-Quantum TLS

- **URL gốc:** https://doi.org/10.62056/ahee0iuc
- **DOI:** `10.62056/ahee0iuc` · **Venue:** *IACR Communications in Cryptology*, Vol. 1, Issue 2, 2024
- **Tác giả (thẻ `citation_author` của trang đích):** Nouri Alnahawi, Johannes Müller, Jan Oupický, Alexander Wiesmaier
- **Kết quả truy hồi:** ✅ **LẤY ĐƯỢC.**
  - ResearchLead bị chặn ở chuyển hướng chéo tên miền (`doi.org` → `cic.iacr.org` không tự theo).
  - `curl -L` từ VM này theo đủ chuyển hướng: đích cuối **https://cic.iacr.org/p/1/2/6**, HTTP **200**, 168.296 bytes HTML; đọc được tiêu đề + abstract chính thức.
  - **Đính chính hữu ích:** URL toàn văn đúng là `/p/1/2/6`. URL `/p/1/3/22` từng được suy đoán trước đây là bài khác (đã ghi ở FETCH_STATUS) — khớp với việc bài này thuộc Issue 2, không phải Issue 3.
- **Abstract (nguyên văn từ trang đích):**

> "Transport Layer Security (TLS) is the backbone security protocol of the Internet. As this fundamental
> protocol is at risk from future quantum attackers, many proposals have been made to protect TLS against
> this threat by implementing post-quantum cryptography (PQC). The widespread interest in post-quantum TLS
> has given rise to a large number of solutions over the last decade. These proposals differ in many
> aspects, including the security properties they seek to protect, the efficiency and trustworthiness of
> their post-quantum building blocks, and the application scenarios they consider, to name a few. Based on
> an extensive literature review, we classify existing solutions according to their general approaches,
> analyze their individual contributions, and present the results of our extensive performance
> experiments. Based on these insights, we identify the most reasonable candidates for post-quantum TLS,
> which research problems in this area have already been solved, and which are still open. Overall, our
> work provides a well-founded reference point for researching post-quantum TLS and preparing TLS in
> practice for the quantum age."

---

## X4 — draft-ietf-tls-hybrid-design (IETF Datatracker)

- **URL gốc:** https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/
- **Kết quả truy hồi:** ✅ **LẤY ĐƯỢC — VÀ CÓ PHÁT HIỆN MỚI.**
  - ResearchLead: HTTP 302, không lấy được tiêu đề.
  - `curl -L` từ VM này: đích cuối **https://datatracker.ietf.org/doc/rfc9954/**, HTTP **200**, 79.550 bytes.
  - **Bản thảo đã được xuất bản thành RFC 9954 — "Hybrid Key Exchange in TLS 1.3"** (Informational). Từ giờ hồ sơ nên trích RFC 9954 thay vì bản draft.
- **Abstract của RFC 9954 (nguyên văn):**

> "Hybrid key exchange refers to using multiple key exchange algorithms simultaneously and combining the
> result with the goal of providing security even if a way is found to defeat the encryption for all but
> one of the component algorithms. It is motivated by the transition to post-quantum cryptography. This
> document provides a construction for hybrid key exchange in the Transport Layer Security (TLS) protocol
> version 1.3."

---

## Tổng kết đề tài PQC-TLS

| Mã | Trạng thái tại ResearchLead | Trạng thái tại javis (2026-10-01) |
|---|---|---|
| S16 (MDPI Sci) | 403 | ✅ Toàn văn (bản HTML); riêng file PDF chưa xác minh |
| S15 (MDPI Entropy) | 403 | ✅ Toàn văn |
| S17 (DergiPark) | HTTP 000 | ✅ Toàn văn PDF (1.108.312 bytes) |
| S7 (IACR CiC) | Chặn chuyển hướng | ✅ Trang đích + abstract; URL đúng `/p/1/2/6` |
| X4 (Datatracker) | 302, không có tiêu đề | ✅ Đã thành **RFC 9954**, có abstract |

Người viết file này **không tự verify** kết quả của mình (D-004) — chờ Reviewer1 kiểm chứng độc lập.
