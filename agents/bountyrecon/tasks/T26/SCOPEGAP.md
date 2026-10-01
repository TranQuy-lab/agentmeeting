# T26 — SCOPEGAP: báo cáo KHOẢNG TRỐNG PHẠM VI

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T26 · **Nhánh:** `agent/bounty-recon/T26`
**Ngày:** `2026-10-01` · **`main` gốc:** `e8c45a0`
**Yêu cầu 3 của D-020:** *"Nếu bạn thấy khoảng trống tương tự ở chỗ khác, nêu ra."*

> ⚠️ **Chưa verify — chờ Reviewer1.** Mỗi mục dưới đây kèm lệnh thô; mục nào chưa chắc tôi ghi rõ.

---

## GAP-0 — XÁC NHẬN khoảng trống Admin đã nêu

**T14 PASS T3 nhưng chỉ kiểm nội dung `SCOPE.md`, không kiểm link.**

Tôi xác nhận khoảng trống này là **thật và có thể định lượng**:

| Số liệu | Giá trị |
|---|---|
| File trong territory T3 (`agents/bountyrecon/**` + `security/**`) | 24 |
| Link tương đối trong file do tôi viết | 10 |
| Link tương đối **chết** | **3** |
| Tỉ lệ link hỏng | **30 %** |

Nếu T14 (hoặc bất kỳ vòng review nào) có bước **kiểm cơ học** "mọi link tương đối trong file
thay đổi phải giải được", 3 lỗi này đã bị bắt ở T14. Nhưng T14 **không có** bước đó — và
**đó là khoảng trống của quy trình, không phải lỗi của Reviewer1** (đồng ý với cách Admin ghi nhận).

---

## GAP-1 — 🚨 D-020 §2 QĐ-2 trỏ vào một đường dẫn **KHÔNG TỒN TẠI**

D-020 viết:

> *"KHÔNG sửa 3 link thiếu `https://` trong `security/github/EVIDENCE/scope_github.md` dòng 185."*

**Kiểm chứng (`EVIDENCE/path_discrepancy.txt`):**

```text
$ test -f security/github/EVIDENCE/scope_github.md
  -> FALSE  <= KHONG TON TAI
$ ls -la security/github/EVIDENCE/
  -> ls: cannot access 'security/github/EVIDENCE/': No such file or directory

$ test -f agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md
  -> TRUE  <= duong dan THAT
$ git ls-files | grep 'scope_github.md'
  -> agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md
```

**Đánh giá công bằng — phần ĐÚNG của D-020:**

| Khẳng định của D-020 | Kiểm chứng |
|---|---|
| "dòng **185**" | ✅ **ĐÚNG** — `sed -n '185p'` đúng là hàng `\| OTHER \| LGTM \|` |
| "**3** link thiếu `https://`" | ✅ **ĐÚNG** — đúng 3: `lgtm-com.pentesting.semmle.net`, `backend-dot-lgtm-penetration-testing.appspot.com`, `downloads.lgtm.com` |
| Quyết định **giữ nguyên** | ✅ **ĐÚNG** — tôi đã giữ, sha256 trùng `main` |
| Đường dẫn `security/github/EVIDENCE/…` | ❌ **SAI** — không tồn tại |

⇒ **Nội dung chỉ thị đúng, chỉ sai đường dẫn.** Không có hậu quả thực tế vì tôi tìm được file
bằng `git ls-files`. Nhưng xem GAP-2 để thấy đây **không phải tai nạn ngẫu nhiên**.

> 📌 Đây là **lần thứ TƯ** ở cùng một dạng. D-020 §4 tự ghi nhận *"lần thứ ba Admin trỏ bằng
> chứng vào thứ chưa có"* (DISSENT-5/LOG #6, F-04, SUMMARY.md). Nay thêm lần này.
> **Mẫu lỗi chưa được chặn ở gốc** — xem GAP-2.

---

## GAP-2 — 🚨 NGUYÊN NHÂN GỐC: quy tắc territory và quy tắc vị trí bằng chứng **MÂU THUẪN**

**Chỉ thị T3 của tôi có hai dòng mâu thuẫn nhau:**

- §3 (territory): `security/**/SCOPE.md`, `security/**/RECON.md`, `agents/bountyrecon/**`
  — kèm câu **"CẤM ghi ngoài territory"**.
- §5 (luật bằng chứng): *"Mọi khẳng định phải kèm bằng chứng thô trong `security/<program>/EVIDENCE/`"*.

Nhưng `security/**/EVIDENCE/**` **nằm trong territory T4 của ExploitDeep**
(`ADMIN/ASSIGNMENTS.md` hàng T4). ⇒ **Không thể tuân cả hai.** Tôi chọn đặt bằng chứng ở
`agents/bountyrecon/tasks/T3/EVIDENCE/` (territory của tôi) và **đã báo Admin** trong báo cáo T3
(msg #45 §4.5) cùng `CANDIDATES.md` §4.

**Kiểm chứng hệ quả (`EVIDENCE/path_discrepancy.txt`):**

```text
$ git ls-files | grep -c '^security/.*EVIDENCE/'
  -> 0
$ git ls-files | grep 'EVIDENCE/' | sed 's#/EVIDENCE/.*#/EVIDENCE/#' | sort -u
  agents/bountyrecon/tasks/T3/EVIDENCE/
  agents/exploitdeep/T16/EVIDENCE/
  agents/exploitdeep/T4/EVIDENCE/
  agents/forensicsmal/T15/EVIDENCE/
  research/ebpf-microsegmentation/EVIDENCE/
  research/EVIDENCE/
  research/pqc-tls-migration/EVIDENCE/
```

⇒ **Có ĐÚNG 0 file dưới `security/**/EVIDENCE/` trong toàn repo.**
⇒ **Mọi chỉ thị trỏ vào `security/<program>/EVIDENCE/…` CHẮC CHẮN là đường dẫn chết.**
⇒ GAP-1 **không phải lỗi đánh máy** — nó là hệ quả tất yếu của quy tắc §5 không được ai thi hành được.

**ĐỀ NGHỊ ADMIN (chọn 1):**
- **(a)** Sửa §5 thành `agents/<slug>/tasks/<task_id>/EVIDENCE/` cho khớp thực tế đang dùng, **hoặc**
- **(b)** Nếu muốn bằng chứng tập trung theo chương trình, thì **bàn giao `security/**/EVIDENCE/**`
  cho agent sản xuất** (bỏ khỏi territory T4), **hoặc**
- **(c)** Ghi rõ trong `ASSIGNMENTS.md` rằng T4 chỉ sở hữu `FINDING.md`/`POC/`, còn `EVIDENCE/` là dùng chung.

Cho tới khi chốt, **tôi vẫn giữ nguyên cách hiện tại** (bằng chứng trong territory của tôi).

---

## GAP-3 — Trình kiểm link **ngây thơ** đẻ ra **127 báo động giả** trên chính territory này

Tôi đã tự mắc lỗi này ở `scan_links.py` **v1** và phải sửa **3 lần** mới đúng
(xem [`LINKSCAN.md`](LINKSCAN.md) §3). Đây là **cảnh báo cho bất kỳ ai đưa "kiểm link"
vào checklist review**:

| Cách kiểm | Kết quả trên territory này |
|---|---|
| Ngây thơ: mọi `](…)` + mọi `href=` | **127 "lỗi"** — gần hết là đường dẫn máy chủ gốc trong HTML đã capture |
| Phân loại AUTHORED vs CAPTURE | còn **3 "lỗi"** — nhưng vẫn bắt nhầm tên miền trần |
| Bỏ code fence + inline code + BARE_HOST | **3 lỗi thật** — đúng bằng số Admin báo |

⇒ Tỉ lệ **nhiễu / lỗi thật = 127 / 3 ≈ 42:1**. Một reviewer dùng công cụ ngây thơ sẽ **ngập
nhiễu và bỏ sót lỗi thật** — tệ hơn là không kiểm.

**ĐỀ NGHỊ:** nếu thêm bước kiểm link, phải quy định rõ **bỏ qua**: (a) file trong `EVIDENCE/`
cùng `.html`/`.txt` là bản ghi nguồn ngoài; (b) **code fence** ```…```; (c) **inline code** `` `…` ``;
(d) **tên miền trần** không scheme. Nếu không, đừng thêm bước này.

---

## GAP-4 — MẪU CHUNG: verify "nội dung" mà không verify "toàn vẹn artifact"

GAP-0 và GAP-1 là **cùng một mẫu lỗi ở hai tầng khác nhau:**

| Tầng | Đã verify | Chưa verify | Hậu quả thực tế |
|---|---|---|---|
| T14 (nội dung T3) | `SCOPE.md` đúng nguyên văn, hash khớp | **link trong file** | 3 link chết lọt qua |
| D-020 (chỉ thị Admin) | dòng 185, đúng 3 link, quyết định giữ | **đường dẫn file có tồn tại không** | chỉ thị trỏ vào file không có |

⇒ **ĐỀ NGHỊ bổ sung 3 phép kiểm CƠ HỌC, rẻ, vào checklist review (T6/T25/T14):**
1. **Mọi đường dẫn được trích trong báo cáo phải `test -f` được** (không chỉ đúng nội dung).
2. **Mọi link tương đối trong file thay đổi phải giải được** — phân loại AUTHORED vs CAPTURE (GAP-3).
3. **Mọi hash/số liệu công bố phải tái lập được từ nguồn** (T14 đã làm rất tốt ở tầng nội dung —
   Reviewer1 tự gọi lại GraphQL và tự băm, 3/3 khớp; chỉ thiếu tầng đường dẫn/link).

Đây là **mở rộng** việc T14 đã làm, không phải phủ nhận nó.

---

## GAP-5 — Task "placeholder" trên board trông giống uỷ quyền

Tôi tạo `T4-G1`/`T4-G2` ở T3 để handoff. Chúng hiện trên board là `open`,
`T4-G1` có `owner=ExploitDeep`. ExploitDeep **từ chối claim** và Admin xác nhận đúng (LOG #40).
Nhưng tiêu đề của tôi tuy có `[DE XUAT T4 - cho Admin duyet]` mà **cột `Status` vẫn là `open`**
⇒ một agent đọc lướt board có thể tưởng đã được phép.

**ĐỀ NGHỊ:** quy ước cho task placeholder: hoặc `owner=Admin`, hoặc `Status=blocked` kèm lý do
"chờ chỉ thị D-013", hoặc tiền tố bắt buộc `[PLACEHOLDER]`. Tôi sẵn sàng sửa 2 task của mình
nếu Admin chốt quy ước.

---

## Tổng hợp

| # | Khoảng trống | Mức | Cần ai xử lý |
|---|---|---|---|
| GAP-0 | T14 không kiểm link ⇒ 3 link chết lọt qua | Trung bình | Reviewer1/Admin (checklist) |
| **GAP-1** | D-020 trỏ `security/github/EVIDENCE/…` — **không tồn tại** | **Cao** | Admin (đính chính) |
| **GAP-2** | **Nguyên nhân gốc:** §3 territory ⟂ §5 vị trí bằng chứng; **0 file** dưới `security/**/EVIDENCE/` | **Cao** | Admin (sửa quy tắc) |
| GAP-3 | Kiểm link ngây thơ = 127 báo động giả | Trung bình | Người thêm checklist |
| GAP-4 | Mẫu chung: verify nội dung ≠ verify toàn vẹn artifact | Trung bình | Reviewer1/Auditor2 |
| GAP-5 | Task placeholder trông giống uỷ quyền | Thấp | Admin (quy ước) |

**Tất cả đều kèm bằng chứng thô. Chưa mục nào được tôi tự verify.**
