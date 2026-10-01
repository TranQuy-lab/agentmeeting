# T5 — Pháp y số & Phân tích Mã độc (phần CHUẨN BỊ)

**Agent:** ForensicsMal (`ag_82f7cb07`) · **Ngày:** 2025-10-01
**Nhánh:** `agent/forensics-mal/T5` · **Nền:** `main` @ `abe0c3e`

> ⚠️ **Chưa có mẫu.** Vòng này chỉ là **chuẩn bị**: kiểm kê công cụ thật + quy trình + khuôn báo cáo.
> Mọi kết quả điều tra cụ thể sẽ nằm trong `FORENSICS.md` của nhánh nghiên cứu/bounty tương ứng.

---

## Sản phẩm trong thư mục này

| Tệp | Nội dung |
|---|---|
| `FORENSICS_PROCEDURE.md` | **Quy trình 5 bước bất biến** + **khuôn báo cáo `FORENSICS.md`** + **danh sách kiểm tra trước khi kết luận** |
| `EVIDENCE/tool_inventory_raw.txt` | Output **thô** kiểm kê công cụ trên máy (A) |
| `EVIDENCE/tooling_bootstrap_raw.txt` | Output **thô** cài & **test chức năng** công cụ Python qua `uv` |
| `scripts/bootstrap_tools.sh` | Script tái lập môi trường công cụ, **không cần sudo** |
| `CHECKIN.md` | Bản lưu check-in đã gửi phòng (đối chiếu D-002) |

## Tóm tắt kết quả

- **Có sẵn:** Python 3.12.3, `sha256sum`/`sha1sum`/`md5sum`, `file`, `strings`, `xxd`,
  `objdump`/`readelf`/`nm`/`gdb`, `tshark` **4.2.2**, `tcpdump`, `git`, `curl`, `jq`, `unzip`, `uv` 0.12.13.
- **Đã bổ sung qua `uv` (đã test chức năng thật):** `volatility3` 2.28.2, `pefile` 2024.8.26,
  `scapy` 2.7.0, `capstone` **5.0.9 (metadata) / 5.0.7 (`__version__`)**, `yara-python` 4.5.4, `oletools` 0.60.2.
- **Vẫn thiếu (cần `sudo`/Admin):** `binwalk`, `foremost`, `yara` (CLI), `zeek`,
  `exiftool`, `steghide`, sleuthkit, `upx`, `7z`.
- **Chưa được coi là năng lực đã kiểm chứng:** phân tích **động** (chưa có môi trường cô lập),
  **memory forensics trên dump thật** (công cụ sẵn sàng nhưng chưa chạy lần nào).

## Ràng buộc tự áp đặt (theo D-004 + lệnh T5)

- ❌ Không sửa chứng cứ gốc — chỉ làm trên bản sao.
- ❌ Không chạy mẫu ngoài môi trường cô lập.
- ❌ Không push mẫu / dump / dữ liệu cá nhân thật lên repo.
- ❌ Không kết luận vượt bằng chứng (đặc biệt **attribution**).
- ❌ Không bịa IOC/hash/output — không chắc ghi nguyên văn `chưa xác minh`.

## Territory

Được ghi: `research/**/FORENSICS.md`, `security/**/FORENSICS.md`, `agents/forensicsmal/**`.
**Cấm** ghi ngoài territory. **Cấm** merge `main`.
