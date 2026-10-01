# STRUCTURED SCOPE v2 (có `archived_at`) — GitHub (handle `github`)

**Ngày chụp:** `2026-10-01T15:28:34Z` (UTC) · **Nguồn:** `POST https://hackerone.com/graphql` (công khai, không auth)
**Quan hệ với bản gốc:** đây là **BẢN CHỤP LẠI** theo `D-026` phương án (a).
Bản gốc `scope_github.md` **KHÔNG bị sửa, KHÔNG bị xoá** — vẫn là bằng chứng pháp lý cho thời điểm chụp gốc `2026-10-01`.

> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** cột `archived_at` cho biết bản ghi **đã nghỉ hưu hay chưa**. **KHÔNG** được suy ra 'ngoài scope'. Chỉ được khẳng định: bảng thiếu chiều này thì **KHÔNG PHÂN BIỆT ĐƯỢC**.
> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi `archived_at != None` **chưa có định nghĩa chính thức**. Ghi hiện tượng, KHÔNG kết luận ngữ nghĩa.

**Thống kê tự đo:** `archived:false` = **39** scope (sub=True **27**) · `archived:true` = **158** scope (sub=True **156**) · TỔNG **197**

## archived=false (đang hiệu lực) — n=39

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| URL | github.com | True | True | critical | `None` | GitHub.com is our main web site. It is our most intricate application with a number of user inputs and access methods. GitHub.com is built on Ruby on Rails and leverages a number of Open Source technologies.  Rewards range from $555 up to $20,000 and are determined at our discretion based on a number of factors. For example, if you find a reflected XSS that is only possible in Opera, and Opera is  |
| URL | api.github.com | True | True | critical | `None` | The GitHub API is used by thousands of developers and applications to programatically interact with GitHub data and services. Because so much of the GitHub.com functionality is exposed in the API, security has always been a high priority.  Rewards range from $555 up to $20,000 and are determined at our discretion based on a number of factors.  You can find the app at [https://api.github.com](https |
| URL | gist.github.com | True | True | critical | `None` | Gist is one of the first products launched by GitHub after GitHub.com. It is a service for sharing snippets of code or other text content. Gist is built on Ruby on Rails and leverages a number of Open Source technologies.  Rewards range from $555 up to $20,000 and are determined at our discretion based on a number of factors. For example, if you find a reflected XSS that is only possible in Opera, |
| URL | classroom.github.com | True | True | critical | `None` |    |
| URL | *.githubapp.com | True | True | critical | `None` | Subdomains under `*.githubapp.com` provide a number of internal services to GitHub employees. Not all subdomains are [in-scope](https://bounty.github.com/#scope)  |
| URL | *.github.net | True | True | critical | `None` | Subdomains under `*.github.net` run services for our internal production network. Many of these services are not accessible from outside our internal network. Not all subdomains are [in-scope](https://bounty.github.com/#scope) |
| URL | education.github.com | True | True | critical | `None` | GitHub Education offers a variety of tools to help educators and researchers work more effectively inside and outside of the classroom. More details are available at https://education.github.com/. GitHub Classroom is [open-source](https://github.com/education/classroom) |
| URL | *.githubusercontent.com | True | True | critical | `None` |  |
| URL | npmjs.com | True | True | critical | `None` | This is the domain for npm’s public-facing websites. All subdomains under npmjs.com are in scope. |
| URL | npmjs.org | True | True | critical | `None` | This is the domain for npm’s registry, public-facing databases, and APIs. All subdomains under npmjs.org are in scope. |
| OTHER | GitHub Enterprise Cloud | True | True | critical | `None` | GitHub Enterprise Cloud is the cloud-hosted version of GitHub Enterprise. It is designed for teams who want advanced authentication and permissions without managing infrastructure. More information about GitHub Enterprise Cloud is available at https://github.com/enterprise   |
| OTHER | GitHub Pages | True | True | critical | `None` | GitHub Pages is our static site hosting service designed to host your personal, organization, or project pages directly from a GitHub repository. It uses the Jekyll static site generator and officially supported themes are are developed in the pages-themes organization. GitHub Pages support custom domains and can be secured with HTTPS. Eligible submissions include: - Executing arbitrary code durin |
| OTHER | GitHub Production Credentials | True | True | critical | `None` | GitHub, Inc. uses a mix of our own physical infrastructure, cloud platforms and third-party services to keep everything running smoothly. Keeping credentials and access tokens secure for these resources is paramount to the security of our employees and users.  * Credentials allowing access to cloud services, package managers and other resources used by GitHub, Inc employees * Credentials accidenta |
| OTHER | Dependabot | True | True | critical | `None` | Dependabot powers GitHub's [automated security fixes](https://help.github.com/en/articles/configuring-automated-security-fixes). This feature allows GitHub users to automatically update vulnerable dependencies. The core logic of Dependabot is [open-source](https://github.com/dependabot/dependabot-core) and an [overview of the architecture](https://github.com/dependabot/dependabot-core#architecture |
| OTHER | GitHub for mobile | True | True | critical | `None` | Bring GitHub collaboration tools to your small screens with [GitHub for mobile](https://github.com/mobile). |
| OTHER | Copilot | True | True | critical | `None` |  |
| OTHER | Copilot for Business | True | True | critical | `None` |  |
| OTHER | GitHub Enterprise Cloud with Data Residency (GHEC-DR) | True | True | critical | `None` |  |
| OTHER | Copilot Spaces | True | True | critical | `None` |  |
| OTHER | Copilot Coding Agent | True | True | critical | `None` |  |
| OTHER | GitHub Spark | True | True | critical | `None` |  |
| OTHER | GitHub CSP | True | True | high | `None` | While content-injection vulnerabilities are already in-scope for our [GitHub.com bounty](https://bounty.github.com/targets/github.html), we also accept bounty reports for novel [CSP](https://developers.google.com/web/fundamentals/security/csp/) bypasses affecting GitHub.com, even if they do not include a content-injection vulnerability. Using an intercepting proxy or your browser's developer tools |
| OTHER | Copilot Chat on dotcom | True | True | high | `None` |  |
| HARDWARE | GitHub Enterprise Server | True | True | critical | `None` | GitHub Enterprise Server is the on-premise version of GitHub Enterprise. GitHub Enterprise Server shares a code-base with GitHub.com, is built on Ruby on Rails and leverages a number of open source technologies. GitHub Enterprise Server adds a number of features for enterprise infrastructures, including additional authentication backends and clustering options.   Below is a subset of features uniq |
| DOWNLOADABLE_EXECUTABLES | GitHub Desktop | True | True | critical | `None` | [GitHub Desktop](https://desktop.github.com) is an open-source [Electron](https://electronjs.org)-based app for working with your GitHub.com or GitHub Enterprise account. Only the following vulnerabilities are eligible for reward:   * Remote code execution via protocol handlers such as `x-github-client://`   * Code execution without user interaction when cloning or fetching malicious repositories  |
| DOWNLOADABLE_EXECUTABLES | GitHub CLI | True | True | high | `None` | [GitHub CLI](https://cli.github.com) is an open source command line tool for working with your GitHub.com account. It is built with Golang, and performs several GitHub.com commands from your terminal, such as viewing, commenting and performing other actions on issues and PRs. |
| DOWNLOADABLE_EXECUTABLES | npm CLI | True | True | high | `None` |  |
| URL | enterprise.github.com | False | False | none | `None` | `enterprise.github.com` is commonly confused with the [GitHub Enterprise Server product](https://github.com/enterprise) which is an on-premise instance of GitHub.  |
| URL | *.github.io | False | False | none | `None` | Individual sites which are hosted on GitHub Pages are out-of-scope.  |
| URL | git.io | False | False | none | `None` | The [git.io](https://git.io) URL shortener is out-of-scope. |
| URL | spectrum.chat | False | False | none | `None` | [Spectrum](https://spectrum.chat) is currently out-of-scope. |
| URL | github.blog | False | False | none | `None` | [github.blog](https://github.blog) is out-of-scope. |
| URL | http://education.github.com/forum | False | False | none | `None` | The [GitHub Education Community forum](https://education.github.com/forum) is not in-scope and ineligible for rewards. |
| URL | blog.github.com | False | False | none | `None` | The GitHub Blog is not in-scope and ineligible for rewards.   |
| URL | community.github.com | False | False | none | `None` | The GitHub Community forum is not in-scope and ineligible for rewards. |
| URL | shop.github.com | False | False | none | `None` | The GitHub Shop is not in-scope and ineligible for rewards. |
| DOWNLOADABLE_EXECUTABLES | Atom | False | False | none | `None` | [https://atom.io](https://atom.io "https://atom.io")  |
| DOWNLOADABLE_EXECUTABLES | Electron | False | False | none | `None` | Electron vulnerabilities which do not directly affect GitHub Desktop are out-of-scope and should be [reported](https://electronjs.org/community) to the Electron developers.   |
| DOWNLOADABLE_EXECUTABLES | GitHub Classroom Assistant  | False | False | none | `None` | The [GitHub Classroom Assistant application](https://classroom.github.com/assistant) is currently out-of-scope. |

## archived=true (đã nghỉ hưu) — n=158

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.983Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.962Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.941Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.919Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.899Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.877Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.856Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.833Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.809Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.787Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.765Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.745Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.724Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.703Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.681Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.658Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.637Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.616Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.595Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.574Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.553Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.533Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.512Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.491Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.470Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.449Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.428Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.408Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.385Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.362Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.339Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.316Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.295Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.274Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.254Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.233Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.214Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.194Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.173Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.151Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.131Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.108Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.085Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.062Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.041Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.021Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:21.001Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.980Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.960Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.939Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.917Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.864Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.843Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.823Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.802Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.782Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.760Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.740Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.720Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.698Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.677Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.656Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.635Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.615Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.595Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.576Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.556Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.536Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.515Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.494Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.473Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.450Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.430Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.410Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.390Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.368Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.346Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.326Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.303Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.282Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.263Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.244Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.223Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.202Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.180Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.158Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.137Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.115Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.092Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.066Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.036Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:20.015Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:19.993Z` |  |
| OTHER | All Other Scope | True | True | critical | `2022-09-13T02:27:19.968Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.944Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.919Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.895Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.870Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.844Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.821Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.793Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.769Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.742Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.716Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.692Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.667Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.644Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.621Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.594Z` |  |
| OTHER | GHES | True | True | critical | `2022-09-13T02:27:19.562Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.531Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.502Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.472Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.436Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.407Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.377Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.351Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.328Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.304Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.278Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.252Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.229Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.202Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.177Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:19.148Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.504Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.481Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.458Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.433Z` |  |
| OTHER | Codespaces | True | True | critical | `2022-09-13T02:27:17.409Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.386Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.362Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.342Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.319Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.298Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.275Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.253Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.230Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.205Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.182Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.160Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.138Z` |  |
| OTHER | GitHub Enterprise Importer | True | True | critical | `2022-09-13T02:27:17.113Z` |  |
| OTHER |  Code Search | True | True | critical | `2022-09-13T02:27:17.089Z` |  |
| OTHER |  Code Search | True | True | critical | `2022-09-13T02:27:17.065Z` |  |
| OTHER | Copilot | True | True | critical | `2022-09-13T02:27:17.018Z` |  |
| OTHER | Copilot | True | True | critical | `2022-09-13T02:27:16.989Z` |  |
| URL | lab.github.com | True | True | critical | `2022-08-31T20:36:05.233Z` | Get the skills you need without leaving GitHub. GitHub Learning Lab takes you through a series of fun and practical projects, sharing helpful feedback along the way. |
| URL | jobs.github.com | True | True | critical | `2022-08-31T18:48:33.138Z` | [GitHub Jobs](https://jobs.github.com/) is a great place to attract the best technical talent for your company’s open software development positions |
| URL | semmle.com | True | True | critical | `2022-08-31T18:46:33.704Z` | Our main domain for Semmle and LGTM services. All subdomains under semmle.com are in-scope **except**: * dev.semmle.com * git.semmle.com * jira.semmle.com * wiki.semmle.com |
| OTHER | LGTM | True | True | critical | `2022-08-31T18:46:24.171Z` | LGTM is a code analysis platform for development teams to identify vulnerabilities early and prevent them from reaching production. It uses [CodeQL](https://semmle.com/ql)  which works by retrieving source code from version control systems, building it with custom tooling, and creating analysis results.  LGTM uses Docker containers to isolate the build and analysis environment from the rest of the |
| URL | semmle.net | True | True | critical | `2022-08-31T18:46:14.564Z` | Our domain for non-production Semmle services. All subdomains under `semmle.net` are in-scope.  |
| OTHER | GitHub Education Community forum | False | False | none | `2019-02-27T19:33:48.767Z` | The [GitHub Education Community forum](https://education.github.com/forum) is not in-scope and ineligible for rewards. |
| DOWNLOADABLE_EXECUTABLES | Other Applications | True | True | low | `2019-02-19T19:29:54.119Z` | GitHub builds and operates a number of web properties and applications. Not all of them are currently part of an open bounty, however, we still appreciate the effort researchers put forth to identify vulnerabilities. Vulnerabilities found in applications not specifically listed on the [Open bounties](https://bounty.github.com/index.html#open-bounties) are not currently eligible for cash rewards.   |
| URL | speakerdeck.com | False | False | none | `2018-06-13T18:29:52.871Z` |  |
| DOWNLOADABLE_EXECUTABLES | Atom | True | False | critical | `2017-06-22T23:35:22.423Z` |  |
| URL | http://GitHub.com/CSP | True | True | critical | `2017-06-22T23:29:38.991Z` | While content-injection vulnerabilities are already in-scope for our [GitHub.com bounty](https://bounty.github.com/targets/github.html), we also accept bounty reports for novel [CSP](https://developers.google.com/web/fundamentals/security/csp/) bypasses affecting GitHub.com, even if they do not include a content-injection vulnerability. Using an intercepting proxy or your browser's developer tools |
| URL | https://gist.github.com | True | True | critical | `2017-06-22T23:23:44.719Z` |  |

