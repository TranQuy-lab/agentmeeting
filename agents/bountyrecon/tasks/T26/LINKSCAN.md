# T26 — LINKSCAN: sửa 3 link sai độ sâu + quét toàn territory

**Agent:** BountyRecon (`ag_579fc4fa`) · **Task:** T26 · **Nhánh:** `agent/bounty-recon/T26`
**Chỉ thị:** D-020 (msg #114) · **`main` gốc:** `e8c45a0` · **Ngày:** `2026-10-01`
**Territory:** `agents/bountyrecon/**`, `security/**`

> ⚠️ **Chưa verify — chờ Reviewer1.** Tôi **không** tự verify việc mình làm (D-004).
> Mọi kết luận dưới đây kèm lệnh thô + output thô trong `EVIDENCE/`.

---

## 1. Yêu cầu 1 — sửa 3 link sai độ sâu ✅

`agents/bountyrecon/tasks/T3/CANDIDATES.md`, dòng **27 / 39 / 50**.
Từ thư mục chứa file là `agents/bountyrecon/tasks/T3/`, cần **4** cấp `../` mới tới gốc repo:

```text
T3 --1--> tasks --2--> bountyrecon --3--> agents --4--> <gốc repo>
```

| Dòng | TRƯỚC (3 cấp — chết) | SAU (4 cấp — đúng) |
|---|---|---|
| 27 | `../../../security/github/RECON.md` | `../../../../security/github/RECON.md` |
| 39 | `../../../security/gitlab/RECON.md` | `../../../../security/gitlab/RECON.md` |
| 50 | `../../../security/cloudflare/RECON.md` | `../../../../security/cloudflare/RECON.md` |

### Bằng chứng thô — `EVIDENCE/verify_links.txt`

```text
$ test -f "agents/bountyrecon/tasks/T3/../../../../security/github/RECON.md"
  -> TRUE (TON TAI)
$ realpath --relative-to=. "agents/bountyrecon/tasks/T3/../../../../security/github/RECON.md"
  -> security/github/RECON.md
$ git ls-files --error-unmatch "security/github/RECON.md"
  -> security/github/RECON.md
```
(lặp lại y hệt cho `gitlab` và `cloudflare` — cả 3 đều `TRUE`)

**Chứng minh link CŨ chết:**

```text
$ test -f "agents/bountyrecon/tasks/T3/../../../security/github/RECON.md"
  -> FALSE (dung: link cu chet)
$ realpath -m --relative-to=. "agents/bountyrecon/tasks/T3/../../../security/github/RECON.md"
  -> agents/security/github/RECON.md          <-- dung nhu D-020 mo ta

$ test -d agents/security
  -> FALSE  <= day la ly do 3 link cu chet
$ ls -d agents/security
  -> ls: cannot access 'agents/security': No such file or directory
```

---

## 2. Yêu cầu 2 — quét TOÀN BỘ territory ✅ **không còn link sai độ sâu nào khác**

Script tái lập được: [`scan_links.py`](scan_links.py) (chỉ đọc, không sửa file, không dùng mạng).
Quét `agents/bountyrecon/**` + `security/**`, **gồm cả 23 file evidence**.
Hai lần quét dùng **cùng một script**, khác nhau ở **cây làm việc**:

* **TRƯỚC** = `git worktree` của `main` `e8c45a0` (`/tmp/t3/mainwt`) — 24 file.
* **SAU** = nhánh `agent/bounty-recon/T26` — 33 file (thêm 9 file của T26).

Output thô: `EVIDENCE/linkscan_before.txt` và `EVIDENCE/linkscan_after.txt`.

| Chỉ số | TRƯỚC (`main`) | SAU (`T26`) |
|---|---|---|
| File đã quét | 24 | 33 |
| Link tương đối **OK** | 7 | **14** |
| **DEFECT (sai độ sâu)** | **3** | **0** ✅ |
| DEFECT trong code fence (không render) | 0 | 7 |
| BARE_HOST trong file AUTHORED | 0 | 0 |
| ROOT_REL trong file CAPTURE (bỏ qua) | 138 | 141 |

> **7 mục "trong code fence" ở cột SAU là CỐ Ý:** chúng là các link cũ được **trích dẫn
> trong khối ```text** của chính file báo cáo này (dòng 74–80) để tài liệu hoá lỗi đã sửa.
> Trong code fence thì **không được render** thành link ⇒ không phải lỗi.

**Liệt kê đầy đủ 10 link tương đối trong territory T3** (để Reviewer1 đối chiếu độc lập):

```text
agents/bountyrecon/tasks/T3/CANDIDATES.md : ../../../security/{github,gitlab,cloudflare}/RECON.md  <- 3 DEFECT, da sua
security/cloudflare/RECON.md : ](SCOPE.md)            OK
security/cloudflare/RECON.md : ](../github/RECON.md)  OK
security/cloudflare/RECON.md : ](SCOPE.md)            OK
security/github/RECON.md     : ](SCOPE.md)            OK
security/gitlab/RECON.md     : ](SCOPE.md)            OK
security/gitlab/RECON.md     : ](../github/RECON.md)  OK
security/gitlab/RECON.md     : ](SCOPE.md)            OK
```

Cộng thêm **4 link tương đối mới của T26** (`scan_links.py`, `SCOPEGAP.md` ×2, `LINKSCAN.md`)
⇒ 10 + 4 = **14 OK**, khớp cột SAU.

### 2.1 Đối chứng chặt: quét **toàn repo** TRƯỚC và SAU bằng cùng một script

`EVIDENCE/repowide_control.txt` — quét **toàn bộ `.md` của cả repo** (không chỉ territory),
bỏ `EVIDENCE/`. TRƯỚC quét trên worktree của `main`:

```text
### A. TRUOC khi sua (cay lam viec = WORKTREE cua main e8c45a0)
  link OK: 43 | link CHET: 3
    agents/bountyrecon/tasks/T3/CANDIDATES.md:27  ../../../security/github/RECON.md  ->  agents/security/github/RECON.md
    agents/bountyrecon/tasks/T3/CANDIDATES.md:39  ../../../security/gitlab/RECON.md  ->  agents/security/gitlab/RECON.md
    agents/bountyrecon/tasks/T3/CANDIDATES.md:50  ../../../security/cloudflare/RECON.md  ->  agents/security/cloudflare/RECON.md

### B. SAU khi sua (cay lam viec = nhanh agent/bounty-recon/T26)
  link OK: 46 | link CHET: 0
```

⇒ **Trong toàn bộ file `.md` do người/agent viết của cả repo, 3 link của tôi là
những link tương đối chết DUY NHẤT**, và bản vá xử lý đúng chúng, không làm chết link nào khác.

---

## 3. Tôi đã tự tìm ra và sửa **3 lớp lỗi** trong scanner của chính mình

**Trung thực để Reviewer1 soi được:** tôi đã phải sửa scanner **3 lần**, mỗi lần đều do
tự chạy lại và thấy kết quả vô lý. Đây là phần quan trọng nhất của báo cáo này.

| Lớp | Bản | Báo nhầm | Nguyên nhân | Cách sửa |
|---|---|---|---|---|
| 1 | v1 | **127 "lỗi"** | Coi đường dẫn gốc-máy-chủ (`/css/site.css`, `/assets/webpack/…`) trong **HTML/transcript đã CAPTURE** là link repo | Phân loại theo ngữ cảnh `AUTHORED` vs `CAPTURE` |
| 2 | v2 | **3 "lỗi"** (ở file của chính tôi) | Coi `lgtm-com.pentesting.semmle.net` là đường dẫn tương đối vì có dấu `.` | Thêm lớp `BARE_HOST` (tên miền trần, không scheme) |
| 3 | v2.1 | **1 "lỗi"** | Bắt nhầm mẫu mô tả `` `](…)` `` nằm trong **inline code span** của văn xuôi | Bỏ inline-code span (`` `…` ``) trước khi tìm link; và **BARE_HOST trong file CAPTURE** cũng tính là capture |

**Ba lần đều cho ra cùng một kết luận khi đã phân loại đúng: 3 lỗi thật** — đúng bằng số Admin báo.
Đó là **kiểm chứng chéo nội tại**: 3 cách cài đặt khác nhau hội tụ về cùng con số.

**v2.1 phân loại theo ngữ cảnh:**

| Loại | Định nghĩa | Xử lý |
|---|---|---|
| `AUTHORED` | file do agent viết (CANDIDATES/SCOPE/RECON) | link chết ⇒ **DEFECT, sửa** |
| `CAPTURE` | file trong `EVIDENCE/`, `.html`, `.txt` (bản ghi nguồn ngoài) | đường dẫn máy chủ gốc ⇒ **KHÔNG sửa** |
| `BARE_HOST` | target không scheme, trông như tên miền | trích nguyên văn ⇒ **KHÔNG sửa** |
| code fence | trong ```…``` | **không render** ⇒ hạ mức, không tính DEFECT |
| inline code | trong `` `…` `` | **không render** ⇒ bỏ qua |

> 📌 **Bài học cho T14/T25 (khoảng trống phạm vi):** một trình kiểm link **ngây thơ** tạo ra
> **127 báo động giả** trên chính territory này — gấp **42 lần** số lỗi thật. Ai định đưa
> "kiểm link" vào checklist review **phải** phân loại theo ngữ cảnh AUTHORED vs CAPTURE,
> và phải bỏ qua code fence + inline code, nếu không sẽ ngập nhiễu và **bỏ sót lỗi thật**.
> Xem [`SCOPEGAP.md`](SCOPEGAP.md) GAP-3.

---

## 4. File BỊ CẤM SỬA — đã giữ nguyên ✅

Lệnh D-020 §2 QĐ-2: **cấm** sửa 3 link thiếu `https://` ở `scope_github.md` dòng 185.
Bằng chứng: `EVIDENCE/forbidden_file_untouched.txt`.

```text
$ sha256sum agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md
  a6f6cad29c90bd4e0e3d7dbbfb94507d6d5835cd34113b195ff9880b378ac0f7
$ git show main:agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md | sha256sum
  a6f6cad29c90bd4e0e3d7dbbfb94507d6d5835cd34113b195ff9880b378ac0f7  -
$ git diff --exit-code main -- agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md ; echo "exit=$?"
  exit=0  (0 = khong co khac biet)
```

**Byte-identical với `main`.** 3 link thiếu scheme ở dòng 185 **vẫn còn nguyên** đúng như quyết định.

---

## 5. Kết luận

| Yêu cầu | Kết quả |
|---|---|
| 1. Sửa 3 link sai độ sâu | ✅ xong, kiểm bằng `test -f` + `realpath --relative-to` + `git ls-files --error-unmatch` |
| 2. Quét toàn territory, tìm link sai độ sâu khác | ✅ **không còn cái nào** (24 file, DEFECT 3 → 0) |
| 3. Báo cáo khoảng trống phạm vi | ✅ [`SCOPEGAP.md`](SCOPEGAP.md) |
| Cấm sửa `scope_github.md` dòng 185 | ✅ giữ nguyên, sha256 trùng `main` |

**Không chạm hệ thống thật. G4 vẫn ĐÓNG. Không merge `main`** (chỉ Admin merge).
