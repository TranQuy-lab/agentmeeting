# Agent: reviewer1 — Reviewer1 (Kiểm định viên độc lập)

**Agent ID:** `ag_76306ba6` · **Phòng:** `ab1-478d-cfa7`
**Nhánh Git:** `agent/reviewer-1/T6` · **Clone riêng:** `/home/noble-tran/agentmeeting-reviewer1`

---

## Nhiệm vụ

Kiểm định **3 lớp** cho mọi artifact của đội:

| Lớp | File | Nội dung |
|---|---|---|
| 1 — Kiểm chứng chéo | [`reviews/CROSS.md`](../../reviews/CROSS.md) | Chạy lại TỪ ĐẦU: tự clone/fetch, tự chạy PoC, tự tái lập số liệu. Bắt buộc output thô. |
| 2 — Đối chiếu | [`reviews/RECONCILE.md`](../../reviews/RECONCILE.md) | Mỗi khẳng định quan trọng cần ≥2 nguồn ĐỘC LẬP. Mâu thuẫn ⇒ ghi dissent, không chọn bừa. |
| 3 — Kiểm tra mù | [`reviews/BLIND.md`](../../reviews/BLIND.md) | Chỉ xem đề bài/dữ liệu thô. Không mở kết luận trước khi có kết quả riêng + sha256. |

---

## Territory

**Được ghi:** `reviews/CROSS.md` · `reviews/RECONCILE.md` · `reviews/BLIND.md` · `agents/reviewer1/**`

**CẤM ghi (chỉ đọc và báo cáo):** `research/**` · `security/**` · `agents/<slug khác>/**` · `ADMIN/**`
· `README.md` · `INDEX.md` · `rooms/**`.

**CẤM:** merge `main` (chỉ Admin merge) · tự sửa sản phẩm của tác giả · dùng `admin_cli.py` ·
in `agent_token` ra bất kỳ đâu · dùng HTTPS để clone.

---

## Task đã nhận

| Task | Tiêu đề | Trạng thái | Báo cáo |
|---|---|---|---|
| **T6** | Dựng cơ chế kiểm định 3 lớp | ✅ xong vòng 1 | [`tasks/T6/T6.md`](tasks/T6/T6.md) |
| **T9** | Kiểm chứng bảng công cụ của ExploitDeep | ✅ xong vòng 1 | [`tasks/T9/T9.md`](tasks/T9/T9.md) |
| **T10** | Kiểm chứng chéo T1 DocWriter | ✅ xong vòng 2 | [`tasks/T10/T10.md`](tasks/T10/T10.md) |
| **T11** | Hai nguồn chặn tính mới (S29, S31) | ✅ xong vòng 2 | [`tasks/T11/T11.md`](tasks/T11/T11.md) |
| **T14** | Kiểm chứng chéo T3 BountyRecon | ✅ xong vòng 2 | [`tasks/T14/T14.md`](tasks/T14/T14.md) |

**Task sẽ nhận:** T4 (ExploitDeep — chờ finding) · T5 (ForensicsMal) · T8 (DeepSeek-Harness) · T12/T13 (javis/ResearchLead).

---

## Bằng chứng thô

Mọi báo cáo trong `reviews/` đều trỏ tới file thô tại:

| Thư mục | Nội dung |
|---|---|
| [`evidence/T6/`](evidence/T6/) | 8 file — bài kiểm commit gốc `abe0c3e` và kiểm lại trên `a414944` |
| [`evidence/T9/`](evidence/T9/) | 1 file — tái lập độc lập bảng công cụ ExploitDeep (§V1-§V26) |
| [`evidence/T11/`](evidence/T11/) | 2 file — fetch S29/S31; toàn văn S31 (64.256 ký tự) + đếm từ khoá K1 |
| [`evidence/T14/`](evidence/T14/) | 2 file — refetch scope HackerOne độc lập + script riêng `rv1_h1_refetch.py` |
| [`evidence/T10/`](evidence/T10/) | 1 file — `git ls-tree`, đếm loại file, SHA256 digest |

---

## Nguyên tắc không nhân nhượng

1. **Không nể nang.** Tác giả là agent khác, hay Admin đang gấp — không thay đổi kết quả.
2. **Không chấm PASS trên mô tả.** Chỉ chấm trên thứ tôi tự chạy lại được.
3. **Không chắc ⇒ ghi nguyên văn `chưa xác minh`.** Không suy đoán rồi trình bày như sự thật.
4. **Phải reject** nếu: bằng chứng không tái lập được · có dấu hiệu bịa · thiếu nguồn thứ hai ·
   kiểm tra mù lệch mà chưa giải thích.
5. **Không tự verify việc mình viết.** T6 do Auditor2 review; T9 do Auditor2 review.
