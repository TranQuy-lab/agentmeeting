# STRUCTURED SCOPE — Cloudflare Public Bug Bounty (handle: cloudflare)
offers_bounties=True submission_state=open

## IN SCOPE / eligible_for_submission=true  (n=55)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| URL | dash.cloudflare.com | True | critical | The Cloudflare dashboard (https://dash.cloudflare.com/) and any direct calls from the dashboard to other Cloudflare owned resources are considered in scope. |
| URL | cloudflareworkers.com | True | critical | This is a Cloudflare Workers test site. Cloudflare Workers provides a lightweight JavaScript execution environment that allows developers to augment existing applications or create entirely new ones without configuring or maintaining infrastructure. https://www.cloudflare.com/products/cloudflare-workers/ |
| URL | *.teams.cloudflare.com | True | critical |  |
| URL | api.cloudflare.com | True | critical |  |
| URL | *.cloudflare.com | True | critical | Excluding support.cloudflare.com, community.cloudflare.com and other SaaS applications |
| URL | http://github.com/cloudflare | True | critical | - |
| URL | one.dash.cloudflare.com | True | critical |  |
| SOURCE_CODE | https://github.com/cloudflare/workerd | True | critical |  |
| SOURCE_CODE | https://github.com/cloudflare/vinext | True | critical |  The Next.js API surface, reimplemented on Vite. Experimental — under heavy development. Triage may delay for this repo as we will be assessing for duplicates. |
| OTHER | Cloudflare Pages | True | critical | https://developers.cloudflare.com/pages |
| OTHER | CDNJS | True | critical | CDNJS is a free and open source project to organize and provide popular front-end web development resources to developers via a fast CDN infrastructure without usage limitations and fees.  https://github.com/cdnjs/cdnjs https://blog.cloudflare.com/an-update-on-cdnjs/ |
| OTHER | WARP Mobile Apps | True | critical | Download on Android: https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone Download on iOS: https://itunes.apple.com/us/app/1-1-1-1-faster-internet/id1423538627 WARP is a free VPN for mobile phones. The app can be used as a 1.1.1.1 DNS resolver or VPN or our premium paid service Warp+. It works on wireguard protocol. See documentation section for more details. Areas of interest: Can other apps snoop with Warp Downgrade of connections Misconfiguration in the apps or backend MITM attacks  Out of scope: Using WARP+ features without paying |
| OTHER | Cloudflare Access | True | critical | Cloudflare Access is an application that controls access to your sites and integrates with social and enterprise identity providers (IdP) for managing user credentials.  https://www.cloudflare.com/products/cloudflare-access/   |
| OTHER | Stream | True | critical | Cloudflare Stream is an easy-to-use, affordable, on-demand video streaming platform. Stream seamlessly integrates video storage, encoding, and a customizable player with Cloudflare’s fast, secure, and reliable global network.  https://www.cloudflare.com/products/cloudflare-stream/ |
| OTHER | 1.1.1.1 Resolver | True | critical |  A blazing fast DNS resolver built for private browsing. https://1.1.1.1/ https://developers.cloudflare.com/1.1.1.1/what-is-1.1.1.1/ https://developers.cloudflare.com/1.1.1.1/setting-up-1.1.1.1/ |
| OTHER | Magic Transit | True | critical | Magic Transit is a software-defined networking product that offers IP transit with DDoS protection, next-gen firewall, traffic acceleration and more for your on-premise and data center networks from a single, easy-to-use interface.  https://www.cloudflare.com/magic-transit/ |
| OTHER | Spectrum | True | critical |  Spectrum extends the power of Cloudflare's DDoS, TLS, and IP Firewall to TCP and UDP-based services, keeping them online and secure. https://www.cloudflare.com/products/cloudflare-spectrum/ |
| OTHER | Load Balancing | True | critical |  Cloudflare's Load Balancing automatically reduces latency by directing visitors to infrastructure closest to them.  https://www.cloudflare.com/load-balancing/ |
| OTHER | Bot Management | True | critical | Cloudflare enables you to manage bots with speed and accuracy by applying several detection methods: Behavioral analysis, machine learning, and fingerprinting. https://www.cloudflare.com/products/bot-management/ |
| OTHER | Cloudflare Zero Trust/Cloudflare One | True | critical |  |
| OTHER | Open source tools from Cloudflare | True | critical | https://github.com/cloudflare |
| OTHER | Area 1 | True | critical |  |
| OTHER | Cloudflare D1 | True | critical | https://blog.cloudflare.com/introducing-d1/ |
| OTHER | Cloudflare R2 | True | critical | https://blog.cloudflare.com/r2-open-beta/ |
| OTHER | WARP desktop client | True | critical | Cloudflare Zero Trust client applications releases on Windows, Linux and MacOS |
| OTHER | *.cloudflarepartners.com | True | critical |  |
| OTHER | Cloudflare DNS | True | critical |  |
| OTHER | Cloudflare CASB | True | critical | Cloudflare's cloud access security broker (CASB) service gives comprehensive visibility and control over SaaS apps, so you can easily prevent data leaks and compliance violations. With Zero Trust security, block insider threats, Shadow IT, risky data sharing, and bad actors. https://www.cloudflare.com/products/zero-trust/casb/ |
| OTHER | Workers | True | critical | https://developers.cloudflare.com/workers/ |
| OTHER | Cloudflare Tunnel | True | critical | Cloudflare Tunnel offers an easy way to expose web servers securely to the internet, without opening up firewall ports and configuring ACLs.  https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/   |
| OTHER | AMP Real URL | True | critical | https://developers.cloudflare.com/speed/optimization/other/amp-real-url/ |
| OTHER | Cloudflare Cache  | True | critical | https://developers.cloudflare.com/cache/ |
| OTHER | Magic Firewall | True | critical | https://developers.cloudflare.com/magic-firewall/ |
| OTHER | Cloudflare Zaraz | True | critical | https://developers.cloudflare.com/zaraz/ |
| OTHER | China Network | True | critical | https://developers.cloudflare.com/china-network/ |
| OTHER | API Shield | True | critical | https://developers.cloudflare.com/api-shield/ |
| OTHER | Gateway | True | critical | https://developers.cloudflare.com/cloudflare-one/policies/gateway/ |
| OTHER | Browser Isolation | True | critical | https://developers.cloudflare.com/cloudflare-one/policies/browser-isolation/ |
| OTHER | AI Gateway | True | critical | https://developers.cloudflare.com/ai-gateway/ |
| OTHER | Vectorize | True | critical | https://developers.cloudflare.com/vectorize/ |
| OTHER | Hyperdrive | True | critical | https://developers.cloudflare.com/hyperdrive/ |
| OTHER | Workers KV | True | critical | https://developers.cloudflare.com/kv/ |
| OTHER | Cloudflare Analytics | True | critical | https://developers.cloudflare.com/analytics/ |
| OTHER | Cloudflare Durable Objects | True | critical | https://developers.cloudflare.com/durable-objects/ |
| OTHER | Waiting Room | True | critical | https://developers.cloudflare.com/waiting-room/ |
| OTHER | Magic WAN | True | critical | https://developers.cloudflare.com/magic-wan/ |
| OTHER | Data Loss Prevention (DLP) | True | critical | https://developers.cloudflare.com/cloudflare-one/policies/data-loss-prevention/ |
| OTHER | SSL/TLS | True | critical | https://developers.cloudflare.com/ssl/ |
| OTHER | Cloudflare Workers CI | True | critical |  |
| OTHER | Images | True | none | https://developers.cloudflare.com/speed/optimization/images/#image-optimization |
| AI_MODEL | Workers AI | True | critical | Reports on Prompt Injection attacks on models hosted by Workers AI without demonstrating an impact on Cloudflare will not be accepted.  |
| OTHER | Durable Objects | True | none | https://developers.cloudflare.com/durable-objects/ |
| OTHER | Argo Tunnel | True | critical | Cloudflare Tunnel offers an easy way to expose web servers securely to the internet, without opening up firewall ports and configuring ACLs.  https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/ |
| URL | dash.teams.cloudflare.com | True | critical | Secondary scope. |
| URL | http://cloudflare.com/apps/ | True | critical | This is the Cloudflare Marketplace. Only the platform itself and first-party apps (those created by Cloudflare) are considered in scope. |

## OUT OF SCOPE / eligible_for_submission=false  (n=28)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| WILDCARD | *.plugins.realtime.cloudflare.com | False | none |  |
| URL | support.cloudflare.com | False | none | This asset is hosted by Zendesk, and as such these reports should be submitted to their program instead via @Zendesk |
| URL | community.cloudflare.com | False | none |  |
| URL | support.cloudflarewarp.com | False | none | This asset is hosted by Zendesk, and as such these reports should be submitted to their program instead via @zendesk. |
| URL | waf.cumulusfire.net | False | none | This domain must be used for testing WAF bypasses. |
| URL | events.www.cloudflare.com | False | none |  |
| URL | demo.realtime.cloudflare.com | False | none |  |
| URL | api.staging.realtime.cloudflare.com | False | none |  |
| URL | examples.realtime.cloudflare.com | False | none |  |
| URL | react-examples.realtime.cloudflare.com | False | none |  |
| URL | app.dyte.io | False | none |  |
| URL | test.realtime.cloudflare.com | False | none |  |
| URL | files.plugins.realtime.cloudflare.com | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/vinext-private | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/moq-rs | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/privacy-gateway-server-go | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/saffron.git | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/realtimekit-web-examples  | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/recapn | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/computer | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/cloudflare-os | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/templates | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/pp-browser-extension | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/agentic-inbox | False | none |  |
| SOURCE_CODE | https://github.com/cloudflare/cf | False | none |  |
| OTHER | Turnstile | False | none | https://developers.cloudflare.com/turnstile/ |
| OTHER | 172.65.0.0/16  | False | none | These are customer applications protected by Cloudflare Spectrum, hence out of scope |
| SOURCE_CODE | https://github.com/cloudflare/wirefilter/ | False | none |  |
