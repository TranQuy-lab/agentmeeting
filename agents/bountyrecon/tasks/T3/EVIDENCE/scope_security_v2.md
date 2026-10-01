# STRUCTURED SCOPE v2 (có `archived_at`) — HackerOne (handle `security`)

**Ngày chụp:** `2026-10-01T15:28:34Z` (UTC) · **Nguồn:** `POST https://hackerone.com/graphql` (công khai, không auth)
**Quan hệ với bản gốc:** đây là **BẢN CHỤP LẠI** theo `D-026` phương án (a).
Bản gốc `scope_security.md` **KHÔNG bị sửa, KHÔNG bị xoá** — vẫn là bằng chứng pháp lý cho thời điểm chụp gốc `2026-10-01`.

> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** cột `archived_at` cho biết bản ghi **đã nghỉ hưu hay chưa**. **KHÔNG** được suy ra 'ngoài scope'. Chỉ được khẳng định: bảng thiếu chiều này thì **KHÔNG PHÂN BIỆT ĐƯỢC**.
> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi `archived_at != None` **chưa có định nghĩa chính thức**. Ghi hiện tượng, KHÔNG kết luận ngữ nghĩa.

**Thống kê tự đo:** `archived:false` = **34** scope (sub=True **26**) · `archived:true` = **39** scope (sub=True **31**) · TỔNG **73**

## archived=false (đang hiệu lực) — n=34

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| URL | hackerone.com | True | True | critical | `None` | This is our main application that hackers and customers use to interact with each other. It connects with a database that contains information about vulnerability reports, users, and programs. This system’s backend is written in Ruby and exposes data to the client through GraphQL, rendered pages, and JSON endpoints. |
| URL | api.hackerone.com | True | True | critical | `None` | This is our public API that customers use to read and interact with reports. To look for vulnerabilities in this asset, create a sandboxed program, select HackerOne Professional or HackerOne Enterprise in the Product Edition settings page, and create an API token. This system’s backend is written in Ruby, converts the request to a GraphQL query, and serializes the GraphQL result to JSON. |
| URL | www.hackerone.com | True | True | critical | `None` | This is our marketing website. It does not contain any report or customer information. It may store information about hackers, such as information collected through the [penetration tester sign up form](https://www.hackerone.com/hackers/pentest-community-application). The website runs Drupal with a few customizations. |
| URL | app.pullrequest.com | True | True | critical | `None` | Please use your `@wearehackerone.com` email address when signing up. |
| URL | reviewer.pullrequest.com | True | True | critical | `None` | Please use your `@wearehackerone.com` email address when signing up. |
| URL | hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com | True | True | critical | `None` | This is an Amazon S3 bucket that contains attachments of reports and activities. These attachments may contain confidential information. A signed request is required to download an object. |
| URL | www.wearehackerone.com | True | True | critical | `None` |  |
| URL | mta-sts.wearehackerone.com | True | True | critical | `None` |  |
| URL | errors.hackerone.net | True | True | high | `None` | A separate domain that we use to capture information of client and server side exceptions. |
| URL | https://*.hackerone-ext-content.com | True | True | medium | `None` | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | a5s.hackerone-ext-content.com | True | True | medium | `None` | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | b5s.hackerone-ext-content.com | True | True | medium | `None` | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | hackerone-ext-content.com | True | True | medium | `None` | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | https://*.hackerone-user-content.com/ | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object.   |
| URL | ctf.hacker101.com | True | True | low | `None` | The Hacker101 CTF domain, ctf.hacker101.com, is not connected to HackerOne's production environment. It is hosted on Amazon AWS. Users authenticate through HackerOne.com (OAuth). The maximum bounty for any vulnerability on this asset is $500 right now. The CTF challenges itself are not in scope for our bug bounty program. |
| URL | hackathon-photos.hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | cover-photos.hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | hackathon-photos-us-east-2.hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | profile-photos.hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | profile-photos-us-east-2.hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | cover-photos-us-east-2.hackerone-user-content.com | True | True | low | `None` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | hackerone.live | True | True | low | `None` |  |
| OTHER | *.vpn.hackerone.net | True | True | critical | `None` | The HackerOne hacker VPN is used by hackers and HackerOne personnel. We'd be most interested in vulnerabilities that allow you to route traffic to other clients (lack of client isolation), routing traffic to internal HackerOne / Amazon networks, and bypassing [sslsplit](https://github.com/droe/sslsplit). Traffic routed through the VPN will originate from `66.232.20.0/23` or `206.166.248.0/23` (Hac |
| OTHER | https://hackerone.com/mcp | True | True | critical | `None` |  |
| OTHER | https://github.com/Hacker0x01/react-datepicker | True | False | critical | `None` |  |
| URL | support.hackerone.com | False | False | none | `None` | This asset is hosted by Freshdesk (as of 2023-04-28), and as such these reports should be submitted to the appropriate program: https://hackerone.com/freshworks |
| URL | go.hacker.one | False | False | none | `None` | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | info.hacker.one | False | False | none | `None` | This asset is hosted by Unbounce, and as such these reports should be submitted to them via https://unbounce.com/security/. |
| URL | ma.hacker.one | False | False | none | `None` | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | h1.community | False | False | none | `None` |  |
| URL | www.h1.community | False | False | none | `None` |  |
| URL | www.hackeronestatus.com | False | False | none | `None` | This asset is hosted by Atlassian, and as such these reports should be submitted to their program instead via https://bugcrowd.com/statuspage.  |
| URL | hackerone-swag.com | False | False | none | `None` |  |

## archived=true (đã nghỉ hưu) — n=39

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| CIDR | 66.232.20.0/23 | True | True | critical | `2026-05-01T10:16:16.315Z` | This net block is the origin of all traffic routed through the HackerOne hacker VPN. See the description for *.vpn.hackerone.net for the stack and vulnerabilities we're interested in. |
| CIDR | 206.166.248.0/23 | True | True | critical | `2026-05-01T10:15:49.217Z` | This net block is the origin of all traffic routed through the HackerOne hacker VPN. See the description for *.vpn.hackerone.net for the stack and vulnerabilities we're interested in. |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.277Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.249Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.226Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.203Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.181Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.159Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.136Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.114Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.092Z` | HackerOne GraphQL  |
| URL | hackerone.com/graphql | True | False | critical | `2023-03-10T15:19:52.069Z` | HackerOne GraphQL  |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.699Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.677Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.656Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.633Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.611Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.589Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.567Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.544Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.522Z` | HackerOne Web Application |
| URL | hackerone.com | True | False | critical | `2023-03-10T15:19:51.497Z` | HackerOne Web Application |
| URL | app.qualified.dev | False | False | none | `2022-09-06T18:11:01.059Z` |  |
| URL | qualified.dev | False | False | none | `2022-09-06T18:11:01.059Z` |  |
| URL | hackerone.com | True | False | critical | `2022-07-11T12:44:06.753Z` | HackerOne Web Application |
| URL | https://ma.hacker.one | False | False | none | `2022-07-11T12:44:06.374Z` | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | https://info.hacker.one/ | False | False | none | `2022-07-11T12:44:06.349Z` | This asset is hosted by Unbounce, and as such these reports should be submitted to them via https://unbounce.com/security/. |
| URL | https://www.hackeronestatus.com/ | False | False | none | `2022-07-11T12:44:06.322Z` | This asset is hosted by Atlassian, and as such these reports should be submitted to their program instead via https://bugcrowd.com/statuspage.  |
| URL | https://go.hacker.one | False | False | none | `2022-07-11T12:44:06.293Z` | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | https://ctf.hacker101.com | True | True | low | `2022-07-11T12:44:06.093Z` | The Hacker101 CTF domain, ctf.hacker101.com, is not connected to HackerOne's production environment. It is hosted on Amazon AWS. Users authenticate through HackerOne.com (OAuth). The maximum bounty for any vulnerability on this asset is $500 right now. The CTF challenges itself are **not** in scope for our bug bounty program. |
| URL | https://reviewer.pullrequest.com | True | True | critical | `2022-07-11T12:44:06.060Z` | Please use your `@wearehackerone.com` email address when signing up. |
| URL | https://app.pullrequest.com | True | True | critical | `2022-07-11T12:44:06.032Z` | Please use your `@wearehackerone.com` email address when signing up. |
| URL | https://hackerone-us-west-2-production-attachments.s3-us-west-2.amazonaws.com/ | True | True | critical | `2022-07-11T12:44:06.004Z` | This is an Amazon S3 bucket that contains attachments of reports and activities. These attachments may contain confidential information. A signed request is required to download an object. |
| OTHER | *.hackerone-ext-content.com | True | True | medium | `2022-06-07T12:38:56.224Z` | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| OTHER | *.hackerone-user-content.com | True | True | low | `2022-06-07T12:38:33.235Z` | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | http://hackerone.com/graphql | True | False | critical | `2021-05-06T03:28:45.343Z` | HackerOne GraphQL  |
| URL | events.hackerone.com | False | False | none | `2021-01-14T21:25:22.455Z` |  |
| URL | hackerone-attachments.s3.amazonaws.com | True | True | critical | `2018-07-06T02:41:18.663Z` | This is an Amazon S3 bucket that contains attachments of reports and activities. These attachments may contain confidential information. A signed request is required to download an object.   |
| URL | hackerone-test.com | False | False | none | `2017-11-13T04:15:16.680Z` |  |

