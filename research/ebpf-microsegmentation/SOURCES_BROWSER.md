# SOURCES_BROWSER — Truy hồi bằng trình duyệt/fetch từ VM độc lập (Task T13)

**Task:** T13 (D-012, msg #43; assignment msg #48) · **Agent:** javis (`ag_3bef07fd`)
**Ngày truy hồi:** 2026-10-01 · **Môi trường:** VM riêng của javis (`/home/hatch`), khác máy với ResearchLead.
**Danh sách nguồn:** `research/EVIDENCE/FETCH_STATUS.md` (nhánh `agent/research-lead/T2`).
**Quy ước:** trích dẫn là **nguyên văn** từ nội dung lấy được; không lấy được thì ghi `chưa xác minh`.

---

## S24 — Dissecting Overheads of Service Mesh Sidecars

- **URL gốc:** https://dl.acm.org/doi/pdf/10.1145/3620678.3624652
- **DOI:** `10.1145/3620678.3624652` · **Venue (Crossref):** *Proceedings of the 2023 ACM Symposium on Cloud Computing* (SoCC '23), 2023
- **Tác giả (Crossref):** Zhu Xiangfeng, She Guozhen, Xue Bowen, Zhang Yu, Zhang Yongsu, Zou Xuan Kelvin, Duan XiongChun, He Peng, Krishnamurthy Arvind, Lentz Matthew, Zhuo Danyang, Mahajan Ratul
- **Kết quả truy hồi:** ❌ **CHƯA XÁC MINH ĐƯỢC TOÀN VĂN / ABSTRACT.** Đã thử 3 kênh độc lập từ VM này:
  1. `curl -L` kèm User-Agent trình duyệt: HTTP **000** (không nhận được phản hồi).
  2. Fetch nội dung trang: HTTP **403** — cùng kết quả với ResearchLead.
  3. **Trình duyệt thật** (Chromium có giao diện): trang đích `https://dl.acm.org/doi/10.1145/3620678.3624652` dừng ở **thử thách Cloudflare "Thực hiện xác minh bảo mật"** với ô chọn "Xác minh bạn là con người". Theo luật không lách kiểm soát truy cập, trình duyệt **không** tự vượt qua thử thách; cần con người tự xác minh mới đọc tiếp được.
- **Những gì đã xác minh được:** metadata thư mục ở trên (qua Crossref API, 2026-10-01). Crossref **không có** abstract của bài này.
- **Kết luận đúng mức:** toàn văn và abstract của S24 vẫn là `chưa xác minh`. Không trích dẫn nội dung nào của bài này cho tới khi có kênh truy cập hợp lệ (quyền ACM DL hoặc người dùng tự qua bước xác minh Cloudflare).

---

## ebpf.io — What is eBPF?

- **URL gốc:** https://ebpf.io/what-is-ebpf/
- **Kết quả truy hồi:** ✅ **LẤY ĐƯỢC TOÀN VĂN.**
  - ResearchLead: HTTP 200 nhưng nội dung bị cắt ngắn, không đủ để trích.
  - `curl -L` từ VM này: HTTP **200**, **340.219 bytes** HTML đầy đủ, trích xuất được toàn bộ nội dung trang.
- **Trích nguyên văn định nghĩa (mục "What is eBPF?"):**

> "eBPF is a revolutionary technology with origins in the Linux kernel that can run sandboxed programs in
> a privileged context such as the operating system kernel. It is used to safely and efficiently extend
> the capabilities of the kernel without requiring to change kernel source code or load kernel modules."

> "Historically, the operating system has always been an ideal place to implement observability,
> security, and networking functionality due to the kernel's privileged ability to oversee and control
> the entire system."

---

## Tổng kết đề tài eBPF

| Nguồn | Trạng thái tại ResearchLead | Trạng thái tại javis (2026-10-01) |
|---|---|---|
| S24 (ACM DL PDF) | 403 | ❌ Chưa xác minh — chặn ở cả 3 kênh (curl 000, fetch 403, trình duyệt thật vướng Cloudflare) |
| ebpf.io/what-is-ebpf | 200 nhưng bị cắt | ✅ Toàn văn 340.219 bytes |

Người viết file này **không tự verify** kết quả của mình (D-004) — chờ Reviewer1 kiểm chứng độc lập.
