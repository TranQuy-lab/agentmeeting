# T31 — Dọn nhóm B: `RECON.md` 5 dòng + `CANDIDATES.md` §2

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T31 · **Nhánh:** `agent/bounty-recon/T31`
**Chỉ thị:** D-023 (msg #176) · **`main` gốc (merge-base):** `6d47749` · **Ngày:** `2026-10-01`
**Territory:** `security/**/RECON.md`, `security/**/SCOPE.md`, `agents/bountyrecon/**`

> ⚠️ **Chưa verify — chờ Reviewer1.** Tôi không tự verify (D-004).

---

## 0. Tuyên bố hiệu lực chứng thực (Admin yêu cầu ghi rõ)

> **Thay đổi này supersede chứng thực T14/T27 ở RIÊNG các dòng đã sửa; phần trích nguyên văn
> không đổi nên chứng thực byte-exact vẫn nguyên giá trị cho phần đó.**

Cụ thể: mọi khối **trích nguyên văn** trong `security/gitlab/SCOPE.md` (§1, §2a, §3, §4) và
`security/gitlab/RECON.md` (§1.1, §1.2, §2.3, §2.4) **không bị chạm một byte nào**.

---

## 1. Đã sửa gì (CHỈ file sống)

### 1.1 `security/gitlab/RECON.md` — 3 dòng bảng + §5 mục 2

| Dòng | TRƯỚC | SAU |
|---|---|---|
| **39** | `about.gitlab.com` \| `⚠️ **XUNG ĐỘT** (§2b SCOPE)` | `✅ URL (medium) — **Admin loại khỏi T4** (§2b)` |
| **40** | `docs.gitlab.com` \| `⚠️ **XUNG ĐỘT** (§2b SCOPE)` | `✅ URL (medium) — **Admin loại khỏi T4** (§2b)` |
| **47** | `gitlab.net` \| `⚠️ **XUNG ĐỘT** (§2b SCOPE)` | `⛔ **NGOÀI scope** (apex đã nghỉ hưu `2020-10-05`) — nhưng `*.gitlab.net` **trong scope** (medium)` |
| **206–210** (§5 mục 2) | `**4 tài sản bị XUNG ĐỘT scope** … **trước khi** phát hiện xung đột. ⛔ … **Cần Admin phán quyết.**` | `**4 tài sản đã được Admin loại khỏi T4** … **0 xung đột hiệu lực**: vế OUT là bản ghi **đã nghỉ hưu** (archived_at 2022-07-21) … ⛔ **Phán quyết đã xong (D-021): CẤM chạm 4 tài sản này trong T4.**` |

> 🔎 **Sửa thêm một lỗi THẬT ở dòng 47 (không chỉ đổi tên):** `gitlab.net` (apex) **không** thuộc
> 4 tài sản "xung đột" — nó là **bản ghi riêng đã nghỉ hưu `2020-10-05`** (khác hẳn `2022-07-21`).
> `*.gitlab.net` (WILDCARD) thì **trong scope**. Nhãn cũ "XUNG ĐỘT" gộp nhầm hai chuyện khác nhau.
> Dữ liệu: query `archived:true` → `gitlab.net type=URL eligible=False archived_at=2020-10-05T18:32:21.936Z`.

### 1.2 `agents/bountyrecon/tasks/T3/CANDIDATES.md` — dòng 19, 21, 64–82

| Dòng | TRƯỚC | SAU |
|---|---|---|
| **19** | `\| 4 \| Chốt 4 **xung đột scope** … \| ⏸ **CHƯA** — **CẦN ADMIN PHÁN QUYẾT** \|` | `\| 4 \| GitLab: **0 xung đột hiệu lực** — vế OUT là bản ghi đã nghỉ hưu (`archived_at` 2022-07-21); Admin đã **loại cả 4 tài sản khỏi T4** \| ✅ **XONG** \|` |
| **21** | `**⇒ Chưa đủ 4/4. ĐỀ NGHỊ CHƯA MỞ T4.**` | `**⇒ Điều kiện còn thiếu duy nhất: chỉ thị nêu target cụ thể của Admin (D-013). G4 vẫn ĐÓNG.**` |
| **64** | `## 2. 🚨 VẤN ĐỀ CHẶN — 4 XUNG ĐỘT SCOPE CỦA GITLAB (CẦN ADMIN PHÁN QUYẾT)` | `## 2. GitLab — **0 xung đột hiệu lực**; 4 tài sản đã nghỉ hưu (ĐÃ PHÁN QUYẾT)` |
| **66–82** | `Đã xác minh … 4 tài sản nằm **đồng thời** …` + bảng thiếu `archived_at` + `**Đề nghị Admin chọn 1 trong 2:** (a)/(b)` | Ghi chú đính chính + bằng chứng `44 entry · IN=19 · OUT=25 · giao = 0` + **bảng có cột `archived_at`** + `⛔ **QUYẾT ĐỊNH CỦA ADMIN (giữ nguyên): loại cả 4 tài sản khỏi T4.**` + điều kiện mở T4 = **chỉ thị target (D-013)** |

**Đã bỏ hoàn toàn** khối *"Đề nghị Admin chọn (a)/(b)"* — câu hỏi đã được trả lời.

---

## 2. Bằng chứng thô — băm từng phần (D-023 phép kiểm [2], phần 2 điểm)

Nguồn: `EVIDENCE/verify_regions.txt` (script tái lập: [`verify_t31.py`](verify_t31.py)).

### QUY ƯỚC RANH GIỚI (ghi rõ — Reviewer1 từng lệch 1 ký tự vì quy ước khác)

```text
* Tách file thành DÒNG bằng `str.splitlines()`  -> BỎ ký tự kết thúc dòng (\n, \r\n).
* Một "VÙNG" = "\n".join(dòng_a .. dòng_b), 1-based, HAI ĐẦU ĐÓNG (inclusive),
  KHÔNG có ký tự \n ở cuối vùng.
* Vùng "đã sửa" xác định bằng difflib.SequenceMatcher (opcodes replace/delete/insert)
  — KHÔNG đoán số dòng bằng tay.
* ĐỂ TRIỆT TIÊU MỌI TRANH CÃI VỀ 1 KÝ TỰ: mỗi vùng được băm theo CẢ HAI quy ước
      (A) KHÔNG \n ở cuối     (B) CÓ \n ở cuối
  Nếu cả A và B đều khớp trước/sau  =>  kết luận KHÔNG phụ thuộc quy ước.
```

### Kết quả

```text
FILE security/gitlab/RECON.md   blob 5c088a23 -> 75f163cf   dong 213 -> 214
  opcodes khac: replace 39..40 | replace 47..47 | replace 206..209 -> 206..210
  VUNG KHONG DOI (A/B deu GIONG HET):
    V0 dong 1..38     776ef897/776ef897   |  77d226b5/77d226b5
    V1 dong 41..46    84baedad/84baedad   |  ff105a98/ff105a98
    V2 dong 48..205   28f7abc2/28f7abc2   |  5efe5dea/5efe5dea
    V3 dong 210..213  4e126826/4e126826   |  eb8682aa/eb8682aa

FILE agents/bountyrecon/tasks/T3/CANDIDATES.md  blob 95d16d76 -> 095006ce  dong 118 -> 121
  opcodes khac: 19 | 21 | 64 | 66..67 | 69->69..73 | 71..74 | 76..77 | 79..82
  VUNG KHONG DOI (A/B deu GIONG HET):
    V0 dong 1..18     5aa4af3d/5aa4af3d   |  1f90b9bf/1f90b9bf
    V1 dong 20        e3b0c442/e3b0c442   |  01ba4719/01ba4719
    V2 dong 22..63    91d499bd/91d499bd   |  2a0b7549/2a0b7549
    V3 dong 65        e3b0c442/e3b0c442   |  01ba4719/01ba4719
    V4 dong 68        e3b0c442/e3b0c442   |  01ba4719/01ba4719
    V5 dong 70->74    4da1ec6f/4da1ec6f   |  831fe3c0/831fe3c0
    V6 dong 75->79    e3b0c442/e3b0c442   |  01ba4719/01ba4719
    V7 dong 78->83    e3b0c442/e3b0c442   |  01ba4719/01ba4719
    V8 dong 83..118   6dadecbe/6dadecbe   |  cc2de093/cc2de093

TONG dong da sua (2 file): 23
KET LUAN: moi vung khong doi GIONG HET theo CA HAI quy uoc: True
```
(`e3b0c442…` = sha256 của chuỗi RỖNG — các vùng 1 dòng trống, đúng như dự kiến.)

> 🔄 **ĐÍNH CHÍNH (T34) — khuyết điểm mức thấp (a), Reviewer1 nêu ở T32.**
> Bản đầu dòng trên ghi `blob … -> ac04b460`. **SAI:** `ac04b460` là blob **TRUNG GIAN**
> (đúng cho các commit `52e96ea`→`209c308`), nhưng **blob CUỐI** là **`095006ce`** — sau commit
> `9455f89` tôi **tự sửa dòng 21** (bỏ chữ *"duy nhất"*). `EVIDENCE/verify_regions.txt` ghi đúng
> `095006ce`; **báo cáo ↔ bằng chứng đã mâu thuẫn**, nay đã khớp.
> Kiểm chứng blob theo từng commit: `52e96ea`,`81a56e4`,`683e31f`,`209c308` → `ac04b460…`;
> `9455f89`,`ecce293` → `095006ce…`. **`EVIDENCE/**` KHÔNG bị sửa** (theo đúng chỉ thị).
>
> 🔎 **Tôi còn tự tìm thêm 1 khuyết điểm cùng họ (chưa ai nêu):** `verify_t31.py` in nhãn
> `blob TRUOC (HEAD)` nhưng **giá trị là blob của `HEAD`**, trong khi **phép so dùng `merge-base`**
> ⇒ **nhãn SAI** (đây chính là nguồn gây lệch `ac04b460` vs `095006ce` khi đọc báo cáo).
> Đã sửa script: in rõ **cả** `blob DOI CHIEU (merge-base …)` **và** `blob HEAD`.

---

## 3. Bằng chứng thô — KIỂM THEO LỊCH SỬ, không chỉ 2 điểm (bịt kẽ hở K1)

Nguồn: `EVIDENCE/history_check.txt` (script: [`history_check_t31.py`](history_check_t31.py)).
Đây là **D-023 phép kiểm [2]** — mục đích: một commit trung gian *"sửa rồi revert"* sẽ **lọt**
phép so 2 điểm (trước/head) nhưng **bị bắt ở đây**.

```text
branch agent/bounty-recon/T31   merge-base 6d47749   head 81a56e4

(A) MOI COMMIT CUA NHANH T31 — file bi cham
  so commit: 2
    commit 81a56e4d  OK agents/bountyrecon/tasks/T31/EVIDENCE/history_check.txt
                     OK agents/bountyrecon/tasks/T31/history_check_t31.py
    commit 52e96eaa  OK agents/bountyrecon/tasks/T3/CANDIDATES.md
                     OK agents/bountyrecon/tasks/T31/EVIDENCE/verify_regions.txt
                     OK agents/bountyrecon/tasks/T31/verify_t31.py
                     OK security/gitlab/RECON.md
  => moi file bi cham nam trong danh sach CHO PHEP: True
  => file bi LOAI TRU bi cham: 0
     (DANH SACH LOAI TRU: T28/FIX_2B.md, T29/*, moi EVIDENCE/** khac)

(B) CHUOI COMMIT DA CHAM security/gitlab/SCOPE.md — bam vung NGUYEN VAN moi commit
  commit cham security/gitlab/SCOPE.md (TOAN BO lich su): 3
  (chi KIEM commit co >=1 cha VA co du heading; commit khac bi BO QUA va dem rieng)
    commit        parent        nguyen van (cha)   nguyen van (commit)  KET QUA
    1b318ded14f3  9f73655d9f3e  05235b2a064277b4   05235b2a064277b4     GIONG HET
    9f73655d9f3e  8006168b2f00  05235b2a064277b4   05235b2a064277b4     GIONG HET
  => DA KIEM: 2  |  BO QUA: 0 (khong co cha) + 1 (thieu heading)
  => tong 3 = 2 + 0 + 1
  => so DONG liet ke o tren = DA KIEM (2), KHONG phai tong (3)
  => VUNG TRICH NGUYEN VAN cua SCOPE.md KHONG DOI qua MOI commit: True

(C) scope_github.md
  HEAD:... -> 15c946ff956a3fdb466f7f9768081af29b812088
  main:... -> 15c946ff956a3fdb466f7f9768081af29b812088
  => KHOP CA HAI
```

**VÙNG TRÍCH NGUYÊN VĂN của `SCOPE.md`** ở phép kiểm (B) được định nghĩa là
`[từ dòng '## 1.' .. trước '## 2b.'] + [từ '## 3.' .. trước '## 5.']` — tức §1+§2+§2a+§3+§4,
**cố ý loại §2b** (đã sửa ở T28), §0 và §5 (là phần tổng hợp, không phải nguyên văn).
⇒ Không commit nào trong chuỗi T28→T29 đụng vào vùng nguyên văn ⇒ **kẽ hở K1 đã được bịt**.

> 🔄 **ĐÍNH CHÍNH (T34) — khuyết điểm mức thấp (b), Reviewer1 nêu ở T32.**
> Bản đầu in `so commit cham SCOPE.md: 3` rồi **chỉ liệt kê 2 dòng** ⇒ **con số không khớp số dòng**.
> **Nguyên nhân:** con số in ra là **TỔNG** commit chạm file (3), còn vòng lặp **bỏ qua** commit
> thiếu cha hoặc thiếu heading (ở đây **1 bị bỏ qua vì thiếu heading**).
> **Đã sửa trong `history_check_t31.py`** (script, **KHÔNG** phải `EVIDENCE/**`): nay in rõ
> `DA KIEM`, `BO QUA` (tách 2 lý do) và phép cộng `tong = kiem + boqua`.
> **`EVIDENCE/history_check.txt` giữ nguyên** (là bản ghi lịch sử) — theo đúng chỉ thị.

---

## 4. Trung thực — tôi tự phát hiện và sửa **1 phép thử SAI** của chính mình

Bản đầu của `history_check_t31.py` lọc "file bị cấm bị chạm" bằng điều kiện `"/EVIDENCE/" in f`
⇒ nó **bắt nhầm chính `agents/bountyrecon/tasks/T31/EVIDENCE/`** — là **bằng chứng HỢP LỆ của T31** —
và báo *"file bị LOẠI TRỪ bị chạm: 1"*. **SAI.** Đã sửa: loại tiền tố `T31/` khỏi phép thử.
Sau khi sửa: **0**. Giữ lại cả dấu vết trong output để Reviewer1 soi.

---

## 5. Kết luận

| Yêu cầu T31 | Kết quả |
|---|---|
| 1. Nội dung mới đúng "0 xung đột hiệu lực + 4 đã nghỉ hưu"; điều kiện T4 = chỉ thị target (D-013) | ✅ |
| 2. Chứng minh bằng băm từng phần; ghi rõ quy ước ranh giới; vùng ngoài chỗ sửa GIỐNG HỆT | ✅ **cả 2 quy ước** (A không `\n` cuối / B có `\n` cuối) |
| 3. Kiểm theo **LỊCH SỬ** (D-023 [2]) — bịt kẽ hở K1 | ✅ mọi commit của nhánh + mọi commit chạm `SCOPE.md` |
| 4. Ghi câu tuyên bố hiệu lực chứng thực | ✅ §0 |
| 5. `scope_github.md` blob vẫn `15c946ff…` | ✅ khớp cả `HEAD` lẫn `main` |
| — Không sửa bản ghi lịch sử | ✅ 0 file bị loại trừ bị chạm |
| — Phát hiện thêm | 🔎 dòng 47 sửa **một lỗi thật** (apex `gitlab.net` nghỉ hưu `2020-10-05`, khác `2022-07-21`) |

**G4 vẫn ĐÓNG. Không chạm hệ thống thật. Không merge `main`.**
