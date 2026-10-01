# AUDIT3 — Kiểm định lớp 2 độc lập cho `T18` (Task T24)

**Người kiểm định:** Auditor2 (`ag_d271d4f8`) · **Phòng:** `ab1-478d-cfa7`
**Nhánh:** `agent/auditor-2/T24` — **KHÔNG merge `main`**
**Đối tượng kiểm:** nhánh `agent/deepseek-harness/T8` @ **`ff252f8`** (Admin chỉ định) — artifact `reviews/VERIFY2.md` + `agents/deepseek-harness/**`
**Mốc `main`:** `e8c45a07b73640c68f12b1252f04300ebbae041a` (166 file)
**Bản cũ giữ nguyên:** `AUDIT.md`, `AUDIT.json`, `AUDIT2.md`, `AUDIT2.json` — **không sửa** (đã ở trên `main` = vết kiểm toán).

---

## 0. PHÁN QUYẾT — trả lời trực tiếp câu Admin cần nhất

> *"T18 được tạo ra để làm **nguồn THỨ HAI** cho một khẳng định kỹ thuật. Nếu bạn xác nhận, ta có ≥2 nguồn độc lập đúng nghĩa lớp 2."*

### ✅ **XÁC NHẬN T18 ĐẠT — nhưng kèm MỘT SỬA ĐỔI ở hạng mục 3.**

| # | Khẳng định phải tái lập | Tôi tái lập độc lập | Phán quyết |
|---|---|---|---|
| 1 | **S31 đọc được toàn văn** (arXiv `2603.11006v2`) | HTTP **200**, **368.458 B byte-exact**; **8/8 từ khoá = 0** (tôi đếm trên **RAW HTML**, không chỉ văn bản bóc thẻ); câu future-work **nguyên văn khớp**; **venue SPIQE 2026 qua `arxiv:comment`** | ✅ **XÁC NHẬN HOÀN TOÀN** |
| 2 | **DOI `iccit` vs `ICICT`** | HOA → **404** trên doi.org + Crossref + OpenAlex; thường → **202/200/200** | ✅ **XÁC NHẬN** (một tiểu số lệch — xem §2.2) |
| 3 | **`asset_type` của 4 xung đột GitLab** | Dữ liệu thô **tái lập 100%** (63 entry / IN=24 / OUT=39; tách type 2+2) — **NHƯNG** biến quyết định là **`archived_at`**, thứ **cả hai kiểm định viên trước đều KHÔNG truy vấn** | ⚠️ **DỮ LIỆU ĐÚNG, KẾT LUẬN BỊ TÔI VƯỢT QUA** → xem §3 |
| 4 | **T19 của ResearchLead** (4/4 DOI, N=4) | 4/4 vị trí nay `iccit`; quét vị trí trích dẫn hiệu lực = **5 thường / 0 HOA**; Crossref xác nhận bài **có thật** | ✅ **XÁC NHẬN** (một câu chữ quá mạnh — xem §4.2) |

**Trả lời câu hỏi trung tâm "2 hay 4 xung đột thật?" → KHÔNG PHẢI 2, CŨNG KHÔNG PHẢI 4:**
### **0 xung đột trong chính sách ĐANG HIỆU LỰC.** Cả 4 "xung đột" đều là so với **bản ghi ĐÃ LƯU TRỮ (archived 2020–2022)**.
Đây là **nguồn thứ ba độc lập** mà Admin yêu cầu — và nó **vượt qua cả hai kết luận trước đó**.

**T18 có đủ tư cách làm nguồn thứ hai không?** **CÓ** — với các lý do ở §5: khóa kiểm mù bằng băm **3/3 khớp**,
bằng chứng **đóng băng** không sửa sau khi khóa, **tái lập trên clone mới** cho kết quả y hệt, và **tự sửa mình**
ở chỗ gọi sai bản chất `asset_type`. Artifact này làm việc thô **chính xác**; chỉ **thiếu một chiều dữ liệu** mà tôi bổ sung.

---

## 1. Phương pháp — tôi tự chạy, không đọc kết luận trước

Toàn bộ §1–§4 dưới đây do Auditor2 **tự chạy lệnh trên máy này**, không dùng script hay file tóm tắt của
DeepSeek-Harness/Reviewer1. Tôi **không** đọc `reviews/VERIFY2.md` trước khi chạy xong 4 phép kiểm;
chỉ đọc để **đối chiếu sau** (mục đích: phát hiện chép lại thay vì tái lập).

---

## 2. Hạng mục 1 & 2 — S31 và DOI

### 2.1 S31 (`arXiv:2603.11006v2`) — ✅ **XÁC NHẬN HOÀN TOÀN, BYTE-EXACT**

```text
$ curl -sL -o arxivS31.html -w 'http_code=%{http_code}\nsize_download=%{size_download}\n' \
      'https://arxiv.org/html/2603.11006v2'
http_code=200
size_download=368458
content_type=text/html; charset=utf-8
$ wc -c < arxivS31.html
368458
```
⇒ **Khớp `368.458 B` của DeepSeek-Harness CHÍNH XÁC TỪNG BYTE.** Không thể đoán ra con số này.

**Đếm từ khoá — tôi đếm trên RAW HTML (mạnh hơn cách bóc thẻ):**

| Từ khoá | DeepSeek-Harness | **Tôi đếm trên RAW HTML** | Kết quả |
|---|---|---|---|
| `MTU` | 0 | **0** | ✅ |
| `middlebox` | 0 | **0** | ✅ |
| `fragment` | 0 | **0** | ✅ |
| `packet size` | 0 | **0** | ✅ |
| `network layer` | 0 | **0** | ✅ |
| `certificate chain` | 0 | **0** | ✅ |
| `tunnel` | 0 | **0** | ✅ |
| `VPN` | 0 | **0** | ✅ |
| `ML-DSA` | 4 | **4** | ✅ |
| `hybrid` | 40 | **40** | ✅ |
| `latency` | 74 | **74** | ✅ |
| `handshake` | 64 | **64** | ✅ |
| `load balancer` | 2 | **2** | ✅ |
| `MiTM` | 2 | **2** | ✅ |

**Giá trị gia tăng của phép kiểm này:** tôi đếm trên **HTML thô**, không phải trên văn bản đã bóc thẻ.
Điều đó **loại trừ khả năng** 8 số 0 là do **phương pháp bóc thẻ làm mất chữ** — tức 8 từ khoá đó
**thực sự vắng mặt** trong tài liệu. Tiêu đề bài xác nhận nội dung: *"Layered Performance Analysis of TLS 1.3
Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange"* ⇒ **bài KHÔNG nói về MTU/tầng mạng/phân mảnh**;
các số 0 là **đúng bản chất**, không phải tiểu tiết kỹ thuật.

**Câu future-work về *"commercial load balancers and MiTM inspection devices"* — tôi đọc được, nguyên văn:**

> *"extending the analysis to real network environments with **commercial load balancers and MiTM
> (Man-in-The-Middle) inspection devices** to quantify the performance impact when using PQC in TLS
> especially considering the high network load/connections these devices need to handle, where PQC
> performance impact may be signifiant."* — tìm thấy tại **ký tự 56.165** trong HTML thô.

⇒ **Khớp từng ký tự.** Đây là bằng chứng quyết định: khoảng hở mà T11 nêu nằm **trong future work** của chính bài.

**Venue — kiểm đúng chỗ Admin cảnh báo (ResearchLead từng suýt kết luận sai):**
```text
$ grep -c "SPIQE" arxivS31.html        -> 0        (KHÔNG có trong HTML body)
$ curl -sL 'http://export.arxiv.org/api/query?id_list=2603.11006' | <parse>
   arxiv:comment: "Accepted in SPIQE 2026 (Workshop on Secure Protocol Implementations in the
                   Quantum Era), associated to Euro S&P 2026. v2 incorporates peer-review feedback..."
```
⇒ **Xác nhận:** venue **chỉ** nằm ở **`arxiv:comment` của arXiv API**, **KHÔNG** nằm trong HTML body
(chuỗi `SPIQE` = **0 lần** trong 368.458 B HTML). **Cảnh báo của Admin là ĐÚNG và có thể tái lập.**

### 2.2 DOI `ICICT` vs `iccit` — ✅ **XÁC NHẬN**

```text
10.1109/ICICT63348.2025.10989392   doi.org=404  Crossref=404  OpenAlex=404
10.1109/iccit63348.2025.10989392   doi.org=202  Crossref=200  OpenAlex=200
```
⇒ Khẳng định *"HOA → 404, thường → 200"* **đúng trên cả ba dịch vụ**.

**Một tiểu số lệch — tôi nêu để minh bạch, KHÔNG phải lỗi:**
DeepSeek-Harness ghi `doi.org=302` (ở cả `t18b` và VERIFY2 #10); **tôi và ResearchLead (`T19_checks.txt:11,17`) đều đo `202`**.
Nguyên nhân: tôi dùng `curl -L` (theo redirect, `%{http_code}` trả mã **cuối**), còn 302 là mã **chuyển hướng đầu**.
**Bản chất giống hệt nhau** (đều là "phân giải được"); chỉ khác cách đo mã redirect. Không ảnh hưởng kết luận.

**Metadata bài — tôi tự lấy từ Crossref:**
```text
title    : Zero Trust Implementation for Legacy Systems using Dynamic Microsegmentation,
           Role-Based Access Control (RBAC), and Attribute-Based Access Control (ABAC)
container: 2025 4th International Conference on Computing and Information Technology (ICCIT)
published: 2025-04-13      type: proceedings-article
```
⇒ Bài **có thật**; tên hội nghị trong `container-title` là **ICCIT** — khớp `iccit` trong DOI và **giải thích luôn
vì sao `ICICT` sai**: đó là **đảo chữ của ICCIT**. Không có dấu hiệu bịa nguồn.

---

## 3. ⚠️ Hạng mục 3 — `asset_type` 4 xung đột GitLab: **TÔI VƯỢT QUA CẢ HAI KẾT LUẬN TRƯỚC**

### 3.1 Dữ liệu thô của DeepSeek-Harness — **TÁI LẬP ĐƯỢC 100%**
Tôi tự `POST https://hackerone.com/graphql` (không cần auth) và tự parse:
```text
TONG scope entry (khong loc) : 63        <- khop
IN (eligible_for_submission) : 24        <- khop
OUT                          : 39        <- khop
```
Phân tách theo `asset_type` — **khớp y hệt** bản của họ:

| Tài sản | Vế IN (đang hiệu lực) | Vế OUT | Cùng `asset_type`? | DeepSeek-Harness gọi |
|---|---|---|---|---|
| `about.gitlab.com` | `URL`, eligible=True | `URL`, eligible=False | **CÓ** | xung đột THẬT |
| `docs.gitlab.com` | `URL`, eligible=True | `URL`, eligible=False | **CÓ** | xung đột THẬT |
| `*.gitlab.net` | `WILDCARD`, eligible=True | `URL`, eligible=False | KHÔNG | không phải xung đột |
| `*.gitlap.com` | `WILDCARD`, eligible=True | `URL`, eligible=False | KHÔNG | không phải xung đột |

⇒ **Việc thô của DeepSeek-Harness chính xác.** Reviewer1 cũng đúng khi dùng `asset_type` làm tiêu chí phân biệt
(DeepSeek-Harness **tự nhận** điều này ở VERIFY2 #3 §3: *"tôi gọi đó là 'xung đột' là **sai về bản chất**"*).
**DISSENT-7 phán Reviewer1 đúng về kỹ thuật — phán quyết đó đúng.**

### 3.2 **NHƯNG biến quyết định KHÔNG phải `asset_type` — mà là `archived_at`**
Cả hai kiểm định viên **chưa từng truy vấn** trường `archived_at`/`archived` (kiểm chứng:
`grep -rn "archived" --include=*.md --include=*.txt .` chỉ ra **3 dòng**, và cả 3 là về *"archived repos"*
trong **chính sách GitHub** — **không liên quan** scope GitLab). Tôi bổ sung chiều dữ liệu đó:

```text
$ <GraphQL, them truong archived_at>
TONG (khong loc) = 63   |  archived_at != null = 19  |  active = 44
```
**Và đây là kết quả quyết định — bật `archived:false` (chính sách ĐANG HIỆU LỰC):**
```text
$ <GraphQL: structured_scopes(first:200, archived:false)>
TONG = 44
IN   = 19   OUT = 25
=> TAI SAN XUAT HIEN CA 2 PHIA: 0   (KHONG MOT TAI SAN NAO)
```

**Chi tiết 4 tài sản — vế OUT đều là bản ghi ĐÃ LƯU TRỮ:**

| Tài sản | Vế IN (active) | Vế OUT (archived) |
|---|---|---|
| `about.gitlab.com` | `URL`, submission=**True**, bounty=**True**, sev=medium | `URL`, submission=False, **archived 2022-07-21** |
| `docs.gitlab.com` | `URL`, submission=**True**, bounty=**True**, sev=medium | `URL`, submission=False, **archived 2022-07-21** |
| `*.gitlab.net` | `WILDCARD`, submission=**True**, bounty=**True**, sev=medium | `URL`, submission=False, **archived 2022-07-21** |
| `*.gitlap.com` | `WILDCARD`, submission=**True**, bounty=**True**, sev=medium | `URL`, submission=False, **archived 2022-07-21** |

Trong 19 bản ghi lưu trữ còn có `*.gitter.im`, `api.gitter.im`, `blog.gitter.im`, `ws*.gitter.im`
(**archived 2020-10-05**) — dấu hiệu rõ ràng của **scope lịch sử đã nghỉ hưu**, không phải chính sách hiện hành.

### 3.3 Kết luận hạng mục 3 — **sửa lại cả hai kết luận trước**
- **Câu hỏi "2 hay 4 xung đột thật?" có TIỀN ĐỀ SAI.** Đáp án đúng: **0 xung đột trong chính sách đang hiệu lực.**
  Cả 4 "xung đột" sinh ra **chỉ vì** đem vế IN đang hiệu lực so với vế OUT **đã lưu trữ 4–6 năm**.
- **Chính sách sống của GitLab rõ ràng, KHÔNG mâu thuẫn:** cả 4 tài sản đều là một dòng **duy nhất**,
  `eligible_for_submission=True` **và** `eligible_for_bounty=True`, `archived_at=null`.
- **Không có hại:** quyết định **loại cả 4 khỏi T4** vẫn là **thận trọng an toàn**, và `DISSENT-7` **đã tự nhận**
  *"thận trọng hơn mức cần nhưng không gây hại"*. Tôi chỉ **làm chính xác thêm**: không phải "2 thật + 2 thận trọng",
  mà là **"0 thật + 4 thận trọng"**.
- **Cần sửa câu chữ (không phải sửa quyết định):** `rooms/ab1-478d-cfa7/directives.md:183-184` viết
  *"4 tài sản GitLab có **XUNG ĐỘT SCOPE trong dữ liệu công bố của chính GitLab**"* — **tiền đề này không chính xác**.
  Nên sửa thành: *"xung đột chỉ xuất hiện khi so với **bản ghi đã lưu trữ (archived 2020–2022)**;
  chính sách đang hiệu lực ghi cả 4 là in-scope và có thưởng"*.

> **Vì sao đây là giá trị thật của lớp kiểm định thứ ba:** hai kiểm định viên độc lập **đều** dừng ở `asset_type`
> và **đều** kết luận "2 xung đột thật". Một nguồn thứ ba **không chép lại** mà **truy vấn thêm một chiều dữ liệu**
> đã phát hiện tiền đề sai. Nếu chỉ có 2 nguồn, kho đã chốt "2 xung đột thật" — **sai**.

---

## 4. Hạng mục 4 — `T19` của ResearchLead

### 4.1 ✅ **XÁC NHẬN: 4/4 vị trí đã sửa đúng**
Bốn vị trí mà `DISSENT-6` nêu nay đều dùng dạng thường:
```text
research/ebpf-microsegmentation/BLINDCHECK.md:53    DOI=10.1109/iccit63348.2025.10989392
research/ebpf-microsegmentation/LITREVIEW.md:264    DOI=10.1109/iccit63348.2025.10989392
research/ebpf-microsegmentation/SOURCES.md:81       DOI=10.1109/iccit63348.2025.10989392
research/pqc-tls-migration/SOURCES.md:109           DOI=10.1109/iccit63348.2025.10989392
```
**Quét ở vị trí trích dẫn thật** (tôi tự tách trường DOI, loại file bằng chứng):
```text
5 × 10.1109/iccit63348.2025.10989392    0 × bất kỳ dạng HOA nào
```
⇒ **Đạt.** Crossref xác nhận metadata thật (§2.2) ⇒ **không phải bịa nguồn, đúng là lỗi chép hoa/thường.**

### 4.2 ⚠️ **Một câu chữ QUÁ MẠNH — nêu để chính xác, KHÔNG phải vi phạm**
`research/EVIDENCE/T19_checks.txt:28` và hai `SOURCES.md` (`:157`, `:181`) đều viết:
*"Sau khi sửa: `grep -rn "ICICT63348" research/` → **0 match**"*. **Câu này SAI nếu chạy nguyên văn:**
```text
$ grep -rn "ICICT63348" research/ | wc -l
8
```
**Nhưng tôi đọc cả 8 dòng và tất cả đều hợp lệ:**
- **3 dòng** trong chính `T19_checks.txt:12,14,16` — **URL dùng để chứng minh 404** (ghi lại chuỗi SAI để đối chiếu);
- **3 dòng** là **câu văn mô tả việc sửa** (`T19_checks.txt:23,28`, `SOURCES.md:157`, `SOURCES.md:181`);
- **1 dòng** `T19_checks.txt:117` — và dòng này **chính là lời tự cảnh báo của ResearchLead**:
  > *"Lưu ý về `grep -rn "ICICT63348" research/`: sau khi sửa, các match còn lại CHỈ nằm trong
  > (a) chính file bằng chứng này (ghi lại chuỗi SAI để đối chiếu) và (b) câu văn giải thích việc sửa.
  > KHÔNG còn match nào ở vị trí trích dẫn thật."*

⇒ **Bản chất ĐÚNG (0 ở vị trí trích dẫn thật), và tác giả ĐÃ TỰ GHI RÕ giới hạn của phép đếm.**
Đây là **thiếu sót về trình bày mức thấp**: nên viết `grep … | grep -v EVIDENCE` hoặc nói rõ "0 ở vị trí trích dẫn".
**DeepSeek-Harness cũng đã bắt đúng điểm này** (VERIFY2 #11: *"nếu không, tôi đã báo sai 'T19 còn sót 8 chỗ'"*) — tôi xác nhận độc lập.

### 4.3 `N=4` — ✅ **XÁC NHẬN**
`ADMIN/D-017` yêu cầu N của T1 phải **≥3**, không giữ `N=2`; nay ghi **`N=4`** và T19 ghi lại **theo bằng chứng**.
Tôi **không** chấm lại điểm tính mới (ngoài phạm vi T24) nhưng xác nhận **con số đã được ghi lại và khớp yêu cầu**.

---

## 5. Vì sao `T18` **ĐỦ TƯ CÁCH** làm nguồn thứ hai — kiểm chứng độc lập

Đây là phần Admin cần nhất, nên tôi kiểm **cơ chế liêm chính** của artifact, không chỉ nội dung:

### 5.1 ✅ **Khóa kiểm mù bằng băm — KHỚP 3/3 TỪNG BYTE**
`agents/deepseek-harness/T18/BLIND_LOCK.md` khai 3 hash chốt **trước** khi đọc kết luận Reviewer1.
Tôi **tự tính lại** sha256 từ blob trong git:
```text
3c5668eb582581470dd000c8145dcf57b8c52c3beacf635faacf0d2096c4a407  t18a_s31_blind_raw.txt   ✅ KHỚP
54fd0e99a80c75fdfd78649b5b5b4ffb3345ada02fcb1335e0ebe500e215c7d6  t18b_doi_blind_raw.txt   ✅ KHỚP
af52f7eae8ba07e69de4cc02be8032f36bda46e31346f6ecf3eaadfb981b5a65  t18c_scope_blind_raw.txt ✅ KHỚP
```

### 5.2 ✅ **Bằng chứng KHÔNG bị sửa sau khi khóa**
```text
$ git log --format='%h %s' origin/agent/deepseek-harness/T8 -- agents/deepseek-harness/T18/
441a72f [T18] blind: khoa bang chung kiem mu (3 file hash) TRUOC khi doc ket luan Reviewer1
ff252f8 [T18] tai lap lan 2 tren clone moi — ca 3 phep kiem khop y het, chung minh on dinh
```
Cả 3 file bằng chứng **được tạo ở `441a72f` và KHÔNG bị chạm lần nào sau đó**
(`git log <branch> -- <file> | tail -1` = `441a72f` cho từng file). `ff252f8` **chỉ thêm output tái lập lần 2**,
không sửa 3 file blind. ⇒ **Bằng chứng đóng băng thật, không thể sửa hậu kiểm mà lệch hash.**

### 5.3 ✅ **Tái lập trên clone MỚI cho kết quả y hệt**
`ff252f8` tự khai *"ca 3 phep kiem khop y het"*. **Tôi là nguồn kiểm thứ ba độc lập trên máy này** và 3/3 phép
kiểm then chốt (S31, DOI, scope) **đều cho cùng con số** (§2.1, §2.2, §3.1). ⇒ Độ ổn định **được xác nhận bởi
một bên không liên quan**, không chỉ bởi chính tác giả.

### 5.4 ✅ **Tác giả tự sửa mình, không tự vệ**
VERIFY2 #3 §3: DeepSeek-Harness **tự nhận** cách gọi *"xung đột"* của mình là **sai về bản chất**, ghi
*"Đây là lần **thứ hai** Reviewer1 đi xa hơn tôi"*. Ở #12 họ cũng ghi nhận ResearchLead đúng về sai số `edge`
(99,5% vs 99,7%, khác do cách bóc thẻ). ⇒ **Không có dấu hiệu tự vệ hay thổi phồng.**

### 5.5 ✅ **Tuân thủ D-004**
VERIFY2 #10 §7 và #11 §8 đều ghi rõ: *"File này do tôi viết — tôi KHÔNG tự verify (D-004). Cần Reviewer1 hoặc
Auditor2 kiểm; nếu bất đồng ⇒ **Auditor2 chốt**."* Chính hành vi **chuyển quyền phán quyết cuối cho tôi** là
đúng luật "người viết không tự verify".

### 5.6 🔎 **Kiểm thêm ngoài phạm vi (ghi nhận công bằng) — 4/4 quan sát DNS khớp**
Không thuộc 4 hạng mục Admin giao, nhưng tôi chạy nhanh vì nó rẻ và có giá trị pháp lý:
```text
registry.gitlab.com A -> 35.227.35.254     ✅ khop
gitlab.com A          -> 172.65.251.78     ✅ khop
license.gitlab.com A  -> (khong co)        ✅ khop
license.gitlab.com CNAME -> (khong co)     ✅ khop  => khong phai subdomain takeover
```

---

## 6. PHÁT HIỆN CỦA T24

| ID | Mức | Loại | Tóm tắt | Bằng chứng |
|---|---|---|---|---|
| **M-01** | **Trung bình** | **vi phạm (tiền đề sai trong chỉ thị)** | `directives.md:183-184` (D-013 addendum) khẳng định *"4 tài sản GitLab có XUNG ĐỘT SCOPE trong dữ liệu công bố của chính GitLab"*. **Sai tiền đề:** xung đột chỉ xuất hiện khi so với **bản ghi đã lưu trữ**; chính sách đang hiệu lực ghi **cả 4 là in-scope + có thưởng**. `DISSENT-7` cũng phán *"2 là xung đột THẬT"* — **cũng chưa đúng**: số đúng là **0**. | `directives.md:183-184`; `ADMIN/DISSENT.md` DISSENT-7; GraphQL `archived:false` → 44 entry, **0 tài sản 2 phía**; 4 vế OUT đều `archived_at` 2022-07-21 |
| **M-02** | Thấp | **nghi vấn (kết luận lớp 2 bị vượt)** | `T18` kết luận *"4 xung đột → 2 thật + 2 khác type"* và chấm **PASS 8/8**. Kết luận này **thiếu chiều `archived_at`** ⇒ **PASS không còn giá trị nguyên vẹn** ở hạng mục 3. Hai kiểm định viên độc lập **cùng** kết luận sai vì **cùng** thiếu một chiều dữ liệu. | VERIFY2 #T18 bảng §4 dòng 8 + §6 dòng 4; `grep -rn archived` = 3 dòng, **không dòng nào** về scope GitLab |
| **M-03** | Thấp | thiếu sót trình bày | Câu *"`grep -rn "ICICT63348" research/` → 0 match"* (`T19_checks.txt:28`, `ebpf…/SOURCES.md:157`, `pqc…/SOURCES.md:181`) **sai khi chạy nguyên văn: 8 match**. Bản chất đúng (0 ở vị trí trích dẫn) và **tác giả đã tự ghi rõ** giới hạn ở `T19_checks.txt:117`. | `grep -rn "ICICT63348" research/ \| wc -l` = **8**; `T19_checks.txt:117-119` |
| **M-04** | Thấp | thiếu sót trình bày (đo lường) | `doi.org` cho DOI đúng: DeepSeek-Harness ghi **302**, tôi và ResearchLead (`T19_checks.txt:11,17`) đều đo **202**. Khác do **có/không theo redirect (`-L`)**. Bản chất giống hệt. | `t18b_doi_blind_raw.txt`; `T19_checks.txt:11,17`; đo lại của tôi |

**Điểm tôi muốn nói rõ:** **M-01/M-02 KHÔNG phải lỗi của DeepSeek-Harness hay Reviewer1.** Cả hai làm đúng
việc được giao và dữ liệu thô của họ **chính xác 100%**. Đây là **giới hạn của thiết kế kiểm định**: hai nguồn
cùng truy vấn **một tập trường** thì cùng mù **một chiều dữ liệu**. Giá trị của nguồn thứ ba nằm ở chỗ
**hỏi thêm một câu hỏi mới**, không phải chạy lại câu hỏi cũ.

---

## 7. ĐÃ KIỂM VÀ **KHÔNG** PHÁT HIỆN VẤN ĐỀ

1. **S31 tồn tại thật, tải được toàn văn:** HTTP 200, **368.458 B byte-exact** với khai báo.
2. **8/8 từ khoá MTU/middlebox/fragment/packet size/network layer/certificate chain/tunnel/VPN = 0** —
   tôi đếm trên **RAW HTML**, loại trừ khả năng mất chữ do bóc thẻ.
3. **Câu future-work về *"commercial load balancers and MiTM inspection devices"* nguyên văn khớp**, tại ký tự 56.165.
4. **Venue `SPIQE 2026` xác nhận qua `arxiv:comment`**, và **`SPIQE` = 0 lần trong HTML body** — đúng chỗ Admin cảnh báo.
5. **DOI: HOA → 404 (3/3 dịch vụ), thường → 200/200/202.**
6. **Metadata S29 có thật** trên Crossref: tiêu đề + `container-title` = *"2025 4th ICCIT"* + 2025-04-13 + proceedings-article.
7. **Khóa kiểm mù T18: sha256 3/3 khớp từng byte.**
8. **Bằng chứng T18 không bị sửa sau khi khóa** (tạo ở `441a72f`, không chạm lại).
9. **T18 tái lập trên clone mới, và tôi tái lập lần thứ ba** — cùng con số.
10. **T19: 4/4 vị trí DOI đã sửa đúng; vị trí trích dẫn hiệu lực = 5 thường / 0 HOA; `N=4` khớp yêu cầu D-017.**
11. **Dữ liệu thô scope GitLab của DeepSeek-Harness khớp 100%** (63 / IN=24 / OUT=39 / tách type 2+2).
12. **4/4 quan sát DNS khớp** (kiểm thêm ngoài phạm vi).
13. **Không có vi phạm territory:** T18 nằm trong `reviews/VERIFY2.md` + `agents/deepseek-harness/**` — đúng territory T18.
14. **Không rò rỉ credential** trong artifact mới (không thấy `agent_token`/`creds`/token nào).

---

## 8. KHUYẾN NGHỊ

1. **[M-01 — sửa câu chữ, KHÔNG đổi quyết định]** Sửa `directives.md:183-184`: nêu rõ 4 "xung đột" chỉ tồn tại
   khi so với **bản ghi đã lưu trữ (archived 2020–2022)**; chính sách đang hiệu lực ghi cả 4 là
   `eligible_for_submission=True` + `eligible_for_bounty=True`. **Giữ nguyên việc loại khỏi T4** (thận trọng, vô hại).
2. **[M-01 — cập nhật DISSENT-7]** Ghi bổ sung: sau nguồn thứ ba, con số đúng là **0 xung đột hiệu lực**,
   không phải 2; và **thêm `archived_at` vào tiêu chí so scope** cho mọi lần kiểm sau.
3. **[M-02]** Không cần hạ cấp T18 toàn bộ: **T18 vẫn ĐẠT** ở S31/DOI/T19 và ở **tính liêm chính** (khóa băm, không sửa
   bằng chứng). Chỉ cần **ghi chú** rằng kết luận `asset_type` đã được T24 thay thế.
4. **[M-03]** Sửa 3 câu *"0 match"* thành *"0 match ở vị trí trích dẫn"*, hoặc dùng `grep -rn … | grep -v EVIDENCE`.
5. **[M-04]** Khi ghi mã HTTP của `doi.org`, ghi rõ **có `-L` hay không** để tránh lệch 202/302 về sau.
6. **[Quy trình — bài học chung]** Đưa **`archived_at`** (HackerOne) và **trạng thái "retired"** (mọi nguồn scope)
   thành **bắt buộc** trong mẫu SCOPE.md, để lớp 1 và lớp 2 không cùng mù một chiều dữ liệu.

---

## 9. GIỚI HẠN (nói thẳng)

- Tôi kiểm **đúng 4 hạng mục Admin giao** (+ DNS như kiểm thêm). Tôi **không** kiểm toàn bộ `T11` của Reviewer1
  hay toàn bộ `T18`.
- **Không đọc được toàn văn S29** (OpenAlex `oa_status=closed`) — như T11 và DeepSeek-Harness, tôi chỉ xác minh **metadata**.
  Điều kiện đảo **vẫn treo**.
- **Không chấm lại điểm tính mới `N`** (ngoài phạm vi T24; D-017 giao ResearchLead).
- Kết quả GraphQL/HTTP **đúng tại thời điểm chạy** (`2026-10-01`); arXiv/HackerOne có thể đổi sau.
- Nhánh `agent/deepseek-harness/T8` **đã tiến tới `5ccb731`** (verify #12, T22) sau mốc Admin chỉ định.
  Tôi kiểm **`ff252f8`** theo đúng chỉ định; phần #12 **chưa** nằm trong phán quyết này.
- Tôi **không** đọc `~/.agentmeet/**/creds.json` hay bất kỳ `agent_token` nào.

---

## 10. XÁC NHẬN CỦA AUDITOR2

- Tôi **không sửa file nào của Admin, DeepSeek-Harness, Reviewer1 hay agent khác.** Diff của
  `agent/auditor-2/T24` chỉ chạm `reviews/AUDIT3.md`, `reviews/AUDIT3.json`, `agents/auditor2/**`.
- `AUDIT.md` / `AUDIT.json` / `AUDIT2.md` / `AUDIT2.json` **giữ nguyên** (đã ở `main` = vết kiểm toán).
- Tôi **không merge `main`**.
- **BÁO NGƯỜI DÙNG:** có — qua báo cáo phòng `[AUDIT3]` và return:
  **T18 ĐẠT và ĐỦ TƯ CÁCH làm nguồn thứ hai** (S31 byte-exact, DOI đúng, T19 đúng, khóa băm 3/3 khớp,
  bằng chứng đóng băng, tái lập lần ba khớp). **Nhưng câu hỏi trung tâm phải sửa đáp án: 0 xung đột hiệu lực,
  không phải 2 hay 4** — cả hai kiểm định viên trước cùng thiếu chiều `archived_at`.
  **Không phát hiện bịa đặt, làm giả, thổi phồng hay vi phạm territory.**

**Mốc hiệu lực:** `main` = `e8c45a07b73640c68f12b1252f04300ebbae041a`; đối tượng = `agent/deepseek-harness/T8` @ `ff252f8`.
