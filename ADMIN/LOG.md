# LOG — Nhật ký quyết định của Admin

**Luật:** Mọi quyết định điều chỉnh phải ghi kèm LÝ DO. Quyết định không giải thích = vi phạm,
Auditor2 có quyền chất vấn.

| # | Thời điểm | Quyết định | Lý do | Bằng chứng |
|---|---|---|---|---|
| 1 | 2025-10-01 | Dựng khung repo và push commit đầu tiên lên `main` | §0 kế hoạch: nếu worker vào trước, mỗi agent sẽ tự bịa một cấu trúc khác nhau | commit đầu tiên của repo |
| 2 | 2025-10-01 | Admin tự viết bản khung `README.md` + `INDEX.md` thay vì chờ DocWriter | Cần khung tồn tại trước khi clone cho worker; DocWriter sẽ tiếp quản và chuẩn hoá ở T1 | `README.md`, `INDEX.md` |
| 3 | 2025-10-01 | Giữ nguyên §4 luật cấm trong prompt của BountyRecon/ExploitDeep/ForensicsMal | Đây là ràng buộc pháp lý (Luật An ninh mạng 24/2018/QH14) và điều kiện của chương trình bounty, không phải cổng hành chính. Người dùng đã cho Admin toàn quyền quyết định phần điều phối, không miễn trừ phần pháp lý | `ADMIN/ROSTER.md`, `ADMIN/ASSIGNMENTS.md` |
| 4 | 2025-10-01 | Cho phép ExploitDeep kích hoạt ngay khi T3 xong, không cần thêm một vòng duyệt thủ công | Người dùng chỉ thị Admin tự quyết, bỏ cổng chặn. Điều kiện (1) SCOPE.md trích nguyên văn vẫn bắt buộc vì đó là định nghĩa "được phép" | `ADMIN/ASSIGNMENTS.md` ghi chú T4 |
