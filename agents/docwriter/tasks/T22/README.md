# T22 — Cập nhật `INDEX.md` theo mốc `main` hiện tại

**Tác giả:** DocWriter (`ag_da78519d`) · **Ngày:** 2026-10-01 · **Nhánh:** `agent/doc-writer/T22`
**Mốc đối chiếu:** `main` @ `0f41ebb` · **Số file đếm được:** **157** (`git ls-files | wc -l`)
**Nguồn lệnh:** D-019 §2 (msg #102) · **Trạng thái:** chờ Reviewer1 kiểm định

---

## 1. Đã làm

| # | Việc | Kết quả |
|---|---|---|
| 1 | Đếm lại số file bằng lệnh thật | **157** — khớp con số Admin nêu, **nhưng do DocWriter tự đếm**, không chép |
| 2 | Viết lại bảng §2 `INDEX.md` theo `git ls-files` | **157 dòng dữ liệu**, liên tục, không dòng trống cắt giữa |
| 3 | Lấy **tác giả** từ commit thêm file lần đầu | `git log --diff-filter=A --format=%an -- <file>` (lấy dòng **cũ nhất**) |
| 4 | Giữ nguyên **3 mục Admin đã vá** ở đầu `INDEX.md` | chốt ngày `2026-10-01`; bản gốc Admin viết ở `abe0c3e`; cảnh báo phạm vi |
| 5 | Kiểm **link chết** trên toàn bộ 71 file `.md` | **7 kết quả**, phân loại ở §3 |
| 6 | Kiểm **tham chiếu tới đường dẫn không tồn tại** | **7 đường dẫn**, phân loại ở §3 |
| 7 | Kiểm **mục lục lệch** | bảng ↔ `git ls-files`: khớp **157/157**, không thiếu không thừa |

## 2. Cách lập bảng (để Reviewer1 tái lập được)

> ⚠️ **Nhánh `agent/doc-writer/T22` có 158 file, không phải 157** — vì T22 **thêm 1 file**
> (`agents/docwriter/tasks/T22/README.md`). Bảng mô tả **mốc `main@0f41ebb` = 157 file**, nên mọi
> lệnh dưới đây **trỏ vào mốc `$M`**, không trỏ vào nhánh. Lần đầu DocWriter viết `git ls-files | wc -l`
> và tự phát hiện lệnh đó **sẽ ra 158** khi Reviewer1 chạy trên nhánh — đã sửa trước khi báo.

```bash
cd /home/noble-tran/agentmeeting-docwriter
M=0f41ebb                                # mốc của bảng
git ls-tree -r --name-only $M | wc -l    # 157
# danh sách file:
git ls-tree -r --name-only $M
# tác giả (commit THÊM file lần đầu — git log mới->cũ nên lấy dòng CUỐI):
git log --diff-filter=A --format='%h|%an' -- <file> | tail -1
# sửa cuối (để suy task):
git log -1 --format='%h|%s' -- <file>
```

**Suy trạng thái:** `✅ đã nghiệm thu (lớp 1)` nếu task của commit **sửa cuối** nằm trong danh sách
nghiệm thu của `ADMIN/SUMMARY.md` §1: `T1 T3 T6 T7 T11 T15 T16 T17 T19 T20`. **Không** đọc nội dung file để chấm.

## 3. Phát hiện mới của T22 (chi tiết + cách kiểm ở `INDEX.md` §4)

| # | Phát hiện | Mức | Ai sửa |
|---|---|---|---|
| 1 | `ADMIN/SUMMARY.md` dẫn **3 đường dẫn bằng chứng của T5 KHÔNG tồn tại trên `main`** (T5 chưa merge) ⇒ cột "Bằng chứng" của 2 dòng rủi ro **không kiểm chứng được từ repo** | **Cao** | Admin |
| 2 | **3 link tương đối sai độ sâu** trong `agents/bountyrecon/tasks/T3/CANDIDATES.md` (`../../../security/` → phải `../../../../security/`); `ls -d agents/security` không tồn tại ⇒ link **chết** | Trung bình | BountyRecon |
| 3 | **3 link thiếu `https://`** trong `agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md` — **trích nguyên văn** từ chính sách GitHub; sửa sẽ phá tính nguyên văn | Thấp | Admin quyết |
| 4 | **16 file** (11 của `[T2]`, 5 của `[T4]`) **đã ở trên `main`** nhưng T2/T4 **không** có trong danh sách nghiệm thu `SUMMARY.md` §1, và `ASSIGNMENTS.md` vẫn ghi T2 `⏳ todo` / T4 `⏸ chờ T3` | Trung bình | Admin làm rõ |

**Ghi chú về phát hiện #2:** T3 **đã PASS lớp 1 (T14)**, nhưng T14 kiểm **nội dung `SCOPE.md`**,
**không** kiểm link trong `CANDIDATES.md`. Đây là **khoảng trống phạm vi kiểm định**,
**không** phải Reviewer1 làm sai.

## 4. Giới hạn — nói thẳng

1. Bảng dựa trên **Git**, **không** dựa trên việc đọc 157 file. File có thể hỏng nội dung mà vẫn `✅`.
2. **Tác giả = người commit**, không chắc là người viết nội dung.
3. Cột "Loại"/"Chủ trì" là **phân loại theo đường dẫn** của DocWriter.
4. Bảng khoá ở mốc `0f41ebb`; `main` đang tiến nên bảng sẽ lạc hậu.
5. **Chưa được Reviewer1 kiểm định** — theo D-004, DocWriter **không** tự verify.

## 5. Lệnh kiểm chứng bảng §2 (không đếm lẫn bảng khác, không lẫn file mới của T22)

```bash
cd /home/noble-tran/agentmeeting-docwriter
M=0f41ebb
# chỉ đếm trong §2, từ tiêu đề "## 2." tới "### 2.1"
awk '/^## 2\. Bảng/{f=1} /^### 2\.1/{f=0} f' INDEX.md | grep -c '^| [0-9]'   # phải ra 157
# đối chiếu từng đường dẫn trong bảng với MỐC 0f41ebb (không thiếu, không thừa):
awk '/^## 2\. Bảng/{f=1} /^### 2\.1/{f=0} f' INDEX.md \
  | sed -n 's/^| [0-9]* | `\([^`]*\)`.*/\1/p' | sort > /tmp/idx.txt
git ls-tree -r --name-only $M | sort > /tmp/git.txt
diff /tmp/idx.txt /tmp/git.txt && echo "KHOP 157/157"
# bảng §2 phải liên tục:
awk '/^## 2\. Bảng/{f=1} /^### 2\.1/{f=0} f' INDEX.md \
  | awk '/^\|/{n++;next} n>0 && !/^\|/ && !/^$/{print "BANG BI CAT"; exit}'   # không in gì = đạt
```

**Kết quả DocWriter đã chạy trước khi push:** `157` · `KHOP 157/157` · không in gì (bảng liên tục).
