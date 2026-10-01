# T28 — Sửa nhãn §2b của `security/gitlab/SCOPE.md`

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T28 · **Nhánh:** `agent/bounty-recon/T28`
**Chỉ thị:** D-021 (msg #141/#142) · **`main` gốc:** `8006168` · **Ngày:** `2026-10-01`
**Territory:** `security/**`, `agents/bountyrecon/**`

> ⚠️ **Chưa verify — chờ Reviewer1 (vòng sau).** Tôi không tự verify (D-004).

---

## 0. Tuyên bố hiệu lực chứng thực — Admin yêu cầu ghi rõ

> **Thay đổi này supersede chứng thực T14 ở RIÊNG §2b; phần trích nguyên văn không đổi nên
> chứng thực byte-exact vẫn nguyên giá trị cho phần đó.**

Cụ thể: §1 (in-scope nguyên văn), §2a (out-of-scope nguyên văn), §3 (quy định cấm),
§4 (mức thưởng) **KHÔNG bị chạm một byte nào**. Chứng thực T14 byte-exact vẫn nguyên giá trị
cho các phần đó. Chỉ **thân §2b** được viết lại ⇒ chứng thực cũ ở §2b hết hiệu lực, và
**chỉ ở §2b**.

---

## 1. Đã sửa gì (CHỈ §2b)

| | Trước | Sau |
|---|---|---|
| Nhãn | `## 2b. 🚨 XUNG ĐỘT SCOPE ĐÃ XÁC MINH — KHÔNG ĐƯỢC ĐOÁN` | `## 2b. TÀI SẢN ĐÃ NGHỈ HƯU — **0 XUNG ĐỘT HIỆU LỰC** (đã đính chính ở T28)` |
| Nội dung | Bảng "Dòng IN / Dòng OUT" + kết luận *"mâu thuẫn trong dữ liệu công trình"* | Đính chính + nguyên nhân gốc M-01 + bảng có cột **`archived_at`** + bằng chứng thô tái lập |
| `archived_at` | **không có** | **có** — bảng 4 dòng kèm `archived_at` từng vế OUT |

Thêm 2 tiểu mục trong §2b: `### Nguyên nhân gốc — bài học M-01 (Auditor2 T24)` và
`### Bằng chứng thô — tự tái lập (T28)`. Thêm dòng dẫn chiếu `security/_TEMPLATE/SCOPE.md`
xác nhận **`archived_at` của MỌI asset là trường BẮT BUỘC**.

---

## 2. Bằng chứng thô — chỉ §2b đổi, vùng nguyên văn nguyên vẹn

Nguồn: `EVIDENCE/verify_section2b.txt`.

### 2.1 Blob hash trước / sau

```text
$ git rev-parse HEAD:security/gitlab/SCOPE.md      # blob TRUOC
  9eafa8d050f51727148853e48d916190c66fd3ca
$ git hash-object security/gitlab/SCOPE.md         # blob SAU
  c6b1131d498fd694acd62b648c9644824c3f6492
```
⇒ blob **khác nhau là ĐÚNG** (thân §2b đã viết lại). Điều cần chứng minh **không phải** blob
giống nhau, mà là **các phần ngoài §2b giống nhau** — xem 2.2.

### 2.2 Tách file tại ranh giới §2b và băm từng phần (đây là phép kiểm quyết định)

```text
  PHAN                          sha256 TRUOC        sha256 SAU          KET QUA
  TRUOC §2b (truoc dong '## 2b.')  09fce4b8afac0ede    09fce4b8afac0ede    GIONG HET ✅
    §2b (than muc)                 2f7322f812e7e249    099b489f47f5e953    KHAC ⚠️
  SAU §2b (tu '## 3.' tro di)      40904074229cbabc    40904074229cbabc    GIONG HET ✅

  do dai TRUOC: pre=8284 mid=1695 suf=5490  tong=15469
  do dai SAU  : pre=8284 mid=3164 suf=5490  tong=16938

  => VUNG TRICH NGUYEN VAN (pre + suf) KHONG DOI: True
  => chi than §2b thay doi: True
```

**Diễn giải:** `pre` = mọi thứ trước dòng `## 2b.` (gồm §0, §1, §2, §2a);
`suf` = mọi thứ từ `## 3.` trở đi (gồm §3, §4, §5).
**`pre` và `suf` GIỐNG HỆT TỪNG BYTE.** `pre` dài **8284** ký tự ở cả hai bản, `suf` dài **5490**
ở cả hai bản ⇒ không byte nào ngoài §2b bị dịch chuyển hay sửa.

### 2.3 `git diff` — mọi hunk đều nằm trong §2b

```text
$ git diff -U0 HEAD -- security/gitlab/SCOPE.md | grep -E '^@@'
  @@ -146 +146 @@          <- dong tieu de §2b
  @@ -148,2 +148,6 @@
  @@ -151 +155,31 @@
  @@ -153,18 +187,14 @@   <- ket thuc o dong 170 (cuoi §2b cu)
$ git diff --stat HEAD -- security/gitlab/SCOPE.md
   security/gitlab/SCOPE.md | 74 ++++++++++++++++++++++++++++++++--------------
   1 file changed, 52 insertions(+), 22 deletions(-)
```
§2b cũ = dòng **146–170**. Hunk cuối là `-153,18` ⇒ phủ dòng 153–170 ⇒ **nằm trọn trong §2b**.
Không có hunk nào chạm dòng 1–145 hoặc 171+.

### 2.4 Không chạm file bị cấm và không chạm file nào khác

```text
$ git diff --exit-code HEAD -- agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md ; echo exit=$?
  exit=0                       # 0 = KHONG chạm (3 link thieu scheme dong 185 van nguyen)

$ git status --short
   M security/gitlab/SCOPE.md
  ?? agents/bountyrecon/tasks/T28/
```
⇒ **Đúng 1 file được sửa.** Không file nào khác trong repo bị ảnh hưởng.

---

## 3. Bằng chứng thô cho nhãn mới (tự tái lập) — Admin yêu cầu dán lại

`POST https://hackerone.com/graphql` (công khai, không auth), `team(handle:"gitlab")`:

```text
archived:false -> tong 44   IN=19   OUT=25
IN giao OUT (theo asset_identifier): 0        <-- KHONG con xung dot nao

archived:true  -> tong 19
   *.gitlab.net      type=URL  eligible=False  archived_at=2022-07-21T15:51:33.499Z
   *.gitlap.com      type=URL  eligible=False  archived_at=2022-07-21T15:51:16.877Z
   about.gitlab.com  type=URL  eligible=False  archived_at=2022-07-21T15:53:03.572Z
   docs.gitlab.com   type=URL  eligible=False  archived_at=2022-07-21T15:53:13.475Z
```

Và xác nhận `archived_at` **có** trong schema công khai (nên đây không phải giới hạn công cụ):

```text
$ {__type(name:"StructuredScope"){fields{name}}}  ->  archived_at = True
```

Số liệu này **khớp** kết luận Auditor2 (T24) và bản tôi đã trình ở ACK D-021 (msg #143).

---

## 4. 📌 PHÁT HIỆN — 3 dòng cũ CÒN SÓT **NGOÀI §2b** (tôi KHÔNG sửa, xin Admin quyết)

Chỉ thị T28 ghi rõ **"Sửa CHỈ §2b"**, nên tôi **giữ nguyên** và báo cáo.
Bằng chứng: `EVIDENCE/residual_old_wording.txt`. Cả 3 dòng **đã có từ trước T28**
(đã đối chiếu `git show HEAD:…` ⇒ **không phải do tôi tạo ra**).

| # | Vị trí | Dòng (nguyên văn) | Vấn đề |
|---|---|---|---|
| A | **dòng 9** (khối Tiêu đề/Trạng thái, §0) | `**Trạng thái:** ⚠️ **Trích được nguyên văn, NHƯNG có 4 XUNG ĐỘT scope — xem §2b. PHẢI HỎI ADMIN.**` | Vẫn khẳng định "4 XUNG ĐỘT" + "PHẢI HỎI ADMIN" — nay đã có phán quyết |
| B | **§5, dòng 284** | `\| Trích được nguyên văn in-scope? \| ✅ **CÓ** (24 tài sản) — nhưng 4 tài sản bị xung đột \|` | Vẫn gọi "xung đột" |
| C | **§5, dòng 289** | `\| Đủ điều kiện chuyển ExploitDeep (T4)? \| ⚠️ **CÓ ĐIỀU KIỆN** — phải chốt 4 xung đột ở §2b trước \|` | Vẫn nói "phải chốt 4 xung đột" — việc chốt **đã xong** (loại cả 4, D-021) |

**Kiểm chứng nằm ngoài §2b:** `## 2b.` ở dòng **146**, `## 3.` ở dòng **204** ⇒ §2b = dòng 146–202;
cả 3 dòng trên đều **ngoài** khoảng đó.

> ⚠️ **Hệ quả nếu để nguyên:** tài liệu **tự mâu thuẫn** — §2b nói "0 xung đột hiệu lực" nhưng
> dòng 9 nói "4 XUNG ĐỘT … PHẢI HỎI ADMIN". Người đọc sau sẽ tin dòng 9 (nó ở đầu file).
> **Đây là cùng loại rủi ro "di chuyển mục tiêu" mà tôi đã tránh ở T26.**
>
> **Tôi KHÔNG tự sửa vì chỉ thị giới hạn ở §2b.** Xin Admin chọn:
> **(1)** cho tôi sửa 3 dòng này trong một task riêng (dòng 9 + 2 dòng §5),
> **(2)** Admin tự sửa, hoặc **(3)** giữ nguyên và ghi đính chính ở `ADMIN/`.
>
> *Lưu ý kỹ thuật:* dòng 9 và §5 **không phải** văn bản trích nguyên văn — chúng là phần
> **tổng hợp của tôi**. Sửa chúng **không** ảnh hưởng cơ sở pháp lý của các khối trích dẫn.

---

## 5. Kết luận

| Yêu cầu T28 | Kết quả |
|---|---|
| 1. Sửa CHỈ §2b, nhãn đúng "0 xung đột hiệu lực + 4 đã nghỉ hưu", thêm `archived_at` | ✅ |
| 2. KHÔNG chạm phần trích nguyên văn; kiểm bằng blob hash trước/sau | ✅ `pre`+`suf` **giống hệt từng byte**; blob khác đúng như dự kiến |
| 3. Ghi câu tuyên bố hiệu lực chứng thực | ✅ §0 |
| 4. Dán lại output thô `archived:false` | ✅ §3 |
| — Phát hiện thêm | 📌 §4: 3 dòng cũ ngoài §2b (giữ nguyên, xin Admin quyết) |

**G4 vẫn ĐÓNG. Không chạm hệ thống thật. Không merge `main`.**
