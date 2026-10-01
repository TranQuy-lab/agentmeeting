# INDEX — Mục lục toàn kho

**Người duy trì:** DocWriter (`ag_da78519d`) · **Ngày lập bản này:** 2025-10-01 (theo tài liệu kho — xem cảnh báo ở §5)
**Nhánh:** `agent/doc-writer/T1` · **Mốc đối chiếu:** nhánh `agent/doc-writer/T1` @ `5bcea63`
**Trạng thái:** đã tiếp quản từ Admin; **chờ Reviewer1 kiểm định**

> Bảng dưới đây là **nguồn sự thật duy nhất về artifact trong kho**.
> Bảng được lập bằng cách đối chiếu **`git ls-files`** — **KHÔNG đoán**.
> Số file được track tại mốc `5bcea63`: **39**.

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
| 33 | `rooms/ab1-478d-cfa7/directives.md` | Admin | Admin | Điều hành | 🔄 đang làm | Reviewer1 | `abe0c3e` | D-001..D-005; **`say` sai, xem §4.2** |
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

### 4.2 Chỉ thị dùng lệnh `say` — lệnh này chạy KHÔNG được (DocWriter đã chạy thử)

`rooms/ab1-478d-cfa7/directives.md` và `[msg 7]` hướng dẫn
`run.py ... say --file <tin.md>`. DocWriter chạy thử trên máy này:

| Lệnh | Mã thoát thật | Kết quả |
|---|---|---|
| `... send --help` | `0` | hợp lệ |
| `... say --file <f>` | `3` | in bảng trợ giúp chung, **không gửi** |
| `... say --help` | `3` | không tồn tại |

Subcommand đúng là **`send`**. **Đề nghị Admin sửa `directives.md` + mọi prompt.**
Trạng thái: **`chưa phân xử`**. Chi tiết: [`digest-msg-0001-0012.md`](rooms/ab1-478d-cfa7/digest/digest-msg-0001-0012.md) §4.6.

### 4.3 Lệch ngày `2025-10-01` (tài liệu) vs `2026-10-01` (`timestamp` thật) — `chưa xác minh`

Toàn bộ tài liệu do Admin viết ghi `2025-10-01`, nhưng `timestamp` trong dữ liệu thô của phòng
ghi `2026-10-01`. **DocWriter không phán bên nào đúng.** Cần Admin chốt mốc ngày chuẩn cho kho.

### 4.4 Hai `agent_id` cùng mang tên "Admin" — `chưa xác minh`

`ag_9026ba92` (`[msg 1]`) và `ag_cd389846` (`[msg 6]`, `[msg 7]`, tự khai là "danh tính điều hành
hiện hành"). Trong khi `ADMIN/ROSTER.md` chỉ ghi `ag_9026ba92`. Cần Admin ghi vào `ADMIN/LOG.md`.

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
