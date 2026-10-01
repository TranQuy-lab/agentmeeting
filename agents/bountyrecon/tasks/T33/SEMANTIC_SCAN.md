# T33 — QUÉT THEO NGHĨA (yêu cầu 5): tìm mọi dòng khẳng định "CHƯA XONG"

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T33 · **Nhánh:** `agent/bounty-recon/T33`
**Ngày:** `2026-10-01` · **Bằng chứng thô:** `EVIDENCE/semantic_scan.txt`

> ⚠️ **Chưa verify — chờ Reviewer1 (T32).** Tôi không tự verify (D-004).

Theo D-024 §3: bộ quét T29 quét **theo mẫu câu** (`"4 xung đột"`, `"PHẢI HỎI ADMIN"`) nên **bỏ sót**
dòng 18 — *cùng lớp lỗi nhưng khác chữ*. Lần này tôi quét **theo NGHĨA**: mọi dòng khẳng định
một điều kiện/việc là **CHƯA XONG**, rồi kiểm xem điều kiện đó nay **đã xong chưa**.

---

## 🔴 PHÁT HIỆN LỚN: **6 dòng** (không phải 1) khẳng định "Chưa verify" — nhưng T14 đã PASS cả 6

`reviews/CROSS.md` §2.8 ghi **nguyên văn** phạm vi kiểm của T14:

```text
## 2.8 Bài kiểm #4 — T14: kiểm chứng chéo T3 BountyRecon
[REVIEW] T14 / BountyRecon (ag_579fc4fa) / Lớp 1+2 / KẾT QUẢ: PASS
         (20/20 câu trích nguyên văn khớp · 3/3 policy byte-exact · 1 TINH CHỈNH nhỏ về "4 xung đột")
**Artifact kiểm:** `security/{gitlab,github,cloudflare}/SCOPE.md` + `RECON.md` @ `03d304b`
...
**Phán quyết T14:** **PASS.** 20/20 câu trích nguyên văn · 3/3 policy byte-exact bằng hash ·
```

⇒ **T14 đã kiểm CẢ `SCOPE.md` LẪN `RECON.md` của CẢ 3 chương trình**, và **PASS**.
Nhưng trong `security/**` vẫn còn **6 dòng** nói ngược lại:

| # | File:dòng | Nguyên văn | Đánh giá |
|---|---|---|---|
| 1 | `security/github/SCOPE.md:12` | `> ⚠️ **Chưa được verify.** Theo D-004, người viết KHÔNG tự verify. Chờ Reviewer1 kiểm lại.` | ❌ **LỖI THỜI** — T14 PASS |
| 2 | `security/github/RECON.md:6` | `**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.** ...` | ❌ **LỖI THỜI** — T14 PASS |
| 3 | `security/cloudflare/SCOPE.md:12` | `> ⚠️ **Chưa được verify.** Theo D-004, ... Chờ Reviewer1.` | ❌ **LỖI THỜI** — T14 PASS |
| 4 | `security/cloudflare/RECON.md:6` | `**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.** ...` | ❌ **LỖI THỜI** — T14 PASS |
| 5 | `security/gitlab/SCOPE.md:11` | `> ⚠️ **Chưa được verify.** Theo D-004, ... Chờ Reviewer1.` | ❌ **LỖI THỜI** — T14 PASS |
| 6 | `security/gitlab/RECON.md:6` | `**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.** ...` | ❌ **LỖI THỜI** — T14 PASS |

⇒ **6/6 đều lỗi thời.** Đây **đúng cùng lớp lỗi với dòng 18** mà T33 được giao — nhưng **6 chỗ**,
không phải 1. Bộ quét **theo mẫu câu** không bắt được **chỗ nào** trong 6 chỗ này (chúng dùng
"Chưa verify"/"Chưa được verify", không dùng "4 xung đột"/"PHẢI HỎI ADMIN").

**Lệnh kiểm (thô):** `grep -rn 'Chưa verify\|Chưa được verify' security/` → đúng **6 dòng**.
Và `grep -n 'Artifact kiểm' reviews/CROSS.md` → dòng **358** = `security/{gitlab,github,cloudflare}/SCOPE.md + RECON.md @ 03d304b`.

> ⛔ **Tôi CHƯA sửa 6 dòng này.** T33 chỉ được giao **dòng 18** của `CANDIDATES.md`.
> Theo đúng kỷ luật Admin đã xác nhận ở T29/T31 (*"đừng giới hạn việc QUÉT"* — không phải
> *"sửa mọi nơi"*), tôi **báo hết** và **xin Admin quyết**.
>
> **Xin Admin chọn:** (1) giao task riêng cho tôi sửa **6 dòng** (đổi thành `✅ Đã verify — T14 PASS`,
> kèm căn cứ `reviews/CROSS.md` §2.8 + commit `03d304b`), (2) Admin tự sửa, (3) giữ nguyên.
>
> *Lưu ý:* `security/gitlab/SCOPE.md:11` và `:12` — dòng 11 là dòng này, còn **§0 của file đó**
> đã có ghi chú *"Thay đổi này supersede chứng thực T14 ở RIÊNG §2b"* (T28) và *"RIÊNG các dòng đã sửa"* (T29),
> nên khi sửa cần **giữ** các ghi chú đó.

---

## ✅ Các dòng còn lại — đã kiểm từng dòng, TẤT CẢ ĐỀU ĐÚNG

### `agents/bountyrecon/tasks/T3/CANDIDATES.md`

| Dòng | Nguyên văn (rút gọn) | Đánh giá |
|---|---|---|
| **5** | `**Trạng thái:** ⏸ **CHỜ ADMIN** — T4 chỉ mở khi Admin ban hành chỉ thị bằng văn bản` | ✅ **ĐÚNG** — G4 vẫn ĐÓNG, chưa có chỉ thị target (D-013) |
| **17** (hàng 2) | `Admin ban hành chỉ thị T4 bằng văn bản \| ⏸ **CHƯA**` | ✅ **ĐÚNG** — Admin đã xác nhận **không đụng** dòng này |
| **18** (hàng 3) | `Reviewer1 verify T3 độc lập \| ⏸ **CHƯA**` | ✅ **ĐÃ SỬA Ở T33** → `✅ XONG — T14 PASS + đã merge (4642e3c)` |
| **31** | `GitHub **chưa** loại trừ tường minh SPF/DMARC, nhưng cũng **chưa xác minh** ...` | ✅ **ĐÚNG** — C1 vẫn chưa được giải quyết |
| **67** | `(CẦN ADMIN PHÁN QUYẾT)"*. **Việc phán quyết ĐÃ XONG.**` | ✅ **ĐÚNG** — "CẦN ADMIN" nằm trong **trích lại tên cũ** của ghi chú đính chính |
| **93** | `GitLab chặn **500 request chưa xác thực** / cửa sổ` | ✅ **ĐÚNG** — "chưa xác thực" = *unauthenticated* (nghĩa kỹ thuật), **không** phải "chưa kiểm" |

### `security/gitlab/RECON.md`

| Dòng | Nguyên văn (rút gọn) | Đánh giá |
|---|---|---|
| **6** | `⚠️ Chưa verify — chờ Reviewer1` | ❌ **XEM PHÁT HIỆN Ở TRÊN** |
| **28** | `⇒ **SPF gốc của gitlab.com: CHƯA XÁC MINH.**` | ✅ **ĐÚNG** — `dig ... TXT` vẫn timeout, chưa giải quyết |
| **109** | `500 request **chưa xác thực** mỗi cửa sổ` | ✅ **ĐÚNG** — *unauthenticated* |
| **165** | `🔎 **Quan sát (CHƯA XÁC MINH):** chứng chỉ gộp 6 tên` | ✅ **ĐÚNG** — chưa xác minh |
| **176** | C1 `registry.gitlab.com` ... `chưa phải lỗi` | ✅ **ĐÚNG** — nêu mức tin cậy, không phải điều kiện |
| **185** | `**chưa xác minh**, **không phải lỗ hổng**` | ✅ **ĐÚNG** |
| **203** | `## 5. Hạn chế & điều CHƯA xác minh` | ✅ **ĐÚNG** — mục này liệt kê hạn chế thật |
| **205** | `dig gitlab.com TXT **timeout** ⇒ SPF gốc **chưa xác minh**` | ✅ **ĐÚNG** |
| **212** | `license.gitlab.com không phân giải — **chưa xác minh** lý do` | ✅ **ĐÚNG** |
| **177, 195** | `... đã được sở hữu ...` (không phải takeover) | ✅ **ĐÚNG** |
| **206, 210** | `4 tài sản đã được Admin loại khỏi T4` / `Phán quyết đã xong (D-021)` | ✅ **ĐÚNG** (đã sửa ở T31) |

---

## Kết luận yêu cầu 5

| | |
|---|---|
| Số dòng khẳng định "chưa xong" đã rà | **16** (6 trong `CANDIDATES.md`, 10 trong `RECON.md`) |
| **Lỗi thời phát hiện** | **6** — tất cả là dòng "Chưa verify" trong `security/**` |
| Đúng | **10** (+ dòng 18 đã sửa) |
| **Bộ quét mẫu câu bắt được** | **0/6** |
| **Bộ quét theo nghĩa bắt được** | **6/6** |

⇒ **Xác nhận bài học D-024:** quét theo mẫu câu bỏ sót **toàn bộ** 6 lỗi cùng lớp;
quét theo **nghĩa** bắt được **cả 6**. Đây là **bằng chứng định lượng** cho nhận định của Admin.
