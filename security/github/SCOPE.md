# SCOPE — GitHub Security Bug Bounty

**Chương trình:** GitHub Security Bug Bounty
**Tổ chức:** GitHub, Inc. (công ty tư nhân, Hoa Kỳ) — **KHÔNG phải** cơ quan nhà nước.
**Nền tảng:** HackerOne — handle `github` → <https://hackerone.com/github>
**URL chính sách gốc:** <https://bounty.github.com/>
**URL bảng thưởng:** <https://bounty.github.com/rewards>
**Ngày fetch:** `2026-10-01` (giờ máy UTC `2026-10-01T13:49:44Z`, giờ VN `2026-10-01 20:49:44 +07`)
**Người lập:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Trạng thái:** ✅ **Trích được NGUYÊN VĂN in-scope + out-of-scope + cấm + mức thưởng.**

> ⚠️ **Chưa được verify.** Theo D-004, người viết KHÔNG tự verify. Chờ Reviewer1 kiểm lại.
> Mọi câu trong khối trích dẫn dưới đây là bản sao nguyên văn từ nguồn đã fetch; phần
> không trích dẫn là tổng hợp của tôi và được ghi rõ.

---

## 0. Phương pháp fetch (để Reviewer1 chạy lại được)

| Bước | Lệnh / URL | Kết quả |
|---|---|---|
| 1 | `POST https://hackerone.com/graphql` (GraphQL công khai, KHÔNG cần auth) truy vấn `team(handle:"github"){ policy structured_scopes }` | HTTP 200, JSON parse OK |
| 2 | `curl -sS https://bounty.github.com/` | HTTP 200, 5240 B |
| 3 | `curl -sS https://bounty.github.com/rewards` | HTTP 200, 6258 B |
| 4 | `curl -sS https://github.com/.well-known/security.txt` | HTTP 200 — xác nhận `Policy: https://bounty.github.com` |

Script fetch và JSON thô nằm tại `agents/bountyrecon/tasks/T3/EVIDENCE/`
(`fetch_h1.py`, `h1_github.json`, `gh_bounty.html`, `gh_rewards.html`).

**Bằng chứng nguồn chính sách là chính thức** — trích nguyên văn `https://github.com/.well-known/security.txt`:

```text
Contact: https://hackerone.com/github
Acknowledgments: https://hackerone.com/github/hacktivity
Preferred-Languages: en
Canonical: https://github.com/.well-known/security.txt
Policy: https://bounty.github.com
Hiring: https://github.careers
Expires: 2026-10-31T13:50:56z
```

---

## 1. TRÍCH NGUYÊN VĂN — IN SCOPE

Nguồn: `policy` của chương trình GitHub trên HackerOne, mục `## Scope`.
Bản đầy đủ: `agents/bountyrecon/tasks/T3/EVIDENCE/policy_github.md` (dòng 98–157).

```text
## Scope

GitHub runs a number of services but only submissions under the following domains are eligible for rewards. Any GitHub-owned domains not listed below are *not* in scope, *not* eligible for rewards, and *not* covered by [our legal safe harbor](https://bounty.github.com#legal_safe_harbor).

### github.com

This is our main domain for hosting user-facing GitHub services.. All subdomains under `github.com` are in-scope *except*:
* `blog.github.com`
* `community.github.com`
* `email.enterprise.github.com`
* `email.finance.github.com`
* `email.staging.finance.github.com`
* `email.support.github.com`
* `email.verify.github.com`
* `google7650dcf6146f04d8.github.com`
* `k1._domainkey.github.com`
* `k1._domainkey.mcmail.github.com`
* `mcmail.github.com`
* `resources.github.com`
* `*.resources.github.com`
* `sgmail.github.com`
* `*.sgmail.github.com`
* `shop.github.com`
* `smtp.github.com`
* `*.smtp.github.com`

### githubassets.com

This is our domain for hosting static assets.. All subdomains under `githubassets.com` are in-scope

### githubusercontent.com

This is our domain for hosting and rendering users' data.. All subdomains under `githubusercontent.com` are in-scope

### githubapp.com

This is our domain for hosting employee-facing services.. All subdomains under `githubapp.com` are in-scope *except*:
* `atom-io.githubapp.com`
* `atom-io-staging.githubapp.com`
* `email.enterprise-staging.githubapp.com`
* `email.haystack.githubapp.com`
* `reply.githubapp.com`

### githubwebhooks.net

This is our domain for receiving webhooks for employee-facing services.. All subdomains under `githubwebhooks.net` are in-scope

### github.net

This is our domain for hosting GitHub's internal production services. Many of these services are not accessible from outside our internal network.. All subdomains under `github.net` are in-scope

### npmjs.com

This is the domain for npm's public-facing websites.. All subdomains under `npmjs.com` are in-scope

### npmjs.org

This is the domain for npm's registry, public-facing databases, and APIs.. All subdomains under `npmjs.org` are in-scope
```

**Tài sản phi-tên-miền trong scope** (trích `instruction` từ `structured_scopes`, `eligible_for_bounty=true`):

```text
GitHub Enterprise Cloud | GitHub Pages | GitHub Production Credentials | Dependabot |
GitHub for mobile | Copilot | Copilot for Business |
GitHub Enterprise Cloud with Data Residency (GHEC-DR) | Copilot Spaces |
Copilot Coding Agent | GitHub Spark | GitHub CSP | Copilot Chat on dotcom
```
(`asset_type = OTHER`, `max_severity = critical`, trừ `GitHub CSP` = `high` và `Copilot Chat on dotcom` = `high`.)

> 📝 **Quan sát của tôi (KHÔNG phải nguyên văn):** trường `asset_identifier` của 25 dòng
> `OTHER` trong scope GitHub bị lặp chuỗi `All Other Scope` — đây là cách HackerOne biểu diễn
> mục gộp, không phải 25 tài sản riêng biệt. Chi tiết đầy đủ ở `scope_github.md`.

---

## 2. TRÍCH NGUYÊN VĂN — OUT OF SCOPE

**(a) Tên miền loại trừ** — nằm ngay trong mục `## Scope` ở trên (danh sách `* except:` của
`github.com` và `githubapp.com`). Không trích lại để tránh trùng.

**(b) Mục out-of-scope khai báo tường minh** (`structured_scopes`, `eligible_for_submission=false`, n=14):

```text
enterprise.github.com  — "`enterprise.github.com` is commonly confused with the GitHub Enterprise Server product which is an on-premise instance of GitHub."
*.github.io            — "Individual sites which are hosted on GitHub Pages are out-of-scope."
git.io                 — "The git.io URL shortener is out-of-scope."
spectrum.chat          — "Spectrum is currently out-of-scope."
github.blog            — "github.blog is out-of-scope."
http://education.github.com/forum — "The GitHub Education Community forum is not in-scope and ineligible for rewards."
blog.github.com        — "The GitHub Blog is not in-scope and ineligible for rewards."
community.github.com   — "The GitHub Community forum is not in-scope and ineligible for rewards."
shop.github.com        — "The GitHub Shop is not in-scope and ineligible for rewards."
Atom                   — "Atom" (DOWNLOADABLE_EXECUTABLES)
Electron               — "Electron vulnerabilities which do not directly affect GitHub Desktop are out-of-scope and should be reported to the Electron developers."
GitHub Classroom Assistant — "The GitHub Classroom Assistant application is currently out-of-scope."
GitHub Education Community forum — "not in-scope and ineligible for rewards."
speakerdeck.com        — (không có instruction)
```

**(c) Bản ghi chỉ-được-gửi-không-được-thưởng** — các dòng có `eligible_for_submission=true`
nhưng `eligible_for_bounty=false`, ví dụ `https://github.com/Hacker0x01/react-datepicker`
và nhiều dòng `hackerone.com/graphql`. Xem bảng đầy đủ trong `scope_github.md`.

---

## 3. TRÍCH NGUYÊN VĂN — QUY ĐỊNH CẤM / GIỚI HẠN

Nguồn: `policy_github.md` § `### Performing your research`, dòng 45–58.

```text
* Do not impact other users with your testing, this includes testing vulnerabilities in repositories or organizations you do not own. If you are attempting to find an authorization bypass, you must use accounts you own.
* The following are **never** allowed and are ineligible for reward. We may suspend your GitHub account and ban your IP address for:

  * Performing distributed denial of service (DDoS) or other volumetric attacks
  * Spamming content
  * Large-scale vulnerability scanners, scrapers, or automated tools which produce excessive amounts of traffic.
    * Note: We _do_ allow the use of automated tools so long as they do not produce excessive amounts of traffic. For example, running one `nmap` scan against one host is allowed, but sending 65,000 requests in two minutes using Burp Suite Intruder is excessive.
* Researching denial-of-service attacks is allowed and eligible for rewards only if you follow these rules:

  * There are no limits for researching denial of service vulnerabilities against your own instance of [GitHub Enterprise Server](https://bounty.github.com/targets/github-enterprise-server.html). We strongly recommend/prefer this method for researching denial of service issues.
  * If you choose to test on GitHub proper (i.e. `https://github.com`)
    * Research **must** be performed in organizations or repositories you own
    * Stop **immediately** if you believe you have affected the availability of our services. Don't worry about demonstrating the full impact of your vulnerability, GitHub's security team will be able to determine the impact.
```

Về dữ liệu cá nhân (PII) — § `### Handling personally identifiable information (PII)`, dòng 69–72:

```text
* Do not intentionally access others' PII. If you suspect a service provides access to PII, limit queries to your own personal information.
* Report the vulnerability *immediately* and do not attempt to access any other data. The GitHub Security team will assess the scope and impact of the PII exposure.
* Limit the amount of data returned from services. For SQL injection, for example, limit the number of rows returned
* You must delete all your local, stored, or cached copies of data containing PII as soon as possible.
```

Về công bố — § `### Reporting your vulnerability`, dòng 79–81:

```text
* When reporting vulnerabilities you must keep all information on HackerOne. Do not post information to video-sharing or pastebin sites. Videos and images can be uploaded directly via HackerOne.
* During the course of an investigation, it may take time to resolve the issue you have reported. We ask that you refrain from publicly disclosing details regarding an issue you've reported until the fix has been publicly made available.
```

---

## 4. TRÍCH NGUYÊN VĂN — MỨC THƯỞNG CÔNG BỐ

Nguồn: <https://bounty.github.com/rewards> (HTTP 200, `2026-10-01`).

```text
Reward Guidelines
Every submission is evaluated individually. The amounts below are general
guidelines for our public and private programs, not guaranteed payouts.
Actual rewards vary based on the affected product, demonstrated impact,
exploitability, exposure, the percentage of users or systems affected, and
mitigating controls. Product-specific guidance, where available, takes
precedence.

Severity            Public program                      Private program
Critical            $10,000                             $30,000+
High                $5,000                              $20,000
Medium              $2,000                              $7,500
Low                 $250                                $1,000
Defense in depth    GitHub swag, no cash bounty

GitHub determines the final severity and reward after reviewing the
specific facts and demonstrated impact of each submission.
```

Và trích từ <https://bounty.github.com/>:

```text
GitHub Bug Bounty
Our bounty program gives a tip of the hat to these researchers and provides
rewards of $10,000 or more in our public program, and $30,000 or more in our
private program for critical vulnerabilities.
```

Số liệu tổng hợp công bố trên trang chương trình HackerOne (`team.bounty_table` metadata):

```json
{"minimum_bounty_table_value": 250, "maximum_bounty_table_value": 10000,
 "top_bounty_lower_amount": 10000, "top_bounty_upper_amount": 100000,
 "average_bounty_lower_amount": 617, "average_bounty_upper_amount": 617,
 "formatted_total_bounties_paid_amount": 6650165, "offers_bounties": true}
```
(`formatted_total_bounties_paid_amount` = **6.650.165 USD** đã trả; đây là số của nền tảng
HackerOne công bố, **chưa xác minh độc lập**.)

---

## 5. KẾT LUẬN SCOPE (tổng hợp của tôi — KHÔNG phải nguyên văn)

| Hạng mục | Kết luận |
|---|---|
| Trích được nguyên văn in-scope? | ✅ **CÓ** (8 nhóm tên miền + 13 tài sản `OTHER`) |
| Trích được nguyên văn out-of-scope? | ✅ **CÓ** (18 tên miền loại trừ + 14 mục tường minh) |
| Trích được quy định cấm? | ✅ **CÓ** (DDoS, scanner diện rộng, PII, công bố) |
| Mức thưởng công bố? | ✅ **CÓ** (bảng $250 – $30.000+) |
| Tài sản dễ kiểm chứng? | ✅ **CÓ** — `github.com`, `api.github.com`, `npmjs.com`, `gist.github.com` |
| Đủ điều kiện chuyển ExploitDeep (T4)? | ✅ **CÓ** — nhưng **cổng G4 vẫn cần chỉ thị bằng văn bản của Admin** |

**Cảnh báo bắt buộc cho ExploitDeep — trích nguyên văn:**
> "Only test for vulnerabilities on sites you know to be operated by GitHub and are in-scope.
> Some sites hosted on subdomains of `GitHub.com` are operated by third parties and should not be tested."

⇒ **Bất kỳ subdomain nào của `github.com` trỏ ra dịch vụ bên thứ ba đều NGOÀI SCOPE**, kể cả
khi không có tên trong danh sách loại trừ. Phải kiểm tra chủ sở hữu trước khi chạm.

**Không có tài sản nào trong scope thuộc:** cơ quan nhà nước, hạ tầng trọng yếu, hay tổ chức
Việt Nam. Điều kiện bất khả xâm phạm của D-005 được thoả.
