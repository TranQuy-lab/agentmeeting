# [CHECK-IN] ResearchLead — `ag_d85dde8d`

**Ngày:** 2026-10-01 · **Task:** T2 · **Nhánh:** `agent/research-lead/T2` · **Repo riêng:** `/home/noble-tran/agentmeeting-researchlead` (nền `abe0c3e`)

## 1. Skill đang nạp — đường dẫn THẬT (đã kiểm chứng)
| Skill | SKILL.md | Base dir |
|---|---|---|
| `nckh` | `/home/noble-tran/.agents/skills/nckh/SKILL.md` | `/home/noble-tran/.agents/skills/nckh/` |
| `nckh` (bản đầy đủ) | `/home/noble-tran/agent-skills/skills/nckh/SKILL.md` | `/home/noble-tran/agent-skills/skills/nckh/` |
| `giao-su` | `/home/noble-tran/.dsh/skills/giao-su/SKILL.md` | `/home/noble-tran/.dsh/skills/giao-su/` |

Module con đã `ls` xác minh tồn tại: `literature-review`, `research-lookup`, `citation-management`, `experimental-design`, `hypothesis-generation`, `scientific-writing`, `peer-review` (đều nằm trong `.../references/skills/<tên>/SKILL.md`, 168 module tổng).

## 2. Chuyên môn chính — phụ
- **Chính:** tổng quan tài liệu hệ thống; thiết kế nghiên cứu & giả thuyết; xác minh trích dẫn qua CrossRef/OpenAlex; viết đề xuất.
- **Phụ:** thống kê/thiết kế thí nghiệm ở mức dùng thư viện chuẩn; an ninh mạng & thiết kế hệ thống ở góc **đo lường/đánh giá**, KHÔNG phải góc khai thác.

## 3. Điểm MẠNH + bằng chứng cụ thể
**Xác minh trích dẫn bằng API học thuật thật, không trích từ trí nhớ.** Output thô vừa chạy:
```text
$ curl -s https://api.crossref.org/works/10.6028/NIST.FIPS.203
10.6028/nist.fips.203 | Module-lattice-based key-encapsulation mechanism standard
| [[2024, 8, 13]] | National Institute of Standards and Technology (U.S.)
```
→ DOI FIPS 203 tồn tại thật, metadata khớp tiêu đề + ngày + nhà xuất bản.
Bằng chứng 2: đã `ls -R` repo, đọc `ADMIN/ROSTER.md` (41 dòng) + `ADMIN/ASSIGNMENTS.md` (26 dòng) trước khi viết file đầu tiên.

## 4. Điểm YẾU (nói thẳng)
1. **Không có CSDL trả phí** (IEEE Xplore full-text, Springer, ACM DL, Scopus). Lý do: không có tài khoản. Hệ quả: với bài sau paywall tôi chỉ xác minh được **metadata + abstract công khai**, thân bài không đọc được ⇒ tôi sẽ ghi rõ `chỉ xác minh metadata`.
2. **Không chạy được thực nghiệm mạng thật** (không testbed, không uỷ quyền scan). Lý do: môi trường chỉ có filesystem + HTTP client. Hệ quả: đề xuất dừng ở **thiết kế phương pháp + ước lượng chi phí**, tôi không tự sinh dữ liệu kết quả.
3. **Không có chuyên môn mật mã lý thuyết** (chứng minh an toàn lattice). Lý do: nền tảng đo lường/hệ thống. Hệ quả: không nhận việc đánh giá độ an toàn toán học của một scheme.
4. Tiếng Anh học thuật tốt hơn tiếng Việt ở một số thuật ngữ chuyên ngành.

## 5. NGOÀI KHẢ NĂNG / VƯỚNG ĐẠO ĐỨC
- **Ngoài khả năng:** khai thác lỗ hổng, viết PoC tấn công, dịch ngược, pháp y số, benchmark phần cứng thật → **không nhận** việc thuộc T4/T5.
- **Sẽ TỪ CHỐI và báo Admin nếu bị yêu cầu:** (a) quét/đo chủ động hệ thống không có uỷ quyền văn bản; (b) chỉnh sửa kết quả cho khớp kỳ vọng người đặt hàng; (c) trích nguồn không tồn tại hoặc tự "verify" việc mình làm; (d) công bố dữ liệu cá nhân/token vào repo.
- **Xung đột lợi ích:** tôi là tác giả mọi file ở nhánh này ⇒ **không được** làm Reviewer1 cho chính nhánh này.

## 6. Công cụ THỰC SỰ có (đã kiểm chứng trong phiên)
`bash`, `python3`, `git`+SSH tới `TranQuy-lab/agentmeeting.git` ✅ · HTTP client Internet ✅ (`curl api.crossref.org`, `api.openalex.org` trả JSON thật) · `web_search`/`web_fetch` ✅ · RFC Editor (`rfc-editor.org` tải được RFC 8446 = 337,736 bytes; RFC 9370 = 81,487 bytes) ✅ · agent-meet CLI ✅ (`join` OK, `board list` OK, `poll` OK).
**KHÔNG có:** CSDL KH trả phí, testbed mạng, GPU. **CẤM dùng:** `admin_cli.py` (§0.3).

## 7. Mức sẵn sàng
**Sẵn sàng T2** — bắt đầu ngay trong vòng này: ≥1 hồ sơ đề tài đủ 4 file + `research/RANKING.md`. Bế tắc quá 2 vòng tôi báo ngay.

## 8. Territory đề xuất
Giữ đúng ASSIGNMENTS.md: `research/**`, `agents/researchlead/**`.
**Xin Admin xác nhận 1 điểm mơ hồ:** `research/**/FORENSICS.md` thuộc T5 (ForensicsMal) — tôi sẽ **không** tạo/chạm file tên `FORENSICS.md` trừ khi Admin nói khác.

```text
[ACK §0] Chỉ SSH, không HTTPS. Không dùng admin_cli.py. Mọi lệnh có --session + --as.
[ACK §4] Không bịa URL/DOI/số liệu/output. Nguồn nào không fetch được => ghi "chưa xác minh".
[ACK §4] Không tự verify việc mình làm — chờ Reviewer1.
[ACK §5] Chỉ push nhánh agent/research-lead/T2; không merge main; không push token/credential.
```
