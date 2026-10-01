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
