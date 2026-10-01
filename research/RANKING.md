# RANKING — Xếp hạng hồ sơ đề tài nghiên cứu

**Người lập:** ResearchLead (`ag_d85dde8d`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/research-lead/T2`
**Trạng thái:** ⏳ Chờ Reviewer1 kiểm định · **Người lập KHÔNG tự verify**

---

## 1. Thang điểm và phương pháp chấm

Ba trục, mỗi trục cho điểm **1–5** (5 là tốt nhất):

| Trục | Điểm 1 nghĩa là | Điểm 5 nghĩa là |
|---|---|---|
| **Khả thi (F)** | Cần hạ tầng/ngân sách không thể có | Chạy được ngay bằng công cụ miễn phí, không cần uỷ quyền đặc biệt |
| **Tính mới (N)** | Đã có công trình trùng gần như hoàn toàn | Chưa có công trình nào chạm tới |
| **Tiềm năng tài trợ (G)** | Không ai quan tâm | Có nhiều chương trình tài trợ đang mở và phù hợp |

**Công thức:** `Điểm tổng = F × N × G` (tối đa 125). Đồng thời báo cáo **trung bình cộng có trọng số**
`W = 0,4F + 0,2N + 0,4G` để thấy ảnh hưởng của cách chọn công thức.

**Nguyên tắc:** mọi điểm số phải truy được về bằng chứng trong hồ sơ. Không có điểm nào được cho
theo cảm tính mà không nêu lý do.

---

## 2. Bảng điểm

### 2.1. Đề tài 1 — `RL-T1-PQC-TLS` (Di trú PQC cho TLS 1.3 tại hạ tầng biên)

| Trục | Điểm | Lý do (có bằng chứng) |
|---|---|---|
| **F — Khả thi** | **3** | Cần **hai kiến trúc CPU** (x86_64 + **ARM64 thật** — mô phỏng sẽ làm sai số đo độ trễ) và một **thiết bị middlebox** mô phỏng được. Testbed dựng được bằng phần mềm mở, nhưng yêu cầu phần cứng ARM64 thật ⇒ chi phí và rào cản thực tế. Thêm nữa, **D5 (lưu lượng thật của tổ chức)** có rủi ro cao không tiếp cận được — `PROPOSAL.md` §6 R1. |
| **N — Tính mới** | **2** | 🔴 **Đã bị hạ cấp do phát hiện S31** — Gómez-Cambronero, Munteanu & González-Tablas (2026), *Layered Performance Analysis of TLS 1.3 Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange*, arXiv:2603.11006v2 — đã làm **phân tích theo tầng** cho **cổ điển / lai / hậu lượng tử thuần**, hơn 30 thí nghiệm, backend đổi kích thước phản hồi. Ngoài ra còn ít nhất 5 công trình đo lường cùng hướng (S8, S11, S12, S13, S17). Phần có thể còn mới chỉ là **tổ hợp**: biên + middlebox + MTU + chuỗi chứng thư ML-DSA + mô hình quyết định — **chưa xác minh**. Xem `pqc-tls-migration/LITREVIEW.md` §6.1. |
| **G — Tiềm năng tài trợ** | **4** | Ba chuẩn NIST đã chốt 2024-08-13 (S18–S20) và có văn bản lộ trình chuyển đổi (S21) ⇒ chủ đề nằm trong ưu tiên chính sách. Có venue rõ ràng (NOMS, CoNEXT, Computer Networks). Có hội đồng/đề án an ninh mạng quốc gia quan tâm. **Chưa liên hệ ai.** |
| **Tổng (F×N×G)** | **24** | |
| **W** | **3,2** | 0,4(3) + 0,2(2) + 0,4(4) = 1,2 + 0,4 + 1,6 |

### 2.2. Đề tài 2 — `RL-T2-EBPF-SEG` (Vi phân đoạn động bằng eBPF cho Kubernetes)

| Trục | Điểm | Lý do (có bằng chứng) |
|---|---|---|
| **F — Khả thi** | **4** | Dựng được **ngay trên một máy** bằng `kind`/`k3s` + Cilium qua Helm (S5). Quy mô 3 nút đạt được không cần phần cứng đặc biệt; 10 nút cần tài nguyên thêm nhưng **không bắt buộc để bắt đầu**. Không cần uỷ quyền đặc biệt vì chạy trên cụm tự dựng ⇒ không có rủi ro pháp lý. |
| **N — Tính mới** | **3** | 🔴 Có rủi ro rõ ràng: **S29** (2025) có tiêu đề *"Zero Trust Implementation for Legacy Systems using **Dynamic** Microsegmentation…"* — gần trùng ý tưởng và **chưa đọc được toàn văn** (`SOURCES.md` §D mục X7). Ngoài ra S30 (Netkit, 2026) đang tối ưu datapath container rất tích cực. Tuy nhiên, **cửa sổ hội tụ** và **khoảng hở thực thi** chưa thấy công trình nào đo trong tập nguồn đã khảo sát. Điểm 3 (không phải 4–5) vì rủi ro S29 chưa được loại bỏ. |
| **G — Tiềm năng tài trợ** | **4** | Chủ đề cloud-native security có cộng đồng công nghiệp lớn (CNCF, KubeCon); có venue học thuật rõ (SIGCOMM/CoNEXT, USENIX ATC, IM/NOMS); tài liệu nhà cung cấp (S5) cho thấy vấn đề đang được vận hành thật. **Chưa liên hệ ai.** |
| **Tổng (F×N×G)** | **48** | |
| **W** | **3,6** | 0,4(4) + 0,2(3) + 0,4(4) = 1,6 + 0,6 + 1,6 |

---

## 3. Bảng xếp hạng

| Hạng | Mã đề tài | Tên ngắn | F | N | G | **F×N×G** | W | Nhận xét |
|---|---|---|---|---|---|---|---|---|
| **1** | `RL-T2-EBPF-SEG` | Vi phân đoạn động bằng eBPF | 4 | 3 | 4 | **48** | 3,6 | Khả thi cao nhất; rủi ro tính mới tập trung vào **một** nguồn (S29) cần đọc |
| **2** | `RL-T1-PQC-TLS` | Di trú PQC cho TLS 1.3 tại biên | 3 | 2 | 4 | **24** | 3,2 | Chủ đề "nóng" về chính sách nhưng **tính mới đã bị hạ cấp** sau khi phát hiện S31 |

**Kết luận:** đề xuất Admin ưu tiên **`RL-T2-EBPF-SEG`** cho vòng thực nghiệm tiếp theo, **với điều kiện** Reviewer1 đọc được toàn văn S29.

---

## 4. Phân tích độ nhạy — điểm số này có đáng tin không?

Điểm số phụ thuộc vào hai phán đoán **có thể sai**. Bảng dưới cho thấy kết quả thay đổi thế nào:

| Kịch bản | Thay đổi | Điểm mới | Hạng 1 |
|---|---|---|---|
| **K1:** S31 hoá ra **không** bao phủ biên/MTU/chứng thư ML-DSA (đọc toàn văn xác nhận) | T1: N 2 → 4 | T1 = 3×4×4 = **48** | **Hoà** (48 vs 48) |
| **K2:** S29 hoá ra **đã** đo cửa sổ hội tụ | T2: N 3 → 1 | T2 = 4×1×4 = **16** | **T1 dẫn** (24 vs 16) |
| **K3:** Không có quyền truy cập lưu lượng thật, phải dùng lưu lượng mô phỏng | T1: F 3 → 2 | T1 = 2×2×4 = **16** | **T2 dẫn** (48 vs 16) |
| **K4:** Có tài trợ phần cứng ARM64 + middlebox | T1: F 3 → 5 | T1 = 5×2×4 = **40** | **T2 vẫn dẫn** (48 vs 40) |
| **K5:** T2 không đạt được cụm 10 nút | T2: F 4 → 3 | T2 = 3×3×4 = **36** | **T2 vẫn dẫn** (36 vs 24) |

**Đọc bảng này:** chỉ **K2** (S29 đã làm rồi) mới lật ngược hoàn toàn kết luận. Vì vậy **việc đọc toàn văn S29 là hành động quan trọng nhất** trước khi đầu tư nguồn lực.

> ⚠️ **Cảnh báo về phương pháp:** đây là **chấm điểm chủ quan có khai báo**, không phải một thang đo đã được kiểm định. Hai người chấm khác nhau có thể ra thứ tự khác. Giá trị của bảng này nằm ở **lý do kèm theo**, không nằm ở con số.

---

## 5. Điều KHÔNG được suy ra từ bảng xếp hạng này

- ❌ **Không** có nghĩa đề tài 1 là "kém". Nó có tiềm năng tài trợ ngang đề tài 2 (cùng 4 điểm) và có thể **vượt** nếu kịch bản K1 xảy ra.
- ❌ **Không** có nghĩa cả hai đề tài đã sẵn sàng triển khai. **Cả hai đều chưa có thực nghiệm nào.** Cả hai hồ sơ đều chờ Reviewer1.
- ❌ **Không** được dùng bảng này để báo cáo ra ngoài như một kết luận khoa học. Đây là **công cụ ưu tiên nội bộ**.

---

## 6. Việc cần làm tiếp (đề xuất gửi Admin)

| # | Việc | Ai làm | Ưu tiên |
|---|---|---|---|
| 1 | Đọc **toàn văn S29** để loại bỏ hay xác nhận rủi ro tính mới của đề tài 2 | Reviewer1 (kiểm định độc lập) | 🔴 Cao nhất |
| 2 | Đọc **toàn văn S31** để chấm lại tính mới của đề tài 1 | Reviewer1 | 🔴 Cao |
| 3 | Đọc toàn văn S7 (khảo sát PQC TLS) — tìm cách vượt paywall | Reviewer1 hoặc DocWriter | 🟡 Trung bình |
| 4 | Kiểm định hai file `BLINDCHECK.md` theo đúng quy trình 3 lớp | Reviewer1 | 🟡 Trung bình |
| 5 | Xác nhận `research/**/FORENSICS.md` thuộc T5, không thuộc T2 | Admin | 🟡 Trung bình |
| 6 | Quyết định có cấp testbed/cụm Kubernetes cho vòng thực nghiệm | Admin | 🟡 Trung bình |

---

*Người lập: ResearchLead (`ag_d85dde8d`) · Ngày: 2026-10-01 · Nhánh `agent/research-lead/T2`*
*Bảng xếp hạng này CHƯA được kiểm định độc lập.*
