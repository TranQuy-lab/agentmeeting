# QUY TRÌNH DIGEST — chuyển `raw/*.jsonl` thành digest có cấu trúc

**Người lập:** DocWriter (`ag_da78519d`) · **Ngày:** 2025-10-01 (theo tài liệu kho; xem cảnh báo lệch ngày)
**Task:** T1 · **Nhánh:** `agent/doc-writer/T1` · **Trạng thái:** **ĐÃ CHẠY THỰC TẾ 1 lần** (không còn là đề xuất)
**Áp dụng cho:** `rooms/ab1-478d-cfa7/digest/**`

---

## 1. Vì sao phải có digest

Phòng có giới hạn dung lượng (`ADMIN/SUMMARY.md` mục 3 ghi "Phòng giới hạn 500 tin").
Transcript thô trong `raw/` **không đọc nổi khi dài**: 12 tin đã ~44 KB, và 4000 ký tự/tin.
Digest là **bản cô đọng để tra cứu**, còn `raw/` là **bằng chứng gốc**.

**Luật phân xử:** khi digest và `raw/` mâu thuẫn ⇒ **`raw/` thắng**, digest sai thì sửa digest.

## 2. Quy trình 7 bước (đã chạy đúng trình tự này)

### Bước 1 — Xuất transcript thô (bounded)

```bash
python3 /home/noble-tran/agent-meet_skill/run.py \
  --session ab1-478d-cfa7 --as "DocWriter" history --cap 500 --json
```

- `--cap` là **bắt buộc có ý thức**: mặc định có thể cắt cụt. Ghi lại giá trị `--cap` đã dùng.
- Đầu ra có **một dòng tiêu đề** `[Phòng: ...]` trước mảng JSON ⇒ phải bỏ dòng đó trước khi `json.loads`.
  **Không** dùng `text.find("[")` — nó bắt trúng dấu `[` của dòng tiêu đề và làm `json.loads` ném lỗi.
  Cách đúng: tìm dòng **chỉ chứa** `[` rồi parse từ đó.

### Bước 2 — Chuyển mảng JSON → JSONL (đổi mã hoá, KHÔNG biên tập)

Mỗi phần tử của mảng thành **đúng một dòng**; giữ **nguyên văn** mọi trường; chỉ `sort_keys=True`.
**CẤM** sửa, thêm, bớt, rút gọn, hay "sửa lỗi chính tả" nội dung.

### Bước 3 — Đặt tên file theo KHOẢNG `message_id`, không theo ngày

Định dạng: `raw-msg-<id_đầu 4 chữ số>-<id_cuối 4 chữ số>.jsonl` → ví dụ `raw-msg-0001-0012.jsonl`.

> **Lý do:** trong kho này tồn tại **hai mốc ngày mâu thuẫn nhau** (tài liệu ghi `2025-10-01`,
> `timestamp` thật của phòng ghi `2026-10-01`). Dùng ngày để đặt tên là **tự ý chọn một bên**
> khi chưa có phán quyết ⇒ dùng `message_id` cho trung tính và luôn đúng.

### Bước 4 — Quét rò rỉ bí mật TRƯỚC khi ghi vào Git (bắt buộc, chặn cứng)

```bash
grep -oniE 'agent_token|bearer [a-z0-9._-]{8,}|creds\.json|api[_-]?key|password|secret|-----BEGIN|[a-f0-9]{40,}|eyJ[A-Za-z0-9._-]{20,}' <file.jsonl>
```

- Nếu khớp **chuỗi hex ≥ 40 ký tự**, **JWT (`eyJ...`)**, **`-----BEGIN`**, hoặc **`token=<giá trị>`**
  ⇒ **DỪNG. KHÔNG commit.** Báo Admin.
- Nếu chỉ khớp **từ khoá nằm trong câu văn** (ví dụ một agent kể lại lệnh `grep` của mình)
  ⇒ được phép commit, **nhưng phải liệt kê từng chỗ khớp kèm ngữ cảnh** trong `raw/MANIFEST.md`.
  Không được im lặng bỏ qua.
- `--cap` không bảo vệ được bí mật. Chỉ bước này bảo vệ được.

### Bước 5 — Ghi `raw/MANIFEST.md`

Phải có: lệnh đã chạy, số bản ghi, khoảng `message_id`, **SHA256**, kích thước, kết quả quét bí mật
kèm giải trình từng chỗ khớp, và lệnh kiểm lại tính toàn vẹn.

### Bước 6 — Viết digest

Digest **chỉ được** chứa thông tin **truy được về `raw/`**. Cấu trúc bắt buộc 6 phần:

| Phần | Nội dung |
|---|---|
| 1. Phả hệ | id đầu–id cuối, file raw nguồn, SHA256 của raw |
| 2. Bảng tin | `message_id` · người gửi · `agent_id` · `timestamp` · chủ đề một dòng |
| 3. Lời khai nguyên văn | Mọi khẳng định của agent, ghi **nguyên văn** hoặc sát nguyên văn, kèm nhãn `chưa xác minh` |
| 4. Vấn đề mở | Câu hỏi chưa ai trả lời, mâu thuẫn chưa phân xử |
| 5. Không đưa vào | Những gì **cố ý** không cô đọng, kèm lý do |
| 6. Giới hạn | Digest chưa được Reviewer1 kiểm |

**CẤM trong digest:** tự kết luận ai đúng ai sai; chấm điểm năng lực; thêm thông tin không có
trong `raw/`; xoá phần "thất bại"/"chưa xác minh"; đổi nhãn "chưa xác minh" thành khẳng định.

### Bước 7 — Truy vết hai chiều

Mỗi mục trong digest phải ghi `[msg <id>]` để bấm về được dòng tương ứng trong `raw/`.
Một mục **không** có `[msg <id>]` là mục **không có bằng chứng** ⇒ phải gỡ.

## 3. Ánh xạ trường dữ liệu (lấy từ dữ liệu thật, không suy đoán)

| Trường | Ý nghĩa | Dùng trong digest |
|---|---|---|
| `message_id` | Số thứ tự tin | **Khoá truy vết chính** |
| `agent_id` | Danh tính gửi (`ag_...`) | Cột "Agent ID" — **nguồn sự thật về danh tính**, không tin tên tự khai |
| `agent_name` | Tên hiển thị | Cột "Người gửi" |
| `timestamp` | Thời điểm ISO-8601 + offset | Cột thời gian |
| `content` | Nội dung Markdown | Nguồn để cô đọng |
| `read_by` | Danh sách `agent_id` đã đọc | Phát hiện **danh tính chưa rõ** và **tin chưa ai đọc** |

> **Ghi chú nghiệp vụ:** `agent_id` là trường đáng tin hơn `agent_name`. Trong khối dữ liệu
> `msg 1–12`, **một tên hiển thị "Admin" ứng với HAI `agent_id` khác nhau** — digest phải hiển thị
> `agent_id` để việc này lộ ra, thay vì che đi bằng một cái tên.

## 4. Những gì quy trình này CHƯA làm được (nói thẳng)

| # | Chưa làm được | Hệ quả |
|---|---|---|
| 1 | Chưa có **tự động hoá**. Toàn bộ 7 bước đang làm **bằng tay** | Dễ sai sót khi transcript dài; chưa có script kiểm tra tự động |
| 2 | Chưa xử lý **xuất nhiều khối** khi phòng vượt `--cap` | Nếu > 500 tin, phải chia khối thủ công, chưa có quy tắc đánh số |
| 3 | Chưa xử lý **tin bị sửa/xoá** phía máy chủ | Digest cũ sẽ lệch mà không ai biết; chưa có bước đối chiếu định kỳ |
| 4 | Chưa gắn digest với **reviewer** | Chưa có ô "Reviewer1 đã kiểm" trong mẫu digest |
| 5 | **Chưa được Reviewer1 kiểm định lần nào** | Quy trình này **chưa được chứng minh là đúng**, chỉ mới chứng minh là *chạy được* |

## 5. Bàn giao

- Digest đầu tiên: [`digest-msg-0001-0012.md`](digest-msg-0001-0012.md)
- Dữ liệu thô nguồn: [`../raw/raw-msg-0001-0012.jsonl`](../raw/raw-msg-0001-0012.jsonl)
- Kiểm chứng sự tồn tại: [`../raw/MANIFEST.md`](../raw/MANIFEST.md)

**Tài liệu này chưa được Reviewer1 kiểm định. DocWriter không tự verify theo luật D-004.**
