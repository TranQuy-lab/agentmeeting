# STRUCTURED SCOPE — HackerOne (handle: security)
offers_bounties=True submission_state=open

## IN SCOPE / eligible_for_submission=true  (n=57)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| URL | hackerone.com | True | critical | This is our main application that hackers and customers use to interact with each other. It connects with a database that contains information about vulnerability reports, users, and programs. This system’s backend is written in Ruby and exposes data to the client through GraphQL, rendered pages, and JSON endpoints. |
| URL | api.hackerone.com | True | critical | This is our public API that customers use to read and interact with reports. To look for vulnerabilities in this asset, create a sandboxed program, select HackerOne Professional or HackerOne Enterprise in the Product Edition settings page, and create an API token. This system’s backend is written in Ruby, converts the request to a GraphQL query, and serializes the GraphQL result to JSON. |
| URL | www.hackerone.com | True | critical | This is our marketing website. It does not contain any report or customer information. It may store information about hackers, such as information collected through the [penetration tester sign up form](https://www.hackerone.com/hackers/pentest-community-application). The website runs Drupal with a few customizations. |
| URL | app.pullrequest.com | True | critical | Please use your `@wearehackerone.com` email address when signing up. |
| URL | reviewer.pullrequest.com | True | critical | Please use your `@wearehackerone.com` email address when signing up. |
| URL | hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com | True | critical | This is an Amazon S3 bucket that contains attachments of reports and activities. These attachments may contain confidential information. A signed request is required to download an object. |
| URL | www.wearehackerone.com | True | critical |  |
| URL | mta-sts.wearehackerone.com | True | critical |  |
| URL | errors.hackerone.net | True | high | A separate domain that we use to capture information of client and server side exceptions. |
| URL | https://*.hackerone-ext-content.com | True | medium | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | a5s.hackerone-ext-content.com | True | medium | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | b5s.hackerone-ext-content.com | True | medium | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | hackerone-ext-content.com | True | medium | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| URL | https://*.hackerone-user-content.com/ | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object.   |
| URL | ctf.hacker101.com | True | low | The Hacker101 CTF domain, ctf.hacker101.com, is not connected to HackerOne's production environment. It is hosted on Amazon AWS. Users authenticate through HackerOne.com (OAuth). The maximum bounty for any vulnerability on this asset is $500 right now. The CTF challenges itself are not in scope for our bug bounty program. |
| URL | hackathon-photos.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | cover-photos.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | hackathon-photos-us-east-2.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | profile-photos.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | profile-photos-us-east-2.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | cover-photos-us-east-2.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | hackerone.live | True | low |  |
| OTHER | *.vpn.hackerone.net | True | critical | The HackerOne hacker VPN is used by hackers and HackerOne personnel. We'd be most interested in vulnerabilities that allow you to route traffic to other clients (lack of client isolation), routing traffic to internal HackerOne / Amazon networks, and bypassing [sslsplit](https://github.com/droe/sslsplit). Traffic routed through the VPN will originate from `66.232.20.0/23` or `206.166.248.0/23` (HackerOne netblocks). The VPN is based on OpenVPN. |
| OTHER | https://hackerone.com/mcp | True | critical |  |
| OTHER | https://github.com/Hacker0x01/react-datepicker | False | critical |  |
| CIDR | 66.232.20.0/23 | True | critical | This net block is the origin of all traffic routed through the HackerOne hacker VPN. See the description for *.vpn.hackerone.net for the stack and vulnerabilities we're interested in. |
| CIDR | 206.166.248.0/23 | True | critical | This net block is the origin of all traffic routed through the HackerOne hacker VPN. See the description for *.vpn.hackerone.net for the stack and vulnerabilities we're interested in. |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | hackerone.com | False | critical | HackerOne Web Application |
| URL | https://ctf.hacker101.com | True | low | The Hacker101 CTF domain, ctf.hacker101.com, is not connected to HackerOne's production environment. It is hosted on Amazon AWS. Users authenticate through HackerOne.com (OAuth). The maximum bounty for any vulnerability on this asset is $500 right now. The CTF challenges itself are **not** in scope for our bug bounty program. |
| URL | https://reviewer.pullrequest.com | True | critical | Please use your `@wearehackerone.com` email address when signing up. |
| URL | https://app.pullrequest.com | True | critical | Please use your `@wearehackerone.com` email address when signing up. |
| URL | https://hackerone-us-west-2-production-attachments.s3-us-west-2.amazonaws.com/ | True | critical | This is an Amazon S3 bucket that contains attachments of reports and activities. These attachments may contain confidential information. A signed request is required to download an object. |
| OTHER | *.hackerone-ext-content.com | True | medium | This domain is used to serve static marketing assets. No confidential information is stored on these systems. However, it is important to us that these assets cannot be updated by an unauthorized third-party. |
| OTHER | *.hackerone-user-content.com | True | low | This is an Amazon S3 bucket that contains profile and cover photos of users and programs. It does not contain any highly confidential information and would not impact the main application if it would be unreachable. A signed request is required to download an object. |
| URL | http://hackerone.com/graphql | False | critical | HackerOne GraphQL  |
| URL | hackerone-attachments.s3.amazonaws.com | True | critical | This is an Amazon S3 bucket that contains attachments of reports and activities. These attachments may contain confidential information. A signed request is required to download an object.   |

## OUT OF SCOPE / eligible_for_submission=false  (n=16)

| asset_type | asset_identifier | eligible_for_bounty | max_severity | instruction |
|---|---|---|---|---|
| URL | support.hackerone.com | False | none | This asset is hosted by Freshdesk (as of 2023-04-28), and as such these reports should be submitted to the appropriate program: https://hackerone.com/freshworks |
| URL | go.hacker.one | False | none | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | info.hacker.one | False | none | This asset is hosted by Unbounce, and as such these reports should be submitted to them via https://unbounce.com/security/. |
| URL | ma.hacker.one | False | none | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | h1.community | False | none |  |
| URL | www.h1.community | False | none |  |
| URL | www.hackeronestatus.com | False | none | This asset is hosted by Atlassian, and as such these reports should be submitted to their program instead via https://bugcrowd.com/statuspage.  |
| URL | hackerone-swag.com | False | none |  |
| URL | app.qualified.dev | False | none |  |
| URL | qualified.dev | False | none |  |
| URL | https://ma.hacker.one | False | none | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | https://info.hacker.one/ | False | none | This asset is hosted by Unbounce, and as such these reports should be submitted to them via https://unbounce.com/security/. |
| URL | https://www.hackeronestatus.com/ | False | none | This asset is hosted by Atlassian, and as such these reports should be submitted to their program instead via https://bugcrowd.com/statuspage.  |
| URL | https://go.hacker.one | False | none | This asset is hosted by Marketo, and as such these reports should be submitted to them directly. |
| URL | events.hackerone.com | False | none |  |
| URL | hackerone-test.com | False | none |  |
