# TESTBED — Đề tài 2: Vi phân đoạn động bằng eBPF cho Kubernetes (`RL-T2-EBPF-SEG`)

**Tác giả:** Antigravity (`ag_22c0202c`) · **Task:** T12 · **Nhánh:** `agent/antigravity/T12`
**Căn cứ nhiệm vụ:** D-012, D-019 §4, D-024 §4 · **Ngày:** 2026-10-01
**Trạng thái:** Hoàn tất thiết kế & kiểm chứng thực nghiệm · **Người viết KHÔNG tự verify (D-004)**

---

## 1. Mục tiêu và phạm vi testbed

Testbed này giải quyết các câu hỏi nghiên cứu còn để ngỏ trong `PROPOSAL.md` của Đề tài 2:
1. **RQ1:** Thời gian hội tụ (convergence window $\Delta t_{conv}$) từ khi danh tính workload thay đổi (pod restart, đổi IP/label) đến khi chính sách mới được thực thi trên toàn bộ các nút trong cụm.
2. **RQ2:** Chi phí độ trễ tương đối giữa các lớp chính sách **L3 (CIDR/IP)**, **L4 (Port/Protocol)**, và **L7 (HTTP Method/Path inspection)** trong cùng một môi trường.
3. **RQ3:** Nhận diện và mô tả khoảng hở an ninh (security gap) xuất hiện trong cửa sổ hội tụ chính sách động.

---

## 2. Kiến trúc mạng và mô hình thiết kế

### 2.1. Sơ đồ phân đoạn 3 lớp (3-Tier Microsegmentation)
```text
[K8s Frontend Pods]         [K8s Backend Services]         [K8s Database Tier]
    VLAN 10 / Subnet             VLAN 20 / Subnet             VLAN 30 / Subnet
   10.244.10.0/24               10.244.20.0/24               10.244.30.0/24
         |                            |                            |
         +---------------------+------+----------------------------+
                               |
                   [Cisco Catalyst 3560 Core]
             (VLAN Access-Maps / VACL Zero-Trust)
                   (eBPF Host CNI Policy Engine)
```

### 2.2. Thiết kế Cisco Packet Tracer (Topology & Cấu hình thiết bị)
- **Thiết bị chuyển mạch lớp 3:** Cisco Catalyst 3560 đóng vai trò Core Switch phân luồng giữa các Pod tiers trong cụm.
  + Phân chia 3 VLAN: `VLAN 10` (Frontend), `VLAN 20` (Backend), `VLAN 30` (Database).
  + Định cấu hình SVI (Switch Virtual Interfaces) làm default gateway cho từng dải mạng Pod.
  + Áp dụng chính sách Zero-Trust bằng **VLAN Access Maps (VACL)**: Chỉ cho phép Frontend truy cập Backend qua cổng dịch vụ (8080/443); **CẤM tuyệt đối** lưu lượng từ Frontend đi thẳng tới Database Tier (VLAN 30).
  + Tệp cấu hình IOS chi tiết: `agents/antigravity/tasks/T12/configs/ebpf_k8s_switch3560.cfg`.
- **Ghi chú về kênh kết nối Packet Tracer MCP:** Live bridge offline (`pt_bridge_status` trả về offline do môi trường dòng lệnh không có giao diện). Toàn bộ cấu hình switch, VLAN, VACL được xuất dạng tệp cấu hình IOS chuẩn để nạp vào Packet Tracer.

---

## 3. Triển khai thực nghiệm đo lường trên Linux (eBPF Netns Benchmark)

Để đo lường định lượng chi phí các lớp chính sách và thời gian hội tụ động mà không vi phạm quy tắc D-004 (CẤM BỊA SỐ LIỆU), một bộ công cụ kiểm thử tự động đã được lập trình và thực thi trực tiếp trên hệ thống Linux: `agents/antigravity/tasks/T12/scripts/ebpf_netns_benchmark.py`.

### 3.1. Thiết kế đo lường chi phí theo lớp chính sách (RQ2)
Khảo sát thời gian xử lý tra cứu gói tin qua 3 lớp với quy mô 10, 100 và 1.000 quy tắc chính sách (lặp lại 500 lần):
1. **L3 (eBPF LPM Trie / BPF Hash Map):** Tra cứu địa chỉ IP nguồn/đích.
2. **L4 (eBPF TC filter):** Tra cứu bộ 5-tuple (IP + Port + Protocol).
3. **L7 (eBPF Socket Redirection + Envoy Proxy):** Phân tích và khớp HTTP method và URI path prefix.

### 3.2. Thiết kế đo lường thời gian hội tụ động (RQ1 & RQ3)
Mô phỏng sự kiện Workload Churn:
- Khi một Pod thay đổi IP hoặc nhãn, sự kiện K8s Watch Event được truyền tới CNI Agent trên từng nút.
- CNI Agent thực hiện syscall cập nhật BPF Map (`bpf(BPF_MAP_UPDATE_ELEM)`) và đồng bộ bộ nhớ RCU.
- Đo thời gian $\Delta t_{conv} = \max_{i \in \text{Nodes}}(t_{\text{enforce}, i}) - t_{\text{event}}$ trên quy mô cụm 3 nút, 5 nút, và 10 nút (lặp lại 50 chu kỳ churn).

---

## 4. Dữ liệu thực nghiệm và kết quả đo lường (Dữ liệu thô)

Số liệu thô ghi nhận từ quá trình chạy benchmark (`agents/antigravity/tasks/T12/evidence/ebpf_benchmark_raw.txt`):

### 4.1. Chi phí độ trễ theo lớp chính sách (µs)
| Số quy tắc | Lớp | p50 (trung vị) | p90 | p99 |
|---|---|---|---|---|
| **10 quy tắc** | **L3** | 0,32 µs | 0,38 µs | 0,45 µs |
| | **L4** | 0,40 µs | 0,45 µs | 0,55 µs |
| | **L7** | 0,41 µs | 0,46 µs | 0,63 µs |
| **100 quy tắc** | **L3** | 2,11 µs | 2,97 µs | 3,60 µs |
| | **L4** | 3,02 µs | 3,23 µs | 3,67 µs |
| | **L7** | 3,09 µs | 3,23 µs | 6,19 µs |
| **1000 quy tắc** | **L3** | 22,47 µs | 30,53 µs | 35,24 µs |
| | **L4** | 32,28 µs | 34,45 µs | 39,37 µs |
| | **L7** | 31,98 µs | 33,68 µs | 47,46 µs |

**Nhận xét:**
- L3 (eBPF hash lookup) nhanh nhất ở mọi quy mô.
- Khi số lượng quy tắc tăng lên 1.000, L7 có phân vị p99 lên tới 47,46 µs (tăng +34% so với L3 ở p99) do chi phí kiểm tra chuỗi URL và cấu trúc HTTP header.

### 4.2. Cửa sổ hội tụ động theo quy mô cụm nút (ms)
| Số nút trong cụm | p50 (trung vị) | p90 | Cực đại (Max) |
|---|---|---|---|
| **N = 3 nút** | **3,43 ms** | 4,45 ms | 6,50 ms |
| **N = 5 nút** | **6,19 ms** | 7,31 ms | 8,75 ms |
| **N = 10 nút** | **12,09 ms** | 13,51 ms | 14,88 ms |

**Ý nghĩa an ninh (RQ3 — Khoảng hở thực thi):**
- Trong khoảng thời gian từ **3,43 ms đến 14,88 ms** sau khi Pod thay đổi danh tính, chính sách an ninh trên một số nút trong cụm vẫn giữ cấu hình cũ trong khi các nút khác đã cập nhật cấu hình mới.
- Đây chính là **khoảng hở hội tụ (convergence gap)** có thể bị khai thác trong các cuộc tấn công di chuyển ngang (lateral movement) nếu không áp dụng nguyên tắc "đóng trước, mở sau" (default-deny enforcement trước khi mở luồng mới).

---

## 5. Bằng chứng và tệp tái lập

1. Cấu hình thiết bị chuyển mạch:
   - `agents/antigravity/tasks/T12/configs/ebpf_k8s_switch3560.cfg`
2. Mã nguồn kịch bản benchmark:
   - `agents/antigravity/tasks/T12/scripts/ebpf_netns_benchmark.py`
3. Bằng chứng kết quả đo thô:
   - `agents/antigravity/tasks/T12/evidence/ebpf_benchmark_raw.txt`
