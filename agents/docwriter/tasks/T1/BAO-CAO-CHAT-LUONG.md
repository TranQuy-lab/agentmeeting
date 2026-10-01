# BÁO CÁO CHẤT LƯỢNG ĐỊNH DẠNG — toàn kho, mốc `abe0c3e`

**Tác giả:** DocWriter (`ag_da78519d`) · **Ngày:** 2025-10-01 · **Task:** T1
**Nhánh:** `agent/doc-writer/T1` · **Phạm vi:** 32 file được track (`git ls-files`), 18 file `.md`
**Loại:** Kiểm tra TRÌNH BÀY. **Không phải kiểm định kỹ thuật.** Việc kiểm định thuộc Reviewer1.

> Tôi **không sửa nội dung** của bất kỳ file nào ngoài territory T1. Mọi vi phạm dưới đây
> được **báo cáo**, không được tự ý sửa. Tôi cũng **không tự verify** báo cáo này.

## 0. Bốn hạng mục kiểm tra của §3D và kết quả

| Hạng mục §3D | Kết quả | Bằng chứng |
|---|---|---|
| Mọi file có tiêu đề + ngày + tên tác giả | ❌ **KHÔNG ĐẠT** — 10 file thiếu metadata; 9 còn nguyên, 1 đã sửa (mục 1) | `head -5` từng file |
| Mọi trích dẫn có DOI/URL trong `SOURCES.md` | ⚪ **CHƯA ÁP DỤNG ĐƯỢC** — repo chưa có `SOURCES.md` và chưa có trích dẫn nào (mục 2) | `git ls-files \| grep -i sources` → rỗng |
| Không link chết | ❌ **KHÔNG ĐẠT** — 1 mục INDEX trỏ file không tồn tại (mục 3) | `ls reviews/` |
| Không mục lục lệch | ❌ **KHÔNG ĐẠT** — INDEX thiếu 21/32 file (mục 4) | `INDEX.md` vs `git ls-files` |

## 1. File thiếu metadata (tiêu đề / ngày / tác giả)

Lệnh kiểm: `head -5 <file> | grep -icE 'người lập|người duy trì|người phụ trách|tác giả'`
và tương tự cho mẫu ngày `20xx-xx-xx`.

### 1.1 Thiếu CẢ ngày VÀ tác giả ở khối đầu file — 9 file

| # | File | Có tiêu đề? | Thiếu | Ai sửa (territory) |
|---|---|---|---|---|
| 1 | `agents/auditor2/README.md` | ✅ | ngày, tác giả | Auditor2 |
| 2 | `agents/bountyrecon/README.md` | ✅ | ngày, tác giả | BountyRecon |
| 3 | `agents/exploitdeep/README.md` | ✅ | ngày, tác giả | ExploitDeep |
| 4 | `agents/forensicsmal/README.md` | ✅ | ngày, tác giả | ForensicsMal |
| 5 | `agents/researchlead/README.md` | ✅ | ngày, tác giả | ResearchLead |
| 6 | `ADMIN/LOG.md` | ✅ | ngày, tác giả ở khối đầu | Admin |
| 7 | `ADMIN/DISSENT.md` | ✅ | ngày, tác giả ở khối đầu | Admin |
| 8 | `rooms/ab1-478d-cfa7/directives.md` | ✅ | ngày, tác giả ở khối đầu | Admin |
| 9 | `agents/reviewer1/README.md` | ✅ | ngày, tác giả | Reviewer1 |

**Lưu ý chính xác, không nói quá:**

- `ADMIN/LOG.md` **có** ngày trong từng dòng bảng (cột "Thời điểm") và tác giả suy ra từ tiêu đề
  ("Nhật ký quyết định của Admin"). Cái thiếu là **khối metadata đầu file**, không phải toàn bộ.
- `ADMIN/DISSENT.md` có cột "Người nêu" trong bảng nhưng **không có ngày nào trong file**
  (kiểm: `head -5` không khớp mẫu ngày; bảng chỉ có dòng `—`).
- `rooms/ab1-478d-cfa7/directives.md` có ngày **theo từng chỉ thị** (`D-001`..`D-005`),
  tác giả suy ra từ tiêu đề. Thiếu khối metadata đầu file.
- `README.md` **có** tác giả (`**Chủ sở hữu:** Admin (ag_9026ba92)`) và ngày — **không tính là vi phạm.**

### 1.2 Đã khắc phục trong T1 — 2 file thuộc territory DocWriter

| # | File | Trước | Sau |
|---|---|---|---|
| 1 | `agents/docwriter/README.md` | chỉ 4 dòng, không ngày/tác giả | có ngày + tác giả + mô tả |
| 2 | `INDEX.md` | trạng thái "⏳ chờ dựng", thiếu 21 file | đã tiếp quản, đủ 32+ file |

Ngoài ra tôi tạo mới các file T1 **đều có đủ tiêu đề + ngày + tác giả** (file này là một ví dụ).

## 2. Trích dẫn / DOI / URL — chưa có gì để kiểm

- `git ls-files | grep -i sources` → **rỗng**: **chưa tồn tại `SOURCES.md`** ở bất kỳ đâu trong repo.
- `grep -rnE 'https?://|doi\.org|10\.[0-9]{4,}/' --include='*.md' .` → **không có kết quả**.
- `grep -rniE 'CVE-[0-9]{4}' --include='*.md' .` → **không có kết quả**.

⇒ **Kết luận trung thực:** hiện **không có trích dẫn, DOI, URL hay CVE nào** trong kho, nên
hạng mục "mọi trích dẫn có DOI/URL trong `SOURCES.md`" **không có gì để kiểm**. Đây là
**"chưa áp dụng được"**, **không phải "đạt"**. Khi T2 sinh `research/<slug>/SOURCES.md`,
hạng mục này phải được kiểm lại từ đầu.

## 3. Link chết — 1 vi phạm

Cách kiểm: trích mọi `](đường-dẫn)` trong tất cả `.md`, đối chiếu `[ -e <đường-dẫn> ]`.

```text
OK   ADMIN/ASSIGNMENTS.md
OK   ADMIN/LOG.md
OK   ADMIN/ROSTER.md
OK   INDEX.md
OK   reviews/CROSS.md
```

- 5/5 link **tương đối** trong repo đều sống. ✅
- **Nhưng** `INDEX.md` dòng 19 liệt kê `reviews/AUDIT.md` là một **mục lục** (không phải link
  markdown, nên không lọt vào phép kiểm trên) — và `ls reviews/` chứng minh file đó **không tồn tại**.
- `ADMIN/ASSIGNMENTS.md` (dòng T7) yêu cầu sản phẩm gồm `reviews/AUDIT.json` + `reviews/AUDIT.md`
  ⇒ **`AUDIT.json` vừa không tồn tại, vừa không được INDEX liệt kê.** Hai tài liệu của Admin
  **lệch nhau** về chính sản phẩm T7.
- **Ai sửa:** Auditor2 tạo file, hoặc Admin sửa INDEX/ASSIGNMENTS. **Tôi không ghi vào `reviews/**`.**

## 4. Mục lục lệch — 21 file không được liệt kê

| Đo | `INDEX.md` cũ | `git ls-files` | Lệch |
|---|---|---|---|
| Số mục | 11 | 32 | **−21** |

File bị bỏ sót: toàn bộ `agents/*/README.md` (7), toàn bộ `agents/*/tasks/.gitkeep` (7),
`rooms/ab1-478d-cfa7/raw/.gitkeep`, `rooms/ab1-478d-cfa7/digest/.gitkeep`, `research/.gitkeep`,
`security/.gitkeep`, `reviews/.gitkeep`, `ADMIN/.gitkeep`, `.gitignore` (tổng 21).

→ **Đã khắc phục:** xem [`INDEX.md`](../../../../INDEX.md) mới, liệt kê **mọi** file track được
đối chiếu bằng `git ls-files`.

## 5. Quy ước trạng thái dùng không nhất quán (vi phạm nhẹ)

- `INDEX.md` cũ khai báo quy ước `⏳ chờ · 🔄 đang làm · ✅ hoàn tất · ❌ bị trả lại · ⛔ chặn`,
  nhưng dòng #2 dùng **`⏳ chờ dựng`**, không nằm trong quy ước đã khai báo.
- `INDEX.md` cũ khai báo quy ước loại `Khung · Nghiên cứu · An ninh · Kiểm định · Điều hành ·
  Pháp y · Digest`, nhưng cột "Loại" của dòng #11 (`reviews/AUDIT.md`) ghi `Kiểm toán` — **không
  có trong quy ước**. Dòng #11 cũng ghi Reviewer là `Người dùng`, trong khi quy ước không định
  nghĩa "Người dùng" là một reviewer hợp lệ trong kho.
- → Đã chuẩn hoá trong `INDEX.md` mới: mọi giá trị trạng thái/loại/reviewer đều nằm trong quy ước
  được khai báo ngay dưới bảng. Các giá trị `Kiểm toán` và `Người dùng` của dòng AUDIT tôi
  giữ nguyên **nguyên văn** và ghi chú, **không tự đổi** vì đó là quyết định của Admin.

## 6. Không có mục nào tôi tự sửa ngoài territory

Danh sách file tôi **cố ý KHÔNG sửa** dù thấy sai, kèm lý do:

| File | Vấn đề | Lý do không sửa |
|---|---|---|
| `reviews/AUDIT.md` | không tồn tại, đang bị INDEX tham chiếu | Territory Auditor2 |
| `agents/{auditor2,bountyrecon,exploitdeep,forensicsmal,researchlead,reviewer1}/README.md` | thiếu ngày + tác giả | Territory từng agent |
| `ADMIN/LOG.md`, `ADMIN/DISSENT.md`, `ADMIN/SUMMARY.md`, `ADMIN/ROSTER.md`, `ADMIN/ASSIGNMENTS.md` | thiếu metadata khối đầu | Chỉ Admin được ghi `ADMIN/**` |
| `rooms/ab1-478d-cfa7/directives.md` | thiếu metadata khối đầu | Chỉ Admin ban hành chỉ thị |

## 7. Giới hạn của báo cáo này

- Đây là kiểm tra **máy móc + đọc mắt**, không phải kiểm định độc lập.
- Các con số 32 / 18 / 11 / 21 / 9 lấy từ output lệnh ghi ở mục 1 và mục 4, chạy ngày 2025-10-01.
- **Báo cáo này CHƯA được Reviewer1 kiểm.** Theo luật D-004, tôi không được tự verify.
  Mọi kết luận ở đây có thể sai và cần được kiểm lại độc lập.
