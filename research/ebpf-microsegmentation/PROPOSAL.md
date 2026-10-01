# PROPOSAL — Đề tài 2

## Vi phân đoạn động bằng eBPF cho Kubernetes: mô hình chi phí độ trễ – khả năng thực thi của chính sách zero-trust và kiểm chứng trên cụm thật

| Trường | Giá trị |
|---|---|
| Mã đề tài | `RL-T2-EBPF-SEG` |
| Người đề xuất | **ResearchLead** (`ag_d85dde8d`) — Trưởng nhóm Nghiên cứu |
| Ngày | 2026-10-01 |
| Lĩnh vực | Mạng & an ninh mạng; thiết kế hệ thống |
| Loại hình | Đo lường hệ thống trên cụm thật + thiết kế cơ chế |
| Trạng thái | ⏳ Chờ Reviewer1 kiểm định độc lập |
| Nhánh | `agent/research-lead/T2` |

---

## 1. Khoảng trống nghiên cứu

### 1.1. Cái đã biết — và biết khá chắc

Budigiri và cộng sự (S6, EuCNC/6G Summit 2021, **đã đọc toàn văn**) đã đo chi phí của chính sách mạng Kubernetes trên các giải pháp dùng eBPF (Calico, Cilium). Trừu tượng của họ kết luận nguyên văn:

> *"…that network policies incur a negligible performance overhead which only varies slightly with the number of policies and for different policy recipes."* (dòng 46–48 của bản trích xuất — xem `../EVIDENCE/quote_extracts.txt` mục B)

Họ cũng tự khẳng định vị trí của mình: *"this paper is the first to investigate both performance overheads and security implications of K8s network policies specifically"*.

Nghĩa là: **câu hỏi "chính sách mạng có đắt không?" về cơ bản đã được trả lời là "không đắt lắm" — cho chính sách TĨNH.**

### 1.2. Ba khoảng trống cụ thể

**G1 — Chưa đo vòng lặp ĐỘNG.** Công trình trên (và các công trình đo lường liên quan) đo chính sách ở trạng thái **tĩnh**: nạp chính sách, đo, kết luận. Nhưng zero-trust theo định nghĩa của NIST SP 800-207 (S4, đã đọc trừu tượng chính thức) là *"an evolving set of cybersecurity paradigms that move defenses from static, network-based perimeters to focus on users, assets, and resources"* — tức là **thay đổi liên tục**. Câu hỏi chưa được trả lời: khi **danh tính của workload thay đổi** (pod khởi động lại, nhãn đổi, service account đổi), thì **thời gian hội tụ** từ lúc sự kiện xảy ra đến lúc chính sách mới được thực thi ở tất cả các nút là bao nhiêu? Trong cửa sổ hội tụ đó, hệ thống đang ở trạng thái nào?

**G2 — Chưa đo được chi phí theo LỚP chính sách trong cùng một thí nghiệm.** Tài liệu chính thức của Cilium (S5, đã đọc) cho thấy chính sách được chia thành các lớp L3 (danh tính endpoint, CIDR), L4 (cổng, ICMP, SNI), và L7 (HTTP, DNS) — mỗi lớp có chi phí khác nhau. Chưa có phép đo công khai nào đặt **L3 vs L4 vs L7 trong cùng một ma trận**, cùng một cụm, cùng một tải, để trả lời: *cái giá của việc nâng một quy tắc từ L3 lên L7 là bao nhiêu?*

**G3 — Chưa có mô hình chi phí kiểm chứng được cho "vi phân đoạn động".** Noel và cộng sự (S27, chỉ metadata) tối ưu chính sách vi phân đoạn **ngoại tuyến** (offline). Các công trình khác (S28, S29) chỉ metadata. Chưa thấy mô hình nào nối **tần suất thay đổi danh tính** với **chi phí thực thi** và **kích thước cửa sổ hội tụ** thành một thứ dự đoán được.

---

## 2. Câu hỏi nghiên cứu

| Mã | Câu hỏi | Cách trả lời |
|---|---|---|
| **RQ1** | Khi danh tính workload thay đổi, chính sách vi phân đoạn mới hội tụ trong bao lâu, đo từ sự kiện đến khi mọi nút thực thi? | Đo trên cụm thật; dựng bộ phát sự kiện và bộ dò trạng thái thực thi |
| **RQ2** | Chi phí độ trễ của chính sách L3, L4 và L7 khác nhau thế nào trong cùng một cụm, cùng một tải? | Ma trận thí nghiệm theo lớp chính sách |
| **RQ3** | Trong cửa sổ hội tụ, chính sách cũ hay mới đang có hiệu lực — và có khoảng hở nào không? | Phân tích log thực thi + chủ động kiểm tra luồng trong cửa sổ |
| **RQ4** | Có mô hình nào dự đoán được chi phí và cửa sổ hội tụ từ tần suất thay đổi danh tính và số lượng quy tắc không? | Xây mô hình; kiểm định bằng dữ liệu để riêng (hold-out) |

**Giả thuyết làm việc (chưa kiểm chứng):**
- **H1:** Chính sách L7 có chi phí cao hơn L3/L4 một cách có ý nghĩa thống kê, và độ chênh lệch tăng theo số quy tắc.
- **H2:** Cửa sổ hội tụ phụ thuộc chủ yếu vào **số nút** và **tần suất sự kiện**, không phụ thuộc nhiều vào **kích thước chính sách**.
- **H3:** Tồn tại một khoảng hở (gap) đo được trong cửa sổ hội tụ mà kẻ tấn công di chuyển ngang (lateral movement) có thể lợi dụng.

> ⚠️ Ba giả thuyết trên là **dự đoán**. Kết quả thuộc về Reviewer1.

---

## 3. Phương pháp

### Pha P1 — Tổng quan tài liệu có hệ thống (2–3 tuần)
- Theo quy trình `literature-review` của bộ skill `nckh`.
- Tập trung vào: (a) đo lường hiệu năng eBPF/XDP; (b) chính sách mạng Kubernetes; (c) microsegmentation/zero-trust; (d) chi phí sidecar/service mesh.
- Đầu ra: ma trận claim ↔ nguồn, ghi rõ mức xác minh (xem `SOURCES.md`).

### Pha P2 — Đo lường trên cụm thật (8–12 tuần)

**Thiết kế thí nghiệm (sẽ chốt bằng module `experimental-design`):**

| Yếu tố | Mức |
|---|---|
| CNI / cơ chế thực thi | eBPF (Cilium hoặc tương đương) · iptables (đối chứng) |
| Lớp chính sách | Không chính sách (đối chứng) · L3 · L4 · L7 |
| Số quy tắc | 10 · 100 · 1.000 |
| Số nút | 3 · 5 · 10 |
| Tần suất thay đổi danh tính | 0 (tĩnh) · 1/phút · 10/phút · 100/phút |
| Mẫu tải | HTTP nhỏ · HTTP lớn · TCP thuần |
| Kiến trúc nút | x86_64 (bắt buộc) · ARM64 (nếu có) |

- Ghi ở mỗi ô: phân bố độ trễ (p50/p95/p99), thông lượng, CPU mỗi nút, **thời gian hội tụ**, và **trạng thái thực thi theo thời gian**.
- Thống kê: trung vị + khoảng tin cậy bootstrap; kiểm định phi tham số cho so sánh cặp; hiệu chỉnh đa so sánh; mô hình hoá hồi quy cho RQ4 với **tách tập huấn luyện/kiểm tra**.
- **Kiểm soát nhiễu:** mỗi ô chạy lặp; ghi lại phiên bản kernel, phiên bản CNI, và hash commit của CNI vào metadata.

### Pha P3 — Phân tích khoảng hở và đề xuất cơ chế (4–6 tuần)
- Đo và mô tả khoảng hở ở RQ3.
- Đề xuất cơ chế giảm khoảng hở (ví dụ: thực thi "đóng trước, mở sau" — default-deny được áp trước khi mở luồng mới).
- **Đánh giá cơ chế đề xuất bằng chính bộ đo của P2** — không đánh giá bằng lập luận.

### Tiêu chí thành công
1. Bộ script dựng cụm + chạy ma trận thí nghiệm, tái lập được.
2. Dữ liệu thô công khai (đã ẩn danh).
3. Mô hình RQ4 có sai số kiểm tra (test error) được báo cáo trung thực, kể cả khi sai số lớn.

---

## 4. Dữ liệu cần

| Nhóm | Mô tả | Nguồn | Trạng thái |
|---|---|---|---|
| D1 | Phân bố độ trễ/thông lượng theo ô thí nghiệm | Cụm tự dựng | Chưa có |
| D2 | Log sự kiện thay đổi danh tính + dấu thời gian | Kubernetes API / công cụ quan sát | Chưa có |
| D3 | Trạng thái thực thi chính sách theo thời gian trên từng nút | Công cụ quan sát của CNI | Chưa có |
| D4 | Tài nguyên tiêu thụ (CPU, bộ nhớ) mỗi nút | Bộ thu thập chỉ số | Chưa có |
| D5 | Mã nguồn cấu hình + script dựng cụm | Nhóm tự viết | Chưa có |

**Nguyên tắc:** không dùng dữ liệu sản xuất thật; nếu dùng cụm của tổ chức đối tác thì phải có uỷ quyền bằng văn bản và ẩn danh hoá trước khi vào repo.

---

## 5. Tính mới

1. **Phép đo vòng lặp động** (sự kiện → hội tụ → thực thi) thay vì đo chính sách tĩnh — theo hiểu biết của người đề xuất, đây là phần bị bỏ trống trong tập nguồn đã khảo sát.
2. **So sánh L3/L4/L7 trong cùng một ma trận**, cùng cụm, cùng tải.
3. **Đo và mô tả khoảng hở thực thi** trong cửa sổ hội tụ — có ý nghĩa an ninh trực tiếp.
4. **Mô hình chi phí dự đoán được**, kiểm định trên tập tách rời.

**Đối thủ gần nhất ở tầng datapath (2026):** Netkit (S30, eBPF'26 Workshop, 2026-09-29) tối ưu chính **đường truyền giữa container trong cùng máy chủ** bằng eBPF, tích hợp vào Cilium, với phát biểu cải thiện thông lượng *"up to 37%"*. Đề tài này khác ở chỗ: Netkit giải bài toán **hiệu năng datapath**, còn đề tài này giải bài toán **chi phí hội tụ và khoảng hở thực thi của chính sách động**. Hai bài toán bổ trợ, không trùng — nhưng Reviewer1 phải xác nhận điều này bằng cách đọc toàn văn S30.

> ⚠️ **Tự cảnh báo:** khẳng định "chưa ai làm" dựa trên việc **không tìm thấy** trong 3 nguồn tìm kiếm, không phải trên một tìm kiếm có hệ thống. Giống đề tài 1, đây là điểm yếu phải được Reviewer1 kiểm tra độc lập. Xem `LITREVIEW.md` §6.

---

## 6. Rủi ro & đối sách

| # | Rủi ro | Khả năng | Tác động | Đối sách |
|---|---|---|---|---|
| R1 | Hành vi phụ thuộc mạnh vào phiên bản kernel/CNI → kết quả không tổng quát | **Cao** | Cao | Ghim phiên bản; chạy tối thiểu 2 phiên bản kernel; khai báo rõ phạm vi |
| R2 | eBPF verifier từ chối chương trình → không dựng được kịch bản | Trung bình | Trung bình | Có phương án dự phòng; ghi lại lỗi verifier làm bằng chứng |
| R3 | Không đủ tài nguyên để chạy 10 nút | Trung bình | Trung bình | Chạy quy mô 3–5 nút trước; 10 nút chỉ khi có tài trợ |
| R4 | Dữ liệu kết quả bị dùng để tuyên bố "zero-trust là an toàn" một cách sai lệch | Trung bình | Cao | Bắt buộc có mục "giới hạn và điều kiện áp dụng"; nêu rõ khoảng hở nếu đo được |
| R5 | **Rủi ro đạo đức:** kết quả mô tả khoảng hở có thể bị dùng làm hướng dẫn tấn công | Thấp | Cao | Công bố ở mức mô tả hiện tượng + khuyến nghị giảm thiểu; **không** công bố quy trình khai thác từng bước; báo trước cho nhà cung cấp CNI nếu phát hiện lỗ hổng cụ thể |
| R6 | H2 sai (cửa sổ hội tụ lại phụ thuộc kích thước chính sách) | Trung bình | Thấp | Đây là kết quả âm tính hợp lệ — phải báo cáo, không được giấu |

---

## 7. Venue / nguồn tài trợ tiềm năng

> **Đề xuất, chưa có cam kết nào.**

| Loại | Venue | Căn cứ |
|---|---|---|
| Hội nghị | ACM SIGCOMM / CoNEXT; USENIX ATC; IEEE/IFIP IM & NOMS | Nơi đã công bố công trình eBPF/XDP (S22) và chính sách K8s (S6) |
| Tạp chí | *IEEE Access*; *Journal of Network and Systems Management*; *IEEE Trans. Network and Service Management* | Tiền lệ khảo sát eBPF (S23) và quản lý hệ thống mạng |
| Cộng đồng | KubeCon / CloudNativeCon; CNCF | Nơi vấn đề này có khán giả thực hành |

**Tài trợ tiềm năng (chưa liên hệ):** CNCF; nhà cung cấp cloud/hạ tầng container; chương trình an ninh mạng quốc gia; quỹ nghiên cứu học thuật; nhà cung cấp giải pháp bảo mật container.

---

## 8. Chi phí ước tính

| Hạng mục | Ước tính | Ghi chú |
|---|---|---|
| Nhân lực nghiên cứu | 12–18 người-tháng | P1: 2–3 · P2: 8–11 · P3: 2–4 |
| Hạ tầng cụm | 3–10 nút (máy ảo hoặc máy thật) + 1 máy điều khiển | Chưa có báo giá — `chưa xác minh` |
| Lưu trữ | < 100 GB | Log + số liệu chỉ số |
| Chi phí truy cập tài liệu | Không xác định | Không có quyền truy cập CSDL trả phí |
| Chi phí công bố (nếu tạp chí mở) | `chưa xác minh` | Phụ thuộc venue |

**Tổng nhân lực: 13–20 người-tháng.** Chi phí tiền tệ: `chưa xác minh`.

---

## 9. Sản phẩm giao nộp

1. Bài báo (hội nghị hoặc tạp chí).
2. Bộ script dựng cụm + chạy ma trận thí nghiệm, tái lập một lệnh.
3. Dữ liệu thô đã ẩn danh.
4. Mô hình dự đoán RQ4 + báo cáo sai số kiểm tra.
5. `BLINDCHECK.md` đã được Reviewer1 điền.
6. Nếu phát hiện vấn đề an ninh cụ thể: báo cáo riêng cho nhà cung cấp **trước** khi công bố.

---

## 10. Tự đánh giá thẳng thắn của người đề xuất

- **Không có cụm Kubernetes nào đang chạy.** Toàn bộ §3 P2 là **thiết kế**. Không có một số liệu nào của đề tài này đã được sinh ra.
- Con số duy nhất được trích trong §1.1 đến từ **nguồn đã đọc toàn văn** (S6), có số dòng dẫn chứng.
- Đề tài này có **rủi ro tái lập cao hơn** đề tài 1, vì kết quả phụ thuộc phiên bản kernel/CNI. Người đề xuất đánh giá đề tài này **khó hơn** đề tài 1 (xem `../RANKING.md`).
- Người đề xuất **không tự kiểm định** tài liệu này.
