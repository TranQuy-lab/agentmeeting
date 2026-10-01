# KIỂM TRA KHUNG — đối chiếu cấu trúc Admin đã dựng với cấu trúc chuẩn

**Tác giả:** DocWriter (`ag_da78519d`) · **Ngày:** 2025-10-01 · **Task:** T1
**Nhánh:** `agent/doc-writer/T1` · **Mốc đối chiếu:** commit `abe0c3e` (khung gốc của Admin)
**Loại:** Kiểm tra trình bày — **KHÔNG phải kiểm định kỹ thuật** (việc đó thuộc Reviewer1)

> **Phạm vi:** tài liệu này chỉ so *sự tồn tại của đường dẫn* và *metadata trình bày*.
> Không có kết luận nào về tính đúng/sai của nội dung kỹ thuật.

## 1. Lệnh đã chạy để lấy bằng chứng

```bash
cd /home/noble-tran/agentmeeting-docwriter
git log --oneline -1                 # abe0c3e ...
git ls-files                          # 32 file được track
find . -path ./.git -prune -o -print  # cây thư mục thật
ls reviews/                           # kiểm sự tồn tại của AUDIT.*
```

Kết quả thô (không lược bỏ):

- `git ls-files | wc -l` → **32**
- `git ls-files '*.md' | wc -l` → **18**
- `ls reviews/` → `BLIND.md` `CROSS.md` `RECONCILE.md` (không có `AUDIT.md`, không có `AUDIT.json`)
- `git ls-files | grep -i sources` → **không có kết quả** (chưa tồn tại `SOURCES.md` nào)

## 2. Đối chiếu từng mục của cấu trúc chuẩn (§3A)

| # | Đường dẫn chuẩn | Có trên đĩa? | Ghi chú |
|---|---|---|---|
| 1 | `README.md` | ✅ | có, 59 dòng |
| 2 | `INDEX.md` | ✅ | có, 23 dòng — nhưng **nội dung chưa đầy đủ**, xem mục 3 |
| 3 | `rooms/<room_id>/raw/` | ✅ | `rooms/ab1-478d-cfa7/raw/` + `.gitkeep` |
| 4 | `rooms/<room_id>/digest/` | ✅ | `rooms/ab1-478d-cfa7/digest/` + `.gitkeep` |
| 5 | `rooms/<room_id>/directives.md` | ✅ | có, 65 dòng, 5 chỉ thị D-001..D-005 |
| 6 | `agents/<agent_slug>/tasks/<task_id>/` | ⚠️ **một phần** | `agents/*/tasks/` có đủ 7 slug + `.gitkeep`, **nhưng chưa có tầng `<task_id>/` nào** |
| 7 | `research/<topic_slug>/` | ❌ **THIẾU** | `research/` chỉ có `.gitkeep`. Không có `topic_slug` nào |
| 8 | `security/<program_slug>/<finding_id>/` | ❌ **THIẾU** | `security/` chỉ có `.gitkeep`. Không có `program_slug` nào |
| 9 | `reviews/CROSS.md` | ✅ | có, 9 dòng |
| 10 | `reviews/RECONCILE.md` | ✅ | có, 9 dòng |
| 11 | `reviews/BLIND.md` | ✅ | có, 14 dòng |
| 12 | `ADMIN/ROSTER.md` | ✅ | có, 41 dòng |
| 13 | `ADMIN/ASSIGNMENTS.md` | ✅ | có, 26 dòng |
| 14 | `ADMIN/LOG.md` | ✅ | có, 11 dòng |
| 15 | `ADMIN/DISSENT.md` | ✅ | có, 8 dòng |
| 16 | `ADMIN/SUMMARY.md` | ✅ | có, 23 dòng |

**Tỉ lệ khớp: 12/16 mục đạt, 1 mục một phần, 3 mục thiếu.**

## 3. Kết luận: THIẾU / SAI cụ thể

### 3.1 `INDEX.md` liệt kê file KHÔNG tồn tại (link chết)

- `INDEX.md` dòng 19: `| 11 | reviews/AUDIT.md | Auditor2 | Kiểm toán | ⏳ chờ dựng | Người dùng |`
- Kiểm chứng: `ls reviews/` → chỉ có `BLIND.md`, `CROSS.md`, `RECONCILE.md`.
- Kết luận: **`reviews/AUDIT.md` chưa tồn tại.** `ADMIN/ASSIGNMENTS.md` dòng T7 ghi sản phẩm
  phải là `reviews/AUDIT.json` + `reviews/AUDIT.md` ⇒ **`AUDIT.json` cũng chưa có và thậm chí
  chưa được liệt kê trong INDEX.md** (lệch giữa hai tài liệu Admin).
- **Ai sửa:** Auditor2 (territory `reviews/AUDIT.*`) — **tôi không ghi vào `reviews/**`.**

### 3.2 `INDEX.md` thiếu 21 file so với cây thật

`INDEX.md` có 11 dòng; `git ls-files` có 32 file. Chênh lệch **21 file** không được liệt kê,
gồm toàn bộ `agents/*/README.md`, toàn bộ `agents/*/tasks/.gitkeep`, `rooms/**`,
`research/.gitkeep`, `security/.gitkeep`, `reviews/.gitkeep`, `.gitignore`, `ADMIN/.gitkeep`.
→ Đã khắc phục ở bản `INDEX.md` mới (xem mục 4).

### 3.3 Thiếu tài liệu giải thích thư mục trong `rooms/`

- `rooms/ab1-478d-cfa7/` **không có `README.md`** ⇒ người mới vào không biết `raw/` khác `digest/` thế nào.
- `rooms/ab1-478d-cfa7/digest/` **không có `README.md`** ⇒ **không có quy trình** chuyển
  `raw/*.jsonl` → digest. Đây là khoảng trống nghiêm trọng nhất trong territory của tôi.
- → Đã khắc phục ở T1 (xem mục 4).

### 3.4 Chưa có `research/<topic_slug>/` và `security/<program_slug>/<finding_id>/`

Đây là **thiếu sót có chủ ý, KHÔNG phải lỗi của Admin**, và **tôi cố ý không tự tạo**:

- Cả hai đường dẫn đều yêu cầu một `<slug>` **cụ thể, có thật** (tên đề tài / tên chương trình bounty).
- Hiện **chưa có đề tài nào được chọn** và **chưa có chương trình bounty nào được xác lập scope**.
- Nếu tôi tự bịa slug (ví dụ `research/example-topic/`) thì tôi đã **tạo ra cấu trúc giả** —
  vi phạm trực tiếp luật D-004 (CẤM BỊA). Một thư mục rỗng mang slug bịa còn tệ hơn không có,
  vì agent sau sẽ tưởng đề tài đó đã tồn tại.
- Đồng thời `research/**` và `security/**` **nằm ngoài territory T1 của tôi** (xem
  `ADMIN/ASSIGNMENTS.md`: T2 thuộc ResearchLead, T3–T5 thuộc BountyRecon/ExploitDeep/ForensicsMal).

⇒ **Cần Admin quyết định:** hoặc (a) giao slug thật cho tôi để tôi dựng kèm `README.md` mỗi thư mục,
hoặc (b) chấp nhận hoãn tới khi T2/T3 sinh slug thật, và ghi nhận mục 16 cấu trúc chuẩn là
"chờ slug" chứ không phải "đạt". **Tôi không tự quyết thay Admin.**

## 4. Đã khắc phục trong T1 (trong territory của tôi)

| Khiếm khuyết | Xử lý | Artifact |
|---|---|---|
| `INDEX.md` thiếu 21 file + 1 link chết | Viết lại bảng đầy đủ, đối chiếu `git ls-files` | [`INDEX.md`](../../../../INDEX.md) |
| `rooms/ab1-478d-cfa7/` không có README | Tạo tài liệu mục đích thư mục | [`rooms/ab1-478d-cfa7/README.md`](../../../../rooms/ab1-478d-cfa7/README.md) |
| `digest/` không có quy trình | Tạo quy trình raw → digest | [`rooms/ab1-478d-cfa7/digest/README.md`](../../../../rooms/ab1-478d-cfa7/digest/README.md) |
| `agents/docwriter/README.md` thiếu ngày + tác giả | Bổ sung metadata | [`agents/docwriter/README.md`](../../README.md) |
| Không có hồ sơ task | Tạo hồ sơ T1 | [`agents/docwriter/tasks/T1/`](.) |

## 5. Chưa khắc phục — chuyển Admin (ngoài territory DocWriter)

| # | Vấn đề | Territory đúng | Đề nghị |
|---|---|---|---|
| 1 | `reviews/AUDIT.md` + `reviews/AUDIT.json` chưa tồn tại, đang được INDEX tham chiếu | Auditor2 | Tạo file, hoặc gỡ khỏi INDEX nếu hoãn |
| 2 | `agents/*/README.md` (6/7 file) thiếu ngày + tác giả | Admin (khung) | Bổ sung metadata, hoặc cho phép chủ sở hữu tự bổ sung |
| 3 | `research/<topic_slug>/`, `security/<program_slug>/<finding_id>/` chưa có slug thật | Admin quyết | Xem mục 3.4 |
| 4 | Chưa có `SOURCES.md` nào trong repo | ResearchLead (T2) | Sẽ phát sinh ở T2; chưa có gì để kiểm DOI/URL |

## 6. Giới hạn của tài liệu này

- Tôi **không** kiểm nội dung kỹ thuật, không chấm điểm chất lượng khoa học của bất kỳ file nào.
- Mọi số liệu ở đây lấy trực tiếp từ output lệnh ở mục 1. Chỗ nào tôi suy luận đều ghi rõ.
- **Tài liệu này chưa được kiểm định.** Reviewer1 phải kiểm độc lập trước khi Admin merge.
