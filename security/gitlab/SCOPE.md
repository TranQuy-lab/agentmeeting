# SCOPE — GitLab Bug Bounty

**Chương trình:** GitLab Bug Bounty
**Tổ chức:** GitLab Inc. (công ty tư nhân, Hoa Kỳ) — **KHÔNG phải** cơ quan nhà nước.
**Nền tảng:** HackerOne — handle `gitlab` → <https://hackerone.com/gitlab>
**URL chính sách gốc:** <https://hackerone.com/gitlab?view=policy>
**Ngày fetch:** `2026-10-01` (giờ máy UTC `2026-10-01T13:5xZ`, giờ VN `2026-10-01 20:5x +07`)
**Người lập:** BountyRecon (`ag_579fc4fa`) · **Task:** T3 · **Nhánh:** `agent/bounty-recon/T3`
**Trạng thái:** ⚠️ **Trích được nguyên văn, NHƯNG có 4 XUNG ĐỘT scope — xem §2b. PHẢI HỎI ADMIN.**

> ⚠️ **Chưa được verify.** Theo D-004, người viết KHÔNG tự verify. Chờ Reviewer1.

---

## 0. Phương pháp fetch

| Bước | Lệnh / URL | Kết quả |
|---|---|---|
| 1 | `POST https://hackerone.com/graphql` (công khai, không auth) `team(handle:"gitlab")` | HTTP 200, JSON parse OK |
| 2 | `curl -sS https://gitlab.com/.well-known/security.txt` | HTTP 200 — xác nhận HackerOne là kênh chính thức |

Bằng chứng nguồn chính sách chính thức — trích nguyên văn `https://gitlab.com/.well-known/security.txt`:

```text
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

# Preferred disclosure is via HackerOne
Contact: https://hackerone.com/gitlab/

# Additional disclosure processes are available in our handbook:
Contact: https://about.gitlab.com/security/disclosure/

Policy: https://hackerone.com/gitlab/
```

Script + JSON thô: `agents/bountyrecon/tasks/T3/EVIDENCE/` (`fetch_h1.py`, `h1_gitlab.json`,
`policy_gitlab.md`, `scope_gitlab.md`, `recon_gitlab.txt`).

---

## 1. TRÍCH NGUYÊN VĂN — IN SCOPE (`eligible_for_submission=true`, n=24)

```text
WILDCARD    *.gitlab.net
            instruction: "Hosts owned and operated by GitLab."
WILDCARD    *.gitlab.org
            instruction: "Hosts owned and operated by GitLab."
WILDCARD    *.gitlap.com
            instruction: "Hosts owned and operated by GitLab. gitla**p** with a p!"
URL         gitlab.com                            max_severity=critical
URL         registry.gitlab.com                   max_severity=critical
URL         customers.gitlab.com                  max_severity=critical
            instruction: "Server-side Denial of Service is out of scope as per our Policy."
URL         license.gitlab.com                    max_severity=critical
URL         about.gitlab.com                      max_severity=medium
            instruction: "There is no user data therefore no confidentiality impact is possible,
            however we want to know if you can modify the content or make it unavailable."
URL         docs.gitlab.com                       max_severity=medium   (instruction như trên)
URL         design.gitlab.com                     max_severity=medium   (instruction như trên)
URL         advisories.gitlab.com                 max_severity=medium   (instruction như trên)
OTHER       Your Own GitLab Instance              max_severity=critical
OTHER       Other non-production infrastructure   max_severity=medium
            instruction: "Hosts owned and operated by GitLab other than gitlab.com itself
            and our static websites."
OTHER       Static websites                       max_severity=medium
            instruction: "Our static websites like the marketing website, the handbook, or the
            documentation. There is no user data therefore no confidentiality impact is possible,
            however we want to know if you can modify the content or make it unavailable."
OTHER       GitLab for Jira Cloud                 max_severity=medium
OTHER       GitLab for Jira Cloud Plugin          max_severity=critical
SOURCE_CODE https://gitlab.com/gitlab-org/gitlab
SOURCE_CODE https://gitlab.com/gitlab-org/gitlab-runner
SOURCE_CODE https://gitlab.com/gitlab-org/gitaly
SOURCE_CODE https://gitlab.com/gitlab-org/gitlab-pages
SOURCE_CODE https://gitlab.com/gitlab-org/gitlab-shell
SOURCE_CODE https://gitlab.com/gitlab-org/gitlab-vscode-extension
SOURCE_CODE https://gitlab.com/gitlab-org/gitlab-workhorse
SOURCE_CODE https://gitlab.com/gitlab-org/opstrace/
```

Policy prose bổ sung — `policy_gitlab.md` § `# Scope`, dòng 87–89:

```text
All GitLab Inc. products are in scope unless explicitly noted otherwise.
 
Testing on subdomains that are neither explicitly in scope nor out of scope isn't encouraged, but if you can find a vulnerability with business impact on such a subdomain please report it. We normally close sufficiently clear reports as `Informative` so there will be [no negative effect](https://www.hackerone.com/blog/reputation-signal-impact-enhancements-whats-changing-and-why) on your reputation score if we decide that it's out of scope. However, remember that GitLab subdomains that are running third party services are strictly out of scope.
```

---

## 2. TRÍCH NGUYÊN VĂN — OUT OF SCOPE

### 2a. Danh sách out-of-scope (n=39)

```text
WILDCARD  *.gitlab.cn        — "gitlab.cn and the JiHu-specific GitLab distribution which are
                                property of GitLab Information Technology (Hubei) Co., Ltd.
                                (JiHu), security issues in those products should be reported
                                to security@gitlab.cn"
WILDCARD  *.runway.gitlab.net
WILDCARD  *.gitlab-private.org — "Dangling DNS for *.gitlab-private.org is out of scope"
WILDCARD  *.service-now.com
WILDCARD  *.gitter.im ; URL blog.gitter.im ; update.gitter.im ; files.gitter.im ;
          next.gitter.im ; beta.gitter.im ; api.gitter.im ; WILDCARD ws*.gitter.im
URL       dashboards.gitlab.com | alerts.gitlab.com | support.gitlab.com | shop.gitlab.com |
          forum.gitlab.com | status.gitlab.com | partners.gitlab.com | aptly.gitlab.com |
          translate.gitlab.com | federal-support.gitlab.com | us-federal-gitlab.com |
          ir.gitlab.com | levelup.gitlab.com | packages.gitlab.com | gitlabsandbox.net |
          gitlabdemo.cloud | gitlabtraining.cloud | gitlab.net | gitlap.com
URL       gitlab.biterg.io   — "This is a third-party website that aggregates public data from
                                GitLab.com. It is out of scope and the data hosted there is not
                                meant to be confidential. https://contributors.gitlab.com/
                                redirects to this website."
SOURCE_CODE https://gitlab.com/gitlab-org/cli/  — "This is a community project that is now
                                officially maintained by GitLab. It will be in scope at a later
                                time but it is not ready yet."
SOURCE_CODE https://gitlab.com/gitlab-org/opstrace/opstrace-ui
SOURCE_CODE https://gitlab.com/gitlab-org/opstrace/opstrace
```

Prose out-of-scope (không nằm trong bảng structured) — `policy_gitlab.md` § `## Out of scope`,
dòng 125–191, danh sách rất dài. Các mục quan trọng nhất cho giai đoạn trinh sát:

```text
- Automated scanning reports of any kind
- GitLab sites of third party software and services (marketing services, third-party mail services, developer/support installations etc.)
- Our customers' GitLab installs
- Social engineering, phishing, or other fraud including but not limited to: internationalized domain name (IDN) homograph attacks, Right-to-left (RTL) Ambiguity, RTL Override (RTLO), SPF and DKIM issues, most HTML content injection, Tabnabbing
- Missing Security Headers (eg. HSTS, CSP) and Missing Secure Flags on Cookies
- TLS/SSL or SSH issues (weak ciphers/key-size/BEAST/CRIME)
- User and project enumeration/path disclosure unless an additional impact can be demonstrated
- Denial of Service (DoS) issues
- Lack of, or insufficient, rate limiting.
- Metadata disclosure, enumeration, and information gathering issues are out of scope unless the researcher demonstrates a **privacy breach that exposes confidential user data or credentials**.
- Vulnerabilities that are only reproducible in our [GitLab Development kit](https://gitlab.com/gitlab-org/gitlab-development-kit).
```

> 📌 **Hệ quả cực kỳ quan trọng cho T3:** GitLab tuyên bố thẳng **"Automated scanning reports of
> any kind"** và **"Metadata disclosure, enumeration, and information gathering issues are out of
> scope"**. Nghĩa là **kết quả trinh sát thụ động KHÔNG tự nó là một finding có thưởng.**
> Trinh sát chỉ có giá trị làm *đầu vào* để tìm lỗi có tác động thật.

---

## 2b. TÀI SẢN ĐÃ NGHỈ HƯU — **0 XUNG ĐỘT HIỆU LỰC** (đã đính chính ở T28)

> 🔄 **ĐÍNH CHÍNH (T28, `2026-10-01`).** Mục này trước đây gọi là *"4 XUNG ĐỘT SCOPE ĐÃ XÁC MINH"*.
> **Cách gọi đó SAI.** Cách đọc đúng: **0 xung đột hiệu lực + 4 bản ghi đã nghỉ hưu
> (`archived_at` = 2022-07-21)**.
>
> **Thay đổi này supersede chứng thực T14 ở RIÊNG §2b; phần trích nguyên văn (§1, §2a, §3, §4)
> KHÔNG đổi nên chứng thực byte-exact vẫn nguyên giá trị cho phần đó.**

### Nguyên nhân gốc — bài học M-01 (Auditor2 T24)

Bốn tài sản xuất hiện ở **cả hai phía** không phải vì chính sách mâu thuẫn, mà vì phép so đã đem
vế IN **đang hiệu lực** so với vế OUT **đã nghỉ hưu từ 2022-07-21** — cách nhau **4 năm**.

Biến quyết định **không phải `asset_type`**, mà là **`archived_at`** — trường mà **cả ba** kiểm
định viên ở thời điểm đó (BountyRecon, Reviewer1, DeepSeek-Harness) **đều không truy vấn**.

> 📋 Theo `security/_TEMPLATE/SCOPE.md`: **`archived_at` của MỌI asset là trường BẮT BUỘC.**
> Bỏ nó ⇒ sinh ra "xung đột scope" giả giữa chính sách **đang hiệu lực** và bản ghi **đã nghỉ hưu**.

Truy vấn T3 của tôi **không hỏi** trường này ⇒ bỏ sót một chiều dữ liệu. **`archived_at` CÓ trong
schema công khai** (đã tự kiểm ở T28: `{__type(name:"StructuredScope"){fields{name}}}` →
`archived_at` = `True`), nên đây **không phải giới hạn công cụ** mà là chiều dữ liệu tôi đã không hỏi.

### Bằng chứng thô — tự tái lập (T28)

`POST https://hackerone.com/graphql` (công khai, không auth), `team(handle:"gitlab")`:

```text
archived:false -> tong 44   IN=19   OUT=25
IN giao OUT (theo asset_identifier): 0        <-- KHONG con xung dot nao

archived:true  -> tong 19
   *.gitlab.net      type=URL  eligible=False  archived_at=2022-07-21T15:51:33.499Z
   *.gitlap.com      type=URL  eligible=False  archived_at=2022-07-21T15:51:16.877Z
   about.gitlab.com  type=URL  eligible=False  archived_at=2022-07-21T15:53:03.572Z
   docs.gitlab.com   type=URL  eligible=False  archived_at=2022-07-21T15:53:13.475Z
```

| # | Tài sản | Vế IN (còn hiệu lực) | Vế OUT (**`archived_at`**) |
|---|---|---|---|
| 1 | `*.gitlab.net` | `WILDCARD`, bounty=`True`, `medium`, `archived_at=None` | `URL`, bounty=`False`, **`2022-07-21T15:51:33.499Z`** |
| 2 | `*.gitlap.com` | `WILDCARD`, bounty=`True`, `medium`, `archived_at=None` | `URL`, bounty=`False`, **`2022-07-21T15:51:16.877Z`** |
| 3 | `about.gitlab.com` | `URL`, bounty=`True`, `medium`, `archived_at=None` | `URL`, bounty=`False`, **`2022-07-21T15:53:03.572Z`** |
| 4 | `docs.gitlab.com` | `URL`, bounty=`True`, `medium`, `archived_at=None` | `URL`, bounty=`False`, **`2022-07-21T15:53:13.475Z`** |

⇒ **0 xung đột hiệu lực.** Cả 4 vế OUT thuộc **một đợt lưu trữ duy nhất ngày 2022-07-21**.

> ⛔ **QUYẾT ĐỊNH CỦA ADMIN KHÔNG ĐỔI:** vẫn **loại cả 4 tài sản khỏi T4**.
> Nay gọi đúng tên: **"0 xung đột thật + 4 loại thận trọng"**. Thận trọng hơn mức cần nhưng
> **không gây hại**, trong khi khai thác nhầm gây hại không khắc phục được
> (D-021 §1; `DISSENT-7`/`DISSENT-8`).

*(Ghi chú: GitHub cũng có 1 mục tương tự — `Atom`, nhưng cả hai phía đều `eligible_for_bounty=False`
nên dù hiểu thế nào thì Atom cũng không được thưởng.)*

---

## 3. TRÍCH NGUYÊN VĂN — QUY ĐỊNH CẤM / GIỚI HẠN

`policy_gitlab.md` § `# Rules of Engagement, Testing, and Proof-of-concepts`, dòng 34–59:

```text
When researching security issues, especially those which may compromise the privacy of others, you must use only test accounts in order to respect our users' privacy. Accessing private information of other users, performing actions that may negatively affect GitLab's users (e.g., spam, denial of service) will disqualify the report. Activity that is disruptive to GitLab operations will result in account bans and disqualification of the report. Examples of disruptive activity include, but are not limited to:
 - Generating abuse requests
 - Submission of support, sales or other requests to 3rd party systems
 - Mass creation of users, groups, and projects
 - Typosquatting or other namesquatting
 - Spam-like or other high volume activity

Sending reports from automated tools without verifying them will immediately disqualify the report.
```

```text
**For Denial of Service (DoS) vulnerabilities specifically:** 
Testing and demonstrating DoS impact on a local GDK instance can be problematic. If you need to demonstrate DoS impact, we recommend testing on a self-managed GitLab instance with specifications and resources equal to or greater than the [self-managed GitLab installation requirements](https://docs.gitlab.com/install/requirements/).
**Never test DoS vulnerabilities on GitLab.com.**
```

```text
For vulnerabilities requiring GitLab.com production architecture, you must use test accounts created with your HackerOne email alias (yourhandle@wearehackerone.com). **Never test against projects, groups, accounts, or instances you do not own.**
```

`## Demonstrating Impact`, dòng 63–64:

```text
- Always choose a non disruptive option to demonstrate the impact. If the only way to demonstrate an impact is a disruptive one then stop and report the issue, we will validate the impact.
- In the case of reports related to credential leaks do not create additional access credentials using the leaked one. We will determine impact ourselves and award for the maximum impact we uncover.
```

`Testing on GitLab.com`, dòng 73:

```text
Please don't request Developer access to our projects, including the GitLab Community Forks group. While it can indeed be a security risk for the company that a random person joins those projects, it is something the security team handles and we don't want bug bounty hunters to test those workflows as it creates unnecessary noise for our teams.
```

---

## 4. TRÍCH NGUYÊN VĂN — MỨC THƯỞNG CÔNG BỐ

`policy_gitlab.md` § `# Rewards`, dòng 4 và 6:

```text
For reports with critical or high severity we pay $1000 at the time the report is triaged, and for medium severity reports we pay $500. The remainder, if any, will be paid as soon as the severity has been fully analyzed internally. The calculator we use to calculate CVSS-based bounty amounts is [accessible to everyone](https://gitlab-com.gitlab.io/gl-security/appsec/cvss-calculator/).
```

```text
Reports about intended behavior resulting in an update of our documentation will be rewarded with a $100 bounty, as long as this update is security related.
```

```text
For valid reports for which the author can't accept monetary rewards, we offer to plant trees in our [GitLab forest](https://tree-nation.com/trees/view/5119567) on their behalf.
```

Bảng theo mức độ (dòng 2, không nêu số cụ thể trong text — dùng công cụ CVSS):

```text
We have different rewards depending on the business impact of each asset. A more complete description of each asset will be in the scope section, but in general GitLab.com and all our products' source code is rewarded the highest, then non-production environments have reduced bounties and our static websites have the lowest payouts.
```

Khoảng thưởng do nền tảng HackerOne công bố:

```json
{"minimum_bounty_table_value": 100, "maximum_bounty_table_value": 35000,
 "top_bounty_lower_amount": 10000, "top_bounty_upper_amount": 36500,
 "average_bounty_lower_amount": 1000, "average_bounty_upper_amount": 1370,
 "formatted_total_bounties_paid_amount": 7443997, "offers_bounties": true}
```

⇒ Khoảng công bố **100 USD – 35.000 USD** (top thực tế tới 36.500 USD). Tổng đã trả
**7.443.997 USD** (số HackerOne, **chưa xác minh độc lập**).

---

## 5. KẾT LUẬN SCOPE (tổng hợp của tôi — KHÔNG nguyên văn)

| Hạng mục | Kết luận |
|---|---|
| Trích được nguyên văn in-scope? | ✅ **CÓ** (24 tài sản) — nhưng 4 tài sản bị xung đột |
| Trích được nguyên văn out-of-scope? | ✅ **CÓ** (39 tài sản + danh sách prose dài) |
| Trích được quy định cấm? | ✅ **CÓ** (rất chặt về DoS, test account, tự động hoá) |
| Mức thưởng công bố? | ✅ **CÓ** ($500/$1000 khi triage, $100 tài liệu, tối đa $35.000) |
| Tài sản dễ kiểm chứng? | ✅ **CÓ** — `gitlab.com`, `registry.gitlab.com`, `customers.gitlab.com` |
| Đủ điều kiện chuyển ExploitDeep (T4)? | ⚠️ **CÓ ĐIỀU KIỆN** — phải chốt 4 xung đột ở §2b trước |

**Cảnh báo bắt buộc cho ExploitDeep — trích nguyên văn:**
> "**Never test DoS vulnerabilities on GitLab.com.**"
> "**Never test against projects, groups, accounts, or instances you do not own.**"

⇒ Nghiên cứu DoS **chỉ** trên instance tự dựng (GDK / self-managed). Mọi hành vi gây gián đoạn
trên `gitlab.com` = mất quyền + có thể bị khoá tài khoản.

**Không có tài sản nào trong scope thuộc:** cơ quan nhà nước, hạ tầng trọng yếu, hay tổ chức
Việt Nam. Điều kiện bất khả xâm phạm của D-005 được thoả.
