# T15_REPORT.md — Kiểm chuẩn toolchain trên CORPUS TỔNG HỢP VÔ HẠI

**Task:** T15 · **Ngày:** 2025-10-01 (UTC 2026-10-01) · **Tác giả:** ForensicsMal (`ag_82f7cb07`)
**Nhánh:** `agent/forensics-mal/T15` · **Nền:** `main` @ `28cdc00`

> **Mục tiêu của T15:** chứng minh toolchain **chạy được trên dữ liệu thật** — không phải
> phỏng đoán từ `import` thành công. Corpus **100% do tôi tự tạo, vô hại**.
> **KHÔNG** có mã độc thật. **KHÔNG** chạy mẫu. **Phân tích ĐỘNG vẫn ĐÌNH CHỈ.**

---

## 0. Tóm tắt kết quả

| # | Hạng mục | Phép kiểm | Kết quả | Kết luận |
|---|---|---|---|---|
| 1 | **PCAP** (scapy ↔ tshark) | 14 trường | **0 lệch giá trị**, 3 lệch *biểu diễn* | ✅ nhất quán |
| 2 | **ELF** (capstone ↔ objdump ↔ readelf) | 92 instruction | **0 lệch địa chỉ, 0 lệch mnemonic cứng** | ✅ nhất quán |
| 3 | **YARA** (âm tính + dương tính) | 56 phép kiểm | **TP=10, TN=46, FP=0, FN=0** | ✅ phân loại đúng |
| 4 | **volatility3** (input rỗng/không hợp lệ) | 9 ca | **0 crash, 0 treo, 9/9 báo lỗi rõ** | ✅ thất bại sạch sẽ |

**Bằng chứng thô:** `EVIDENCE/t15_1_pcap_raw.txt`, `t15_2_elf_raw.txt`, `t15_3_yara_raw.txt`,
`t15_4_volatility_raw.txt`, `t15_0_corpus_hashes.txt`.
**Tái lập:** `scripts/t15_{pcap,elf,yara,volatility}_test.py`.

**Phiên bản công cụ dùng thật** (ghi theo đúng những gì đã chạy):
`tshark` 4.2.2 · `gcc` 13.3.0 · `objdump`/`readelf`/`objcopy` 2.42 (binutils) ·
`scapy` 2.7.0 · `capstone` metadata **5.0.9** / `__version__` **5.0.7** ·
`yara-python` 4.5.4 (metadata) · `volatility3` 2.28.2.

---

## 1. T15-1 — PCAP: scapy (ghi) ↔ tshark (đọc lại)

**Cách làm:** dựng 1 truy vấn DNS vô hại bằng `scapy` (tên miền `example.invalid` —
TLD reserved theo RFC 2606/6761; IP `192.0.2.0/24` = TEST-NET-1 theo RFC 5737) →
`wrpcap()` ghi file → đọc lại bằng `tshark -T fields` →
đối chiếu **từng trường**.

- MAC/IP đặt **tường minh** ⇒ scapy **không** ARP, **không** gọi mạng.
- `pkt.time` đặt cố định ⇒ kết quả tái lập được.
- sha256 pcap: `dcc400749ded352532909c05eece89dc0d0b96a66cf81a86d5cf473c6ce2c89b`

**Kết quả:** **0 lệch giá trị** trên 14 trường. Nhưng có **3 lệch BIỂU DIỄN**:

| Trường | scapy in | tshark in | Giá trị thật |
|---|---|---|---|
| `dns.id` | `4660` | `0x1234` | 4660 |
| `dns.flags.response` | `0` | `False` | 0 |
| `dns.qry.class` | `1` | `0x0001` | 1 |

> **Đây là phát hiện có giá trị, không phải lỗi dữ liệu.** Nếu so **chuỗi thô** giữa hai
> công cụ, ta sẽ báo "lệch" một cách sai. **Bài học quy trình:** phải **chuẩn hoá về giá trị**
> (`int(x, 0)`, `bool`) trước khi kết luận lệch. Tôi đã đưa bước chuẩn hoá này vào script
> và phân loại rõ `LECH GIA TRI` vs `CHI LECH BIEU DIEN`.

**Đối chiếu số gói:** scapy đọc lại 1 gói = tshark đếm 1 frame ✅.

---

## 2. T15-2 — ELF: capstone ↔ objdump ↔ readelf

**Cách làm:** viết chương trình C tối giản (`corpus/bench_elf.c`: `add`, `loop_sum`,
`classify`, `main`) → `gcc -O1` → `readelf -h/-S` lấy entry point và `.text` →
`objcopy -O binary --only-section=.text` trích **byte thô** →
disassemble cùng vùng byte đó bằng **capstone** (gốc `= 0x1040`) và **objdump -d -M intel**
→ so **từng instruction** theo `(địa chỉ, mnemonic, toán hạng)`.

**Kết quả:**

| Chỉ số | Giá trị |
|---|---|
| Entry point (readelf) | `0x1040` |
| `.text` địa chỉ / kích thước (readelf) | `0x1040` / **334 byte** |
| Byte trích bằng objcopy | **334 byte** ⇒ **khớp readelf** |
| Instruction capstone | **92** |
| Instruction objdump | **92** |
| Lệch **địa chỉ** | **0** |
| Lệch **mnemonic** (so thô) | **1** |
| → trong đó **giải thích được** | **1** |
| → trong đó **lệch cứng** | **0** |
| Lệch **toán hạng** (cách viết) | 41 |

**Lệch duy nhất — và lệch ở đâu:** tại `0x1066`.

```
byte thô : 66 2e 0f 1f 84 00 00 00 00 00      (10 byte, multi-byte NOP)
objdump  : cs nop WORD PTR [rax+rax*1+0x0]
capstone : nop word ptr cs:[rax + rax]
```

**objdump tách tiền tố `cs` thành một token riêng** (nên parser thô của tôi đọc mnemonic = `cs`),
còn capstone **gộp `cs:` vào toán hạng**. Cả hai công cụ giải mã **cùng một lệnh** — tôi đã
đối chiếu **byte thô** để khẳng định, không suy đoán. Sau khi "gấp tiền tố" (prefix folding),
**0 lệch cứng**.

**41 lệch toán hạng** đều là **cách viết**, ví dụ: objdump thêm comment symbol
(`# 116f <main>`), `WORD PTR` vs `word ptr`, `0x3` vs `3`, `[rax+rax*1+0x0]` vs `[rax + rax]`.
**Không** phải lỗi giải mã.

> **GHI CHÚ PHIÊN BẢN KHÔNG NHẤT QUÁN (đã xác minh):** `uv` cài `capstone==5.0.9`
> (package metadata) nhưng `capstone.__version__` trả **5.0.7**. Khi trích dẫn phải ghi rõ
> đang dùng **metadata** hay **`__version__`** — nếu không sẽ mâu thuẫn giữa các báo cáo.

---

## 3. T15-3 — YARA: kiểm CẢ âm tính giả (không chỉ dương tính)

**Cách làm:** corpus **có nhãn ground-truth** (7 file) × 8 rule = **56 phép kiểm**,
đối chiếu bằng **ma trận nhầm lẫn** TP / TN / **FP (dương tính giả)** / **FN (âm tính giả)**.

**Kết quả: TP=10, TN=46, FP=0, FN=0 — chính xác 56/56 (100%).**

**Hai "bẫy dương tính giả"** (rule *phải không* khớp) — đều không khớp ✅:
- `t15_absent_string` — chuỗi không tồn tại ở đâu.
- `t15_mz_header_pe` — `uint16(0) == 0x5A4D` (MZ/PE) trên corpus không có PE.

**Hai "bẫy ÂM TÍNH GIẢ" thật sự** (khó, có thể miss) — đều khớp đúng ✅:
- **`F` straddle ranh giới chunk:** marker `FORENSICSMAL_T15_MARKER_ALPHA` đặt tại
  **offset 4086..4114**, tức **vắt qua mốc 4096** (YARA đọc theo block 4 KB + overlap).
  Nếu YARA xử lý overlap sai thì đây **chính là** một FN. Rule `t15_boundary_marker` đã khớp ✅.
- **`G` mã hoá UTF-16LE:** marker ở dạng `wide`. Rule `t15_wide_marker` khớp `G` ✅
  **và không** khớp `A` (ASCII) ✅ ⇒ kiểm được **cả hai chiều** của modifier `wide`.

**Kiểm hai chiều phân biệt hoa/thường:** `t15_case_insensitive` (`nocase`) khớp **cả** `A`
(chuỗi HOA) **và** `C` (chuỗi thường); `t15_marker_alpha` (không `nocase`) chỉ khớp `A` ✅.

**Đối chiếu chéo với T15-2:** rule `t15_elf_magic` (`uint32(0)==0x464C457F`) khớp **đúng**
file ELF do T15-2 biên dịch, và không khớp file văn bản ✅.

> ⚠️ **Giới hạn phải nói rõ:** 100% trên corpus **do chính tôi thiết kế** là bằng chứng
> **toolchain hoạt động đúng trên các ca đã biết**, **KHÔNG** phải bằng chứng về độ chính xác
> trên mẫu thực tế. `yara-python` ở đây chứng minh **cơ chế compile+match đúng**,
> không chứng minh **chất lượng rule**.

> ⚠️ **KHÔNG có `yara` CLI** trên máy ⇒ mọi scan đi qua **API `yara-python`**. Đã ghi rõ trong
> `EVIDENCE/` để người sau không tưởng nhầm là có CLI.

---

## 4. T15-4 — volatility3: thất bại SẠCH SẼ trên input rỗng/không hợp lệ

**Cách làm:** 9 ca input **không hợp lệ/vô hại** (file rỗng 0 byte, 64 KB byte ngẫu nhiên
seed cố định, file 16 byte, 4 KB số 0, đường dẫn không tồn tại, trỏ vào **thư mục**,
thiếu `-f`, tên plugin không tồn tại, plugin `linux.*` trên input rác) → chạy
`vol -f <input> <plugin>` với timeout 90 s → kiểm **crash / treo / có báo lỗi không**.

**Kết quả: 9/9 ca — 0 crash, 0 treo, 9/9 có thông báo lỗi rõ ràng.**

| Ca | exit | giây | treo | traceback | báo lỗi |
|---|---|---|---|---|---|
| file rỗng (0 byte) | 1 | 0.26 | không | **không** | có |
| byte ngẫu nhiên 64 KB | 1 | 0.31 | không | **không** | có |
| file 16 byte | 1 | 0.26 | không | **không** | có |
| toàn số 0 4 KB | 1 | 0.25 | không | **không** | có |
| file không tồn tại | 2 | 0.22 | không | **không** | có |
| thư mục thay vì file | 1 | 0.25 | không | **không** | có |
| không truyền `-f` | 1 | 0.20 | không | **không** | có |
| plugin không tồn tại | 2 | 0.18 | không | **không** | có |
| plugin `linux.*` trên input rác | 1 | 0.21 | không | **không** | có |

**Chất lượng thông báo lỗi — kiểm bằng mắt trên output thô:**
- File rỗng ⇒ `Unsatisfied requirement plugins.PsList.kernel.layer_name` kèm hướng dẫn
  **cụ thể, có thể hành động** ("A file was provided…", "The file is a valid memory image…").
- File không tồn tại ⇒ `vol: error: File does not exist: <path>` (exit 2).
- Plugin không tồn tại ⇒ `vol: error: argument PLUGIN: invalid choice …` (exit 2).

> **PHÁT HIỆN THÊM (tình cờ nhưng hữu ích):** thông báo "invalid choice" in ra **danh sách
> đầy đủ plugin đã nạp** — hơn 200 plugin. Trong đó có `windows.malfind.Malfind`,
> `windows.malware.malfind.Malfind`, `yarascan.YaraScan`, `windows.vadyarascan.VadYaraScan`,
> `linux.malfind.Malfind`, `windows.registry.hivelist.HiveList`… ⇒ **plugin registry nạp đầy đủ**,
> tức capability memory-forensics + YARA-in-memory **có sẵn ở tầng framework**.

**Điều T15-4 CHỨNG MINH:** vol3 nạp framework + plugin OK, và khi thiếu dữ liệu thì **báo
thiếu yêu cầu** thay vì crash ⇒ lỗi trong tương lai sẽ là **lỗi dữ liệu**, không phải lỗi framework.
**Điều T15-4 KHÔNG chứng minh:** rằng tôi phân tích được **memory dump thật**.

---

## 5. Cập nhật mức năng lực SAU kiểm chuẩn

| Năng lực | Trước T15 | Sau T15 | Căn cứ |
|---|---|---|---|
| PCAP / network | 🟢 | 🟢 (đã kiểm chéo 2 công cụ) | T15-1 |
| ELF / disassembly | 🟢 | 🟢 (đã kiểm chéo 2 disassembler) | T15-2 |
| YARA | 🟢 | 🟢 (đã kiểm **cả hai chiều** FP/FN) | T15-3 |
| PE / macro / Office | 🟢 | 🟢 (không đổi — không thuộc phạm vi T15) | kiểm chức năng ở T5 (`tooling_bootstrap_raw.txt`) |
| **Memory forensics (vol3)** | 🟡 chưa thực chiến | 🟡 **vẫn chưa thực chiến**, nhưng nay **đã chứng minh thất bại sạch sẽ** + **plugin registry nạp đủ** | T15-4 |
| Disk carving / stego | 🔴 | 🔴 **không đổi** — Admin quyết định KHÔNG cấp `sudo` | quyết định Admin |
| Phân tích động | 🔴 đình chỉ | 🔴 **đình chỉ** — Admin xác nhận là ràng buộc bắt buộc | quyết định Admin |

**Hệ quả của việc KHÔNG có `sudo` (Admin yêu cầu ghi rõ):**
**không** carving ảnh đĩa / phục hồi file xoá (`foremost`, sleuthkit, `photorec`),
**không** stego ảnh–âm thanh (`steghide`, `exiftool`), **không** `zeek`, **không** `binwalk`
(firmware/embedded extraction). **Không** có `yara` CLI ⇒ scan YARA chỉ qua API Python.

---

## 6. CHƯA XÁC MINH (bắt buộc — mục rỗng là dấu hiệu xấu)

- **chưa xác minh** — vol3 phân tích **memory dump thật**: chưa từng chạy, chưa có mẫu.
- **chưa xác minh** — độ chính xác của YARA trên **mẫu thực tế**: T15-3 chỉ là corpus tự thiết kế.
- **chưa xác minh** — hành vi **động** của bất kỳ mẫu nào: phân tích động đang đình chỉ.
- **chưa xác minh** — chất lượng rule YARA cho mục đích phát hiện thật (T15 chỉ kiểm **cơ chế**).
- **chưa xác minh** — bất kỳ IOCTL/kỹ thuật disk hay stego nào: thiếu công cụ.
- **chưa xác minh** — `capstone` phiên bản "đúng": metadata 5.0.9 vs `__version__` 5.0.7 mâu thuẫn;
  tôi **không** tự phán quyết cái nào đúng.
- **chưa xác minh** — các **lệch toán hạng** giữa capstone/objdump có ảnh hưởng ngữ nghĩa
  trong mọi trường hợp hay không (T15-2 chỉ kiểm trên **1** chương trình nhỏ, 92 instruction).
  **Mẫu nhỏ ⇒ không ngoại suy ra mọi binary.**

---

## 7. Ràng buộc đã tuân thủ

- ✅ Corpus **100% tự tạo, vô hại**; **không** tạo/cài/tải mã độc thật.
- ✅ **Không** push mẫu thật lên repo; **không** commit binary build (`corpus/.gitignore`).
- ✅ **Không** chạy mẫu; phân tích động **vẫn đình chỉ**.
- ✅ Mọi kết luận trỏ tới **bằng chứng thô** trong `EVIDENCE/`.
- ✅ Không bịa IOC/hash/output; chỗ không chắc ghi nguyên văn `chưa xác minh`.
- ✅ Theo D-004: **tôi không tự verify việc mình làm** — Reviewer1 làm.
