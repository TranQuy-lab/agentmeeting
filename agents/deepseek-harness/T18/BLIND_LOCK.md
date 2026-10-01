# T18 — KHÓA BẰNG CHỨNG KIỂM MÙ (chốt TRƯỚC khi đọc kết luận Reviewer1)

**Người chạy:** DeepSeek-Harness (`ag_d1739b2a`) · **Task:** T18 · **Ngày:** 2026-10-01

## Cam kết kiểm mù — bằng chứng thời gian

| Mốc | Thời điểm (UTC) | Việc |
|---|---|---|
| Bắt đầu T18 | `2026-10-01T14:32:36Z` | Bắt đầu thu thập sự thật thô, **CHƯA** đọc `reviews/CROSS.md` |
| Chốt hash bằng chứng | `2026-10-01T14:33:46Z` | Ghi và băm 3 file blind |
| Đọc kết luận Reviewer1 | sau `14:33:46Z` | Chỉ mở `reviews/CROSS.md` SAU khi đã băm xong |

## Hash bằng chứng của tôi (chốt trước)

```text
3c5668eb582581470dd000c8145dcf57b8c52c3beacf635faacf0d2096c4a407  t18a_s31_blind_raw.txt
54fd0e99a80c75fdfd78649b5b5b4ffb3345ada02fcb1335e0ebe500e215c7d6  t18b_doi_blind_raw.txt
af52f7eae8ba07e69de4cc02be8032f36bda46e31346f6ecf3eaadfb981b5a65  t18c_scope_blind_raw.txt
```

**Kiểm chứng được:** người kiểm tra sau có thể `sha256sum` 3 file trong `EVIDENCE/` và thấy khớp.
Nếu tôi sửa file sau khi đọc kết luận Reviewer1, hash sẽ lệch ⇒ phát hiện được.
