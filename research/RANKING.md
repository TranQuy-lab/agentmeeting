# RANKING — Xếp hạng hồ sơ đề tài nghiên cứu

**Người lập:** ResearchLead (`ag_d85dde8d`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/research-lead/T19`
**Cập nhật vòng T19:** chấm lại N của Đề tài 1 theo **bằng chứng dương** sau khi tự đọc toàn văn S31.
**Quyết định thứ tự đề tài:** do **Admin** chốt — xem §3b. Người lập **không tự chốt**.
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
| **N — Tính mới** | **4** | 🟢 **NÂNG LẠI theo BẰNG CHỨNG DƯƠNG (vòng T19), từ 2 lên 4.** Người lập **tự tải và đọc toàn văn HTML của S31** — Gómez-Cambronero, Munteanu & González-Tablas (2026), arXiv:2603.11006v2, **đã qua bình duyệt** (SPIQE 2026 / Euro S&P 2026, theo trường `arxiv:comment`). Đếm trên toàn văn (67.743 ký tự): `MTU`=0 · `middlebox`=0 · `fragment`=0 · `packet size`=0 · `network layer`=0 · `certificate chain`=0 · `tunnel`=0 · `VPN`=0; `edge`=1 nhưng ở **99,5% độ dài** (footer arXiv). S31 **tự liệt kê đúng khoảng hở của T1 vào *future work***: *"extending the analysis to real network environments with commercial load balancers and MiTM (Man-in-The-Middle) inspection devices…"*. **Không cho 5 điểm** vì phần lõi "đo hybrid so với cổ điển" **đã có người làm** (S31 và ít nhất 5 công trình khác: S8, S11, S12, S13, S17). Bằng chứng thô: `EVIDENCE/T19_checks.txt` mục VIỆC 2. |
| **G — Tiềm năng tài trợ** | **4** | Ba chuẩn NIST đã chốt 2024-08-13 (S18–S20) và có văn bản lộ trình chuyển đổi (S21) ⇒ chủ đề nằm trong ưu tiên chính sách. Có venue rõ ràng (NOMS, CoNEXT, Computer Networks). Có hội đồng/đề án an ninh mạng quốc gia quan tâm. **Chưa liên hệ ai.** |
| **Tổng (F×N×G)** | **48** | 3 × 4 × 4 |
| **W** | **3,6** | 0,4(3) + 0,2(4) + 0,4(4) = 1,2 + 0,8 + 1,6 |

### 2.2. Đề tài 2 — `RL-T2-EBPF-SEG` (Vi phân đoạn động bằng eBPF cho Kubernetes)

| Trục | Điểm | Lý do (có bằng chứng) |
|---|---|---|
| **F — Khả thi** | **4** | Dựng được **ngay trên một máy** bằng `kind`/`k3s` + Cilium qua Helm (S5). Quy mô 3 nút đạt được không cần phần cứng đặc biệt; 10 nút cần tài nguyên thêm nhưng **không bắt buộc để bắt đầu**. Không cần uỷ quyền đặc biệt vì chạy trên cụm tự dựng ⇒ không có rủi ro pháp lý. |
| **N — Tính mới** | **3** | 🔴 Có rủi ro rõ ràng: **S29** (2025) có tiêu đề *"Zero Trust Implementation for Legacy Systems using **Dynamic** Microsegmentation…"* — gần trùng ý tưởng và **chưa đọc được toàn văn** (`SOURCES.md` §D mục X7). Ngoài ra S30 (Netkit, 2026) đang tối ưu datapath container rất tích cực. Tuy nhiên, **cửa sổ hội tụ** và **khoảng hở thực thi** chưa thấy công trình nào đo trong tập nguồn đã khảo sát. Điểm 3 (không phải 4–5) vì rủi ro S29 chưa được loại bỏ. |
| **G — Tiềm năng tài trợ** | **4** | Chủ đề cloud-native security có cộng đồng công nghiệp lớn (CNCF, KubeCon); có venue học thuật rõ (SIGCOMM/CoNEXT, USENIX ATC, IM/NOMS); tài liệu nhà cung cấp (S5) cho thấy vấn đề đang được vận hành thật. **Chưa liên hệ ai.** |
| **Tổng (F×N×G)** | **48** | |
| **W** | **3,6** | 0,4(4) + 0,2(3) + 0,4(4) = 1,6 + 0,6 + 1,6 |

---

## 3. Bảng xếp hạng (điểm số)

| Hạng | Mã đề tài | Tên ngắn | F | N | G | **F×N×G** | W | Nhận xét |
|---|---|---|---|---|---|---|---|---|
| **=1** | `RL-T1-PQC-TLS` | Di trú PQC cho TLS 1.3 tại biên | 3 | **4** | 4 | **48** | 3,6 | Khoảng hở **được chứng minh CÒN MỞ bằng bằng chứng DƯƠNG** (S31 đã bình duyệt, tự nhận phần này là future work) |
| **=1** | `RL-T2-EBPF-SEG` | Vi phân đoạn động bằng eBPF | 4 | 3 | 4 | **48** | 3,6 | Khả thi cao hơn, nhưng rủi ro tính mới (**S29**) vẫn **CHƯA GIẢI QUYẾT** — không lấy được toàn văn |

**Hai đề tài HOÀ 48–48.** Điểm số **không** phân định được thứ tự ⇒ thứ tự phải do Admin chốt bằng tiêu chí khác. Xem §3b.

---

## 3b. QUYẾT ĐỊNH CỦA ADMIN — CHỐT THỨ TỰ ĐỀ TÀI

**Admin chốt (ghi tại `ADMIN/LOG.md` quyết định #35, `main@a1e026f`):**

> **`pqc-tls-migration` (RL-T1) là CHÍNH, `ebpf-microsegmentation` (RL-T2) là PHỤ.**

**Lý do — ghi NGUYÊN VĂN theo yêu cầu của Admin:**

> *"Reviewer1 chấm lại: hai đề tài **HOÀ 48–48**. Lý do chọn T1: khoảng hở của T1 được **chứng minh là CÒN MỞ** bằng bằng chứng DƯƠNG (S31 đã qua bình duyệt, tự liệt kê đúng khoảng hở của T1 vào *future work*), trong khi rủi ro của T2 (S29) là **CHƯA GIẢI QUYẾT** (toàn văn không lấy được). Bằng chứng dương về khoảng hở > rủi ro chưa xác minh."*

**Nguyên tắc rút ra:** **bằng chứng dương > rủi ro chưa xác minh.** Một khoảng hở được một công trình **đã qua bình duyệt** tự nhận là việc chưa làm là bằng chứng mạnh hơn một rủi ro "có thể có công trình trùng" mà ta chưa đọc được.

### ⚠️ ĐIỀU KIỆN ĐẢO (BẮT BUỘC ghi kèm — theo Admin)

> **Nếu sau này đọc được toàn văn S29 và S29 KHÔNG đo cửa sổ hội tụ ⇒ `RL-T2-EBPF-SEG` TRỞ LẠI HẠNG 1.**

Điều kiện này **phải được kiểm trước khi phân bổ nguồn lực thực nghiệm** cho T2. Ai đọc được S29 **phải** cập nhật lại mục này kèm bằng chứng thô.

---

## 4. Phân tích độ nhạy — điểm số này có đáng tin không?

Điểm số phụ thuộc vào những phán đoán **có thể sai**. Bảng dưới cho thấy kết quả thay đổi thế nào.
**Cột "Hạng 1" tính lại theo điểm số, KHÔNG theo quyết định §3b.**

| Kịch bản | Thay đổi | Điểm mới | Hạng 1 theo điểm số |
|---|---|---|---|
| **K1:** S31 hoá ra **có** bao phủ biên/MTU/chứng thư ML-DSA | T1: N 4 → 2 | T1 = 3×2×4 = **24** | **T2 dẫn** (48 vs 24) |
| **K2:** S29 hoá ra **đã** đo cửa sổ hội tụ | T2: N 3 → 1 | T2 = 4×1×4 = **16** | **T1 dẫn** (48 vs 16) |
| **K3:** Không có quyền truy cập lưu lượng thật, phải dùng lưu lượng mô phỏng | T1: F 3 → 2 | T1 = 2×4×4 = **32** | **T2 dẫn** (48 vs 32) |
| **K4:** Có tài trợ phần cứng ARM64 + middlebox | T1: F 3 → 5 | T1 = 5×4×4 = **80** | **T1 dẫn** (80 vs 48) |
| **K5:** T2 không đạt được cụm 10 nút | T2: F 4 → 3 | T2 = 3×3×4 = **36** | **T1 dẫn** (48 vs 36) |
| **K6:** S29 **KHÔNG** đo cửa sổ hội tụ (đọc được toàn văn) | T2: N 3 → 4 | T2 = 4×4×4 = **64** | **T2 dẫn** (64 vs 48) |

**Đọc bảng này:**
- **K1** và **K2** là hai kịch bản **có thể lật kết luận**. Nhưng **K1 nay đã bị loại bỏ bằng bằng chứng** (người lập đã tự đọc toàn văn S31 — xem §2.1). **K2 vẫn còn treo** vì S29 chưa lấy được toàn văn.
- **K4** cho thấy nếu có tài trợ phần cứng, T1 **vượt xa** T2 — đúng với quyết định §3b.
- **K6** là **điều kiện đảo** ở §3b được diễn đạt bằng số: nếu S29 không đo cửa sổ hội tụ, T2 vượt lên.

> ⚠️ **Cảnh báo về phương pháp:** đây là **chấm điểm chủ quan có khai báo**, không phải thang đo đã kiểm định. Hai người chấm khác nhau có thể ra thứ tự khác. Giá trị nằm ở **lý do kèm theo**, không nằm ở con số.

---

## 5. Điều KHÔNG được suy ra từ bảng xếp hạng này

- ❌ **Không** được suy ra rằng đề tài 1 "thắng" vì điểm cao hơn — **hai đề tài hoà 48–48**. Thứ tự T1 > T2 là **quyết định điều phối của Admin** (§3b) dựa trên *chất lượng bằng chứng*, không phải kết quả của công thức điểm.
- ❌ **Không** có nghĩa cả hai đề tài đã sẵn sàng triển khai. **Cả hai đều chưa có thực nghiệm nào.** Cả hai hồ sơ đều chờ Reviewer1.
- ❌ **Không** được dùng bảng này để báo cáo ra ngoài như một kết luận khoa học. Đây là **công cụ ưu tiên nội bộ**.

---

## 6. Việc cần làm tiếp (đề xuất gửi Admin)

| # | Việc | Ai làm | Ưu tiên | Trạng thái sau T19 |
|---|---|---|---|---|
| 1 | Đọc **toàn văn S29** để loại bỏ hay xác nhận rủi ro tính mới của T2. **Đây là điều kiện đảo ở §3b** | Reviewer1 / javis (có trình duyệt thật) | 🔴 Cao nhất | ⏳ CHƯA — toàn văn vẫn không lấy được |
| 2 | ~~Đọc toàn văn S31~~ | ~~Reviewer1~~ | — | ✅ **XONG** — chính người lập đã tự đọc ở T19; N của T1 đã ghi lại thành 4 |
| 3 | Đọc toàn văn S7 (khảo sát PQC TLS) — vượt paywall | Reviewer1 / javis / DocWriter | 🟡 Trung bình | ⏳ chưa |
| 4 | Kiểm định hai file `BLINDCHECK.md` theo quy trình 3 lớp | Reviewer1 | 🟡 Trung bình | ⏳ chưa |
| 5 | ~~Xác nhận `research/**/FORENSICS.md` thuộc T5~~ | ~~Admin~~ | — | ✅ **XONG** — Admin xác nhận tại `ADMIN/LOG.md` #26 |
| 6 | Cấp testbed mạng / cụm Kubernetes cho vòng thực nghiệm | Admin | 🟡 Trung bình | ⏳ chưa — Admin đã cấp slot 9/10 (`Antigravity`, `javis`) để bù rào cản này (`LOG.md` #24, #25) |
| 7 | Kiểm định độc lập file `EVIDENCE/T19_checks.txt` (bằng chứng sửa DOI + đọc S31) | Reviewer1 (T20) | 🟡 Trung bình | ⏳ mới tạo ở T19 |

---

*Người lập: ResearchLead (`ag_d85dde8d`) · Ngày: 2026-10-01 · Nhánh `agent/research-lead/T19`*
*Bảng xếp hạng này CHƯA được kiểm định độc lập. Người lập KHÔNG tự verify.*
