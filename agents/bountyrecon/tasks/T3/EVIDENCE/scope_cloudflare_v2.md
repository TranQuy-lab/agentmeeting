# STRUCTURED SCOPE v2 (có `archived_at`) — Cloudflare Public Bug Bounty (handle `cloudflare`)

**Ngày chụp:** `2026-10-01T15:28:34Z` (UTC) · **Nguồn:** `POST https://hackerone.com/graphql` (công khai, không auth)
**Quan hệ với bản gốc:** đây là **BẢN CHỤP LẠI** theo `D-026` phương án (a).
Bản gốc `scope_cloudflare.md` **KHÔNG bị sửa, KHÔNG bị xoá** — vẫn là bằng chứng pháp lý cho thời điểm chụp gốc `2026-10-01`.

> ⛔ **GIỚI HẠN (D-026, KHÔNG được vượt):** cột `archived_at` cho biết bản ghi **đã nghỉ hưu hay chưa**. **KHÔNG** được suy ra 'ngoài scope'. Chỉ được khẳng định: bảng thiếu chiều này thì **KHÔNG PHÂN BIỆT ĐƯỢC**.
> ❗ **`DISSENT-12` vẫn MỞ:** ngữ nghĩa `eligible_for_submission=True` trên bản ghi `archived_at != None` **chưa có định nghĩa chính thức**. Ghi hiện tượng, KHÔNG kết luận ngữ nghĩa.

**Thống kê tự đo:** `archived:false` = **78** scope (sub=True **51**) · `archived:true` = **5** scope (sub=True **4**) · TỔNG **83**

## archived=false (đang hiệu lực) — n=78

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| URL | dash.cloudflare.com | True | True | critical | `None` | The Cloudflare dashboard (https://dash.cloudflare.com/) and any direct calls from the dashboard to other Cloudflare owned resources are considered in scope. |
| URL | cloudflareworkers.com | True | True | critical | `None` | This is a Cloudflare Workers test site. Cloudflare Workers provides a lightweight JavaScript execution environment that allows developers to augment existing applications or create entirely new ones without configuring or maintaining infrastructure. https://www.cloudflare.com/products/cloudflare-workers/ |
| URL | *.teams.cloudflare.com | True | True | critical | `None` |  |
| URL | api.cloudflare.com | True | True | critical | `None` |  |
| URL | *.cloudflare.com | True | True | critical | `None` | Excluding support.cloudflare.com, community.cloudflare.com and other SaaS applications |
| URL | http://github.com/cloudflare | True | True | critical | `None` | - |
| URL | one.dash.cloudflare.com | True | True | critical | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/workerd | True | True | critical | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/vinext | True | True | critical | `None` |  The Next.js API surface, reimplemented on Vite. Experimental — under heavy development. Triage may delay for this repo as we will be assessing for duplicates. |
| OTHER | Cloudflare Pages | True | True | critical | `None` | https://developers.cloudflare.com/pages |
| OTHER | CDNJS | True | True | critical | `None` | CDNJS is a free and open source project to organize and provide popular front-end web development resources to developers via a fast CDN infrastructure without usage limitations and fees.  https://github.com/cdnjs/cdnjs https://blog.cloudflare.com/an-update-on-cdnjs/ |
| OTHER | WARP Mobile Apps | True | True | critical | `None` | Download on Android: https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone Download on iOS: https://itunes.apple.com/us/app/1-1-1-1-faster-internet/id1423538627 WARP is a free VPN for mobile phones. The app can be used as a 1.1.1.1 DNS resolver or VPN or our premium paid service Warp+. It works on wireguard protocol. See documentation section for more details. Areas of |
| OTHER | Cloudflare Access | True | True | critical | `None` | Cloudflare Access is an application that controls access to your sites and integrates with social and enterprise identity providers (IdP) for managing user credentials.  https://www.cloudflare.com/products/cloudflare-access/   |
| OTHER | Stream | True | True | critical | `None` | Cloudflare Stream is an easy-to-use, affordable, on-demand video streaming platform. Stream seamlessly integrates video storage, encoding, and a customizable player with Cloudflare’s fast, secure, and reliable global network.  https://www.cloudflare.com/products/cloudflare-stream/ |
| OTHER | 1.1.1.1 Resolver | True | True | critical | `None` |  A blazing fast DNS resolver built for private browsing. https://1.1.1.1/ https://developers.cloudflare.com/1.1.1.1/what-is-1.1.1.1/ https://developers.cloudflare.com/1.1.1.1/setting-up-1.1.1.1/ |
| OTHER | Magic Transit | True | True | critical | `None` | Magic Transit is a software-defined networking product that offers IP transit with DDoS protection, next-gen firewall, traffic acceleration and more for your on-premise and data center networks from a single, easy-to-use interface.  https://www.cloudflare.com/magic-transit/ |
| OTHER | Spectrum | True | True | critical | `None` |  Spectrum extends the power of Cloudflare's DDoS, TLS, and IP Firewall to TCP and UDP-based services, keeping them online and secure. https://www.cloudflare.com/products/cloudflare-spectrum/ |
| OTHER | Load Balancing | True | True | critical | `None` |  Cloudflare's Load Balancing automatically reduces latency by directing visitors to infrastructure closest to them.  https://www.cloudflare.com/load-balancing/ |
| OTHER | Bot Management | True | True | critical | `None` | Cloudflare enables you to manage bots with speed and accuracy by applying several detection methods: Behavioral analysis, machine learning, and fingerprinting. https://www.cloudflare.com/products/bot-management/ |
| OTHER | Cloudflare Zero Trust/Cloudflare One | True | True | critical | `None` |  |
| OTHER | Open source tools from Cloudflare | True | True | critical | `None` | https://github.com/cloudflare |
| OTHER | Area 1 | True | True | critical | `None` |  |
| OTHER | Cloudflare D1 | True | True | critical | `None` | https://blog.cloudflare.com/introducing-d1/ |
| OTHER | Cloudflare R2 | True | True | critical | `None` | https://blog.cloudflare.com/r2-open-beta/ |
| OTHER | WARP desktop client | True | True | critical | `None` | Cloudflare Zero Trust client applications releases on Windows, Linux and MacOS |
| OTHER | *.cloudflarepartners.com | True | True | critical | `None` |  |
| OTHER | Cloudflare DNS | True | True | critical | `None` |  |
| OTHER | Cloudflare CASB | True | True | critical | `None` | Cloudflare's cloud access security broker (CASB) service gives comprehensive visibility and control over SaaS apps, so you can easily prevent data leaks and compliance violations. With Zero Trust security, block insider threats, Shadow IT, risky data sharing, and bad actors. https://www.cloudflare.com/products/zero-trust/casb/ |
| OTHER | Workers | True | True | critical | `None` | https://developers.cloudflare.com/workers/ |
| OTHER | Cloudflare Tunnel | True | True | critical | `None` | Cloudflare Tunnel offers an easy way to expose web servers securely to the internet, without opening up firewall ports and configuring ACLs.  https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/   |
| OTHER | AMP Real URL | True | True | critical | `None` | https://developers.cloudflare.com/speed/optimization/other/amp-real-url/ |
| OTHER | Cloudflare Cache  | True | True | critical | `None` | https://developers.cloudflare.com/cache/ |
| OTHER | Magic Firewall | True | True | critical | `None` | https://developers.cloudflare.com/magic-firewall/ |
| OTHER | Cloudflare Zaraz | True | True | critical | `None` | https://developers.cloudflare.com/zaraz/ |
| OTHER | China Network | True | True | critical | `None` | https://developers.cloudflare.com/china-network/ |
| OTHER | API Shield | True | True | critical | `None` | https://developers.cloudflare.com/api-shield/ |
| OTHER | Gateway | True | True | critical | `None` | https://developers.cloudflare.com/cloudflare-one/policies/gateway/ |
| OTHER | Browser Isolation | True | True | critical | `None` | https://developers.cloudflare.com/cloudflare-one/policies/browser-isolation/ |
| OTHER | AI Gateway | True | True | critical | `None` | https://developers.cloudflare.com/ai-gateway/ |
| OTHER | Vectorize | True | True | critical | `None` | https://developers.cloudflare.com/vectorize/ |
| OTHER | Hyperdrive | True | True | critical | `None` | https://developers.cloudflare.com/hyperdrive/ |
| OTHER | Workers KV | True | True | critical | `None` | https://developers.cloudflare.com/kv/ |
| OTHER | Cloudflare Analytics | True | True | critical | `None` | https://developers.cloudflare.com/analytics/ |
| OTHER | Cloudflare Durable Objects | True | True | critical | `None` | https://developers.cloudflare.com/durable-objects/ |
| OTHER | Waiting Room | True | True | critical | `None` | https://developers.cloudflare.com/waiting-room/ |
| OTHER | Magic WAN | True | True | critical | `None` | https://developers.cloudflare.com/magic-wan/ |
| OTHER | Data Loss Prevention (DLP) | True | True | critical | `None` | https://developers.cloudflare.com/cloudflare-one/policies/data-loss-prevention/ |
| OTHER | SSL/TLS | True | True | critical | `None` | https://developers.cloudflare.com/ssl/ |
| OTHER | Cloudflare Workers CI | True | True | critical | `None` |  |
| OTHER | Images | True | True | none | `None` | https://developers.cloudflare.com/speed/optimization/images/#image-optimization |
| AI_MODEL | Workers AI | True | True | critical | `None` | Reports on Prompt Injection attacks on models hosted by Workers AI without demonstrating an impact on Cloudflare will not be accepted.  |
| WILDCARD | *.plugins.realtime.cloudflare.com | False | False | none | `None` |  |
| URL | support.cloudflare.com | False | False | none | `None` | This asset is hosted by Zendesk, and as such these reports should be submitted to their program instead via @Zendesk |
| URL | community.cloudflare.com | False | False | none | `None` |  |
| URL | support.cloudflarewarp.com | False | False | none | `None` | This asset is hosted by Zendesk, and as such these reports should be submitted to their program instead via @zendesk. |
| URL | waf.cumulusfire.net | False | False | none | `None` | This domain must be used for testing WAF bypasses. |
| URL | events.www.cloudflare.com | False | False | none | `None` |  |
| URL | demo.realtime.cloudflare.com | False | False | none | `None` |  |
| URL | api.staging.realtime.cloudflare.com | False | False | none | `None` |  |
| URL | examples.realtime.cloudflare.com | False | False | none | `None` |  |
| URL | react-examples.realtime.cloudflare.com | False | False | none | `None` |  |
| URL | app.dyte.io | False | False | none | `None` |  |
| URL | test.realtime.cloudflare.com | False | False | none | `None` |  |
| URL | files.plugins.realtime.cloudflare.com | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/vinext-private | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/moq-rs | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/privacy-gateway-server-go | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/saffron.git | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/realtimekit-web-examples  | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/recapn | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/computer | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/cloudflare-os | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/templates | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/pp-browser-extension | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/agentic-inbox | False | False | none | `None` |  |
| SOURCE_CODE | https://github.com/cloudflare/cf | False | False | none | `None` |  |
| OTHER | Turnstile | False | False | none | `None` | https://developers.cloudflare.com/turnstile/ |
| OTHER | 172.65.0.0/16  | False | False | none | `None` | These are customer applications protected by Cloudflare Spectrum, hence out of scope |

## archived=true (đã nghỉ hưu) — n=5

| asset_type | asset_identifier | eligible_submission | eligible_bounty | max_severity | **archived_at** | instruction |
|---|---|---|---|---|---|---|
| SOURCE_CODE | https://github.com/cloudflare/wirefilter/ | False | False | none | `2026-08-21T10:46:26.424Z` |  |
| OTHER | Durable Objects | True | True | none | `2023-10-26T15:40:54.533Z` | https://developers.cloudflare.com/durable-objects/ |
| OTHER | Argo Tunnel | True | True | critical | `2023-10-26T15:25:05.200Z` | Cloudflare Tunnel offers an easy way to expose web servers securely to the internet, without opening up firewall ports and configuring ACLs.  https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/ |
| URL | dash.teams.cloudflare.com | True | True | critical | `2023-05-08T10:11:33.083Z` | Secondary scope. |
| URL | http://cloudflare.com/apps/ | True | True | critical | `2023-03-01T17:47:43.944Z` | This is the Cloudflare Marketplace. Only the platform itself and first-party apps (those created by Cloudflare) are considered in scope. |

