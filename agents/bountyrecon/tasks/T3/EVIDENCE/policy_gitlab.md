# Rewards
We have different rewards depending on the business impact of each asset. A more complete description of each asset will be in the scope section, but in general GitLab.com and all our products' source code is rewarded the highest, then non-production environments have reduced bounties and our static websites have the lowest payouts.

See the Rewards section above for our bounty ranges. For reports with critical or high severity we pay $1000 at the time the report is triaged, and for medium severity reports we pay $500. The remainder, if any, will be paid as soon as the severity has been fully analyzed internally. The calculator we use to calculate CVSS-based bounty amounts is [accessible to everyone](https://gitlab-com.gitlab.io/gl-security/appsec/cvss-calculator/).

Reports about intended behavior resulting in an update of our documentation will be rewarded with a $100 bounty, as long as this update is security related.

GitLab assigns CVE identifiers to vulnerabilities affecting GitLab products. While the CVSS score for those should generally align with the severity set in the HackerOne report, sometimes they will differ depending on our assessment of the business impact based on existing mitigations, the sensitivity of the impacted data, and number of impacted customers among other factors.

While we try to be as consistent as possible with rewards, our program is also evolving and rewards may change accordingly to how our program evolves with time.

For valid reports for which the author can't accept monetary rewards, we offer to plant trees in our [GitLab forest](https://tree-nation.com/trees/view/5119567) on their behalf. 

## GitLab Ultimate License

Reporters which have submitted three or more valid findings to our program are eligible to receive a one year self-hosted Ultimate license supporting up to five users. If you believe you're eligible, please request the Ultimate license via a comment in one of your reports mentioning the assigned security engineer, and include links to your other two valid reports. Once verified, the license will be sent to your `[username]@wearehackerone.com` email address. Any further valid submissions in that year will extend you the next year's license for free too.

## How severity is determined

Upon receipt of the finding, we will conduct an internal investigation to understand the full impact of the vulnerability. We then assess the severity using the Common Vulnerability Scoring System (CVSS) and score according to the guidelines you can see in the "help & definitions" section of our [CVSS calculator](https://gitlab-com.gitlab.io/gl-security/appsec/cvss-calculator/). Note that even if GitLab.com allows self-registration, most GitLab instances in the wild don't -- which makes vulnerabilities that are exploitable without authentication a lot more impactful. For this reason, any vulnerability that requires an account will not be scored with "Privilege Required: None".

Reports for security issues that aren't vulnerabilities in our systems and where CVSS isn't appropriate (for example a leaked confidential document) will receive a discretionary bounty based on our assessment of the impact of the finding.

We collaborate with HackerOne Triage Service for quickly identifying valid and impactful reports. By-passing the HackerOne triage service by opening issues in GitLab project or reaching out to GitLab team members directly on reports or via other mediums is a violation of [HackerOne Code of Conduct (CoC)](https://www.hackerone.com/policies/code-of-conduct) and might attract CoC enforcement actions.

CVSS scores and bounty awards are determined by the consensus of the GitLab Bug Bounty Council. Multiple team members review and validate the CVSS for each triaged report to ensure accurate and impartial assessments. Reporters can raise concerns if they believe a CVSS metric has been misjudged. However, the final decision on CVSS scoring and bounty awards rests with the council.

## Duplicates

For different attack vectors that result in the same mitigation, GitLab reserves the right to reward the first report that is validated for that fix. All subsequent reports that are addressed by that mitigation will be considered as duplicates, regardless of the attack vector.

# Rules of Engagement, Testing, and Proof-of-concepts

When researching security issues, especially those which may compromise the privacy of others, you must use only test accounts in order to respect our users’ privacy. Accessing private information of other users, performing actions that may negatively affect GitLab’s users (e.g., spam, denial of service) will disqualify the report. Activity that is disruptive to GitLab operations will result in account bans and disqualification of the report. Examples of disruptive activity include, but are not limited to:
 - Generating abuse requests
 - Submission of support, sales or other requests to 3rd party systems
 - Mass creation of users, groups, and projects
 - Typosquatting or other namesquatting
 - Spam-like or other high volume activity

Sending reports from automated tools without verifying them will immediately disqualify the report.

Disruptive activity such as that listed above can be researched freely on your own installation of `gitlab`. GitLab is an open-core company, with the source code powering GitLab.com available in the [main GitLab Project](https://gitlab.com/gitlab-org/gitlab). You are encouraged to [install](https://about.gitlab.com/install/) your own standalone instance for researching vulnerabilities. 

Due to an increase in low-quality AI-generated submissions, all reports must include one of the following reproduction artifacts: screen captures, videos, and logs showing vulnerabilities against your own GitLab installation. Reports without sufficient and verifiable evidence will be closed as N/A without further investigation and will not be considered as the original submission when it comes to duplication handling.

**We strongly encourage security testing on your local [GitLab Development Kit (GDK)](https://gitlab.com/gitlab-org/gitlab-development-kit) instance** rather than GitLab.com for most vulnerability research. The GDK provides:
- Access to the latest development features before public release
- No rate limits or testing restrictions on your local instance
- Safe environment for testing most vulnerability types
- [GDK Security Testing Guide - link to create]

**For Denial of Service (DoS) vulnerabilities specifically:** 
Testing and demonstrating DoS impact on a local GDK instance can be problematic. If you need to demonstrate DoS impact, we recommend testing on a self-managed GitLab instance with specifications and resources equal to or greater than the [self-managed GitLab installation requirements](https://docs.gitlab.com/install/requirements/).
**Never test DoS vulnerabilities on GitLab.com.**

For vulnerabilities requiring GitLab.com production architecture, you must use test accounts created with your HackerOne email alias (yourhandle@wearehackerone.com). **Never test against projects, groups, accounts, or instances you do not own.**

**Behave professionally**. Failure to follow HackerOne's policies, such as the [Code of Conduct](https://www.hackerone.com/policies/code-of-conduct), may result in the report being ineligible for a bounty at GitLab's sole discretion, in addition to any enforcement action HackerOne may decide to take.

## Demonstrating Impact

- Always choose a non disruptive option to demonstrate the impact. If the only way to demonstrate an impact is a disruptive one then stop and report the issue, we will validate the impact.
- In the case of reports related to credential leaks do not create additional access credentials using the leaked one. We will determine impact ourselves and award for the maximum impact we uncover.
- In the case of reports related to Subdomain Takeovers, PoC's should create a simple page with your HackerOne handle as a single line of text at the affected URL. The page should utilize a UUID or complex string that wouldn't ordinarily be accessed. An example would be `vulnerable-subdomain.example.com/$UUID-poc.txt` where $UUID is a hard-to-guess value.
- For sharing POC videos, directly upload the video in the report. Do not upload POC videos in public platforms until the report is disclosed.  Please refer to our disclosure policy for more details.

## Testing on GitLab.com
**When testing on GitLab.com, your `@wearehackerone.com` address must be associated with the testing account.** If separate accounts are necessary, [you can use an alias](https://docs.hackerone.com/hackers/hacker-email-alias.html#multiple-aliases). This will help us separate testing from other forms of abuse, and help inform the decision of blocking an account. Note that this does not provide immunity and the Rules of engagement must be followed at all times.

Please keep note of any IP addresses you use during your research, as this can help us when investigating and remediating vulnerabilities.

Please don't request Developer access to our projects, including the GitLab Community Forks group. While it can indeed be a security risk for the company that a random person joins those projects, it is something the security team handles and we don't want bug bounty hunters to test those workflows as it creates unnecessary noise for our teams.

# SLA

GitLab will make a best effort to meet the following SLAs for hackers participating in our program:

* Time to first response (from report submit) - 1 business day
* Time to triage (from report submit) - 5 business days
* Time to bounty (from triage) - between 5 and 45 business days

The only appropriate place to inquire about a HackerOne report's status is on the report itself. Please refrain from submitting your report or inquiring about its status through additional channels including any other unrelated HackerOne report, as this unnecessarily binds resources in the security team.

# Scope

All GitLab Inc. products are in scope unless explicitly noted otherwise.
 
Testing on subdomains that are neither explicitly in scope nor out of scope isn't encouraged, but if you can find a vulnerability with business impact on such a subdomain please report it. We normally close sufficiently clear reports as `Informative` so there will be [no negative effect](https://www.hackerone.com/blog/reputation-signal-impact-enhancements-whats-changing-and-why-it-matters) on your reputation score if we decide that it's out of scope. However, remember that GitLab subdomains that are running third party services are strictly out of scope.

## GitLab Releases

We release new features every month. You can [learn more about our release process](https://about.gitlab.com/releases/), see the latest [monthly release blog post](https://about.gitlab.com/releases/categories/releases/) and see what's coming in [future releases](https://about.gitlab.com/upcoming-releases/). If you're bug hunting, might we suggest a newly released feature? 😉

## Vulnerabilities in 3rd-party dependencies & packaged software

Reports on vulnerabilities in third-party software which GitLab depends on will be accepted and a bounty rewarded if and only if:

* The report includes a new vulnerability, for which a patch is not available, or
* A patch has been available for more than 30 days.
* It has a clear and working proof of concept that illustrates the impact to GitLab.
* It has Critical or High impact to GitLab.

This does _not_ include websites of third party software and services and only includes dependencies & packaged software.

### AI related vulnerabilities
We only accept prompt injection related vulnerability reports where there is demonstrable impact beyond its current security boundary. GitLab continues to develop security protections for Duo and agentic systems which can be referred to [here](https://docs.gitlab.com/user/duo_agent_platform/security_threats/). Stay tuned for further iterations to the Bug Bounty program around AI related vulnerabilites in the near future.

Below is a running table of known prompt injection vulnerabilities that are **out of scope** for the GitLab bug bounty program. Do not submit reports for these specific known instances.

| Vulnerability  | Link |
|---|---|
| Duo Agentic Chat prompt injection vulnerability  | [#581264](https://gitlab.com/gitlab-org/gitlab/-/work_items/581264) |
| Filename Injection in TRUSTED_INTERNAL Tools  | [#587934](https://gitlab.com/gitlab-org/gitlab/-/work_items/587934) |
| Invisible Prompt Injection in Issues/MRs  | [#586481](https://gitlab.com/gitlab-org/gitlab/-/work_items/586481) |
| Context Boundary Failure in GitLab Duo Agent Tools  | [#582995](https://gitlab.com/gitlab-org/gitlab/-/work_items/582995) |
| TOCTOU and Prompt Injection in GitLab Duo "Issue to MR" Flow  | [#584107](https://gitlab.com/gitlab-org/gitlab/-/work_items/584107) |
| Hidden Prompt Injection in AI Catalog Agents  | [#579778](https://gitlab.com/gitlab-org/gitlab/-/work_items/579778) |
| MCP Tool Description Injection  | [#552644](https://gitlab.com/gitlab-org/gitlab/-/work_items/552644) |

AI generated or assisted reports that include static code analysis without providing clear proof of exploitability and demonstrating practical security impact will not be accepted.

For AI hallucination reports, such as AI suggesting a package that does not exist, we will not be accepting any such report going forward.

## Out of scope
- Automated scanning reports of any kind
- GitLab sites of third party software and services (marketing services, third-party mail services, developer/support installations etc.)
  - This includes `gitlab.cn` and the JiHu-specific GitLab distribution which are property of  GitLab Information Technology (Hubei) Co., Ltd. (JiHu), security issues in those products should be reported to `security@gitlab.cn`
- User content on GitLab.com (for example, a user that is not using proper permissions on their projects containing sensitive information)
- Access tokens that do not provide access to GitLab company projects/groups/infrastructure or GitLab team member accounts (Please contact the owner of the token (you can find their email address by querying the `/api/v4/user` API). If unable to find the token owner's email address you can disclose leaked tokens by creating a confidential issue assigned to the token owner in the project where the token was leaked)
- Our customers' GitLab installs
- Intentionally public information and hosts, for example our marketing issues at https://gitlab.com/gitlab-com/marketing
- Social engineering, phishing, or other fraud including but not limited to: internationalized domain name (IDN) homograph attacks, Right-to-left (RTL) Ambiguity, RTL Override (RTLO), SPF and DKIM issues, most HTML content injection, Tabnabbing
- HTML or text injection is eligible only when significant impact can be achieved with minimal user interaction
- Missing Security Headers (eg. HSTS, CSP) and Missing Secure Flags on Cookies
- TLS/SSL or SSH issues (weak ciphers/key-size/BEAST/CRIME)
- CSRF without any security impact
- User and project enumeration/path disclosure unless an additional impact can be demonstrated
  - Reports where an attacker can validate a guess will not be accepted. Examples include but are not limited to:
    - An API route returning different status codes depending on if a private path exists or not
    - An identical response but with significantly different timing depending on if a private path exists or not
    - A response validating that a specific email address is registered
  - Reports where an attacker can only disclose the ID of a private element will not be accepted
- Denial of Service (DoS) issues
    - **Note:** Exceptions may be considered for DoS vulnerabilities that both achieve persistent total service disruption AND can be executed through unauthenticated endpoints. The GitLab security team will determine, at our sole discretion, whether a report falls into this exception
    - Volumetric attack (network flooding, request flooding, port flooding, etc.) submissions are never eligible
    - A scenario where service disruption stops as soon as the requests stop does not qualify as persistent total service disruption, regardless of the request rate.
- Lack of, or insufficient, rate limiting. (We are aware of the lack of rate-limiting in many places and our application-wide [application limits](https://gitlab.com/groups/gitlab-org/-/epics/1737#type-of-limits) initiative aims to improve that)
- Reports about CVEs published on mailing lists, groups etc. without demonstrating an impact on GitLab
- GitLab Runner reports that do not demonstrate the ability to impact data of other projects or GitLab infrastructure
  - Note that it is [documented behavior](https://docs.gitlab.com/runner/executors/shell.html#security) of the Shell Executor to be able to see other projects on the same server
- [Self-managed Runner](https://docs.gitlab.com/runner/security/) issues 
- Scenarios in which only the number of private objects is exposed, unless it can be used to extract any sensitive information contained in those objects
  - For example a report showing that it's possible to see that a certain project has 17 issues even if only 15 are publicly visible would not be accepted
  - However being able to demonstrate that there are 4 confidential issues with the word "SECRET TOKEN" in them would be a valid report
- Spoofing email and username in git commits that aren't [signed with GPG](https://docs.gitlab.com/ee/user/project/repository/signed_commits/gpg.html)
- Clickjacking on pages with no sensitive actions
- High privilege users (maintainers, owners) using a bug to sabotage/deface their own projects
- Being able to access attachments directly with a known URL (this is a [documented behavior](https://gitlab.com/help/security/user_file_uploads.md)
- EXIF metadata not being stripped from images
  - We are aware of ways to bypass the EXIF metadata stripping and intend to improve this, but we don't consider this impactful enough to be eligible for bounty
- Bypassing or creating fake licenses, or bypasses of feature restrictions where there is no security impact
- Name squatting on dependencies without demonstrating automated impact (e.g. namesquatting a rubygem on rubygems.org where GitLab only ever installs a locally vendored gem)
- Dangling DNS records on gitlabsandbox.net 
- Ability of banned users to behave as if they are unbanned. We have [a confidential epic](https://gitlab.com/groups/gitlab-org/modelops/anti-abuse/-/epics/14) to improve this feature.
- Open redirects - in general these type of issues are informational and we only accept them if chained with other issues in order to create a more severe vulnerability
- Team member personal data leaked through YouTube videos - unless our own automation missed it.
- Vulnerabilities in [Debian packages in the Package Registry](https://docs.gitlab.com/ee/user/packages/debian_repository/)
- GitLab's ServiceNow platform.
- `*.runway.gitlab.net` endpoints
- Takeover of S3 buckets, domains or subdomains that are used for testing or if the takeover don't have an impact on GitLab infrastructure or to GitLab customers. Domains listed below are not eligible for vulnerability reports (GitLab reserves the right to adjust this list):
  - `*.gitlab-private.org`
- CI/CD Variable Disclosure - as it stands, we currently see [our guidance to use external secret storage](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-security) as sufficient for addressing reports that rely on disclosing Masked CI/CD variables to prove impact. 
- Taking over third party domains, such as external sites linked in old blog posts, or claiming unused employee social media accounts.
- Attacks that require having a victim share or leak a privileged access token (e.g. personal access token, OAuth token, project or group access token, deploy token, `_gitlab_session` token, or runner authentication token). Reports about leaked team member access tokens are still in-scope and eligible for non-CVSS bounties.
- Attacks requiring physical access to the victim's computer, including employee computer compromise
- Man-in-the-middle attacks
- Metadata disclosure, enumeration, and information gathering issues are out of scope unless the researcher demonstrates a **privacy breach that exposes confidential user data or credentials**. GitLab is a collaborative DevOps platform designed for information sharing within projects.
  - **Out of scope examples:**
    - Enumerating project IDs or determining whether a project exists
    - Accessing branch names, feature flag names, or version information visible to legitimate project members
    - Discovering template names, default configuration settings, or non-sensitive project metadata (creation dates, public descriptions)
    - Extracting version history metadata that does not expose confidential commit content
  - **In scope examples (privacy breaches):**
    - Revealing another user's private email address or credentials
    - Accessing a different project's environment variables, secrets, or confidential CI/CD configuration you don't have legitimate access to
    - Enumerating private repository contents without authorization
    - Extracting confidential data from projects you don't have legitimate access to
- DSN credentials for `new-sentry.gitlab.net`. As per  [sentry document](https://docs.sentry.io/concepts/key-terms/dsn-explainer/#the-parts-of-the-data-source-name-dsn):
  > The secret part of the DSN is optional and effectively deprecated. While clients will still honor it, if supplied, future versions of Sentry will entirely ignore it.
- Vulnerabilities that are only reproducible in our [GitLab Development kit](https://gitlab.com/gitlab-org/gitlab-development-kit). 

# Disclosure

All `Resolved` reports will be made public via issues on GitLab.com 90 days after releasing a fix. We will redact all information we consider sensitive (such as cookies or tokens), but do not hesitate to let us know if additional content should be hidden. If you also want the report to be disclosed via HackerOne, please [request disclosure](https://docs.hackerone.com/programs/disclosure.html#requesting-disclosure).
`Informative` or self-closed reports that are determined to be bugs or new [feature requests](https://handbook.gitlab.com/handbook/security/product-security/application-security/vulnerability-management/#vulnerability-vs-feature-vs-bug) with no current security impact may be imported as public issues in our issue tracker at https://gitlab.com/gitlab-org/gitlab/issues.

# Safe Harbor

The [Gold Standard Safe Harbor](https://hackerone.com/gitlab/safe_harbor) applies.

Practices authorized under this GitLab HackerOne Bug Bounty Program policy are exceptions to GitLab's [Acceptable Use Policy](https://about.gitlab.com/handbook/legal/acceptable-use-policy/).

# Eligibility for Participation

You are responsible for complying with any applicable laws. You are not eligible to participate in this program if you are currently an employee of GitLab, Inc. or any of its subsidiaries.  Reports from former employees, immediate family of current employees, or other associates of GitLab.com that may present a conflict of interest of the goals of the program will be more thoroughly reviewed and may not qualify for the stated bounty awards at GitLab's discretion.

# Our Process and Additional Information of Interest

- For more details on the process the GitLab Security Team follows when working with HackerOne reports, please see [our handbook](https://handbook.gitlab.com/handbook/security/product-security/application-security/runbooks/hackerone-process/). This includes further details on our triage and award review process.
- Practice bug hunting with our [Reproducible Vulnerabilities](https://handbook.gitlab.com/handbook/security/product-security/application-security/reproducible-vulnerabilities/) resource.
- Check out our Ask Me Anything (AMA) series with [@rpadovani](https://hackerone.com/rpadovani?type=user), [@ajxchapman](https://hackerone.com/ajxchapman?type=user), [@vakzz](https://hackerone.com/vakzz?type=user), [@joaxcar](https://hackerone.com/joaxcar?type=user), and [@0xn3va](https://hackerone.com/0xn3va?type=user) in our [Live AMA playlist on YouTube](https://www.youtube.com/playlist?list=PL05JrBw4t0Kqvvpk9PmRO6fZ0xmnKBp_s).
- Want to see how Bug Bounty Hunters use GitLab to improve their research efforts? Check out ["How do bug bounty hunters use GitLab to help their hack?"](https://about.gitlab.com/blog/2021/06/11/how-i-use-gitlab-to-help-my-hack/). See all of our [bug bounty related blog posts](https://about.gitlab.com/blog/tags.html#bug-bounty).
- See our Ask a Hacker blog series, where we profiled some of our top hackers. See the [blog](https://about.gitlab.com/blog/2023/10/02/ask-a-hacker/) profiling [@0xn3va](https://hackerone.com/0xn3va?type=user), the [blog](https://about.gitlab.com/blog/2020/11/10/rpadovani-ask-a-hacker/) profiling [@rpadovani](https://hackerone.com/rpadovani?type=user) and this [blog](https://about.gitlab.com/blog/2021/03/04/ajxchapman-ask-a-hacker/) where we profile [@ajxchapman](https://hackerone.com/ajxchapman?type=user), and [this blog](https://about.gitlab.com/blog/2022/07/27/cracking-our-bug-bounty-top-10/) where we chat with [@joaxcar](https://hackerone.com/joaxcar?type=user)
- The [GitLab Red Team](https://about.gitlab.com/handbook/engineering/security/security-operations/red-team/) hosted a live, public AMA/Ask Me Anything on Jan. 26, 2021. Check out the [replay](https://youtu.be/FCu7MiRX5Lw).
- If you have suggestions for improving this program, please open an issue in [our HackerOne Questions GitLab project](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/hackerone-questions)

# Work at GitLab

GitLab is regularly looking to hire talented security professionals. Learn more at [our jobs page](https://about.gitlab.com/jobs/).

