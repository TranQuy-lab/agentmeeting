# RECON — Cloudflare Public Bug Bounty (trinh sát THỤ ĐỘNG)

**Chương trình:** Cloudflare — xem [`SCOPE.md`](SCOPE.md) (scope đã trích nguyên văn)
**Người thực hiện:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Ngày chạy:** `2026-10-01`, giờ máy UTC `2026-10-01T13:51:4xZ`
**Trạng thái:** ✅ **Đã verify — T14 PASS** (`reviews/CROSS.md` §2.8, mốc `03d304b`). Đây là *quan sát bề mặt*, KHÔNG phải kết luận lỗ hổng.

---

## 0. Phạm vi phương pháp & tuyên bố đạo đức

**CHỈ thụ động.** Xem bảng phương pháp đầy đủ ở
[`../github/RECON.md`](../github/RECON.md) §0 — cùng script `recon.sh`, cùng giới hạn.

Tổng cho Cloudflare: **40 request** (35 `dig` + `curl` robots.txt/security.txt/header + 1 TLS
handshake + 3 request bổ sung theo redirect), **5 tên miền**. 39 rc=0, 1 timeout DNS ghi rõ bên dưới.

Lệnh thô: `agents/bountyrecon/tasks/T3/EVIDENCE/recon_cloudflare.txt` (301 dòng + phần supplement).

> ⛔ **TUYÊN BỐ TUÂN THỦ — BẮT BUỘC ĐỌC:** Cloudflare cấm test vào khách hàng của họ
> ("Do not perform tests against customers of Cloudflare") và yêu cầu scanner chỉ được dùng
> IP trong `https://cloudflare.com/ips`. **T3 chỉ đọc DNS/robots/header công khai của tài sản
> Cloudflare sở hữu** — không chạm IP khách hàng, không gửi payload, không quét.

**Trung thực về kết quả:** 1 truy vấn thất bại —
`dig cloudflare.com TXT` → `;; communications error to 127.0.0.53#53: timed out` (rc=9).
⇒ **SPF gốc của `cloudflare.com`: CHƯA XÁC MINH.** Không suy đoán.

---

## 1. Bản ghi DNS công khai

Nguồn thô: `recon_cloudflare.txt`.

| Tên miền | NS | A / AAAA | MX |
|---|---|---|---|
| `cloudflare.com` | `ns3`–`ns7.cloudflare.com` (tự vận hành) | A `104.16.132.229`, `104.16.133.229` · AAAA `2606:4700::6810:85e5`, `…84e5` | `5 mxb-canary…`, `10 mxb…`, `5 mxa-canary…` (`*.global.inbound.cf-emailsecurity.net`) |
| `api.cloudflare.com` | `merlin.ns.cloudflare.com`, `linda.ns.cloudflare.com` | A nhiều bản ghi `104.19.192.175/176/177/29`, `104.19.193.29` · AAAA `2606:4700:300a::6813:c0ae` … | rỗng |
| `dash.cloudflare.com` | `merlin`/`linda.ns.cloudflare.com` | A `104.17.110.184`, `104.17.111.184` · AAAA `2606:4700::6811:6fb8`, `…6eb8` | rỗng |
| `cloudflareworkers.com` | `sofia`/`clyde.ns.cloudflare.com` | A `104.17.54.117`, `104.17.55.117` · AAAA `2606:4700::6811:3675`, `…3775` | rỗng |
| `www.cloudflare.com` | `vin`/`jule.ns.cloudflare.com` | A `104.16.123.96`, `104.16.124.96` · AAAA `2606:4700::6810:7b60`, `…7c60` | rỗng |

**Quan sát:** mọi bản ghi A đều nằm trong các dải Cloudflare công bố
(`104.16.0.0/13`, `104.17.0.0/16`, `104.19.0.0/16`, `2606:4700::/32`). Nhất quán với
"hạ tầng của chính Cloudflare". **Chưa xác minh** từng dải bằng `cloudflare.com/ips` — **cần
làm trước khi T4 chạm bất cứ IP nào.**

### 1.1 TXT đáng chú ý (nguyên văn)

```text
cloudflareworkers.com  "v=spf1 -all"                              ← SPF chặt nhất
dash.cloudflare.com    "google-site-verification=HF9tnjO_sKKqJwktMzJNRImLQ_TyJocDqQqOfUvg8Cg"
www.cloudflare.com     "adobe-idp-site-verification=6fa8fbb72d7bb29889c39830d60eb0309c678510fef7692ee2679400a4096349"
_dmarc.cloudflare.com  "v=DMARC1; p=reject; sp=reject; adkim=r; aspf=r; pct=100; rua=mailto:a1c47f179bc04efd8ee4dcd4d85dfc65@dmarc-reports.cloudflare.net,mailto:rua@cloudflare.com"
_dmarc.cloudflareworkers.com "v=DMARC1; p=reject; sp=reject; adkim=s; aspf=s;"
```

### 1.2 CAA (nguyên văn, rút gọn)

```text
cloudflare.com        issuewild: digicert.com, ssl.com ; issue: ssl.com ;
                      iodef: mailto:tls-abuse@cloudflare.com
cloudflareworkers.com issuewild: letsencrypt.org, comodoca.com, pki.goog ;
                      iodef: mailto:tls-abuse@cloudflare.com
```
⇒ CAA có `iodef` (kênh báo cáo lạm dụng) trên cả hai — thực hành tốt.
⇒ DMARC `p=reject; sp=reject` toàn bộ ⇒ **mạnh**, không có điểm yếu kiểu `pct` như `npmjs.com`.

---

## 2. Bề mặt web công khai

### 2.1 `https://cloudflare.com/` → **301** sang `https://www.cloudflare.com/`

```text
HTTP/2 301
location: https://www.cloudflare.com/
strict-transport-security: max-age=15780000; includeSubDomains
set-cookie: __cf_bm=...; HttpOnly; SameSite=None; Secure; Path=/; Domain=cloudflare.com
server: cloudflare
cf-ray: a43bf18d0a827d2e-HKG
```

### 2.2 `https://www.cloudflare.com/` → **200** (header công khai, rút gọn)

```text
HTTP/2 200
strict-transport-security: max-age=31536000; includeSubDomains
content-security-policy: default-src 'self'; ... object-src 'none'; frame-ancestors 'none';
                         upgrade-insecure-requests
cross-origin-opener-policy: unsafe-none
cross-origin-resource-policy: cross-origin
permissions-policy: geolocation=(), camera=(), microphone=()
referrer-policy: strict-origin-when-cross-origin
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-served-by: marketing-site
x-rm: GW
server: cloudflare
```

> 🔎 **Quan sát (CHƯA XÁC MINH, độ tin cậy THẤP):** `cloudflare.com` đặt HSTS
> `max-age=15780000` (~6 tháng) **không có** `preload`, trong khi `www.cloudflare.com` đặt
> `max-age=31536000` (1 năm). Chênh lệch nhỏ. **Gần như chắc chắn không đủ điều kiện thưởng** —
> và cần đối chiếu với danh sách báo-cáo-bị-từ-chối của Cloudflare (policy dài 434 dòng có
> nhiều mục loại trừ "missing security headers"-kiểu). **Không kết luận.**
>
> `x-frame-options: SAMEORIGIN` (không phải `DENY`) trên trang marketing tĩnh — cũng thuộc
> nhóm "cấu hình yếu nhẹ", **không** phải lỗ hổng khai thác được.

### 2.3 `robots.txt` (trên `www.cloudflare.com` — apex 301 nên phải theo redirect)

```text
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Cohere-ai
Allow: /
Content-Signal: ai-train=yes, search=yes, ai-input=yes
```
⇒ Cho phép thu thập rộng rãi. Không có thông tin bề mặt ẩn.

### 2.4 `/.well-known/security.txt` — xác nhận kênh chính thức

```text
Contact: https://hackerone.com/cloudflare
Contact: https://www.cloudflare.com/abuse/
Policy: https://www.cloudflare.com/disclosure/ 
Hiring: https://www.cloudflare.com/careers/jobs/
Preferred-Languages: en
Canonical: https://www.cloudflare.com/.well-known/security.txt
```
⇒ **Bằng chứng quan trọng nhất buổi trinh sát:** xác nhận `hackerone.com/cloudflare` là kênh
chính thức. Policy bổ sung tại `cloudflare.com/disclosure/`.

### 2.5 Chứng chỉ TLS (1 handshake, không quét)

```text
subject=CN = cloudflare.com
issuer=C = US, O = Google Trust Services, CN = WE1
notBefore=Sep  5 22:29:39 2026 GMT
notAfter=Dec  4 23:29:33 2026 GMT
X509v3 Subject Alternative Name:
    DNS:cloudflare.com, DNS:ns.cloudflare.com, DNS:*.ns.cloudflare.com,
    DNS:*.secondary.cloudflare.com, DNS:secondary.cloudflare.com
```

> 🔎 **Quan sát (CHƯA XÁC MINH):** một chứng chỉ duy nhất phục vụ cả `cloudflare.com` **và**
> hạ tầng DNS (`*.ns.cloudflare.com`, `*.secondary.cloudflare.com`) — chứng tỏ cùng một
> termination point. **Chưa xác minh** ý nghĩa bảo mật. **Không kết luận.**

---

## 3. Ứng viên chuyển ExploitDeep (T4)

| # | Ứng viên | Bằng chứng | Độ tin cậy | Cảnh báo |
|---|---|---|---|---|
| C1 | HSTS apex ngắn hơn + không `preload` | §2.1 vs §2.2 | **RẤT THẤP** | Gần như chắc chắn bị loại là "missing security headers". **Không nên theo.** |
| C2 | `x-frame-options: SAMEORIGIN` trên trang marketing | §2.2 | **RẤT THẤP** | Trang tĩnh không có hành động nhạy cảm ⇒ clickjacking vô hại. **Không nên theo.** |
| C3 | Cert dùng chung cho apex + nameserver | §2.5 | **RẤT THẤP** | Quan sát kiến trúc, không phải lỗi. |

**Đánh giá thẳng thắn:** **KHÔNG có ứng viên nào đáng theo.** Bề mặt Cloudflare được cấu hình
chặt (HSTS includeSubDomains, CSP có `object-src 'none'` + `frame-ancestors 'none'`,
DMARC `p=reject; sp=reject`, CAA có `iodef`). Tôi **không** thổi phồng các quan sát yếu này.

> 🚨 **KHUYẾN NGHỊ (đã nêu trong [`SCOPE.md`](SCOPE.md) §5):** Cloudflare là
> **nhà cung cấp CDN/WAF** — phần lớn hạ tầng "trông giống Cloudflare" là **tài sản khách hàng**.
> Chạm nhầm = **loại vĩnh viễn** khỏi chương trình. **Đề nghị Admin KHÔNG mở T4 cho Cloudflare**
> ở giai đoạn này. Ưu tiên GitHub/GitLab.

---

## 4. Kết quả âm tính

| Hạng mục | Kết quả |
|---|---|
| Port scan / service scan | **KHÔNG thực hiện** (`nmap` MISSING) |
| Subdomain enumeration | **KHÔNG thực hiện** (`subfinder`/`amass` MISSING) |
| Zone transfer | **KHÔNG thử** (hoạt động chủ động) |
| DMARC yếu | **Không có** — `p=reject; sp=reject` trên cả 2 tên miền kiểm tra |
| SPF hở (`~all` hoặc `?all`) | **Không có** — `cloudflareworkers.com` dùng `-all` |
| `security.txt` thiếu | **Không** — có, đúng chuẩn, có `Policy` + `Canonical` |
| Subdomain takeover (CNAME trỏ ra ngoài) | **Không thấy** — mọi bản ghi đều trong dải Cloudflare |

---

## 5. Hạn chế & điều CHƯA xác minh

1. `dig cloudflare.com TXT` **timeout** ⇒ SPF gốc **chưa xác minh**.
2. **Chưa đối chiếu** các bản ghi A với danh sách chuẩn `https://cloudflare.com/ips`
   ⇒ **chưa khẳng định** chúng thuộc Cloudflare (dù dải IP rất khớp).
3. `cloudflare.com`/`robots.txt` và `/security.txt` ở apex trả 301 — đã lấy lại qua
   `www.cloudflare.com`; bản apex chưa kiểm bằng `curl -L` trên chính apex.
4. Chỉ kiểm **5 tên miền**; policy liệt kê **55 tài sản**.
5. Policy Cloudflare dài 434 dòng với nhiều mục loại trừ chi tiết (report quality, WAF bypass,
   AI/MCP, memory-safety) — **tôi chưa đọc hết** để đối chiếu từng quan sát. **Chưa xác minh.**
