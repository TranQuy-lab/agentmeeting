# SCOPE — GitHub Security Bug Bounty

**Chương trình:** GitHub Security Bug Bounty
**Tổ chức:** GitHub, Inc. (công ty tư nhân, Hoa Kỳ) — **KHÔNG phải** cơ quan nhà nước.
**Nền tảng:** HackerOne — handle `github` → <https://hackerone.com/github>
**URL chính sách gốc:** <https://bounty.github.com/>
**URL bảng thưởng:** <https://bounty.github.com/rewards>
**Ngày fetch:** `2026-10-01` (giờ máy UTC `2026-10-01T13:49:44Z`, giờ VN `2026-10-01 20:49:44 +07`)
**Người lập:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Trạng thái:** ✅ **Trích được NGUYÊN VĂN in-scope + out-of-scope + cấm + mức thưởng.**

> ✅ **Đã verify — T14 PASS** (Reviewer1; `reviews/CROSS.md` §2.8, mốc `03d304b`; đã merge `4642e3c`). Theo D-004, người viết KHÔNG tự verify.
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

### 1b. Bảng tài sản GitHub kèm `archived_at` (AUTHORED — KHÔNG phải nguyên văn)

> 🧭 **Mục này do BountyRecon TẠO Ở T37 (D-027).** `§1` phía trên là **KHỐI TRÍCH NGUYÊN VĂN**
> và **KHÔNG bị sửa một ký tự nào** — đúng nguyên tắc *trích nguyên văn > yêu cầu định dạng*.
> Bảng dưới đây là **bảng tổng hợp do tôi lập** từ `structured_scopes` (đã TÁCH khỏi nguyên văn).
> Tự truy vấn lại `2026-10-01T15:28Z` (`archived:false` / `archived:true`).
>
> **Thống kê tự đo:** `archived:false` **39** · `archived:true` **158** · TỔNG **197** · `sub=True` **183** (live **27** + archived **156**).
>
> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** **KHÔNG** suy ra *"ngoài scope"* cho bản ghi
> `archived_at != None`. Chỉ được khẳng định: bảng **THIẾU chiều `archived_at`** ⇒
> **KHÔNG PHÂN BIỆT ĐƯỢC** còn hiệu lực hay đã nghỉ hưu.
> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi archived
> **CHƯA có định nghĩa chính thức** ⇒ hiệu lực **CHƯA XÁC MINH**. Cần trả lời chính thức từ chương trình.

| asset_type | asset_identifier | sub | bounty | max_severity | **archived_at** |
|---|---|---|---|---|---|
| URL | *.github.net | True | True | critical | `None` |
| URL | *.githubapp.com | True | True | critical | `None` |
| URL | *.githubusercontent.com | True | True | critical | `None` |
| OTHER | Copilot | True | True | critical | `None` |
| OTHER | Copilot Chat on dotcom | True | True | high | `None` |
| OTHER | Copilot Coding Agent | True | True | critical | `None` |
| OTHER | Copilot Spaces | True | True | critical | `None` |
| OTHER | Copilot for Business | True | True | critical | `None` |
| OTHER | Dependabot | True | True | critical | `None` |
| DOWNLOADABLE_EXECUTABLES | GitHub CLI | True | True | high | `None` |
| OTHER | GitHub CSP | True | True | high | `None` |
| DOWNLOADABLE_EXECUTABLES | GitHub Desktop | True | True | critical | `None` |
| OTHER | GitHub Enterprise Cloud | True | True | critical | `None` |
| OTHER | GitHub Enterprise Cloud with Data Residency (GHEC-DR) | True | True | critical | `None` |
| HARDWARE | GitHub Enterprise Server | True | True | critical | `None` |
| OTHER | GitHub Pages | True | True | critical | `None` |
| OTHER | GitHub Production Credentials | True | True | critical | `None` |
| OTHER | GitHub Spark | True | True | critical | `None` |
| OTHER | GitHub for mobile | True | True | critical | `None` |
| URL | api.github.com | True | True | critical | `None` |
| URL | classroom.github.com | True | True | critical | `None` |
| URL | education.github.com | True | True | critical | `None` |
| URL | gist.github.com | True | True | critical | `None` |
| URL | github.com | True | True | critical | `None` |
| DOWNLOADABLE_EXECUTABLES | npm CLI | True | True | high | `None` |
| URL | npmjs.com | True | True | critical | `None` |
| URL | npmjs.org | True | True | critical | `None` |
| URL | https://gist.github.com | True | True | critical | `2017-06-22T23:23:44.719Z` |
| URL | http://GitHub.com/CSP | True | True | critical | `2017-06-22T23:29:38.991Z` |
| DOWNLOADABLE_EXECUTABLES | Atom | True | False | critical | `2017-06-22T23:35:22.423Z` |
| DOWNLOADABLE_EXECUTABLES | Other Applications | True | True | low | `2019-02-19T19:29:54.119Z` |
| URL | semmle.net | True | True | critical | `2022-08-31T18:46:14.564Z` |
| OTHER | LGTM | True | True | critical | `2022-08-31T18:46:24.171Z` |
| URL | semmle.com | True | True | critical | `2022-08-31T18:46:33.704Z` |
| URL | jobs.github.com | True | True | critical | `2022-08-31T18:48:33.138Z` |
| URL | lab.github.com | True | True | critical | `2022-08-31T20:36:05.233Z` |
| OTHER | Copilot | True | True | critical | `2022-09-13T02:27:16.989Z` |
| OTHER | Copilot | True | True | critical | `2022-09-13T02:27:17.018Z` |
| OTHER |  Code Search | True | True | critical | `2022-09-13T02:27:17.065Z` |
| OTHER |  Code Search | True | True | critical | `2022-09-13T02:27:17.089Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.113Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.138Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.160Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.182Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.205Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.230Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.253Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.275Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.298Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.319Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.342Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.362Z` |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.386Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.409Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.433Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.458Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.481Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.504Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.148Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.177Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.202Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.229Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.252Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.278Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.304Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.328Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.351Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.377Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.407Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.436Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.472Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.502Z` |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.531Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.562Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.594Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.621Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.644Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.667Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.692Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.716Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.742Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.769Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.793Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.821Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.844Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.870Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.895Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.919Z` |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.944Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:19.968Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:19.993Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.015Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.036Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.066Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.092Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.115Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.137Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.158Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.180Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.202Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.223Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.244Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.263Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.282Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.303Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.326Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.346Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.368Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.390Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.410Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.430Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.450Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.473Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.494Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.515Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.536Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.556Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.576Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.595Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.615Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.635Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.656Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.677Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.698Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.720Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.740Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.760Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.782Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.802Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.823Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.843Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.864Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.917Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.939Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.960Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.980Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.001Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.021Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.041Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.062Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.085Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.108Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.131Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.151Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.173Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.194Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.214Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.233Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.254Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.274Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.295Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.316Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.339Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.362Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.385Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.408Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.428Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.449Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.470Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.491Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.512Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.533Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.553Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.574Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.595Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.616Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.637Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.658Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.681Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.703Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.724Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.745Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.765Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.787Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.809Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.833Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.856Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.877Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.899Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.919Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.941Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.962Z` |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.983Z` |

**Tài sản phi-tên-miền trong scope** (trích `instruction` từ `structured_scopes`, `eligible_for_bounty=true`):

```text
GitHub Enterprise Cloud | GitHub Pages | GitHub Production Credentials | Dependabot |
GitHub for mobile | Copilot | Copilot for Business |
GitHub Enterprise Cloud with Data Residency (GHEC-DR) | Copilot Spaces |
Copilot Coding Agent | GitHub Spark | GitHub CSP | Copilot Chat on dotcom
```
(`asset_type = OTHER`, `max_severity = critical`, trừ `GitHub CSP` = `high` và `Copilot Chat on dotcom` = `high`.)

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

## 4b. TRÍCH NGUYÊN VĂN — DANH SÁCH **KHÔNG ĐỦ ĐIỀU KIỆN** (ineligible)

Nguồn: <https://bounty.github.com/ineligible.html> (HTTP 200, 113.590 B, fetch `2026-10-01`).
Bản đầy đủ: `agents/bountyrecon/tasks/T3/EVIDENCE/gh_ineligible.txt` (517 dòng).
Đây là phần **bắt buộc** của xác lập scope: tính năng "hoạt động đúng thiết kế" thì không có thưởng.

Nhóm **All Targets** (áp dụng cho mọi tài sản):

```text
* OAuth client ID and secrets are publicly available in desktop and mobile apps
* Use of known-vulnerable software
* Vulnerability in upstream dependencies
* Clickjacking a static site
* Local Access
* Network Denial of Service
* Cache purging and cache eviction
* Content that stays cached after you delete it or make it private
* Git hooks, filters, and local repository configuration
* Attacks that require following an attacker's instructions
* Typosquatting
* Vulnerabilities identified in Open Source Repositories
* Assets that are not owned by GitHub
* Abuse of a service is not automatically a vulnerability
* Attacks that require intercepting or modifying traffic
```

Trích nguyên văn phần giải thích `Network Denial of Service`:

```text
Network-level and volumetric denial of service attacks (e.g., DDoS, traffic flooding) are not allowed and are ineligible for reward. We have mitigation plans in place for these types of attacks. Application-layer denial of service vulnerabilities (e.g., ReDoS, logic bombs) are eligible. Please see our rules for guidelines on how to research these responsibly.
```

Trích nguyên văn phần `Assets that are not owned by GitHub` (nhóm All Targets) và
`Local Access`:

```text
Local Access
Vulnerabilities that require local system access are out of scope and ineligible for bounty across all services.
```

Các nhóm theo sản phẩm (nguyên văn tiêu đề mục):
`Dependabot`, `GitHub Gist`, `GitHub Actions`, `GitHub API`, `GitHub CLI`, `GitHub Codespaces`,
`GitHub Copilot`, `GitHub Credentials`, `GitHub Desktop`, `GitHub Education`,
`GitHub Enterprise Cloud`, `GitHub Enterprise Server`, `... npm Registry`.

> 📌 **Hệ quả cho T4 — rất quan trọng:**
> * **DoS/DDoS mạng = KHÔNG BAO GIỜ** (ineligible + cấm). Chỉ DoS tầng ứng dụng (ReDoS,
>   logic bomb) mới được thưởng.
> * **Prompt Injection vào Copilot = ineligible** ("Prompt Injections", nhóm GitHub Copilot).
> * **Lỗi trong thư viện upstream = out of scope** — phải báo cho upstream.
> * **Tài sản không thuộc GitHub = ineligible** — khớp với cảnh báo ở §5.

---

## 5. KẾT LUẬN SCOPE (tổng hợp của tôi — KHÔNG phải nguyên văn)

| Hạng mục | Kết luận |
|---|---|
| Trích được nguyên văn in-scope? | ✅ **CÓ** (8 nhóm tên miền + 13 tài sản `OTHER`) |
| Trích được nguyên văn out-of-scope? | ✅ **CÓ** (18 tên miền loại trừ + 14 mục tường minh) |
| Trích được quy định cấm? | ✅ **CÓ** (DDoS, scanner diện rộng, PII, công bố) |
| Trích được danh sách ineligible? | ✅ **CÓ** (517 dòng, xem §4b) |
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
