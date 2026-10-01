# STRUCTURED SCOPE — GitLab (handle: gitlab)
offers_bounties=True submission_state=open

## IN SCOPE / eligible_for_submission=true  (n=24)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| WILDCARD | *.gitlab.net | True | medium | Hosts owned and operated by GitLab. |
| WILDCARD | *.gitlab.org | True | medium | Hosts owned and operated by GitLab. |
| WILDCARD | *.gitlap.com | True | medium | Hosts owned and operated by GitLab. gitla**p** with a p! |
| URL | customers.gitlab.com | True | critical | Server-side Denial of Service is out of scope as per our Policy. |
| URL | registry.gitlab.com | True | critical |  |
| URL | gitlab.com | True | critical |  |
| URL | about.gitlab.com | True | medium | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | docs.gitlab.com | True | medium | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | design.gitlab.com | True | medium | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | advisories.gitlab.com | True | medium | There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-runner | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitaly | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-pages | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-shell | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-vscode-extension | True | critical |  |
| OTHER | Your Own GitLab Instance | True | critical |  |
| OTHER | Other non-production infrastructure | True | medium | Hosts owned and operated by GitLab other than gitlab.com itself and our static websites. |
| OTHER | GitLab for Jira Cloud | True | medium |  |
| OTHER | GitLab for Jira Cloud Plugin | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/opstrace/ | True | critical |  |
| OTHER | Static websites | True | medium | Our static websites like the marketing website, the handbook, or the documentation. There is no user data therefore no confidentiality impact is possible, however we want to know if you can modify the content or make it unavailable. |
| URL | license.gitlab.com | True | critical |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/gitlab-workhorse | True | critical |  |

## OUT OF SCOPE / eligible_for_submission=false  (n=39)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| WILDCARD | *.gitlab.cn | False | none | `gitlab.cn` and the JiHu-specific GitLab distribution which are property of GitLab Information Technology (Hubei) Co., Ltd. (JiHu), security issues in those products should be reported to `security@gitlab.cn` |
| WILDCARD | *.runway.gitlab.net | False | none |  |
| WILDCARD | *.gitlab-private.org | False | none | Dangling DNS for *.gitlab-private.org is out of scope |
| WILDCARD | *.service-now.com | False | none |  |
| URL | dashboards.gitlab.com | False | none |  |
| URL | alerts.gitlab.com | False | none |  |
| URL | support.gitlab.com | False | none |  |
| URL | shop.gitlab.com | False | none |  |
| URL | forum.gitlab.com | False | none |  |
| URL | status.gitlab.com | False | none |  |
| URL | partners.gitlab.com | False | none |  |
| URL | aptly.gitlab.com | False | none |  |
| URL | translate.gitlab.com | False | none |  |
| URL | federal-support.gitlab.com | False | none |  |
| URL | us-federal-gitlab.com | False | none |  |
| URL | ir.gitlab.com | False | none |  |
| URL | levelup.gitlab.com | False | none |  |
| URL | gitlab.biterg.io | False | none | This is a third-party website that aggregates public data from GitLab.com. It is out of scope and the data hosted there is not meant to be confidential. https://contributors.gitlab.com/ redirects to this website. |
| URL | gitlabsandbox.net | False | none |  |
| URL | gitlabdemo.cloud | False | none |  |
| URL | gitlabtraining.cloud | False | none |  |
| URL | packages.gitlab.com | False | none |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/cli/ | False | none | This is a community project that is [now officially maintained by GitLab](https://about.gitlab.com/blog/2022/12/07/introducing-the-gitlab-cli/). It will be in scope at a later time but it is not ready yet. |
| SOURCE_CODE | https://gitlab.com/gitlab-org/opstrace/opstrace-ui | False | none |  |
| SOURCE_CODE | https://gitlab.com/gitlab-org/opstrace/opstrace | False | none |  |
| URL | docs.gitlab.com | False | none |  |
| URL | about.gitlab.com | False | none |  |
| URL | *.gitlab.net | False | none |  |
| URL | *.gitlap.com | False | none |  |
| WILDCARD | *.gitter.im | False | none |  |
| URL | blog.gitter.im | False | none |  |
| URL | update.gitter.im | False | none |  |
| URL | files.gitter.im | False | none |  |
| URL | next.gitter.im | False | none |  |
| URL | beta.gitter.im | False | none |  |
| WILDCARD | ws*.gitter.im | False | none |  |
| URL | api.gitter.im | False | none |  |
| URL | gitlab.net | False | none |  |
| URL | gitlap.com | False | none |  |
