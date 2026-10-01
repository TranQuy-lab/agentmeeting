# RECON — GitHub Security Bug Bounty (trinh sát THỤ ĐỘNG)

**Chương trình:** GitHub — xem [`SCOPE.md`](SCOPE.md) (scope đã trích nguyên văn)
**Người thực hiện:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Ngày chạy:** `2026-10-01`, giờ máy UTC `2026-10-01T13:49:44Z` → `13:50:57Z`
**Trạng thái:** ⚠️ **Chưa verify — chờ Reviewer1.** Đây là *quan sát bề mặt*, KHÔNG phải kết luận lỗ hổng.

---

## 0. Phạm vi phương pháp & tuyên bố đạo đức

**CHỈ thụ động / không xâm nhập.** Đúng danh sách được phép trong lệnh T3:

| Loại | Cụ thể | Số lượng request |
|---|---|---|
| Bản ghi DNS công khai | `dig` NS/A/AAAA/MX/TXT/CAA + `_dmarc` | 56 truy vấn cho 8 tên miền |
| Tài liệu công khai | `robots.txt` | 1 |
| Header HTTP công khai | `curl -I` (1 request/host) | 1 |
| Tài liệu công khai | `/.well-known/security.txt` | 2 |
| TLS công khai | 1 handshake đọc chứng chỉ | 1 |
| **TỔNG** | | **61 request, 8 tên miền, ~1 phút** |

**KHÔNG** thực hiện: quét cổng, fuzz đường dẫn, brute-force, gửi payload, khai thác, thu thập
dữ liệu người dùng, quét diện rộng. **Không có request nào mang payload.**

Lệnh thô đầy đủ (kèm output): `agents/bountyrecon/tasks/T3/EVIDENCE/recon_github.txt`
(953 dòng, 60/61 lệnh rc=0, 1 lệnh timeout DNS được ghi rõ bên dưới).
Script tái lập: `agents/bountyrecon/tasks/T3/EVIDENCE/recon.sh`.

**Trung thực về kết quả:** 1 truy vấn thất bại —
`dig github.com TXT` → `;; communications error to 127.0.0.53#53: timed out` (rc=9).
⇒ **TXT của `github.com` (bao gồm SPF gốc): CHƯA XÁC MINH.** Không suy đoán.

---

## 1. Bản ghi DNS công khai

Nguồn thô: `recon_github.txt` dòng 10–430.

| Tên miền | NS | A / AAAA | MX | Ghi chú |
|---|---|---|---|---|
| `github.com` | 8 NS: `ns-421.awsdns-52.com`, `dns1-4.p08.nsone.net`, `ns-1283.awsdns-32.org`, `ns-1707.awsdns-21.co.uk`, `ns-520.awsdns-01.net` | A `20.205.243.166` · **AAAA rỗng** | `0 github-com.mail.protection.outlook.com.` | DNS kép AWS Route 53 + NS1. Không có IPv6 ở apex. |
| `githubassets.com` | AWS Route 53 + NS1 (p02) | **A/AAAA rỗng ở apex** | rỗng | TXT: `"v=spf1 a -all"` — SPF rất chặt (`-all`). |
| `githubusercontent.com` | AWS Route 53 + NS1 (p01) | **A/AAAA rỗng ở apex** | rỗng | — |
| `githubapp.com` | — | A `140.82.112.29`, `.113.29`, `.113.30`, `.114.30` (… rút gọn trong bảng) | — | Nằm trong dải `140.82.112.0/20`. TXT: `"v=spf1 a include:_spf.google.com ~all"`. |
| `githubwebhooks.net` | — | A `140.82.113.18` | — | 1 host duy nhất. |
| `github.net` | AWS Route 53 + NS1 (p05) | **A/AAAA rỗng ở apex** | rỗng | Đúng như policy mô tả: dịch vụ nội bộ, không lộ ra ngoài. |
| `npmjs.com` | — | A `104.17.134.117`, `104.17.135.117` · AAAA `2606:4700::6811:8675`, `…8775` | Google Workspace (`aspmx.l.google.com` …) | Đứng sau Cloudflare (`104.17.0.0/16`). |
| `npmjs.org` | `sandy.ns.cloudflare.com`, `bayan.ns.cloudflare.com` | A nhiều bản ghi `104.16.x.34` · AAAA `2606:4700::6810:…` | Google Workspace | TXT: `"v=spf1 -all"` — SPF chặt nhất (`-all`). |

### 1.1 CAA (ai được phép phát hành chứng chỉ)

```text
github.com          → issuewild/issue: letsencrypt.org, digicert.com, sectigo.com, globalsign.com
githubassets.com    → issuewild: digicert.com, sectigo.com
githubusercontent.com → issue: digicert.com, letsencrypt.org, sectigo.com
githubapp.com       → issue: digicert.com, letsencrypt.org; issuewild: sectigo.com
github.net          → issue: letsencrypt.org, sectigo.com; issuewild: digicert.com, sectigo.com
npmjs.com           → issuewild: digicert.com; issue: letsencrypt.org; issuewild: pki.goog
npmjs.org           → issue: letsencrypt.org, digicert.com; issuewild: digicert.com
```
⇒ CAA được cấu hình trên **mọi** tên miền kiểm tra. Không thấy điểm bất thường.

### 1.2 DMARC — quan sát đáng chú ý

| Tên miền | DMARC (nguyên văn) |
|---|---|
| `github.com` | `"v=DMARC1; p=quarantine; sp=reject; pct=100; rua=mailto:dmarc@github.com; ruf=mailto:dmarc@github.com; fo=1"` |
| `npmjs.org` | `"v=DMARC1; p=reject; rua=mailto:dmarc@github.com; pct=100"` |
| **`npmjs.com`** | `"v=DMARC1; p=quarantine;  pct=5; rua=mailto:dmarc@github.com,mailto:d@rua.agari.com"` |
| `githubassets.com`, `githubusercontent.com`, `githubapp.com`, `github.net` | **không có bản ghi `_dmarc`** |
| `_dmarc.githubwebhooks.net` | `CNAME glb-db52c2cf8be544.github.com.` (trỏ về `github.com`; **không** trả về policy DMARC) |

> 🔎 **Quan sát (KHÔNG phải kết luận lỗ hổng — CHƯA XÁC MINH):**
> `npmjs.com` đặt `pct=5` ⇒ chính sách DMARC `quarantine` **chỉ được áp dụng cho 5% thư**.
> Đây là cấu hình yếu hơn đáng kể so với `npmjs.org` (`pct=100`, `p=reject`).
> **Chưa kiểm chứng** liệu điều này có khai thác được hay không, và **chưa đối chiếu** với
> danh sách ineligible của chương trình — GitHub **không** liệt kê SPF/DMARC là ineligible,
> nhưng chương trình **GitLab thì có** ("SPF and DKIM issues"). Với GitHub: **chưa xác minh**.

---

## 2. Bề mặt web công khai

Nguồn thô: `recon_github.txt` dòng 432–949.

### 2.1 `https://github.com/` — header công khai (nguyên văn, rút gọn phần dài)

```text
HTTP/2 200
server: github.com
x-github-edge-region: southeastasia
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 0
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
content-security-policy: default-src 'none'; ... script-src github.githubassets.com
    'sha256-tSjmyPUky1KbRZ0fw9VUil3wFEbeM82rtbJDygGJAXw='; frame-ancestors 'none';
    object-src 'none' (không có trong chuỗi); upgrade-insecure-requests
set-cookie: _gh_sess=...; path=/; HttpOnly; secure; SameSite=Lax
set-cookie: _octo=...; domain=.github.com; path=/; secure; SameSite=Lax
set-cookie: logged_in=no; domain=.github.com; path=/; HttpOnly; secure; SameSite=Lax
```

**Quan sát:** HSTS có `preload` + `includeSubdomains`. CSP `default-src 'none'` và
`script-src` chỉ cho **một** hash SHA-256 cố định + `github.githubassets.com` — rất chặt.
`x-frame-options: deny` + `frame-ancestors 'none'`. Không thấy cấu hình yếu.
`x-github-edge-region: southeastasia` tiết lộ vùng edge phục vụ (do máy chạy ở VN).

### 2.2 `robots.txt` — trích các dòng đáng chú ý (nguyên văn)

```text
Disallow: /.git/
Disallow: */.git/
Disallow: /*.git$
Disallow: /search$
Disallow: /account-login
Disallow: /copilot/
Disallow: /*/*/issues/new
Disallow: /*/archive/
Allow: /security
Allow: /mcp
Crawl-delay: 1   (chỉ áp cho GPTBot, OAI-SearchBot, ClaudeBot, anthropic-ai, PerplexityBot)
```
⇒ Đây là **quy ước thu thập dữ liệu**, KHÔNG phải lỗ hổng. Ghi lại vì § High-Value Recon Checks
trong skill `ctf-web` coi `robots.txt` là nguồn liệt kê bề mặt. **Không** dùng nó để suy ra
đường dẫn nhạy cảm rồi dò — dò là hoạt động chủ động, ngoài phạm vi T3.

### 2.3 `/.well-known/security.txt` — xác nhận kênh chính thức

```text
Contact: https://hackerone.com/github
Acknowledgments: https://hackerone.com/github/hacktivity
Policy: https://bounty.github.com
Expires: 2026-10-31T13:50:56z
```
⇒ **Bằng chứng quan trọng nhất của buổi trinh sát này:** xác nhận `bounty.github.com` là
chính sách chính thức và HackerOne là kênh duy nhất. `security.txt` ở gốc (`/security.txt`)
trả `Not Found` — chỉ bản `.well-known` tồn tại.

### 2.4 Chứng chỉ TLS (1 handshake, không quét)

```text
subject=CN = github.com
issuer=C = GB, O = Sectigo Limited, CN = Sectigo Public Server Authentication CA DV E36
notBefore=Sep  1 00:00:00 2026 GMT
notAfter=Nov 29 23:59:59 2026 GMT
X509v3 Subject Alternative Name:
    DNS:github.com, DNS:www.github.com
```

> 🔎 **Quan sát (CHƯA XÁC MINH):** chứng chỉ trả về từ edge này là **DV** (Domain Validation)
> của Sectigo và **chỉ có 2 SAN**, không có wildcard, không có OV/EV. Với một tổ chức như GitHub,
> điều này có thể do edge CDN trả chứng chỉ theo vùng. **Tôi chưa xác minh** chứng chỉ này có
> phải là chứng chỉ chuẩn của GitHub ở mọi vùng hay không. **Không kết luận.**

---

## 3. Ứng viên chuyển ExploitDeep (T4) — kèm mức độ tin cậy

> ⛔ **Tôi KHÔNG tự khai thác.** Mọi mục dưới đây là **quan sát bề mặt**, chưa phải lỗ hổng.
> **Chuyển qua task board** theo đúng lệnh T3. ExploitDeep phải tự đối chiếu với
> `SCOPE.md` §4b (ineligible) **trước khi** động vào.

| # | Ứng viên | Bằng chứng | Độ tin cậy | Cảnh báo |
|---|---|---|---|---|
| C1 | `npmjs.com` DMARC `p=quarantine; pct=5` | `recon_github.txt` dòng TXT `_dmarc.npmjs.com` | **THẤP** | Cần xác minh email spoofing có nằm ngoài ineligible không; GitHub chưa loại trừ tường minh, nhưng **chưa xác minh** đây là finding được thưởng. Rủi ro: bị coi là "known risk". |
| C2 | `github.net` / `githubassets.com` / `githubusercontent.com` **không có DMARC** | bảng §1.2 | **RẤT THẤP** | Các apex này không có A record → không phải bề mặt web. Gần như chắc chắn là chủ ý. |
| C3 | Chứng chỉ DV 2-SAN trên `github.com` | §2.4 | **RẤT THẤP** | Nhiều khả năng là hành vi edge/CDN bình thường. **Chưa xác minh.** |
| C4 | `_dmarc.githubwebhooks.net` → `CNAME github.com` không trả policy | §1.2 | **RẤT THẤP** | **Không phải subdomain takeover** — target `github.com` tồn tại và do GitHub sở hữu. Chỉ là cấu hình DMARC thiếu. |

**Đánh giá thẳng thắn của tôi:** buổi trinh sát thụ động này **KHÔNG tìm ra ứng viên nào có
độ tin cậy cao.** Bề mặt GitHub được cấu hình rất tốt (HSTS preload, CSP chặt, SPF `-all`,
CAA đầy đủ, `x-frame-options: deny`). Đây là kết quả **trung thực** — tôi không thổi phồng
quan sát yếu thành "lỗ hổng" để có sản phẩm báo cáo.

---

## 4. Kết quả âm tính (đã kiểm, không thấy gì)

| Hạng mục | Kết quả |
|---|---|
| Zone transfer (`AXFR`) | **KHÔNG thử** — đây là hoạt động chủ động, ngoài phạm vi T3 |
| Subdomain enumeration | **KHÔNG thực hiện** — `subfinder`/`amass` không có trên máy (`MISSING`) |
| Port scanning | **KHÔNG thực hiện** — `nmap` không có trên máy (`MISSING`) |
| Lỗi cấu hình header rõ ràng | Không thấy: HSTS preload ✅, CSP chặt ✅, `x-frame-options: deny` ✅, `nosniff` ✅ |
| SPF hở | `githubassets.com` `-all`, `npmjs.org` `-all` — chặt. `github.com` **chưa lấy được** (timeout) |
| Bản ghi CNAME trỏ ra dịch vụ bên thứ ba | `_dmarc.githubwebhooks.net` → `github.com` (nội bộ, không phải takeover) |

---

## 5. Hạn chế & điều CHƯA xác minh

1. `dig github.com TXT` **timeout** ⇒ SPF gốc của `github.com` **chưa xác minh**.
2. Chỉ kiểm **8 tên miền apex**; **không** liệt kê subdomain (không có công cụ, và đó là hoạt
   động chủ động/xâm nhập hơn so với mức T3 cho phép).
3. Chứng chỉ TLS chỉ đọc **1 lần** từ **1 edge** (khu vực Đông Nam Á) — có thể khác theo vùng.
4. `whois` **không có trên máy** ⇒ không tra được thông tin đăng ký tên miền.
5. Toàn bộ mục §1.2 và §2.4 là **quan sát thô**, **chưa** đối chiếu đầy đủ với 517 dòng
   ineligible ⇒ **chưa khẳng định** bất kỳ mục nào là finding hợp lệ.
