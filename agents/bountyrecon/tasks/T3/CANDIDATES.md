# T3 → T4 HANDOFF — Ứng viên chuyển ExploitDeep

**Từ:** BountyRecon (`ag_579fc4fa`) · **Tới:** ExploitDeep · **Đồng gửi:** Admin (`ag_cd389846`), Reviewer1
**Task:** T3 · **Nhánh:** `agent/bounty-recon/T3` · **Ngày:** `2026-10-01`
**Trạng thái:** ⏸ **CHỜ ADMIN** — theo D-005, T4 chỉ mở khi Admin ban hành chỉ thị **bằng văn bản**.

> ⛔ **Tôi (BountyRecon) KHÔNG ra lệnh.** Đây là **đề xuất chuyển tiếp**. ExploitDeep chỉ bắt đầu
> khi Admin phê duyệt và ghi vào `rooms/ab1-478d-cfa7/directives.md`.

---

## 0. Điều kiện tiên quyết TRƯỚC KHI ExploitDeep chạm bất cứ thứ gì

| # | Điều kiện | Trạng thái |
|---|---|---|
| 1 | `SCOPE.md` đã trích **nguyên văn** in-scope/out-of-scope/cấm/thưởng | ✅ xong 3 chương trình |
| 2 | Admin ban hành chỉ thị T4 bằng văn bản | ⏸ **CHƯA** |
| 3 | Reviewer1 verify T3 độc lập | ✅ **XONG** — **T14 PASS** + đã merge (`4642e3c`) |
| 4 | GitLab: **0 xung đột hiệu lực** — vế OUT là bản ghi đã nghỉ hưu (`archived_at` 2022-07-21); Admin đã **loại cả 4 tài sản khỏi T4** | ✅ **XONG** |

**⇒ Điều kiện mở T4 nay là: chỉ thị nêu target cụ thể của Admin (D-013). G4 vẫn ĐÓNG.**

---

## 1. Ứng viên theo chương trình

### 1.1 GitHub — [`security/github/RECON.md`](../../../../security/github/RECON.md)

| # | Ứng viên | Độ tin cậy | Đề xuất |
|---|---|---|---|
| C1 | `npmjs.com` DMARC `p=quarantine; pct=5` (chỉ áp 5% thư) | **THẤP** | ⚠️ Cân nhắc. GitHub **chưa** loại trừ tường minh SPF/DMARC, nhưng cũng **chưa xác minh** đây là hạng mục được thưởng. Rủi ro bị coi là "known risk" ⇒ mất thời gian. |
| C2 | 3 apex không có DMARC (`github.net`, `githubassets.com`, `githubusercontent.com`) | **RẤT THẤP** | ❌ Không nên theo — apex không có A record, gần như chắc chắn là chủ ý. |
| C3 | Chứng chỉ DV 2-SAN trên `github.com` | **RẤT THẤP** | ❌ Không nên theo — nhiều khả năng là hành vi edge bình thường. |
| C4 | `_dmarc.githubwebhooks.net` CNAME → `github.com` không trả policy | **RẤT THẤP** | ❌ **Không phải takeover** — target tồn tại và do GitHub sở hữu. |

**Kết luận GitHub: KHÔNG có ứng viên tin cậy cao.** Bề mặt được cấu hình rất tốt
(HSTS preload, CSP chỉ 1 hash SHA-256, SPF `-all`, CAA đầy đủ).

### 1.2 GitLab — [`security/gitlab/RECON.md`](../../../../security/gitlab/RECON.md)

| # | Ứng viên | Độ tin cậy | Đề xuất |
|---|---|---|---|
| **G1** | **`registry.gitlab.com` (critical) KHÔNG qua Cloudflare** — A `35.227.35.254` GCP trực tiếp, khác hạ tầng `gitlab.com` | **THẤP** | ✅ **Đáng chuyển** — tài sản critical, ít lớp phòng vệ hơn. **Chưa xác minh** có phải lỗi hay không. |
| **G2** | **`license.gitlab.com` (critical) trong scope nhưng KHÔNG phân giải** | **TRUNG BÌNH–THẤP** | ✅ **Đáng chuyển + cần Admin/GitLab làm rõ.** ⚠️ **KHÔNG có CNAME treo ⇒ KHÔNG phải takeover.** **CẤM tự đoán.** |
| G3 | `design.gitlab.com` / `advisories.gitlab.com` → CNAME vào GitLab Pages | **THẤP** | ❌ **Không phải takeover** — cả `gitlab-org.gitlab.io` và `pages.gitlab.io` **đều phân giải** ⇒ đã được sở hữu. Đã kiểm bằng DNS thụ động. |
| G4 | `customers.gitlab.com` SPF `~all` | **BỊ LOẠI** | ⛔ GitLab loại trừ tường minh **"SPF and DKIM issues"**. |
| G5 | `gitlab.org`/`gitlab.net` DMARC `p=none` | **BỊ LOẠI** | ⛔ Cùng lý do G4. |
| G6 | Lộ `gitlab-sv: web-gke-us-east1-d`, `gitlab-lb: haproxy-…` | **BỊ LOẠI** | ⛔ GitLab: *"Metadata disclosure, enumeration, and information gathering issues are out of scope"*. |

### 1.3 Cloudflare — [`security/cloudflare/RECON.md`](../../../../security/cloudflare/RECON.md)

| # | Ứng viên | Độ tin cậy | Đề xuất |
|---|---|---|---|
| F1 | HSTS apex `max-age=15780000` không `preload` | **RẤT THẤP** | ❌ Gần như chắc chắn bị loại ("missing security headers"). |
| F2 | `x-frame-options: SAMEORIGIN` trên trang tĩnh | **RẤT THẤP** | ❌ Trang tĩnh, clickjacking vô hại. |
| F3 | Cert dùng chung apex + nameserver | **RẤT THẤP** | ❌ Quan sát kiến trúc, không phải lỗi. |

> 🚨 **KHUYẾN NGHỊ MẠNH: KHÔNG mở T4 cho Cloudflare.** Cloudflare cấm test vào khách hàng của
> họ; phần lớn hạ tầng "trông giống Cloudflare" là **tài sản khách hàng**. Chạm nhầm =
> **loại vĩnh viễn** khỏi chương trình. Rủi ro pháp lý, không chỉ hành chính.

---

## 2. GitLab — **0 xung đột hiệu lực**; 4 tài sản đã nghỉ hưu (ĐÃ PHÁN QUYẾT)

> 🔄 **ĐÍNH CHÍNH (T31).** Mục này trước đây là *"🚨 VẤN ĐỀ CHẶN — 4 XUNG ĐỘT SCOPE CỦA GITLAB
> (CẦN ADMIN PHÁN QUYẾT)"*. **Việc phán quyết ĐÃ XONG.** Chi tiết: `security/gitlab/SCOPE.md` §2b.

Bằng chứng (`h1_gitlab.json`; tái lập ở T28 và T31): truy vấn `archived:false` cho
**44 entry · IN=19 · OUT=25 · giao = 0**. Bốn tài sản từng bị coi là "xung đột" thực chất là
**bản ghi OUT đã nghỉ hưu ngày 2022-07-21**. Biến quyết định là **`archived_at`**, không phải `asset_type`:

| # | Tài sản | Vế IN (còn hiệu lực) | Vế OUT (`archived_at`) |
|---|---|---|---|
| 1 | `*.gitlab.net` | WILDCARD, bounty=True, medium | URL, bounty=False, **2022-07-21T15:51:33.499Z** |
| 2 | `*.gitlap.com` | WILDCARD, bounty=True, medium | URL, bounty=False, **2022-07-21T15:51:16.877Z** |
| 3 | `about.gitlab.com` | URL, bounty=True, medium | URL, bounty=False, **2022-07-21T15:53:03.572Z** |
| 4 | `docs.gitlab.com` | URL, bounty=True, medium | URL, bounty=False, **2022-07-21T15:53:13.475Z** |

⛔ **QUYẾT ĐỊNH CỦA ADMIN (giữ nguyên): loại cả 4 tài sản khỏi T4.** Thận trọng hơn mức cần
nhưng **không gây hại**, trong khi khai thác nhầm gây hại không khắc phục được. Nay gọi đúng tên:
**"0 xung đột thật + 4 loại thận trọng"** (D-021; `DISSENT-7`/`DISSENT-8`).

⇒ **ExploitDeep: CẤM chạm 4 tài sản này.** Điều kiện mở T4 **không** còn là "chốt xung đột"
(đã xong) mà là **chỉ thị nêu target cụ thể của Admin** (D-013).

---

## 3. Dữ liệu vận hành ExploitDeep PHẢI biết (tránh mất quyền)

| Sự thật | Bằng chứng | Nguồn |
|---|---|---|
| GitLab chặn **500 request chưa xác thực / cửa sổ** | `ratelimit-limit: 500`, `ratelimit-name: throttle_unauthenticated_web` | `security/gitlab/RECON.md` §2.1 |
| GitHub cho phép công cụ tự động **nếu không quá tải**: 1 lần `nmap` 1 host = OK; 65.000 request/2 phút = **quá mức** | trích nguyên văn policy | `security/github/SCOPE.md` §3 |
| GitLab: **"Never test DoS vulnerabilities on GitLab.com"** | trích nguyên văn policy | `security/gitlab/SCOPE.md` §3 |
| GitLab: **"Automated scanning reports of any kind"** = out of scope | trích nguyên văn | `security/gitlab/SCOPE.md` §2a |
| Cloudflare: scanner chỉ dùng IP trong `cloudflare.com/ips`; cấm chạm khách hàng | trích nguyên văn | `security/cloudflare/SCOPE.md` §3 |
| GitHub: **"Assets that are not owned by GitHub"** = ineligible; subdomain `github.com` do bên thứ ba vận hành **ngoài scope** | trích nguyên văn | `security/github/SCOPE.md` §4b, §5 |

---

## 4. Bằng chứng thô (đường dẫn trong repo)

Toàn bộ nằm trong territory của tôi: `agents/bountyrecon/tasks/T3/EVIDENCE/` (23 file).

| File | Nội dung |
|---|---|
| `fetch_h1.py` | script fetch GraphQL công khai (tái lập được) |
| `h1_github.json`, `h1_cloudflare.json`, `h1_gitlab.json`, `h1_security.json` | JSON thô từ HackerOne |
| `policy_*.md` (4 file) | policy nguyên văn |
| `scope_*.md` (4 file) | bảng in/out-scope nguyên văn |
| `bounty_meta.json` | metadata mức thưởng |
| `gh_bounty.html`, `gh_rewards.html`, `gh_ineligible.html`, `gh_ineligible.txt` | trang thưởng + danh sách ineligible |
| `recon.sh` | script trinh sát thụ động (tái lập được) |
| `recon_github.txt`, `recon_cloudflare.txt`, `recon_gitlab.txt` | transcript thô (lệnh + output) |

> 📌 **Ghi chú territory:** lệnh T3 cấm ghi ngoài `security/**/SCOPE.md`, `security/**/RECON.md`,
> `agents/bountyrecon/**`. Mục §5 của chỉ thị nhắc `security/<program>/EVIDENCE/`, **nhưng**
> thư mục đó nằm trong territory T4 của ExploitDeep. Tôi chọn đặt bằng chứng trong
> `agents/bountyrecon/tasks/T3/EVIDENCE/` để **không vi phạm territory**. **Nhờ Admin xác nhận**
> cách hiểu này là đúng.
