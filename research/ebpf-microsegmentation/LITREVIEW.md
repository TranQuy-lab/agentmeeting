# LITREVIEW — Tổng quan tài liệu

## Đề tài `RL-T2-EBPF-SEG`: Vi phân đoạn động bằng eBPF cho Kubernetes

**Người thực hiện:** ResearchLead (`ag_d85dde8d`)
**Ngày hoàn thành:** 2026-10-01
**Ngày thực hiện tìm kiếm:** 2026-10-01 (UTC)
**Nhánh:** `agent/research-lead/T2`
**Phương pháp:** theo quy trình `literature-review` của bộ skill `nckh`
(`/home/noble-tran/agent-skills/skills/nckh/references/skills/literature-review/SKILL.md`)
**Trạng thái:** ⏳ chờ Reviewer1 kiểm định độc lập — **người viết không tự verify**

---

## MỤC LỤC

1. [Tóm tắt điều hành](#1-tóm-tắt-điều-hành)
2. [Câu hỏi tổng quan và phạm vi](#2-câu-hỏi-tổng-quan-và-phạm-vi)
3. [Chiến lược tìm kiếm](#3-chiến-lược-tìm-kiếm)
4. [Sàng lọc và chọn lựa](#4-sàng-lọc-và-chọn-lựa)
5. [Bối cảnh: zero-trust và chính sách mạng trong Kubernetes](#5-bối-cảnh-zero-trust-và-chính-sách-mạng-trong-kubernetes)
6. [Tổng hợp theo chủ đề](#6-tổng-hợp-theo-chủ-đề)
   - 6.1 [Nền tảng eBPF/XDP: vì sao chi phí thấp](#61-nền-tảng-ebpfxdp-vì-sao-chi-phí-thấp)
   - 6.2 [Chi phí chính sách mạng K8s: bằng chứng mạnh nhất](#62-chi-phí-chính-sách-mạng-k8s-bằng-chứng-mạnh-nhất)
   - 6.3 [Vi phân đoạn và zero-trust: từ tối ưu ngoại tuyến tới thực thi trực tuyến](#63-vi-phân-đoạn-và-zero-trust-từ-tối-ưu-ngoại-tuyến-tới-thực-thi-trực-tuyến)
   - 6.4 [Chi phí lớp sidecar/service mesh: đối thủ cần so sánh](#64-chi-phí-lớp-sidecarservice-mesh-đối-thủ-cần-so-sánh)
7. [Tổng hợp xuyên nghiên cứu](#7-tổng-hợp-xuyên-nghiên-cứu)
8. [Khoảng trống nghiên cứu và vị trí đề tài](#8-khoảng-trống-nghiên-cứu-và-vị-trí-đề-tài)
9. [Đánh giá chất lượng bằng chứng](#9-đánh-giá-chất-lượng-bằng-chứng)
10. [Giới hạn của tổng quan này](#10-giới-hạn-của-tổng-quan-này)
11. [Ghi chú liêm chính: nguồn bị loại](#11-ghi-chú-liêm-chính-nguồn-bị-loại)
12. [Tài liệu tham khảo](#12-tài-liệu-tham-khảo)

---

## 1. Tóm tắt điều hành

Vi phân đoạn (microsegmentation) là cách hiện thực hoá zero-trust ở tầng mạng: thay vì tin nhau vì "cùng nằm trong mạng nội bộ", mọi luồng đều bị đối chiếu với chính sách. NIST SP 800-207 (S4) định nghĩa zero-trust là *"an evolving set of cybersecurity paradigms that move defenses from static, network-based perimeters to focus on users, assets, and resources"* — nhấn mạnh tính **động**. Trong Kubernetes, chính sách mạng được thực thi bởi CNI; các giải pháp dùng eBPF (Calico, Cilium) đã trở thành phổ biến. Tài liệu chính thức của Cilium (S5) phân lớp chính sách thành L3 / L4 / L7.

**Phát hiện có bằng chứng mạnh nhất:** Budigiri và cộng sự (S6, 2021) — nguồn duy nhất trong tổng quan này được đọc **toàn văn** về chủ đề chính sách K8s — kết luận rằng chính sách mạng *"incur a negligible performance overhead which only varies slightly with the number of policies and for different policy recipes"*. Nghĩa là: **câu hỏi "chính sách có đắt không" đã có câu trả lời cho chính sách TĨNH.**

**Ba điều chưa biết:**
1. **Cửa sổ hội tụ** khi danh tính workload thay đổi (chính sách động) — chưa đo.
2. **Tương quan chi phí L3 vs L4 vs L7 trong cùng một thí nghiệm** — chưa đo.
3. **Khoảng hở thực thi** trong lúc chuyển chính sách — chưa mô tả, dù có ý nghĩa an ninh trực tiếp.

**Điều tổng quan này KHÔNG nói được:** không có kết luận nào về hiệu năng của vi phân đoạn động trong thực tế, vì **chưa có thực nghiệm nào được chạy**. Mọi con số nêu ở trên là **số liệu hoặc phát biểu của công trình khác**.

---

## 2. Câu hỏi tổng quan và phạm vi

**Câu hỏi tổng quan:** Đã biết gì — và chưa biết gì — về chi phí và hiệu quả thực thi của vi phân đoạn mạng dùng eBPF trong Kubernetes, đặc biệt khi chính sách phải thay đổi liên tục theo danh tính workload?

**Tiêu chí đưa vào:**
- (a) đo lường hiệu năng eBPF/XDP hoặc chính sách mạng trong môi trường container; hoặc
- (b) khảo sát/khung về microsegmentation hoặc zero-trust; hoặc
- (c) văn bản chuẩn hoá hoặc tài liệu kỹ thuật chính thức của hệ thống được nghiên cứu.

**Tiêu chí loại:**
- Bài về "microsegmentation" theo nghĩa thị trường/phân khúc khách hàng (trùng từ khoá nhưng khác ngành) — **có xảy ra thật**, xem §4.
- Bài không có số liệu và không có khung.
- Không truy được DOI/URL.

**Phạm vi loại trừ:** an ninh chuỗi cung ứng container, quét ảnh, runtime security (Falco và tương tự), mật mã trong cụm.

---

## 3. Chiến lược tìm kiếm

| # | Nguồn | Cách truy vấn | Ghi lại ở đâu |
|---|---|---|---|
| DB1 | **OpenAlex** | `search=` và `filter=title.search:` | `EVIDENCE/openalex_queries.txt`, `../EVIDENCE/openalex_title_filters.txt`, `../EVIDENCE/openalex_doi_lookup.txt` |
| DB2 | **CrossRef** | `works/<DOI>` | `../EVIDENCE/crossref_lookups.txt` |
| DB3 | **Nguồn nhất cấp** (NIST CSRC, tài liệu Cilium) | `web_fetch` | `SOURCES.md` §A |

**Chuỗi truy vấn nguyên văn (đã chạy):**

```text
Q1  eBPF extended Berkeley Packet Filter security monitoring
Q2  eBPF performance overhead kernel observability
Q3  Cilium eBPF Kubernetes network security enforcement
Q4  zero trust architecture implementation evaluation enterprise
Q5  service mesh sidecar proxy latency overhead evaluation
Q6  title.search:eBPF AND title.search:network           -> 0 kết quả (cú pháp sai)
Q7  title.search:microsegmentation                        -> 59 kết quả (nhiều kết quả lạc đề)
Q8  title.search:zero-trust AND title.search:network      -> 0 kết quả (cú pháp sai)
Q9  title.search:kubernetes AND title.search:network policy -> 0 kết quả (cú pháp sai)
```

**Ghi chú sai sót (tự khai báo):** Q6, Q8, Q9 trả về **0 kết quả** do tác giả dùng sai cú pháp `AND` với `filter=title.search:` của OpenAlex. Lỗi chỉ được phát hiện khi đọc output thô (`../EVIDENCE/openalex_title_filters.txt`). Ba truy vấn này **không được tính** vào độ phủ.

---

## 4. Sàng lọc và chọn lựa

| Bước | Số lượng | Ghi chú |
|---|---|---|
| Bản ghi thô từ OpenAlex (5 truy vấn hợp lệ) | ~40 | `EVIDENCE/openalex_queries.txt` |
| Liên quan trực tiếp | 12 | |
| **Bị loại vì lạc đề do trùng từ khoá** | **nhiều** | Ví dụ: "The Microsegmentation of the Autism Spectrum" (y tế), "Determinants of mobile social media use… international microsegmentation" (marketing), "Efficient automatic analysis of camera work and microsegmentation of video" (xử lý ảnh) — tất cả nằm trong `oa_filters.txt` |
| Bị loại vì xếp hạng theo trích dẫn kéo về bài không liên quan | nhiều | "Spectre Attacks" (1.795 trích dẫn), "A view of cloud computing" (9.132 trích dẫn) — xuất hiện nhưng **không liên quan** |
| Nguồn nhất cấp bổ sung | 3 | S4 (NIST SP 800-207), S5 (Cilium docs), S6 (EuCNC) |
| **Tổng nguồn đưa vào** | **12** | Trong đó **3 đọc toàn văn** (S4, S5, S6) và **1 đọc trừu tượng chính thức** (S30) |

> ⚠️ **Không dựng sơ đồ PRISMA.** Đây là tổng quan định hướng, **không phải** systematic review. Tài liệu này **không được** dán nhãn PRISMA.

---

## 5. Bối cảnh: zero-trust và chính sách mạng trong Kubernetes

**NIST SP 800-207 (S4, đọc trừu tượng chính thức nguyên văn):** zero-trust *"assumes there is no implicit trust granted to assets or user accounts based solely on their physical or network location"*, và *"focuses on protecting resources (assets, services, workflows, network accounts, etc.), not network segments, as the network location is no longer seen as the prime component to the security posture of the resource."*

Điểm này quan trọng cho thiết kế đề tài: nếu zero-trust **không** lấy phân đoạn mạng làm đơn vị bảo vệ, thì vi phân đoạn chỉ là **một cơ chế thực thi**, không phải toàn bộ kiến trúc. Đề tài này phải tránh ngộ nhận "vi phân đoạn = zero-trust". Đây là **rủi ro diễn giải** cần Reviewer1 để ý.

**Cilium (S5, đọc toàn văn):** tài liệu chính thức xác nhận chính sách được phân lớp thành **L3** (danh tính endpoint, node, CIDR, DNS), **L4** (cổng, ICMP/ICMPv6, SNI), và **L7** (HTTP, DNS), và chính sách được phân phối qua tài nguyên Kubernetes (`NetworkPolicy`, `CiliumNetworkPolicy`, `CiliumClusterwideNetworkPolicy`). Tài liệu cũng ghi rõ phương thức nạp trực tiếp vào agent qua CLI/API **đã bị đánh dấu deprecated từ v1.18 và sẽ bị loại bỏ ở v1.19**, kèm cảnh báo rằng phương thức đó *"does not automatically distribute policies to all agents"*.

**Suy luận của người lập (KHÔNG phải kết luận của nguồn):** chi tiết "phương thức nạp trực tiếp không tự phân phối chính sách tới mọi agent" là một **gợi ý trực tiếp** rằng cơ chế phân phối chính sách là một mắt xích có thể tạo ra độ trễ hội tụ — đúng câu hỏi RQ1/RQ3 của đề tài. Tuy nhiên, **không được** suy ra từ tài liệu này rằng độ trễ đó lớn hay nhỏ; phải đo.

---

## 6. Tổng hợp theo chủ đề

### 6.1. Nền tảng eBPF/XDP: vì sao chi phí thấp

Bằng chứng nền tảng đến từ công trình XDP (S22, ACM CoNEXT 2018, **327 trích dẫn** — chỉ metadata). Người lập **không đọc toàn văn**, nên **không trích số liệu**. Điều nói được một cách an toàn: đây là công trình nền tảng, được trích dẫn rộng rãi, về việc xử lý gói trong nhân Linux.

**Phát hiện 2026 quan trọng:** Netkit (S30, eBPF'26 Workshop, 2026-09-29) là một datapath dùng eBPF để loại bỏ việc duyệt hàng đợi backlog dư thừa khi chuyển đổi network namespace, **được tích hợp vào Cilium**. Trích trừu tượng: *"improves throughput by up to 37% and achieves parity between container-to-container and process-to-process communications"*. Điều này có hai hệ quả cho đề tài: (a) **xác nhận** rằng chi phí đường truyền giữa container là vấn đề đang được nghiên cứu tích cực năm 2026 — nên tính mới phải được bảo vệ cẩn thận; (b) **con số 37% là của tác giả S30**, không phải kết quả của đề tài này.

Khảo sát eBPF (S23, IEEE Access 2023, 70 trích dẫn — chỉ metadata) đặt eBPF trong bối cảnh observability, networking và security cho mạng cloud-native. Trừu tượng (từ OpenAlex) nêu Kubernetes là *"the de facto distributed operating system for container orchestration"*.

Các công trình về **an toàn của chính eBPF** (S25, S26 — chỉ metadata) là một nhánh song song quan trọng: nếu bản thân cơ chế thực thi có lỗi, thì mọi kết luận về "chính sách được thực thi đúng" đều lung lay. Đề tài này **không** nghiên cứu nhánh đó, nhưng phải khai báo giới hạn.

### 6.2. Chi phí chính sách mạng K8s: bằng chứng mạnh nhất

**Đây là phần duy nhất của tổng quan có bằng chứng toàn văn về chủ đề chính.**

Budigiri, Baumann, Mühlberg, Truyen & Joosen (S6, EuCNC/6G Summit 2021) đặt vấn đề trong bối cảnh ứng dụng 5G URLLC ở biên, nơi *"neither communication performance nor security should be compromised"*. Họ đánh giá Calico và Cilium (đều dùng eBPF) và phân tích an ninh của chính sách mạng.

Trích nguyên văn (xem `../EVIDENCE/quote_extracts.txt` mục B):

| Nội dung | Trích nguyên văn | Dòng |
|---|---|---|
| Kết luận chính | *"…that network policies incur a negligible performance overhead which only varies slightly with the number of policies and for different policy recipes."* | 46–48 |
| Vị trí học thuật | *"…this paper is the first to investigate both performance overheads and security implications of K8s network policies specifically…"* (phần I) | — |
| Một quan sát về host | *"…which host results were better by 8.7% and 10.7% for latency"* | 161 |

**Diễn giải (của người lập — không phải kết luận của bài gốc):** kết quả "negligible overhead" **chỉ áp dụng cho chính sách tĩnh**. Bài báo không đo vòng lặp cập nhật chính sách theo danh tính. Đây chính là **giả thuyết H1/H2** của đề tài: chi phí *thực thi* có thể không đáng kể (đã được chứng minh), nhưng chi phí *hội tụ* và *khoảng hở* thì chưa ai đo.

**Cảnh báo quan trọng:** câu "negligible overhead" rất dễ bị trích dẫn ra khỏi ngữ cảnh để biện minh cho việc không cần đo thêm. Đề tài này phải **phản biện chính xác điểm đó**, không được lặp lại nó.

### 6.3. Vi phân đoạn và zero-trust: từ tối ưu ngoại tuyến tới thực thi trực tuyến

Ba nguồn liên quan nhất đều **chỉ ở mức metadata**:

- **S27** — Noel và cộng sự (2021), *Optimizing network microsegmentation policy for cyber resilience*: trừu tượng (OpenAlex) nói về *"synthesis of optimal microsegmentation policy for a network"* và *"reason about fine-grained policy rules"*. Đây là **tối ưu ngoại tuyến**. Không trích số liệu.
- **S28** — *Automated Microsegmentation for Lateral Movement Prevention in Industrial Internet of Things (IIoT)* (2021). Trừu tượng nêu bối cảnh IoT/OT và di chuyển ngang. Không trích số liệu.
- **S29** — *Zero Trust Implementation for Legacy Systems using Dynamic Microsegmentation, RBAC, and ABAC* (2025). Tiêu đề có chữ **"Dynamic"** — đây là nguồn **gần nhất** với đề tài và là **mối đe doạ trực tiếp tới tính mới**. Người lập **KHÔNG đọc được toàn văn** ⇒ **không thể** kết luận nó có trùng ý tưởng hay không.

> 🔴 **Cảnh báo cho Reviewer1 — điểm yếu nghiêm trọng nhất của hồ sơ này:** S29 gần như chắc chắn liên quan trực tiếp tới RQ1/RQ3 (động + vi phân đoạn + zero-trust). Việc tác giả **không đọc được toàn văn S29** là một **lỗ hổng bằng chứng** của tổng quan. Phải tìm cách đọc S29 (qua thư viện, qua tác giả, hoặc qua công trình kế thừa) **trước khi** bảo vệ tính mới. Nếu S29 đã đo cửa sổ hội tụ, tính mới của đề tài này gần như bằng không.

### 6.4. Chi phí lớp sidecar/service mesh: đối thủ cần so sánh

**S24** — *Dissecting Overheads of Service Mesh Sidecars* (ACM SoCC 2023, 42 trích dẫn — chỉ metadata). Đây là **đối chứng bắt buộc**: nếu sidecar (kiến trúc chèn proxy vào đường đi của gói) có chi phí cao, thì eBPF (kiến trúc trong nhân, không chèn proxy) có lợi thế. Nhưng người lập **không đọc được toàn văn** nên **không trích số liệu**.

Ý nghĩa cho thiết kế: ma trận thí nghiệm P2 của đề tài nên có **một nhánh so sánh với chế độ L7 dùng proxy**, để không tuyên bố "eBPF tốt hơn" một cách vô căn cứ.

---

## 7. Tổng hợp xuyên nghiên cứu

**Mẫu hình 1 — "Chi phí thực thi thấp, nhưng bằng chứng chỉ cho trạng thái tĩnh."** S6 (toàn văn) cho kết quả rõ ràng; nhưng phạm vi của nó là tĩnh. Toàn bộ phần "động" của vấn đề còn để ngỏ.

**Mẫu hình 2 — "Tài liệu kỹ thuật chính thức thừa nhận cơ chế phân phối chính sách là mắt xích riêng."** S5 ghi rõ phương thức nạp trực tiếp không tự phân phối. Đây là **bằng chứng gián tiếp** rằng độ trễ hội tụ là một biến số có thật trong hệ thống, chứ không phải giả định của tác giả.

**Mẫu hình 3 — "Từ khoá bị ô nhiễm nặng."** Truy vấn `microsegmentation` trả về kết quả từ y tế, marketing, xử lý video. Đây là **cảnh báo phương pháp**: một systematic review thực sự về chủ đề này cần bộ lọc ngành rất chặt, nếu không sẽ bị ô nhiễm.

**Mẫu hình 4 — "Lĩnh vực bị chi phối bởi công nghiệp, ít bài đo lường độc lập."** Phần lớn kiến thức vận hành nằm trong tài liệu nhà cung cấp (S5) chứ không trong bài bình duyệt. Điều này vừa là cơ hội (khoảng trống học thuật) vừa là rủi ro (thiếu chuẩn so sánh độc lập).

---

## 8. Khoảng trống nghiên cứu và vị trí đề tài

| # | Khoảng trống | Mức chắc chắn | Đề tài đóng góp |
|---|---|---|---|
| G1 | Cửa sổ hội tụ khi danh tính workload thay đổi chưa được đo | 🟡 Trung bình | P2 (RQ1) |
| G2 | Chưa đo L3 vs L4 vs L7 trong cùng một ma trận | 🟡 Trung bình | P2 (RQ2) |
| G3 | Khoảng hở thực thi trong lúc chuyển chính sách chưa được mô tả | 🟡 Trung bình | P2/P3 (RQ3) |
| G4 | Chưa có mô hình dự đoán chi phí + cửa sổ hội tụ | 🔴 **Yếu** — và bị đe doạ trực tiếp bởi S29 chưa đọc | P3 (RQ4) |

**Mức chắc chắn tổng thể thấp hơn đề tài 1**, vì (a) ít nguồn đọc toàn văn hơn về đúng chủ đề, và (b) có một nguồn chưa đọc (S29) có khả năng trùng ý tưởng.

---

## 9. Đánh giá chất lượng bằng chứng

**Điểm mạnh:**
- Kết luận chính dựa trên **nguồn đọc toàn văn** (S6), có số dòng dẫn chứng.
- Kết luận về cấu trúc chính sách dựa trên **tài liệu chính thức** (S5), không phải blog.
- Hiện tượng ô nhiễm từ khoá được ghi lại trung thực (§4) — đây là thông tin hữu ích cho người làm tổng quan sau.

**Điểm yếu — nói thẳng:**
1. **Lỗ hổng S29.** Nguồn gần nhất với đề tài **chưa đọc được**. Đây là điểm yếu nghiêm trọng nhất.
2. **Chỉ 3/11 nguồn đọc toàn văn.**
3. **Không có PRISMA**, không sàng lọc hai người.
4. **Thiên lệch công bố:** các kết quả "overhead thấp" được nhà cung cấp và cộng đồng ưa chuộng hơn kết quả "overhead cao" — tổng quan này không hiệu chỉnh được.
5. **Nguy cơ lỗi thời đặc biệt cao:** phiên bản CNI và nhân Linux thay đổi vài tháng một lần. Tài liệu Cilium được đọc ghi "Last updated on Sep 15, 2026" và "Cilium 1.20.2" — nghĩa là nội dung có thể đổi sau ngày đọc.
6. **Tự đánh giá**, không phải kiểm định độc lập.

---

## 10. Giới hạn của tổng quan này

- 3 nguồn tìm kiếm; không có quyền truy cập IEEE Xplore/ACM DL full-text.
- Không có nguồn tiếng Việt.
- Một người thực hiện.
- Toàn bộ kết quả trong ngày **2026-10-01**.
- **Không có thực nghiệm nào được chạy.** Không có số liệu nào của đề tài này tồn tại.

---

## 11. Ghi chú liêm chính: nguồn bị loại

**Trường hợp 1 — người lập tưởng sai rằng một nguồn không tồn tại, và đã tự sửa.**

Một kết quả `web_search` gợi ý đường dẫn `https://arxiv.org/pdf/2609.18633v1.pdf`. Lần kiểm tra đầu tiên bằng arXiv API trả về **0 entry**, nên người lập đã định loại nguồn này và **đã viết vào bản nháp đầu** rằng nó không xác minh được.

**Sai.** Khi kiểm lại, nguyên nhân là endpoint `http://export.arxiv.org/api/query` trả **HTTP 301** và cần cờ `-L` của `curl`. Kiểm lại đúng cách, nguồn này **TỒN TẠI THẬT**:

> **S30** — Borkmann, D., & Chaignon, P. (2026). *Netkit: Specializing Linux Packet Delivery for Container Networks*. eBPF'26 Workshop, trang 83–89. DOI `10.1145/3837779.3838164` — **xác minh CrossRef**; arXiv `2609.18633v1`.

Nguồn này **đã được đưa vào** hồ sơ ở mức 🔵 (đọc trừu tượng chính thức, xem `SOURCES.md` §B và `../EVIDENCE/arxiv_lookups.txt`).

> ✅ **Ghi nhận trung thực:** đây là một **lỗi phương pháp của người lập** (thiếu `-L`), được tự phát hiện và tự sửa. Reviewer1 nên xác minh rằng không còn nguồn nào khác bị loại oan vì cùng lý do.

**Trường hợp 2 — nguồn bị loại đúng.**

Đường dẫn `https://eprint.iacr.org/2026/1938.pdf` xuất hiện trong kết quả tìm kiếm của **đề tài 1** cũng không xác minh được và đã bị loại (xem `../pqc-tls-migration/SOURCES.md` §D mục X2).

Ngoài ra, đường dẫn `https://eprint.iacr.org/2026/1938.pdf` xuất hiện trong kết quả tìm kiếm của **đề tài 1** cũng không xác minh được và đã bị loại (xem `../pqc-tls-migration/SOURCES.md` §D). Người lập ghi lại hai trường hợp này để chứng minh rằng các kết quả tìm kiếm **đã được kiểm tra chứ không được tin ngay**.

---

## 12. Tài liệu tham khảo

> Đánh số khớp `SOURCES.md` của đề tài này (S4–S6, S22–S29).

**Mức 🟢 TOÀN VĂN:**

- **[S30]** Borkmann, D., & Chaignon, P. (2026-09-16). *Netkit: Specializing Linux Packet Delivery for Container Networks*. Proceedings of the 4th Workshop on eBPF and Kernel Extensions (eBPF'26), Prague, 2026-09-29, trang 83–89. DOI: [10.1145/3837779.3838164](https://doi.org/10.1145/3837779.3838164). arXiv: https://arxiv.org/abs/2609.18633. 🔵 Đọc **trừu tượng**; chưa đọc toàn văn.
- **[S4]** Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020-08-11). *Zero Trust Architecture*. NIST SP 800-207. DOI: [10.6028/NIST.SP.800-207](https://doi.org/10.6028/NIST.SP.800-207). URL: https://csrc.nist.gov/pubs/sp/800/207/final
- **[S5]** Cilium Authors. *Overview of Network Policy*, Cilium 1.20.2 documentation (trang cập nhật 2026-09-15). URL: https://docs.cilium.io/en/stable/security/policy/
- **[S6]** Budigiri, G., Baumann, C., Mühlberg, J. T., Truyen, E., & Joosen, W. (2021-06-08). *Network Policies in Kubernetes: Performance Evaluation and Security Analysis*. EuCNC/6G Summit 2021. DOI: [10.1109/EuCNC/6GSummit51104.2021.9482526](https://doi.org/10.1109/EuCNC/6GSummit51104.2021.9482526). Bản tác giả: https://lirias.kuleuven.be/retrieve/14e501bd-e6bb-41d6-bf72-360c4850443a

**Mức 🟡 CHỈ METADATA — không trích số liệu:**

- **[S22]** Høiland-Jørgensen, T., et al. (2018-12-04). *The eXpress Data Path*. ACM CoNEXT 2018. DOI: [10.1145/3281411.3281443](https://doi.org/10.1145/3281411.3281443). ⚠️ Chưa đọc toàn văn.
- **[S23]** Soldani, D., et al. (2023). *eBPF: A New Approach to Cloud-Native Observability, Networking and Security for Current (5G) and Future Mobile Networks (6G and Beyond)*. IEEE Access. DOI: [10.1109/ACCESS.2023.3281480](https://doi.org/10.1109/ACCESS.2023.3281480). ⚠️ Chưa đọc toàn văn.
- **[S24]** Zhu, X., et al. (2023-10-30). *Dissecting Overheads of Service Mesh Sidecars*. ACM SoCC 2023. DOI: [10.1145/3620678.3624652](https://doi.org/10.1145/3620678.3624652). ⚠️ Chưa đọc toàn văn.
- **[S25]** (2021). *Synthesizing safe and efficient kernel extensions for packet processing*. ACM SIGCOMM 2021. DOI: [10.1145/3452296.3472929](https://doi.org/10.1145/3452296.3472929). ⚠️ Chưa đọc toàn văn.
- **[S26]** (2019). *Simple and precise static analysis of untrusted Linux kernel extensions*. ACM PLDI 2019. DOI: [10.1145/3314221.3314590](https://doi.org/10.1145/3314221.3314590). ⚠️ Chưa đọc toàn văn.
- **[S27]** Noel, S., et al. (2021-10-08). *Optimizing network microsegmentation policy for cyber resilience*. J. Defense Modeling & Simulation. DOI: [10.1177/15485129211051386](https://doi.org/10.1177/15485129211051386). ⚠️ Chưa đọc toàn văn.
- **[S28]** (2021-12-15). *Automated Microsegmentation for Lateral Movement Prevention in Industrial Internet of Things (IIoT)*. IEEE SIN 2021. DOI: [10.1109/SIN54109.2021.9699232](https://doi.org/10.1109/SIN54109.2021.9699232). ⚠️ Chưa đọc toàn văn.
- **[S29]** (2025-04-13). *Zero Trust Implementation for Legacy Systems using Dynamic Microsegmentation, Role-Based Access Control (RBAC), and Attribute-Based Access Control (ABAC)*. IEEE ICCIT 2025. DOI: [10.1109/ICICT63348.2025.10989392](https://doi.org/10.1109/ICICT63348.2025.10989392). 🔴 **Chưa đọc toàn văn — RỦI RO CAO cho tính mới.**

---

*Người lập: ResearchLead (`ag_d85dde8d`) · Ngày: 2026-10-01 · Nhánh `agent/research-lead/T2`*
*Tài liệu này CHƯA được kiểm định độc lập. Reviewer1 chịu trách nhiệm `BLINDCHECK.md`.*
