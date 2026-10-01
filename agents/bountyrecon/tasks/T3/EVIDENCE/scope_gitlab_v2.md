# STRUCTURED SCOPE v2 (có `archived_at`) — GitLab (handle `gitlab`)

**Ngày chụp:** `2026-10-01T15:28:34Z` (UTC) · **Nguồn:** `POST https://hackerone.com/graphql` (công khai, không auth)
**Quan hệ với bản gốc:** đây là **BẢN CHỤP LẠI** theo `D-026` phương án (a).
Bản gốc `scope_gitlab.md` **KHÔNG bị sửa, KHÔNG bị xoá** — vẫn là bằng chứng pháp lý cho thời điểm chụp gốc `2026-10-01`.

> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** cột `archived_at` cho biết bản ghi **đã nghỉ hưu hay chưa**. **KHÔNG** được suy ra 'ngoài scope'. Chỉ được khẳng định: bảng thiếu chiều này thì **KHÔNG PHÂN BIỆT ĐƯỢC**.
> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi `archived_at != None` **chưa có định nghĩa chính thức**. Ghi hiện tượng, KHÔNG kết luận ngữ nghĩa.

**Thống kê tự đo:** `archived:false` = **44** scope (sub=True **19**) · `archived:true` = **19** scope (sub=True **5**) · TỔNG **63**

## archived=false (đang hiệu lực) — n=44

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| WILDCARD | *.gitlab.net | True | True | medium | `None` | Hosts owned and operated by GitLab. |
| WILDCARD | *.gitlab.org | True | True | medium | `None` | Hosts owned and operated by GitLab. |
| WILDCARD | *.gitlap.com | True | True | medium | `None` | Hosts owned and operated by GitLab. gitla**p** with a p! |
| URL | customers.gitlab.com | True | True | critical | `None` | Server-side Denial of Service is out of scope as per our Policy. |
| URL | registry.gitlab.com | True | True | critical | `None` |  |
| URL | gitlab.com | True | True | critical | `None` |  |
| URL | about.gitlab.com | True | True | medium | `None` | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | docs.gitlab.com | True | True | medium | `None` | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | design.gitlab.com | True | True | medium | `None` | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | advisories.gitlab.com | True | True | medium | `None` | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab | True | True | critical | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-runner | True | True | critical | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitaly | True | True | critical | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-pages | True | True | critical | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-shell | True | True | critical | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-vscode-extension | True | True | critical | `None` |  |
| OTHER | Your Own GitLab Instance | True | True | critical | `None` |  |
| OTHER | Other non-production infrastructure | True | True | medium | `None` | Hosts owned and operated by GitLab other than gitlab.com itself and our static websites. |
| OTHER | GitLab for Jira Cloud | True | True | medium | `None` |  |
| WILDCARD | *.gitlab.cn | False | False | none | `None` | `gitlab.cn` and the JiHu-specific GitLab distribution which are property of GitLab Information Technology (Hubei) Co., Ltd. (JiHu), security issues in those products should be reported to `security@gitlab.cn` |
| WILDCARD | *.runway.gitlab.net | False | False | none | `None` |  |
| WILDCARD | *.gitlab-private.org | False | False | none | `None` | Dangling DNS for *.gitlab-private.org is out of scope |
| WILDCARD | *.service-now.com | False | False | none | `None` |  |
| URL | dashboards.gitlab.com | False | False | none | `None` |  |
| URL | alerts.gitlab.com | False | False | none | `None` |  |
| URL | support.gitlab.com | False | False | none | `None` |  |
| URL | shop.gitlab.com | False | False | none | `None` |  |
| URL | forum.gitlab.com | False | False | none | `None` |  |
| URL | status.gitlab.com | False | False | none | `None` |  |
| URL | partners.gitlab.com | False | False | none | `None` |  |
| URL | aptly.gitlab.com | False | False | none | `None` |  |
| URL | translate.gitlab.com | False | False | none | `None` |  |
| URL | federal-support.gitlab.com | False | False | none | `None` |  |
| URL | us-federal-gitlab.com | False | False | none | `None` |  |
| URL | ir.gitlab.com | False | False | none | `None` |  |
| URL | levelup.gitlab.com | False | False | none | `None` |  |
| URL | gitlab.biterg.io | False | False | none | `None` | This is a third-party website that aggregates public data from GitLab.com. It is out of scope and the data hosted there is not meant to be confidential. https://contributors.gitlab.com/ redirects to this website. |
| URL | gitlabsandbox.net | False | False | none | `None` |  |
| URL | gitlabdemo.cloud | False | False | none | `None` |  |
| URL | gitlabtraining.cloud | False | False | none | `None` |  |
| URL | packages.gitlab.com | False | False | none | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/cli/ | False | False | none | `None` | This is a community project that is [now officially maintained by GitLab](https://about.gitlab.com/blog/2022/12/07/introducing-the-gitlab-cli/). It will be in scope at a later time but it is not ready yet. |
| SOURCE_CODE | https://gitlab.com/gitlab-org/opstrace/opstrace-ui | False | False | none | `None` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/opstrace/opstrace | False | False | none | `None` |  |

## archived=true (đã nghỉ hưu) — n=19

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| OTHER | GitLab for Jira Cloud Plugin | True | True | critical | `2023-12-07T13:38:09.687Z` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/opstrace/ | True | True | critical | `2023-06-04T21:02:31.693Z` |  |
| OTHER | Static websites | True | True | medium | `2022-07-21T16:00:50.221Z` | Our static websites like the marketing website, the handbook, or the documentation. There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | docs.gitlab.com | False | False | none | `2022-07-21T15:53:13.475Z` |  |
| URL | about.gitlab.com | False | False | none | `2022-07-21T15:53:03.572Z` |  |
| URL | *.gitlab.net | False | False | none | `2022-07-21T15:51:33.499Z` |  |
| URL | *.gitlap.com | False | False | none | `2022-07-21T15:51:16.877Z` |  |
| URL | license.gitlab.com | True | True | critical | `2022-03-21T22:30:03.041Z` |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-workhorse | True | True | critical | `2021-12-28T13:36:15.653Z` |  |
| WILDCARD | *.gitter.im | False | False | none | `2021-05-25T18:36:39.198Z` |  |
| URL | blog.gitter.im | False | False | none | `2020-10-05T18:33:57.577Z` |  |
| URL | update.gitter.im | False | False | none | `2020-10-05T18:33:50.259Z` |  |
| URL | files.gitter.im | False | False | none | `2020-10-05T18:33:45.165Z` |  |
| URL | next.gitter.im | False | False | none | `2020-10-05T18:33:39.863Z` |  |
| URL | beta.gitter.im | False | False | none | `2020-10-05T18:33:33.863Z` |  |
| WILDCARD | ws*.gitter.im | False | False | none | `2020-10-05T18:33:28.485Z` |  |
| URL | api.gitter.im | False | False | none | `2020-10-05T18:33:21.413Z` |  |
| URL | gitlab.net | False | False | none | `2020-10-05T18:32:21.936Z` |  |
| URL | gitlap.com | False | False | none | `2020-10-05T18:32:08.263Z` |  |

