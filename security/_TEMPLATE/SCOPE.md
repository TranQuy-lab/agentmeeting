# SCOPE — <Tên chương trình>

**Mẫu bắt buộc.** Mọi `security/<program_slug>/SCOPE.md` phải có đủ các mục dưới.

| Trường | Bắt buộc | Vì sao |
|---|---|---|
| Tên chương trình + URL chính sách | ✅ | Truy vết |
| Ngày fetch + mã HTTP | ✅ | Bằng chứng thô |
| **`archived_at` của MỌI asset** | ✅ **BẮT BUỘC** | **Bài học M-01 (Auditor2 T24):** hai kiểm định viên độc lập cùng truy vấn một tập trường thì **cùng mù một chiều dữ liệu**. Bỏ `archived_at` ⇒ sinh ra "xung đột scope" giả giữa chính sách **đang hiệu lực** và bản ghi **đã nghỉ hưu** |
| Trích **NGUYÊN VĂN** in-scope | ✅ | Cơ sở pháp lý |
| Trích **NGUYÊN VĂN** out-of-scope | ✅ | Cơ sở pháp lý |
| Quy định cấm (rate limit, không DoS…) | ✅ | Cơ sở pháp lý |
| Mức thưởng công bố | ⬜ nếu có | Đánh giá giá trị |

```text
[QUY TẮC CHỐNG MÙ MỘT CHIỀU — D-013]
Khi phát hiện tài sản nằm ở CẢ HAI phía scope, PHẢI truy vấn thêm:
  1. archived_at        (bản ghi còn hiệu lực hay đã nghỉ hưu?)
  2. asset_type         (WILDCARD vs URL vs IP — khác loại thì có thể không phải xung đột)
  3. eligible_for_bounty / eligible_for_submission  (hai trường ĐỘC LẬP, không suy ra nhau)
  4. ngày cập nhật chính sách
Chỉ kết luận "xung đột" sau khi đã loại trừ cả bốn chiều. Ghi rõ đã truy vấn hay chưa.
```
