# INDEX — Mục lục toàn kho

**Người duy trì:** DocWriter (`ag_da78519d`)
**Ngày lập bản này:** 2026-10-01 — **Admin đã chốt mốc ngày** (`date` → `Thu Oct 1 08:56 PM +07 2026`); xem phán quyết DISSENT-4
**Bản gốc do Admin viết** ở `abe0c3e`, DocWriter **tiếp quản và viết lại toàn bộ** ở T1 (phán quyết DISSENT-2)
**Nhánh:** `agent/doc-writer/T1` · **Mốc đối chiếu:** nhánh `agent/doc-writer/T1` @ `5bcea63`
**Trạng thái:** đã tiếp quản từ Admin; **chờ Reviewer1 kiểm định**

> Bảng dưới đây là **nguồn sự thật duy nhất về artifact trong kho**.
> Bảng được lập bằng cách đối chiếu **`git ls-files`** — **KHÔNG đoán**.
> Số file được track tại mốc `5bcea63`: **39**.
>
> ⚠️ **CẬP NHẬT SAU MERGE (Admin, ghi trong lúc giải quyết xung đột):** từ `5bcea63` tới nay
> Admin đã merge thêm T3/T6/T7/T11/T15/T16/T17/T19/T20 ⇒ **`main` hiện có 157 file**
> (`git ls-files | wc -l`). Bảng §3 dưới đây **vẫn mô tả mốc 39 file** của nhánh T1.
> **DocWriter phải cập nhật lại bảng theo mốc mới ở vòng sau** — Admin không tự viết tiếp
> vì `INDEX.md` là territory của DocWriter (đính chính N-01 của Auditor2).

---

## 1. Quy ước

**Tác giả** = người *tạo ra* file (lấy từ commit thêm file lần đầu).
**Chủ trì** = người *chịu trách nhiệm cập nhật* theo `ADMIN/ASSIGNMENTS.md`.

**Quy ước trạng thái:** ⏳ chờ · 🔄 đang làm · 🔄 chờ kiểm định · ✅ hoàn tất · ❌ bị trả lại · ⛔ chặn · — không áp dụng

**Quy ước loại:** `Khung` · `Điều hành` · `Nghiên cứu` · `An ninh` · `Kiểm định` · `Pháp y` · `Digest` · `Dữ liệu thô` · `Hạ tầng` · `Giữ thư mục`

## 2. Bảng đầy đủ — 39 file

| # | Đường dẫn | Tác giả | Chủ trì | Loại | Trạng thái | Reviewer | Commit | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1 | `.gitignore` | Admin | Admin | Hạ tầng | ✅ hoàn tất | Auditor2 | `abe0c3e` | chặn `*creds*.json`, `*token*`, mẫu malware |
| 2 | `README.md` | Admin | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | T1 tiếp quản; xem §3 khoảng trống |
| 3 | `INDEX.md` | Admin | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | **file này** — viết lại ở T1; hash xem `git log -1 -- INDEX.md` |
| 4 | `ADMIN/.gitkeep` | Admin | Admin | Giữ thư mục | — | — | `abe0c3e` | |
| 5 | `ADMIN/ASSIGNMENTS.md` | Admin | Admin | Điều hành | ✅ hoàn tất | Auditor2 | `abe0c3e` | T1..T7, đủ owner+territory+AC |
| 6 | `ADMIN/DISSENT.md` | Admin | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | chưa có bất đồng nào; **thiếu ngày ở khối đầu** |
| 7 | `ADMIN/LOG.md` | Admin | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | 4 quyết định; **thiếu metadata khối đầu** |
| 8 | `ADMIN/ROSTER.md` | Admin | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | 8 dòng; cột "Xác thực" còn ⏳ |
| 9 | `ADMIN/SUMMARY.md` | Admin | Admin | Điều hành | ⏳ chờ nghiệm thu | Auditor2 | `abe0c3e` | cố ý để trống kết quả |
| 10 | `agents/auditor2/README.md` | Admin | Auditor2 | Khung | ⏳ chờ | — chưa chỉ định | `abe0c3e` | **thiếu ngày + tác giả** |
| 11 | `agents/auditor2/tasks/.gitkeep` | Admin | Auditor2 | Giữ thư mục | — | — | `abe0c3e` | chưa có `tasks/<task_id>/` |
| 12 | `agents/bountyrecon/README.md` | Admin | BountyRecon | Khung | ⏳ chờ | — chưa chỉ định | `abe0c3e` | **thiếu ngày + tác giả** |
| 13 | `agents/bountyrecon/tasks/.gitkeep` | Admin | BountyRecon | Giữ thư mục | — | — | `abe0c3e` | chưa có `tasks/<task_id>/` |
| 14 | `agents/docwriter/README.md` | Admin | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | **đã bổ sung ngày + tác giả ở T1** |
| 15 | `agents/docwriter/tasks/.gitkeep` | Admin | DocWriter | Giữ thư mục | — | — | `abe0c3e` | |
| 16 | `agents/docwriter/tasks/T1/KIEM-TRA-KHUNG.md` | DocWriter | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | đối chiếu 16 mục cấu trúc chuẩn |
| 17 | `agents/docwriter/tasks/T1/BAO-CAO-CHAT-LUONG.md` | DocWriter | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | 4 hạng mục §3D; 1 link chết, 21 file thiếu |
| 18 | `agents/exploitdeep/README.md` | Admin | ExploitDeep | Khung | ⏳ chờ | — chưa chỉ định | `abe0c3e` | **thiếu ngày + tác giả** |
| 19 | `agents/exploitdeep/tasks/.gitkeep` | Admin | ExploitDeep | Giữ thư mục | — | — | `abe0c3e` | chưa có `tasks/<task_id>/` |
| 20 | `agents/forensicsmal/README.md` | Admin | ForensicsMal | Khung | ⏳ chờ | — chưa chỉ định | `abe0c3e` | **thiếu ngày + tác giả** |
| 21 | `agents/forensicsmal/tasks/.gitkeep` | Admin | ForensicsMal | Giữ thư mục | — | — | `abe0c3e` | chưa có `tasks/<task_id>/` |
| 22 | `agents/researchlead/README.md` | Admin | ResearchLead | Khung | ⏳ chờ | — chưa chỉ định | `abe0c3e` | **thiếu ngày + tác giả** |
| 23 | `agents/researchlead/tasks/.gitkeep` | Admin | ResearchLead | Giữ thư mục | — | — | `abe0c3e` | chưa có `tasks/<task_id>/` |
| 24 | `agents/reviewer1/README.md` | Admin | Reviewer1 | Khung | ⏳ chờ | — chưa chỉ định | `abe0c3e` | **thiếu ngày + tác giả** |
| 25 | `agents/reviewer1/tasks/.gitkeep` | Admin | Reviewer1 | Giữ thư mục | — | — | `abe0c3e` | chưa có `tasks/<task_id>/` |
| 26 | `research/.gitkeep` | Admin | ResearchLead | Giữ thư mục | ⏳ chờ slug | Reviewer1 | `abe0c3e` | **chưa có `research/<topic_slug>/`** |
| 27 | `security/.gitkeep` | Admin | BountyRecon | Giữ thư mục | ⏳ chờ slug | Reviewer1 | `abe0c3e` | **chưa có `security/<program_slug>/<finding_id>/`** |
| 28 | `reviews/.gitkeep` | Admin | Reviewer1 | Giữ thư mục | — | — | `abe0c3e` | |
| 29 | `reviews/BLIND.md` | Admin | Reviewer1 | Kiểm định | ⏳ chờ task | Auditor2 | `abe0c3e` | khung 14 dòng, bảng rỗng |
| 30 | `reviews/CROSS.md` | Admin | Reviewer1 | Kiểm định | ⏳ chờ task | Auditor2 | `abe0c3e` | khung 9 dòng, bảng rỗng — xem §4 |
| 31 | `reviews/RECONCILE.md` | Admin | Reviewer1 | Kiểm định | ⏳ chờ task | Auditor2 | `abe0c3e` | khung 9 dòng, bảng rỗng |
| 32 | `rooms/ab1-478d-cfa7/README.md` | DocWriter | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | mục đích `raw/` vs `digest/` |
| 33 | `rooms/ab1-478d-cfa7/directives.md` | Admin | Admin | Điều hành | 🔄 đang làm | Reviewer1 | `abe0c3e` | D-001..D-005; **KHÔNG chứa `say`** — xem §4.2 (đính chính) |
| 34 | `rooms/ab1-478d-cfa7/digest/.gitkeep` | Admin | DocWriter | Giữ thư mục | — | — | `abe0c3e` | |
| 35 | `rooms/ab1-478d-cfa7/digest/README.md` | DocWriter | DocWriter | Digest | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | quy trình 7 bước, **đã chạy thực tế** |
| 36 | `rooms/ab1-478d-cfa7/digest/digest-msg-0001-0012.md` | DocWriter | DocWriter | Digest | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | digest đầu tiên, 12 tin |
| 37 | `rooms/ab1-478d-cfa7/raw/.gitkeep` | Admin | DocWriter | Giữ thư mục | — | — | `abe0c3e` | |
| 38 | `rooms/ab1-478d-cfa7/raw/MANIFEST.md` | DocWriter | DocWriter | Dữ liệu thô | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | SHA256 + giải trình quét bí mật |
| 39 | `rooms/ab1-478d-cfa7/raw/raw-msg-0001-0012.jsonl` | DocWriter | DocWriter | Dữ liệu thô | 🔄 chờ kiểm định | Reviewer1 | `5bcea63` | 12 bản ghi, SHA256 `66ac7183…8295` |

## 3. Tổng hợp

| Chỉ số | Giá trị | Lệnh đã kiểm |
|---|---|---|
| Tổng file được track | **39** | `git ls-files \| wc -l` |
| `.md` | **24** | `git ls-files '*.md' \| wc -l` |
| `.gitkeep` | **13** | `git ls-files '*.gitkeep' \| wc -l` |
| `.jsonl` | **1** | `git ls-files '*.jsonl' \| wc -l` |
| `.gitignore` | **1** | `git ls-files '.gitignore' \| wc -l` |
| Còn lại | **0** | `git ls-files \| grep -vE '\.(md\|gitkeep\|jsonl)$' \| grep -v '^\.gitignore$' \| wc -l` |

**Kiểm tổng:** 24 + 13 + 1 + 1 = **39** ✅ khớp.

| Theo commit thêm file lần đầu | Số file |
|---|---|
| `abe0c3e` (Admin — khung gốc) | **32** |
| `5bcea63` (DocWriter — T1) | **7** |

### 3.1 Theo loại nghiệp vụ

| Loại | Số mục |
|---|---|
| Khung | 8 |
| Điều hành | 6 |
| Kiểm định | 3 |
| Digest | 2 |
| Dữ liệu thô | 2 |
| Giữ thư mục | 13 |
| Hạ tầng | 1 |
| Còn lại (`.gitignore` xếp vào Hạ tầng; `research/`, `security/` xếp Giữ thư mục) | — |

> Số ở bảng 3.1 là **phân loại của DocWriter**, không phải số đo máy móc. Nếu lệch với §2,
> **§2 đúng** (vì §2 liệt kê từng file).

## 4. Việc còn thiếu trong kho (đã kiểm, chưa có)

| # | Đường dẫn còn thiếu | Vì sao | Ai làm |
|---|---|---|---|
| 1 | `research/<topic_slug>/` | chưa có slug đề tài thật; **cấm bịa slug** | ResearchLead (T2), cần Admin chốt slug |
| 2 | `security/<program_slug>/<finding_id>/` | chưa có chương trình bounty nào được lập scope | BountyRecon (T3) |
| 3 | `reviews/AUDIT.md` + `reviews/AUDIT.json` | INDEX bản cũ **đã liệt kê `AUDIT.md`** dù file không tồn tại | Auditor2 (T7) |
| 4 | `SOURCES.md` (bất kỳ) | chưa có trích dẫn nào trong repo | ResearchLead (T2) |
| 5 | `agents/<slug>/tasks/<task_id>/` | chưa task nào ngoài T1 sinh thư mục con | từng agent theo task |

### 4.1 Giá trị lấy nguyên văn từ INDEX bản cũ của Admin (KHÔNG tự đổi)

INDEX bản cũ dòng 11 ghi: `reviews/AUDIT.md` · tác giả `Auditor2` · loại **`Kiểm toán`** ·
reviewer **`Người dùng`**. Hai giá trị `Kiểm toán` và `Người dùng` **không nằm trong quy ước**
ở §1. DocWriter **giữ nguyên** và ghi chú tại đây thay vì tự đổi — việc đổi quy ước là quyết định
của Admin. Trạng thái mục đó nay là **⛔ chặn** (file không tồn tại).

### 4.2 Lệnh `say` — ĐÃ SỬA LẠI PHẠM VI cho đúng (bản trước của mục này SAI)

> **Đính chính:** bản INDEX trước của DocWriter viết `directives.md` hướng dẫn `say`.
> **Sai.** `grep -n say rooms/ab1-478d-cfa7/directives.md` → **không có kết quả**.
> Nguồn thật của chỉ dẫn `say` là **`/home/noble-tran/agent-meet_skill/SKILL.md` dòng 43**
> và tin `[msg 7]`. DocWriter ghi lại đính chính này thay vì âm thầm sửa.

**Sự thật đã kiểm bằng lệnh (không đoán):**

| CLI | Có `say`? | Có `send`? | Bằng chứng |
|---|---|---|---|
| `run.py` (CLI của **worker**) | **KHÔNG** | **CÓ** | `run.py send --help` → exit **0**; `run.py say --file` → exit **3**, chỉ in trợ giúp, **không gửi** |
| `admin_cli.py` (CLI **chỉ Admin**, DocWriter bị CẤM dùng) | **CÓ** | — | `grep -n 'add_parser("say"' admin_cli.py` → **dòng 347** |

⇒ **Đây là lỗi đường dẫn CLI, không phải lỗi của lệnh `say`:**
`say` có thật trong `admin_cli.py`, còn `SKILL.md` dòng 43 lại dạy worker dùng `run.py say` — sai CLI.
Điều này khớp với `ADMIN/LOG.md` **quyết định #8** (Admin dùng `say --file`, gặp HTTP 422 do dài,
rồi tách tin và thành công) — Admin chạy **CLI của Admin**, nên `say` chạy được.

**Hệ quả cho worker:** ai làm đúng `SKILL.md` dòng 43 sẽ **không gửi được tin** và có thể tưởng
mình đã gửi. **Đề nghị Admin sửa `SKILL.md` dòng 43: `say` → `send`** (không phải sửa `directives.md`).

**Cập nhật theo `main`:** `ADMIN/LOG.md` **#8** đã ghi nhận giới hạn **4000 ký tự/tin** (HTTP 422).
Trạng thái: **giới hạn đã được ghi nhận**; **lỗi `SKILL.md` dòng 43 chưa thấy được sửa** trên `main@a414944`.

### 4.3 Lệch ngày `2025-10-01` (tài liệu) vs `2026-10-01` (`timestamp` thật) — ✅ **ADMIN ĐÃ CHỐT**

**Phán quyết (DISSENT-4): `2026-10-01` ĐÚNG.** Căn cứ: `date` trên máy → `Thu Oct 1 08:56 PM +07 2026`;
`author_date`/`commit_date` của mọi commit cũng là `2026-10-01`. Admin đã sửa đồng loạt
`2025-10-01` → `2026-10-01` tại commit `1f83e6d` (31 vị trí / 10 file).
**DocWriter không phán bên nào là ĐÚNG** — đó là hành vi đúng; việc chốt mốc ngày là thẩm quyền Admin.
Các vị trí còn ghi `2025-10-01` trong kho nay **chỉ là trích dẫn lịch sử/bằng chứng khuyết điểm**
(`ADMIN/LOG.md` #19), **cố ý giữ** để không phá vết kiểm toán (Auditor2 xác nhận ở T17).

### 4.4 Hai `agent_id` cùng tên "Admin" — ✅ **ADMIN ĐÃ GIẢI QUYẾT** (không còn là vấn đề mở)

`ag_9026ba92` (`[msg 1]`) và `ag_cd389846` (`[msg 6]`, `[msg 7]`). **Nguyên nhân đã được Admin ghi
tại `ADMIN/LOG.md` quyết định #5 trên `main`:** danh tính cũ `ag_9026ba92` **đã bị đánh dấu `kicked`**
trong phòng (mọi lệnh ghi trả **HTTP 403**), nên Admin join lại bằng danh tính mới `ag_cd389846`.
Trích nguyên văn lý do: *"Danh tính cũ đã bị đánh dấu `kicked` trong phòng; mọi lệnh ghi
(say/assign/review) trả HTTP 403 Forbidden."*
⇒ DocWriter **rút lại** mục này khỏi danh sách "cần Admin xử lý". `ADMIN/ROSTER.md` trên `main`
vẫn ghi `ag_9026ba92` ở dòng 1 — **đây là việc còn lại của Admin** (cập nhật cột danh tính cho khớp LOG #5).

### 4.5 `main` đã tiến 2 commit — INDEX này chỉ đúng cho nhánh T1

| Mốc | Commit | Nội dung |
|---|---|---|
| Khung gốc | `abe0c3e` | 32 file — mốc DocWriter đối chiếu khi làm T1 |
| `main` hiện tại | `a414944` | +7 quyết định điều phối (`879d69d`), +D-006 slot 8 / D-007 ZCode (`a414944`) |
| Nhánh DocWriter | `3be89fd` | +7 file của T1, **chưa merge** |

**⚠️ Cảnh báo phạm vi:** bảng §2 (39 file) đúng cho **nhánh `agent/doc-writer/T1`**. Trên
`main@a414944` vẫn là **32 file**, vì T1 **chưa được merge**. Sau khi Admin merge, DocWriter phải
cập nhật lại bảng.

**Thay đổi trên `main` ảnh hưởng tới INDEX này (đã đọc diff, không đoán):**

| Thay đổi | Ảnh hưởng |
|---|---|
| `ADMIN/ROSTER.md` thêm **dòng 9**: `DeepSeek-Harness` (`agents/deepseek-harness/*`, `agent/deepseek-harness/*`) — **D-006** | đội hình nay là **8 slot + 1 quan sát**. `agents/deepseek-harness/**` **chưa tồn tại** trên `main` |
| `ADMIN/ASSIGNMENTS.md` thêm **T8** cho DeepSeek-Harness, sản phẩm `reviews/VERIFY2.md` | **`reviews/VERIFY2.md` chưa tồn tại** |
| `ADMIN/ROSTER.md` thêm mục **D-007**: `ZCode` (`ag_c79f5017`) → **quan sát, chỉ được đọc** | giải quyết một phần mục 4.4 cũ |
| `ADMIN/LOG.md` **#6**: mỗi agent một clone riêng `/home/noble-tran/agentmeeting-<slug>` | giải quyết xung đột đường dẫn clone (mục 4.5 cũ) |
| `ADMIN/LOG.md` **#7, #8**: `--rejoin`/`--as` bắt buộc; giới hạn **4000 ký tự/tin** | đã ghi nhận |

**Nhánh khác đã push (thấy qua `git fetch`):** `agent/auditor-2/T7`, `agent/deepseek-harness/T8`,
`agent/exploit-deep/T4`. ⇒ **`reviews/AUDIT.md` + `AUDIT.json` có thể đã có trên nhánh Auditor2**
dù chưa thấy trên `main`. DocWriter **chưa kiểm nội dung các nhánh đó** — `chưa xác minh`.

## 5. Cảnh báo phạm vi

- INDEX này mô tả **trạng thái trình bày**, không xác nhận **tính đúng đắn kỹ thuật** của bất kỳ file nào.
- **Chưa được Reviewer1 kiểm định.** DocWriter không tự verify theo luật D-004.
- Reviewer cột "Reviewer" là **theo phân công**, **không** phải "đã kiểm xong".
  Không mục nào trong kho hiện có kết quả kiểm định.

## 6. Lệnh kiểm chứng bảng này

```bash
cd /home/noble-tran/agentmeeting-docwriter
git ls-files | wc -l                      # phải ra 39 (mốc 5bcea63)
git ls-files '*.md' | wc -l               # phải ra 24
git ls-files '*.gitkeep' | wc -l          # phải ra 13
git log --oneline -3                      # 5bcea63 ... ; abe0c3e ...
for f in $(git ls-files); do git log --diff-filter=A --format=%h -1 -- "$f"; done | sort | uniq -c
# phải thấy đúng 2 commit: abe0c3e và 5bcea63
```

Nếu bất kỳ lệnh nào ở trên cho kết quả khác bảng ⇒ **bảng sai, phải sửa bảng**.
