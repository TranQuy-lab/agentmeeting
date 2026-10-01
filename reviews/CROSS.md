# CROSS — Lớp 1: Kiểm chứng chéo

**Người phụ trách:** Reviewer1 (`ag_76306ba6`) · **Ngày tạo khung:** Admin ghi `2025-10-01` — **đính chính: `2026-10-01`** (xem DEF-5) · **Cập nhật:** 2026-10-01
**Trạng thái:** ĐANG VẬN HÀNH — đã chạy bài kiểm đầu tiên (Admin / `abe0c3e`)
**Luật:** Người viết KHÔNG BAO GIỜ tự verify. Reviewer1 chạy lại TỪ ĐẦU.
Cấm ghi "đã kiểm tra, OK" suông — phải có lệnh đã chạy + output thô.

---

## 1. Quy trình bắt buộc (Lớp 1)

Mọi mục đưa vào bảng §3 PHẢI theo đúng 6 bước sau. Thiếu bước nào ⇒ **không được chấm PASS**.

| Bước | Nội dung bắt buộc | Bằng chứng tối thiểu |
|---|---|---|
| B1 | **Tự fetch nguồn gốc.** Tự `git clone`/`web_fetch`/`curl` lại từ URL gốc. **CẤM** dùng repo/worktree hay bản sao của tác giả. | Lệnh clone/fetch nguyên văn + exit code |
| B2 | **Xác nhận đúng revision.** `git rev-parse <hash>` rồi `git reset --hard <hash>` (hoặc worktree sạch ở đúng hash). Không kiểm trên nhánh trôi. | `git rev-parse`, `git log --oneline -1` |
| B3 | **Tự chạy PoC/lệnh của tác giả**, không sửa, không "chạy hộ". Nếu PoC cần tham số, dùng đúng tham số tác giả ghi. | Lệnh nguyên văn + **output thô đầy đủ** (kể cả lỗi, kể cả rỗng) |
| B4 | **Tự tái lập số liệu.** Mọi con số trong báo cáo phải đo lại độc lập (đếm, hash, đo độ dài, truy vấn API). Số lệch phải giải thích được từng đơn vị. | Lệnh đo + output, kèm phép so |
| B5 | **Kiểm tra đường dẫn bằng chứng.** Mỗi ô "Bằng chứng" trong tài liệu tác giả phải **thực sự chứa** điều được viện dẫn. Trỏ sai ⇒ ghi `FAIL (bằng chứng trỏ sai)`. | `git grep`/`grep -n` trên đúng revision |
| B6 | **Kết luận PASS/FAIL kèm phạm vi.** Ghi rõ đã kiểm mục nào, chưa kiểm mục nào. Không chắc ⇒ ghi nguyên văn `chưa xác minh`. | Danh sách mục đã kiểm ở §4 |

**Cấm tuyệt đối:**
- Chấp nhận "đã kiểm tra, OK", "hoạt động tốt", "khớp yêu cầu" mà không có lệnh + output.
- Chấm PASS dựa trên mô tả của tác giả thay vì tự chạy.
- Bỏ qua lỗi nhỏ rồi ghi PASS chung. Lỗi nhỏ ⇒ ghi `PASS có khuyết điểm` và nêu rõ.

**Ngưỡng reject tự động (Reviewer1 PHẢI reject):** bằng chứng không tái lập được · có dấu hiệu bịa ·
thiếu nguồn thứ hai cho khẳng định quan trọng · kiểm tra mù lệch mà chưa giải thích.

---

## 2. Nhật ký bài kiểm #1 — commit đầu tiên của Admin `abe0c3e`

**Đối tượng:** Admin (`Admin AgentMeet <admin@agentmeet.local>`) · **Task:** T0 (khung repo)
**Revision kiểm:** `abe0c3e55f3404dc0c623d67734b79856c933fd9` (root commit)
**Bản sao dùng để kiểm:** `rm -rf /tmp/rv1-fresh && git clone git@github.com:TranQuy-lab/agentmeeting.git /tmp/rv1-fresh`
**Bằng chứng thô:** `agents/reviewer1/evidence/T6/01..06-*.txt`

### 2.1 Kết quả từng mục

| # | Mục kiểm | Lệnh đã chạy lại | Output thô | Kết quả |
|---|---|---|---|---|
| A1 | `abe0c3e` tồn tại | `git clone …` rồi `git log --oneline` | `abe0c3e [T0] log: khung kho AgentMeet + ho so dieu hanh Admin (commit dau tien)` | **PASS** |
| A1b | `abe0c3e` là **commit gốc** (không phải commit chèn) | `git rev-list --max-parents=0 HEAD` → `abe0c3e…`; `git rev-list --parents -n1 abe0c3e` → chỉ 1 hash = không có parent | `abe0c3e55f3404dc0c623d67734b79856c933fd9` | **PASS** |
| A2 | Mọi họ file đề bài yêu cầu có thật | `git show --stat abe0c3e`; `git ls-tree -r --name-only abe0c3e \| sort` | 32 file / 337 dòng chèn; xem EV02 | **PASS có khuyết điểm** (xem 2.2) |
| A3 | **Rò rỉ credential** | `git log -p --all \| grep -iE "agent_token\|creds\|password\|api[_-]?key"` | Khớp **đúng 1 dòng**: `+*creds*.json` — chính là quy tắc `.gitignore`, **không phải bí mật** | **PASS** |
| A3b | Quét mở rộng | đếm theo từng mẫu: `agent_token`→0, `password`→0, `api[_-]?key`→0, `bearer`→0, `BEGIN … PRIVATE KEY`→0 | xem EV03 | **PASS** |
| A3c | Bí mật nhúng dạng chuỗi dài | `git show abe0c3e:<f> \| grep -oE "[A-Za-z0-9+/=_-]{40,}"` cho **mọi** file | **không có dòng nào** | **PASS** |
| A4 | `ADMIN/LOG.md` khớp bằng chứng | xem §2.3 | xem §2.3 | **FAIL cục bộ** (2 quyết định có khuyết điểm) |
| A5 | `ADMIN/SUMMARY.md` có kết luận vượt bằng chứng? | `git show abe0c3e:ADMIN/SUMMARY.md` | §1 và §2 đều ghi `*Chưa có.*` ⇒ **không có kết luận nào để vượt bằng chứng** | **PASS nội dung / FAIL tự nhất quán** (xem 2.4) |
| A6 | Số liệu "852 + 3658 ký tự" (LOG #8) | API transcript: `len(content)` của msg #6/#7 | `msg #6 = 851`, `msg #7 = 3657` (lệch đúng **1 ký tự**/tin = ký tự xuống dòng cuối file) | **PASS** (khớp trong sai số 1 ký tự) |
| A7 | "`__main__.py` dòng 199-210 chặn join thiếu `--rejoin`" (LOG #7) | `sed -n '199,213p' /home/noble-tran/agent-meet_skill/agentmeet/__main__.py` | `if not args.rejoin:` (d.199) … `elif known:` (d.206) → `raise SystemExit(` (d.208, đóng ở d.211) | **PASS** (lệch 1 dòng do dấu `)` đóng) |
| A8 | "Admin đổi danh tính sang `ag_cd389846`" (LOG #5) | đọc `agent_id` của mọi tin `Admin` trong transcript | `ag_9026ba92` → 1 tin (#1); `ag_cd389846` → 7 tin (#6,7,13,15,17,21,22) | **PASS** |
| A9 | "danh tính cũ bị đánh dấu `kicked`" (LOG #5) | `GET /api/v1/ab1-478d-cfa7/status` | `{"agents":{"active":10,"pending":5}, …}` — **API không trả trạng thái từng agent** | **chưa xác minh** |
| A10 | "Phòng giới hạn 500 tin" (SUMMARY rủi ro #1) | `/status` | `"max_messages": 500` | **PASS** |
| A11 | Ngày tháng trong hồ sơ | `git grep -c "2025-10-01" abe0c3e` vs `date` | **18 lần / 10 file** ghi `2025-10-01`; ngày hệ thống và ngày commit thật đều **`2026-10-01`** | **FAIL** (sai năm, hệ thống) |

### 2.2 Khuyết điểm của A2 (khung file)

Đủ 100% các họ file đề bài yêu cầu: `README.md`, `INDEX.md`, `ADMIN/` (6), `reviews/` (4),
`rooms/**` (3), `agents/*/tasks/` (đủ 7/7 slug), `.gitignore`.
**Nhưng:** `research/` và `security/` **chỉ có `.gitkeep`, không có nội dung nào**. Đó là đúng
tinh thần "khung" nhưng phải nói rõ: **không có artifact nghiên cứu/an ninh nào trong commit này.**
Cũng KHÔNG có `reviews/AUDIT.md` dù `INDEX.md` dòng 19 liệt kê nó (chấp nhận được ở giai đoạn khung).

### 2.3 Đối chiếu `ADMIN/LOG.md` ↔ thực tế commit

| # | Quyết định | Kiểm chứng | Kết quả |
|---|---|---|---|
| 1 | Dựng khung + push commit đầu lên `main` | `abe0c3e` là root commit, `origin/main` chứa nó | **PASS** |
| 2 | Admin tự viết `README.md` + `INDEX.md` | `git log -- README.md INDEX.md` → chỉ `abe0c3e`, author `Admin AgentMeet` | **PASS** (nhưng xem §3 mâu thuẫn với INDEX.md) |
| 3 | Giữ nguyên luật cấm §4 trong prompt | `ADMIN/ROSTER.md`, `ADMIN/ASSIGNMENTS.md` có thật; `README.md` §"Luật bất biến" 1-6 khớp | **PASS** |
| 4 | Cho ExploitDeep kích hoạt ngay khi T3 xong | `ADMIN/ASSIGNMENTS.md` dòng 21 "T4 phụ thuộc T3." + dòng 25-26 | **PASS** |
| 5 | Đổi danh tính Admin sang `ag_cd389846` | transcript: tin Admin đầu = `ag_9026ba92`, mọi tin từ #6 = `ag_cd389846` | **PASS phần danh tính** / **chưa xác minh phần "kicked"** |
| 6 | Cấp mỗi agent một thư mục clone RIÊNG | **Bằng chứng ghi `ADMIN/ASSIGNMENTS.md` là SAI**: `git show 879d69d:ADMIN/ASSIGNMENTS.md \| grep -nE "clone\|agentmeeting-"` → **không dòng nào khớp**. `git grep -n "agentmeeting-" 879d69d` → chuỗi chỉ xuất hiện **duy nhất trong chính `ADMIN/LOG.md` dòng 14** (tự viện dẫn). Trên máy có thật 8 thư mục: `agentmeeting` + `-auditor2 -bountyrecon -docwriter -exploitdeep -forensicsmal -researchlead -reviewer1` | **FAIL — bằng chứng trỏ sai** (quyết định đúng, ô bằng chứng sai) |
| 7 | Sửa lệnh join thành `--rejoin` + bắt buộc `--as` | đọc `__main__.py` d.199-211; `SystemExit` có thật | **PASS** |
| 8 | Tách D-001 thành msg #6 + #7 vì giới hạn 4000 | msg #6 = 851 ký tự, msg #7 = 3657 ký tự | **PASS** (khớp claim 852+3658 sai số 1) |
| 9 | Push khung TRƯỚC khi thả worker | commit `abe0c3e` lúc `2026-10-01 20:43:58`; Reviewer1 check-in lúc `13:47:49Z` = `20:47:49+07` ⇒ sau 3m51s | **PASS** |
| 10 | Giữ 4 dòng bất khả xâm phạm trong D-005 | `rooms/ab1-478d-cfa7/directives.md` D-005 có đủ 6 dòng cấm | **PASS** |
| 11 | Thả 7 worker theo T1-T7 | `ADMIN/ASSIGNMENTS.md` có đủ T1..T7 với owner | **PASS** |
| — | **Định dạng bảng** | `git show 879d69d:ADMIN/LOG.md \| cat -n` → **dòng 12 TRỐNG**, nằm giữa dòng 11 (`\| 4 \|…`) và dòng 13 (`\| 5 \|…`) | **FAIL — thiếu sót trình bày**: bảng bị chẻ làm hai; 7 quyết định #5-#11 nằm ngoài bảng, không có dòng tiêu đề/`\|---\|` ⇒ hầu hết renderer hiển thị chúng như văn bản thô, không thành bảng |

**Kết luận A4:** 11/11 quyết định đều **có thật và đa số tái lập được**, **không phát hiện bịa đặt**.
Nhưng có **2 khuyết điểm thật**: (a) quyết định #6 trỏ bằng chứng sai; (b) bảng bị chẻ bởi dòng trống 12.

### 2.4 `ADMIN/SUMMARY.md` — có kết luận nào vượt bằng chứng?

- §1 "Kết quả đã nghiệm thu" = `*Chưa có.*`; §2 = `*Chưa có.*` ⇒ **không có kết luận nào để vượt bằng chứng.** **PASS.**
- Rủi ro #1 "giới hạn 500 tin" ⇒ `/status` trả `max_messages: 500`. **PASS.**
- Rủi ro #2 "Đã xử lý — Đã push khung ở commit đầu tiên" ⇒ `abe0c3e` là root commit. **PASS.**
- Rủi ro #3 "HTTPS credential helper hỏng" ⇒ **`chưa xác minh`**: luật D-001 **CẤM** dùng HTTPS để clone nên tôi không được phép kiểm. Ghi thẳng là chưa xác minh, không suy đoán.
- **FAIL tự nhất quán:** chính SUMMARY.md dòng 6-7 đặt luật "Mọi kết luận đưa vào đây PHẢI trỏ tới
  đường dẫn bằng chứng cụ thể trong repo", nhưng bảng rủi ro (dòng 19-23) **không có cột bằng chứng nào**.
  `grep -nE "Bằng chứng|commit|\.md"` chỉ khớp dòng 6, 7, 22 ⇒ ô "Đã xử lý" là kết luận không có đường dẫn.
- SUMMARY.md **không được cập nhật** ở `879d69d` dù có 7 quyết định điều phối mới.

---

## 2.5 Kiểm LẠI trên `main` hiện hành `a414944` (bắt buộc — không chấm PASS trên revision cũ)

Trong lúc tôi kiểm, `origin/main` đã tiến từ `879d69d` lên **`a414944`**
(`[T0] log: duyet slot 8 DeepSeek-Harness (D-006), tu choi slot ZCode (D-007), cap nhat ROSTER/ASSIGNMENTS/LOG`).
Để không tố cáo một khuyết điểm đã được sửa, tôi **kiểm lại toàn bộ khuyết điểm trên `a414944`**.
Bằng chứng thô: `agents/reviewer1/evidence/T6/08-main-tien-hoa-kiem-lai.txt`.

| Mã | Khuyết điểm | Trạng thái trên `abe0c3e`/`879d69d` | Trạng thái trên `a414944` (HEAD) |
|---|---|---|---|
| **DEF-1** | `ADMIN/LOG.md` **dòng 12 trống** ⇒ bảng bị chẻ đôi | Có (7 quyết định #5-#11 ngoài bảng) | **VẪN CÒN, nặng hơn**: `awk 'NR>=8 && /^$/ {print NR}'` → `dong trong tai dong 12`; nay **10 quyết định #5-#14** nằm ngoài bảng |
| **DEF-2** | `ADMIN/ASSIGNMENTS.md` dòng **T8 nằm NGOÀI bảng** phân công | Chưa có T8 | **MỚI PHÁT SINH**: bảng kết thúc ở dòng 15; dòng 27 `\| T8 \| DeepSeek-Harness \|…` bị chèn **sau phần "Ghi chú điều phối"** (dòng 19-26) ⇒ T8 không render thành hàng bảng |
| **DEF-3** | Hồ sơ ghi Admin = `ag_9026ba92` (đã hết hiệu lực) | Có | **VẪN CÒN**: `README.md` d.3, `ADMIN/ROSTER.md` d.3 + d.11, `ADMIN/ASSIGNMENTS.md` d.3 |
| **DEF-4** | `INDEX.md` ô #2 tự khai `DocWriter` / `⏳ chờ dựng` | Có | **VẪN CÒN** (nguyên văn dòng 10) |
| **DEF-5** | Sai năm: `2025-10-01` | 18 vị trí / 10 file | **VẪN CÒN, tăng lên 27 vị trí / 10 file** (`ADMIN/LOG.md` từ 4 → 14) |
| **DEF-6** | `ADMIN/SUMMARY.md` bảng rủi ro không có cột bằng chứng | Có | **VẪN CÒN** (file không được sửa ở `a414944`) |
| **DEF-7** | `ADMIN/LOG.md` #6 trỏ bằng chứng sai | Có | **VẪN CÒN** |

**Ghi nhận đúng (không hạ bệ):** `a414944` **sửa đúng** phần `ADMIN/ROSTER.md` hàng 9 (thêm `DeepSeek-Harness` đúng
vào trong bảng, dòng `+\| 9 \| DeepSeek-Harness \|…`) và ghi rõ lý do mở slot + lý do từ chối ZCode.
Đây là **PASS** cho phần đó — tôi ghi nhận, không hạ bệ.

**Tổng kết `a414944`:** 7 khuyết điểm được kiểm lại, **7/7 vẫn còn nguyên** (1 trong số đó — DEF-2 — mới phát sinh).
**Cập nhật cuối:** `origin/main` tiếp tục tiến lên **`0f010b7`** (`[T0] log: dinh chinh lenh CLI (D-008), duyet cai tool cho ExploitDeep (D-009), giao Reviewer1 T9`). Kiểm lại: **7/7 khuyết điểm VẪN CÒN**; `2025-10-01` nay **31 vị trí**; dòng **T9 bị thêm tiếp ra ngoài bảng** `ASSIGNMENTS.md` (dòng 28, nối sau dòng T8 ở dòng 27 — cả hai đều nằm ngoài bảng kết thúc ở dòng 15). Bằng chứng: `agents/reviewer1/evidence/T9/t9-raw-verify.txt` §V25.

---

## 2.6 Bài kiểm #2 — T9: Kiểm chứng bảng công cụ của ExploitDeep (Admin giao)

```text
[REVIEW] T9 / ExploitDeep (ag_367372ea) / Lớp 1 CROSS / KẾT QUẢ: PASS có 1 khuyết điểm phải sửa (unicorn)
```

- **Artifact kiểm:** `agents/exploitdeep/T4/READINESS.md` + `agents/exploitdeep/T4/EVIDENCE/tool_inventory_raw.txt`
- **Revision kiểm:** `2cbe90a20089d34f50b2df1cacd8624fdc0fd12f` (nhánh `agent/exploit-deep/T4`)
- **Thời điểm Reviewer1 kiểm:** `2026-10-01T13:55:45Z` (UTC) — nêu rõ vì Admin đã duyệt **D-009**
  (duyệt cài `fpylll`, `gmpy2`, `angr`, `unicorn`, `nmap`) tại **`13:54:20Z`**, tức **85 giây TRƯỚC** khi tôi kiểm.
- **Môi trường kiểm:** `Linux noble-tran-XiaoXin-14-AHP9 7.0.0-34-generic … x86_64` · `python3 3.12.3` · `gcc 13.3.0`
- **Bằng chứng thô:** `agents/reviewer1/evidence/T9/t9-raw-verify.txt` (§V1-§V26)

**Phương pháp:** tôi **tự chạy lại đúng các lệnh kiểm kê**, không đọc bảng rồi tin. Mọi dòng "CÓ"/"THIẾU"
được đối chiếu bằng `which`/`command -v`, `import` thật trong cả `python3` hệ thống **và** venv
`/home/noble-tran/.venvs/ed`, `pip list` **không lọc** (để không bỏ sót), và kiểm chứng chéo bằng
`pip show … | grep Required-by`.

### 2.6.1 Kết quả đối chiếu từng bảng — 47/47 dòng đã kiểm

| Bảng trong `READINESS.md` | Số dòng | Xác nhận đúng | Bác bỏ | Ghi chú |
|---|---|---|---|---|
| §1.1 "Có sẵn" (system + venv) | 14 | **14** | 0 | `python3 3.12.3`, `gcc 13.3.0-6ubuntu2~24.04.1`, `gdb`/`objdump`/`readelf`/`strings`/`nm`/`curl`/`jq`/`file`/`git`/`ssh` tại `/usr/bin/…`, `requests 2.31.0`, `venv OK`, venv `ed` |
| §1.2 "THIẾU" (trạng thái `python3` HỆ THỐNG) | 15 | **15** | 0 | `checksec`, `pwn`, `Crypto`, `sympy`, `z3`, `capstone`, `lief`, `unicorn`, `angr`, `gmpy2`, `fpylll`, `flask_unsign` → `ModuleNotFoundError`; `nmap` → `command not found`; `pip`/`ensurepip` → `No module named …`; `sage` → không có trong PATH, không có `/usr/bin/sage`, không có `/usr/local/bin/sage` |
| §1.4 "Kết quả cài đặt THẬT" (venv `ed`) | 12 | **12** | 0 | `pip 26.2.1` · `pwntools 4.15.0` · `pycryptodome 3.23.0` · `sympy 1.14.0` · `z3-solver 5.1.0.0` · `capstone 6.0.0a11` · `lief 1.0.0` (`lief.__version__` = `1.0.0-d05b3499b`) · `ROPGadget 7.7` · `ropper 1.13.13` · `flask-unsign 1.2.1` · `requests 2.34.2` · `checksec` CLI |
| §1.5 "VẪN THIẾU sau khi cài" | 6 | **5** | **1** | ❌ **`unicorn` — BÁC BỎ**, xem §2.6.2 |
| **Tổng** | **47** | **46** | **1** | |

**Kiểm chứng `checksec` chạy thật:** tôi chạy lại
`/home/noble-tran/.venvs/ed/bin/checksec --file=/bin/ls` → output **khớp từng dòng** với bảng tác giả
(`Full RELRO` / `Canary found` / `NX enabled` / `PIE enabled` / `FORTIFY Enabled` / `SHSTK Enabled` / `IBT Enabled`).
Và `/home/noble-tran/.venvs/ed/bin/checksec --version` → `pwn: error: unrecognized arguments: --version`
— **đúng như tác giả đã ghi nhận trung thực**. **PASS.**
**Kiểm chứng mạng:** `urllib.request.urlopen('https://pypi.org/simple/')` → `200`. **PASS.**
**Kiểm chứng cổng:** `security/` tại đúng revision `2cbe90a` **chỉ có `.gitkeep`** ⇒ cổng T4 vẫn đóng,
khớp kết luận §0 của tác giả. **PASS.**

### 2.6.2 ❌ Khuyết điểm DUY NHẤT — `unicorn` bị khai "vẫn thiếu" nhưng THỰC TẾ ĐÃ CÓ

**Nguyên văn tác giả** (`READINESS.md`):
- dòng **121**: `` `nmap`, `gmpy2`, `fpylll`, `angr`, `unicorn`, `sage` → **vẫn thiếu** ``
- dòng **279**: `` **Còn thiếu thật:** `fpylll`/`gmpy2` (lattice), `angr` (symbolic), `unicorn` (emulation), `sage` ``
- dòng **60** (bảng §1.2): `| unicorn | ModuleNotFoundError: No module named 'unicorn' | không emulate code |`

**Thực tế tôi đo được:**
- `pip list` **không lọc** trong venv `ed` → `unicorn 2.1.2`
- `import unicorn` **trong venv** → `2.1.2` (thành công)
- `pip show unicorn` → `Required-by: pwntools`

**Truy nguyên thời điểm — đây là mấu chốt:**
- mtime `site-packages/unicorn-2.1.2.dist-info` = `2026-10-01 20:47:42 +0700` = **`13:47:42Z`**
- **D-009** (duyệt cài `unicorn`) ký tại commit `0f010b7` lúc `2026-10-01 20:54:20 +0700` = **`13:54:20Z`**
- ⇒ `unicorn` đã có **TRƯỚC D-009 đúng 6 phút 38 giây**. **D-009 KHÔNG thể là nguyên nhân.**

**Nguyên nhân gốc (lỗi phương pháp, không phải lỗi thời điểm):**
1. `unicorn` được cài như **dependency của `pwntools`** (`pip show unicorn` → `Required-by: pwntools`)
   trong chính đợt cài của tác giả — nhưng lệnh kiểm chứng của tác giả dùng
   `` pip list | grep -Ei 'pwntools|pycryptodome|sympy|z3|capstone|lief|ropgadget|ropper|flask|requests|pip ' ``
   (**trích nguyên văn**, `tool_inventory_raw.txt` dòng 113) — **mẫu grep này KHÔNG chứa `unicorn`**
   ⇒ dù có cài, bảng cũng không thể hiện.
2. Tác giả **chưa bao giờ chạy `import unicorn` bên trong venv**. Lệnh `import unicorn` duy nhất
   (`tool_inventory_raw.txt` dòng 51) chạy bằng **`python3` hệ thống** — đúng kết quả `ModuleNotFoundError`,
   nhưng đó là **môi trường khác**.
3. Hệ quả: kết luận "vẫn thiếu" của bảng §1.2 (hệ thống) bị **suy diễn sai sang venv** ở §1.5.

**Ảnh hưởng tới năng lực T4:** câu "không emulate code" / "unicorn (emulation) còn thiếu" là **sai** —
emulation qua `unicorn 2.1.2` **đã dùng được**. (Các hệ quả khác vẫn đúng: `angr` thiếu ⇒ chưa có
symbolic execution; `fpylll`/`gmpy2` thiếu ⇒ chưa có lattice reduction; `nmap` thiếu.)

**Đề xuất cho ExploitDeep (Reviewer1 KHÔNG tự sửa — chỉ báo cáo):**
1. Sửa `READINESS.md` dòng 60, 121, 279: chuyển `unicorn` sang nhóm ĐÃ CÓ trong venv (`2.1.2`,
   dependency của `pwntools`), kèm lệnh chứng minh.
2. **Sửa quy trình kiểm kê (quan trọng hơn cả việc sửa số liệu):** bỏ `grep` lọc tay — dùng
   `pip list` **không lọc** và ghi **toàn bộ** output, hoặc `pip freeze`. Mọi kết luận "thiếu" phải
   được chứng minh bằng `import <mod>` **trong đúng interpreter đang xét**, nêu rõ interpreter đó là ai.
3. Ghi rõ trong mọi bảng: dòng nào là `python3` hệ thống, dòng nào là venv `ed` — hiện §1.2 và §1.5
   đang trộn hai môi trường nên dễ suy diễn sai (đúng như lỗi này).

### 2.6.3 Ghi nhận công bằng (PASS thật, không hạ bệ)

- Tác giả **tự nguyện khai điểm yếu** và **tự chặn mình**: `READINESS.md` §0 kết luận cổng T4 **ĐANG ĐÓNG**
  và cam kết "không chạm bất kỳ hệ thống thật nào" — **tôi xác nhận đúng**: `security/` chỉ có `.gitkeep`.
- Ghi trung thực việc `checksec --version` **không** được hỗ trợ, dù điều đó làm bảng kém "đẹp".
- Ghi **cả hai trạng thái** (trước/sau khi cài) kèm cảnh báo "bảng trên là trạng thái `python3` HỆ THỐNG
  TRƯỚC khi cài" — chính sự trung thực này giúp tôi truy được lỗi. Nếu tác giả gộp hai môi trường
  không ghi chú, lỗi `unicorn` đã khó phát hiện hơn nhiều.
- Toàn bộ 46/47 dòng còn lại **khớp chính xác**, kể cả các phiên bản khó (`capstone 6.0.0a11` vs
  `__version__` báo `6.0.0`, `lief 1.0.0` vs `1.0.0-d05b3499b`) — tác giả đã phân biệt đúng.

**Phán quyết T9:** **PASS có 1 khuyết điểm phải sửa.** Không có dấu hiệu bịa đặt: 46/47 dòng tái lập
được từng ký tự. Khuyết điểm `unicorn` là **lỗi suy diễn giữa hai môi trường python**, không phải
ngụy tạo số liệu — mức độ: **phải sửa, không cần reject toàn bộ artifact**. Tuy nhiên tôi **yêu cầu
ExploitDeep sửa cả quy trình kiểm kê** (§2.6.2 đề xuất 2), vì đây là dạng lỗi sẽ lặp lại ở mọi task sau.

---

## 3. Bảng kiểm chứng chéo (mẫu chuẩn — dùng cho mọi task sau)

| Task | Tác giả | Lệnh đã chạy lại | Output thô | Kết quả | Ghi chú |
|---|---|---|---|---|---|
| T0 / `abe0c3e` | Admin | `git clone`, `git show --stat abe0c3e`, `git log -p --all \| grep -iE "agent_token\|creds\|password\|api[_-]?key"`, `sed -n '199,213p' __main__.py`, API transcript | `agents/reviewer1/evidence/T6/01..06-*.txt` | **PASS** (khung có thật, tái lập được, **không rò rỉ credential**) kèm 2 FAIL cục bộ ở LOG #6 và định dạng bảng | Xem §2.3 |
| T0 / `a414944` | Admin | `git show a414944:ADMIN/LOG.md`, `…:ADMIN/ASSIGNMENTS.md`, `git show a414944 -- ADMIN/ROSTER.md` | `agents/reviewer1/evidence/T6/08-main-tien-hoa-kiem-lai.txt` | **PASS một phần**: ROSTER hàng 9 sửa **đúng**; 7 khuyết điểm DEF-1..DEF-7 **còn nguyên** | Xem §2.5 |
| T9 / `2cbe90a` | ExploitDeep | `which`/`command -v`, `import` thật trong `python3` **và** venv `ed`, `pip list` **không lọc**, `pip show … \| grep Required-by`, `checksec --file=/bin/ls`, `urlopen(pypi)` | `agents/reviewer1/evidence/T9/t9-raw-verify.txt` (§V1-§V26) | **PASS có 1 khuyết điểm**: 46/47 dòng đúng; **`unicorn` bị khai "vẫn thiếu" nhưng thực tế có `2.1.2`** | Xem §2.6 |
| — | — | *(chỗ trống cho T1..T8)* | — | — | — |

---

## 4. Đã kiểm những mục nào (bắt buộc — cấm báo "OK" chung chung)

**Bài kiểm #1 — `abe0c3e` của Admin: đã kiểm 11 mục (A1, A1b, A2, A3, A3b, A3c, A4, A5, A6, A7, A8) + 2 mục phụ (A9, A10) + 1 mục hệ thống (A11).**
**Bài kiểm #1b — kiểm lại trên `main` hiện hành `a414944`: đã kiểm 7 khuyết điểm (DEF-1..DEF-7) + 1 điểm đã sửa đúng.**
**Bài kiểm #2 (T9) — `READINESS.md` + `tool_inventory_raw.txt` của ExploitDeep @ `2cbe90a`: đã kiểm 47 dòng bảng + 3 kiểm chứng phụ.**

- **PASS:** A1, A1b, A2 (có khuyết điểm về nội dung rỗng của `research/`+`security/`), A3, A3b, A3c, A5 (nội dung), A6, A7, A8, A10 — **11 mục**.
- **FAIL:** A4 (LOG #6 bằng chứng trỏ sai + bảng chẻ đôi), A5 (tự nhất quán của SUMMARY), A11 (sai năm ở 18 vị trí) — **3 mục**.
- **PASS (ghi nhận trên `a414944`):** `ADMIN/ROSTER.md` hàng 9 thêm `DeepSeek-Harness` **đúng trong bảng** — **1 mục**.
- **FAIL còn nguyên trên `a414944`:** DEF-1 (LOG bảng chẻ đôi, nay 10 dòng ngoài bảng), DEF-2 (**T8 ngoài bảng ASSIGNMENTS** — mới), DEF-3 (danh tính Admin hết hiệu lực), DEF-4 (INDEX ô #2 sai), DEF-5 (sai năm, nay 27 vị trí), DEF-6 (SUMMARY thiếu cột bằng chứng), DEF-7 (LOG #6 bằng chứng sai) — **7 mục**.
- **FAIL còn nguyên trên `0f010b7` (mới nhất):** 7/7 DEF **còn nguyên**; `2025-10-01` nay **31 vị trí**; **T9 lại bị thêm ra ngoài bảng** `ASSIGNMENTS.md` (dòng 28) — **3 mục**.
- **T9 PASS:** **46/47 dòng** bảng khớp chính xác (14/14 §1.1 · 15/15 §1.2 · 12/12 §1.4 · 5/6 §1.5);
  3 kiểm chứng phụ PASS (`checksec --file=/bin/ls` khớp từng dòng · PyPI `HTTP 200` · `security/` chỉ `.gitkeep` ⇒ cổng T4 đóng đúng như tác giả kết luận).
- **T9 BÁC BỎ 1 mục:** `unicorn` — tác giả khai "vẫn thiếu" (dòng 60, 121, 279), thực tế **có `2.1.2`** trong venv `ed`,
  `Required-by: pwntools`, cài lúc `13:47:42Z` — **trước D-009 (`13:54:20Z`) 6 phút 38 giây**.
- **T9 lỗi phương pháp:** mẫu `grep` của tác giả (raw dòng 113) **không chứa `unicorn`**; tác giả **chưa từng chạy
  `import unicorn` trong venv** (lệnh duy nhất, raw dòng 51, chạy bằng `python3` hệ thống) ⇒ suy diễn sai giữa hai môi trường.
- **chưa xác minh:** A9 ("kicked") — API không trả trạng thái từng agent; và claim 4892 ký tự → HTTP 422 **chưa xác minh trực tiếp** (tôi không gửi tin quá 4000 ký tự để thử; gián tiếp ủng hộ: tin 3988 ký tự của tôi gửi thành công, và `/status` xác nhận phòng đang chạy với `max_messages: 500`). — **2 mục**.

**Chưa kiểm (chưa có artifact):** T1 (DocWriter), T2 (ResearchLead), T3 (BountyRecon), T4 (ExploitDeep —
phần finding, chưa có `FINDING.md`), T5 (ForensicsMal), T7 (Auditor2), T8 (DeepSeek-Harness).
**Không có mục nào trong số này được chấm PASS.**

> **Phán quyết bài kiểm #2 (T9):** `READINESS.md` của ExploitDeep **PASS có 1 khuyết điểm phải sửa**.
> 46/47 dòng tái lập được **từng ký tự** ⇒ **không có dấu hiệu bịa đặt**. Khuyết điểm `unicorn` là
> **lỗi suy diễn giữa hai môi trường python**, không phải ngụy tạo số liệu ⇒ **không reject toàn bộ artifact**,
> nhưng **yêu cầu sửa cả quy trình kiểm kê** (bỏ `grep` lọc tay, dùng `pip list` không lọc, mọi kết luận
> "thiếu" phải chứng minh bằng `import` trong **đúng** interpreter và nêu rõ interpreter đó).

> **Phán quyết bài kiểm #1:** commit `abe0c3e` **PASS** ở tầng "khung có thật, tái lập được, không rò rỉ credential".
> Hồ sơ điều hành kèm theo có **7 khuyết điểm phải sửa** (DEF-1 LOG bảng chẻ đôi · DEF-2 T8 ngoài bảng ASSIGNMENTS ·
> DEF-3 danh tính Admin hết hiệu lực · DEF-4 INDEX ô #2 sai · DEF-5 sai năm 27 vị trí · DEF-6 SUMMARY thiếu cột bằng chứng ·
> DEF-7 LOG #6 bằng chứng trỏ sai). Đây là khuyết điểm **trình bày/truy vết**, **không phải bịa đặt kỹ thuật** —
> nên tôi **không reject** commit khung, nhưng **yêu cầu Admin sửa 7 mục** trước khi nghiệm thu bất kỳ báo cáo cuối nào.
>
> **Điểm đã sửa đúng (ghi nhận công bằng):** `a414944` thêm `DeepSeek-Harness` vào `ADMIN/ROSTER.md` **đúng trong bảng**.

---

# VÒNG 2 — Bài kiểm #3, #4, #5 (T11, T14, T10)

**Người kiểm:** Reviewer1 (`ag_76306ba6`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/reviewer-1/T11`
**Base:** `origin/main` = `28cdc00` · **Thời điểm kiểm:** `2026-10-01T14:03Z` → `14:26Z`

---

## 2.7 Bài kiểm #3 — T11: hai nguồn đang chặn tính mới (cao nhất)

```text
[REVIEW] T11 / ResearchLead (ag_d85dde8d) / Lớp 1+2 / KẾT QUẢ: S31 = CHẮC CHẮN (đọc toàn văn)
                                              S29 = chưa xác minh toàn văn + PHÁT HIỆN DOI SAI
```

**Artifact kiểm:** `research/RANKING.md`, `research/{pqc-tls-migration,ebpf-microsegmentation}/SOURCES.md`
@ `a23c004` · **Bằng chứng thô:** `agents/reviewer1/evidence/T11/`

### 2.7.1 Bảng đối chiếu S29 / S31

| # | Khẳng định của ResearchLead | Lệnh đã chạy lại | Output thô | Kết quả |
|---|---|---|---|---|
| S31-1 | Title/author/ngày S31 | `curl -sL 'http://export.arxiv.org/api/query?id_list=2603.11006'` | HTTP 200; `Layered Performance Analysis of TLS 1.3 Handshakes…`; Gómez-Cambronero, Munteanu, González-Tablas; entry `updated=2026-07-07T10:08:49Z` | **PASS** (khớp cả 3) |
| S31-2 | "hơn 30 thí nghiệm" | trích abstract | *"Across more than thirty experiments"* | **PASS** |
| S31-3 | "backend đổi kích thước phản hồi" | trích abstract | *"Each set of tests also varied the backend response size"* | **PASS** |
| S31-4 | **Đọc được TOÀN VĂN** | `curl -sL 'https://arxiv.org/html/2603.11006v2'` | HTTP 200 · 368.458 B HTML → bóc thẻ = **64.256 ký tự**; PDF 618.743 B | **PASS — ĐÃ ĐỌC TOÀN VĂN** |
| S31-5 | **(K1) S31 KHÔNG bao phủ biên/middlebox/MTU/chứng thư ML-DSA** | đếm từ khoá trong toàn văn | `MTU`=**0** · `middlebox`=**0** · `fragment`=**0** · `packet size`=**0** · `network layer`=**0** · `tunnel`=**0** · `VPN`=**0** · `certificate chain`=**0** · `edge`=**1** (ở 99,7% độ dài = footer arXiv, KHÔNG phải kỹ thuật) | **K1 ĐƯỢC XÁC NHẬN** |
| S31-6 | ML-DSA có được S31 đo? | trích toàn văn | *"Additional tests varying the digital signature algorithm (e.g., ECDSA vs. ML-DSA vs. SLH-DSA) to isolate signature overhead are **planned as future work**"*; future-work list ghi *"evaluating post-quantum digital signature algorithms (Falcon, SPHINCS+, ML-DSA) and their impact on **certificate verification latency**"* | **KHÔNG đo — là FUTURE WORK** |
| S31-7 | S31 tự nêu khoảng hở nào? | trích toàn văn | *"extending the analysis to **real network environments with commercial load balancers and MiTM (Man-in-The-Middle) inspection devices**…"* | **S31 TỰ LIỆT KÊ ĐÚNG KHOẢNG HỞ CỦA T1 VÀO FUTURE WORK** |
| S31-8 | Venue/trọng số S31 | arXiv API `arxiv:comment` | *"Accepted in **SPIQE 2026** (Workshop on Secure Protocol Implementations in the Quantum Era), associated to **Euro S&P 2026**. v2 incorporates peer-review feedback…"* | **ĐÃ QUA BÌNH DUYỆT** — trọng số cao hơn "preprint" |
| S29-1 | DOI `10.1109/ICICT63348.2025.10989392` | `curl -sIL 'https://doi.org/10.1109/ICICT63348.2025.10989392'` | **HTTP 404** (doi.org) · Crossref **404** · OpenAlex **404** | **❌ DOI SAI** |
| S29-2 | DOI đúng là gì? | `curl -sL '…/works/10.1109/iccit63348.2025.10989392'` | **HTTP 200** — chữ thường `iccit` | **DOI ĐÚNG: `10.1109/iccit63348.2025.10989392`** |
| S29-3 | Metadata S29 (DOI đúng) | Crossref + OpenAlex | Title đầy đủ `…, Role-Based Access Control (RBAC), and Attribute-Based Access Control (ABAC)`; venue `2025 4th International Conference on Computing and Information Technology (ICCIT)`; tr. 181-189; 2025-04-13; Bello, Diyan, Asghar | **PASS** (khớp nhãn "ICCIT" mà ResearchLead ghi ở cột venue) |
| S29-4 | **Đọc được TOÀN VĂN S29?** | doi.org → IEEE Xplore (**202**); `xplorestaging…pdf` → trả **HTML captcha** không phải PDF; Teesside portal → **không có PDF** (`…/files/…pdf` **403**, `…/ws/portalfiles/…` **400**) | OpenAlex: `oa_status = **closed**`, `is_oa=False`, `any_repository_has_fulltext=False` | **`chưa xác minh` — KHÔNG lấy được toàn văn** |
| S29-5 | S29 có đo "cửa sổ hội tụ" không? | đọc **trừu tượng chính thức đầy đủ 1.215 ký tự** (OpenAlex) | Toàn văn trừu tượng **không** chứa `convergence`/`latency`/`measure`; mô tả: *"encompasses a comprehensive literature review, prototype design, and critical evaluation… The technical artefact, a prototype…"* | **chưa xác minh** (trừu tượng KHÔNG ủng hộ, nhưng trừu tượng ≠ toàn văn) |

### 2.7.2 PHÁT HIỆN MỚI — DOI S29 bị ghi SAI ở cả 4 tài liệu, nhưng metadata CÓ được xác minh thật

Đây là phát hiện quan trọng nhất của T11, và nó **không phải bịa đặt**:

- **Trong 4 tài liệu giao nộp**, DOI ghi HOA: `10.1109/**ICICT**63348.2025.10989392` →
  `BLINDCHECK.md:53`, `LITREVIEW.md:264`, `ebpf-microsegmentation/SOURCES.md:81`, `pqc-tls-migration/SOURCES.md:109`.
  Dạng HOA này **KHÔNG resolve được** (404 ở cả doi.org / Crossref / OpenAlex).
- **Trong chính file bằng chứng của ResearchLead**, DOI ghi THƯỜNG và **resolve được**:
  `openalex_doi_lookup.txt:15`, `openalex_title_filters.txt:50`, `crossref_lookups.txt:18`
  đều là `10.1109/**iccit**63348.2025.10989392`.
- ⇒ **Metadata S29 đã được xác minh thật** (họ tra đúng DOI). Lỗi là **sao chép sai hoa/thường
  vào 4 tài liệu giao nộp**. Đây là **lỗi chép chính tả**, KHÔNG phải bịa nguồn.
- **Tự mâu thuẫn nội bộ:** cùng một hàng bảng `SOURCES.md:81` ghi cột venue `IEEE **ICCIT**` nhưng
  cột DOI ghi `**ICICT**63348` — hai nửa của cùng một dòng không khớp nhau.

**Đề xuất (Reviewer1 KHÔNG tự sửa — ngoài territory):** sửa hoa/thường DOI tại 4 vị trí trên thành
`10.1109/iccit63348.2025.10989392`, và ghi kèm URL resolve được để người sau không mất thời gian.

### 2.7.3 Chấm lại tính mới (Lớp 2 — đối chiếu, chi tiết ở `reviews/RECONCILE.md` §6)

| Đề tài | ResearchLead chấm | Bằng chứng tôi đọc được | Kết luận của Reviewer1 |
|---|---|---|---|
| `RL-T1-PQC-TLS` | **N=2** (F×N×G = 24) | S31 **KHÔNG** bao phủ biên/middlebox/MTU/chứng thư ML-DSA (0 lần xuất hiện); S31 **tự ghi** hướng đó vào future work; ML-DSA signature/cert **"planned as future work"** | **N=2 KHÔNG được bằng chứng ủng hộ.** Bằng chứng ủng hộ **N=3 hoặc 4**. Tôi nghiêng **N=4** vì S31 tự liệt kê đúng khoảng hở đó vào future work ⇒ T1 = 3×4×4 = **48** (K1 xảy ra) |
| `RL-T2-EBPF-SEG` | **N=3** (F×N×G = 48) | Không lấy được toàn văn S29. Trừu tượng đầy đủ **không** nêu đo lường/hội tụ; S29 là `conference-paper`, `cited 9`, `closed` | **K2 vẫn MỞ — `chưa xác minh`.** Không có bằng chứng S29 đo cửa sổ hội tụ, nhưng **không thể loại trừ**. **Giữ N=3** và ghi rủi ro mở, KHÔNG tự nâng lên 4 |

> **Cách đọc kết quả này cho Admin:** T11 **không** kết luận "S29 đã làm rồi" (K2) và **không**
> kết luận "S31 vô hại" một cách cảm tính — mà **đọc toàn văn S31 để chứng minh K1**.
> Hệ quả: hai đề tài **hoà 48–48** theo kịch bản K1, tức ResearchLead **không còn cơ sở** để xếp
> `ebpf-microsegmentation` là hạng 1 duy nhất. Việc chọn đề tài phải quay lại Admin.

### 2.7.4 Kiểm riêng: 4 nguồn của S31 mà ResearchLead khai — có thật không?

| Nguồn ResearchLead khai | Tôi kiểm | Kết quả |
|---|---|---|
| S31 chưa có DOI | Crossref tra theo DOI arXiv → không có bản ghi tạp chí | **PASS** (đúng: chỉ có arXiv ID) |
| S31 là "mối đe doạ tính mới" | toàn văn xác nhận **cùng chủ đề** (per-layer TLS 1.3 PQC) | **PASS — đe doạ là THẬT** |
| S31 ngày `2026-03-11` (cập nhật `2026-07-07`) | arXiv API `published` / entry `updated` | **PASS chính xác** |
| S31 "chưa đọc toàn văn" | nay đã đọc được qua `arxiv.org/html` | **ĐÃ GIẢI QUYẾT** |

**Phán quyết T11:** **PASS về phương pháp** (không bịa nguồn; tự khai đúng chỗ chưa đọc được) ·
**1 LỖI PHẢI SỬA** (DOI sai hoa/thường ở 4 tài liệu) · **1 kết luận cần chỉnh** (T1 N=2 không có bằng chứng).

---

## 2.8 Bài kiểm #4 — T14: kiểm chứng chéo T3 BountyRecon

```text
[REVIEW] T14 / BountyRecon (ag_579fc4fa) / Lớp 1+2 / KẾT QUẢ: PASS
         (20/20 câu trích nguyên văn khớp · 3/3 policy byte-exact · 1 TINH CHỈNH nhỏ về "4 xung đột")
```

**Artifact kiểm:** `security/{gitlab,github,cloudflare}/SCOPE.md` + `RECON.md` @ `03d304b`
**Bằng chứng thô:** `agents/reviewer1/evidence/T14/t14-refetch-scope.txt` · script riêng `rv1_h1_refetch.py`

### 2.8.1 Policy — kiểm bằng hash, mạnh nhất có thể

Tôi **tự gọi lại** `POST https://hackerone.com/graphql` (không dùng script/JSON của BountyRecon) và
so **từng byte** với `policy_*.md` của họ:

| Chương trình | policy tôi fetch | policy của BountyRecon | SHA256 | Kết quả |
|---|---|---|---|---|
| GitLab | 26.083 ký tự | 26.083 ký tự | `1629f6dd7238ed166b5ab995f0ba1fab7a332e4941bee582c9b39d82a88f3c35` | **✅ BYTE-EXACT** |
| GitHub | 13.768 ký tự | 13.768 ký tự | `cddb4181b2ef35a0d8d0e145403e0914e4c7cdbc72bca52e3b281dec745c6585` | **✅ BYTE-EXACT** |
| Cloudflare | 44.784 ký tự | 44.784 ký tự | `a5997a98f915b09a5e360360e91e5762168de1a7904bd3b351990bca1d2a5c01` | **✅ BYTE-EXACT** |

Đồng thời tôi kiểm `policy_gitlab.md` là **bản dump trung thực 100%** của trường `policy` trong
`h1_gitlab.json` của chính họ: `md == policy` → **byte-exact** (GitLab và GitHub).

> **Minh bạch về một lần thất bại:** lần fetch **đầu tiên** của tôi, trường `policy` trả về **rỗng**
> (`policy_chars=0`) cho cả 3 chương trình. Fetch lại lần 2 thì được đủ. Tôi ghi lại vì đây là
> **hành vi không ổn định của endpoint công khai** — nếu người sau gặp `policy` rỗng thì **không phải
> BountyRecon bịa**, mà là endpoint chập chờn. Bản ghi đầy đủ ở `t14-refetch-scope.txt` §T14-5 và §T14-8.

### 2.8.2 Đối chiếu TỪNG DÒNG trích nguyên văn — 20/20 khớp

Kiểm từng câu `SCOPE.md` trích, tìm **nguyên văn** trong `policy_gitlab.md`, kèm **đúng số dòng** họ ghi:

| Con trỏ ResearchLead ghi | Thực tế | Kết quả |
|---|---|---|
| `# Rewards` **dòng 4 và 6** | d.4 = "…we pay $1000 at the time the report is triaged…"; d.6 = "$100 bounty…" | **✅ CHÍNH XÁC** |
| `# Rules of Engagement…` **dòng 34–59** | d.34 mở đầu đúng; d.41, d.55, d.57 nằm trong khoảng | **✅ CHÍNH XÁC** |
| `## Demonstrating Impact` **dòng 63–64** | d.63, d.64 khớp nguyên văn | **✅ CHÍNH XÁC** |
| `Testing on GitLab.com` **dòng 73** | d.73 khớp nguyên văn | **✅ CHÍNH XÁC** |
| `# Scope` **dòng 87–89** | d.87 + d.89 khớp (d.88 trống) | **✅ CHÍNH XÁC** |
| `## Out of scope` **dòng 125–191** | d.125 = `## Out of scope`, d.191 = "GitLab Development kit" | **✅ CHÍNH XÁC** |

**20/20 câu trích tìm thấy nguyên văn** (`All GitLab Inc. products are in scope…` · `Never test DoS
vulnerabilities on GitLab.com.` · `Never test against projects, groups, accounts, or instances you do
not own.` · `Automated scanning reports of any kind` · `Metadata disclosure, enumeration…` · `$1000…$500`
· `GitLab forest` …). **Không có câu nào bị viết lại, cắt ghép hay diễn giải thành "nguyên văn".**

### 2.8.3 Xác minh 4 xung đột scope GitLab bằng script ĐỘC LẬP — **1 TINH CHỈNH**

`python3 rv1_h1_refetch.py gitlab` → tổng **63** scope · IN=**24** · OUT=**39** ⇒ **khớp y hệt** con số BountyRecon khai.

Nhưng khi tách theo **cả `asset_identifier` VÀ `asset_type`**, kết quả khác đi:

| # | Tài sản | Phía IN | Phía OUT | Có phải xung đột THẬT? |
|---|---|---|---|---|
| 1 | `about.gitlab.com` | `URL` · eligible=**true** · bounty=true · medium | `URL` · eligible=**false** · bounty=false · none | ✅ **XUNG ĐỘT THẬT** (cùng `asset_type=URL` ở cả hai phía) |
| 2 | `docs.gitlab.com` | `URL` · eligible=**true** · bounty=true · medium | `URL` · eligible=**false** · bounty=false · none | ✅ **XUNG ĐỘT THẬT** |
| 3 | `*.gitlab.net` | `WILDCARD` · eligible=**true** · bounty=true · medium | `URL` · eligible=**false** · bounty=false · none | ⚠️ **KHÁC `asset_type`** — IN là **wildcard**, OUT là **apex URL** |
| 4 | `*.gitlap.com` | `WILDCARD` · eligible=**true** · bounty=true · medium | `URL` · eligible=**false** · bounty=false · none | ⚠️ **KHÁC `asset_type`** |

**Đọc đúng bản chất:**
- **2 xung đột thật** (`about`/`docs.gitlab.com`): cùng một URL xuất hiện hai lần với hai giá trị
  `eligible_for_submission` trái ngược trong **cùng** dữ liệu công bố ⇒ **mâu thuẫn dữ liệu**, không
  thể tự suy ra.
- **2 cặp wildcard/apex** (`*.gitlab.net`, `*.gitlap.com`): một chính sách **hoàn toàn có thể có ý**
  "subdomain thì trong scope, apex thì không" ⇒ **không chắc là mâu thuẫn**.
- **BountyRecon KHÔNG sai về dữ liệu**: bảng §2b của họ có ghi rõ cột "Dòng IN: `WILDCARD`" và
  "Dòng OUT: `URL`", và phần trích §1/§2a cũng giữ đúng `WILDCARD` vs `URL`. Cái cần chỉnh chỉ là
  **cách gọi tên**: "4 xung đột" nên là **"2 xung đột thật + 2 cặp wildcard/apex khác `asset_type`"**.
- **Khuyến nghị của họ vẫn ĐÚNG và nên giữ**: dừng lại, hỏi Admin, không tự đoán. Với 2 cặp
  wildcard/apex, việc loại luôn cả 4 là **thận trọng hơn mức cần** — không gây hại.

### 2.8.4 GitHub `Atom` và Cloudflare — kiểm 2 kết luận phụ của Admin

| Khẳng định | Tôi kiểm | Kết quả |
|---|---|---|
| BountyRecon: "GitHub cũng có 1 xung đột — `Atom`, nhưng cả hai phía đều `eligible_for_bounty=False`" | tôi fetch lại: IN = `DOWNLOADABLE_EXECUTABLES`, sub=**true**, **bounty=false**, `critical`; OUT = cùng type, sub=false, **bounty=false**, `none` | **✅ ĐÚNG CẢ HAI Ý** ⇒ kết luận "dù hiểu thế nào thì Atom cũng không được thưởng" **đúng** |
| D-013: "Cloudflare — KHÔNG mở T4. Chính sách Cloudflare cấm test vào khách hàng của họ" | tôi fetch lại Cloudflare: **0 xung đột** (IN=55, OUT=28, giao=∅); policy nguyên văn d.13 `* Do not perform tests against customers of Cloudflare.`; d.21 liệt kê `* Testing against Cloudflare customers, partners, service providers, suppliers, or vendors` là **cấm**; d.419 nêu **có thể khởi kiện** | **✅ D-013 KHỚP DỮ LIỆU TÔI TỰ FETCH** |
| D-013: loại 4 tài sản GitLab khỏi T4 (lựa chọn (a)) | khớp đề nghị §2b của BountyRecon | **✅ KHỚP** |

> **Điểm quan trọng:** lý do **không** mở T4 cho Cloudflare **không phải** xung đột scope
> (Cloudflare có **0** xung đột) mà là **điều khoản cấm test khách hàng**. D-013 ghi đúng như vậy —
> không có sự nhầm lẫn giữa hai lý do.

**Phán quyết T14:** **PASS.** 20/20 câu trích nguyên văn · 3/3 policy byte-exact bằng hash ·
63/24/39 scope khớp · kết luận Atom đúng · quyết định D-013 khớp dữ liệu tôi tự fetch.
**1 tinh chỉnh bắt buộc ghi lại:** "4 xung đột" → **2 xung đột thật + 2 cặp wildcard/apex khác `asset_type`**.

---

## 2.9 Bài kiểm #5 — T10: kiểm chứng chéo T1 DocWriter

```text
[REVIEW] T10 / DocWriter (ag_da78519d) / Lớp 1 / KẾT QUẢ: PASS — 6/6 mục khớp chính xác
```

**Artifact kiểm:** `INDEX.md` @ `6977d36` (nhánh `agent/doc-writer/T1`)
**Revision ghi chú:** `5bcea63` (mốc DocWriter ghi trong `INDEX.md` §đầu) · **`5bcea63` là tổ tiên của `6977d36`**
**Bằng chứng thô:** `agents/reviewer1/evidence/T10/t10-verify.txt`

| # | Khẳng định của DocWriter | Lệnh đã chạy lại | Output thô | Kết quả |
|---|---|---|---|---|
| T10-1 | Tổng file được track = **39** | `git ls-tree -r --name-only 6977d36 \| wc -l` | `39` (và `5bcea63` cũng `39`) | **✅ PASS** |
| T10-2 | `.md`=24 · `.gitkeep`=13 · `.jsonl`=1 · `.gitignore`=1 · còn lại=0 | đếm từng mẫu trên `6977d36` | `24 / 13 / 1 / 1 / 0` — **khớp từng con số**; 24+13+1+1=39 | **✅ PASS** |
| T10-3 | Bảng §2 có **39 hàng**, đánh số liên tục | parse `INDEX.md` | `so hang du lieu: 39` · `dai so thu tu: 1 -> 39` · `lien tuc? True` · `thieu so: (khong)` | **✅ PASS** |
| T10-4 | **7 file mới** (so với `abe0c3e`), 0 file bị xoá | `diff <(ls-tree abe0c3e) <(ls-tree 6977d36)` | 7 dòng `+` (`BAO-CAO-CHAT-LUONG.md`, `KIEM-TRA-KHUNG.md`, `digest-msg-0001-0012.md`, `digest/README.md`, `raw/MANIFEST.md`, `raw-msg-0001-0012.jsonl`, `rooms/.../README.md`); **0** dòng `-` | **✅ PASS — 7/7 file có thật** |
| T10-5 | SHA256 digest `66ac7183…8295` | `git show 6977d36:…raw-msg-0001-0012.jsonl \| sha256sum` | `66ac7183fadedd481ccc839e2c82ef05cbdef568065b11d4f8e546bc27e88295` | **✅ PASS — khớp từng ký tự** |
| T10-6 | digest có **12 bản ghi** | `… \| wc -lc` | `12  44186` ⇒ 12 dòng, 44.186 B (MANIFEST khai `44.186 B`) | **✅ PASS** |

**Kiểm chứng chéo con trỏ §4.2 của DocWriter (họ tự đính chính một lỗi của chính mình):**
`git show 6977d36:rooms/ab1-478d-cfa7/directives.md | grep -n "say"` → **không có kết quả**;
`grep -c '^## \[D-'` → **5** (D-001..D-005). ⇒ Khẳng định của họ *"`directives.md` KHÔNG chứa `say`"*
là **ĐÚNG**, và việc họ **tự đính chính** một câu sai trước đó là hành vi đúng kỷ luật D-004.

**Hash xuất hiện nhất quán ở 3 nơi** (INDEX §2 hàng 39 · `raw/MANIFEST.md` d.29+d.37 ·
`digest-msg-0001-0012.md` d.21) — cùng một giá trị đầy đủ, không nơi nào ghi khác.

> ⚠️ **Lưu ý revision (theo đúng yêu cầu của Admin):** con số **39 file đúng cho NHÁNH T1**
> (`6977d36` / `5bcea63`). `origin/main` hiện tại (`28cdc00`) có **46 file** — nhiều hơn 7 vì các
> nhánh khác đã merge sau đó. **Không được** dùng "39" để nói về `main`. `INDEX.md` ở revision
> `6977d36` mô tả `reviews/CROSS.md` là "khung 9 dòng, bảng rỗng" — điều này **đúng ở revision đó**
> (bản T6 của tôi được merge sau, ở `c579d1f`), nên **không phải lỗi lỗi thời** của DocWriter.

**Phán quyết T10:** **PASS — 6/6 mục khớp chính xác, không có sai lệch nào, không mục nào `chưa xác minh`.**

---

## 2.10 Phụ lục — Reviewer1 xác minh độc lập phát hiện N-03 của Auditor2

**Không thuộc task nào của tôi.** Tôi ghi vào đây vì tôi **đã khẳng định việc này với Admin trong báo cáo
vòng 2**, nên theo D-004 nó phải trỏ tới bằng chứng thô.
**Bằng chứng:** `agents/reviewer1/evidence/T11/t11-phuluc-N03-INDEX.md.txt`

| Lệnh | Output thô | Ý nghĩa |
|---|---|---|
| `git log --oneline origin/agent/doc-writer/T1 -- INDEX.md` | `6977d36` · `3be89fd` · `abe0c3e` | Nhánh T1 **sửa `INDEX.md` ở 2 commit** |
| `git show 3be89fd --stat` | `INDEX.md \| 179 +++---` | Commit đó đụng `INDEX.md` **179 dòng** |
| `git diff --stat origin/main origin/agent/doc-writer/T1 -- INDEX.md` | `200 insertions(+), 21 deletions(-)` | **Phân kỳ thật** giữa `main` và T1 trên cùng file |
| `git merge-base origin/main origin/agent/doc-writer/T1` | `abe0c3e` | T1 tách từ **commit gốc** |
| `git rev-list --count abe0c3e..origin/main` | `16` | `main` đi trước merge-base **16 commit** |
| `git show origin/main:INDEX.md \| sed -n '10p'` | `\| 2 \| \`INDEX.md\` \| **Admin** (DocWriter *chuẩn hoá* ở T1 — xem DISSENT-2) \| … ✅ hoàn tất trên \`main\` …` | Ô #2 = **bản vá DISSENT-2 của Admin** |
| `git show origin/agent/doc-writer/T1:INDEX.md \| sed -n '10p'` | *(dòng trống)* | Ở T1, dòng 10 **không chứa** bản vá đó |

**Kết luận:** xác nhận N-03 của Auditor2. `INDEX.md` **khác** `reviews/**`: với `reviews/**`, bản của
Reviewer1 mới hơn nên lấy bản worker là đúng; với `INDEX.md`, **bản của Admin chứa phán quyết DISSENT-2
mà nhánh T1 không có** ⇒ merge kiểu "lấy bản worker" sẽ **mất bản vá thật**. Đề nghị Admin merge
`INDEX.md` theo hướng **giữ bản `main`** hoặc hợp nhất thủ công.

---

# VÒNG 4 — Bài kiểm #7 (T21): T5 ForensicsMal + T13 javis

**Người kiểm:** Reviewer1 (`ag_76306ba6`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/reviewer-1/T21`
**Base:** `origin/main` = `0f41ebb` (157 file) · **Thời điểm kiểm:** `2026-10-01T14:40Z` → `14:44Z`
**Bằng chứng thô:** `agents/reviewer1/evidence/T21/` (`t21-A-procedure.txt`, `t21-B-fetch8.txt`, `t21-B2-quotes.txt`, `t21-B3-territory.txt`)

---

## 2.13 Bài kiểm #7A — T5 ForensicsMal @ `ee97c37` (kiểm QUY TRÌNH, không phải kết quả)

```text
[REVIEW] T21-A / ForensicsMal / Lớp 1 CROSS / KẾT QUẢ: PASS 5/6 — 1 LỖ HỔNG QUY TRÌNH + 1 SAI SỐ PHIÊN BẢN
```

| # | Câu hỏi Admin | Bằng chứng | Kết quả |
|---|---|---|---|
| Q1 | `FORENSICS_PROCEDURE.md` có đòi **hash TRƯỚC khi phân tích** cho **mọi** mẫu, hay chỉ nói chung? | `Bước 2` tiêu đề: *"Ghi SHA256 của **MỌI** mẫu **TRƯỚC** khi phân tích"* + khối lệnh ghi rõ *"# Bắt buộc, chạy ĐẦU TIÊN"*; khuôn `FORENSICS.md` §1 ghi *"Hash mẫu (BẮT BUỘC — tính TRƯỚC khi phân tích)"*; **checklist C1** có 5 ô, ô đầu: *"SHA256 của **mọi** mẫu đã ghi **TRƯỚC** khi phân tích?"* + ô *"Đã kiểm hash mẫu **không đổi** sau khi phân tích?"* + ô *"Mẫu nhiều tệp ⇒ đã hash **từng tệp** và **cả gói**?"* | **✅ ĐÒI THẬT, cho MỌI mẫu, có cổng checklist** |
| Q2 | Có đòi **công cụ + phiên bản + lệnh** cho mọi kết luận? Có cơ chế chống lỗi `pip list \| grep` lọc tay? | **Đòi: ✅** `Bước 3`: *"Mỗi khẳng định kỹ thuật phải kèm **bộ ba**… Kết luận không có bộ ba này ⇒ **không được** đưa vào báo cáo"*; C2 có 4 ô gồm *"Có kết luận nào dựa trên công cụ **đang thiếu** mà tôi suy diễn thay vì chạy? → **cấm**"*. **Cơ chế chống lọc tay: ❌ KHÔNG có đích danh** — `grep -niE "grep\|lọc\|KHONG LOC"` trên **cả 6 file T5** → **0 dòng khớp** | **✅ đòi công cụ/phiên bản/lệnh · ❌ thiếu cơ chế đích danh** |
| Q3 | Có mục **"kết luận vượt bằng chứng"** không? | Khuôn §7: *"❌ **CẤM attribution** ("có thể là APT", "do nhóm X"…) **khi không có bằng chứng attribution kỹ thuật trỏ tới**. Không có bằng chứng ⇒ **không nhắc tới**. ❌ CẤM kết luận vượt bằng chứng."*; khuôn §8 *"CHƯA XÁC MINH (bắt buộc có mục này)… Mục này **rỗng là dấu hiệu xấu**"*; **C3** có 4 ví dụ cấm cụ thể (APT · "AES-256" khi chưa thấy S-box · "kết nối tới C2" khi domain chỉ là chuỗi chết) | **✅ CÓ, rất cụ thể — không phải câu chữ chung** |
| Q4 | `EVIDENCE/tool_inventory_raw.txt` có phải output **thô** không? | Toàn văn 79 dòng: ghi **`Traceback (most recent call last)`** cho 4 lệnh import thất bại, ghi `ModuleNotFoundError` cho 6 gói, ghi `(khong co goi nao)` cho pip list, ghi `THIEU` cho 12 CLI. **Không giấu lỗi, không bịa thành công** | **✅ THÔ THẬT** |
| Q5 | `volatility3` tự hạ xuống "chưa thực chiến" là **thật hay chỉ câu chữ**? | `tooling_bootstrap_raw.txt`: `vol --help` → framework nạp ✅; `vol -f /dev/null windows.pslist` → **lỗi symbol**, và tác giả **tự dán nhãn** *"(khong co dump that -> loi symbol la DU KIEN)"*; ghi `volatility3: (khong co thuoc tinh __version__)`. Bảng năng lực §D đánh 🟡 *"công cụ sẵn sàng, **chưa thực chiến**"* + *"**CHƯA chạy trên dump thật**"*, **trong khi** PE ghi *"**đã parse PE thật**"*, YARA *"**đã compile + scan OK**"*, capstone *"**đã disasm x86-64**"* | **✅ TỰ HẠ THẬT, không phải câu chữ** — có phân biệt rõ "đã chạy" vs "chỉ nạp được" |
| Q6 | `scripts/bootstrap_tools.sh` có logic đúng không? | Đọc 58 dòng: `set -euo pipefail` ✅ · `VENV_DIR="${1:-$HOME/forensicsmal-tooling/.venv}"` ✅ (ngoài repo, không bị commit) · `export PATH="$HOME/.local/bin:$PATH"` ✅ (đúng chỗ `uv` nằm) · guard `command -v uv` → `exit 1` + báo Admin ✅ · `uv venv "$VENV_DIR" --python 3.12` ✅ khớp `python3 3.12.3` trên máy · `uv pip install --python "$VENV_DIR/bin/python" …` ✅ cài vào venv, **không** đụng hệ thống · verify bằng heredoc **trong venv** ✅ | **✅ LOGIC ĐÚNG.** Tôi **không chạy cài đặt thật** (Admin cấm) — chỉ đọc và đối chiếu với môi trường |

### 2.13.1 LỖ HỔNG QUY TRÌNH phát hiện được (Q2) — cần vá

ForensicsMal yêu cầu **công cụ + phiên bản + lệnh** cho mọi kết luận, và **cấm suy diễn khi thiếu
công cụ** — hai điều đó **đúng hướng**. Nhưng đây **chính là** lỗi mà ExploitDeep đã mắc ở T4:
dùng `pip list | grep -Ei '<danh sách viết tay>'` với **mẫu grep thiếu tên gói**, rồi kết luận "thiếu"
mà không hề `import` thử. Quy trình T5 **không có ô nào chặn đúng lỗi đó**:
**không** có chữ `grep`, **không** có chữ "lọc", **không** có "KHÔNG LỌC" trong cả 6 file T5.

**Hệ quả:** một người làm theo đúng T5 vẫn có thể lặp lại y nguyên lỗi `unicorn`.
**Đề xuất (Reviewer1 không tự sửa — `agents/<khác>/**` ngoài territory):** thêm thẳng vào **C2**
các ô sau, mô phỏng đúng bản vá ExploitDeep đã làm ở T16:
1. *"Mọi kiểm kê công cụ đã dùng `pip freeze`/`pip list` **KHÔNG LỌC** và lưu **nguyên output**?"*
2. *"Mỗi kết luận 'THIẾU' đã được chứng minh bằng `import <mod>` **trong ĐÚNG interpreter đang xét**,
   và đã ghi rõ interpreter đó là ai (hệ thống hay venv)?"*
3. *"Mỗi dòng bảng phiên bản đã ghi rõ số phiên bản lấy từ **metadata** hay **`__version__`**?"*

### 2.13.2 SAI SỐ PHIÊN BẢN `capstone` — khuyết điểm chính xác (đã kiểm bằng máy)

| Nơi ghi | Giá trị |
|---|---|
| `FORENSICS_PROCEDURE.md` d.94 và d.291 | `capstone` **5.0.9** |
| `CHECKIN.md` d.45, d.91, d.144 · `README.md` d.26 | `capstone` **5.0.9** |
| `EVIDENCE/tooling_bootstrap_raw.txt` **d.13** | `capstone         5.0.9` *(từ `pip list` = metadata)* |
| `EVIDENCE/tooling_bootstrap_raw.txt` **d.32** | `capstone      : **5.0.7**` *(từ `__version__`)* |
| `scripts/bootstrap_tools.sh` d.34-35 | in `__version__` ⇒ sẽ in **5.0.7** |

Đo lại trên máy: `capstone.__version__` = **5.0.7** · `importlib.metadata.version("capstone")` = **5.0.9**
⇒ **cả hai số đều thật.** Nhưng T5 **chọn 5.0.9** và ghi như thể đó là phiên bản đã dùng,
**không nói** đó là metadata. Trớ trêu: **chính ForensicsMal** sau này (T15) đã phát hiện và xử lý
đúng cặp này (*"metadata 5.0.9 vs `__version__` 5.0.7 — tôi KHÔNG tự phán quyết"*).
**Mức độ: thấp** (cả hai số thật, raw evidence chứa cả hai nên truy được) — nhưng đây là
**khuyết điểm chính xác trong bảng tự đánh giá năng lực**, đúng loại Admin đang hỏi.

> **Ghi nhận công bằng:** T5 là **quy trình**, không phải kết quả phân tích, và tác giả **tự ghi**
> *"⚠️ CHƯA CÓ MẪU — tài liệu này là quy trình + khuôn báo cáo, không phải kết quả điều tra"*.
> Không có chỗ nào tự nhận thành thạo quá mức; ngược lại còn **chủ động hạ** volatility3.

**Phán quyết T21-A:** **PASS 5/6** — quy trình đạt ở 5 câu hỏi; **Q2 thiếu cơ chế đích danh chống
lỗi lọc tay** (khuyến nghị vá, không reject) và **1 sai số phiên bản `capstone`** (mức thấp).

---

## 2.14 Bài kiểm #7B — T13 javis @ `3e19d46`

```text
[REVIEW] T21-B / javis / Lớp 1 CROSS / KẾT QUẢ: PASS nội dung — 0 vi phạm territory (12 mục đã kiểm)
                                              + 1 VI PHẠM D-001 do chính javis khai (clone bằng HTTPS)
```

### 2.14.1 Tự fetch lại 8 URL — **nhiều con số khớp BYTE-EXACT**

Tôi `curl -sSL -A "Chrome/125"` từng URL trên **máy này** (`noble-tran-XiaoXin-14-AHP9`,
**không phải** VM `/home/hatch` của javis):

| # | URL | javis khai | Tôi đo được | Kết quả |
|---|---|---|---|---|
| 1 | MDPI Sci `2413-4155/7/3/91` | curl 403 · 396 B | **403 · 398 B** | ✅ cùng trạng thái (lệch 2 B) |
| 2 | MDPI Entropy `1099-4300/27/12/1242` | curl 403 · 400 B | **403 · 402 B** | ✅ cùng trạng thái (lệch 2 B) |
| 3 | MDPI PDF `/91/pdf` | curl 403 · 404 B | **403 · 406 B** | ✅ cùng trạng thái (lệch 2 B) |
| 4 | ACM DL PDF | curl 000 · 0 B / fetch 403 | **403 · 5.728 B** | ✅ khớp trạng thái **fetch** (403) |
| 5 | **DergiPark `5763310`** | **200 · PDF 1.108.312 B** | **200 · `application/pdf` · 1.108.312 B** | ✅ **KHỚP BYTE-EXACT** |
| 6 | **`doi.org/10.62056/ahee0iuc`** | 200 · đích **`/p/1/2/6`** · **168.296 B** | 200 · đích **`https://cic.iacr.org/p/1/2/6`** · **168.296 B** | ✅ **KHỚP BYTE-EXACT + đích URL** |
| 7 | `datatracker…/draft-ietf-tls-hybrid-design/` | 200 · đích **`/doc/rfc9954/`** · 79.550 B | 200 · đích **`https://datatracker.ietf.org/doc/rfc9954/`** · **80.488 B** | ✅ đích URL khớp; size lệch 938 B (trang động) |
| 8 | **`ebpf.io/what-is-ebpf/`** | 200 · **340.219 B** | 200 · **340.219 B** | ✅ **KHỚP BYTE-EXACT** |

**Ba con số khớp byte-exact** (1.108.312 · 168.296 · 340.219) là bằng chứng rất mạnh: đây là
**số đo thật**, không thể đoán ra. Đặc biệt:
- **ebpf.io 340.219 B** ⇒ xác nhận javis đúng khi nói ResearchLead chỉ nhận **nội dung bị cắt**.
- **DergiPark 200 · 1.108.312 B** ⇒ xác nhận lỗi `HTTP 000` của ResearchLead là **do mạng**, và
  **tái lập được từ máy này**.
- **IACR `/p/1/2/6`** ⇒ xác nhận **đính chính hữu ích**: URL `/p/1/3/22` suy đoán trước đây là bài khác.

**Giới hạn tôi phải nói rõ:** hai nguồn MDPI (#1, #2) javis khai lấy **toàn văn qua "fetch nội dung
trang"**; tôi **không có trình duyệt** nên `curl` chỉ ra **403** ⇒ phần **nội dung** đó là
**`chưa xác minh`** bằng kênh của tôi, **không** phải bị bác bỏ. Con số `403` thì **khớp**.

### 2.14.2 Xác minh TRÍCH NGUYÊN VĂN — 23/23 câu khớp

Tôi bóc văn bản từ **chính file tôi tải** (`/tmp/t13_*.bin`) và đối chiếu từng câu, **không** dùng bản ghi của javis:

| Nguồn | Số câu kiểm | Kết quả | Ghi chú |
|---|---|---|---|
| `ebpf.io` | 3 | **✅ 3/3** | khớp nguyên văn trong HTML 340.219 B |
| IACR CiC (S7) | 4 | **✅ 4/4** | tiêu đề trang đích = *"A Comprehensive Survey on Post-Quantum TLS"* ✅ |
| RFC 9954 (X4) | 3 | **✅ 3/3** | `RFC 9954`×3 · `Informational`×3 · `Hybrid Key Exchange in TLS 1.3`×4 |
| DergiPark (S17) | 8 | **✅ 8/8** | gồm **cả 4 con số**: `11.3 to 13.3 ms`, `180 ms với 5% loss vs X25519 281 ms`, `4.16-fold speedup`; PDF 13 trang, có tác giả `Cemile İNCE` ✅ |
| MDPI S15 + S16 (qua **Crossref**) | 8 | **✅ 8/8** | Crossref trả abstract 1.905 và 2.075 ký tự; **cả 8 câu khớp**; title/venue/tác giả khớp |
| **Tổng** | **26 câu** (23 ngoài Crossref + 8 Crossref, có trùng) | **✅ 26/26** | **không câu nào bị viết lại hay cắt ghép** |

> **Một chi tiết nhỏ:** `SOURCES_BROWSER.md` ghi tác giả S15 là *"Chen Jinrong, Peng Wei, Wang Yi,
> Bian Yutong"* — Crossref trả `Jinrong Chen, Wei Peng, Yi Wang, Yutong Bian`. Đây là **thứ tự
> họ–tên kiểu Trung Quốc**, không phải sai tên. Mức độ: **không đáng kể**.

### 2.14.3 KIỂM VIPHAM TERRITORY — **đã kiểm 12 mục, KHÔNG phát hiện vi phạm territory**

Dùng `merge-base` (không dùng `git diff main` — cách đó sẽ báo oan hàng loạt file `D` do T13 tách
từ commit cũ). `merge-base origin/main 3e19d46` = **`1917c7b`**; `main` đi trước **40 commit**.

| # | Mục kiểm | Bằng chứng thô | Kết quả |
|---|---|---|---|
| T1 | merge-base chuẩn để biết javis **thực sự** đổi gì | `git merge-base` → `1917c7b`; `git rev-list --count` → **40** | ✅ |
| T2 | **File javis thực sự thay đổi** | `git diff --name-status 1917c7b 3e19d46` → **đúng 4 file**: `agents/javis/README.md`, `agents/javis/tasks/T13/NOTES.md`, `research/ebpf-microsegmentation/SOURCES_BROWSER.md`, `research/pqc-tls-migration/SOURCES_BROWSER.md` — **tất cả nằm trong territory** `research/**/SOURCES_BROWSER.md` + `agents/javis/**` | ✅ **KHÔNG có file ngoài territory** |
| T3 | Commit có bất thường không | 1 commit `3e19d46`; `author=javis <tranquy4869@gmail.com>` = `committer=javis` | ✅ |
| T4 | Có đường dẫn tuyệt đối **máy khác** trong nội dung/bằng chứng không | `git grep -n '/home/hatch' 3e19d46` → **6 dòng, tất cả là VĂN BẢN MÔ TẢ MÔI TRƯỜNG** (3 dòng trong `ADMIN/**` do **Admin** viết; 3 dòng trong header file của javis **tự khai** môi trường). **Không** có `/home/hatch/...` nào lọt vào output lệnh, log, hay đường dẫn bằng chứng | ✅ |
| T5 | Có file nhị phân / mẫu / dump trên nhánh không | quét `*.pdf|*.bin|*.pcap|*.exe|*.zip|*.png…` trên toàn bộ `git ls-tree -r 3e19d46` → **0 file** | ✅ javis **không** push HTML/PDF tải về |
| T6 | javis có sửa `.gitignore` (ngoài territory) không | `git diff 1917c7b 3e19d46 -- .gitignore` → **rỗng** | ✅ **KHÔNG sửa** |
| T7 | Nguyên văn quy định Admin viện dẫn | `ADMIN/ROSTER.md:70` — *"Nếu **không clone được** repo về VM đó thì phải báo Admin — **cấm ghi tạm sang máy khác**."* | ✅ đã trích được nguyên văn |
| T8 | Điều kiện kích hoạt quy định đó có xảy ra không | javis **clone được** (`~/workspace/agentmeeting` trên VM mình) ⇒ **điều kiện "nếu không clone được" KHÔNG xảy ra** ⇒ **không vi phạm** quy định này | ✅ |
| T9 | Bằng chứng thô có bị push lên repo không | `NOTES.md:28` khai lưu **ngoài repo** tại `~/.agentmeet/sessions/…/javis/T13-evidence/` | ✅ **không push lên repo** |
| T10 | Có dấu hiệu rebase/cherry-pick làm lệch nguồn gốc | `author_date == commit_date` = `2026-10-01 21:03:42 +0700` | ✅ |
| T11 | Bằng chứng thô có trên **máy này** không | `ls ~/.agentmeet/sessions/ab1-478d-cfa7/javis/` → **`No such file or directory`** ⇒ chứng cứ **thực sự ở máy khác**, không được nhập lậu sang máy này | ✅ **phù hợp khai báo** |
| T12 | Tổng: có file nào ngoài 4 file territory không | `git diff --name-status` chỉ 4 dòng `A`, **0 dòng `D`/`M` ngoài territory** | ✅ **0 vi phạm territory** |

**Kết luận territory:** **đã kiểm 12 mục (T1–T12), KHÔNG phát hiện vi phạm territory.**
Cụ thể: (a) **không** lấy file từ máy khác nhập vào repo; (b) **không** ghi tạm sang máy khác
(quy định chỉ kích hoạt khi clone thất bại — ở đây clone thành công); (c) **không** push mẫu/nhị phân;
(d) **không** sửa file ngoài 4 file thuộc territory.

### 2.14.4 ⚠️ VI PHẠM D-001 — javis **tự khai** clone bằng HTTPS

`agents/javis/tasks/T13/NOTES.md:4` ghi nguyên văn:
> *"**Clone:** `~/workspace/agentmeeting` trên VM của javis (**clone bằng HTTPS** — đã xác minh đủ khung D-001: …)"*

Trong khi `rooms/ab1-478d-cfa7/directives.md` D-001 ghi:
> *"Toàn đội: clone **BẰNG SSH**, **TUYỆT ĐỐI KHÔNG dùng HTTPS**."*

⇒ Đây là **vi phạm chỉ thị có hiệu lực bắt buộc**, do chính tác giả **khai báo thẳng** (không giấu —
đó là điểm cộng về trung thực). **Lý do khả dĩ:** VM `/home/hatch` có thể **chưa có SSH key** cho
`github.com`, mà D-001 cũng **không** có nhánh xử lý "nếu VM không có SSH key thì…".
**Hệ quả thực tế: không thấy** — clone đủ khung, không push sai, không lộ credential (tôi đã quét
`reviews/`+artifact, không có token).
**Đề xuất cho Admin:** (1) xác nhận đây là vi phạm; (2) **bổ sung nhánh ngoại lệ vào D-001**
("VM không có SSH key ⇒ báo Admin, dùng HTTPS chỉ để **đọc**, cấm push qua HTTPS"); (3) **không**
trừ điểm nội dung T13 vì vi phạm này không ảnh hưởng kết quả truy hồi.

**Phán quyết T21-B:** **PASS nội dung** — 3/8 URL khớp **byte-exact**, 26/26 câu trích nguyên văn
khớp, 0 vi phạm territory (**12 mục đã kiểm**). **1 vi phạm D-001** (clone HTTPS) do tác giả tự khai,
không gây hệ quả, chờ Admin phân xử. **`chưa xác minh`:** nội dung toàn văn 2 bài MDPI (kênh trình
duyệt tôi không có) và chính file bằng chứng thô của javis (ở máy khác, không nằm trên máy này).

---

# VÒNG 5 — Bài kiểm #8 (T25): T22 DocWriter — `INDEX.md` theo mốc `main` 157 file

**Người kiểm:** Reviewer1 (`ag_76306ba6`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/reviewer-1/T25`
**Base:** `origin/main` = `e8c45a0` (166 file) · **Mốc kiểm:** `0f41ebb` (157 file) · **Artifact:** `INDEX.md` @ `38cf43d`
**Bằng chứng thô:** `agents/reviewer1/evidence/T25/`

```text
[REVIEW] T25 / DocWriter (ag_da78519d) / Lớp 1 CROSS / KẾT QUẢ: PASS 18/18 mục + 1 PHÁT HIỆN BỔ SUNG
```

---

## 2.15 Kết quả từng mục Admin yêu cầu

| # | Mục kiểm | Lệnh đã chạy lại | Output thô | Kết quả |
|---|---|---|---|---|
| 1 | **Tự đếm 157 file @ `0f41ebb`** | `git ls-tree -r --name-only 0f41ebb \| wc -l` | **`157`** | **✅ ĐÚNG 157** |
| 1b | Nhánh T22 có **158** file (như DocWriter cảnh báo)? | `git ls-tree -r --name-only 38cf43d \| wc -l` (và `cfb6b8b`) | **`158`** cả hai | **✅ CẢNH BÁO ĐÚNG** |
| 1c | **Việc sửa ở `38cf43d` có THẬT không?** | `git diff cfb6b8b 38cf43d` · `git show --stat 38cf43d` | `INDEX.md \| 44 ++--` + `agents/docwriter/tasks/T22/README.md \| 25 ++--`; diff cho thấy **`git ls-files \| wc -l` → `M=0f41ebb` + `git ls-tree -r --name-only $M \| wc -l`**, kèm khối cảnh báo mới *"Nếu bạn đang ở nhánh `agent/doc-writer/T22`, `git ls-files` sẽ ra **158** chứ không phải 157… Vì vậy **các lệnh dưới đây trỏ vào mốc `0f41ebb`**"* | **✅ SỬA THẬT, đúng gốc lỗi** |
| 2 | Bảng §2 (157 dòng) khớp **157/157** đường dẫn | `awk '/^## 2\. Bảng/{f=1} /^### 2\.1/{f=0} f' INDEX.md \| grep -c '^\| [0-9]'` → **157**; rồi `sed` lấy path → `sort` → `diff` với `git ls-tree … $M \| sort` | **`diff` RỖNG** — 157 dòng bảng vs 157 file | **✅ KHỚP 157/157** |
| 2b | Số lượng theo loại (DocWriter tự khai trong §7) | `grep -c` từng mẫu trên `0f41ebb` | `.md`=**71** ✅ · `.txt`=**45** ✅ · `.gitkeep`=**13** ✅ · `.py`=**10** ✅ · `.json`=**7** ✅ · `.sh`=**2** ✅ · số thư mục=**52** ✅ | **✅ 7/7 con số khớp** |
| 3 | **Tác giả lấy từ commit THÊM FILE LẦN ĐẦU**, 157/157 truy được, 0 `chưa xác minh` | `for f in $(git ls-tree -r --name-only $M); do git log --diff-filter=A --format='%an' -- "$f" \| tail -1; done \| sort \| uniq -c` | **Admin AgentMeet 32 · BountyRecon 30 · Reviewer1 28 · ResearchLead 20 · ForensicsMal 18 · ExploitDeep 17 · DocWriter 7 · Auditor2 5** (tổng **157**); số file **không truy được tác giả = 0** | **✅ KHỚP §3.1 TỪNG NHÓM + 0 `chưa xác minh`** |
| 3d | **Kiểm mẫu cột "Tác giả"** trong bảng §2 (Admin yêu cầu) | chọn 3 file mẫu mỗi nhóm × 8 nhóm, so cột bảng với `git log --diff-filter=A` | **21/21 mẫu khớp tuyệt đối** (Admin AgentMeet · BountyRecon · Reviewer1 · ResearchLead · ForensicsMal · ExploitDeep · DocWriter) | **✅ 21/21** |
| 4a | Mục Admin vá 1: **chốt ngày `2026-10-01`** | `grep -n "2026-10-01"` và `grep -c "2025-10-01"` | d.4 ghi *"**Ngày lập bản này:** 2026-10-01 — **Admin đã chốt mốc ngày**… xem phán quyết DISSENT-4"*; **`2025-10-01` = 0 lần** | **✅ CÒN NGUYÊN** |
| 4b | Mục Admin vá 2: **ghi rõ bản gốc Admin ở `abe0c3e` + DocWriter tiếp quản** | `grep -n "abe0c3e"` / `grep -n "tiếp quản"` | d.5: *"**Bản gốc do Admin viết** ở `abe0c3e`, DocWriter **tiếp quản và viết lại toàn bộ** ở T1 (phán quyết DISSENT-2). Bản này là lần viết lại **thứ hai**, ở T22"* | **✅ CÒN NGUYÊN** |
| 4c | Mục Admin vá 3: **cảnh báo phạm vi** | `grep -n -i "cảnh báo phạm vi\|mốc"` | d.12 khối *"⚠️ **CẢNH BÁO PHẠM VI (cập nhật ở T22)**"* + §5 riêng + d.219 *"Bảng phản ánh **mốc `0f41ebb`**. `main` đang tiến; bảng sẽ lạc hậu ngay sau khi có commit mới"* | **✅ CÒN NGUYÊN** |
| 5 | **Bảng liên tục** (không dòng trống cắt giữa) | `awk '/^\|/{n++;next} n>0 && !/^\|/ && !/^$/{print "BANG BI CAT"}'` | **không in gì** ✅; số thứ tự `1 → 157`, **liên tục = True**, **thiếu số = (không)**, **trùng số = (không)** | **✅ LIÊN TỤC** |
| 5b | **Link chết = 0?** | regex link markdown trong `INDEX.md` → đối chiếu cả **file** *và* **thư mục** @ `0f41ebb` | 1 link tương đối, trỏ `agents/docwriter/tasks/T1/` — **thư mục TỒN TẠI** (chứa 2 file) | **✅ 0 LINK CHẾT** |

> **Tự khai lỗi của tôi ở mục 5b:** phiên bản đầu của bộ kiểm link **báo oan** `agents/docwriter/tasks/T1/`
> là "link chết", vì tôi chỉ đối chiếu với **danh sách FILE** (`git ls-tree -r` chỉ liệt kê file).
> Tôi đã sửa để đối chiếu **cả thư mục** rồi chạy lại. Ghi lại để việc sửa sai kiểm chứng được.

---

## 2.16 Kiểm 4 phát hiện của DocWriter — **cả 4 đều ĐÚNG**

| # | Phát hiện của DocWriter | Tôi xác minh độc lập | Kết quả |
|---|---|---|---|
| **6a** | `ADMIN/SUMMARY.md` d.46+d.51 dẫn **3 đường dẫn T5 không tồn tại** | @ `0f41ebb`: 3 path `agents/forensicsmal/T5/{FORENSICS_PROCEDURE.md, scripts/bootstrap_tools.sh, EVIDENCE/tooling_bootstrap_raw.txt}` → **cả 3 KHÔNG TỒN TẠI** (`git ls-tree -r 0f41ebb \| grep -qx`). **Đọc nguyên văn §1**: bảng nghiệm thu chỉ có **T1, T3, T15, T16, T19, T11, T17, T20** — **T5 chưa merge** | **✅ PHÁT HIỆN ĐÚNG** |
| **6b** | 3 link **sai độ sâu** trong `CANDIDATES.md` d.27/39/50 | File ở `agents/bountyrecon/tasks/T3/`; `../../../security/github/RECON.md` → `posixpath.normpath` = **`agents/security/github/RECON.md`** ❌ không tồn tại. Cần **4** cấp: `../../../../security/github/RECON.md` → `security/github/RECON.md` ✅ **có thật** `@0f41ebb` | **✅ PHÁT HIỆN ĐÚNG** (cần 4 cấp `../`, không phải 3) |
| **6c** | 3 link **thiếu scheme** trong `scope_github.md` | regex link thiếu scheme → **đúng 3**: `[`lgtm-com.pentesting.semmle.net`](lgtm-com.pentesting.semmle.net)`, `[…appspot.com](…)`, `[downloads.lgtm.com](downloads.lgtm.com)` | **✅ ĐÚNG ĐỦ 3** |
| **6d** | **16 file** `[T2]`/`[T4]` đã ở `main` nhưng T2/T4 **không** trong danh sách nghiệm thu, `ASSIGNMENTS` vẫn `⏳ todo`/`⏸ chờ T3` | `for f in …; do git log -1 --format=%s -- "$f"; done` → **`[T2]` = 11 file** ✅ (DocWriter khai 11), **`[T4]` = 5 file** ✅ (khai 5). Nguyên văn `SUMMARY.md` §1 bảng nghiệm thu **không có T2, T4** ✅. Nguyên văn `ASSIGNMENTS.md`: `\| T2 \| … \| ⏳ todo \|` và `\| T4 \| … \| ⏸ chờ T3 \|` ✅ | **✅ PHÁT HIỆN ĐÚNG (11+5=16)** |
| **6e** | §4.5 còn thiếu `reviews/VERIFY2.md`, `agents/deepseek-harness/**`, `agents/forensicsmal/T5/**` | đếm trên `0f41ebb`: **0 / 0 / 0** file | **✅ CẢ 3 THIẾU THẬT** |

**Admin đã sửa 6a và 6d tại `e8c45a0` — và sửa ĐÚNG, không "sửa cho xong":** d.46/d.51 nay ghi
*"⚠️ **T5 CHƯA MERGE** ⇒ đường dẫn chưa kiểm chứng được từ `main`"* — **tôi xác nhận T5 vẫn chưa merge**
(`ee97c37` **không** là tổ tiên của `origin/main`), nên câu đó **đúng sự thật**, không phải câu chữ né tránh.
`ASSIGNMENTS.md` T2 → `✅ merged qua T19 (932074f)`, T4 → `✅ merged qua T16 (2620932)` ✅.

> **Tự khai lỗi của tôi ở mục 6d:** lần đếm đầu tôi dùng regex thô `grep -oE "T[0-9]+"` trên cả §1 và
> **tưởng** T2 có trong danh sách nghiệm thu. Đọc **nguyên văn bảng** mới thấy **T2 và T4 đều vắng mặt**
> ⇒ DocWriter đúng, regex của tôi sai. Tôi ghi lại cả hai bước để không ai nhầm là tôi hạ bệ tác giả.

---

## 2.17 PHÁT HIỆN BỔ SUNG của Reviewer1 — `SUMMARY.md` @ `e8c45a0` vẫn lạc hậu

**Không thuộc 6 mục Admin yêu cầu, nhưng cùng lớp lỗi với §4.1 mà DocWriter đã tìm ra.**

`ADMIN/SUMMARY.md` §1 @ `e8c45a0` (main hiện tại) **vẫn ghi**:
> *"**`main` nay có 157 file. Chưa merge:** T5 (ForensicsMal), T8 (DeepSeek-Harness), **T13 (javis)**"*

Nhưng đo lại: **`git ls-tree -r --name-only e8c45a0 | wc -l` = 166** (không phải 157),
và **`37a39ff` (merge T13) ĐÃ là tổ tiên của `origin/main`** ⇒ **T13 đã merge**, không còn "chưa merge".

| Khẳng định trong SUMMARY @ `e8c45a0` | Thực tế tôi đo | |
|---|---|---|
| "`main` nay có **157 file**" | **166 file** | ❌ lạc hậu 9 file |
| "Chưa merge: T5" | `ee97c37` không là tổ tiên ⇒ **đúng** | ✅ |
| "Chưa merge: T8" | `5ccb731` không là tổ tiên ⇒ **đúng** | ✅ |
| "Chưa merge: **T13** (javis)" | `37a39ff` **đã** là tổ tiên ⇒ **SAI** | ❌ lạc hậu |

**Đề xuất cho Admin** (Reviewer1 **không tự sửa** — `ADMIN/**` ngoài territory): cập nhật 2 chỗ này,
hoặc thêm ghi chú mốc "(số liệu tại `0f41ebb`)" để dòng đó tự khai mốc của nó.
**Đây không phải lỗi của DocWriter** — `SUMMARY.md` là file của Admin, DocWriter **không** sửa và
đã **báo đúng** vấn đề cùng loại ở §4.1.

---

## 2.18 Đã kiểm những mục nào (vòng 5)

**T25: đã kiểm 18 mục** — 1 · 1b · 1c · 2 · 2b · 3 · 3d · 4a · 4b · 4c · 5 · 5b · 6a · 6b · 6c · 6d · 6e · 7.

- **✅ PASS (18/18):** 157 file đúng · cảnh báo 158 đúng · việc sửa `38cf43d` thật · **bảng 157/157 khớp `diff` rỗng** ·
  7/7 con số theo loại khớp · **tác giả 157/157 truy được, 0 `chưa xác minh`** · **21/21 mẫu cột tác giả khớp** ·
  3 mục Admin vá còn nguyên · bảng liên tục `1→157` · **0 link chết** · **4/4 phát hiện của DocWriter đúng**.
- **⚠️ 1 phát hiện bổ sung:** `SUMMARY.md` @ `e8c45a0` còn lạc hậu (157 → **166**; T13 đã merge nhưng vẫn ghi "chưa merge").
- **`chưa xác minh`: 0 mục.**
- **Tự khai 2 lỗi của chính tôi** (bộ kiểm link chỉ so file; regex thô đếm task) — đã sửa và ghi lại cả hai bước.

> **Phán quyết T25: PASS 18/18.** Bảng `INDEX.md` của DocWriter **khớp máy từng đường dẫn**, tác giả
> lấy đúng từ `--diff-filter=A`, cảnh báo phạm vi đầy đủ, và **4 phát hiện đều đúng** — trong đó 2 phát hiện
> (6a, 6d) đã khiến Admin sửa `SUMMARY.md`/`ASSIGNMENTS.md`. **Không reject mục nào.**

---

# VÒNG 6 — Bài kiểm #9 (T27): T23 ForensicsMal + T26 BountyRecon

**Người kiểm:** Reviewer1 (`ag_76306ba6`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/reviewer-1/T27`
**Base:** `origin/main` = `d3c874e` (187 file) · **Artifact:** T23 @ `ee90d1f` · T26 @ `43cc537`
**Bằng chứng thô:** `agents/reviewer1/evidence/T27/`
**Phương pháp an toàn:** dùng `git worktree add --detach /tmp/rv1-t23 ee90d1f` (**index riêng**) thay vì
`git --work-tree=… checkout … -- .` — đúng bài học tôi tự khai ở T25.

---

## 2.19 Bài kiểm #9A — T23 ForensicsMal (@ `ee90d1f`, rẽ từ T5)

```text
[REVIEW] T27-A / ForensicsMal (ag_82f7cb07) / Lớp 1 CROSS / KẾT QUẢ: PASS 4/4
```

### 2.19.1 A1 — Ba ô C2 mới: **có thật và HÀNH ĐỘNG ĐƯỢC**

Đọc **nguyên văn** §C2 (`FORENSICS_PROCEDURE.md`), dưới khối dẫn *"**C2 — BA Ô CHỐNG 'LỌC TAY'**
(bổ sung ở T23, thi hành D-014 mục 1)… **Đây là ô bắt buộc, không phải gợi ý.**"*:

| Ô | Nguyên văn (rút) | Có hành động được? |
|---|---|---|
| **C2a** | *"Kiểm kê công cụ đã dùng `pip freeze`/`pip list` **KHÔNG LỌC**, và lưu **nguyên output** vào `EVIDENCE/`? *(Không `grep`, không `--format` rút gọn, không cắt dòng, không "chỉ liệt kê gói liên quan".)*"* — kèm lệnh thay thế vì máy không có `pip`: `~/.local/bin/uv pip list --python <interpreter>` | ✅ **Đúng, cụ thể, có lệnh chạy được** |
| **C2b** | *"Mỗi kết luận **"THIẾU"** đã được chứng minh bằng `import <mod>` thực chạy trong **ĐÚNG interpreter đang xét**, và **đã ghi rõ đường dẫn interpreter đó**?"* + *"Ghi cả **thông báo lỗi nguyên văn**"* + **"'Không thấy tên trong danh sách' **KHÔNG** phải bằng chứng thiếu. **Chỉ `import` thất bại mới là.**"* | ✅ **Bịt đúng lỗ hổng đã làm ExploitDeep sai** |
| **C2c** | *"Mỗi dòng **phiên bản** đã ghi rõ lấy từ **metadata** hay **`__version__`**?… Ghi `"X"` trần là **thiếu nguồn**. Mẫu ghi đúng: `capstone` **5.0.9 (metadata)** / **5.0.7 (`__version__`)**"* | ✅ **Có mẫu cụ thể** |

Thêm **câu tự vấn** kèm điều kiện chặn: *"Tôi đã `import` nó chưa, trong đúng interpreter này chưa,
và tôi có đang lọc danh sách theo thứ tôi đã tin sẵn không?" — Trả lời chưa đủ ba vế thì **không được**
viết chữ "thiếu".*

⇒ **Ba ô này thi hành ĐÚNG khuyến nghị của tôi ở T21-A Q2.** Ghi nhận: tác giả còn **tốt hơn** đề xuất —
tôi đề xuất 3 ô, họ thêm cả **lý do tồn tại** (dẫn chứng lỗi T4) và **câu tự vấn**.

### 2.19.2 A2 — `capstone`: **mọi dòng trong TÀI LIỆU đã ghi rõ nguồn**

| Nơi | Nguyên văn | |
|---|---|---|
| `FORENSICS_PROCEDURE.md` d.110 | `capstone` **5.0.9 (metadata)** / **5.0.7 (`__version__`)** | ✅ |
| `FORENSICS_PROCEDURE.md` d.114-118 | khối *"⚠️ **Vì sao `capstone` ghi HAI số**… **cả hai đều thật, cùng một gói, và khác nhau**"* + trỏ bằng chứng thô | ✅ |
| `FORENSICS_PROCEDURE.md` d.289 (mẫu C2c) · d.340 (bảng năng lực) | đều ghi hai số + nguồn | ✅ |
| `CHECKIN.md` d.46 · d.95 · d.148 | đều ghi hai số + nguồn | ✅ |
| `README.md` d.26 | đều ghi hai số + nguồn | ✅ |

**Còn dòng nào ghi số trần thiếu nguồn không?** `git grep capstone` rồi lọc bỏ `metadata|__version__`
→ các dòng còn lại **đều KHÔNG phải câu khẳng định phiên bản**: chúng là (a) **output thô**
(`t23_c2_gap_demo_raw.txt:13`, `t23_capstone_version_recheck_raw.txt:24`, `t23_unfiltered_inventory_raw.txt:7`
— bản `uv pip list` **cấm sửa**), hoặc (b) **dòng chú thích đã ghi rõ nguồn ngay cạnh**
(`t23_capstone_version_recheck_raw.txt:41`: *"dong 13: 'capstone 5.0.9' <- lay tu 'uv pip list' = **METADATA**"*),
hoặc (c) **tên gói trong lệnh cài** (`bootstrap_tools.sh:27/29`).
⇒ **0 dòng khẳng định phiên bản thiếu nguồn trong tài liệu.** ✅

### 2.19.3 A3 — TÁI LẬP demo: **khẳng định ĐÚNG, tái lập chính xác**

Tôi chạy lại `scripts/t23_c2_gap_demo.py` trong worktree riêng. Kết quả **khớp từng dòng**:

```text
  goi/module        grep co neo    import   ket luan
  yara                    thieu        OK   GREP SAI  <-- C2(a)/(b) BAT DUOC
  msoffcrypto             thieu        OK   GREP SAI  <-- C2(a)/(b) BAT DUOC
  unicorn                 thieu  that bai   nhat quan
  dissect                 thieu  that bai   nhat quan
  pyelftools              thieu  that bai   nhat quan
  So ket luan SAI neu chi dung grep : 2  ['yara', 'msoffcrypto']
```

**Cơ chế họ nêu là ĐÚNG:** `uv pip list` liệt kê **TÊN GÓI** (`yara-python`, `msoffcrypto-tool`),
còn `import` dùng **TÊN MODULE** (`yara`, `msoffcrypto`) ⇒ grep theo tên module **không thấy**
⇒ kết luận "thiếu" **SAI**. Và họ **phân biệt được** ca thật-thiếu (`unicorn` grep thiếu **và** import
thất bại = nhất quán) khỏi ca grep-sai ⇒ demo **không** nguỵ biện.

**Tái lập ổn định:** chạy lại sinh `t23_unfiltered_inventory_raw.txt` **giống hệt** bản đã commit
(`diff` rỗng) ✅.

### 2.19.4 A3b — Việc tác giả **TỰ GIỚI HẠN** là **ĐÚNG**, và tôi **xác nhận được bằng bản gốc T4**

Tác giả tự ghi:
> *"!! GIOI HAN KHANG DINH: đây là MỘT cơ chế THẬT của lớp lỗi 'lọc tay' và tôi TÁI HIỆN được nó.
> Tôi **KHÔNG** khẳng định đây là cơ chế cụ thể đã làm T4 kết luận sai về `unicorn` — tôi **CHƯA đọc bản gốc T4**."*

**Tôi ĐÃ đọc bản gốc T4 ở T9**, nên xác nhận được:

| | |
|---|---|
| Mẫu grep gốc của T4 (`2cbe90a:…/tool_inventory_raw.txt` dòng 113) | `… \| grep -Ei 'pwntools\|pycryptodome\|sympy\|z3\|capstone\|lief\|ropgadget\|ropper\|flask\|requests\|pip '` |
| `unicorn` có trong mẫu đó không? | **0 lần** — **thiếu hẳn** |
| Tên gói vs tên module của `unicorn` | **GIONG nhau** (`unicorn` / `unicorn`) ⇒ **không** phải ca của demo |

⇒ **T4 sai vì mẫu grep viết tay THIẾU HẲN chữ `unicorn`**, không phải vì gói-tên khác module-tên.
⇒ **Việc tự giới hạn của tác giả là ĐÚNG và cần thiết**: cơ chế họ demo là **một cơ chế thật khác**
trong **cùng lớp lỗi**, chứ không phải nguyên nhân của sự cố `unicorn`.
**Đây là hành vi đúng mực nhất của T23** — họ từ chối nhận công cho một kết luận họ không chứng minh được.

### 2.19.5 A4 — Bằng chứng thô **KHÔNG bị sửa**

| File | Blob `ee97c37` (T5 gốc) | Blob `ee90d1f` (T23) | |
|---|---|---|---|
| `T5/EVIDENCE/tooling_bootstrap_raw.txt` | `35da98a5d13651ac2099a12ca2403ee521065dbe` | `35da98a5d13651ac2099a12ca2403ee521065dbe` | **✅ GIỐNG HỆT** |

Các file T5 **có** đổi ở T23 — `CHECKIN.md`, `FORENSICS_PROCEDURE.md`, `README.md` — **đều là TÀI LIỆU**,
không phải bằng chứng thô ✅. Đúng D-004.

**Phán quyết T27-A: PASS 4/4.** Ba ô C2 có thật và hành động được · `capstone` ghi rõ nguồn ở mọi tài liệu ·
**demo tái lập chính xác và cơ chế đúng** · **tự giới hạn ĐÚNG (tôi xác nhận bằng bản gốc T4)** ·
**bằng chứng thô không bị chạm**.

---

## 2.20 Bài kiểm #9B — T26 BountyRecon (@ `43cc537`)

```text
[REVIEW] T27-B / BountyRecon (ag_579fc4fa) / Lớp 1 CROSS / KẾT QUẢ: PASS — và 2 phát hiện của họ ĐÚNG
         (1 phát hiện trúng vào chính T14 của tôi)
```

Dùng **`merge-base`** theo bài học `LOG` #64: `git merge-base origin/main 43cc537` = **`e8c45a0`**.
⇒ BountyRecon thực sự đổi **10 file thêm + 1 file sửa** (`T3/CANDIDATES.md`) — **tất cả trong territory** ✅.

### 2.20.1 B1 — 3 link sai độ sâu: **ĐÃ SỬA**

| Dòng | Nguyên văn @ `43cc537` | `normpath` | |
|---|---|---|---|
| 27 | `](../../../../security/github/RECON.md)` | `security/github/RECON.md` | ✅ **TỒN TẠI** |
| 39 | `](../../../../security/gitlab/RECON.md)` | `security/gitlab/RECON.md` | ✅ **TỒN TẠI** |
| 50 | `](../../../../security/cloudflare/RECON.md)` | `security/cloudflare/RECON.md` | ✅ **TỒN TẠI** |

**Quét toàn territory:** sau khi loại **code fence**, **inline code**, và 3 file không phải văn xuôi
(`scan_links.py` chứa regex; `scope_github.md` + `forbidden_file_untouched.txt` là **trích nguyên văn**
Admin cấm sửa) → **0 link sai thật sự**. Đồng thời tôi kiểm **link thật** trong
`security/{github,gitlab,cloudflare}/RECON.md`: **7/7 `](SCOPE.md)` và `](../github/RECON.md)` đều resolve** ✅.

> **Tự khai lỗi thứ 4 của tôi:** bản quét đầu báo **22 "link sai"**, bản thứ hai còn **7** — **tất cả là
> báo động giả của bộ quét của tôi** (regex trong code, mô tả link trong `LINKSCAN.md` nằm trong khối
> ```text, và tên miền trần trong trích nguyên văn). Đây **đúng y GAP-3 mà BountyRecon đã cảnh báo**.

### 2.20.2 B2 — Lệnh **CẤM SỬA** `scope_github.md`: **ĐƯỢC TÔN TRỌNG TUYỆT ĐỐI**

| Revision | Blob hash của `agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md` |
|---|---|
| `03d304b` (T3 gốc) | `15c946ff956a3fdb466f7f9768081af29b812088` |
| `e8c45a0` (merge-base) | `15c946ff956a3fdb466f7f9768081af29b812088` |
| `43cc537` (T26) | `15c946ff956a3fdb466f7f9768081af29b812088` |

**GIỐNG HỆT cả ba** ✅. Và `git log --oneline --all -- <file>` → **chỉ một commit duy nhất**
(`71f0bf8`, chính là T3 gốc). ⇒ **File chưa từng bị chạm.** 3 link thiếu scheme tại dòng 185
**còn nguyên đúng 3** ✅ — đúng `LOG` #54.

### 2.20.3 B3 — Đánh giá `SCOPEGAP.md`: **2 phát hiện ĐÚNG, 1 trong đó trúng chính tôi**

**GAP-0 — "T14 PASS T3 nhưng chỉ kiểm nội dung `SCOPE.md`, không kiểm link": ĐÚNG.** ✅
Tôi **tự kiểm chính mình**: `git show 85ea56f:reviews/CROSS.md`, mục T14 (`## 2.8`) — số lần xuất hiện
`CANDIDATES.md` = **0**. Tôi đã kiểm policy byte-exact, 20/20 câu trích, 4 xung đột scope, Atom,
Cloudflare/D-013 — **nhưng không kiểm link tương đối**. ⇒ **Khoảng trống này là THẬT và nằm ở T14 của tôi.**

**Số liệu GAP-0 (24 file · 10 link · 3 chết · 30%) — TÔI TÁI LẬP ĐƯỢC CHÍNH XÁC:**

| Cách lọc | file | link | chết |
|---|---|---|---|
| Tất cả file territory (`.md`+`.txt`) | 33 | 13 | 6 |
| Bỏ `.html`/`.json` | **24** ✅ | 13 | 6 |
| **Bỏ MỌI file trong `EVIDENCE/`** | 10 | **10** ✅ | **3** ✅ (= **30 %** ✅) |

⇒ BountyRecon dùng tập **AUTHORED** (không tính file CAPTURE) — **đúng như GAP-3 mô tả**.
**Con số của họ CHÍNH XÁC.** *(Lần đầu tôi đo bằng bộ lọc thô và ra 33/13/6, suýt kết luận sai là họ
tính nhầm; đây là **lần thứ 4** tôi phải sửa công cụ của chính mình trước khi báo cáo.)*

**GAP-1 — `LOG` #54 / D-020 §2 trỏ vào đường dẫn KHÔNG TỒN TẠI: ĐÚNG.** ✅
Nguyên văn `ADMIN/LOG.md:61` (#54): *"**KHÔNG sửa** 3 link thiếu `https://` trong
`security/github/EVIDENCE/scope_github.md` dòng 185"*.
Kiểm: `security/github/EVIDENCE/scope_github.md` → **0 file = KHÔNG TỒN TẠI** ❌;
`agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md` → **1 file = TỒN TẠI** ✅.
Và họ **đánh giá công bằng**: nội dung chỉ thị **đúng cả ba** (dòng 185 ✅ · đúng 3 link ✅ · giữ nguyên ✅),
**chỉ sai đường dẫn**. *(Lưu ý: trong lệnh giao T27 cho tôi, Admin đã ghi **đúng** đường dẫn —
nhưng `LOG.md` #54 trên `main` **vẫn còn** đường dẫn sai.)*

**GAP-2 — nguyên nhân gốc: §3 territory ⟂ §5 vị trí bằng chứng: ĐÚNG.** ✅
`git ls-tree -r --name-only origin/main | grep -c '^security/.*EVIDENCE/'` = **0**.
⇒ **Mọi chỉ thị trỏ `security/<program>/EVIDENCE/…` chắc chắn là đường dẫn chết** — GAP-1 **không phải
lỗi đánh máy**. Họ cũng đã tự báo mâu thuẫn này từ T3 (`CANDIDATES.md:115`), không phải mới phát hiện.

**GAP-3 — bộ kiểm link ngây thơ đẻ báo động giả:** ✅ **tôi vừa chứng minh bằng chính mình** (22 → 7 → 0).
Tỉ lệ nhiễu của họ (127/3 ≈ **42:1**) là hợp lý; tôi không tái lập được con số 127 nhưng **cơ chế thì đúng**.

**GAP-4/GAP-5:** GAP-4 (*verify nội dung ≠ verify toàn vẹn artifact*) là **nhận định đúng và quan trọng** —
nó khái quát hoá đúng cả GAP-0 (T14) và GAP-1 (`LOG` #54). GAP-5 (task placeholder trông như uỷ quyền)
là **quan sát hợp lý**, mức thấp, đúng như họ tự xếp.

**Phán quyết T27-B: PASS.** 3 link đã sửa đúng · **lệnh cấm sửa `scope_github.md` được tôn trọng tuyệt đối
(hash giống hệt 3 revision)** · `SCOPEGAP.md` có **2 phát hiện đúng** (GAP-0 trúng **chính T14 của tôi**;
GAP-1 trúng **`LOG` #54 của Admin**) và **số liệu tái lập được chính xác**.

---

## 2.21 Đã kiểm những mục nào (vòng 6)

**T27: đã kiểm 20 mục.**

- **T27-A (T23) — 9 mục, PASS 4/4 hạng mục:** A1 ba ô C2 (C2a/C2b/C2c) tồn tại + hành động được · A2 `capstone`
  ghi rõ nguồn ở **5 vị trí tài liệu**, **0 dòng khẳng định thiếu nguồn** · A3 **tái lập demo chính xác**
  (`yara`/`msoffcrypto` grep-thiếu-nhưng-import-THÀNH-CÔNG = 2 kết luận sai nếu chỉ grep) · A3-ổn định
  (`diff` rỗng) · A3b **tự giới hạn ĐÚNG, xác nhận bằng bản gốc T4** (`unicorn` không có trong mẫu grep T4;
  tên gói = tên module) · A4 **blob hash bằng chứng thô giống hệt** · +2 mục phụ (file T5 đổi đều là tài liệu).
- **T27-B (T26) — 11 mục:** B0 merge-base (11 file, tất cả trong territory) · B1 3 link đã sửa + resolve ·
  B1b quét toàn territory (sau khi sửa bộ quét: **0 link sai**) · B1f `security/*/RECON.md` **7/7 link resolve** ·
  B2 **blob hash `scope_github.md` giống hệt 3 revision** + 3 link thiếu scheme còn nguyên · B3 GAP-0 **ĐÚNG**
  (tự kiểm chứng T14 của mình) · B3 số liệu **tái lập chính xác** (24/10/3/30 %) · B3 GAP-1 **ĐÚNG**
  (đường dẫn trong `LOG` #54 không tồn tại) · B3 GAP-2 **ĐÚNG** (0 file dưới `security/**/EVIDENCE/`) ·
  B3 GAP-3 **đúng, tôi vừa tự chứng minh** · B3 GAP-4/GAP-5 đánh giá hợp lý.
- **`chưa xác minh`: 0 mục.**
- **Tự khai 2 lỗi của tôi trong vòng này:** (1) **bộ quét link báo động giả** (22 → 7 → **0**) — đúng y GAP-3;
  (2) **đo số liệu GAP-0 bằng bộ lọc thô** ra 33/13/6, suýt kết luận sai là BountyRecon tính nhầm —
  sau khi lọc theo AUTHORED thì **khớp chính xác 24/10/3**.
- **Phương pháp:** dùng `git worktree add` (**index riêng**) — đúng bài học tự khai ở T25; xác nhận
  `git status` của repo chính **sạch** trong suốt quá trình.

> **Phán quyết vòng 6: T23 PASS 4/4 · T26 PASS.** Không reject mục nào. **Hai phát hiện của BountyRecon
> là đóng góp thật**: GAP-0 chỉ ra **T14 của tôi** không kiểm link, GAP-1 chỉ ra **`LOG` #54 của Admin**
> trỏ đường dẫn chết. Tôi ghi nhận cả hai **không kèm biện hộ**.

---

# VÒNG 7 — Bài kiểm #10 (T30): T28 + T29 BountyRecon

**Người kiểm:** Reviewer1 (`ag_76306ba6`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/reviewer-1/T30`
**Base:** `origin/main` = `c1462df` (213 file) · **Artifact:** T28 @ `9f73655` · **T29: CHƯA PUSH**
**Bằng chứng thô:** `agents/reviewer1/evidence/T30/`

```text
[REVIEW] T30-A / BountyRecon / Lớp 1 CROSS / KẾT QUẢ: PASS — 6/6 giá trị băm tái lập CHÍNH XÁC
[REVIEW] T30-B / BountyRecon T29      / KẾT QUẢ: chưa xác minh — NHÁNH CHƯA TỒN TẠI TRÊN REMOTE
```

---

## 2.22 T28 — phép kiểm "vùng trích nguyên văn nguyên vẹn": **tái lập CHÍNH XÁC 6/6**

**Quan trọng — tôi đã sai một lần trước khi ra kết quả đúng:** bộ tách của tôi lúc đầu **loại** ký tự
xuống dòng phân cách, nên đo `pre` = **8283** ký tự và băm `f78c5158c9702b42` — **lệch 1 ký tự** so với
khai báo. Tôi **không** vội kết luận tác giả sai; tôi kiểm giả thuyết **quy ước ranh giới** (gộp hay
không gộp dòng phân cách). Sau khi dùng đúng quy ước (*`pre` gồm cả dòng xuống hàng trước `## 2b.`*),
**toàn bộ 6 giá trị khớp tuyệt đối**:

| Phần | Bản TRƯỚC (`8006168`) | Bản SAU (`9f73655`) | Khai báo của T28 | |
|---|---|---|---|---|
| **`pre`** (trước §2b) | len **8284** · `09fce4b8afac0ede` | len **8284** · `09fce4b8afac0ede` | 8284 · `09fce4b8afac0ede` **cả hai** | ✅ **CHÍNH XÁC** |
| **thân §2b** | len 1695 · `2f7322f812e7e249` | len 3164 · `099b489f47f5e953` | `2f7322f812e7e249` → `099b489f47f5e953` | ✅ **CHÍNH XÁC** |
| **`suf`** (từ `## 3.`) | len **5490** · `40904074229cbabc` | len **5490** · `40904074229cbabc` | 5490 · `40904074229cbabc` **cả hai** | ✅ **CHÍNH XÁC** |

⇒ **`pre` và `suf` giống hệt từng byte; độ dài không đổi ⇒ không byte nào ngoài §2b bị dịch chuyển.**
Dòng ranh giới: `## 2b.` ở dòng **146** ở **cả hai bản**; `## 3.` dịch `174 → 204` (vì §2b dài ra) — **đúng dự kiến**.

**A3 — mọi hunk `git diff` nằm trong §2b:** 4 hunk `-146`, `-148,2`, `-151`, `-153,18` → dải cũ
**146..170**; §2b cũ thực tế chiếm dòng **146..173** (dòng 171–173 là ngữ cảnh không đổi). ⇒ **4/4 hunk
TRONG §2b** ✅. Khai báo của họ ("146–170") **đúng về dòng cuối bị sửa**.

**A4 — vùng nguyên văn khác không bị chạm:** `git diff --name-status 8006168 9f73655` → **đúng 3 file mới
của T28 + `security/gitlab/SCOPE.md`**, không file nào khác. Và `scope_github.md` blob =
**`15c946ff956a3fdb466f7f9768081af29b812088`** ✅ — **trùng đúng blob tôi đã trích ở T27**.

**A5 — nội dung §2b mới:** nhãn *"**0 XUNG ĐỘT HIỆU LỰC**"* ✅ · bảng có cột **`archived_at`** với 4 giá trị
thời gian cụ thể ✅ · dẫn chiếu **`security/_TEMPLATE/SCOPE.md`** xác nhận `archived_at` là trường **bắt buộc** ✅ ·
**quyết định của Admin giữ nguyên** ("vẫn loại cả 4 khỏi T4") ✅.

### 2.22.1 TÁI LẬP ĐỘC LẬP phát hiện `archived_at` — **mọi con số khớp tuyệt đối**

Tôi tự gọi `POST https://hackerone.com/graphql` (không dùng script/JSON của tác giả), **có hỏi thêm
trường `archived_at`** — trường mà **tôi đã KHÔNG hỏi ở T14**:

| Khẳng định của T28 | Tôi đo được | |
|---|---|---|
| `archived_at` **có** trong schema công khai | `__type(name:"StructuredScope"){fields{name}}` → **39 trường**, `archived_at` **có mặt** | ✅ |
| Tổng scope | **63** — **khớp đúng con số tôi đo ở T14** | ✅ |
| `archived:false` → **44** (IN=**19**, OUT=**25**) | **44 (19 / 25)** | ✅ **CHÍNH XÁC** |
| `archived:true` → **19** | **19** | ✅ **CHÍNH XÁC** |
| Giao IN ∩ OUT trong tập **đang hiệu lực** = **0** | **`[]`** | ✅ **CHÍNH XÁC** |
| 4 tài sản: vế OUT có `archived_at` | `*.gitlab.net` `2022-07-21T15:51:33.499Z` · `*.gitlap.com` `…15:51:16.877Z` · `about.gitlab.com` `…15:53:03.572Z` · `docs.gitlab.com` `…15:53:13.475Z` | ✅ **KHỚP TỪNG MILI-GIÂY** |
| Vế IN đều `archived_at=None` | ✅ cả 4 | ✅ |

### 2.22.2 ⚠️ ĐIỀU NÀY SỬA LẠI **CHÍNH T14 CỦA TÔI** — tôi ghi nhận công khai

Ở T14 tôi kết luận: *"**2 xung đột THẬT** (`about`/`docs.gitlab.com`, cùng `asset_type=URL`)"* và
*"2 cặp wildcard/apex khác `asset_type` — chưa chắc là mâu thuẫn"*. **Kết luận "xung đột thật" của tôi SAI.**
Sự thật: **cả 4 vế OUT đều là bản ghi ĐÃ NGHỈ HƯU ngày `2022-07-21`** — cách vế IN **4 năm**.
**0 xung đột hiệu lực.**

**Nguyên nhân sai của tôi:** truy vấn T14 của tôi **không hỏi `archived_at`** — dù trường đó **có sẵn
trong schema**. Đây là **lỗ hổng thứ hai của T14**, khác GAP-0 (không kiểm link): tôi **không liệt kê
các trường schema có sẵn** trước khi kết luận về dữ liệu. **Auditor2 (M-01) + BountyRecon (T28) tìm ra
đúng nguyên nhân; DeepSeek-Harness và tôi đều từng nói "4 xung đột thật" — cả hai đều sai.**
Tôi ghi vào `reviews/RECONCILE.md` để phán quyết cũ không còn đứng một mình.

### 2.22.3 KẼ HỞ của phép kiểm "vùng nguyên văn nguyên vẹn" (Admin yêu cầu nêu)

Phép kiểm này **mạnh và đúng**, nhưng nó là phép so **HAI ĐIỂM**, không phải so **LỊCH SỬ**. Tôi nêu 3 kẽ hở:

| # | Kẽ hở | Mức | Cách bịt |
|---|---|---|---|
| **K1** | So `merge-base` ↔ `branch head`. Một commit **trung gian** sửa `pre` rồi **revert** sẽ **lọt** — hai điểm vẫn giống nhau | **Thật** | Thêm `git log -p <merge-base>..<head> -- <file>` và kiểm **mọi hunk của MỌI commit** nằm trong §2b |
| **K2** | Ranh giới §2b/§3 lấy theo **dòng tiêu đề**. Nếu ai đó **đổi tên tiêu đề** §2b hoặc chèn mục mới **trước** nó, ranh giới dịch ⇒ nội dung bị "gán nhầm vùng" mà hash vẫn có thể trùng hợp | Thấp | Ghim ranh giới bằng **chuỗi neo cố định** đã thoả thuận, không chỉ "dòng bắt đầu bằng `## 2b.`" |
| **K3** | Không kiểm **nguồn gốc thượng nguồn**: `pre`/`suf` có thể vẫn nguyên trong repo nhưng **lệch** so với chính sách GitLab **hiện hành** (upstream đổi) | Thấp (ngoài phạm vi) | Định kỳ tái fetch và đối chiếu byte-exact với nguồn |

**Tôi ĐÃ thử K1 trên chính artifact này:** `git log --oneline 8006168..9f73655 -- security/gitlab/SCOPE.md`
→ **chỉ MỘT commit** (`9f73655`), và **cả 4 hunk của nó đều trong §2b** ⇒ **K1 KHÔNG bị khai thác ở đây**.
Và `core.autocrlf` **không đặt** ⇒ không có chuẩn hoá xuống dòng làm sai hash.
⇒ **Phép kiểm của T28 đạt**, kèm **1 khuyến nghị phương pháp** (thêm kiểm theo lịch sử, không chỉ 2 điểm).

---

## 2.23 T29 — **CHƯA THỂ KIỂM: NHÁNH CHƯA TỒN TẠI TRÊN REMOTE**

```text
$ git ls-remote origin agent/bounty-recon/T29
(rong)
```

`git ls-remote --heads origin | grep bounty-recon` → chỉ có **T3, T26, T28**. ⇒ **T29 chưa được push**
tại thời điểm kiểm (`2026-10-01T15:04Z`). **4 mục B1–B4 của Admin không thể chấm** ⇒ ghi `chưa xác minh`.

**Thay vào đó tôi kiểm TRẠNG THÁI `9f73655` để xác nhận TIỀN ĐỀ của T29** — và **tiền đề đó ĐÚNG**:

| Dòng Admin nêu | Nguyên văn @ `9f73655` | Còn mâu thuẫn §2b? |
|---|---|---|
| **dòng 9** | `**Trạng thái:** ⚠️ **Trích được nguyên văn, NHƯNG có 4 XUNG ĐỘT scope — xem §2b. PHẢI HỎI ADMIN.**` | ❌ **CÓ** |
| **§5 dòng 284** | `\| Trích được nguyên văn in-scope? \| ✅ **CÓ** (24 tài sản) — nhưng 4 tài sản bị xung đột \|` | ❌ **CÓ** |
| **§5 dòng 289** | `\| Đủ điều kiện chuyển ExploitDeep (T4)? \| ⚠️ **CÓ ĐIỀU KIỆN** — phải chốt 4 xung đột ở §2b trước \|` | ❌ **CÓ** — phải đổi sang **chỉ thị target của Admin (D-013)** |

`FIX_2B.md` của T28 **đã tự liệt kê đúng cả 3 dòng (A/B/C)** và **từ chối sửa** vì chỉ thị T28 giới hạn ở §2b —
**kỷ luật đúng**. Họ cũng đúng khi chỉ ra 3 dòng này **không phải văn bản trích nguyên văn** (là phần tổng hợp
của họ) ⇒ sửa **không** ảnh hưởng cơ sở pháp lý.

### 2.23.1 ⚠️ PHÁT HIỆN MỚI — T29 **bỏ sót** một chỗ cùng loại

Quét **toàn territory** BountyRecon (không chỉ `SCOPE.md`), còn một chỗ **cùng loại chưa được xử lý** và
**không** nằm trong danh sách 3 dòng của Admin:

```text
9f73655:agents/bountyrecon/tasks/T3/CANDIDATES.md:64:
## 2. 🚨 VẤN ĐỀ CHẶN — 4 XUNG ĐỘT SCOPE CỦA GITLAB (CẦN ADMIN PHÁN QUYẾT)
```

và ngay dưới nó vẫn còn nguyên **bảng 4 tài sản** + **`⛔ CẤM ExploitDeep chạm 4 tài sản này`** +
**"Đề nghị Admin chọn 1 trong 2: (a) … (b) …"** — tức vẫn **khẳng định một blocker chưa giải quyết** và
**xin một phán quyết mà Admin ĐÃ ban hành** (D-021: loại cả 4; `DISSENT-7/8`).

- **Mức:** trung bình — đây là mục **đọc-là-thấy-cần-hành-động**, nguy hiểm hơn ghi chú lịch sử.
- **Đề xuất:** mở rộng T29 (hoặc task riêng) để sửa **`CANDIDATES.md:64`** theo cùng cách: đổi tiêu đề sang
  *"4 BẢN GHI ĐÃ NGHỈ HƯU — 0 XUNG ĐỘT HIỆU LỰC"*, thay bảng bằng bản có `archived_at`, và ghi
  **quyết định D-021 đã ban hành** thay cho lời xin phán quyết.
- **B3/B4 của T29 (tái lập phép băm từng phần; quét toàn bộ):** **`chưa xác minh`** — không có nhánh để kiểm.

---

## 2.24 Bổ sung quy trình vào Lớp 1 (Admin mời ở D-022)

Admin đã thêm **4 phép kiểm cơ học bắt buộc** vào `LOG` #69. Tôi bổ sung vào **Lớp 1 của tôi** 2 phép kiểm
tương ứng — mỗi phép kèm lệnh chạy được, để người sau tái lập:

### 2.24.1 [MỚI] Kiểm link tương đối — có phân loại AUTHORED vs CAPTURE

```bash
# Voi MOI file .md trong pham vi kiem:
#  1. Boc bo fenced code (```...```) va inline code (`...`) TRUOC khi quet link
#  2. Phan loai AUTHORED (nguoi viet) vs CAPTURE (bang chung tho: EVIDENCE/, .html, .json)
#  3. Chi ket luan DEFECT tren file AUTHORED
#  4. Tinh tu thu muc cua file, KHONG tinh tu goc repo
#  5. Doi chieu ca FILE lan THU MUC (link tro thu muc la hop le)
```

**Vì sao phải có bước phân loại:** đo trên chính territory này, bộ quét **ngây thơ** cho
**127 "lỗi"** trong khi **lỗi thật = 3** (nhiễu/lỗi ≈ **42:1**) — `LOG` #69; và **tôi tự mắc đúng lỗi đó
trong vòng này** (22 → 7 → **0**). Một reviewer dùng công cụ ngây thơ sẽ **ngập nhiễu và bỏ sót lỗi thật**.

### 2.24.2 [MỚI] Kiểm toàn vẹn VÙNG TRÍCH NGUYÊN VĂN — **theo LỊCH SỬ, không chỉ 2 điểm**

```bash
# Cho moi vung nguyen van duoc tuyen bo "khong doi":
#  a) Bam rieng pre / than-muc / suf o HAI diem (merge-base va head)  -> phai trung nhau
#  b) VA: git log -p <merge-base>..<head> -- <file>  -> MOI hunk cua MOI commit phai nam trong vung duoc phep sua
#  c) Ghi ro QUY UOC RANH GIOI (co gom dong phan cach hay khong) — lech 1 ky tu la lech hash
```

**Vì sao cần (b):** phép so 2 điểm **bỏ lọt** thao tác *sửa rồi revert* ở commit trung gian (kẽ hở **K1**).
**Vì sao cần (c):** trong vòng này, bộ tách của tôi lệch **đúng 1 ký tự** so với tác giả **chỉ vì quy ước
ranh giới** — nếu tôi không kiểm giả thuyết đó, tôi đã **báo oan** một phép kiểm đúng.

> **Đây chính là dạng kiểm tôi đã THIẾU ở T14 (GAP-0).** Tôi đã áp dụng nó ở T27 và T30; từ nay nó là
> bước bắt buộc trong Lớp 1.

---

## 2.25 Đã kiểm những mục nào (vòng 7)

- **T30-A (T28) — 12 mục, PASS 5/5 hạng mục:** A1 băm 3 phần (**6/6 giá trị khớp chính xác**) ·
  A2 độ dài `pre`=8284 / `suf`=5490 ở **cả hai** bản · A3 **4/4 hunk trong §2b** · A4 `scope_github.md`
  blob `15c946ff…` khớp + **chỉ 1 file văn bản bị sửa** · A5 nội dung §2b (nhãn · `archived_at` · `_TEMPLATE` ·
  quyết định Admin giữ nguyên) · A6 **tái lập độc lập `archived_at`** (7/7 con số khớp) · A7 **thử kẽ hở K1** ✅.
- **T30-B (T29) — 4 mục `chưa xác minh`** (nhánh chưa push) **+ 2 mục kiểm được:** tiền đề T29 **ĐÚNG**
  (3/3 dòng còn mâu thuẫn) · **phát hiện mới: `CANDIDATES.md:64` cùng loại, T29 bỏ sót**.
- **`chưa xác minh`: 4 mục** (B1/B2/B3/B4 của T29) — **nêu rõ lý do: nhánh chưa tồn tại trên remote.**
- **Tự khai lỗi của tôi:** (1) bộ tách vùng lệch **1 ký tự** do quy ước ranh giới (đã sửa, ra đúng 6/6);
  (2) **T14 kết luận "2 xung đột THẬT" là SAI** — tôi không hỏi `archived_at` dù trường đó có sẵn trong schema;
  (3) T14 cũng không kiểm link (GAP-0, đã ghi ở T27).

> **Phán quyết vòng 7: T28 PASS — phép kiểm mạnh nhất của họ tái lập chính xác 6/6 giá trị băm và 7/7 con số
> `archived_at`; điều này sửa lại chính kết luận T14 của tôi. T29 `chưa xác minh` (nhánh chưa push),
> kèm 1 phát hiện mới về chỗ bỏ sót.**
