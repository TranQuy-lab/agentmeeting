# MANIFEST — dữ liệu thô trong `rooms/ab1-478d-cfa7/raw/`

**Người lập:** DocWriter (`ag_da78519d`) · **Ngày lập:** `2026-10-01` theo `timestamp` của dữ liệu thô; tài liệu kho ghi `2025-10-01` ⇒ **lệch, chưa xác minh — xem mục 4**
**Task:** T1 · **Nhánh:** `agent/doc-writer/T1`
**Luật:** Thư mục này chứa **bằng chứng gốc**. **CẤM sửa, CẤM xoá, CẤM biên tập** nội dung file trong đây.

---

## 1. Lệnh đã dùng để xuất dữ liệu (tái lập được)

```bash
python3 /home/noble-tran/agent-meet_skill/run.py \
  --session ab1-478d-cfa7 --as "DocWriter" \
  history --cap 500 --json
```

Đầu ra là một **mảng JSON**. DocWriter chuyển sang **JSONL** bằng cách: **mỗi phần tử của mảng
thành đúng một dòng**, giữ **nguyên văn** mọi trường, chỉ sắp xếp thứ tự khoá (`sort_keys=True`)
và **không** đổi, thêm, hay bớt bất kỳ nội dung nào. Đây là thao tác **đổi cách mã hoá**,
không phải biên tập.

Trường có trong mỗi dòng (lấy từ chính dữ liệu, không suy đoán):
`agent_id`, `agent_name`, `content`, `message_id`, `read_by`, `timestamp`.

## 2. Danh mục file thô

| # | File | Số bản ghi | Khoảng `message_id` | SHA256 | Kích thước |
|---|---|---|---|---|---|
| 1 | `raw-msg-0001-0012.jsonl` | 12 | 1 → 12 | `66ac7183fadedd481ccc839e2c82ef05cbdef568065b11d4f8e546bc27e88295` | 44.186 B |

**Ngày xuất:** `2026-10-01T13:49Z` theo `timestamp` trong dữ liệu (xem mục 5).

Cách kiểm lại tính toàn vẹn:

```bash
sha256sum rooms/ab1-478d-cfa7/raw/raw-msg-0001-0012.jsonl
# phải ra đúng 66ac7183fadedd481ccc839e2c82ef05cbdef568065b11d4f8e546bc27e88295
python3 -c "import json;print(len([json.loads(l) for l in open('rooms/ab1-478d-cfa7/raw/raw-msg-0001-0012.jsonl')]))"
# phải ra 12
```

## 3. Kiểm tra rò rỉ bí mật — ĐÃ CHẠY, kết quả âm tính

Trước khi ghi file thô vào repo, DocWriter đã quét nội dung:

```bash
grep -oniE 'agent_token|bearer [a-z0-9._-]{8,}|creds\.json|api[_-]?key|password|secret|-----BEGIN|[a-f0-9]{40,}|eyJ[A-Za-z0-9._-]{20,}' room.jsonl
```

| Mẫu quét | Số khớp | Kết luận |
|---|---|---|
| Chuỗi hex ≥ 40 ký tự (token/API key) | **0** | không có |
| Chuỗi dạng JWT (`eyJ...`) | **0** | không có |
| `token=<giá trị>` | **0** | không có |
| `-----BEGIN` (khoá riêng) | **0** | không có |
| Từ khoá `agent_token`, `password`, `creds.json` | 4 | **chỉ là chữ trong câu văn**, không phải bí mật — xem mục 3.1 |

### 3.1 Bốn chỗ khớp từ khoá — giải trình từng chỗ (không giấu)

| `message_id` | Từ khoá | Ngữ cảnh nguyên văn (rút gọn) | Đánh giá |
|---|---|---|---|
| 4 | `password` | "…git (SSH **passwordless**), Python venv…" — ZCode mô tả công cụ | Không phải bí mật |
| 9 | `creds.json` | "Credential ở `~/.agentmeet/…/docwriter/**creds.json**` (quyền 600) — cam kết không in ra" — DocWriter nêu **đường dẫn**, không nêu nội dung | Không phải bí mật (chỉ là tên file) |
| 10 | `agent_token` | "…grep -iE \"**agent_token**\|creds\|password\|api[_-]?key\"" — Reviewer1 mô tả **lệnh grep** của mình | Không phải bí mật |
| 10 | `password` | cùng dòng lệnh grep trên | Không phải bí mật |

⇒ **Không có token, khoá, mật khẩu hay dữ liệu cá nhân thật nào trong file thô.** Đã đối chiếu
`.gitignore` (đã chặn `*creds*.json`, `*token*`, `.env`, `*.pem`, `*.key`) — file thô này
**không** khớp mẫu bị chặn nào, và cũng **không chứa** nội dung thuộc nhóm bị chặn.

## 4. Phát hiện lệch NGÀY giữa tài liệu và dữ liệu thô — chưa xác minh

| Nguồn | Ngày ghi |
|---|---|
| `README.md`, `ADMIN/*.md`, `rooms/…/directives.md` (do Admin viết) | **2025-10-01** |
| Trường `timestamp` trong dữ liệu thô của phòng | **2026-10-01** (`13:23Z` → `13:48Z`) |

**DocWriter KHÔNG tự phán ngày nào đúng.** Đây là **dị bản giữa hai nguồn**, và theo luật D-004
tôi ghi thẳng `chưa xác minh`. **Admin cần phân xử** và chốt một mốc thời gian chuẩn cho kho,
vì từ đây mọi digest sẽ phải ghi ngày.

Để tránh chọn sai bên, tên file thô dùng **khoảng `message_id`** (`raw-msg-0001-0012`),
**không** dùng ngày.

## 5. Giới hạn

- `--cap 500` là giới hạn xuất của CLI; hiện chỉ có 12 tin nên chưa chạm trần. Khi phòng vượt
  500 tin, phải xuất **nhiều khối** và ghi thêm dòng vào bảng mục 2.
- File thô là **ảnh chụp tại thời điểm xuất**. Nếu `read_by` thay đổi sau đó, file này **không**
  tự cập nhật — phải xuất khối mới, **không được sửa file cũ**.
- Manifest này **chưa được Reviewer1 kiểm định**.
