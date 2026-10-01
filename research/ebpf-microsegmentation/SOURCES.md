# SOURCES — Đề tài `RL-T2-EBPF-SEG`

**Người lập:** ResearchLead (`ag_d85dde8d`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/research-lead/T2`

**Quy ước mức xác minh — đọc kỹ trước khi trích dẫn lại:**

| Nhãn | Nghĩa |
|---|---|
| 🟢 **TOÀN VĂN** | Đã tải được nội dung và **đọc thật**. Trích dẫn an toàn. |
| 🔵 **TRỪU TƯỢNG** | Đã tải **trừu tượng chính thức** từ API của nhà xuất bản (arXiv/OpenAlex). Được phép trích **phát biểu trong trừu tượng**, ghi rõ là trích trừu tượng. **Không** được trích chi tiết thân bài. |
| 🟡 **METADATA** | DOI/URL tồn tại thật, metadata khớp — **chưa đọc toàn văn lẫn trừu tượng**. Chỉ được nói "tồn tại và nói về chủ đề X". **Cấm trích số liệu/kết luận.** |
| 🔴 **CHƯA XÁC MINH** | Không xác minh được. **CẤM trích dẫn.** |

> Đề tài 1 dùng chung các nguồn S1–S21, S31 — xem `../pqc-tls-migration/SOURCES.md`.
> File này liệt kê **các nguồn dùng cho đề tài 2**, bao gồm cả những nguồn dùng chung.

---

## A. Nguồn mức 🟢 TOÀN VĂN

### S4 — NIST SP 800-207: Zero Trust Architecture
- **Tác giả:** Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly · **Ngày:** 2020-08-11 · **NIST**
- **DOI:** `10.6028/NIST.SP.800-207` — ✅ xác minh CrossRef (`../EVIDENCE/crossref_lookups.txt`)
- **URL:** https://csrc.nist.gov/pubs/sp/800/207/final
- **Trạng thái fetch:** ✅ HTTP 200; đã đọc **trừu tượng chính thức nguyên văn** trên trang CSRC.
- **Trích nguyên văn (từ trang CSRC đã fetch):**
  - *"zero trust (ZT) is the term for an evolving set of cybersecurity paradigms that move defenses from static, network-based perimeters to focus on users, assets, and resources."*
  - *"Authentication and authorization (both subject and device) are discrete functions performed before a session to an enterprise resource is established."*
  - *"Zero trust focuses on protecting resources (assets, services, workflows, network accounts, etc.), not network segments, as the network location is no longer seen as the prime component to the security posture of the resource."*
- **Dùng cho:** định nghĩa nền tảng zero-trust; và cảnh báo rằng vi phân đoạn chỉ là **cơ chế**, không phải toàn bộ kiến trúc ZT.

### S5 — Cilium: Overview of Network Policy (tài liệu chính thức)
- **Nhà xuất bản:** Cilium Authors · **Phiên bản:** Cilium 1.20.2 · **Trang cập nhật:** 2026-09-15
- **URL:** https://docs.cilium.io/en/stable/security/policy/
- **Trạng thái fetch:** ✅ HTTP 200; đã đọc nội dung.
- **Nội dung đã đọc (mô tả lại, không phải trích dẫn nguyên văn toàn bộ):**
  - Chính sách được phân lớp: **Layer 3** (endpoint/node/entity/CIDR/DNS), **Layer 4** (cổng, ICMP/ICMPv6, SNI), **Layer 7** (HTTP, DNS).
  - Cơ chế nạp: qua tài nguyên Kubernetes (`NetworkPolicy`, `CiliumNetworkPolicy`, `CiliumClusterwideNetworkPolicy`) hoặc nạp trực tiếp qua CLI/API của agent.
  - **Trích nguyên văn:** phương thức nạp trực tiếp *"is deprecated as of v1.18 and will be removed in v1.19"*, và *"does not automatically distribute policies to all agents"*.
- **Dùng cho:** căn cứ phân lớp chính sách (RQ2) và căn cứ cho giả thuyết rằng cơ chế phân phối chính sách là một mắt xích riêng có thể tạo độ trễ (RQ1/RQ3).

### S6 — Network Policies in Kubernetes: Performance Evaluation and Security Analysis
- **Tác giả:** Gerald Budigiri, Christoph Baumann, Jan Tobias Mühlberg, Eddy Truyen, Wouter Joosen · **Năm:** 2021-06-08 · **Venue:** EuCNC/6G Summit 2021
- **DOI:** `10.1109/EuCNC/6GSummit51104.2021.9482526` — ✅ xác minh CrossRef
- **URL toàn văn (bản tác giả):** https://lirias.kuleuven.be/retrieve/14e501bd-e6bb-41d6-bf72-360c4850443a
- **Trạng thái fetch:** ✅ HTTP 200, **718.671 bytes**, PDF 6 trang; `pdftotext -layout` → **440 dòng**; đã đọc trừu tượng + phần I.
- **Trích nguyên văn đã kiểm chứng** (`../EVIDENCE/quote_extracts.txt` mục B):
  - *"…that network policies incur a negligible performance overhead which only varies slightly with the number of policies and for different policy recipes."* (dòng 46–48)
  - *"…this paper is the first to investigate both performance overheads and security implications of K8s network policies specifically…"* (phần I)
  - *"…which host results were better by 8.7% and 10.7% for latency"* (dòng 161)
- **Dùng cho:** mốc so sánh chính; và là **ranh giới phạm vi** — bài này đo chính sách **tĩnh**.

---

## B. Nguồn mức 🔵 TRỪU TƯỢNG (đã tải trừu tượng chính thức)

### S30 — Netkit: Specializing Linux Packet Delivery for Container Networks
- **Tác giả:** Daniel Borkmann, Paul Chaignon · **Ngày:** 2026-09-16 · **Venue:** Proceedings of the 4th Workshop on eBPF and Kernel Extensions (eBPF'26), Prague, 2026-09-29, trang 83–89
- **DOI:** `10.1145/3837779.3838164` — ✅ xác minh CrossRef (`../EVIDENCE/crossref_lookups.txt`); ✅ xác minh arXiv `2609.18633v1`
- **URL:** https://arxiv.org/abs/2609.18633
- **Trạng thái fetch:** ✅ HTTP 200 qua arXiv API; **đã tải và đọc trừu tượng chính thức**. Toàn văn: **chưa mở** (cần quyền ACM DL).
- **Trích trừu tượng nguyên văn (có ghi rõ là trừu tượng):**
  - *"In this paper, we present netkit, an eBPF-based datapath that specializes the Linux networking stack to eliminate redundant backlog queue traversals during network namespace transitions."*
  - *"Our implementation in the Linux kernel, integrated with minimal changes to the Cilium network plugin for Kubernetes, improves throughput by up to 37% and achieves parity between container-to-container and process-to-process communications…"*
- **Dùng cho:** bằng chứng rằng **chi phí đường truyền giữa container vẫn là nút thắt đang được nghiên cứu tích cực trong 2026**, và rằng hướng "tối ưu datapath eBPF + tích hợp Cilium" là hướng **đang nóng** — có nghĩa là tính mới của đề tài 2 phải được bảo vệ cẩn thận hơn.
- ⚠️ **Con số "up to 37%" là phát biểu của tác giả S30, không phải kết quả của đề tài này.**

---

## C. Nguồn mức 🟡 CHỈ METADATA — **cấm trích số liệu/kết luận**

| Mã | Tài liệu | Tác giả (nếu biết) | DOI | Venue / Năm | Trích dẫn (OpenAlex) | Lý do chỉ metadata |
|---|---|---|---|---|---|---|
| S22 | The eXpress Data Path (XDP) | Høiland-Jørgensen, T., et al. | `10.1145/3281411.3281443` | ACM CoNEXT, 2018-12-04 | 327 | ACM DL chặn tải PDF (HTTP 403) |
| S23 | eBPF: A New Approach to Cloud-Native Observability, Networking and Security… | Soldani, D., et al. | `10.1109/ACCESS.2023.3281480` | IEEE Access, 2023 | 70 | Không tải được toàn văn |
| S24 | Dissecting Overheads of Service Mesh Sidecars | Zhu, X., et al. | `10.1145/3620678.3624652` | ACM SoCC, 2023-10-30 | 42 | ACM DL chặn PDF (HTTP 403) |
| S25 | Synthesizing safe and efficient kernel extensions for packet processing | — | `10.1145/3452296.3472929` | ACM SIGCOMM, 2021 | 30 | Không truy cập được |
| S26 | Simple and precise static analysis of untrusted Linux kernel extensions | — | `10.1145/3314221.3314590` | ACM PLDI, 2019 | 99 | Không truy cập được |
| S27 | Optimizing network microsegmentation policy for cyber resilience | Noel, S., et al. | `10.1177/15485129211051386` | J. Defense Modeling & Simulation, 2021-10-08 | 12 | Không có bản mở. **Trừu tượng** có đọc được qua OpenAlex — xem ghi chú bên dưới |
| S28 | Automated Microsegmentation for Lateral Movement Prevention in Industrial Internet of Things (IIoT) | — | `10.1109/SIN54109.2021.9699232` | IEEE SIN, 2021-12-15 | 18 | Không đọc toàn văn. **Trừu tượng** đọc được qua OpenAlex |
| S29 | Zero Trust Implementation for Legacy Systems using Dynamic Microsegmentation, RBAC, and ABAC | — | `10.1109/ICICT63348.2025.10989392` | IEEE ICCIT, 2025-04-13 | 9 | 🔴 **Không có bản mở. RỦI RO CAO cho tính mới — xem §D** |

**Ghi chú về trừu tượng OpenAlex:** với S27, S28, S29, người lập **có** đọc trừu tượng do OpenAlex cung cấp (lưu trong `EVIDENCE/openalex_queries.txt`). Tuy nhiên các trừu tượng này **không đầy đủ** như trừu tượng chính thức của nhà xuất bản (OpenAlex tái tạo từ chỉ mục ngược). Vì vậy các nguồn này vẫn bị xếp mức 🟡 và **không được trích số liệu**.

Ví dụ trừu tượng đã đọc:
- **S27:** *"This paper describes an approach for improving cyber resilience through the synthesis of optimal microsegmentation policy for a network. By leveraging microsegmentation security architecture, we can reason about fine-grained policy rules that enforce access for given combinations of source address, destination address, destination port…"*
- **S28:** *"The integration of the IoT network with the Operational Technology (OT) network is increasing rapidly. However, this incorporation of IoT devices into the OT network makes the industrial control system vulnerable to various cyber threats. Hacking an IoT device at the network edge, an attacker can move laterally to compromise the…"*
- **S29:** *"This paper… addresses the critical cybersecurity challenges legacy systems pose. Legacy infrastructures, integral to numerous organizations, exhibit vulnerabilities d…"*

---

## D. 🔴 CHƯA XÁC MINH — **CẤM TRÍCH DẪN**

| # | Thứ bị nghi | Kết quả kiểm tra | Kết luận |
|---|---|---|---|
| X6 | `arXiv:2609.18633` | Ban đầu người lập tưởng không xác minh được. Kiểm lại với `curl -L` → **TỒN TẠI THẬT** | 🟢 **ĐÃ SỬA SAI.** Trở thành nguồn **S30** (mức 🔵). Nguyên nhân lỗi: `http://export.arxiv.org/api/` trả HTTP 301, phải dùng `-L`. |
| X7 | Nguồn S29 (Zero Trust… **Dynamic** Microsegmentation, 2025) — **nội dung toàn văn** | Không có bản mở; không truy cập được | 🔴 **Lỗ hổng bằng chứng nghiêm trọng.** S29 có tiêu đề gần như trùng ý tưởng đề tài. **Không được trích** cho tới khi có toàn văn. |

---

## E. Nguồn đã cố fetch nhưng **THẤT BẠI**

| URL | Kết quả | Ghi chú |
|---|---|---|
| `https://dl.acm.org/doi/pdf/10.1145/3620678.3624652` | ❌ HTTP **403** | Nguồn S24 |
| `https://dl.acm.org/doi/pdf/10.1145/3281411.3281443` | ❌ không tải được | Nguồn S22 |
| `https://ebpf.io/what-is-ebpf/` | ⚠️ HTTP 200 nhưng nội dung **bị cắt ngắn**, không đủ để trích | Không dùng làm nguồn |
| `https://ieeexplore.ieee.org/ielx7/6287639/10005208/10138542.pdf` | ❌ không tải được | Nguồn S23 |
| `https://lirias.kuleuven.be/retrieve/14e501bd-…` qua `web_fetch` | ❌ `unsupported content type "application/pdf"` | Nhưng **tải được bằng `curl`** → đã đọc toàn văn (S6) |
| `https://docs.cilium.io/en/stable/security/policy/` | ✅ HTTP 200 | Thành công (S5) |
| `https://csrc.nist.gov/pubs/sp/800/207/final` | ✅ HTTP 200 | Thành công (S4) |

**Tổng kết truy cập (Reviewer1 phải kiểm lại):**
- 🟢 Toàn văn: **3** nguồn (S4, S5, S6).
- 🔵 Trừu tượng chính thức: **1** nguồn (S30).
- 🟡 Metadata: **8** nguồn (S22–S29).
- 🔴 Không xác minh được: **1** nguồn có nội dung (S29 toàn văn).
- ❌ Fetch thất bại: **4** URL (trừ 2 dòng ✅).

---

## F. Phương pháp xác minh (tái lập được)

```bash
# 1) Metadata DOI
curl -s "https://api.crossref.org/works/10.1109/EuCNC/6GSummit51104.2021.9482526"
curl -s "https://api.openalex.org/works/https://doi.org/10.1177/15485129211051386"
# 2) Trừu tượng arXiv — BẮT BUỘC có -L vì endpoint trả HTTP 301
curl -sL "http://export.arxiv.org/api/query?id_list=2609.18633"
# 3) Toàn văn PDF mở
curl -sL "https://lirias.kuleuven.be/retrieve/14e501bd-e6bb-41d6-bf72-360c4850443a" -o k8s_policies.pdf
pdftotext -layout k8s_policies.pdf k8s.txt && wc -l k8s.txt
# 4) Tài liệu chính thức
curl -s "https://docs.cilium.io/en/stable/security/policy/"
```

Công cụ: `curl`, `python3`, `pdftotext` (poppler), `web_search`, `web_fetch`.
Không dùng CSDL trả phí. Không trích từ trí nhớ. Danh sách tác giả xác minh qua OpenAlex (`../EVIDENCE/openalex_authors.txt`).
