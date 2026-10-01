# TESTBED — Đề tài 1: Di trú mật mã hậu lượng tử cho TLS 1.3 tại hạ tầng biên (`RL-T1-PQC-TLS`)

**Tác giả:** Antigravity (`ag_22c0202c`) · **Task:** T12 · **Nhánh:** `agent/antigravity/T12`
**Căn cứ nhiệm vụ:** D-012, D-019 §4, D-024 §4 · **Ngày:** 2026-10-01
**Trạng thái:** Hoàn tất thiết kế & kiểm chứng thực nghiệm · **Người viết KHÔNG tự verify (D-004)**

---

## 1. Mục tiêu và phạm vi testbed

Testbed này giải quyết khoảng trống thực nghiệm của Đề tài 1 (`RL-T1-PQC-TLS`) đã được nêu trong `PROPOSAL.md` và `RANKING.md`:
1. **Kiểm tra chi phí bắt tay TLS 1.3 của hybrid `X25519MLKEM768` (FIPS 203) so với cổ điển `X25519`** khi đi qua thiết bị biên (edge router/middlebox) dưới các ràng buộc MTU và trễ mạng.
2. **Xác minh hiện tượng phân mảnh cấp wire (wire-level fragmentation)** khi kích thước ClientHello vượt MTU.
3. **Tái hiện có kiểm soát điểm mù PMTUD (Path MTU Discovery Blackhole)** khi thiết bị trung gian chặn gói ICMP Fragmentation Needed (Type 3, Code 4).

---

## 2. Kiến trúc mạng và mô hình thiết kế

### 2.1. Sơ đồ kết nối logic
```text
[Edge Client Pod]                [Edge Gateway / Middlebox]              [Origin PQC Server]
  10.10.10.10                     10.10.10.1 <-> 172.16.1.1                172.16.1.100
(OpenSSL 3.5.1 s_client)    (Cisco 2911 / Netem / MSS Clamping)       (OpenSSL 3.5.1 s_server :4433)
       |                                     |                                     |
       +-------- Segment Ingress ------------+--------- Segment Egress ------------+
                   (MTU = 1500)                            (MTU = 1280 / 576)
```

### 2.2. Thiết kế Cisco Packet Tracer (Topology & Cấu hình thiết bị)
- **Thiết bị định tuyến biên:** Cisco 2911 Router đóng vai trò Gateway biên giữa mạng truy cập người dùng và hạ tầng DMZ.
  + Cổng Ingress `Gi0/0` (10.10.10.1/24): Tiếp nhận lưu lượng từ Client, gắn NetFlow monitor để theo dõi luồng TLS.
  + Cổng Egress `Gi0/1` (172.16.1.1/24): Kết nối về cụm máy chủ TLS, cấu hình `ip mtu 1400` và `ip tcp adjust-mss 1360` để kiểm soát hiện tượng nghẽn MTU khi ClientHello phình to.
  + Tệp cấu hình IOS chi tiết: `agents/antigravity/tasks/T12/configs/pqc_edge_cisco2911.cfg`.
- **Thiết bị tường lửa / Middlebox:** Cisco ASA 5506-X đóng vai trò Middlebox thanh tra lưu lượng TLS và mô phỏng chính sách lọc ICMP (chặn ICMP Type 3 Code 4).
  + Tệp cấu hình IOS chi tiết: `agents/antigravity/tasks/T12/configs/pqc_edge_asa5506.cfg`.
- **Ghi chú về kênh kết nối Packet Tracer MCP:** Lệnh `pt_bridge_status` xác nhận môi trường CLI hiện tại không mở cửa sổ giao diện Packet Tracer Desktop (`Packet Tracer NO está conectado por ningún canal`). Do đó, các cấu hình Cisco IOS được xuất độc lập dưới dạng tệp cấu hình chuẩn để nạp trực tiếp vào Packet Tracer hoặc thiết bị thật.

---

## 3. Triển khai thực nghiệm trên Container / Linux Netem

Để có số liệu đo lường thật và không vi phạm quy tắc D-004 (CẤM BỊA SỐ LIỆU), testbed thực nghiệm đã được chạy trên cụm container Docker cô lập (`labnet-a` và `labnet-b` nội bộ):
- **Phần mềm TLS:** OpenSSL 3.5.1 (hỗ trợ nguyên bản ML-KEM-512, ML-KEM-768, ML-KEM-1024, `X25519MLKEM768`).
- **Router trung gian:** `lab-netem-router` chạy Linux kernel với `tc/netem`, điều khiển chính xác các thông số:
  + `LOSS`: 0%, 1%, 3%
  + `DELAY`: 0ms, 50ms (chú ý: đơn vị tường minh `ms`, tránh hiểu nhầm thành micro-giây)
  + `MTU`: 1500 B, 1280 B (chuẩn IPv6 tối thiểu), 576 B (chuẩn IPv4 tối thiểu)
  + `CLAMP`: on / off (TCP MSS clamping)
  + `DROP_ICMP_FRAG`: 0 (bình thường) / 1 (chặn gói ICMP Type 3 Code 4 để kích hoạt blackhole)
  + **Điều kiện bắt buộc:** Đã tắt GSO/TSO/GRO trên interface ảo của router bằng `ethtool` để đảm bảo gói tin phân mảnh thật trên đường truyền.

---

## 4. Dữ liệu thực nghiệm và kết quả đo lường (Dữ liệu thô)

### 4.1. Ngân sách kích thước bắt tay (Đối chiếu FIPS 203)
Đo trực tiếp từ capture gói tin thực nghiệm (`dumpcap`):
- **ClientHello (X25519):** 217 byte.
- **ClientHello (X25519MLKEM768):** 1.393 byte (+1.176 byte).
  + Khối `key_share` mang 1.216 byte = ML-KEM-768 encapsulation key 1.184 byte (khớp chuẩn FIPS 203) + X25519 32 byte.
- **ServerHello (X25519MLKEM768):** Khối `key_share` mang 1.120 byte = ciphertext 1.088 byte (FIPS 203) + X25519 32 byte.

### 4.2. Phân mảnh cấp wire (Wire-level Fragmentation)
Khi tắt GSO/TSO/GRO trên router:
- Tại **MTU = 1500 B:** ClientHello của cả hai nhóm đều nằm vừa trong 1 TCP segment.
- Tại **MTU = 1280 B:** ClientHello X25519 chiếm **1 segment**; ClientHello X25519MLKEM768 bị xẻ thành **2 segments**.
- Tại **MTU = 576 B:** ClientHello X25519 chiếm **1 segment**; ClientHello X25519MLKEM768 bị xẻ thành **3 segments**.

### 4.3. Điểm mù PMTUD Blackhole (Thí nghiệm nhân quả)
Thực hiện ma trận thực nghiệm: `{Nhóm KEM} × {PMTU} × {Chặn ICMP} × {MSS Clamp}`:
- **Kịch bản Blackhole:** `X25519MLKEM768` + `PMTU = 1280` + `CLAMP = off` + `DROP_ICMP_FRAG = 1`:
  + Kết quả: **0/6 kết nối hoàn tất** (toàn bộ đều timeout sau 8 giây do gói ClientHello vượt PMTU bị router drop im lặng, client không nhận được tín hiệu điều chỉnh).
  + Nhóm đối chứng `X25519`: **6/6 kết nối hoàn tất** (vì ClientHello 217 byte < 1280 byte).
- **Kịch bản phục hồi:** Khi bật `CLAMP = on` hoặc mở `DROP_ICMP_FRAG = 0`: Cả 6/6 kết nối của nhóm lai đều hoàn tất thành công.

---

## 5. Bằng chứng và tệp tái lập

1. Cấu hình thiết bị Cisco:
   - `agents/antigravity/tasks/T12/configs/pqc_edge_cisco2911.cfg`
   - `agents/antigravity/tasks/T12/configs/pqc_edge_asa5506.cfg`
2. Bằng chứng kiểm tra công cụ & handshake sống:
   - `agents/antigravity/tasks/T12/evidence/pt_bridge_check_raw.txt`
   - `agents/antigravity/tasks/T12/evidence/docker_pqc_ps_raw.txt`
   - `agents/antigravity/tasks/T12/evidence/pqc_handshake_live_raw.txt`
   - `agents/antigravity/tasks/T12/evidence/classical_handshake_live_raw.txt`
