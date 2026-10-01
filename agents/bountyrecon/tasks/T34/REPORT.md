# T34 + T36 + T37 — `[3b] archived_at` · 6 dòng "Chưa verify" · 3 khuyết điểm T31

**Agent:** BountyRecon (`ag_579fc4fa`) · **Nhánh:** `agent/bounty-recon/T34`
**Chỉ thị:** D-025, D-026, **D-027 (đính chính)** · **Ngày:** `2026-10-01`
**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.**

---

## 0. TÔI ĐÃ LÀM SAI RỒI SỬA LẠI — theo đúng D-027 (không giấu)

Admin giao T37 (D-026) với **5 vị trí**. Sau đó **D-027 đính chính: 3/5 vị trí SAI**.
**Tôi đã chèn khối `[3b]` vào cả 5 vị trí TRƯỚC khi D-027 tới.** Nay đã sửa lại:

| Vị trí Admin liệt kê ở D-026 | D-027 phán | Tôi đã làm | Nay |
|---|---|---|---|
| `security/gitlab/SCOPE.md` §1 | ✅ ĐÚNG | chèn `[3b]` + `archived_at=` từng dòng | **GIỮ** |
| `security/gitlab/SCOPE.md` §2a | ✅ ĐÚNG | chèn `[3b]` (SAI định dạng) | **ĐÃ ĐỔI** sang `archived_at=` từng dòng |
| `security/cloudflare/SCOPE.md` §1a | ✅ ĐÚNG | chèn `[3b]` (SAI định dạng) | **ĐÃ ĐỔI** sang `archived_at=` từng dòng |
| `security/github/SCOPE.md` §1 | ❌ SAI — **khối nguyên văn** | chèn `[3b]` (bóc xếp nguyên văn) | **ĐÃ GỠ**; thay bằng mục AUTHORED mới **§1b** |
| `security/github/RECON.md` | ❌ SAI — không có bảng scope | chèn `[3b]` | **ĐÃ GỠ** |
| `security/cloudflare/RECON.md` | ❌ SAI — không có bảng scope | chèn `[3b]` | **ĐÃ GỠ** |
| `security/gitlab/RECON.md` | *(không được nêu)* | chèn `[3b]` | **ĐÃ GỠ** — theo **cùng nguyên tắc** "RECON.md không có bảng scope"; tôi tự mở rộng và **báo rõ ở đây** |

**Cách đúng cho GitHub (D-027):** giữ nguyên §1 (nguyên văn), thêm **mục AUTHORED mới**:
`### 1b. Bảng tài sản GitHub kèm archived_at` — **TÁCH** nguyên văn khỏi bảng tổng hợp.
Đã tạo: **183 tài sản** (`sub=True`: 27 live + 156 archived), cột `archived_at` đầy đủ.

> 📌 **Nguyên tắc D-027 (LOG #94) tôi đã kiểm trước khi thêm cột:** *"kiểm bảng đó có phải
> BẢNG thật hay là KHỐI TRÍCH NGUYÊN VĂN. Trích nguyên văn > mọi yêu cầu định dạng."*
> Kết quả tự kiểm: `github/SCOPE.md` §1 — số dòng bắt đầu bằng `|` = **0** ⇒ **không phải bảng**
> ⇒ **không được thêm cột**. `github|cloudflare|gitlab/RECON.md` — **0 bảng scope**, chỉ bảng DNS.

---

## 1. Nội dung đã làm (đúng D-027)

### 1.1 Ba bảng AUTHORED nay có cột `archived_at`
```text
gitlab/SCOPE.md §1   : 24 dong tai san  -> 19 None + 5 RETIRED   (da lam o T34.1)
gitlab/SCOPE.md §2a  : 10 dong tai san  -> *.gitter.im=2021-05-25T18:36:39.198Z
                                           gitlab.net=2020-10-05T18:32:21.936Z
                                           gitlap.com=2020-10-05T18:32:08.263Z
                                           (dong nhieu identifier: ghi ro "XEN KE")
cloudflare/SCOPE.md §1a : 12 dong       -> 10 None + 2 RETIRED dung nhu Reviewer1 do:
                                           dash.teams.cloudflare.com = 2023-05-08T10:11:33.083Z
                                           http://cloudflare.com/apps/ = 2023-03-01T17:47:43.944Z
```
**Tôi TỰ ĐO LẠI, không chép** (GraphQL công khai, `archived:false`/`archived:true`):
GitLab **63 = 44 live + 19 arch** (sub=True: 19 live / **5** arch) ·
GitHub **197 = 39 + 158** (sub=True: 27 / **156**) ·
Cloudflare **83 = 78 + 5** (sub=True: 51 / **4**).

### 1.2 Bốn bản CAPTURE chụp lại thành `_v2` (D-026 (a))
`agents/bountyrecon/tasks/T3/EVIDENCE/scope_{github,cloudflare,gitlab,security}_v2.md`
— **có cột `archived_at`**, ghi rõ **ngày chụp `2026-10-01T15:28Z`**.
**Bản gốc GIỮ NGUYÊN** — blob trước/sau y hệt:
`scope_github.md 15c946ff…` · `scope_cloudflare.md 62cb927e…` · `scope_security.md aec4f6dc…` ·
`scope_gitlab.md 22e3dc7d…` (không sửa, không xoá).

### 1.3 Sáu dòng "Chưa verify" (T36)
6 dòng → `✅ Đã verify — T14 PASS` (căn cứ `reviews/CROSS.md` §2.8 + mốc `03d304b` + merge `4642e3c`).
`grep -rn 'Chưa verify|Chưa được verify' security/` → **0**. **Ghi chú "supersede" ở
`gitlab/SCOPE.md` §2b GIỮ NGUYÊN** (đã kiểm bằng grep; thêm 1 ghi chú mới ở §0 trỏ tới nó).

### 1.4 Ba khuyết điểm mức thấp của T31 (sửa **báo cáo**, KHÔNG sửa `EVIDENCE/**`)
- **(a)** `FIX_GROUP_B.md` §2 ghi blob cũ `ac04b460` → sửa thành **`095006ce`** (blob cuối).
  Kiểm theo commit: `52e96ea…209c308` = `ac04b460`; `9455f89`,`ecce293` = `095006ce`.
- **(b)** `history_check.txt` §(B) ghi *"3 commit"* mà chỉ liệt kê **2** → **sửa SCRIPT**
  (`history_check_t31.py`): nay in `DA KIEM` / `BO QUA` (tách 2 lý do) / `tong = kiem + boqua`
  ⇒ **3 = 2 + 0 + 1**. Bản `EVIDENCE/history_check.txt` **giữ nguyên** (bản ghi lịch sử).
- **(c) TÔI TỰ TÌM THÊM (chưa ai nêu):** `verify_t31.py` in nhãn `blob TRUOC (HEAD)` nhưng **giá trị
  là `HEAD`** trong khi **phép so dùng `merge-base`** ⇒ **nhãn SAI** — chính là nguồn gây lệch
  `ac04b460` vs `095006ce`. Đã sửa: in rõ **cả** `blob DOI CHIEU (merge-base)` **và** `blob HEAD`.

---

## 2. Băm từng phần (CẢ HAI quy ước) + vùng nguyên văn

**Quy ước ranh giới (ghi rõ):** `dòng = str.splitlines()` (bỏ `\n` cuối dòng);
`vùng = "\n".join(dòng_a..dòng_b)`, 1-based, hai đầu ĐÓNG, KHÔNG `\n` ở cuối vùng;
vùng "đã sửa" xác định bằng `difflib`; **mỗi vùng băm theo CẢ HAI quy ước** (A không `\n` cuối /
B có `\n` cuối) ⇒ kết luận không phụ thuộc quy ước.

`EVIDENCE/verify_t34.txt`:
- **[1]** 10 file — **mọi vùng không đổi GIỐNG HỆT** theo cả A và B ⇒ `True`.
- **[2]** **VÙNG NGUYÊN VĂN BẢO VỆ** = khối fence đầu tiên sau tiêu đề (KHÔNG phải "cả mục",
  vì T37 chèn khối không-nguyên-văn vào trong mục): tất cả **GIONG HET** —
  `gitlab §1 policy prose` · `gitlab §3` · `gitlab §4` · `github §1 in-scope` · `github §4b` ·
  `cloudflare §3` · 3 bảng DNS của 3 `RECON.md`.
- **[2b]** **VÙNG ĐƯỢC PHÉP ĐỔI (D-027 yêu cầu)** — `gitlab §1`, `gitlab §2a`, `cloudflare §1a`:
  cả 3 **ĐÃ ĐỔI** đúng yêu cầu.
- **[4]** `scope_github.md` = **`15c946ff956a3fdb466f7f9768081af29b812088`** (khớp `HEAD` + `main`).

> 🔎 **Trung thực — tôi sửa 4 lỗi trong chính bộ kiểm của mình:** (i) vùng §1 policy prose chọn
> nhầm fence đầu (bắt cả khối đã sửa); (ii) gọi vùng bằng "tiêu đề→tiêu đề" nên bắt cả khối `[3b]`
> mới chèn → báo KHÁC sai; (iii) 2 vùng D-027 **buộc phải đổi** lại nằm trong danh sách "không đổi";
> (iv) để sót 1 dòng `PROTECTED` trùng. Đã sửa hết và **giữ dấu vết trong output**.

---

## 3. Quét theo NGHĨA toàn territory (D-025 [3a]) — JOIN với BẢNG NGUỒN

`EVIDENCE/semantic_scan.txt` (script `semantic_scan_t34.py`). Tài liệu sống: 3 `SCOPE.md` +
3 `RECON.md` + `T3/CANDIDATES.md`.

**DELTA = 5, và nguyên nhân gốc là BẢNG NGUỒN THIẾU — không phải câu văn sai:**

| # | DELTA | Bằng chứng |
|---|---|---|
| 1 | `T28` được trích nhưng **không có** trong `ADMIN/ASSIGNMENTS.md` | `gitlab/SCOPE.md:12,190,192,211,214` · `CANDIDATES.md:69` |
| 2 | `T31` — như trên | `CANDIDATES.md:66,69` |
| 3 | `T32` — như trên | `gitlab/SCOPE.md:55,68` |
| 4 | `T34` — như trên | `gitlab/SCOPE.md:12,45,54` · `CANDIDATES.md:44` |
| 5 | `T37` — như trên | `github/SCOPE.md:112` |

⇒ **Nguyên nhân gốc (tự đo):** `ADMIN/ASSIGNMENTS.md` chỉ có **T1…T26**;
**T27 trở đi KHÔNG nằm trong bảng** — chúng chỉ tồn tại dưới dạng **tin nhắn phòng**.
⇒ Theo đúng D-025 [3a] ("nguồn sự thật là BẢNG"), **bảng task trong file KHÔNG đủ làm nguồn sự thật**.

**Phát hiện thứ hai (cùng lớp, tôi tự tìm):** `rooms/ab1-478d-cfa7/directives.md` **THIẾU 7 chỉ thị**
`D-015 D-016 D-017 D-018 D-019 D-020 D-024` — chúng chỉ có trong phòng, không có trong file.
(D-021 **có** trong file.)

> ❗ **3 FALSE POSITIVE của bộ quét — đã sửa và báo rõ:** (i) chỉ nhận `[D-0NN]` dạng tiêu đề
> nên báo oan `D-021` (có trong file, chỉ khác định dạng); (ii) báo oan dòng 5 `CANDIDATES.md`
> *"dùng D-005 cho trạng thái G4"* — dòng đó **đã** nêu D-013; (iii) báo oan `license.gitlab.com`
> *"vẫn gọi trong scope"* — dòng 44 **đã** gạch bỏ và ghi `SAI: ĐÃ NGHỈ HƯU`.

---

## 4. Giới hạn tôi TỰ GIỮ (D-026 + tiêu chí REJECT LOG #95)

- ❌ **KHÔNG** nói 153/156 (GitHub), 4 (Cloudflare), 5 (GitLab) bản ghi là *"ngoài scope"*.
  ✅ Chỉ khẳng định: **bảng THIẾU chiều `archived_at` ⇒ KHÔNG PHÂN BIỆT ĐƯỢC**.
- ❌ **KHÔNG** nói bản ghi *"không còn hiệu lực / đã bị loại"*.
  ✅ Chỉ nói: **có `archived_at`; hiệu lực CHƯA XÁC MINH**.
- ❌ **KHÔNG** suy ra *"đừng khai thác"* từ `archived_at`.
  ✅ Nêu **`DISSENT-12` — ngữ nghĩa `sub=True` trên bản ghi archived CHƯA XÁC MINH**;
  cần **trả lời chính thức từ chương trình**.
- ✅ Câu *"vẫn loại cả 4 tài sản khỏi T4"* ở §2b **là ĐÚNG và GIỮ NGUYÊN** — dựa trên **quyết định
  `D-021` của Admin**, **không** phải suy luận từ `archived_at`.

---

## 5. Việc CHƯA làm / cần Admin

1. **`_v2` cho `scope_security.md`** đã sinh (34 live + 39 arch, orphan 31) nhưng chương trình
   HackerOne `security` **không nằm trong 3 chương trình T3** — tôi vẫn sinh vì D-027 nêu tên nó
   trong "4 file CAPTURE liên quan". Nếu Admin thấy không cần, xin chỉ thị.
2. **`github §1b` = 183 dòng** — bảng dài; nếu Admin muốn rút gọn (ví dụ chỉ liệt kê orphan),
   xin chỉ thị.
3. **Bảng nguồn thiếu** (§3): `ASSIGNMENTS.md` dừng ở T26; `directives.md` thiếu D-015…D-020, D-024.
   Đây là **việc của Admin** (ngoài territory tôi) — tôi chỉ báo.
4. **Reviewer1 verify tại head cuối** (T35/T38).

**G4 vẫn ĐÓNG. Không chạm hệ thống thật. Không merge `main`.**
