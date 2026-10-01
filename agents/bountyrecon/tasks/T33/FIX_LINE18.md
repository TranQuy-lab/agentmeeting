# T33 — Sửa dòng 18 `CANDIDATES.md` (+ quét theo nghĩa)

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T33 · **Nhánh:** `agent/bounty-recon/T33`
**Chỉ thị:** D-024 (msg #186) · **`main` gốc (merge-base):** `6d47749` · **Ngày:** `2026-10-01`
**Territory:** `agents/bountyrecon/**`, `security/**`

> ⚠️ **Chưa verify — chờ Reviewer1 (T32).** Tôi không tự verify (D-004).

---

## 0. ⚠️ CẦN ADMIN BIẾT: **T31 CHƯA ĐƯỢC MERGE VÀO `main`** ⇒ T33 là nhánh **XẾP CHỒNG**

**Kiểm chứng:**

```text
$ git merge-base --is-ancestor ecce293 main ; echo $?
  -> KHONG phai to tien (T31 KHONG co trong main)
$ git branch -a --contains ecce293
  agent/bounty-recon/T31 ; remotes/origin/agent/bounty-recon/T31   <- chi o nhanh rieng
$ git rev-parse main:agents/bountyrecon/tasks/T3/CANDIDATES.md
  95d16d76c55fd0358d93632245f7c0123526c4ba   <- ban CU (chua co T31)
$ git show main:...CANDIDATES.md | sed -n '19p'
  | 4 | Chốt 4 **xung đột scope** của GitLab (xem §2) | ⏸ **CHƯA** — **CẦN ADMIN PHÁN QUYẾT** |
$ git show main:...CANDIDATES.md | sed -n '21p'
  **⇒ Chưa đủ 4/4. ĐỀ NGHỊ CHƯA MỞ T4.**
```

⇒ Trên `main`, `CANDIDATES.md` **vẫn là bản CŨ**: dòng 19 và 21 **chưa** được T31 sửa.
Nếu T33 cắt từ `main` thì bản vá 1 dòng của tôi sẽ nằm **cạnh dòng 19/21 cũ** ⇒
**tái tạo mâu thuẫn** (dòng 18 nói "đã verify xong" trong khi dòng 19 nói "CẦN ADMIN PHÁN QUYẾT").

**⇒ Tôi cắt T33 từ `origin/agent/bounty-recon/T31`** — đúng như Admin đã giao ở D-024
(*"Reviewer1 verify **T31 + T33** tại **HEAD CUỐI**"*), tức T32 phải thấy **cả hai** cùng lúc.

**Hệ quả cho Admin:** `T31` **chưa** merge. Admin nên **merge T31 trước**, hoặc **merge T33**
(bao gồm T31). `git diff main agent/bounty-recon/T33` sẽ hiện **cả** T31 + T33;
muốn xem **riêng T33**: `git diff agent/bounty-recon/T31 agent/bounty-recon/T33` → **đúng 1 dòng**.

---

## 1. Yêu cầu 1 — dòng 18 ✅

```text
TRƯỚC: | 3 | Reviewer1 verify T3 độc lập | ⏸ **CHƯA** |
SAU  : | 3 | Reviewer1 verify T3 độc lập | ✅ **XONG** — **T14 PASS** + đã merge (`4642e3c`) |
```

**Căn cứ (2 nguồn độc lập, đều có thật trong repo):**
- **T14 PASS:** `reviews/CROSS.md` §2.8 → `[REVIEW] T14 / BountyRecon / Lớp 1+2 / KẾT QUẢ: PASS`
  · `**Artifact kiểm:** security/{gitlab,github,cloudflare}/SCOPE.md + RECON.md @ 03d304b`
  · `**Phán quyết T14: PASS.** 20/20 câu trích nguyên văn · 3/3 policy byte-exact bằng hash`
- **Đã merge:** commit `4642e3c` (Admin báo ở D-021 §1; `security/*/SCOPE.md` có mặt trên `main`).

## 2. Yêu cầu 2 — **KHÔNG đụng dòng 2** ✅

Dòng 17 (hàng 2) giữ nguyên: `| 2 | Admin ban hành chỉ thị T4 bằng văn bản | ⏸ **CHƯA** |`
⇒ **ĐÚNG** — G4 vẫn ĐÓNG, chưa có chỉ thị target nào (D-013). Xem §3 để thấy nó **không** nằm trong vùng sửa.

## 3. Yêu cầu 3 — băm từng phần + QUY ƯỚC RANH GIỚI

Nguồn: `EVIDENCE/verify_t33.txt` (script: [`verify_t33.py`](verify_t33.py)).

### QUY ƯỚC RANH GIỚI (ghi rõ — Reviewer1 từng lệch 1 ký tự vì quy ước khác)
```text
* dòng = str.splitlines()             -> BỎ ký tự kết thúc dòng (\n, \r\n)
* vùng = "\n".join(dòng_a..dòng_b), 1-based, HAI ĐẦU ĐÓNG, KHÔNG có \n ở cuối vùng
* vùng "đã sửa" xác định bằng difflib.SequenceMatcher (opcodes replace/delete/insert)
  — KHÔNG đoán số dòng bằng tay
* MỖI VÙNG ĐƯỢC BĂM THEO CẢ HAI QUY ƯỚC:  (A) KHÔNG \n cuối   (B) CÓ \n cuối
  => nếu cả A và B đều khớp trước/sau thì kết luận KHÔNG phụ thuộc quy ước
```

### Cô lập thay đổi CỦA RIÊNG T33 (base = T31 → cây làm việc)
```text
agents/bountyrecon/tasks/T3/CANDIDATES.md: dong TRUOC=121 SAU=121
  opcodes khac: [('replace', 18, 18, 18, 18)]
    - | 3 | Reviewer1 verify T3 độc lập | ⏸ **CHƯA** |
    + | 3 | Reviewer1 verify T3 độc lập | ✅ **XONG** — **T14 PASS** + đã merge (`4642e3c`) |
  DONG DA SUA: 1
  VUNG KHONG DOI:
    V0: TRUOC 1..17  (SAU 1..17)  n=17   (A)9317e9a78e13b14a/9317e9a78e13b14a OK  (B)39fce0a4330764c1/39fce0a4330764c1 OK
    V1: TRUOC 19..121 (SAU 19..121) n=103 (A)2e075d6514fc21be/2e075d6514fc21be OK  (B)b6d656bf9576a6a6/b6d656bf9576a6a6 OK
  => MOI VUNG KHONG DOI GIONG HET theo CA HAI quy uoc: True

security/gitlab/RECON.md: dong TRUOC=214 SAU=214
  opcodes khac: []            DONG DA SUA: 0
    V0: TRUOC 1..214 (SAU 1..214) n=214  (A)9a221ca46fb801ca/9a221ca46fb801ca OK  (B)80726013cba9adc1/80726013cba9adc1 OK
  => MOI VUNG KHONG DOI GIONG HET theo CA HAI quy uoc: True
```

**Điểm mấu chốt:**
- T33 sửa **đúng 1 dòng (18)**; `RECON.md` **0 dòng** (không đụng).
- **V1 = dòng 19..121** (chứa **dòng 19 và 21 cũ của T31** và **dòng 17/hàng 2**) — hash
  `2e075d6514fc21be` **giống hệt** trước/sau ⇒ **dòng 2 KHÔNG bị đụng**, đúng yêu cầu 2.
- Số dòng `121 = 121` ⇒ không thêm/bớt dòng nào.

## 4. Yêu cầu 4 — KIỂM THEO LỊCH SỬ (D-023 phép kiểm [2])
```text
so commit trong merge-base..HEAD: 6
  ecce293d2921  [T31] evidence: ...        OK  T31/EVIDENCE/history_check.txt
  9455f8932de7  [T31] fix: tu sua 1 cau... OK  T3/CANDIDATES.md
                                           OK  T31/EVIDENCE/verify_regions.txt
                                           OK  T31/verify_t31.py
  209c3084e082  [T31] evidence: ...        OK  T31/EVIDENCE/history_check.txt
  683e31f35493  [T31] report: ...          OK  T31/EVIDENCE/history_check.txt
                                           OK  T31/FIX_GROUP_B.md
  81a56e4dd799  [T31] evidence: ...        OK  T31/EVIDENCE/history_check.txt
                                           OK  T31/history_check_t31.py
  52e96eaa92ed  [T31] fix: don nhom B ...  OK  T3/CANDIDATES.md
                                           OK  T31/EVIDENCE/verify_regions.txt
                                           OK  T31/verify_t31.py
                                           OK  security/gitlab/RECON.md
  => moi file bi cham nam trong danh sach CHO PHEP: True
  => file bi LOAI TRU bi cham: 0
     LOAI TRU = T28/FIX_2B.md, T28|T29|T30|T32/**, va moi EVIDENCE/** ngoai T31/T33

  VUNG TRICH NGUYEN VAN cua security/gitlab/SCOPE.md qua tung commit:
    so commit kiem: 0 ; VUNG NGUYEN VAN KHONG DOI: True
    GHI CHU: KHONG commit nao trong khoang 6d47749..ecce293 cham SCOPE.md
             => vung trich nguyen van duong nhien khong doi (T28/T29 da o trong main)
```
> 📌 **Trung thực — tôi tự sửa 2 lỗi logic trong `verify_t33.py`:** bản đầu coi file của **T31**
> là "vi phạm" (vì chỉ cho phép tiền tố `T33/`) — **sai**, vì T31 là **nền hợp lệ** của nhánh xếp chồng;
> và bản đầu xếp `T31/EVIDENCE/*` vào "file bị loại trừ" — **sai**, vì đó là **bằng chứng hợp lệ của T31**.
> Đã sửa: `is_allowed()` nhận cả `T31/` + `T33/`; `is_excluded()` loại trừ đúng
> `T28/FIX_2B.md`, `T28|T29|T30|T32/**`, và `EVIDENCE/**` ngoài T31/T33. Sau khi sửa: **0**.

## 5. Yêu cầu 5 — quét theo NGHĨA → **PHÁT HIỆN LỚN**

**Chi tiết: [`SEMANTIC_SCAN.md`](SEMANTIC_SCAN.md)** (bằng chứng: `EVIDENCE/semantic_scan.txt`).

**Tóm tắt:** `reviews/CROSS.md` §2.8 ghi T14 đã kiểm **`security/{gitlab,github,cloudflare}/SCOPE.md`
+ `RECON.md`** và **PASS**. Nhưng `security/**` **vẫn còn 6 dòng** khẳng định *"Chưa verify"*:

| # | Vị trí | Nguyên văn |
|---|---|---|
| 1 | `security/github/SCOPE.md:12` | `⚠️ **Chưa được verify.** ... Chờ Reviewer1 kiểm lại.` |
| 2 | `security/github/RECON.md:6` | `**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.**` |
| 3 | `security/cloudflare/SCOPE.md:12` | `⚠️ **Chưa được verify.** ... Chờ Reviewer1.` |
| 4 | `security/cloudflare/RECON.md:6` | `**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.**` |
| 5 | `security/gitlab/SCOPE.md:11` | `⚠️ **Chưa được verify.** ... Chờ Reviewer1.` |
| 6 | `security/gitlab/RECON.md:6` | `**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.**` |

⇒ **6/6 LỖI THỜI** — **cùng lớp lỗi với dòng 18**, nhưng **6 chỗ**. Bộ quét **mẫu câu** bắt **0/6**;
bộ quét **theo nghĩa** bắt **6/6**. Đây là **bằng chứng định lượng** cho bài học D-024 §3.

> ⛔ **Tôi CHƯA sửa 6 dòng này** — T33 chỉ được giao dòng 18. Báo hết để Admin quyết (như T31).
> Đã rà **16** dòng khẳng định "chưa xong": **6 lỗi thời** + **10 đúng** (danh sách đầy đủ ở `SEMANTIC_SCAN.md`).
> Đặc biệt `CANDIDATES.md` **dòng 17** (hàng 2) và **dòng 5** (`⏸ CHỜ ADMIN`) đều **ĐÚNG**, giữ nguyên.

## 6. Kết luận

| Yêu cầu T33 | Kết quả |
|---|---|
| 1. Dòng 18 → `✅ XONG` kèm căn cứ T14 PASS + merge `4642e3c` | ✅ |
| 2. KHÔNG đụng dòng 2 | ✅ nằm trong vùng không đổi V1, hash giống hệt |
| 3. Băm từng phần + quy ước ranh giới + **cả hai** quy ước | ✅ T33 sửa **1 dòng**; mọi vùng khác giống hệt |
| 4. Kiểm theo LỊCH SỬ (D-023 [2]) | ✅ 6 commit · **0 file bị loại trừ bị chạm** · vùng nguyên văn không đổi |
| 5. Quét theo NGHĨA | ✅ **bắt 6 lỗi** mẫu câu bỏ sót — xin Admin quyết |
| — Phát hiện thêm | ⚠️ §0: **T31 chưa merge** ⇒ T33 xếp chồng; 🔎 §5: **6 dòng "Chưa verify" lỗi thời** |

**G4 vẫn ĐÓNG. Không chạm hệ thống thật. Không merge `main`.**
