# [CHECK-IN] ForensicsMal

**Ngày:** 2025-10-01 (UTC 2026-10-01T13:46Z theo `date -u` trên máy)
**Phòng:** `ab1-478d-cfa7`
**Task:** T5 — phần CHUẨN BỊ (chưa có mẫu)

---

## 1. Định danh

| Trường | Giá trị |
|---|---|
| Tên | **ForensicsMal** |
| Agent ID | `ag_82f7cb07` |
| Slug / vai trò | `forensicsmal` — Pháp y số & phân tích mã độc |
| Nhánh Git | `agent/forensics-mal/T5` |
| Repo (clone riêng) | `/home/noble-tran/agentmeeting-forensicsmal` (SSH, commit nền `abe0c3e`) |
| Trạng thái join | ✅ đã join bằng `--rejoin`, chạy **đúng 1 lần** |

## 2. Skill đang nạp (tên + đường dẫn THẬT đã kiểm chứng)

| Skill | Đường dẫn thật | Trạng thái |
|---|---|---|
| `ctf-forensics` | `/home/noble-tran/.agents/skills/ctf-forensics/` | ✅ đã nạp |
| `ctf-malware` | `/home/noble-tran/.agents/skills/ctf-malware/` | ✅ đã nạp |
| `ctf-misc` | `/home/noble-tran/.agents/skills/ctf-misc/` | ✅ có, nạp khi challenge lệch category |
| `security-agent` | `/home/noble-tran/.agents/skills/security-agent/SKILL.md` | ✅ đã đọc (map MITRE ATT&CK) |
| Thư viện mở rộng | `/home/noble-tran/security-agent/` (`index.json`, `ATTACK_COVERAGE.md`, `skills/<name>/SKILL.md`) | ✅ có |

## 3. Chuyên môn

- **Chính:** pháp y số (disk / memory / network / log / registry) và phân tích mã độc tĩnh.
- **Phụ:** trích xuất IOC, dựng dòng thời gian, map **MITRE ATT&CK**, viết YARA rule.
- **Hỗ trợ hai nhánh:** điều tra cho cả `research/**` và `security/**` (bounty) khi có mẫu/log.

## 4. Điểm MẠNH (kèm bằng chứng THẬT)

1. **Python 3.12.3 sẵn sàng cho scripting pháp y** — đã tự viết được parser thô khi thiếu tool.
   *Bằng chứng:* `python3 --version` → `Python 3.12.3`.
2. **Chuỗi công cụ hạch toán hash & phân tích nhị phân cơ bản đầy đủ.**
   *Bằng chứng:* `/usr/bin/sha256sum`, `sha1sum`, `md5sum`, `file`, `strings`, `xxd`, `objdump`, `readelf`, `nm`, `gdb` — tất cả `CO`.
3. **Phân tích mạng PCAP làm được thật, không cần cài thêm.**
   *Bằng chứng:* `tshark --version | head -1` → `TShark (Wireshark) 4.2.2 (Git v4.2.2 packaged as 4.2.2-1.1build3).`; `tcpdump` → `/usr/bin/tcpdump`.
4. **Tự dựng được môi trường công cụ Python mà KHÔNG cần sudo** — đã cài & **test chức năng thật**
   `volatility3` 2.28.2, `pefile` 2024.8.26, `scapy` 2.7.0,
   `capstone` **5.0.9 (metadata)** / **5.0.7 (`__version__`)**,
   `yara-python` 4.5.4, `oletools` 0.60.2.
   *Bằng chứng:* `/home/noble-tran/.local/bin/uv` (uv 0.12.13) + `EVIDENCE/tooling_bootstrap_raw.txt`.
   *Riêng `capstone`:* hai số **5.0.9** (metadata) và **5.0.7** (`__version__`) **cả hai đều thật** —
   đo lại độc lập tại `agents/forensicsmal/T23/EVIDENCE/t23_capstone_version_recheck_raw.txt`
   (thi hành D-014 mục 2; T5 bản đầu ghi `5.0.9` trần, **thiếu nguồn**).
5. **Kỷ luật bằng chứng:** mọi kết luận gắn hash + lệnh + phiên bản; không chắc ghi `chưa xác minh`.

## 5. Điểm YẾU (lý do THẬT, không tô hồng)

1. **Máy TRẮNG công cụ pháp y hệ thống.** Thiếu `binwalk`, `foremost`, `yara` (CLI), `zeek`,
   `exiftool`, `steghide`, sleuthkit (`fls`/`icat`/`photorec`), `upx`, `7z`.
   *Bằng chứng:* `agents/forensicsmal/T5/EVIDENCE/tool_inventory_raw.txt`.
   → Hệ quả: **chưa** làm được **carving ảnh đĩa / phục hồi file xoá / stego**. Không có `yara` CLI
   ⇒ scan YARA phải qua Python API.
2. **Không có `pip`/`ensurepip`; `sudo` cần mật khẩu** ⇒ không cài được qua `apt`/`pip` truyền thống.
   *Bằng chứng:* `python3 -m pip` → `No module named pip`; `python3 -m ensurepip` → `No module named ensurepip`;
   `sudo -n true` → `sudo: a password is required`. **Đã vòng qua được bằng `uv`** (§6).
3. **`volatility3` MỚI CHỈ ĐƯỢC NẠP, CHƯA CHẠY TRÊN DUMP THẬT.** Plugin load OK nhưng chưa có
   memory dump nào để thực chiến ⇒ năng lực memory forensics của tôi là
   **"công cụ sẵn sàng, chưa thực chiến"**. Tôi **không** nhận mình thành thạo.
4. **Chưa từng chạy mẫu malware thật trong phiên này** ⇒ mọi năng lực động (dynamic analysis)
   hiện là **lý thuyết**, `chưa xác minh`. Và tôi **sẽ không** chạy mẫu ngoài môi trường cô lập.
5. **Chưa có bằng chứng về sandbox/cô lập trên máy này** — không có VM/container xác nhận.
   Đây là rào cản thật cho phép phân tích động.
6. **Hash/IP/domain nào tôi chưa tự tính thì tôi không dám khẳng định.**

## 6. Công cụ THẬT (bảng có/thiếu)

### 6a. Có sẵn trên hệ thống (không cần cài)

| Công cụ | Có/Thiếu | Bằng chứng |
|---|---|---|
| `python3` | ✅ có | 3.12.3, `/usr/bin/python3` |
| `sha256sum`/`sha1sum`/`md5sum` | ✅ có | `/usr/bin/` |
| `file`, `strings`, `xxd` | ✅ có | `/usr/bin/` |
| `objdump`, `readelf`, `nm`, `gdb` | ✅ có | `/usr/bin/` |
| `tshark` | ✅ có | **4.2.2** |
| `tcpdump` | ✅ có | `/usr/bin/tcpdump` |
| `git`, `curl`, `jq`, `unzip` | ✅ có | `/usr/bin/` |
| `uv` | ✅ có | `0.12.13`, `/home/noble-tran/.local/bin/uv` |

### 6b. ĐÃ BỔ SUNG qua `uv` (venv ngoài repo, KHÔNG cần sudo) — **đã test chức năng**

| Gói | Phiên bản | Test chức năng THẬT | Kết quả |
|---|---|---|---|
| `volatility3` | **2.28.2** | CLI `vol --help`; nạp plugin `windows.pslist` | 🟡 chạy được, **chưa có dump thật** |
| `pefile` | 2024.8.26 | parse `crackme.exe` | ✅ OK, machine=0x8664, 6 section |
| `scapy` | 2.7.0 | dựng gói Ether/IP/TCP | ✅ OK, 54 byte |
| `capstone` | **5.0.9 (metadata)** / **5.0.7 (`__version__`)** | disasm x86-64 | ✅ `mov rbp,rsp` / `mov eax,0` |
| `yara-python` | 4.5.4 | compile rule + scan file | ✅ OK, khớp rule |
| `oletools` | 0.60.2 | CLI `olevba --help` | ✅ OK |

*Bằng chứng thô:* `agents/forensicsmal/T5/EVIDENCE/tooling_bootstrap_raw.txt`
*Tái lập:* `agents/forensicsmal/T5/scripts/bootstrap_tools.sh`

### 6c. VẪN THIẾU (cần `sudo`/Admin — tôi KHÔNG tự cài được)

| Công cụ | Trạng thái | Bằng chứng |
|---|---|---|
| `binwalk` | ❌ **thiếu** | `command -v` rỗng |
| `foremost` | ❌ **thiếu** | `command -v` rỗng |
| `yara` (CLI) | ❌ **thiếu** | `command -v` rỗng (chỉ có `yara-python`) |
| `zeek` | ❌ **thiếu** | `command -v` rỗng |
| `exiftool`, `steghide` | ❌ **thiếu** | `command -v` rỗng |
| sleuthkit (`fls`/`icat`/`photorec`) | ❌ **thiếu** | `command -v` rỗng |
| `upx`, `7z` | ❌ **thiếu** | `command -v` rỗng |

## 7. NGOÀI KHẢ NĂNG / vướng ĐẠO ĐỨC (nói thẳng)

**Ngoài khả năng (hiện tại):**
- Carving ảnh đĩa / phục hồi file xoá (foremost, sleuthkit, photorec) — thiếu công cụ.
- Phân tích stego ảnh/âm thanh (steghide, exiftool) — thiếu công cụ.
- Firmware / binwalk-style extraction — thiếu công cụ.
- Phân tích động malware trong sandbox thật — chưa có môi trường cô lập được xác minh.
- Reverse engineering sâu / decompile .NET (`dnSpy` chỉ có trên Windows) — không có.
- **Memory forensics: công cụ đã có nhưng tôi CHƯA chạy dump thật** ⇒ chưa được coi là năng lực
  đã kiểm chứng; nếu nhận task này tôi cần mẫu nhỏ để luyện và sẽ báo kết quả thô.

**Vướng ĐẠO ĐỨC — tôi TỪ CHỐI, kể cả khi được lệnh:**
- ❌ Chạy mẫu malware trên máy thật / ngoài môi trường cô lập.
- ❌ Sửa đổi chứng cứ gốc — chỉ làm trên bản sao.
- ❌ Trích dẫn nguyên văn **dữ liệu cá nhân** thật (PII) — phải che/mã hoá.
- ❌ Push mẫu malware / dump / dữ liệu thật lên repo.
- ❌ Kết luận vượt bằng chứng, đặc biệt **attribution** ("có thể là APT", "do nhóm X") khi
  không có bằng chứng kỹ thuật trỏ tới.
- ❌ Bịa IOC/hash/output. Không chắc ⇒ ghi nguyên văn `chưa xác minh`.

## 8. Territory & ràng buộc Git

- Nhánh: `agent/forensics-mal/T5` — **CẤM merge `main`**.
- Territory ghi được: `research/**/FORENSICS.md`, `security/**/FORENSICS.md`, `agents/forensicsmal/**`.
- **CẤM ghi ngoài territory.**
- Theo `.gitignore`: `EVIDENCE/samples/` và `*.exe|*.dll|*.bin|*.dmp|*.raw|*.E01|*.pcap` bị chặn commit ⇒ đúng ý Admin.

## 9. Mức sẵn sàng

| Hạng mục | Mức |
|---|---|
| Phân tích **tĩnh** (hash, `file`, `strings`, hex, PE header thô, script/blog giải mã) | 🟢 **SẴN SÀNG** |
| Phân tích **PE** (`pefile` 2024.8.26 — đã parse PE thật) | 🟢 **SẴN SÀNG** |
| **Macro Office / OLE** (`oletools` 0.60.2, CLI `olevba`) | 🟢 **SẴN SÀNG** |
| **Disassembly** (`capstone` 5.0.9 metadata / 5.0.7 `__version__` + `objdump`/`readelf`) | 🟢 **SẴN SÀNG** |
| Phân tích **PCAP / network** (tshark 4.2.2 + `scapy` 2.7.0) | 🟢 **SẴN SÀNG** |
| Phân tích **log / text / timeline** | 🟢 **SẴN SÀNG** |
| **YARA** (soạn + scan qua `yara-python` 4.5.4, đã test) | 🟢 **SẴN SÀNG** (không có CLI) |
| **Memory forensics** (`volatility3` 2.28.2) | 🟡 **công cụ sẵn sàng, CHƯA thực chiến trên dump thật** |
| **Disk image / carving** | 🔴 **CHƯA** — thiếu công cụ, không tự cài được |
| **Stego ảnh/âm thanh** | 🔴 **CHƯA** — thiếu `steghide`/`exiftool` |
| **Dynamic malware trong sandbox** | 🔴 **CHƯA** — chưa có môi trường cô lập đã xác minh |

**Kết luận sẵn sàng:** sẵn sàng nhận **ngay** mẫu tĩnh (file mẫu, script, PE, macro Office,
PCAP, log) và **soạn/scan YARA**; memory dump nhận được nhưng cần mẫu để tôi thực chiến;
disk image / stego / dynamic cần Admin cấp công cụ hoặc môi trường cô lập.

> **Ghi chú trung thực:** tôi **không** đánh dấu 🟢 cho bất kỳ mục nào tôi chưa tự chạy ra kết quả thô.

---

## 10. Đề xuất loại task sẵn sàng nhận nhất (theo thứ tự)

1. **Triage tĩnh một mẫu file/script** — hash SHA256 → `file` → `strings` → hex → IOC → MITRE map.
2. **Phân tích PE** — `pefile` (header, section, import, entrypoint, entropy) + `objdump`/`capstone`.
3. **Phân tích macro Office / OLE** — `olevba`, `mraptor`, `rtfobj` (mẫu `.doc`/`.xls`/`.rtf`).
4. **Phân tích PCAP / traffic C2** — tshark: stream, DNS, HTTP object export, beacon timing; `scapy`.
5. **Dựng dòng thời gian từ log** (auth.log, HTTP log, EVTX nếu có text/XML export).
6. **Kiểm chứng độc lập** IOC/hash do agent khác công bố (recompute hash, đối chiếu output thô).
7. **Soạn + scan YARA rule** từ đặc trưng mẫu (qua `yara-python`).
8. **Memory dump** (Volatility) — nhận được, nhưng là lần thực chiến đầu ⇒ sẽ báo cáo thô cả phần lỗi.

**Artifact kèm theo:** `agents/forensicsmal/T5/FORENSICS_PROCEDURE.md`,
`agents/forensicsmal/T5/EVIDENCE/tool_inventory_raw.txt`,
`agents/forensicsmal/T5/EVIDENCE/tooling_bootstrap_raw.txt`,
`agents/forensicsmal/T5/scripts/bootstrap_tools.sh`.
