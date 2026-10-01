# STRUCTURED SCOPE — GitHub (handle: github)
offers_bounties=True submission_state=open

## IN SCOPE / eligible_for_submission=true  (n=183)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| URL | github.com | True | critical | GitHub.com is our main web site. It is our most intricate application with a number of user inputs and access methods. GitHub.com is built on Ruby on Rails and leverages a number of Open Source technologies.  Rewards range from $555 up to $20,000 and are determined at our discretion based on a number of factors. For example, if you find a reflected XSS that is only possible in Opera, and Opera is \<2% of our traffic, then the severity and reward will be lower. But a persistent XSS that works in Chrome, at \>60% of our traffic, will earn a much larger reward.  You can find the app at [https://github.com](https://github.com "https://github.com").   |
| URL | api.github.com | True | critical | The GitHub API is used by thousands of developers and applications to programatically interact with GitHub data and services. Because so much of the GitHub.com functionality is exposed in the API, security has always been a high priority.  Rewards range from $555 up to $20,000 and are determined at our discretion based on a number of factors.  You can find the app at [https://api.github.com](https://api.github.com "https://api.github.com") and can find the API documentation at [https://developer.github.com](https://developer.github.com "https://developer.github.com").   |
| URL | gist.github.com | True | critical | Gist is one of the first products launched by GitHub after GitHub.com. It is a service for sharing snippets of code or other text content. Gist is built on Ruby on Rails and leverages a number of Open Source technologies.  Rewards range from $555 up to $20,000 and are determined at our discretion based on a number of factors. For example, if you find a reflected XSS that is only possible in Opera, and Opera is \<2% of our traffic, then the severity and reward will be lower. But a persistent XSS that works in Chrome, at \>60% of our traffic, will earn a much larger reward.  You can find the app at [https://gist.github.com](https://gist.github.com "https://gist.github.com").   |
| URL | classroom.github.com | True | critical |    |
| URL | *.githubapp.com | True | critical | Subdomains under `*.githubapp.com` provide a number of internal services to GitHub employees. Not all subdomains are [in-scope](https://bounty.github.com/#scope)  |
| URL | *.github.net | True | critical | Subdomains under `*.github.net` run services for our internal production network. Many of these services are not accessible from outside our internal network. Not all subdomains are [in-scope](https://bounty.github.com/#scope) |
| URL | education.github.com | True | critical | GitHub Education offers a variety of tools to help educators and researchers work more effectively inside and outside of the classroom. More details are available at https://education.github.com/. GitHub Classroom is [open-source](https://github.com/education/classroom) |
| URL | *.githubusercontent.com | True | critical |  |
| URL | npmjs.com | True | critical | This is the domain for npm’s public-facing websites. All subdomains under npmjs.com are in scope. |
| URL | npmjs.org | True | critical | This is the domain for npm’s registry, public-facing databases, and APIs. All subdomains under npmjs.org are in scope. |
| OTHER | GitHub Enterprise Cloud | True | critical | GitHub Enterprise Cloud is the cloud-hosted version of GitHub Enterprise. It is designed for teams who want advanced authentication and permissions without managing infrastructure. More information about GitHub Enterprise Cloud is available at https://github.com/enterprise   |
| OTHER | GitHub Pages | True | critical | GitHub Pages is our static site hosting service designed to host your personal, organization, or project pages directly from a GitHub repository. It uses the Jekyll static site generator and officially supported themes are are developed in the pages-themes organization. GitHub Pages support custom domains and can be secured with HTTPS. Eligible submissions include: - Executing arbitrary code during the build process, either via a custom Jekyll theme or vulnerabilities in the command-line Git tools when cloning or checking-out repositories from user accounts that do not have actions workflow permissions. - Reading arbitrary files during the build process which discloses sensitive information, for example by misusing path traversal or symbolic links in a custom Jekyll theme from user accounts that do not have permissions to view those resources.  Individual GitHub Pages sites hosted under *.github.io are out-of-scope. |
| OTHER | GitHub Production Credentials | True | critical | GitHub, Inc. uses a mix of our own physical infrastructure, cloud platforms and third-party services to keep everything running smoothly. Keeping credentials and access tokens secure for these resources is paramount to the security of our employees and users.  * Credentials allowing access to cloud services, package managers and other resources used by GitHub, Inc employees * Credentials accidentally made public in repositories which allow access to GitHub, Inc resources. This does *not* include credentials exposed by our users and credentials which do not allow access to GitHub, Inc resources. * Credentials exposed by third-party services which allow access to GitHub, Inc resources  Please review our [guidance for handling PII](https://bounty.github.com/#handling_personally_identifiable_information_pii) before investigating credentials allowing access to GitHub, Inc resources. The reward amount is based on the impact of the leaked credential which will be determined by the GitHub Security team. |
| OTHER | Dependabot | True | critical | Dependabot powers GitHub's [automated security fixes](https://help.github.com/en/articles/configuring-automated-security-fixes). This feature allows GitHub users to automatically update vulnerable dependencies. The core logic of Dependabot is [open-source](https://github.com/dependabot/dependabot-core) and an [overview of the architecture](https://github.com/dependabot/dependabot-core#architecture) is available.    * Execution environment breakout attacks, providing access to private networked resources or other users' data   * Security issues in [`dependabot-core`](https://github.com/dependabot/dependabot-core) |
| OTHER | GitHub for mobile | True | critical | Bring GitHub collaboration tools to your small screens with [GitHub for mobile](https://github.com/mobile). |
| OTHER | Copilot | True | critical |  |
| OTHER | Copilot for Business | True | critical |  |
| OTHER | GitHub Enterprise Cloud with Data Residency (GHEC-DR) | True | critical |  |
| OTHER | Copilot Spaces | True | critical |  |
| OTHER | Copilot Coding Agent | True | critical |  |
| OTHER | GitHub Spark | True | critical |  |
| OTHER | GitHub CSP | True | high | While content-injection vulnerabilities are already in-scope for our [GitHub.com bounty](https://bounty.github.com/targets/github.html), we also accept bounty reports for novel [CSP](https://developers.google.com/web/fundamentals/security/csp/) bypasses affecting GitHub.com, even if they do not include a content-injection vulnerability. Using an intercepting proxy or your browser's developer tools, experiment with injecting content into the DOM. See if you can execute arbitrary JavaScript or exfiltrate sensitive page contents such as CSRF tokens. Reports of other previously-unknown impacts from content-injection will also be considered.  Previously identified attacks are not eligible for reward (we've put a lot of thought into CSP bypasses already). You can find a discussion of known attacks and our attempts to mitigate them [here](http://githubengineering.com/githubs-csp-journey/). Attacks against CSP features not used on GitHub.com, such as script nonces, are not eligible for reward. Vulnerabilities resulting from injection in implausible locations, such as within an element that doesn't contain user-content, are not eligible for reward. Rewards are determined at our discretion: if you think you've found something cool and novel, report it!   |
| OTHER | Copilot Chat on dotcom | True | high |  |
| HARDWARE | GitHub Enterprise Server | True | critical | GitHub Enterprise Server is the on-premise version of GitHub Enterprise. GitHub Enterprise Server shares a code-base with GitHub.com, is built on Ruby on Rails and leverages a number of open source technologies. GitHub Enterprise Server adds a number of features for enterprise infrastructures, including additional authentication backends and clustering options.   Below is a subset of features unique to GitHub Enterprise that might be interesting to investigate.    * Bypassing instance-wide authentication, also known as [*private mode*](https://help.github.com/enterprise/admin/guides/installation/enabling-private-mode/)   * External authentication backends including [CAS, LDAP, and SAML](https://help.github.com/enterprise/admin/guides/user-management/)   * In-app administration of the instance using a site administrator control panel   * [User, organization, and repository migration](https://help.github.com/enterprise/admin/guides/migrations/)   * [Web-based management console](https://help.github.com/enterprise/admin/guides/installation/web-based-management-console/) and [SSH access](https://help.github.com/enterprise/admin/guides/installation/administrative-shell-ssh-access/) to configure and update the instance   * [Pre-receive hook scripts](https://help.github.com/enterprise/admin/guides/developer-workflow/creating-a-pre-receive-hook-script/)   * [GitHub Connect](https://help.github.com/enterprise/admin/guides/developer-workflow/connecting-github-enterprise-server-to-github-com/) allows users to share specific features and workflows between your GitHub Enterprise Server instance and a GitHub.com organization on GitHub Enterprise Cloud.   * See [our documentation](https://help.github.com/enterprise/admin/guides/installation/network-ports-to-open/) for a list of services typically open on an instance.  You can request a trial of GitHub Enterprise Server for security testing at [https://enterprise.github.com/bounty](https://enterprise.github.com/bounty). |
| DOWNLOADABLE_EXECUTABLES | GitHub Desktop | True | critical | [GitHub Desktop](https://desktop.github.com) is an open-source [Electron](https://electronjs.org)-based app for working with your GitHub.com or GitHub Enterprise account. Only the following vulnerabilities are eligible for reward:   * Remote code execution via protocol handlers such as `x-github-client://`   * Code execution without user interaction when cloning or fetching malicious repositories   |
| DOWNLOADABLE_EXECUTABLES | GitHub CLI | True | high | [GitHub CLI](https://cli.github.com) is an open source command line tool for working with your GitHub.com account. It is built with Golang, and performs several GitHub.com commands from your terminal, such as viewing, commenting and performing other actions on issues and PRs. |
| DOWNLOADABLE_EXECUTABLES | npm CLI | True | high |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | All Other Scope | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | GHES | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | Codespaces | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER | GitHub Enterprise Importer | True | critical |  |
| OTHER |  Code Search | True | critical |  |
| OTHER |  Code Search | True | critical |  |
| OTHER | Copilot | True | critical |  |
| OTHER | Copilot | True | critical |  |
| URL | lab.github.com | True | critical | Get the skills you need without leaving GitHub. GitHub Learning Lab takes you through a series of fun and practical projects, sharing helpful feedback along the way. |
| URL | jobs.github.com | True | critical | [GitHub Jobs](https://jobs.github.com/) is a great place to attract the best technical talent for your company’s open software development positions |
| URL | semmle.com | True | critical | Our main domain for Semmle and LGTM services. All subdomains under semmle.com are in-scope **except**: * dev.semmle.com * git.semmle.com * jira.semmle.com * wiki.semmle.com |
| OTHER | LGTM | True | critical | LGTM is a code analysis platform for development teams to identify vulnerabilities early and prevent them from reaching production. It uses [CodeQL](https://semmle.com/ql)  which works by retrieving source code from version control systems, building it with custom tooling, and creating analysis results.  LGTM uses Docker containers to isolate the build and analysis environment from the rest of the infrastructure. By nature this environment permits arbitrary code execution by any registered user, so the quality of isolation is a critical part of the security model. The public site includes two user types (user and admin user) as well as anonymous access.  * [`lgtm-com.pentesting.semmle.net`](lgtm-com.pentesting.semmle.net) is a dedicated instance of LGTM for your research.  * [`backend-dot-lgtm-penetration-testing.appspot.com`](backend-dot-lgtm-penetration-testing.appspot.com) is used for triggering automated tasks from other parts of the LGTM system. It does not provide a user interface.  * [`downloads.lgtm.com`](downloads.lgtm.com) |
| URL | semmle.net | True | critical | Our domain for non-production Semmle services. All subdomains under `semmle.net` are in-scope.  |
| DOWNLOADABLE_EXECUTABLES | Other Applications | True | low | GitHub builds and operates a number of web properties and applications. Not all of them are currently part of an open bounty, however, we still appreciate the effort researchers put forth to identify vulnerabilities. Vulnerabilities found in applications not specifically listed on the [Open bounties](https://bounty.github.com/index.html#open-bounties) are not currently eligible for cash rewards.   |
| DOWNLOADABLE_EXECUTABLES | Atom | False | critical |  |
| URL | http://GitHub.com/CSP | True | critical | While content-injection vulnerabilities are already in-scope for our [GitHub.com bounty](https://bounty.github.com/targets/github.html), we also accept bounty reports for novel [CSP](https://developers.google.com/web/fundamentals/security/csp/) bypasses affecting GitHub.com, even if they do not include a content-injection vulnerability. Using an intercepting proxy or your browser's developer tools, experiment with injecting content into the DOM. See if you can execute arbitrary JavaScript or exfiltrate sensitive page contents such as CSRF tokens. Reports of other previously-unknown impacts from content-injection will also be considered.  Previously identified attacks are not eligible for reward (we've put a lot of thought into CSP bypasses already). You can find a discussion of known attacks and our attempts to mitigate them [here](http://githubengineering.com/githubs-csp-journey/). Attacks against CSP features not used on GitHub.com, such as script nonces, are not eligible for reward. Vulnerabilities resulting from injection in implausible locations, such as within an element that doesn't contain user-content, are not eligible for reward. Rewards are determined at our discretion: if you think you've found something cool and novel, report it!   |
| URL | https://gist.github.com | True | critical |  |

## OUT OF SCOPE / eligible_for_submission=false  (n=14)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| URL | enterprise.github.com | False | none | `enterprise.github.com` is commonly confused with the [GitHub Enterprise Server product](https://github.com/enterprise) which is an on-premise instance of GitHub.  |
| URL | *.github.io | False | none | Individual sites which are hosted on GitHub Pages are out-of-scope.  |
| URL | git.io | False | none | The [git.io](https://git.io) URL shortener is out-of-scope. |
| URL | spectrum.chat | False | none | [Spectrum](https://spectrum.chat) is currently out-of-scope. |
| URL | github.blog | False | none | [github.blog](https://github.blog) is out-of-scope. |
| URL | http://education.github.com/forum | False | none | The [GitHub Education Community forum](https://education.github.com/forum) is not in-scope and ineligible for rewards. |
| URL | blog.github.com | False | none | The GitHub Blog is not in-scope and ineligible for rewards.   |
| URL | community.github.com | False | none | The GitHub Community forum is not in-scope and ineligible for rewards. |
| URL | shop.github.com | False | none | The GitHub Shop is not in-scope and ineligible for rewards. |
| DOWNLOADABLE_EXECUTABLES | Atom | False | none | [https://atom.io](https://atom.io "https://atom.io")  |
| DOWNLOADABLE_EXECUTABLES | Electron | False | none | Electron vulnerabilities which do not directly affect GitHub Desktop are out-of-scope and should be [reported](https://electronjs.org/community) to the Electron developers.   |
| DOWNLOADABLE_EXECUTABLES | GitHub Classroom Assistant  | False | none | The [GitHub Classroom Assistant application](https://classroom.github.com/assistant) is currently out-of-scope. |
| OTHER | GitHub Education Community forum | False | none | The [GitHub Education Community forum](https://education.github.com/forum) is not in-scope and ineligible for rewards. |
| URL | speakerdeck.com | False | none |  |
