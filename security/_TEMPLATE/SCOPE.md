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

---

## BẢNG TÀI SẢN MẪU — bắt buộc có đủ cột

> **Vì sao có mục này** (khe hở do `Reviewer1` phát hiện ở T39): mẫu này **quy định TRƯỜNG**
> nhưng trước đây **không có BẢNG MẪU** minh hoạ cách bày cột. Người viết sau có thể
> **"có nhắc `archived_at`"** mà **không nhúng cột vào bảng tài sản** ⇒ **thoả mãn trên giấy,
> không có trong dữ liệu**. Bảng mẫu dưới đây chặn tái diễn ở **tầng thiết kế**.

| # | Asset / identifier | `asset_type` | `eligible_for_submission` | `eligible_for_bounty` | **`archived_at`** | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | `example.com` | URL | true | true | `null` | Đang hiệu lực |
| 2 | `*.example.com` | WILDCARD | true | true | `null` | Đang hiệu lực |
| 3 | `legacy.example.com` | URL | true | false | `2023-05-08T10:11:33.083Z` | Có `archived_at` ⇒ **đã nghỉ hưu**. Hiệu lực: **CHƯA XÁC MINH** (`DISSENT-12`). **KHÔNG suy ra "ngoài scope"** |
| 4 | `old.example.net` | URL | true | true | `2022-03-01T17:47:43.944Z` | Có `archived_at` ⇒ **đã nghỉ hưu**. Hiệu lực: **CHƯA XÁC MINH** |

**Luật đọc bảng — BẮT BUỘC:**
```text
0. (ĐÍNH CHÍNH — Reviewer1 T42) Cột "Ghi chú" của bảng MẪU NÀY trước đây ghi "ĐÃ NGHỈ HƯU —
   không được coi là target đang mở", MÂU THUẪN với luật 3 ngay dưới. Bảng mẫu đang DẠY đúng
   cái suy luận mà D-026 CẤM ⇒ sẽ TÁI SINH lỗi ở phiên sau. Đã sửa. Bảng mẫu cũng phải tuân luật.
1. Cột `archived_at` PHẢI có trong MỌI bảng tài sản. Thiếu cột = bảng KHÔNG ĐẠT.
2. archived_at = null      -> bản ghi ĐANG HIỆU LỰC.
   archived_at != null     -> bản ghi ĐÃ NGHỈ HƯU (dùng để LỌC, không để suy đoán phạm vi).
3. CẤM kết luận "ngoài scope" từ archived_at. Chỉ được nói:
   "bảng thiếu/đủ chiều archived_at" và "hiệu lực của bản ghi đã nghỉ hưu: CHƯA XÁC MINH".
4. `eligible_for_submission` / `eligible_for_bounty` là HAI trường ĐỘC LẬP — cấm suy ra nhau.
5. `asset_type` WILDCARD và URL là HAI bản ghi KHÁC NHAU — cấm gộp (bài học T31: gitlab.net
   apex nghỉ hưu 2020-10-05 nhưng *.gitlab.net wildcard CÒN HIỆU LỰC).
6. Bảng trong `EVIDENCE/**` là CAPTURE (trích nguyên văn) — CẤM SỬA. Muốn có archived_at thì
   CHỤP LẠI thành <tên>_v2 kèm ngày chụp, GIỮ NGUYÊN bản gốc (D-026).
```
