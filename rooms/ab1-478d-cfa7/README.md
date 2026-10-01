# PHÒNG `ab1-478d-cfa7` — hồ sơ dữ liệu phòng họp

**Người lập:** DocWriter (`ag_da78519d`) · **Ngày:** 2025-10-01 · **Task:** T1
**Nhánh:** `agent/doc-writer/T1` · **Territory:** `rooms/**` (DocWriter, Admin)
**Trạng thái:** khung đã dựng, chưa có dữ liệu thô

---

## 1. Thư mục này để làm gì

Phòng AgentMeet `ab1-478d-cfa7` là nơi 8 agent trao đổi. **Phòng có giới hạn dung lượng**
(ghi nhận trong `ADMIN/SUMMARY.md` mục 3: "Phòng giới hạn 500 tin, 8 agent poll liên tục sẽ
đầy nhanh"). Vì vậy **transcript của phòng KHÔNG được phép ở lại duy nhất trong phòng** —
nó phải được sao lưu xuống kho Git dưới dạng dữ liệu thô, rồi cô đọng lại thành digest.

Thư mục `rooms/ab1-478d-cfa7/` là **bộ nhớ dài hạn** của phòng: nếu phòng mất tin, kho vẫn còn.

## 2. Cấu trúc và ai được ghi

| Đường dẫn | Nội dung | Ai được ghi |
|---|---|---|
| `raw/` | Dữ liệu thô, **nguyên văn**, không biên tập — mỗi file `.jsonl` là một khối tin lấy từ phòng | DocWriter, Admin |
| `digest/` | Bản cô đọng **có cấu trúc** từ `raw/`, kèm quy trình tại [`digest/README.md`](digest/README.md) | DocWriter |
| `directives.md` | Chỉ thị chính thức của Admin (`D-001`..`D-005`) — **nguồn sự thật về mệnh lệnh** | **Chỉ Admin** |
| `README.md` | File này — giải thích mục đích thư mục | DocWriter |

## 3. Phân biệt `raw/` và `digest/` — điều quan trọng nhất

| | `raw/` | `digest/` |
|---|---|---|
| Bản chất | **Nguyên văn**, sao chép y nguyên | **Cô đọng**, có cấu trúc, do DocWriter viết |
| Được sửa? | **KHÔNG BAO GIỜ.** Sửa raw = phá hủy bằng chứng | Có, nhưng phải ghi rõ lần sửa |
| Vai trò | **Bằng chứng gốc** để đối chiếu | **Công cụ tra cứu** cho người đọc |
| Khi mâu thuẫn | **`raw/` thắng.** Digest sai thì sửa digest | — |
| Có thể dẫn nguồn? | Có — đây là nguồn gốc | Chỉ dẫn tới `raw/`, không tự nhận là nguồn |

> **Luật bất biến:** một khẳng định trong `digest/` mà không truy được về dòng cụ thể trong
> `raw/` là **khẳng định không có bằng chứng**. Theo luật D-004, nó phải bị gỡ hoặc đánh dấu
> `chưa xác minh`. DocWriter **không được** thêm thông tin không có trong `raw/`.

## 4. Trạng thái hiện tại (đã kiểm chứng, không suy đoán)

Lệnh kiểm và kết quả thô:

```bash
cd /home/noble-tran/agentmeeting-docwriter
git ls-files rooms/
# rooms/ab1-478d-cfa7/digest/.gitkeep
# rooms/ab1-478d-cfa7/directives.md
# rooms/ab1-478d-cfa7/raw/.gitkeep
ls rooms/ab1-478d-cfa7/raw/
# (chỉ có .gitkeep)
```

⇒ **`raw/` hiện KHÔNG có file `.jsonl` nào.** Chưa có dữ liệu thô để chuyển thành digest.
Quy trình ở [`digest/README.md`](digest/README.md) do đó là **quy trình đề xuất, CHƯA được
thực nghiệm lần nào**. Nói cách khác: nó chưa được chứng minh là chạy được.

## 5. Việc còn thiếu — chuyển Admin

| # | Việc | Vì sao chưa làm được |
|---|---|---|
| 1 | Có ít nhất một file `raw/*.jsonl` thật | Cần một lệnh xuất transcript từ phòng; tôi chưa có chỉ thị cụ thể về định dạng xuất, và **không tự bịa dữ liệu phòng** |
| 2 | Chốt định dạng `.jsonl` | Xem [`digest/README.md`](digest/README.md) mục 3 — tôi đề xuất định dạng nhưng **cần Admin phê duyệt** vì đây là hợp đồng dữ liệu giữa các agent |
| 3 | Chỉ định ai chạy việc xuất transcript định kỳ | Chưa được phân công trong `ADMIN/ASSIGNMENTS.md` |

## 6. Giới hạn của tài liệu này

- Tài liệu mô tả **cấu trúc và quy trình**, không chứa kết luận kỹ thuật nào.
- Mọi con số ở mục 4 lấy từ output lệnh ghi ngay trên đó.
- **Chưa được Reviewer1 kiểm định.** Tôi không tự verify theo luật D-004.
