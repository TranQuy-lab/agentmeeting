# T29 — Sửa 3 dòng còn sót trong `security/gitlab/SCOPE.md`

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T29 · **Nhánh:** `agent/bounty-recon/T29`
**Chỉ thị:** D-021 (msg #141/#142) + D-022 (msg #156) · **Ngày:** `2026-10-01`
**Territory:** `security/**`, `agents/bountyrecon/**`

> ⚠️ **Chưa verify — chờ Reviewer1 (T30).** Tôi không tự verify (D-004).

---

## 0. ⚠️ CẦN ADMIN BIẾT NGAY: **T28 CHƯA ĐƯỢC MERGE VÀO `main`** ⇒ T29 là nhánh **XẾP CHỒNG**

**Sự thật đã kiểm chứng:**

```text
$ git log --oneline main | grep -i 'T28'
  d07bf34 [T0] fix: ... giao T28          # chi la commit GIAO task, KHONG phai ban sua cua T28
$ git show main:security/gitlab/SCOPE.md | sed -n '146p'
  ## 2b. 🚨 XUNG ĐỘT SCOPE ĐÃ XÁC MINH — KHÔNG ĐƯỢC ĐOÁN     <-- §2b CU tren main
$ git branch -a --contains 9f73655
  agent/bounty-recon/T28
  remotes/origin/agent/bounty-recon/T28                       <-- T28 chi nam o nhanh rieng
```

⇒ Trên `main` (`c1462df`), **§2b vẫn là bản CŨ**. Nếu tôi cắt T29 từ `main` rồi sửa 3 dòng thành
*"0 xung đột hiệu lực"*, thì **§2b vẫn nói "XUNG ĐỘT SCOPE ĐÃ XÁC MINH"** ⇒ **tạo ra mâu thuẫn MỚI**,
đúng thứ T29 sinh ra để dẹp. Và chỉ thị ghi *"TUYỆT ĐỐI KHÔNG chạm §2b (đã sửa ở T28)"* — điều
chỉ đúng nếu §2b của T28 **có mặt**.

**Nên tôi cắt `agent/bounty-recon/T29` từ `origin/agent/bounty-recon/T28` (nhánh xếp chồng):**

```text
$ git log --oneline -2 agent/bounty-recon/T29
  9f73655 [T28] fix: sua nhan §2b security/gitlab/SCOPE.md - 0 xung dot hieu luc + archived_at
  8006168 [T8] protocol: 4 quy tac bo sung sau su kien archived_at
```

**Hệ quả cho Admin (quan trọng):**
- T29 **chứa commit T28**. Admin nên **merge T28 trước**, hoặc **merge T29** (bao gồm T28).
  Nếu merge T29 mà bỏ T28 ⇒ thứ tự commit sẽ nhảy.
- Reviewer1 (T30) kiểm **T28+T29 cùng lúc** — đúng như Admin đã giao ở D-022.
- `git diff main agent/bounty-recon/T29` sẽ hiện **cả** thay đổi của T28 **và** T29. Muốn xem
  **riêng** T29: `git diff agent/bounty-recon/T28 agent/bounty-recon/T29`.

---

## 1. Ba dòng đã sửa

| # | Dòng | TRƯỚC | SAU |
|---|---|---|---|
| 1 | **9** (§0 khối Tiêu đề) | `**Trạng thái:** ⚠️ **Trích được nguyên văn, NHƯNG có 4 XUNG ĐỘT scope — xem §2b. PHẢI HỎI ADMIN.**` | `**Trạng thái:** ✅ **Trích được nguyên văn. 0 xung đột hiệu lực — 4 tài sản đã nghỉ hưu (`archived_at` 2022-07-21), xem §2b.**` |
| 2 | **284** (§5) | `\| Trích được nguyên văn in-scope? \| ✅ **CÓ** (24 tài sản) — nhưng 4 tài sản bị xung đột \|` | `\| Trích được nguyên văn in-scope? \| ✅ **CÓ** (24 tài sản). 4 tài sản từng bị coi là xung đột đã **nghỉ hưu** (`archived_at` 2022-07-21) ⇒ **0 xung đột hiệu lực** \|` |
| 3 | **289** (§5) | `\| Đủ điều kiện chuyển ExploitDeep (T4)? \| ⚠️ **CÓ ĐIỀU KIỆN** — phải chốt 4 xung đột ở §2b trước \|` | `\| Đủ điều kiện chuyển ExploitDeep (T4)? \| ⚠️ **CÓ ĐIỀU KIỆN** — cần **chỉ thị nêu target cụ thể của Admin** (D-013). 4 tài sản đã nghỉ hưu vẫn **bị loại** khỏi T4 \|` |

- Dòng 9 nay khớp §2b ⇒ **hết tự mâu thuẫn** (đúng yêu cầu 1).
- Dòng 289 nay nêu đúng điều kiện còn lại là **chỉ thị target của Admin (D-013)**, không còn
  là "chốt 4 xung đột" đã xong; và vẫn giữ việc **4 tài sản bị loại** (đúng yêu cầu 2).

---

## 2. Bằng chứng thô — CHỈ 3 dòng đổi, mọi vùng khác GIỐNG HỆT

Nguồn: `EVIDENCE/verify_3lines.txt`.

```text
$ git rev-parse HEAD:security/gitlab/SCOPE.md   # blob TRUOC (ban T28)
  c6b1131d498fd694acd62b648c9644824c3f6492
$ git hash-object security/gitlab/SCOPE.md      # blob SAU (ban T29)
  de53744f623582aaca19b6bbda3b83ea5746bc9d
```

**Băm riêng từng VÙNG KHÔNG ĐỔI quanh mỗi chỗ sửa** (đúng cách Admin yêu cầu):

```text
  so dong: TRUOC=299  SAU=299        dong KHAC nhau: [9, 284, 289]

  VUNG KHONG DOI                              sha256 TRUOC        sha256 SAU          KET QUA
  S1  dong 1..8     (truoc dong 9)            224e8c14e260570d    224e8c14e260570d    GIONG HET ✅
  S2  dong 10..283  (giua dong 9 va 284)      2f0f1bcad024225c    2f0f1bcad024225c    GIONG HET ✅
  S3  dong 285..288 (giua 284 va 289)         9b6bc7713f67ff59    9b6bc7713f67ff59    GIONG HET ✅
  S4  dong 290..het (sau dong 289)            8dabffdc48ced063    8dabffdc48ced063    GIONG HET ✅

  => TAT CA VUNG KHONG DOI GIONG HET: True

  §2b (dong 146..202)  sha256 TRUOC=8d3ea9ac146d2aa3  SAU=8d3ea9ac146d2aa3  -> GIONG HET ✅
  VUNG TRICH NGUYEN VAN (§1+§2a+§3+§4)  e8673612eaefc259 -> e8673612eaefc259  -> GIONG HET ✅
```

⇒ **§2b KHÔNG bị chạm** (yêu cầu 3) · **mọi phần trích nguyên văn KHÔNG bị chạm** ·
số dòng **299 = 299** (không thêm/bớt dòng nào).

**`git diff` — đúng 3 dòng, 3 thêm / 3 xoá:**

```text
$ git diff -U0 HEAD -- security/gitlab/SCOPE.md | grep -E '^(@@|\+[^+]|-[^-])'
  @@ -9 +9 @@      -**Trạng thái:** ⚠️ ...4 XUNG ĐỘT... PHẢI HỎI ADMIN.**
                   +**Trạng thái:** ✅ ...0 xung đột hiệu lực — 4 tài sản đã nghỉ hưu...
  @@ -284 +284 @@  -| Trích được nguyên văn in-scope? | ... — nhưng 4 tài sản bị xung đột |
                   +| Trích được nguyên văn in-scope? | ... ⇒ **0 xung đột hiệu lực** |
  @@ -289 +289 @@  -| Đủ điều kiện chuyển ExploitDeep (T4)? | ... phải chốt 4 xung đột ở §2b trước |
                   +| Đủ điều kiện chuyển ExploitDeep (T4)? | ... chỉ thị nêu target cụ thể của Admin (D-013)...
$ git diff --stat HEAD -- security/gitlab/SCOPE.md
   security/gitlab/SCOPE.md | 6 +++---
   1 file changed, 3 insertions(+), 3 deletions(-)
```

---

## 3. Yêu cầu 4 — file bị cấm sửa VẪN NGUYÊN blob

```text
$ git rev-parse HEAD:agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md
  15c946ff956a3fdb466f7f9768081af29b812088
$ git hash-object agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md
  15c946ff956a3fdb466f7f9768081af29b812088
$ git rev-parse origin/main:agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md
  15c946ff956a3fdb466f7f9768081af29b812088
$ git diff --exit-code HEAD -- agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md ; echo exit=$?
  exit=0
```

⇒ Blob **`15c946ff956a3fdb466f7f9768081af29b812088`** — **trùng đúng giá trị Admin yêu cầu**
và trùng `origin/main`. **Không chạm.**

---

## 4. Yêu cầu 5 — quét sót toàn territory

**Chi tiết đầy đủ + phân loại: [`SCAN_RESIDUAL.md`](SCAN_RESIDUAL.md)** (bằng chứng:
`EVIDENCE/scan_residual_clean.txt`). Tóm tắt:

| Nhóm | Kết quả |
|---|---|
| **A. `SCOPE.md`** | ✅ **SẠCH** — 8 lần xuất hiện, tất cả đều đúng (dòng 148 trích lại tên cũ trong ghi chú đính chính là **cố ý, phải giữ**) |
| **B. CÒN SÓT — file sống, nên sửa** | ⚠️ **`security/gitlab/RECON.md`** (5 dòng: 39, 40, 47, 206, 208 + câu "Cần Admin phán quyết" ở 210 đã lỗi thời) · **`agents/bountyrecon/tasks/T3/CANDIDATES.md`** (dòng 19, 21, 64–82: cả mục §2 đọc như vấn đề **còn treo**) |
| **C. KHÔNG ĐƯỢC SỬA** | ⛔ `T28/FIX_2B.md` + mọi file trong `T28/EVIDENCE/`, `T29/EVIDENCE/` — **bản ghi lịch sử/bằng chứng thô** |
| **D. Không phải vấn đề** | `security/_TEMPLATE/SCOPE.md` dòng 9/19/22 — dùng "xung đột" **đúng nghĩa** (bài học M-01) |

### Vì sao tôi chỉ sửa 3 dòng, không tự sửa nhóm B

Yêu cầu 5 viết *"Báo hết, đừng chỉ sửa 3 chỗ được báo."* Tôi đọc là **"đừng giới hạn việc QUÉT"**,
không phải "hãy sửa thêm" — vì **cùng câu đó liệt kê `T28/FIX_2B.md`**, mà sửa file ấy là
**xuyên tạc báo cáo lịch sử** (nhóm C). Nếu nghĩa là "sửa mọi nơi" thì chính danh sách của Admin
đã tự mâu thuẫn.

Thêm nữa `RECON.md` và `CANDIDATES.md` **đã PASS kiểm định T14/T27**; sửa chúng sẽ **vô hiệu hoá
chứng thực đã có** — đúng loại rủi ro Admin đã khen tôi **hỏi thay vì tự sửa** ở T26/T28.

> **Xin Admin chọn:** (1) task riêng cho tôi sửa nhóm B (tôi đã xác định chính xác từng dòng),
> (2) Admin tự sửa, hoặc (3) chỉ đính chính ở `ADMIN/`.

---

## 5. Trung thực — lần quét đầu của tôi bị nhiễu

Lần quét đầu (`EVIDENCE/scan_residual.txt`) **tự khớp chính output của nó**: file được ghi ra đĩa
**trong khi** `grep` đang đọc ⇒ bắt được các dòng vừa ghi, lặp đệ quy. Đã sửa bằng cách
**loại trừ `/EVIDENCE/`** + dùng Python ⇒ `scan_residual_clean.txt`. **Giữ lại cả hai** để
Reviewer1 thấy sai sót và cách khắc phục.

---

## 6. Kết luận

| Yêu cầu T29 | Kết quả |
|---|---|
| 1. 3 dòng mới nói đúng "0 xung đột hiệu lực + 4 đã nghỉ hưu `archived_at` 2022-07-21"; dòng 9 khớp §2b | ✅ |
| 2. Dòng 289: điều kiện T4 nay là **chỉ thị target của Admin (D-013)** | ✅ |
| 3. KHÔNG chạm §2b / phần trích nguyên văn; chứng minh bằng băm từng phần | ✅ S1–S4 + §2b + vùng nguyên văn **giống hệt** |
| 4. `scope_github.md` blob vẫn `15c946ff…` | ✅ |
| 5. Quét sót toàn territory, báo hết | ✅ `SCAN_RESIDUAL.md` (nhóm A/B/C/D) |
| — Phát hiện thêm | ⚠️ §0: **T28 chưa merge** ⇒ T29 xếp chồng; nhóm B còn sót, xin Admin quyết |

**G4 vẫn ĐÓNG. Không chạm hệ thống thật. Không merge `main`.**
