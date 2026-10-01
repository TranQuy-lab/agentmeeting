# SCOPE — Cloudflare Public Bug Bounty

**Chương trình:** Cloudflare Public Bug Bounty
**Tổ chức:** Cloudflare, Inc. (công ty tư nhân, Hoa Kỳ) — **KHÔNG phải** cơ quan nhà nước.
**Nền tảng:** HackerOne — handle `cloudflare` → <https://hackerone.com/cloudflare>
**URL chính sách gốc:** <https://hackerone.com/cloudflare?view=policy>
**Ngày fetch:** `2026-10-01` (giờ máy UTC `2026-10-01T13:5xZ`, giờ VN `2026-10-01 20:5x +07`)
**Người lập:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Trạng thái:** ✅ **Trích được NGUYÊN VĂN in-scope + out-of-scope + cấm.**
⚠️ **Mức thưởng: chỉ có khoảng min/max công bố, KHÔNG có bảng theo mức độ trong policy.**

> ⚠️ **Chưa được verify.** Theo D-004, người viết KHÔNG tự verify. Chờ Reviewer1.

---

## 0. Phương pháp fetch

| Bước | Lệnh / URL | Kết quả |
|---|---|---|
| 1 | `POST https://hackerone.com/graphql` (công khai, không auth) `team(handle:"cloudflare")` | HTTP 200, JSON parse OK |
| 2 | `curl -sS -I https://cloudflare.com/` | HTTP 200 (xem `recon_cloudflare.txt`) |

Script + JSON thô: `agents/bountyrecon/tasks/T3/EVIDENCE/` (`fetch_h1.py`, `h1_cloudflare.json`,
`policy_cloudflare.md`, `scope_cloudflare.md`, `recon_cloudflare.txt`).

---

## 1. TRÍCH NGUYÊN VĂN — IN SCOPE

### 1a. Tên miền / tài sản web (từ `structured_scopes`, `eligible_for_submission=true`)

```text
URL          dash.cloudflare.com           max_severity=critical
             instruction: "The Cloudflare dashboard (https://dash.cloudflare.com/) and any
             direct calls from the dashboard to other Cloudflare owned resources are
             considered in scope."

URL          cloudflareworkers.com         critical
URL          *.teams.cloudflare.com        critical
URL          api.cloudflare.com            critical
URL          *.cloudflare.com              critical
             instruction: "Excluding support.cloudflare.com, community.cloudflare.com
             and other SaaS applications"
URL          http://github.com/cloudflare  critical
URL          one.dash.cloudflare.com       critical
URL          dash.teams.cloudflare.com     critical   instruction: "Secondary scope."
URL          http://cloudflare.com/apps/   critical
             instruction: "This is the Cloudflare Marketplace. Only the platform itself
             and first-party apps (those created by Cloudflare) are considered in scope."
OTHER        *.cloudflarepartners.com      critical
SOURCE_CODE  https://github.com/cloudflare/workerd     critical
SOURCE_CODE  https://github.com/cloudflare/vinext      critical
```

### 1b. Sản phẩm / dịch vụ trong scope (n=55 tổng; `eligible_for_bounty=true`)

```text
Cloudflare Pages | CDNJS | WARP Mobile Apps | Cloudflare Access | Stream |
1.1.1.1 Resolver | Magic Transit | Spectrum | Load Balancing | Bot Management |
Cloudflare Zero Trust/Cloudflare One | Open source tools from Cloudflare | Area 1 |
Cloudflare D1 | Cloudflare R2 | WARP desktop client | Cloudflare DNS | Cloudflare CASB |
Workers | Cloudflare Tunnel | AMP Real URL | Cloudflare Cache | Magic Firewall |
Cloudflare Zaraz | China Network | API Shield | Gateway | Browser Isolation |
AI Gateway | Vectorize | Hyperdrive | Workers KV | Cloudflare Analytics |
Cloudflare Durable Objects | Waiting Room | Magic WAN | Data Loss Prevention (DLP) |
SSL/TLS | Cloudflare Workers CI | Images | Workers AI (AI_MODEL) | Durable Objects |
Argo Tunnel
```

> 📝 **Quan sát của tôi (KHÔNG nguyên văn):** `Images` và `Durable Objects` có
> `max_severity = none` dù `eligible_for_bounty = true`; `Workers AI` là `AI_MODEL` với
> ghi chú "Reports on Prompt Injection attacks on models hosted by Workers AI without
> demonstrating an impact on Cloudflare will not be accepted."
> Bảng đầy đủ kèm `instruction`: `scope_cloudflare.md`.

---

## 2. TRÍCH NGUYÊN VĂN — OUT OF SCOPE

`structured_scopes`, `eligible_for_submission=false` (n=28), nguyên văn `instruction`:

```text
*.plugins.realtime.cloudflare.com
support.cloudflare.com       — "This asset is hosted by Zendesk, and as such these reports
                                should be submitted to their program instead via @Zendesk"
community.cloudflare.com
support.cloudflarewarp.com   — "This asset is hosted by Zendesk ... via @zendesk."
waf.cumulusfire.net          — "This domain must be used for testing WAF bypasses."
events.www.cloudflare.com
demo.realtime.cloudflare.com
api.staging.realtime.cloudflare.com
examples.realtime.cloudflare.com
react-examples.realtime.cloudflare.com
app.dyte.io
test.realtime.cloudflare.com
files.plugins.realtime.cloudflare.com
https://github.com/cloudflare/vinext-private
https://github.com/cloudflare/moq-rs
https://github.com/cloudflare/privacy-gateway-server-go
https://github.com/cloudflare/saffron.git
https://github.com/cloudflare/realtimekit-web-examples
https://github.com/cloudflare/recapn
https://github.com/cloudflare/computer
https://github.com/cloudflare/cloudflare-os
https://github.com/cloudflare/templates
https://github.com/cloudflare/pp-browser-extension
https://github.com/cloudflare/agentic-inbox
https://github.com/cloudflare/cf
https://github.com/cloudflare/wirefilter/
Turnstile                    — "https://developers.cloudflare.com/turnstile/"
172.65.0.0/16                — "These are customer applications protected by Cloudflare
                                Spectrum, hence out of scope"
```

Ngoài ra policy còn loại trừ gián tiếp các SaaS khác qua instruction của `*.cloudflare.com`
("Excluding support.cloudflare.com, community.cloudflare.com and other SaaS applications").

---

## 3. TRÍCH NGUYÊN VĂN — QUY ĐỊNH CẤM / GIỚI HẠN

Nguồn: `policy_cloudflare.md` § `## Program Rules`, dòng 10–25.

```text
* You must make a good faith effort to avoid privacy violations, destruction of data and interruption or degradation of Cloudflare's services and products during your research.
* All attacks must be executed against your own Cloudflare Account. You can sign up for a free Cloudflare account and use it for testing.
    * Accounts should be created with a `@wearehackerone.com` email address.
* Do not perform tests against customers of Cloudflare.
* Once you find a vulnerability, report it and reach out to us before you use the vulnerability to pivot across multiple in-scope assets.
* Make sure that scanners have a narrow scope set that is [limited to authorized Cloudflare IPs only](https://cloudflare.com/ips). Aggressive, overly broad scans or those which include Cloudflare customer IPs without permission will be considered tests against Cloudflare customers.
* Do not send unsolicited bulk messages (spam) or unauthorized messages.
* Do not knowingly post, transmit, upload, link to, or send any program or script that might be considered malicious.
* If your report is the product of collaboration, please add your collaborators _before the bounty_ is awarded.

Any of the activities below will result in disqualification from the program permanently:
* Testing against Cloudflare customers, partners, service providers, suppliers, or vendors
* Social engineering of Cloudflare employees/contractors, including but not limited to: pre-authenticated clickjacking, phishing, impersonating Cloudflare in emails or convincing customer support to do something on behalf of another user
* Physical attacks against Cloudflare employees/contractors, offices, or data centers
* Executing Denial of Service attacks against Cloudflare
* Publishing, blogging, presenting, or otherwise publicly disclosing a report or its details within 90 days of submission without prior written approval from Cloudflare. This includes social media posts, conference talks, blog articles, YouTube videos, and any other public channel. Researchers who wish to disclose should coordinate with us per the Disclosure section below.
```

Về lưu trữ dữ liệu — § `## Submitting a report`, dòng 34:

```text
- Do not store any Cloudflare IP or PII information once the report is submitted.
```

---

## 4. MỨC THƯỞNG CÔNG BỐ

**Trung thực: policy text của Cloudflare KHÔNG có bảng thưởng theo mức độ.** Nguyên văn
`policy_cloudflare.md` § `## Rewards`, dòng 388:

```text
When duplicates occur, we award only the first report that was received, provided that it can be fully reproduced. If multiple vulnerabilities are caused by one underlying issue, we reserve the right to award only one bounty. All reward decisions are at the sole discretion of Cloudflare.
```

Và dòng 426:

```text
The decision to pay a reward is entirely at our discretion.
```

Khoảng thưởng do **nền tảng HackerOne** công bố trên trang chương trình:

```json
{"minimum_bounty_table_value": 100, "maximum_bounty_table_value": 10000,
 "top_bounty_lower_amount": 1000, "top_bounty_upper_amount": 10000,
 "average_bounty_lower_amount": 250, "average_bounty_upper_amount": 350,
 "formatted_total_bounties_paid_amount": 628500, "offers_bounties": true}
```

⇒ **Kết luận về mức thưởng:** khoảng công bố **100 USD – 10.000 USD**; trung bình ~250–350 USD;
tổng đã trả **628.500 USD** (số của HackerOne, **chưa xác minh độc lập**). Không có bảng
severity→số tiền. **Ghi rõ: chưa xác minh** đối với mọi con số ngoài khoảng min/max.

---

## 5. KẾT LUẬN SCOPE (tổng hợp của tôi — KHÔNG nguyên văn)

| Hạng mục | Kết luận |
|---|---|
| Trích được nguyên văn in-scope? | ✅ **CÓ** (55 tài sản) |
| Trích được nguyên văn out-of-scope? | ✅ **CÓ** (28 tài sản) |
| Trích được quy định cấm? | ✅ **CÓ** (rất chặt — xem §3) |
| Mức thưởng công bố? | ⚠️ **MỘT PHẦN** — chỉ có khoảng min/max, không có bảng severity |
| Tài sản dễ kiểm chứng? | ✅ **CÓ** — `cloudflare.com`, `api.cloudflare.com`, `dash.cloudflare.com` |
| Đủ điều kiện chuyển ExploitDeep (T4)? | ⚠️ **CÓ scope**, nhưng **rào cản lớn** — xem cảnh báo dưới |

### 🚨 CẢNH BÁO ĐẶC THÙ — BẮT BUỘC ĐỌC TRƯỚC KHI CHẠM

Cloudflare là nhà cung cấp CDN/WAF. **Phần lớn IP và tên miền "trông giống Cloudflare"
thực chất là tài sản của KHÁCH HÀNG Cloudflare, không phải Cloudflare.**

> Trích nguyên văn: "Do not perform tests against customers of Cloudflare."
> Trích nguyên văn: "Make sure that scanners have a narrow scope set that is
> [limited to authorized Cloudflare IPs only](https://cloudflare.com/ips)."

⇒ Bất kỳ hoạt động nào chạm tới IP nằm ngoài danh sách `https://cloudflare.com/ips` sẽ bị
coi là **tấn công khách hàng Cloudflare** ⇒ loại khỏi chương trình vĩnh viễn.
Đây là rủi ro pháp lý nghiêm trọng, không chỉ là rủi ro hành chính.

⇒ **Khuyến nghị của tôi với Admin:** Cloudflare **KHÔNG phù hợp** làm target khai thác cho
ExploitDeep ở giai đoạn này, vì phần lớn bề mặt không thể phân biệt an toàn giữa hạ tầng
Cloudflare và khách hàng của họ. Nên ưu tiên GitHub/GitLab. Nếu vẫn chọn Cloudflare thì
**chỉ** dùng account riêng của mình trên `dash.cloudflare.com` và **chỉ** chạm
`https://cloudflare.com/ips`.

**Không có tài sản nào trong scope thuộc:** cơ quan nhà nước, hạ tầng trọng yếu, hay tổ chức
Việt Nam. Điều kiện bất khả xâm phạm của D-005 được thoả.
