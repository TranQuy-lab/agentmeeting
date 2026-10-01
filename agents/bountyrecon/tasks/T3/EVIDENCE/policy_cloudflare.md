# Our Values
Cloudflare appreciates the work of security researchers and takes security, trust, and transparency seriously. This program was developed to make vulnerability reporting easier and to recognize the efforts of all people striving to help make the Internet a better place.

If you believe you have found a security vulnerability that could impact Cloudflare or our users, we encourage you to inform us right away. We will investigate all legitimate reports and do our best to quickly fix the problem.

# What we expect from you
By participating in this program, you agree to the following program rules and guidelines in addition to HackerOne's [Disclosure Guidelines](https://www.hackerone.com/disclosure-guidelines). Failure to follow these rules will lead to disqualification from the Cloudflare Bug Bounty program.

## Program Rules
* You must make a good faith effort to avoid privacy violations, destruction of data and interruption or degradation of Cloudflare’s services and products during your research.
* All attacks must be executed against your own Cloudflare Account. You can sign up for a free Cloudflare account and use it for testing.
    * Accounts should be created with a `@wearehackerone.com` email address.
* Do not perform tests against customers of Cloudflare. 
* Once you find a vulnerability, report it and reach out to us before you use the vulnerability to pivot across multiple in-scope assets.
* Make sure that scanners have a narrow scope set that is [limited to authorized Cloudflare IPs only](https://cloudflare.com/ips). Aggressive, overly broad scans or those which include Cloudflare customer IPs without permission will be considered tests against Cloudflare customers.
* Do not send unsolicited bulk messages (spam) or unauthorized messages.
* Do not knowingly post, transmit, upload, link to, or send any program or script that might be considered malicious.
* If your report is the product of collaboration, please add your collaborators _before the bounty_ is awarded.

Any of the activities below will result in disqualification from the program permanently:
* Testing against Cloudflare customers, partners, service providers, suppliers, or vendors
* Social engineering of Cloudflare employees/contractors, including but not limited to: pre-authenticated clickjacking, phishing, impersonating Cloudflare in emails or convincing customer support to do something on behalf of another user
* Physical attacks against Cloudflare employees/contractors, offices, or data centers
* Executing Denial of Service attacks against Cloudflare
* Publishing, blogging, presenting, or otherwise publicly disclosing a report or its details within 90 days of submission without prior written approval from Cloudflare. This includes social media posts, conference talks, blog articles, YouTube videos, and any other public channel. Researchers who wish to disclose should coordinate with us per the Disclosure section below.

## Submitting a report
When submitting a report, we expect that researchers:

- Provide detailed reports with reproducible steps. If the report is not detailed enough to reproduce the issue, the issue will not be eligible for a reward.
- Provide a realistic attack scenario including prerequisites for an attack and expected gains after the exploitation. Reports without such a scenario, with unrealistic assumptions, or without meaningful outcomes will not be eligible for reward.
- Submit one vulnerability per report, unless you need to chain vulnerabilities in order to demonstrate impact.
- Avoid salami-style reporting of multiple reports. If you identify the same vulnerability on a subset of our products or multiple similar vulnerabilities on the same products, please submit one holistic report.
- Do not store any Cloudflare IP or PII information once the report is submitted.

### Report Quality Requirements

Submitting high-quality reports is highly encouraged and will speed up the triage and award process. Reports that are low quality and unclear will be closed. Please address the following in your report:

- **Affected asset:** Exact product, domain, repository, file, commit, package version, or endpoint.
- **Description of the problem:** What the vulnerability is and how it works.
- **Security boundary:** What trust boundary is crossed and why the attacker should not have that access.
- **Attacker model:** Required privileges, prior access, approval status, account type, network position, and user interaction.
- **Steps to reproduce or Proof of Concept:** Clear, reproducible steps using only authorized accounts and assets.
- **Impact:** What data, actions, or secrets are accessed or modified.
- **Default relevance:** Whether the issue affects default or documented configuration, or requires unusual setup.
- **Production relevance:** Whether impact is shown in Cloudflare production, a supported product, or only a local, demo, or test environment.
- **Safety:** Confirmation that no testing was performed against Cloudflare customers, partners, vendors, employees, or third parties.
- **Public knowledge:** Whether knowledge of this issue is currently public.

Reports that do not clearly identify the affected asset, security boundary, attacker prerequisites, reproduction steps, and meaningful impact may be closed as Informational or Not Applicable. Cloudflare reserves the right to fix hardening issues without awarding a bounty when the report does not demonstrate a bounty-eligible security impact.

### Proof of Concept Requirement

**A working Proof of Concept is required for all bounty-eligible reports. No PoC, no bounty.** Theoretical vulnerability descriptions, source-code-only analysis, static-analysis findings, or speculative attack narratives without a demonstrated reproduction are not eligible for bounty regardless of the claimed severity. "I can provide a PoC if needed" or "please confirm I am allowed to test" is not a PoC. The PoC must be included with the initial submission or provided promptly upon request. Reports submitted without a PoC may be closed without waiting for one to be produced.

Acceptable PoC formats include: curl commands, scripts (Python, Bash, JavaScript, etc.), step-by-step browser reproduction, video recordings with visible requests and responses, or any other format that allows independent reproduction. The PoC must use only the researcher's own accounts and authorized test assets.

**PoC readability requirement:** Proofs of concept must be human-readable and independently verifiable by a security engineer without requiring specialized tooling, deobfuscation, or reverse engineering of the PoC itself. Researchers are welcome to use AI tools to assist in composing their reports, but the PoC code must be clear, commented where non-obvious, and written so that a reviewer can read the script and understand what each step does before running it. Minified, obfuscated, or unnecessarily complex PoC scripts that obscure the attack logic will be sent back for clarification. A good PoC should be short enough to read in under five minutes and should clearly separate setup steps from the exploit trigger. When in doubt, prefer a simple curl command or a short self-contained script over a multi-file framework.

**PoC environment tiers and their impact on severity:**

Not all reproduction environments carry equal weight. The environment in which a vulnerability is demonstrated directly affects the severity assessment and bounty eligibility:

| Tier | Environment | Severity Impact | Examples |
|------|-------------|-----------------|----------|
| **Production** | Cloudflare-operated production services, live customer-facing endpoints, production APIs | Full severity per bounty table | `api.cloudflare.com`, `dash.cloudflare.com`, `*.mcp.cloudflare.com`, `1.1.1.1`, production Workers on `*.workers.dev` serving real traffic |
| **Staging / Internal** | Cloudflare-operated staging, internal tooling, or pre-production environments | Full severity if data or access is real; reduced if test-only | `*.staging.cloudflare.com`, `*.cfdata.org` internal services, staging API endpoints |
| **Researcher-deployed on Cloudflare** | Researcher's own Worker, Durable Object, or Pages project deployed on Cloudflare's managed infrastructure | Eligible if it demonstrates a library or platform-level flaw; severity based on demonstrated cross-client or cross-session impact | Researcher's own Pages deployment triggering a framework bug |
| **Local / standalone** | Local Docker, standalone Node.js, `wrangler dev`, self-hosted environments with no Cloudflare runtime constraints | Informational unless the same code path is shown to be reachable in production with equivalent impact | Docker container running OSS libraries with no memory limits, local workerd build, `wrangler dev` localhost |
| **Source-code-only** | Static analysis, code review, theoretical analysis without any running reproduction | Informational regardless of claimed severity | "This function doesn't validate input" without demonstrating reachability or impact |

Researchers are encouraged to demonstrate findings at the highest applicable tier. A PoC that demonstrates a valid code-level issue may be upgraded if the researcher subsequently provides a  reproduction showing production-context impact (for example, cross-client degradation on a shared Durable Object). 

---

### Leaked Credentials, Passwords, and Tokens

Cloudflare appreciates reports of leaked credentials and secrets, but not all credential reports are bounty eligible.

**Not eligible for bounty:**

- Passwords, username/password combinations, session dumps, cookies, or credential material found on breach forums, paste sites, dark web marketplaces, stealer-log dumps, Telegram channels, Discord servers, or other third-party leak sources.
- Reports that rely on validating leaked employee, customer, partner, or third-party credentials by attempting to log in.
- Reports containing credentials for non-Cloudflare systems, customer systems, vendor systems, or partner systems, unless Cloudflare explicitly owns and operates the affected system.
- Reports that only show that a password or token-looking string exists, without demonstrating that it is a live Cloudflare-owned secret and without safe evidence of impact.
- Reposts, recycled dumps, credential stuffing datasets, or previously public leaked credentials.

**Potentially eligible for bounty:**

- Live Cloudflare-owned API tokens, service account keys, private keys, signing secrets, deploy tokens, GitHub tokens, package registry tokens, or production credentials accidentally committed to a public repository controlled by Cloudflare.


**Rules for credential reports:**

- Do not attempt to authenticate with leaked credentials.
- Do not access non-public systems or data.
- Submit the credential value, source URL, commit hash, file path, and safe evidence showing why the secret appears to be Cloudflare-owned.
- Cloudflare will validate the credential internally. Attempting to validate credentials yourself may make the report ineligible.

---

### GitHub Actions, CI/CD, and Workflow Reports

Reports involving GitHub Actions, CI/CD pipelines, repository automation, or workflow tokens must demonstrate a direct security boundary bypass and reproducible impact without relying on maintainer approval or trusted human action.

**Not eligible for bounty:**

- Issues requiring a maintainer, employee, reviewer, or bot operator to approve a workflow run, label a PR, merge a PR, approve a deployment, approve a GitHub Actions run, or otherwise grant trust before exploitation.
- Issues requiring the researcher to first become a trusted contributor, prior contributor, collaborator, organization member, maintainer, or approved workflow runner, unless the report also demonstrates an independent vulnerability that grants that status.
- Reports where the only impact is modification of the researcher's own fork, branch, pull request, or artifacts.
- Reports where the only impact is comments, labels, check output, preview output, or bot messages on the researcher's own PR, unless a meaningful security impact beyond spam or content injection is demonstrated.
- Reports that rely on untrusted code execution in a low-privilege `pull_request` workflow without showing that secrets, write tokens, protected branches, deployments, or Cloudflare-owned systems are reachable.
- Reports that rely on malicious changes being merged after normal manual or automated review.
- Reports where the claimed exploit requires social engineering maintainers, reviewers, employees, or contributors.

**Potentially eligible for bounty:**

- Reproducible CI/CD issues that allow an external attacker, without maintainer approval, to execute code in a privileged workflow context with access to secrets or write-scoped tokens.
- Artifact poisoning, cache poisoning, workflow injection, or `pull_request_target`/`workflow_run` issues that cross from untrusted PR input into a privileged context and expose secrets, allow protected-branch modification, publish packages, deploy services, or modify Cloudflare-owned production assets.
- Issues allowing unauthorized modification of another user's PR branch or repository branch without required approval, if the modified branch is Cloudflare-controlled and the impact is more than cosmetic.

**Severity guidance:**

- Direct write access to protected branches, package publishing, deployment, or production secret exposure may qualify as High or Critical depending on impact.

---

### Developer Tools, CLIs, Build Systems, and Project-Controlled Files

Developer tools often execute project-controlled code by design. Reports must show a new security boundary bypass beyond the normal risk of running tools in an untrusted project.

**Not eligible for bounty:**

- Command execution requiring attacker control of `package.json`, lockfiles, build scripts, project configuration, npm scripts, package-manager hooks, local plugins, or repository files where the victim must run developer tooling inside that attacker-controlled project.
- Reports where the only impact is that malicious project files execute code when a developer runs install, build, test, or init commands in the project.
- Reports requiring a developer to clone and run commands in an untrusted repository without demonstrating impact beyond ordinary malicious-repository execution.
- Dependency confusion or package hijacking claims without proof that Cloudflare-controlled automation, production systems, or developers install the malicious package from an attacker-controlled namespace.
- VS Code workspace trust bypass claims where the developer has explicitly trusted the workspace.

**Potentially eligible for bounty:**

- Developer-tool vulnerabilities that execute attacker code when processing untrusted input that is not expected to be executable project code, such as a file upload, remote template, package metadata, archive, or URL.
- Issues where Cloudflare automation automatically processes untrusted projects or templates in a privileged environment without normal developer trust decisions.
- Vulnerabilities in official Cloudflare tooling that can be exploited remotely or through standard product workflows without requiring the victim to run commands in an attacker-controlled repository.
- Debug port or inspector exposure that is exploitable from a malicious webpage via WebSocket (which is not subject to browser Same-Origin Policy for localhost connections) without requiring the developer to opt into network exposure.

---

### Local Access, Physical Access, and Same-Machine Attacks

Local access significantly limits security impact and is often out of scope unless a strong privilege boundary is crossed.

**Not eligible for bounty:**

- Attacks requiring physical access to a user's device.
- Attacks requiring local authenticated access where no privilege escalation, cross-user data access, protected secret exposure, or meaningful product security boundary bypass is demonstrated.
- Issues where the attacker can already perform equivalent or greater actions with the required local access (for example, reading diagnostic logs that contain no sensitive data beyond what the attacker can already observe through standard OS tools).
- Local denial-of-service against the attacker's own device or account.

**Potentially eligible for bounty:**

- Local non-admin to admin/SYSTEM privilege escalation in Cloudflare software (for example, command injection via IPC from an unprivileged local user to a SYSTEM-privileged Cloudflare service).
- Cross-user information disclosure where a low-privileged local user can access another user's Cloudflare-managed secrets, credentials, or sensitive data despite OS access controls.
- Local issues that expose Cloudflare Zero Trust credentials, device posture secrets, private keys, session tokens, or other high-value secrets not otherwise accessible to the local attacker.

**Special note on local privilege escalation reports:**

Local privilege escalation (LPE) reports in Cloudflare client software (such as WARP, cloudflared, or other desktop/mobile agents) must meet a high evidence bar due to the inherent complexity of local attack surfaces:

- The PoC must demonstrate a complete, end-to-end privilege escalation from a non-administrative user to admin, SYSTEM, root, or equivalent, without relying on pre-existing elevated access for any step other than initial test-environment setup.
- The report must clearly separate setup steps (which may require elevation for test configuration) from exploitation steps (which must run as the unprivileged attacker).
- Reports claiming LPE through debug ports, named pipes, IPC, or service communication channels must demonstrate that the channel is reachable from the claimed unprivileged context and that the escalation is not gated behind authentication, authorization, or platform security controls that the PoC bypasses only through test-environment configuration.
- Cloudflare reserves the right to adjust severity based on production-environment constraints, platform-specific mitigations (such as endpoint protection, application allowlisting, or managed device policies), and real-world exploitability in enterprise deployment contexts.

---

### Demo, Example, Test, Playground, and Proof-of-Concept Applications

Demo and example applications are not production services unless explicitly listed as in scope. Before submitting a report against a demo, example, or playground application, please check the project's README and any deployment documentation for disclaimers regarding its intended use, security posture, and production status.

**Not eligible for bounty:**

- Issues only affecting demos, examples, sample apps, playgrounds, tutorial code, test harnesses, local development servers, mock services, or proof-of-concept deployments.
- Issues reproduced only in `wrangler dev`, localhost, test fixtures, mock services, or synthetic examples without showing impact against a Cloudflare production service or supported product configuration.
- Reports where the only affected asset is an example application intended to demonstrate functionality, not to provide production security guarantees.
- XSS, injection, or authentication issues in example code that is not deployed as a Cloudflare-operated production service, even if the example is deployable via "Deploy to Workers" or similar one-click mechanisms.

**Potentially eligible for bounty:**

- Issues in demo or example code that are also present in the production Cloudflare stack or in a supported production product.
- Vulnerabilities in widely distributed Cloudflare libraries or templates where the insecure pattern is documented for production use and creates a real security boundary failure in consumer deployments.

---

### Open Source Libraries, Frameworks, and Templates

Open source reports must demonstrate security impact in a supported or realistic deployment, not just isolated source-level behavior. Before submitting a report against a Cloudflare open-source repository, please review the project's README, security model documentation, and any stated disclaimers regarding usage, maturity, deployment context, and known limitations. Many repositories document their intended deployment model, security boundaries, and experimental status. Reports that conflict with documented design decisions, known limitations, or explicitly stated security assumptions may be closed without bounty.

**Not eligible for bounty:**

- Pure API incompatibilities, standards deviations, or missing hardening in open source projects without demonstrated security impact.
- Issues requiring a consumer application to misuse the library in an obviously unsafe way.
- Reports only affecting self-hosted or local deployments where Cloudflare production or documented production usage is not impacted.
- Reports against abandoned, experimental (version 0.x), internal-only, test-only, or demo-only code unless Cloudflare confirms production use.
- IETF interop endpoints, draft-protocol reference implementations, alpha/preview products, and endpoints operated solely for protocol testing or standards conformance are not treated as production Cloudflare services, even when hosted on Cloudflare-controlled domains (e.g., `*.cloudflare.com`, `*.cfdata.org`, `*.mediaoverquic.com`). Findings against these targets are Informational and not bounty eligible unless the report demonstrates impact against a supported Cloudflare product or production deployment with real users, SLA, or SLO commitments.
- Correctness bugs (such as panic on attacker input, API contract violations, or boundary-check errors) that do not cross a security boundary, do not expose unauthorized data, and are isolated per request in Cloudflare's production architecture.
- Reports where the vulnerability is in the library code but production Cloudflare deployments have independent controls that prevent the vulnerable code path from being reached.

**Potentially eligible for bounty:**

- Vulnerabilities in Cloudflare-published packages, frameworks, or templates that create a default insecure behavior for documented production use.
- Tenant isolation failures, auth bypasses, secret exposure, or code execution in supported production deployment patterns.
- Issues that are reproducible in Cloudflare production, Cloudflare-hosted services, or official supported deployment flows.
- Issues in Cloudflare-maintained OSS that is documented for use in Cloudflare's own production infrastructure (such as JSRPC bindings, WAF components, or DNS resolver libraries), even if tested locally, provided the same code runs in production with no independent mitigating layer.

---

### Proxy, Protocol, and Request Smuggling Reports

Reports involving HTTP request smuggling, protocol-level parsing differentials, or proxy behavior in Cloudflare's proxy infrastructure (Pingora, nginx, CDN edge) must demonstrate that the vulnerability is exploitable end-to-end through Cloudflare's stack, not only against a non-conformant upstream or downstream component.

**Not eligible for bounty:**

- Spec-compliance gaps or missing header normalization in Cloudflare proxy software where the actual security impact (such as request smuggling, response splitting, or cache poisoning) depends on the upstream or downstream server also having a parsing bug or non-conformant behavior. Cloudflare proxying a malformed header that a well-behaved upstream would reject is a hardening issue, not a smuggling vulnerability.
- Protocol-level findings that require the researcher to control both the client and the upstream server to demonstrate the differential. Request smuggling requires a disagreement between two real systems about message boundaries -- not a disagreement between the researcher's custom client and the researcher's custom server with Cloudflare in the middle.
- Reports where Cloudflare's proxy faithfully forwards headers or body content and the claimed vulnerability is that a non-conformant upstream misinterprets them. The upstream's parsing bug is outside Cloudflare's security boundary.
- Defense-in-depth observations about secondary protection mechanisms (such as connection pool poisoning guards or overread detection) that are only relevant if a primary vulnerability is already present.

**Potentially eligible for bounty:**

- Request smuggling where Cloudflare's own proxy disagrees with itself or with Cloudflare's own origin infrastructure about message boundaries, leading to cross-tenant request mixing, cache poisoning of Cloudflare-served content, or unauthorized access to Cloudflare-operated services.
- Protocol-level parsing differentials between Cloudflare's edge and Cloudflare's own upstream services that result in requests being routed, cached, or authenticated differently than intended.
- HTTP desynchronization attacks that are exploitable against standard, spec-compliant upstream servers (not only against intentionally misconfigured or non-conformant upstreams).

---

### WAF, Bot, Rate Limiting, and Detection Bypass Reports

Reports must demonstrate a true Cloudflare-controlled detection or enforcement bypass, not only a payload that was not blocked by a specific rule configuration.

The Cloudflare WAF uses a layered detection approach:

1. **Managed Rules**: signature-based detection for known attack patterns.
2. **WAF Attack Score**: ML-based detection that catches mutations and variations not covered by signatures.

Covering all possible attack payload mutations through signature rules alone is not feasible. This is the intended purpose of the Attack Score layer. The recommended approach for comprehensive protection is to deploy a custom rule based on the WAF Attack Score alongside managed rules.

**Not eligible for bounty:**

- Generic WAF bypass payloads, scanner payloads, fuzzing output, or encoded attack strings without a demonstrated security impact against an in-scope Cloudflare-owned application.
- SQL injection, XSS, SSRF, command injection, path traversal, or other application-layer payloads that are not blocked by WAF but do not exploit an actual vulnerability in a Cloudflare-owned application.
- Reports showing that a single managed rule, custom rule, score threshold, sensitivity level, or customer configuration did not block a request.
- Reports where the WAF inspected the request and produced a score, log entry, match, or partial detection, but the customer's rule configuration allowed the request.
- Claims based only on TCP fragmentation, TLS record splitting, HTTP/2 framing, case changes, URL encoding, chunking, compression, or request smuggling terminology without proving that Cloudflare parsed the request differently from the origin in a way that bypasses all relevant inspection.
- Reports requiring an origin server, customer application, or test endpoint configured in an insecure, non-default, or intentionally vulnerable way.
- Reports against Cloudflare customer zones, customer origins, third-party applications, or researcher-owned vulnerable apps unless Cloudflare explicitly authorizes the target and the report demonstrates a Cloudflare product bypass.
- CAPTCHA/Turnstile automation, bot-score tuning disputes, rate-limit threshold disputes, or requests for new signatures or rules without a concrete bypass of an intended Cloudflare enforcement boundary.
- Null-byte injection claims in HTTP headers without packet-level evidence (pcap, tcpdump, or curl --trace) showing a literal 0x00 byte transmitted on the wire and browser-observable payload execution against the designated WAF testbed.
- Status-code differences (such as 403 vs 200) between different endpoints, different WAF configurations, or different request structures without demonstrating that semantically identical requests are treated differently by the same WAF policy.

**Potentially eligible for bounty:**

- A reproducible parser differential where Cloudflare security products allow a request that the protected origin interprets as a materially different malicious request, and the bypass affects Cloudflare-owned infrastructure or a clearly in-scope test asset.
- A bypass of a documented Cloudflare-managed protection that should apply independent of customer rule tuning, such as a request class that is systematically invisible to WAF inspection.
- A WAF, rate-limit, or bot enforcement flaw allowing unauthorized access, account compromise, data exposure, or protected action execution on a Cloudflare-owned application.
- A default managed ruleset bypass with a concrete exploit against an in-scope Cloudflare-owned application where the same request should have been blocked according to the documented product behavior.

**Required evidence for WAF reports:**

- Exact target, zone, endpoint, request, response, Ray ID, timestamp, and account or zone ownership.
- Clear comparison between blocked and bypassing requests that are semantically equivalent at the origin (same payload location, same HTTP method, same protocol version).
- Evidence that Cloudflare security inspection did not occur or was materially bypassed, not merely that the configured action was log, skip, challenge, or allowed by score threshold.
- Demonstrated impact beyond "payload reached the origin," such as exploitation of an in-scope Cloudflare-owned vulnerability or unauthorized action.
- For claims involving raw bytes, null bytes, or protocol-level manipulation: packet capture (pcap, tcpdump, or curl --trace) showing the exact bytes on the wire. Filtered curl -v output or status-code differences alone are not sufficient evidence.



---

### Theoretical, Configuration-Dependent, and Missing-Impact Reports

Reports must demonstrate a realistic attack path and meaningful impact.

**Not eligible for bounty:**

- Reports without a working PoC or reproducible steps.
- Reports that only show source-code behavior without demonstrating exploitability or a realistic affected deployment.
- Reports requiring insecure, non-default, uncommon, or intentionally vulnerable customer configuration.
- Reports where the attacker must control all relevant preconditions, including both attacker and victim services, open redirects, Worker code, callbacks, or downstream systems.
- Reports that describe best-practice improvements, hardening, missing validation, or defense-in-depth changes without a concrete security impact.
- Reports with only scanner output, static analysis warnings, dependency warnings, or framework warnings without exploitability.
- Reports that present theoretical attack narratives using Cloudflare terminology without empirical evidence (such as fabricated packet captures, fictional API endpoints, invented tool names, or speculative root-cause analyses that are not supported by observable behavior).

**Potentially eligible for bounty:**

- Reports with a clear, reproducible attack path against an in-scope asset.
- Reports showing that a default or documented Cloudflare configuration leads to unauthorized access, data exposure, privilege escalation, account takeover, protected action execution, or meaningful tenant isolation failure.

---

### AI Agent, MCP, and Prompt Injection Reports

Reports involving AI agents, MCP (Model Context Protocol) servers, AI-powered automation, or LLM-based tools must demonstrate a concrete security impact beyond normal AI tool behavior.

**Not eligible for bounty:**

- Reports where the only demonstrated impact is that an MCP tool returns data that the authenticated user already has access to through a different API path (for example, path traversal within the same user's authorized API scope).
- Prompt injection claims where the "attacker" is the authenticated user injecting into their own session.
- Reports claiming that AI agent tools return data without "provenance markers" or "trust signals" as a vulnerability class. AI tools returning data from their configured data sources is expected behavior, not a security boundary violation.
- Reports against AI Playground, demo, or testing tools where the security model is intentionally simplified for experimentation.

**Potentially eligible for bounty:**

- Cross-user data exposure through AI agent infrastructure (for example, one user's session credentials or data accessible to another user through an AI-mediated channel).
- MCP consent screen or OAuth flow vulnerabilities that enable XSS, credential theft, or authorization bypass against production Cloudflare MCP servers.
- AI agent configuration injection that enables secret exfiltration or unauthorized actions in production deployments (not demo or playground environments).

---

### Memory Safety and Denial-of-Service in Cloudflare Runtimes

Reports involving memory corruption, panics, crashes, or resource exhaustion in Cloudflare runtimes (workerd, lol-html, quiche, etc.) are evaluated based on exploitability and production impact.

**Not eligible for bounty:**

- Panics or crashes that are isolated per request in production, result in a clean restart, and do not expose data or enable code execution.
- Resource exhaustion claims where the processing cost is linearly proportional to the input size with no amplification (for example, "sending 10MB causes 10MB of memory usage").
- Memory corruption bugs that are only reproducible in local or self-hosted environments where Cloudflare production has independent controls that prevent the vulnerable code path from being reached.
- API contract violations or correctness bugs (such as ArrayBufferView boundary errors) that do not cross a security boundary and where the affected data remains within the same allocation already accessible to the caller.

**Potentially eligible for bounty:**

- Memory corruption enabling cross-tenant data exposure or code execution outside the V8 sandbox.
- Denial-of-service where a small attacker-controlled input causes disproportionate resource consumption (super-linear amplification) or a deterministic crash that is reachable through Cloudflare production without independent mitigating controls.
- Memory safety issues in Cloudflare runtimes that affect all tenants sharing a process, where the crash is reachable through standard Worker primitives (such as fetch, streams, or HTTP decompression) without requiring product-specific bindings.

---

### workerd (Open Source) vs. Cloudflare Workers (Production Service)

[workerd](https://github.com/cloudflare/workerd) is Cloudflare's open-source JavaScript/WebAssembly runtime. Cloudflare Workers is the production service that runs workerd inside Cloudflare's infrastructure with additional layers of isolation, resource enforcement, and operational controls provided by the edgeworker supervisor, process sandboxing, and fleet-wide monitoring.

The security boundaries differ between the two:

- **workerd alone** (as run locally or self-hosted): the V8 isolate sandbox is the primary security boundary. Bugs that escape V8 or corrupt memory outside the isolate are security-relevant at this layer.
- **Cloudflare Workers in production**: workerd runs inside additional containment (process-level sandboxing, per-request resource limits, supervisor-enforced CPU and memory caps, network policy enforcement). Some bugs that are exploitable in standalone workerd may be independently mitigated by these production layers.

**Production reachability is required, production exploitation is not.**

Researchers must demonstrate that the vulnerable code path is reachable through standard Cloudflare Workers APIs and primitives (such as `fetch`, Web Streams, `crypto`, `HTMLRewriter`, WebSocket, or JSRPC) under default production configuration. However, researchers must **not** attempt to exploit the vulnerability against Cloudflare's production Workers infrastructure, other tenants, or customer workloads. Reproduce locally against your own workerd instance and explain why the same code path is reachable in production. We will validate production reachability internally.

For workerd's security model and the boundaries it is designed to enforce, see [workerd's security documentation](https://github.com/cloudflare/workerd/blob/main/security.md).

**Exploit primitives and novel research are valued.**

Cloudflare recognizes that some of the most impactful security research involves discovering exploit primitives -- building blocks that advance the state of the art in attacking a runtime, even before a full end-to-end chain is demonstrated.

Reports that identify novel exploit primitives, new attack surface in the runtime, or techniques that meaningfully reduce the cost of future exploitation are eligible for bounty at severity levels reflecting the primitive's power and production reachability, even without a fully weaponized end-to-end chain. We encourage researchers to explain the primitive's significance and how it could compose with other techniques.

**Severity calibration for workerd reports:**

- **Critical**: Reliable V8 sandbox escape, cross-tenant code execution, or cross-tenant data read in production-reachable code paths.
- **High**: Memory corruption outside V8 (heap UAF, OOB write) reachable through core Worker primitives (fetch, streams, crypto) with demonstrated control over corrupted data, even without a full exploitation chain.
- **Medium**: Deterministic process crash (SIGSEGV, abort) reachable through core Worker primitives that affects all co-located tenants. Memory corruption with limited attacker control or reachable only through product-specific bindings (Queues, KV, D1).
- **Low**: Crashes or resource exhaustion reachable only through narrow or product-specific APIs, or where production resource limits independently bound the impact. DoS with linear cost proportional to input.
- **Informational**: Correctness bugs without security boundary crossing. Resource consumption proportional to input where production controls (CPU time limits, memory caps, body size limits) prevent meaningful impact. Bugs reproducible only in standalone workerd where production has independent mitigating layers.

Any vulnerability that only affects a standalone or self-hosted build of workerd (for example, behavior that requires a non-production build configuration and is not reachable on Cloudflare's production Workers platform) will be treated as Informational. Reports must demonstrate impact on production Workers to be eligible for a bounty. Contributions may still be submitted as a Pull Request to the open-source repository.

---
### Billing, Subscription, and Plan Enforcement Cap

Reports involving billing bypass, subscription bypass, plan enforcement gaps, access to premium features from a free account, or race conditions in billing or subscription flows are capped at **Low severity and $250 maximum payout**, unless Cloudflare determines that the report demonstrates a broader security boundary bypass beyond billing or feature-entitlement impact.

---

# What you can expect from us

## Handling of reports
Cloudflare will make best effort to handle reports within the following time frame. Note that all times are in business days.

| First Response | Triage | Bounty | Resolution |
| --- | --- | --- | --- |
| 10 days | 10 days (from first response) | 10 days (from triage) | Depends on severity and complexity |

## Rewards
When duplicates occur, we award only the first report that was received, provided that it can be fully reproduced. If multiple vulnerabilities are caused by one underlying issue, we reserve the right to award only one bounty. All reward decisions are at the sole discretion of Cloudflare.

Cloudflare continuously invests in internal security research, including automated vulnerability discovery using frontier AI models. Findings identified internally before an external submission are treated as duplicates. Researchers may encounter cases where a valid vulnerability they discovered independently was already identified by Cloudflare's internal security programs. In such cases, the report will be closed as Informational (already known) regardless of severity. We appreciate the independent validation and encourage researchers to continue submitting as many critical findings are first reported through the bug bounty program.

### Mergers and acquisitions
We encourage and appreciate researchers who report vulnerabilities in new Cloudflare products coming through mergers and acquisitions. However, findings are eligible for rewards at Cloudflare's sole discretion.

## Big Bonanza
We're excited to announce an exclusive opportunity for our top-tier talent! Researchers who demonstrate excellence by submitting 2 valid critical severity reports or 4 valid high severity reports can request entry into our prestigious Cloudflare VIP Program.

As a member of the VIP program, you’ll unlock: 

✨ Access to enterprise features!
✨ Exclusive access to test our cutting-edge Beta products 
✨ Opportunity to participate in special bug bounty campaigns 
✨ Higher bounty payouts and more!

Join our VIP program and take your bug hunting to the next level!


## Disclosure
Cloudflare strongly supports coordinated disclosure. Our pledge to you, a vulnerability reporter, is to respond promptly and to fix the vulnerability in the sensible timeframe and in exchange we ask you to coordinate the disclosure with us.

Cloudflare aims to resolve all the vulnerabilities within the 90 days and we ask you not to disclose the information before that time. If we won’t be able to uphold that commitment on our end, we will let you know (but the decision if you would like to publish after the 90 days will be yours).

For some of the submissions we might decide not to treat it as vulnerability or not to issue a bounty. Still, we would like you to coordinate the disclosure with us so we are prepared for it.

Often we decide on the payout before the vulnerability is fixed so the reward is not a payment for your silence. Still, we really want to have a chance to fix the vulnerability before it can be used by a malicious actor. For this reason we ask you to let us know about any plans you might have regarding plans to present your findings in any way (like blog posts, articles, conference presentations etc.)

At the end of the day the decision on what to disclose and when to disclose it is yours and we would like to support you so feel free to share any drafts of your presentation or article before the publishing so we can even provide some feedback or share it with internal teams.

We have to mention however, that any actions done in bad faith might result in excluding malicious reporters from the program or, in case of disclosing Cloudflare or Cloudflare customers’ information (like PII, or other sensitive information) might even force us to take legal actions.

# Privacy Policy, Restrictions and Taxes
Cloudflare maintains both a [privacy policy](https://www.cloudflare.com/privacypolicy/) and [transparency report](https://www.cloudflare.com/transparency/). As mentioned in our Privacy Policy, Cloudflare's website and services are not intended for, or designed to attract individuals under the age of 18. Due to the Children's Online Privacy Protection Act (COPPA), we cannot accept submissions from children under the age of 13. Reporters under the age of 18 will not be eligible to receive Cloudflare service rewards. 

This program is not open to any individual on, or anyone residing in any country on, any U.S. sanctions lists. Cloudflare employees and their family members are not eligible for bounties.

The decision to pay a reward is entirely at our discretion. You must not violate any law. You are responsible for any tax implications or additional restrictions depending on your country and local law. We reserve the right to cancel this program at any time.

## Mediation
Cloudflare encourages hackers to Request Mediation directly on the reports when they feel the program does not honor commitments made on the policy page. Please provide as much context and reasoning for requesting mediation. 
Please refer to https://docs.hackerone.com/en/articles/8466617-hacker-mediation for when and how to request mediation from HackerOne. 

If you still feel dissatisfied or do not receive a response within 30-60 days, depending on the severity of your report, please escalate to the internal Cloudflare team via bugbounty@cloudflare.com. 

This address is only for querying or escalating a report that already exists on HackerOne. It is not an intake channel for new vulnerabilities. New findings sent to bugbounty@cloudflare.com will not be triaged and must be filed through HackerOne as described in the Submitting a Report section.