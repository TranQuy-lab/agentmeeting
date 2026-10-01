# RECON — GitLab Bug Bounty (trinh sát THỤ ĐỘNG)

**Chương trình:** GitLab — xem [`SCOPE.md`](SCOPE.md) (scope đã trích nguyên văn)
**Người thực hiện:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Ngày chạy:** `2026-10-01`, giờ máy UTC `2026-10-01T13:52:0xZ`
**Trạng thái:** ✅ **Đã verify — T14 PASS** (`reviews/CROSS.md` §2.8, mốc `03d304b`). Đây là *quan sát bề mặt*, KHÔNG phải kết luận lỗ hổng.
**Đặc biệt:** chương trình GitLab **tuyên bố thẳng** rằng báo cáo quét tự động và báo cáo thu thập
thông tin là **out of scope** ⇒ nội dung file này **KHÔNG** phải finding. Xem §3.

---

## 0. Phạm vi phương pháp & tuyên bố đạo đức

**CHỈ thụ động.** Cùng script và giới hạn như [`../github/RECON.md`](../github/RECON.md) §0.

Tổng cho GitLab: **75 request** (70 `dig` + header/robots/security.txt + 1 TLS handshake),
**10 tên miền**. 74 rc=0, 1 timeout DNS ghi rõ bên dưới.

Lệnh thô: `agents/bountyrecon/tasks/T3/EVIDENCE/recon_gitlab.txt` (976 dòng).

> ⛔ **TUÂN THỦ:** GitLab cấm "Automated scanning reports of any kind" và
> "**Never test DoS vulnerabilities on GitLab.com**", "**Never test against projects, groups,
> accounts, or instances you do not own**". T3 **không** quét, **không** gửi payload, **không**
> tạo tài khoản, **không** chạm dữ liệu người dùng.

**Trung thực về kết quả:** 1 truy vấn thất bại —
`dig gitlab.com TXT` → `;; communications error to 127.0.0.53#53: timed out` (rc=9).
⇒ **SPF gốc của `gitlab.com`: CHƯA XÁC MINH.** Không suy đoán.

---

## 1. Bản ghi DNS công khai

Nguồn thô: `recon_gitlab.txt`.

| Tên miền | Trong scope? | NS | A / AAAA | Ghi chú |
|---|---|---|---|---|
| `gitlab.com` | ✅ URL (critical) | `jermaine.ns.cloudflare.com`, `diva.ns.cloudflare.com` | A `172.65.251.78` · AAAA `2606:4700:90:0:f22e:fbec:5bed:a9b9` | GitLab dùng DNS của Cloudflare. Cả A và AAAA nằm trong dải Cloudflare. |
| `about.gitlab.com` | ✅ URL (medium) — **Admin loại khỏi T4** (§2b) | `shaz`/`julio.ns.cloudflare.com` | A `104.18.28.129`, `104.18.29.129` | Sau Cloudflare. TXT: `_globalsign-domain-verification=…`. |
| `docs.gitlab.com` | ✅ URL (medium) — **Admin loại khỏi T4** (§2b) | — | A `104.18.39.11`, `172.64.148.245` | TXT: `google-site-verification=YgHoFZLvJOGzjmqfSOAqWD8fU4GnVYXjWojp8Tgxvb4`. |
| `customers.gitlab.com` | ✅ URL (critical) | — | A `172.64.148.245`, `104.18.39.11` · AAAA `2a06:98c1:3105::ac40:94f5` | MX `10 mxa/mxb.mailgun.org`. TXT SPF `"v=spf1 include:mailgun.org ~all"`. |
| `registry.gitlab.com` | ✅ URL (critical) | — | A `35.227.35.254` (**GCP, KHÔNG qua Cloudflare**) | **Khác biệt hạ tầng:** đây là IP Google Cloud trực tiếp. |
| `design.gitlab.com` | ✅ URL (medium) | — | `CNAME gitlab-org.gitlab.io.` → A `35.185.44.232` (**Google**) | Trỏ vào hạ tầng GitLab Pages (`*.gitlab.io`). |
| `advisories.gitlab.com` | ✅ URL (medium) | — | `CNAME pages.gitlab.io.` → A `35.185.44.232` | Như trên. |
| `license.gitlab.com` | ✅ URL (critical) | **không có bản ghi NS/A/AAAA/MX/TXT/CAA** | — | **Trong scope nhưng KHÔNG phân giải.** Xem §3 ứng viên C3. |
| `gitlab.org` | ✅ WILDCARD (medium) | `hal`/`arya.ns.cloudflare.com` | A `104.21.92.3`, `172.67.183.112` | MX `mx1/mx2.emailsrvr.com`. |
| `gitlab.net` | ⛔ **NGOÀI scope** (apex đã nghỉ hưu `2020-10-05`) — nhưng `*.gitlab.net` **trong scope** (medium) | `hal`/`arya.ns.cloudflare.com` | **A/AAAA rỗng** | TXT `google-site-verification=…`. |

### 1.1 DMARC (nguyên văn)

```text
_dmarc.gitlab.com   "v=DMARC1; p=reject; pct=100; rua=mailto:dmarc_agg@vali.email;"
_dmarc.gitlab.org   "v=DMARC1; p=none; pct=100; rua=mailto:dmarc_agg@vali.email;"
_dmarc.gitlab.net   "v=DMARC1; p=none; pct=100; rua=mailto:dmarc_agg@vali.email;"
```

> ⛔ **CẢNH BÁO CHO EXPLOITDEEP — ĐỪNG MẤT THỜI GIAN:** `gitlab.org`/`gitlab.net` đặt
> `p=none` (không thực thi). **Nhưng GitLab đã liệt kê tường minh trong out-of-scope:**
> *"Social engineering, phishing, or other fraud including but not limited to: internationalized
> domain name (IDN) homograph attacks, Right-to-left (RTL) Ambiguity, RTL Override (RTLO),
> **SPF and DKIM issues**, most HTML content injection, Tabnabbing"*.
> ⇒ **SPF/DMARC là OUT OF SCOPE.** Tôi ghi lại để **chặn** hướng đi sai, không phải để đề xuất.

### 1.2 CAA (nguyên văn, rút gọn)

```text
gitlab.com  issue: amazontrust.com, globalsign.com, amazon.com, pki.goog (cansignhttpexchanges=yes); issuewild: co(mo)…
gitlab.org  issue: letsencrypt.org, globalsign.com; issuewild: digicert.com, pki.goog
gitlab.net  issue: digicert.com, comodoca.com, pki.goog; issuewild: letsencrypt.org
customers.gitlab.com / about.gitlab.com / docs.gitlab.com  → KHÔNG có CAA ở subdomain
```
⇒ `customers.gitlab.com` là tài sản **critical** nhưng **không đặt CAA**; CAA kế thừa từ
`gitlab.com` (parent). Không thấy bất thường. **Chưa xác minh** hành vi kế thừa CAA.

---

## 2. Bề mặt web công khai

### 2.1 `https://gitlab.com/` → **301** sang `https://about.gitlab.com/`

```text
HTTP/2 301
location: https://about.gitlab.com/
ratelimit-limit: 500
ratelimit-name: throttle_unauthenticated_web
ratelimit-observed: 1
ratelimit-remaining: 499
ratelimit-reset: 1790862780
gitlab-lb: haproxy-main-51-lb-gprd
gitlab-sv: web-gke-us-east1-d
x-gitlab-meta: {"correlation_id":"a43bf264fa610959-HKG","version":"1"}
x-request-id: a43bf264fa610959-HKG
x-runtime: 0.041644
server: cloudflare
cf-ray: a43bf264fa610959-HKG
strict-transport-security: max-age=31536000
x-frame-options: SAMEORIGIN
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
referrer-policy: strict-origin-when-cross-origin
permissions-policy: interest-cohort=()
content-security-policy: default-src 'self'; object-src 'none'; script-src 'strict-dynamic'
    'self' 'unsafe-inline' 'unsafe-eval' … 'nonce-oN5aCXzp/LF/FCv8I+Scig==';
    report-uri https://new-sentry.gitlab.net/api/4/security/?sentry_key=…
```

> ✅ **PHÁT HIỆN CÓ GIÁ TRỊ VẬN HÀNH CAO NHẤT CỦA T3 — gửi ngay cho ExploitDeep:**
> `ratelimit-limit: 500` + `ratelimit-name: throttle_unauthenticated_web` +
> `ratelimit-remaining: 499` ⇒ **GitLab chặn 500 request chưa xác thực mỗi cửa sổ.**
> Đây là **bằng chứng thô** cho giới hạn phải tuân thủ. Vượt ngưỡng ⇒ dễ bị coi là
> *"Spam-like or other high volume activity"* ⇒ **mất quyền + khoá tài khoản**
> (trích SCOPE.md §3). **Đây KHÔNG phải lỗ hổng** — "Lack of, or insufficient, rate limiting"
> là out-of-scope, và việc **có** rate limit là điều tốt.
>
> ⚠️ **Lưu ý về `object-src 'none'` xuất hiện trong CSP nhưng tôi trích nguyên văn có thể
> thiếu một phần giữa chuỗi do độ dài.** Bản đầy đủ ở `recon_gitlab.txt`. **Chưa xác minh**
> toàn bộ CSP theo từng directive.

### 2.2 `robots.txt`

```text
# See http://www.robotstxt.org/robotstxt.html for documentation on how to use the robots.txt file
# To ban all spiders from the entire site uncomment the next two lines:
# User-Agent: *
# Disallow: /

# Add a 1 second delay between successive requests to the same server, limits resources used by crawler
# Crawl-delay: 1
...
# Based on details in https://gitlab.com/gitlab-org/gitlab/blob/master/config/routes.rb,
```
⇒ robots.txt của GitLab chủ yếu là **hướng dẫn cho crawler**, phần lớn bị chú thích.
Không tiết lộ bề mặt nhạy cảm theo cách dùng được. **Không** dùng để dò đường dẫn.

### 2.3 `/.well-known/security.txt` — xác nhận kênh chính thức (có chữ ký PGP)

```text
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

# Preferred disclosure is via HackerOne
Contact: https://hackerone.com/gitlab/

# Additional disclosure processes are available in our handbook:
Contact: https://about.gitlab.com/security/disclosure/

Policy: https://hackerone.com/gitlab/
```
⇒ **Bằng chứng quan trọng nhất buổi trinh sát:** `security.txt` **được ký PGP** — mức đảm bảo
cao hơn GitHub/Cloudflare (chỉ là text thuần). Xác nhận HackerOne là kênh chính thức.
Gốc `/security.txt` trả về app-shell HTML (không phải văn bản `security.txt`).

### 2.4 Chứng chỉ TLS (1 handshake, không quét)

```text
subject=CN = gitlab.com
issuer=C = GB, O = Sectigo Limited, CN = Sectigo Public Server Authentication CA DV R36
notBefore=Apr 26 00:00:00 2026 GMT
notAfter=Nov 10 23:59:59 2026 GMT
X509v3 Subject Alternative Name:
    DNS:gitlab.com, DNS:auth.gitlab.com, DNS:customers.gitlab.com,
    DNS:email.customers.gitlab.com, DNS:gprd.gitlab.com, DNS:www.gitlab.com
```

> 🔎 **Quan sát (CHƯA XÁC MINH):** chứng chỉ này **gộp 6 tên** — gồm cả `auth.gitlab.com`
> và `customers.gitlab.com` (tài sản **critical** trong scope). Chứng chỉ **DV** (không OV/EV),
> do Sectigo cấp. **Chưa xác minh** đây có phải chứng chỉ phục vụ mọi vùng hay không.
> **Không kết luận.**

---

## 3. Ứng viên chuyển ExploitDeep (T4)

| # | Ứng viên | Bằng chứng | Độ tin cậy | Cảnh báo |
|---|---|---|---|---|
| C1 | **`registry.gitlab.com` không qua Cloudflare** — A `35.227.35.254` (GCP trực tiếp) | §1 | **THẤP** | Khác biệt hạ tầng so với `gitlab.com` (sau Cloudflare). Đây là **quan sát kiến trúc**, chưa phải lỗi. Có thể đáng kiểm vì là tài sản **critical** và ít lớp phòng vệ hơn. |
| C2 | `design.gitlab.com` + `advisories.gitlab.com` → CNAME vào hạ tầng GitLab Pages | §1 | **THẤP** | ⚠️ **KHÔNG phải subdomain takeover:** cả hai target (`gitlab-org.gitlab.io`, `pages.gitlab.io`) **đều phân giải** ra `35.185.44.232` ⇒ đã được sở hữu. Tôi đã kiểm bằng DNS thụ động. **Không** thử chiếm. |
| C3 | **`license.gitlab.com` trong scope (critical) nhưng KHÔNG phân giải** | §1 | **TRUNG BÌNH–THẤP** | **Không có CNAME treo** ⇒ không phải takeover. Có thể là IP-allowlist nội bộ. ⚠️ **TUYỆT ĐỐI không tự đoán** — cần Admin/GitLab làm rõ trước khi chạm. |
| C4 | `customers.gitlab.com` SPF `~all` | §1 | **BỊ LOẠI** | ⛔ GitLab liệt kê tường minh **"SPF and DKIM issues"** là out-of-scope. **Đừng theo.** |
| C5 | `gitlab.org`/`gitlab.net` DMARC `p=none` | §1.1 | **BỊ LOẠI** | ⛔ Cùng lý do C4. **Đừng theo.** |
| C6 | `gitlab-sv: web-gke-us-east1-d`, `gitlab-lb: haproxy-main-51-lb-gprd` lộ hạ tầng | §2.1 | **BỊ LOẠI** | ⛔ GitLab: *"Metadata disclosure, enumeration, and information gathering issues are out of scope unless the researcher demonstrates a privacy breach"*. **Đừng theo.** |

**Đánh giá thẳng thắn:** sau khi loại các mục bị chính sách GitLab loại trừ tường minh (C4–C6),
chỉ còn **C1** và **C3** là đáng chuyển tiếp — và cả hai đều ở mức tin cậy **thấp**,
**chưa xác minh**, **không phải lỗ hổng**.

---

## 4. Kết quả âm tính (đã kiểm, không thấy gì)

| Hạng mục | Kết quả |
|---|---|
| Port scan / service scan | **KHÔNG thực hiện** (`nmap` MISSING) |
| Subdomain enumeration | **KHÔNG thực hiện** (`subfinder`/`amass` MISSING) |
| **Subdomain takeover** | **Không thấy.** Các CNAME treo tiềm năng (`gitlab-org.gitlab.io`, `pages.gitlab.io`) **đều phân giải** ⇒ đã được sở hữu. |
| `*.gitlab.cn` (out of scope) | **KHÔNG chạm** — thuộc JiHu (Trung Quốc), tường minh out-of-scope |
| `*.runway.gitlab.net`, `*.gitlab-private.org` | **KHÔNG chạm** — out-of-scope |
| Zone transfer | **KHÔNG thử** (hoạt động chủ động) |
| `security.txt` thiếu | **Không** — có, và **được ký PGP** |

---

## 5. Hạn chế & điều CHƯA xác minh

1. `dig gitlab.com TXT` **timeout** ⇒ SPF gốc **chưa xác minh**.
2. **4 tài sản đã được Admin loại khỏi T4** (`*.gitlab.net`, `*.gitlap.com`, `about.gitlab.com`,
   `docs.gitlab.com`) — **0 xung đột hiệu lực**: vế OUT là bản ghi **đã nghỉ hưu**
   (`archived_at` 2022-07-21). Tôi đã trinh sát `about.gitlab.com`, `docs.gitlab.com` và `gitlab.net`
   ở mức **thụ động thuần** (chỉ đọc DNS công khai) **trước khi** biết điều đó.
   ⛔ **Phán quyết đã xong (D-021): CẤM chạm 4 tài sản này trong T4.** Xem [`SCOPE.md`](SCOPE.md) §2b.
3. Chỉ kiểm **10 tên miền** trong khi scope có **24 tài sản** (gồm cả source code).
4. `license.gitlab.com` không phân giải — **chưa xác minh** lý do.
5. Toàn bộ §2 là **quan sát thô**; chương trình GitLab **tuyên bố** nhóm này **out of scope**,
   nên **không** có mục nào ở đây là finding.
