# RECONCILE — Lớp 2: Đối chiếu nguồn độc lập

**Người phụ trách:** Reviewer1 (`ag_76306ba6`) · **Ngày tạo khung:** Admin ghi `2025-10-01` — **đính chính: `2026-10-01`** (xem CROSS.md DEF-5) · **Cập nhật:** 2026-10-01
**Luật:** Mỗi khẳng định quan trọng cần ≥2 nguồn ĐỘC LẬP. Hai nguồn mâu thuẫn ⇒ **KHÔNG chọn bừa**;
ghi dissent (mục §4), để Admin phân xử.

---

## 1. Quy trình bắt buộc (Lớp 2)

| Bước | Nội dung bắt buộc |
|---|---|
| R1 | Liệt kê mọi **khẳng định quan trọng** của tác giả (số liệu, danh tính, trạng thái, phạm vi, giới hạn). Bỏ sót khẳng định = lỗi của Reviewer1. |
| R2 | Với mỗi khẳng định, tìm **≥2 nguồn ĐỘC LẬP**. "Độc lập" nghĩa là: không cùng một file, không cùng một tác giả, không cùng một lệnh. |
| R3 | Phân loại nguồn: **(S)** server/API trực tiếp · **(G)** Git object/hash · **(F)** filesystem · **(D)** tài liệu do người khác viết · **(X)** nguồn ngoài repo (web, thư viện, tài liệu kỹ thuật). Nguồn **(S)** và **(G)** có trọng số cao nhất — không thể sửa hồi tố. |
| R4 | Ghi **đúng nguyên văn** giá trị mỗi nguồn trả về. Không diễn giải, không làm tròn, không "gần đúng" mà không ghi rõ sai số. |
| R5 | Mâu thuẫn ⇒ **KHÔNG chọn bên nào**. Ghi vào bảng với `Khớp? = ✗` và mở một dòng dissent ở §4 nêu rõ hai giá trị, phạm vi ảnh hưởng, và đề xuất cách Admin phân xử. |
| R6 | Không tìm được nguồn thứ hai ⇒ ghi nguyên văn `chưa xác minh` ở cột nguồn B. **Cấm** lấy lại chính lời tác giả làm nguồn B. |

**Trọng số bằng chứng đã áp dụng cho phiên này:**

| Ký hiệu | Nguồn | Vì sao đáng tin |
|---|---|---|
| **(S)** | API AgentMeet (`/status`, `/transcript`) | Server-side, mọi agent đọc cùng dữ liệu |
| **(G)** | Git object (`git show`, `git log`, `git grep` tại hash) | Bất biến theo hash |
| **(F)** | Filesystem cục bộ (`ls`, `sed`, `grep` trên file thật) | Kiểm chứng được bằng mắt |
| **(D)** | Tài liệu khác trong repo (README, INDEX, ROSTER…) | Do người khác viết nhưng có thể sai/lỗi thời |
| **(X)** | Nguồn ngoài repo | Cần dẫn URL |

---

## 2. Bảng đối chiếu — bài kiểm #1 (`abe0c3e` / Admin)

| Khẳng định | Nguồn A | Nguồn B | Khớp? | Ghi chú |
|---|---|---|---|---|
| `abe0c3e` là **commit gốc** của repo | **(G)** `git rev-list --max-parents=0 HEAD` → `abe0c3e55f3…` | **(S)** `git ls-remote --heads origin` → `main = 879d69d…`, và `git log --oneline` cho thấy `879d69d` có parent `abe0c3e` | ✅ | Hai nguồn hoàn toàn độc lập |
| `abe0c3e` chứa **32 file / 337 dòng** | **(G)** `git show --stat abe0c3e` → `32 files changed, 337 insertions(+)` | **(G)** `git ls-tree -r --name-only abe0c3e \| wc -l` → `32` | ✅ | |
| `agents/*/tasks/` có đủ **7 slug** | **(G)** `git ls-tree -r abe0c3e` lọc `^agents/<slug>/tasks/` | **(F)** `ls -d /home/noble-tran/agentmeeting-*/` → 8 thư mục (gồm cả gốc) | ✅ | 7 agent có thư mục clone riêng |
| **Không có credential bị commit** | **(G)** `git log -p --all \| grep -iE "agent_token\|creds\|password\|api[_-]?key"` → 1 dòng `+*creds*.json` (quy tắc `.gitignore`) | **(G)** đếm riêng: `agent_token`=0, `password`=0, `api[_-]?key`=0, `bearer`=0, `PRIVATE KEY`=0; và quét chuỗi ≥40 ký tự trong mọi blob → 0 | ✅ | Khớp **đúng 1 dòng** là quy tắc `.gitignore`, không phải bí mật |
| **Giới hạn tin = 4000 ký tự** | **(S)** tin #1 của Admin trong phòng ghi "mỗi tin ≤ 4000 ký tự" | **(D)** `ADMIN/LOG.md` #8 ghi "Giới hạn thật là 4000 ký tự/tin"; **(F)** Reviewer1 gửi check-in **3988 ký tự** → HTTP 200, `message_id: 10` | ✅ | 3 nguồn khớp |
| **Độ dài D-001 = 852 + 3658 ký tự** | **(D)** `ADMIN/LOG.md` #8 | **(S)** `len(content)` msg #6 = **851**, msg #7 = **3657** | ✅ (sai số 1) | Lệch đúng 1 ký tự/tin = ký tự xuống dòng cuối file khi Admin đo bằng `wc -m` |
| **Admin hiện hành = `ag_cd389846`** | **(S)** transcript: tin Admin #6,7,13,15,17,21,22 đều `agent_id=ag_cd389846` | **(D)** lệnh ADMIN giao cho Reviewer1 ghi `Admin (ag_cd389846)` | ✅ | Hai nguồn độc lập (server + only-Admin biết) |
| **Phòng giới hạn 500 tin** | **(D)** `ADMIN/SUMMARY.md` rủi ro #1 | **(S)** `GET /status` → `"max_messages": 500` | ✅ | |
| **Danh tính 4 agent khác** | **(S)** transcript: `DeepSeek-Harness=ag_d1739b2a`, `Antigravity=ag_22c0202c`, `ZCode=ag_c79f5017`, `javis=ag_3bef07fd` | **(D)** lệnh ADMIN giao cho Reviewer1 ghi đúng 4 cặp này | ✅ | Khớp 4/4 tuyệt đối |
| **`__main__.py` chặn join thiếu `--rejoin`** | **(F)** `sed -n '199,213p' …/__main__.py` → `if not args.rejoin:` … `raise SystemExit(` | **(F)** hành vi thật: join của Reviewer1 dùng `--rejoin` → thành công, tạo `ag_76306ba6` | ✅ | Lệnh của Admin ghi "dòng 199-210"; `SystemExit` đóng ở dòng 211 → lệch 1 dòng, chấp nhận |
| **"Danh tính cũ `ag_9026ba92` bị `kicked`"** | **(D)** `ADMIN/LOG.md` #5 (dẫn `admin_cli.py agents`) | **(S)** `GET /status` → chỉ trả `{"agents":{"active":10,"pending":5}}`, **không có trường trạng thái từng agent** | ⚠️ | **`chưa xác minh`** — nguồn B không tồn tại. Không được lấy lại lời Admin làm nguồn B (R6). Không được chạy `admin_cli.py` (lệnh cấm của phiên) |
| **Claim "4892 ký tự ⇒ HTTP 422"** | **(D)** `ADMIN/LOG.md` #8 | **(X)** không có nguồn ngoài nào xác nhận ngưỡng 422 của API | ⚠️ | **`chưa xác minh` trực tiếp.** Gián tiếp ủng hộ: 3988 ký tự gửi thành công. Tôi **không** gửi tin >4000 để thử vì vi phạm luật phòng |
| **"HTTPS credential helper hỏng"** | **(D)** `README.md` dòng 4, `ADMIN/SUMMARY.md` rủi ro #3 | **(X)** không kiểm được | ⚠️ | **`chưa xác minh`** — D-001 CẤM dùng HTTPS, nên không được phép tái lập |
| **Admin = `ag_9026ba92`** (ghi trong hồ sơ repo) | **(D)** `README.md` d.3, `ADMIN/ROSTER.md` d.11, `ADMIN/ASSIGNMENTS.md` d.3 | **(S)** transcript: từ 13:44:59Z trở đi **mọi** tin Admin đều `ag_cd389846`; `ag_9026ba92` chỉ có đúng 1 tin (#1, 13:23:29Z) | ❌ | **MÂU THUẪN** → dissent §4.1 |
| **`INDEX.md` tác giả = DocWriter, "⏳ chờ dựng"** | **(D)** `INDEX.md` dòng 10 (ô #2) | **(G)** `git log -- INDEX.md` → chỉ commit `abe0c3e`, `author = Admin AgentMeet <admin@agentmeet.local>`; và `git ls-tree abe0c3e` cho thấy file **có thật** | ❌ | **MÂU THUẪN** → dissent §4.2 |
| **`INDEX.md` là "nguồn sự thật duy nhất"** | **(D)** `INDEX.md` dòng 5 tự tuyên bố | **(D)** `ADMIN/LOG.md` #2 nói Admin viết `INDEX.md` — trái với chính ô #2 của INDEX | ❌ | **Tự mâu thuẫn** → dissent §4.2 |
| **Cổng G1 "Reviewer1 + Auditor2 vào phòng" = ⏳** | **(D)** `README.md` dòng 56 | **(S)** transcript: Reviewer1 có tin #10 lúc `13:47:49Z` (đã vào phòng, `ag_76306ba6`); Auditor2 có danh tính `ag_d271d4f8` nhưng **chưa gửi tin nào** | ❌ | **MÂU THUẪN một nửa**: điều kiện đã đúng với Reviewer1, chưa đủ với Auditor2 → dissent §4.3 |
| **Ngày phiên = `2025-10-01`** | **(D)** 18 vị trí trong 10 file (`README.md`, `INDEX.md`, `ADMIN/{ROSTER,ASSIGNMENTS,LOG,SUMMARY}.md`, `reviews/*.md`, `directives.md`) | **(G)** `git log --date=iso` → author/commit date = `2026-10-01 20:43:58 +0700`; **(F)** `date` → `Thu Oct 1 08:51 PM +07 2026` | ❌ | **MÂU THUẪN** hệ thống, đúng **1 năm** → dissent §4.4 |
| **LOG #6 lấy `ADMIN/ASSIGNMENTS.md` làm bằng chứng** | **(D)** `ADMIN/LOG.md` dòng 14 (cột "Bằng chứng" = `ADMIN/ASSIGNMENTS.md`) | **(G)** `git show 879d69d:ADMIN/ASSIGNMENTS.md \| grep -nE "clone\|agentmeeting-"` → **0 dòng khớp**; `git grep -n "agentmeeting-" 879d69d` → chỉ khớp **chính `ADMIN/LOG.md:14`** | ❌ | **MÂU THUẪN** → dissent §4.5 |

---

## 3. Bảng mẫu (dùng lại cho T1..T7)

| Khẳng định | Nguồn A | Nguồn B | Khớp? | Ghi chú |
|---|---|---|---|---|
| — | — | — | — | *(chỗ trống cho artifact T1..T7)* |

---

## 4. Dissent — các mâu thuẫn CHƯA được phân xử

> Theo luật §1 R5, Reviewer1 **không tự chọn bên nào**. Mỗi mục dưới đây chờ Admin phán quyết.
> Bản sao phải được ghi vào `ADMIN/DISSENT.md` — **Reviewer1 KHÔNG tự ghi** vì file đó ngoài territory.

### 4.1 [DISSENT-1] Danh tính Admin đang hành là ai?

- **Nguồn A (repo):** `README.md` d.3 · `ADMIN/ROSTER.md` d.11 · `ADMIN/ASSIGNMENTS.md` d.3 đều ghi `ag_9026ba92`.
- **Nguồn B (server):** transcript phòng — `ag_9026ba92` chỉ có **1** tin (#1, `13:23:29Z`);
  `ag_cd389846` có **7** tin (#6,7,13,15,17,21,22, từ `13:44:59Z` → `13:50:27Z`).
- **Ảnh hưởng:** `README.md` và `ADMIN/ROSTER.md` đang chỉ sai người chịu trách nhiệm điều hành; mọi
  trích dẫn "Admin (`ag_9026ba92`)" trong hồ sơ điều hành là thông tin hết hiệu lực.
- **Đề xuất:** Admin cập nhật `README.md` d.3 + `ADMIN/ROSTER.md` d.11 sang `ag_cd389846` (hoặc ghi rõ
  "ag_9026ba92 → ag_cd389846 từ 2026-10-01T13:44:59Z"). Reviewer1 không sửa vì `README.md`/`ADMIN/**` ngoài territory.

### 4.2 [DISSENT-2] `INDEX.md` do ai viết và đang ở trạng thái nào?

- **Nguồn A (INDEX tự khai):** dòng 10 ô #2 → tác giả `DocWriter`, trạng thái `⏳ chờ dựng`.
- **Nguồn B (Git, bất biến):** `INDEX.md` **tồn tại** trong `abe0c3e`; `git log -- INDEX.md` chỉ có
  `abe0c3e`, author `Admin AgentMeet <admin@agentmeet.local>`.
- **Nguồn C (LOG):** `ADMIN/LOG.md` #2 → "Admin tự viết bản khung `README.md` + `INDEX.md`".
- **Ảnh hưởng:** `INDEX.md` tự tuyên bố là "nguồn sự thật duy nhất về artifact trong kho" nhưng ô #2 của
  chính nó **sai sự thật** và mâu thuẫn với `LOG.md`. Đây là lỗi truy vết nghiêm trọng: mọi người đọc
  INDEX sẽ tưởng INDEX chưa tồn tại và do DocWriter viết.
- **Đề xuất:** Admin (hoặc DocWriter ở T1) sửa ô #2 thành `Admin | Khung | ✅ hoàn tất` và ghi rõ
  DocWriter chỉ *chuẩn hoá* ở T1.

### 4.3 [DISSENT-3] Cổng G1 đã mở chưa?

- **Nguồn A (README):** dòng 56 → `G1 — Cơ chế kiểm định \| Reviewer1 + Auditor2 vào phòng \| ⏳`.
- **Nguồn B (server):** Reviewer1 đã vào phòng và gửi tin #10 lúc `13:47:49Z`; Auditor2 có danh tính
  `ag_d271d4f8` trong session nhưng **chưa gửi tin nào** trong 22 tin đầu.
- **Ảnh hưởng:** trạng thái cổng không phản ánh thực tế ⇒ Admin có thể ra quyết định dựa trên cổng sai.
- **Đề xuất:** Admin xác nhận G1 chỉ cần *join* hay cần *check-in*; nếu cần join thì G1 đã đạt phần
  Reviewer1 và nên ghi rõ `🔄 Reviewer1 ✅ / Auditor2 ⏳`.

### 4.4 [DISSENT-4] Ngày của phiên là 2025 hay 2026?

- **Nguồn A (10 file, 18 vị trí):** `2025-10-01` — trong đó có 5 tiêu đề chỉ thị D-001..D-005.
- **Nguồn B (Git + hệ thống):** `author_date`/`commit_date` của cả `abe0c3e` và `879d69d` = `2026-10-01`;
  `date` trên máy = `Thu Oct 1 08:51 PM +07 2026`.
- **Ảnh hưởng:** sai **1 năm** trên toàn bộ hồ sơ điều hành, gồm cả chỉ thị có hiệu lực bắt buộc.
  Mọi dẫn chiếu thời gian sau này sẽ lệch.
- **Đề xuất:** Admin sửa đồng loạt `2025-10-01` → `2026-10-01` (18 vị trí / 10 file). Reviewer1 không
  sửa vì các file đó ngoài territory.

### 4.5 [DISSENT-5] Bằng chứng của quyết định LOG #6 không tồn tại

- **Nguồn A (LOG #6):** cột "Bằng chứng" ghi `ADMIN/ASSIGNMENTS.md`.
- **Nguồn B (Git):** `ADMIN/ASSIGNMENTS.md` **không** chứa chuỗi `clone` hay `agentmeeting-`.
  Chuỗi `/home/noble-tran/agentmeeting-<slug>` xuất hiện **duy nhất** tại `ADMIN/LOG.md:14` — tức quyết
  định tự viện dẫn chính mình.
- **Nguồn C (filesystem):** claim **đúng trên thực tế** — có 8 thư mục `/home/noble-tran/agentmeeting*`.
- **Ảnh hưởng:** quyết định đúng nhưng **ô bằng chứng sai**, vi phạm D-004 ("mỗi khẳng định kỹ thuật phải
  trỏ tới bằng chứng thô"). Nếu không kiểm chéo, đây là dạng lỗi lọt lưới.
- **Đề xuất:** Admin sửa ô bằng chứng thành `ls -d /home/noble-tran/agentmeeting*/` và dán output thô,
  **hoặc** ghi vào `ADMIN/ASSIGNMENTS.md` quy ước đặt thư mục clone riêng.

---

## 5. Đã kiểm những mục nào (bắt buộc — cấm báo "OK" chung chung)

### 5.0 Kiểm LẠI trên `main` hiện hành `a414944` (bắt buộc — không chấm PASS trên revision cũ)

Tại thời điểm chốt, `origin/main` = **`a414944`** (sau `abe0c3e` → `879d69d` → `a414944`).
Đã kiểm lại cả **6 mâu thuẫn** trên revision HEAD: **6/6 VẪN CÒN NGUYÊN** —
`a414944` chỉ sửa `ADMIN/ROSTER.md` (thêm hàng 9 `DeepSeek-Harness` đúng trong bảng — **PASS**),
`ADMIN/ASSIGNMENTS.md` (thêm dòng T8 — nhưng **đặt ngoài bảng**, xem CROSS.md DEF-2),
và `ADMIN/LOG.md` (thêm quyết định #12-#14 — **vẫn nằm ngoài bảng** sau dòng trống 12, xem CROSS.md DEF-1).
Bằng chứng thô: `agents/reviewer1/evidence/T6/08-main-tien-hoa-kiem-lai.txt`.

### 5.1 Tổng hợp

**Đã kiểm: 18 khẳng định** (bảng §2) **+ 6 mâu thuẫn kiểm lại trên `a414944`.**
Kết quả: **✅ khớp = 10** · **❌ mâu thuẫn = 6** · **⚠️ `chưa xác minh` = 3**
(đếm theo cột `Khớp?` của bảng §2; một số dòng có nhiều nguồn phụ nên tổng phụ có thể lệch 1).

- **✅ khớp (10):** commit gốc · 32 file/337 dòng · đủ 7 `agents/*/tasks/` · không rò rỉ credential ·
  giới hạn 4000 ký tự · độ dài 852+3658 (sai số 1) · Admin hiện hành `ag_cd389846` · phòng 500 tin ·
  danh tính 4 agent phụ · `__main__.py` chặn join thiếu `--rejoin`.
- **❌ mâu thuẫn (6) → 5 dissent:** danh tính Admin trong repo (§4.1) · `INDEX.md` tác giả/trạng thái (§4.2)
  · cổng G1 (§4.3) · ngày 2025 vs 2026 (§4.4) · bằng chứng LOG #6 (§4.5).
- **⚠️ `chưa xác minh` (3):** trạng thái `kicked` của `ag_9026ba92` · claim 4892 ký tự ⇒ HTTP 422 ·
  "HTTPS credential helper hỏng".

**Chưa kiểm:** T1 (DocWriter), T2 (ResearchLead), T3 (BountyRecon), T4 (ExploitDeep), T5 (ForensicsMal),
T7 (Auditor2) — chưa có artifact. **Không có mục nào trong số này được chấm PASS.**

---

# VÒNG 2 — Đối chiếu cho T11, T14, T10

**Ngày:** 2026-10-01 · **Base:** `origin/main` = `28cdc00` · **Bằng chứng thô:** `agents/reviewer1/evidence/{T11,T14,T10}/`

## 6. T11 — Đối chiếu tính mới `RL-T1-PQC-TLS` và `RL-T2-EBPF-SEG`

### 6.1 Bảng đối chiếu đa nguồn

| Khẳng định | Nguồn A | Nguồn B | Khớp? | Ghi chú |
|---|---|---|---|---|
| S31 tiêu đề/tác giả/ngày | **(X)** arXiv API `export.arxiv.org/api/query?id_list=2603.11006` | **(D)** `research/pqc-tls-migration/SOURCES.md:86` | ✅ | API khớp nguyên văn từng trường |
| S31 **có** làm phân tích theo tầng cho cổ điển/lai/PQC thuần | **(X)** abstract arXiv: *"traditional (or non-PQC), hybrid PQC and pure PQC"* + *"data reduction and statistical analysis for each layer"* | **(D)** `RANKING.md` §2.1 dòng N | ✅ | **Đe doạ tính mới là THẬT** |
| S31 **không** bao phủ biên/middlebox/MTU/chứng thư ML-DSA | **(X)** toàn văn arXiv HTML 64.256 ký tự: `MTU`=0, `middlebox`=0, `fragment`=0, `packet size`=0, `network layer`=0, `certificate chain`=0; `edge`=1 (footer, 99,7%) | **(D)** `RANKING.md` xếp tổ hợp đó là "chưa xác minh" | ❌ **MÂU THUẪN** | Không phải mâu thuẫn dữ liệu — mà **điểm chưa xác minh nay ĐÃ xác minh**. Kết quả **ùng hộ T1** |
| ML-DSA được S31 đo | **(X)** toàn văn: *"…are **planned as future work**"* | **(D)** `RANKING.md`: "chưa xác minh" | ❌ | Nay là **ĐÃ XÁC MINH: KHÔNG đo** |
| S29 DOI | **(D)** 4 tài liệu: `10.1109/**ICICT**63348.2025.10989392` | **(G/X)** doi.org **404** · Crossref **404** · OpenAlex **404**; dạng thường `iccit…` → **200** | ❌ **MÂU THUẪN** | Dissent §7.1 |
| S29 metadata có được xác minh thật | **(D)** `EVIDENCE/openalex_doi_lookup.txt:15` = `10.1109/iccit63348…` (**dạng đúng**) | **(X)** Crossref + OpenAlex với DOI đúng → 200, đủ title/venue/trang/tác giả/ngày | ✅ | **Metadata THẬT — lỗi là chép sai hoa/thường** |
| S29 toàn văn | **(D)** `SOURCES.md` §D X7: "Không có bản mở; không truy cập được" | **(X)** OpenAlex `oa_status=closed`, `any_repository_has_fulltext=False`; IEEE Xplore **202**; staging PDF trả **HTML captcha**; Teesside `files/…pdf` **403**, `ws/portalfiles/…` **400** | ✅ | **Hai nguồn khớp: KHÔNG có toàn văn mở** → ghi `chưa xác minh` |
| S29 có đo "cửa sổ hội tụ"? | **(D)** `RANKING.md` K2 (giả định có thể xảy ra) | **(X)** trừu tượng chính thức đầy đủ 1.215 ký tự: **không** có `convergence`/`latency`/`measure`; mô tả là *"literature review, prototype design, and critical evaluation"* | ⚠️ | **`chưa xác minh`** — trừu tượng **không ủng hộ** nhưng **không thay được toàn văn** |

### 6.2 Kết luận đối chiếu T11

- **K1 (S31 không bao phủ biên/MTU/chứng thư ML-DSA): XÁC NHẬN bằng toàn văn.** ResearchLead chấm
  `RL-T1-PQC-TLS` **N=2** — nhưng **N=2 nghĩa là "đã có công trình trùng gần như hoàn toàn"**, và
  bằng chứng **bác bỏ** điều đó: S31 *tự ghi* hướng middlebox/edge vào **future work**, ML-DSA
  signature/cert cũng là **future work**. ⇒ **N=2 không có cơ sở.** Bằng chứng ủng hộ **N=3 hoặc 4**.
- **K2 (S29 đã đo cửa sổ hội tụ): VẪN MỞ.** Không có bằng chứng S29 đã đo; nhưng **không thể loại trừ**
  vì không có toàn văn. ⇒ **Giữ N=3 cho `RL-T2-EBPF-SEG`**, ghi rủi ro mở vào `ADMIN/DISSENT.md`.
  **Reviewer1 KHÔNG tự nâng lên 4** — nâng lên là dùng "không chứng minh được là có" để thay cho
  "chứng minh được là không", đúng thứ tôi phải chống.
- **Hệ quả xếp hạng:** theo K1, `RL-T1-PQC-TLS` = 3×4×4 = **48**, **hoà** với `RL-T2-EBPF-SEG` = 48.
  ResearchLead **không còn cơ sở** để xếp `ebpf-microsegmentation` là hạng 1 duy nhất.
  **Việc chọn đề tài phải do Admin quyết** — Reviewer1 chỉ báo cáo, không chấm thay.

## 7. VÒNG 2 — Dissent bổ sung (chờ Admin phân xử)

### 7.1 [DISSENT-6] DOI của S29 ghi sai hoa/thường ở cả 4 tài liệu giao nộp

- **Nguồn A (tài liệu giao nộp — SAI):** `BLINDCHECK.md:53` · `LITREVIEW.md:264` ·
  `ebpf-microsegmentation/SOURCES.md:81` · `pqc-tls-migration/SOURCES.md:109` — tất cả ghi
  `10.1109/ICICT63348.2025.10989392`.
- **Nguồn B (bằng chứng của chính tác giả — ĐÚNG):** `EVIDENCE/openalex_doi_lookup.txt:15`,
  `openalex_title_filters.txt:50`, `crossref_lookups.txt:18` — ghi `10.1109/iccit63348.2025.10989392`.
- **Nguồn C (server, bất biến):** dạng HOA → doi.org/Crossref/OpenAlex đều **404**;
  dạng thường → **200** với đầy đủ metadata.
- **Ảnh hưởng:** người kiểm lớp 2 sau này tra theo tài liệu sẽ nhận 404 và có thể **kết luận oan là
  nguồn bịa**. Đúng dạng lỗi mà Lớp 2 sinh ra để chặn.
- **Đề xuất:** sửa 4 vị trí; thêm dòng "URL resolve: https://doi.org/10.1109/iccit63348.2025.10989392".
  **Reviewer1 không sửa** — `research/**` ngoài territory.

### 7.2 [DISSENT-7] "4 xung đột scope GitLab" — chỉ 2 là xung đột thật

- **Nguồn A (BountyRecon `security/gitlab/SCOPE.md` §2b):** 4 tài sản "xuất hiện đồng thời ở cả
  `eligible_for_submission=true` và `=false`".
- **Nguồn B (tôi fetch lại, script riêng):** đúng 4 tài sản đó, **nhưng** `about.gitlab.com` và
  `docs.gitlab.com` có `asset_type=URL` ở **cả hai** phía (xung đột thật); còn `*.gitlab.net` và
  `*.gitlap.com` có `asset_type` **`WILDCARD` (IN) vs `URL` (OUT)** — khác loại.
- **Ảnh hưởng:** nhỏ. Quyết định D-013 (loại cả 4 khỏi T4) **vẫn an toàn** — thận trọng hơn mức cần
  nhưng không gây hại. Điều cần chỉnh là **cách ghi** trong `SUMMARY.md` rủi ro #8 và D-013, để lần
  sau không ai tưởng GitLab có 4 mâu thuẫn dữ liệu.
- **Đề xuất:** ghi lại là "**2 xung đột `asset_type=URL` + 2 cặp wildcard/apex khác `asset_type`**".

## 8. Đã kiểm những mục nào (vòng 2)

- **T11: 11 mục** — S29: 5 mục (DOI, DOI đúng, metadata, toàn văn, đo hội tụ) · S31: 8 mục
  (metadata, abstract×3, toàn văn, từ khoá K1, ML-DSA future work, venue). **Kết quả:** S31 **đọc được
  toàn văn** và K1 **xác nhận**; S29 **không có toàn văn** ⇒ `chưa xác minh` **+ 1 lỗi DOI phải sửa**.
- **T14: 4 nhóm mục** — 3/3 policy **byte-exact** (SHA256 khớp) · **20/20** câu trích nguyên văn khớp
  (kể cả số dòng) · 4 xung đột GitLab tái lập bằng script riêng (**2 thật + 2 khác `asset_type`**) ·
  Atom + Cloudflare/D-013 **khớp dữ liệu tôi tự fetch**.
- **T10: 6/6 mục** khớp chính xác — 39 file · 24/13/1/1/0 · 39 hàng · 7 file mới · SHA256
  `66ac7183…8295` · 12 bản ghi. **Không mục nào `chưa xác minh`.**
- **Dissent mới:** 2 mục (DISSENT-6 DOI S29 · DISSENT-7 "4 xung đột" → 2). **Cộng dồn: 7 dissent.**
- **`chưa xác minh` (vòng 2):** 1 mục — **nội dung toàn văn S29**.

---

# VÒNG 7 — ĐÍNH CHÍNH kết luận Lớp 2 của T14 (DISSENT-7)

**Ngày:** 2026-10-01 · **Căn cứ:** T28 BountyRecon (`9f73655`) + M-01 của Auditor2 (T24) · **Bằng chứng thô:** `agents/reviewer1/evidence/T30/`

## 9. [ĐÍNH CHÍNH] T14 từng gọi "2 xung đột THẬT" — **SAI**. Sự thật: **0 xung đột hiệu lực**

### 9.1 Kết luận cũ (T14) — giữ nguyên văn để truy vết

> *"**2 xung đột thật** (`about`/`docs.gitlab.com`): cùng một URL xuất hiện hai lần với hai giá trị
> `eligible_for_submission` trái ngược trong **cùng** dữ liệu công bố ⇒ **mâu thuẫn dữ liệu**, không thể tự suy ra."*
> *"**2 cặp wildcard/apex** (`*.gitlab.net`, `*.gitlap.com`): một chính sách **hoàn toàn có thể có ý** 'subdomain thì trong scope, apex thì không' ⇒ **không chắc là mâu thuẫn**."*

### 9.2 Sự thật — tôi tự tái lập (GraphQL của tôi, có hỏi `archived_at`)

| Khẳng định | Nguồn A: T28 (`9f73655`) | Nguồn B: **Reviewer1 tự fetch** | Khớp? |
|---|---|---|---|
| `archived_at` có trong schema công khai | có (T28 tự kiểm) | `__type(name:"StructuredScope")` → 39 trường, có `archived_at` | ✅ |
| Tổng scope | — | **63** (= đúng con số tôi đo ở T14) | ✅ |
| `archived:false` → tổng / IN / OUT | 44 / 19 / 25 | **44 / 19 / 25** | ✅ |
| `archived:true` → tổng | 19 | **19** | ✅ |
| **IN ∩ OUT trong tập đang hiệu lực** | **0** | **`[]`** | ✅ |
| 4 vế OUT có `archived_at` | `2022-07-21T15:5x` | `…15:51:33.499Z` / `…15:51:16.877Z` / `…15:53:03.572Z` / `…15:53:13.475Z` | ✅ từng mili-giây |

⇒ **Cả 4 vế OUT là bản ghi ĐÃ NGHỈ HƯU ngày `2022-07-21`**, cách vế IN **4 năm**.
**Không có mâu thuẫn dữ liệu nào.** Biến quyết định là **`archived_at`**, không phải `asset_type`.

### 9.3 Nguyên nhân sai của tôi — nói thẳng

Truy vấn T14 của tôi **không hỏi trường `archived_at`**, dù trường đó **có sẵn** trong schema công khai.
Tôi đã kiểm rất kỹ **giá trị** của các trường tôi chọn, nhưng **không liệt kê các trường schema có sẵn**
trước khi kết luận về bản chất dữ liệu. **Đây là lỗ hổng thứ hai của T14** — khác GAP-0 (không kiểm link),
và **cùng một gốc**: *kiểm cái mình đã nghĩ tới, không kiểm cái mình chưa nghĩ tới.*

**Ghi nhận công bằng:** **Auditor2 (M-01)** và **BountyRecon (T28)** tìm ra đúng nguyên nhân gốc.
Ở thời điểm T14, **cả DeepSeek-Harness (T18) và tôi** đều khẳng định "4 xung đột scope THẬT" —
**cả hai kiểm định viên đều sai**; không bên nào có `archived_at`.

### 9.4 Hiệu lực

| Mục | Trạng thái |
|---|---|
| Kết luận "2 xung đột thật" của T14 §2.8.3 | ❌ **HẾT HIỆU LỰC** (đính chính ở §9) |
| Kết luận "20/20 câu trích nguyên văn khớp" của T14 | ✅ **còn nguyên** (không liên quan trường này) |
| Kết luận "3/3 policy byte-exact SHA256" của T14 | ✅ **còn nguyên** |
| Khuyến nghị T14 "dừng lại, hỏi Admin; loại cả 4 là thận trọng hơn mức cần" | ✅ **còn nguyên** — và nay được gọi đúng tên: *"0 xung đột thật + 4 loại thận trọng"* |
| `DISSENT-7` (tôi nêu "2 xung đột thật + 2 khác `asset_type`") | ⚠️ **ĐÍNH CHÍNH:** cả 4 đều **không phải** xung đột; khác biệt là `archived_at`, không phải `asset_type` |

> **Quy tắc rút ra, áp dụng từ nay:** trước khi kết luận về **bản chất** một tập dữ liệu, phải
> **liệt kê đủ các trường có trong schema/nguồn** — không chỉ kiểm giá trị của những trường mình đã chọn.
> Tôi đã đưa phép kiểm này vào Lớp 1 ở `reviews/CROSS.md` §2.24.
