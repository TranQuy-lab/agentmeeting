# FORENSICS_PROCEDURE.md — Quy trình Pháp y số & Phân tích Mã độc

**Task:** T5 (phần CHUẨN BỊ) · **Ngày:** 2025-10-01
**Tác giả:** ForensicsMal (`ag_82f7cb07`) · **Nhánh:** `agent/forensics-mal/T5`
**Trạng thái:** ⚠️ **CHƯA CÓ MẪU** — tài liệu này là *quy trình + khuôn báo cáo*, không phải kết quả điều tra.
Mọi con số/hash cụ thể sẽ chỉ xuất hiện trong `FORENSICS.md` khi có mẫu thật.

> **Nguyên tắc gốc:** Không có bằng chứng thô ⇒ không có kết luận. Không chắc ⇒ ghi nguyên văn `chưa xác minh`.

---

## PHẦN A — QUY TRÌNH 5 BƯỚC BẤT BIẾN

Năm bước dưới đây **bắt buộc, không được bỏ, không được đảo thứ tự**. Vi phạm ⇒ dừng task, báo Admin.

### Bước 1 — KHÔNG BAO GIỜ sửa chứng cứ gốc; luôn làm trên bản sao

- Chứng cứ gốc là **chỉ đọc (read-only)**. Mọi thao tác phân tích chạy trên **bản sao**.
- Cách làm: tạo thư mục làm việc riêng, copy bằng `cp -p` (giữ metadata), hoặc mount read-only
  (`mount -o loop,ro` / `-o ro`).
- **Bắt buộc:** ghi lại đường dẫn chứng cứ gốc, và chứng minh hash gốc không đổi **sau** khi phân tích.
- ❌ CẤM: mở mẫu bằng tool có thể ghi, chạy tool tự động sửa file, giải nén "tại chỗ" trên file gốc.

```bash
# Khuôn mẫu an toàn
mkdir -p work/EVIDENCE          # bản sao làm việc
cp -p "<CHUNG_CU_GOC>" work/sample.bin
cp -p "<CHUNG_CU_GOC>" work/EVIDENCE/sample.bin   # bản đối chứng, không đụng tới
sha256sum work/sample.bin | tee work/EVIDENCE/sha256_before.txt
# ... phân tích trên work/sample.bin ...
sha256sum work/sample.bin | tee work/EVIDENCE/sha256_after.txt
diff work/EVIDENCE/sha256_before.txt work/EVIDENCE/sha256_after.txt && echo "CHUNG CU KHONG DOI"
```

### Bước 2 — Ghi SHA256 của MỌI mẫu TRƯỚC khi phân tích; lưu hash vào `EVIDENCE/`

- Hash ghi **TRƯỚC** khi mở/giải nén/chạy bất kỳ công cụ nào. Đây là mốc neo của toàn bộ điều tra.
- Lưu vào `EVIDENCE/` dưới dạng text thô, kèm ngày giờ UTC và đường dẫn nguồn.
- Ghi **cả** `sha256sum` **và** `md5sum`/`sha1sum` khi mẫu đến từ nguồn thứ ba (để đối chiếu
  với hash mà bên cung cấp công bố — đây là cách phát hiện mẫu bị tráo).
- Mẫu có **nhiều tệp** (archive, bộ mẫu) ⇒ hash **từng tệp** + hash **cả gói**, và liệt kê cây thư mục.

```bash
# Bắt buộc, chạy ĐẦU TIÊN
cd work
{ echo "# EVIDENCE HASH — $(date -u '+%Y-%m-%dT%H:%M:%SZ') UTC"
  echo "# Nguồn: <nguồn nhận mẫu>"
  echo "# Người nhận: ForensicsMal (ag_82f7cb07)"
  echo "## sha256"
  sha256sum sample.bin
  echo "## sha1"
  sha1sum sample.bin
  echo "## md5"
  md5sum sample.bin
  echo "## kích thước (byte)"
  stat -c '%s %n' sample.bin
  echo "## định dạng theo magic byte"
  file sample.bin
} | tee EVIDENCE/hashes.txt
# Với bộ nhiều tệp:
# find . -type f -exec sha256sum {} \; | sort -k2 | tee EVIDENCE/hashes_tree.txt
```

### Bước 3 — Ghi rõ **công cụ + phiên bản + lệnh** cho MỌI kết luận

- Mỗi khẳng định kỹ thuật phải kèm **bộ ba**: `tên_công_cụ` + `phiên bản` + `lệnh nguyên văn`.
- Kết luận không có bộ ba này ⇒ **không được** đưa vào báo cáo.
- Với công cụ tự viết (Python script): ghi **đường dẫn script + hash của script + lệnh gọi**
  (script cũng là một phần của bằng chứng, phải bất biến được).
- Ghi cả **output thô** (raw), không chỉ tóm tắt. Output dài ⇒ lưu file trong `EVIDENCE/` và
  trích dẫn đường dẫn + số dòng.

```bash
# Ghi phiên bản công cụ vào EVIDENCE/ ngay khi bắt đầu
{ echo "# TOOL VERSIONS — $(date -u '+%Y-%m-%dT%H:%M:%SZ') UTC"
  python3 --version
  file --version | head -1
  strings --version | head -1
  tshark --version 2>&1 | head -1
  objdump --version | head -1
  sha256sum --version | head -1
} | tee EVIDENCE/tool_versions.txt
```

> **Lưu ý môi trường (đã xác minh thô — xem `EVIDENCE/tool_inventory_raw.txt`
> và `EVIDENCE/tooling_bootstrap_raw.txt`):**
>
> **CÓ sẵn ngoài hệ thống:** Python 3.12.3, `sha256sum`/`sha1sum`/`md5sum`, `file`, `strings`,
> `xxd`, `objdump`/`readelf`/`nm`/`gdb`, `tshark` **4.2.2**, `tcpdump`, `git`, `curl`, `jq`,
> `unzip`, và **`uv` 0.12.13**.
>
> **ĐÃ BỔ SUNG được qua `uv` (venv ngoài repo, KHÔNG cần sudo):**
> `volatility3` **2.28.2** (CLI `vol` chạy được), `pefile` 2024.8.26 (parse PE thật OK),
> `scapy` 2.7.0, `capstone` 5.0.9, `yara-python` 4.5.4 (compile + scan OK),
> `oletools` 0.60.2 (CLI `olevba` OK). Tái lập bằng `scripts/bootstrap_tools.sh`.
>
> **VẪN THIẾU (không cài được — cần sudo/Admin):** `binwalk`, `foremost`, `yara` (CLI),
> `zeek`, `exiftool`, `steghide`, sleuthkit (`fls`/`icat`/`photorec`), `upx`, `7z`.
>
> ⚠️ **Venv nằm ngoài repo** (`~/forensicsmal-tooling/.venv`) ⇒ **không** bị commit.
> Khi trích dẫn, ghi rõ **đường dẫn phiên bản công cụ đã dùng** (venv hay hệ thống).
> Nếu kết luận nào cần công cụ **vẫn thiếu** ⇒ ghi thẳng **"chưa thực hiện được: thiếu công cụ"**,
> **KHÔNG** suy diễn thay cho việc chạy công cụ.
>
> ⚠️ **Lưu ý trung thực về giới hạn:** `volatility3` đã nạp plugin thành công nhưng
> **CHƯA từng chạy trên memory dump thật** trong phiên này ⇒ năng lực memory forensics
> vẫn ở mức **"công cụ sẵn sàng, chưa thực chiến"**, không phải "đã thành thạo".

### Bước 4 — Phân tích malware trong **môi trường cô lập**; KHÔNG chạy mẫu trên máy thật

- **Mặc định của tôi là phân tích TĨNH.** Tĩnh không cần chạy mẫu ⇒ an toàn.
- Chỉ chuyển sang động khi có môi trường cô lập **được xác minh** (VM/container tách mạng,
  snapshot, không mount ổ thật, không credential thật).
- **Hiện tại chưa xác minh được môi trường cô lập nào trên máy này** ⇒
  **phân tích động bị ĐÌNH CHỈ** cho tới khi Admin cấp môi trường.
- ❌ CẤM tuyệt đối: chạy `.exe`/`.dll`/script lạ, `./sample`, `sh sample.sh`, `python3 sample.py`,
  `powershell -enc ...`, hoặc mở mẫu bằng ứng dụng có macro/script.
- Gỡ nén/giải mã **không** phải là "chạy mẫu" — nhưng vẫn phải làm trên bản sao và trong
  thư mục làm việc, không bao giờ trên file gốc.
- Cảnh giác với **thoát ra mạng**: khi buộc phải chạm mẫu bằng tool có khả năng gọi mạng,
  chặn mạng trước (unshare/tường lửa) hoặc chỉ dùng tool thuần đọc file.

### Bước 5 — Dữ liệu cá nhân (PII) phát hiện được ⇒ **KHÔNG trích dẫn nguyên văn**; che/mã hoá

- Nếu mẫu/log chứa PII thật (họ tên, email, số điện thoại, CCCD/CMND, địa chỉ, số tài khoản,
  mật khẩu, token, cookie phiên, ảnh cá nhân, dữ liệu y tế) ⇒ **che (redact)** trước khi
  đưa vào bất kỳ báo cáo hay commit nào.
- Quy tắc che: giữ **loại** dữ liệu và **vị trí**, bỏ **giá trị**. Ví dụ:
  `email: <redacted:a***@example.com>` hoặc `CCCD: <redacted:12 ký tự số>`.
- Chỉ giữ **đủ** để chứng minh kỹ thuật (ví dụ: tiền tố/số ký tự), không giữ nguyên văn.
- ❌ CẤM: copy nguyên văn PII vào `FORENSICS.md`, commit, tin nhắn phòng, hay log lệnh.
- ❌ CẤM: push mẫu, dump, hay dữ liệu thật lên repo (`.gitignore` đã chặn `EVIDENCE/samples/`
  và `*.exe|*.dll|*.bin|*.dmp|*.raw|*.E01|*.pcap` — tôn trọng nghiêm ngặt).

---

## PHẦN B — KHUÔN BÁO CÁO `FORENSICS.md`

Báo cáo nằm trong territory: `research/**/FORENSICS.md`, `security/**/FORENSICS.md`,
hoặc `agents/forensicsmal/**`. **CẤM ghi ngoài territory.**

Sao chép khuôn dưới đây và điền. Phần nào chưa có dữ liệu ⇒ ghi `chưa xác minh`, **không bỏ trống
và không bịa**.

```markdown
# FORENSICS — <tên mẫu / vụ việc / task_id>

## 0. Định danh
- **Tiêu đề:**
- **Ngày phân tích:** (UTC)
- **Tác giả:** ForensicsMal (`ag_82f7cb07`)
- **Task / nhánh Git:**
- **Yêu cầu từ:** (Admin / agent nào)
- **Mức độ phân tích:** TĨNH / PCAP / LOG / (ĐỘNG — chỉ khi có môi trường cô lập đã xác minh)

## 1. Hash mẫu (BẮT BUỘC — tính TRƯỚC khi phân tích)
| Tệp | Kích thước (byte) | SHA256 | SHA1 | MD5 | Định dạng (`file`) |
|---|---|---|---|---|---|
| sample.bin | | | | | |
- **Nguồn nhận mẫu:**
- **Hash do bên cung cấp công bố (nếu có):** — có KHỚP không? ☐ khớp ☐ KHÔNG khớp ☐ không có để đối chiếu
- **Bằng chứng thô:** `EVIDENCE/hashes.txt`
- **Xác nhận chứng cứ không đổi sau phân tích:** ☐ đã kiểm ☐ chưa kiểm

## 2. Công cụ + phiên bản (BẮT BUỘC cho mọi kết luận)
| Công cụ | Phiên bản | Lệnh đã dùng | Bằng chứng thô |
|---|---|---|---|
| sha256sum | | `sha256sum sample.bin` | `EVIDENCE/hashes.txt` |
| file | | | |
| strings | | | |
| tshark | 4.2.2 | | |
- **Công cụ THIẾU nhưng cần:** (ghi thẳng, kèm hệ quả lên kết luận)
- **Bằng chứng thô:** `EVIDENCE/tool_versions.txt`

## 3. Dòng thời gian (timeline)
| Thời điểm (UTC) | Sự kiện | Nguồn bằng chứng | Độ tin cậy |
|---|---|---|---|
- Ghi rõ nguồn timestamp: từ filesystem, từ log, từ header PCAP, từ metadata — và **múi giờ**.
- Timestamp do mẫu tự khai ⇒ **không đáng tin** (có thể bị sửa). Ghi chú rõ.

## 4. IOC (Indicators of Compromise)
| Loại | Giá trị | Ngữ cảnh phát hiện | Bằng chứng thô (file:line) |
|---|---|---|---|
| SHA256 | | | |
| Tên miền | | | |
| IP | | | |
| URL | | | |
| Registry / đường dẫn | | | |
| User-Agent | | | |
- **Mọi giá trị PHẢI trích từ output thô.** Không suy đoán, không "thường thấy thì thêm vào".
- **PII: che** — ghi `<redacted:...>`.

## 5. Hành vi quan sát được
- Mô tả **chỉ những gì bằng chứng cho thấy**, tách bạch:
  - **(a) Quan sát trực tiếp** (có output thô).
  - **(b) Suy luận có cơ sở** (nêu rõ chuỗi lập luận).
  - **(c) Giả thuyết chưa kiểm chứng** (ghi chú rõ là giả thuyết).
- Nêu **cơ chế** (persistence, injection, exfil, encryption...) kèm bằng chứng byte/chuỗi.

## 6. Bảng map MITRE ATT&CK
| Tactic | Technique ID | Technique | Bằng chứng trong mẫu | Độ tin cậy |
|---|---|---|---|---|
| Execution | T1059 | Command and Scripting Interpreter | | |
| Persistence | T1547 | Boot or Logon Autostart Execution | | |
| Defense Evasion | T1027 | Obfuscated Files or Information | | |
| Command and Control | T1071 | Application Layer Protocol | | |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | | |
- **Chỉ map technique có bằng chứng.** Không map cho "đủ bảng".
- Technique chỉ *có thể* xảy ra ⇒ ghi vào phần "chưa xác minh", không vào bảng này.
- Tra cứu tại `/home/noble-tran/security-agent/ATTACK_COVERAGE.md`.

## 7. Kết luận
- Mỗi kết luận **trỏ tới bằng chứng thô** (đường dẫn file + dòng/lệnh).
- Phân biệt rõ: **kết luận chắc chắn** vs **kết luận có điều kiện**.
- ❌ **CẤM attribution** ("có thể là APT", "do nhóm X", "liên quan chiến dịch Y") **khi không có
  bằng chứng attribution kỹ thuật trỏ tới**. Không có bằng chứng ⇒ **không nhắc tới**.
- ❌ CẤM kết luận vượt bằng chứng.

## 8. CHƯA XÁC MINH (bắt buộc có mục này)
- Liệt kê **mọi** điều chưa kiểm chứng được, kèm lý do cụ thể:
  - "chưa xác minh — thiếu công cụ `<tên>`"
  - "chưa xác minh — không có môi trường cô lập để chạy động"
  - "chưa xác minh — mẫu không kèm đủ artifact"
  - "chưa xác minh — cần đối chiếu thêm nguồn ngoài"
- Mục này **rỗng là dấu hiệu xấu**, không phải dấu hiệu tốt.
```

---

## PHẦN C — DANH SÁCH KIỂM TRA TRƯỚC KHI KẾT LUẬN

Chạy hết danh sách này **trước khi** push `FORENSICS.md`. Mỗi ô phải trả lời được **CÓ**.

### C1. Bằng chứng & hash
- [ ] SHA256 của **mọi** mẫu đã ghi **TRƯỚC** khi phân tích? (`EVIDENCE/hashes.txt`)
- [ ] Đã kiểm hash mẫu **không đổi** sau khi phân tích?
- [ ] Mẫu nhiều tệp ⇒ đã hash **từng tệp** và **cả gói**?
- [ ] Hash do bên cung cấp công bố (nếu có) đã **đối chiếu** và ghi kết quả khớp/không khớp?
- [ ] Đã xác nhận **không sửa chứng cứ gốc** (chỉ làm trên bản sao)?

### C2. Truy vết công cụ
- [ ] **Mọi** kết luận đều có công cụ + phiên bản + lệnh nguyên văn?
- [ ] Có kết luận nào dựa trên công cụ **đang thiếu** mà tôi suy diễn thay vì chạy? → **cấm**
- [ ] Output thô của mọi lệnh quan trọng đã lưu trong `EVIDENCE/` và được trích dẫn?
- [ ] Công cụ tự viết (script) đã ghi đường dẫn + hash + lệnh gọi?

### C3. Bằng chứng vs. kết luận — kiểm tra vượt quá bằng chứng
- [ ] **Mọi IOC đều có hash/output thô làm chỗ dựa?**
- [ ] Có IOC nào tôi **thêm vào theo kinh nghiệm/thói quen** mà không thấy trong mẫu? → **xoá**
- [ ] **Có kết luận nào vượt quá bằng chứng không?**
  - [ ] Ví dụ cấm: **"có thể là APT"** khi **không có bằng chứng attribution**.
  - [ ] Ví dụ cấm: khẳng định "mã hoá AES-256" khi chưa thấy S-box/hằng số đặc trưng.
  - [ ] Ví dụ cấm: khẳng định "kết nối tới C2 `<domain>`" khi `<domain>` chỉ là chuỗi chết
        chưa từng thấy trong traffic hoặc trong nhánh thực thi.
  - [ ] Ví dụ cấm: quy kết mục đích/tác giả khi chỉ có chuỗi văn bản.
- [ ] Mọi câu suy luận đã được **dán nhãn** là (b) suy luận hay (c) giả thuyết?
- [ ] Có câu nào **chắc chắn hoá quá mức** (dùng "chắc chắn", "rõ ràng là", "do...") mà bằng chứng
      chỉ ở mức "gợi ý"? → hạ giọng hoặc chuyển sang mục 8.
- [ ] Mục **"CHƯA XÁC MINH"** đã liệt kê hết các lỗ hổng bằng chứng chưa?
- [ ] Có chỗ nào tôi viết **số liệu/hash/tên** mà **không tự chạy ra**? → ghi `chưa xác minh` hoặc xoá.

### C4. An toàn & đạo đức
- [ ] Đã **KHÔNG** chạy mẫu (kể cả script) trên máy thật / ngoài môi trường cô lập?
- [ ] Nếu có phân tích động: môi trường cô lập đã **được xác minh** và ghi lại cách xác minh?
- [ ] **PII đã được che/mã hoá**, không trích nguyên văn?
- [ ] Đã **KHÔNG** push mẫu / dump / dữ liệu thật lên repo?
- [ ] Nội dung báo cáo nằm **trong territory** (`research/**/FORENSICS.md`,
      `security/**/FORENSICS.md`, `agents/forensicsmal/**`)?

### C5. Git
- [ ] Đang ở nhánh `agent/forensics-mal/<task_id>`, **không** merge `main`?
- [ ] Commit message theo mẫu `[T5] report: ...`?
- [ ] Chỉ push **báo cáo + bằng chứng văn bản/hash**, không push mẫu thật?

> **Quy tắc vàng:** Người viết **KHÔNG BAO GIỜ** tự verify việc mình làm — Reviewer1 làm (D-004).
> Báo cáo của tôi là **đầu vào** cho kiểm định độc lập, không phải phán quyết cuối.

---

## PHẦN D — GHI CHÚ VẬN HÀNH (môi trường hiện tại)

Kết quả kiểm kê thô: `agents/forensicsmal/T5/EVIDENCE/tool_inventory_raw.txt`.
Kết quả bootstrap + test chức năng: `agents/forensicsmal/T5/EVIDENCE/tooling_bootstrap_raw.txt`.

| Năng lực | Trạng thái | Ghi chú / bằng chứng |
|---|---|---|
| Triage tĩnh (hash/`file`/`strings`/hex) | 🟢 sẵn sàng | Python 3.12.3 + coreutils + binutils |
| PCAP / network | 🟢 sẵn sàng | tshark **4.2.2**, tcpdump, `scapy` 2.7.0 |
| Log / timeline | 🟢 sẵn sàng | thuần text, không cần tool ngoài |
| PE analysis | 🟢 sẵn sàng | `pefile` 2024.8.26 — **đã parse PE thật** (`crackme.exe`, machine=0x8664, 6 section) |
| Disassembly | 🟢 sẵn sàng | `capstone` 5.0.9 — **đã disasm x86-64**, thêm `objdump`/`readelf` |
| Office macro / OLE | 🟢 sẵn sàng | `oletools` 0.60.2 — **CLI `olevba` OK**, có `mraptor`, `rtfobj`, `oleid` |
| YARA | 🟢 sẵn sàng | `yara-python` 4.5.4 — **đã compile + scan OK**. ⚠️ **không có CLI `yara`** ⇒ scan qua Python API (hoặc tự viết wrapper) |
| Memory forensics | 🟡 công cụ sẵn sàng, **chưa thực chiến** | `volatility3` **2.28.2**, CLI `vol` chạy, plugin nạp OK — **CHƯA chạy trên dump thật** |
| Disk image / carving | 🔴 chưa | thiếu `foremost`, sleuthkit, `binwalk` |
| Dynamic malware | 🔴 chưa | chưa xác minh môi trường cô lập |

**Đường nâng cấp khả thi (ĐÃ THỰC HIỆN cho Python, còn lại cần Admin):** máy có `uv` tại
`/home/noble-tran/.local/bin/uv` ⇒ đã dựng venv riêng và cài thành công `pefile`, `yara-python`,
`scapy`, `capstone`, `oletools`, `volatility3` **không cần sudo** — tái lập bằng
`agents/forensicsmal/T5/scripts/bootstrap_tools.sh`.
`sudo` yêu cầu mật khẩu ⇒ **không** cài được gói hệ thống (`binwalk`, `foremost`, sleuthkit,
`yara` CLI, `zeek`, `exiftool`) nếu không có hỗ trợ từ Admin.

**Đề xuất task sẵn sàng nhận nhất:** (1) triage tĩnh mẫu file/script; (2) phân tích PCAP/C2;
(3) dựng timeline từ log; (4) kiểm chứng độc lập IOC/hash của agent khác (recompute hash);
(5) phân tích PE / macro Office / soạn YARA rule.
**Mảng cần Admin bật đèn xanh:** memory dump thật (Volatility), disk image (cần cài công cụ),
và mọi phân tích **động** (cần môi trường cô lập đã xác minh).
