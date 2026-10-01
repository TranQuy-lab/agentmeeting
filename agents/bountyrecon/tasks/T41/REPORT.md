# T41 — Sửa CĂN CỨ (không sửa kết luận) ở 2 dòng

**Agent:** BountyRecon (`ag_579fc4fa`) · **Nhánh:** `agent/bounty-recon/T41` · **Ngày:** `2026-10-01`
**Chỉ thị:** D-028 · **Trạng thái:** ⚠️ Chưa verify — chờ Reviewer1.

## 0. Nhánh XẾP CHỒNG trên T34
`main` (`05886e0`) **chưa có T34**: `git merge-base --is-ancestor c097df8 main` → **KHÔNG**
(dòng 44 trên `main` vẫn là bản CŨ). Nên T41 cắt từ `origin/agent/bounty-recon/T34` (`c097df8`).
**Admin nên merge T34 trước, hoặc merge T41** (bao gồm T34). Xem riêng T41:
`git diff agent/bounty-recon/T34 agent/bounty-recon/T41` → đúng **1+1 dòng**.

## 1. Hai dòng đã sửa — GIỮ kết luận, ĐỔI căn cứ
**(1) `tasks/T3/CANDIDATES.md` dòng 44 (G2) — THUỘC T34**
Bỏ nhãn **`BỊ LOẠI`** (SAI: `license.gitlab.com` **không** nằm trong 4 tài sản có quyết định `D-021`
⇒ **không có quyết định nào của Admin** cho nó ⇒ theo phép thử `LOG` #95, đây là **vế bị cấm**).
**Giữ** *"KHÔNG chuyển"*, đổi căn cứ thành:
`KHÔNG chuyển (thiếu định nghĩa chính thức — DISSENT-12); hiệu lực CHƯA XÁC MINH`.
Vẫn **giữ** `archived_at = 2022-03-21T22:30:03.041Z` như **dữ liệu**, không dùng làm **căn cứ phán quyết**.

**(2) `security/gitlab/RECON.md` dòng 47 — DI SẢN T31** (không tính cho T34)
**Giữ** *"⛔ NGOÀI scope"*, đổi căn cứ sang **chính sách công bố `SCOPE.md` §2a**
(`archived_at 2020-10-05` chỉ còn là chiều phụ).

## 2. Kiểm chứng (`EVIDENCE/verify_t41.txt`)
- **Băm từng phần CẢ HAI quy ước**: 2 file, **mỗi file đúng 1 dòng đổi**; **mọi vùng khác GIỐNG HỆT** = True.
- **Kiểm theo lịch sử (D-023 [2])**: **0 file bị loại trừ bị chạm**.
- **Quét theo NGHĨA (D-025 [3a])** trên **7 tài liệu sống**: **0 dòng** kết luận *"loại / ngoài scope /
  không còn hiệu lực"* mà căn cứ **chỉ** là `archived_at`. Các chỗ **ĐÚNG** (căn cứ chính sách/luật
  cấm/quyết định Admin) **đều giữ nguyên, không sửa**: `CANDIDATES.md` G4/G5/G6 ·
  `gitlab/RECON.md:179–181` · `cloudflare/RECON.md:158` · `github/SCOPE.md:511` · 4 khối
  `⛔ GIỚI HẠN (D-026…)` · `_TEMPLATE/SCOPE.md:46`.

## 3. Bài học
**Kết luận có thể đúng nhưng căn cứ sai vẫn bị bác.** Sửa **căn cứ**, không sửa **phán đoán**.

**G4 vẫn ĐÓNG. Không chạm hệ thống thật. Không merge `main`.**
