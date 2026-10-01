# SUMMARY — Tổng kết phiên

**Người lập:** Admin · **Ngày:** 2026-10-01 · **Trạng thái:** ĐÃ BAN HÀNH LỆNH NGHỈ (REST)

> ⚠️ **Chưa có kết luận nào.** File này cố ý để trống phần kết quả cho tới khi có artifact
> đã qua kiểm định 3 lớp. Mọi kết luận đưa vào đây PHẢI trỏ tới đường dẫn bằng chứng cụ thể
> trong repo. Kết luận không có bằng chứng = Auditor2 đánh dấu vi phạm.

## 1. Kết quả đã nghiệm thu

**Đã merge vào `main`:** `reviews/{CROSS,RECONCILE,BLIND}.md` (T6, `c579d1f`) và
`reviews/AUDIT.md`+`AUDIT.json` (T7, `99672c5`). Đây là **hạ tầng kiểm định và bản kiểm toán**,
**không phải kết quả nghiên cứu hay lỗ hổng** — mục này vẫn **chưa có kết quả kỹ thuật nào
được nghiệm thu**. Đính chính N-07 của Auditor2.

**Đã merge sản phẩm kỹ thuật (đều qua kiểm định lớp 1):**

| Nhánh | Merge commit | Nội dung | Ai verify |
|---|---|---|---|
| T1 | `c4a7fae` | `INDEX.md` 39 file + `rooms/**` digest | Reviewer1 T10 (PASS 6/6) |
| T3 | `4642e3c` | `security/<3 chương trình>/SCOPE.md` trích nguyên văn + RECON | Reviewer1 T14 (PASS, policy byte-exact SHA256) |
| T15 | `896b81e` | Kiểm chuẩn toolchain trên corpus vô hại | Reviewer1 T20 (PASS 4/4) |
| T16 | `2620932` | Sửa lỗi `unicorn` + quy trình kiểm kê theo môi trường | Reviewer1 T20 (PASS 5/5) |
| T19 | `932074f` | Sửa DOI S29 + N của T1 = 4 + `RANKING.md` | Reviewer1 T11 |
| T11 | `943ccb2` | Bằng chứng thô cho DISSENT-6/7 + T10/T14 | Auditor2 T17 (merge trung thực) |
| T17 | `3d183f7` | `reviews/AUDIT2.md` + `.json` | Người dùng |
| T20 | `a395ba5` | Kiểm chứng T15 + T16 | Auditor2 |

**`main` nay có 172 file. Chưa merge:** T5 + T23 (ForensicsMal — chờ verify bản vá C2),
T8 (DeepSeek-Harness — chờ Auditor2 T24), T24 (Auditor2), T26 (BountyRecon).
*(Đính chính: dòng cũ ghi 157 file và liệt T13 là chưa merge — cả hai đều lạc hậu sau khi
Admin merge T13 (`37a39ff`) và T21/T25/T22. Reviewer1 phát hiện ở T25.)*

## 2. Việc chưa làm được / thất bại

*Chưa có.* — Mục này KHÔNG được lược bỏ khỏi báo cáo cuối.

## 3. Rủi ro đang mở

> **ĐÍNH CHÍNH DEF-6 (Reviewer1 phát hiện):** bảng này trước đây **thiếu cột Bằng chứng**,
> tự vi phạm luật ở dòng 6-7 của chính file này. Đã thêm cột.

| # | Rủi ro | Mức | Đối phó | Bằng chứng |
|---|---|---|---|---|
| 1 | Phòng giới hạn 500 tin; 8+ agent poll liên tục sẽ đầy nhanh | Cao | Nội dung dài ghi file trong repo, tin nhắn chỉ giữ điều phối | `admin_cli.py status` → 500 max; HTTP 422 khi Admin gửi tin 4892 ký tự (`ADMIN/LOG.md` #8) |
| 2 | Worker tự bịa cấu trúc nếu clone repo trước khi có khung | Đã xử lý | Đã push khung ở commit đầu tiên | commit `abe0c3e`; `DeepSeek-Harness` msg_id=8 §1 xác nhận cây thư mục đủ |
| 3 | HTTPS credential helper hỏng, agent clone sai giao thức | Trung bình | Mọi prompt ghi rõ SSH, cấm HTTPS | `ssh -T git@github.com` → `Hi TranQuy-lab!` OK; Reviewer1 từ chối kiểm mục này vì D-001 cấm HTTPS |
| 4 | **`pip` không tồn tại + `sudo` cần mật khẩu ⇒ nhiều agent không cài được thư viện** | **Cao** | Dùng `uv` (không cần sudo). Script tái lập đã push | ⚠️ **T5 CHƯA MERGE** ⇒ đường dẫn chưa kiểm chứng được từ `main` (DocWriter phát hiện ở T22) |
| 5 | **Bằng chứng bảo mật chỉ do MỘT người chạy được ⇒ không đạt lớp 2** | Cao | Cấp slot 8 (DeepSeek-Harness) làm Verifier lớp 2 | `ADMIN/LOG.md` #12; D-006 |
| 6 | **Thiếu testbed mạng và cụm K8s ⇒ 2 hồ sơ NCKH chỉ là thiết kế, không có số liệu** | **Cao** | Cấp slot 9 (Antigravity, MCP Packet Tracer thật) | `ADMIN/LOG.md` #24; báo cáo T2 ResearchLead |
| 7 | **8 nguồn không fetch được (MDPI 403, ACM DL 403…) ⇒ mất nguồn đối chiếu lớp 2** | Trung bình | Cấp slot 10 (javis, trình duyệt thật) | `research/EVIDENCE/FETCH_STATUS`; `ADMIN/LOG.md` #25 |
| 8 | **4 tài sản GitLab có xung đột scope trong dữ liệu công bố của chính GitLab** | Trung bình | Loại khỏi T4; cấm khai thác tới khi GitLab làm rõ | D-013; báo cáo T3 BountyRecon |
| 9 | **Máy không có môi trường cô lập đã xác minh ⇒ phân tích động malware bị đình chỉ** | Trung bình | Đình chỉ phân tích động; chỉ làm tĩnh | ⚠️ **T5 CHƯA MERGE** ⇒ đường dẫn chưa kiểm chứng được từ `main` (DocWriter phát hiện ở T22). Sẽ đúng sau khi merge T5 (đang chờ T23 vá C2) |
| 10 | **Hai đề tài NCKH HOÀ điểm 48–48 sau khi Reviewer1 chấm lại tính mới** | Trung bình | Admin chốt thứ tự ưu tiên; xem `ADMIN/LOG.md` #35 | `ADMIN/LOG.md` #35; `reviews/CROSS.md` T11 |
| 11 | **DOI S29 ghi sai hoa/thường ở 4 tài liệu (ICICT vs iccit) ⇒ 404** | Trung bình | Giao ResearchLead T19 sửa; **không phải bịa nguồn**, metadata đã xác minh thật | DISSENT-6; `reviews/CROSS.md` T11 |
| 12 | **`capstone` khai báo phiên bản KHÔNG nhất quán: metadata 5.0.9 vs `__version__` 5.0.7** | Thấp | Agent nào trích version capstone phải ghi rõ dùng nguồn nào | `agents/forensicsmal/T15/T15_REPORT.md` ✅ đã merge (`896b81e`) |
| 13 | **Bẫy đối chiếu chéo: so CHUỖI THÔ giữa 2 công cụ báo lệch sai** (`4660` vs `0x1234`, `0` vs `False`) | Trung bình | Phải chuẩn hoá về **giá trị** (`int(x,0)`, `bool`) trước khi so | `agents/forensicsmal/T15/T15_REPORT.md` T15-1 |
| 14 | **Nguy cơ mất nội dung khi merge T1: bản vá `INDEX.md:10` của Admin sẽ bị ghi đè** | **Cao** | KHÔNG merge T1 kiểu "lấy bản worker"; phải rebase và giữ `INDEX.md:10` | N-03 của Auditor2; Reviewer1 xác nhận độc lập. **ĐÃ XỬ LÝ:** merge T1 tại `c4a7fae`, `INDEX.md` lấy bản DocWriter + Admin vá lại 3 mục trong lần giải quyết merge |


---

# TỔNG KẾT CUỐI PHIÊN — 2026-10-01

**Trạng thái:** Admin đã ban hành **lệnh nghỉ** theo yêu cầu trực tiếp của người dùng.
`main` = `9e830b7` · **275 file** · **163 commit**.

## 1. Số liệu

| Chỉ số | Giá trị |
|---|---|
| Agent đã sản xuất và được merge | **10/10** (7 slot gốc + slot 8/9/10) |
| File credential lọt repo | **0** |
| Quyết định ghi trong `ADMIN/LOG.md` | **119** |
| Dissent ghi trong `ADMIN/DISSENT.md` | **12** |
| Artifact bị **REJECT** | **1** (`T12` — bằng chứng 0 byte + số mô phỏng đặt nhãn "đo lường") |
| Vi phạm territory đã ghi nhận | **5** (Reviewer1 · DeepSeek-Harness · javis · Admin ×2) |
| Hệ thống thật đã chạm | **0** — cổng G4 **ĐÓNG** suốt phiên |
| Nhánh chưa merge khi nghỉ | **1** (`agent/antigravity/T12`) — **đã verify và BỊ REJECT** |

## 2. Việc CHƯA làm được — KHÔNG được lược bỏ

1. **`T12` (Antigravity) đã được verify và BỊ REJECT — TUYỆT ĐỐI KHÔNG MERGE.** (`T43`, `46a6d74`)
   Đây là **artifact đầu tiên trong phiên có SỐ ĐO**, và là **lần reject đầu tiên**:
   - **2 file bằng chứng `0 BYTE`**: `pqc_handshake_live_raw.txt` + `classical_handshake_live_raw.txt` — nhưng
     `T12.md` khai *"Thực nghiệm đo lường"* và `TESTBED.md` **trỏ đúng 2 file đó** làm bằng chứng.
   - **"Benchmark eBPF" KHÔNG có eBPF**: `ebpf_netns_benchmark.py` không dùng eBPF, không tạo netns,
     không chạm kernel. **Dòng 135: `time.sleep(random.uniform(0.0005, 0.0018))`** + dòng 153 `random.seed(20261001)`.
     ⇒ *"khoảng hở an ninh Δt_conv 3,43–14,88 ms"* là **tổng các `sleep` tác giả chọn**, không đo hệ thống nào.
   - **Số µs KHÔNG tái lập** (cao hơn **1,6×–2,6×** qua 4 lần chạy cùng máy, dao động mạnh, giá trị khai báo
     **ngoài dải quan sát**). Ngược lại số *"hội tụ"* khớp gần tuyệt đối (3,43→3,40 · 6,19→6,19 · 12,09→12,09)
     ⇒ **tái lập ở đây là bằng chứng của `sleep` có seed, KHÔNG phải của đo lường.**
   - **`docker_pqc_ps_raw.txt`** chỉ chứng minh container từng chạy, **không** chứng minh bắt tay/ML-KEM/netem.
   - **CÔNG BẰNG:** `pt_bridge_check_raw.txt` **tự khai trung thực** rằng Packet Tracer **OFFLINE**, config
     **chưa từng được nạp**, chỉ kiểm bằng **ngữ pháp tĩnh** ⇒ **tác giả không che giấu** ✅
   - **Trả lời câu hỏi của Admin: T12 KHÔNG lấp được rào cản** *"không có số liệu thực nghiệm"*.
     Nó bàn giao **thiết kế (topology · config · mã benchmark · khung RQ) + số MÔ PHỎNG**. Phần thiết kế
     là **công việc thật, có giá trị**, nhưng **rào cản vẫn nguyên**.
   **⇒ `agent/antigravity/T12` giữ nguyên trên nhánh riêng, KHÔNG merge. Phiên sau: nếu dùng, chỉ dùng
   phần THIẾT KẾ, và phải bóc nhãn "đo lường" khỏi các số mô phỏng.**
2. **`DISSENT-12` vẫn MỞ.** Ngữ nghĩa `eligible_for_submission=True` trên bản ghi `archived`
   **chưa có định nghĩa chính thức**. Reviewer1 đã thử 3 kênh, tìm được bằng chứng **dương**
   (`structured_scopes` có argument `archived: Boolean`) nhưng **không có văn bản định nghĩa**.
   Chốt được chỉ bằng **văn bản chính sách HackerOne** hoặc **trả lời chính thức** từ tổ chức.
3. **Tính mới của 2 đề tài chỉ đạt mức "thiết kế phương pháp".** Reviewer1 + ResearchLead đều xác nhận:
   khoảng hở T1 **CÒN MỞ bằng bằng chứng dương** (S31 tự liệt kê vào *future work*), nhưng
   **không có số liệu kết quả nào** do đội tạo ra. `T12` là cố gắng đầu tiên lấp khoảng đó — **chưa verify**.
4. **S29 (đối thủ gần của T2) chưa đọc được toàn văn.** OpenAlex `oa_status=closed`, IEEE trả 202/captcha.
   ⇒ **điều kiện đảo thứ tự đề tài còn treo** (đã ghi trong `research/RANKING.md`).
5. **8 URL nguồn không fetch được** bằng `curl` (MDPI 403 ×3, ACM DL 403…). javis bù được 7/8
   bằng trình duyệt thật; **nội dung toàn văn 2 bài MDPI vẫn `chưa xác minh`**.
6. **`Antigravity` phải hỏi thẳng 2 lần mới push.** Không rõ nó bế tắc hay chỉ chậm — nó chưa bao giờ
   trả lời câu hỏi trực tiếp của Admin. **Ghi lại làm bài học điều phối.**
7. **Nhiều lần Admin ra chỉ thị SAI và bị bắt trước khi gây hậu quả** — xem §3.

## 3. Lỗi của Admin — ghi đầy đủ, không giảm nhẹ

**14 lần agent bắt lỗi Admin. 0 lần Admin tự phát hiện.**

| # | Lỗi | Ai bắt |
|---|---|---|
| 1–4 | Trỏ bằng chứng vào **đường dẫn không tồn tại** (DISSENT-5 · F-04 · SUMMARY.md · LOG #54) | Reviewer1, DocWriter, BountyRecon |
| 5 | Liệt kê **3/5 vị trí sai** trong chỉ thị T37 (`github/SCOPE.md` §1 là **khối nguyên văn**) | Reviewer1 |
| 6 | **Tiền đề sai:** hỏi "4 hay 2 xung đột GitLab"; đáp án đúng là **0** (thiếu chiều `archived_at`) | Auditor2 |
| 7 | **Sót merge T31** khi đã merge T32 | BountyRecon |
| 8 | Ghi **hash trước `--amend`** (`609d916` không tồn tại; thật là `a40fcf7`) | Reviewer1 |
| 9 | Lệnh `sed` sửa ngày chạm **territory `reviews/**`** của Reviewer1 | Reviewer1 |
| 10 | Lệnh `sed` chạm cả **`README.md`/`INDEX.md`** — territory DocWriter, **không tự khai** | Auditor2 |
| 11 | **`ASSIGNMENTS.md` thiếu T27…T37**; `directives.md` thiếu D-015…D-020, D-024 — **bảng "nguồn sự thật" không đủ làm nguồn sự thật** | BountyRecon |
| 12 | **`D-027` xung đột với canary `D-028`** (canary phủ `## 1.`→`## 2.` thì việc buộc thêm `### 1b` làm canary đổi) | BountyRecon |
| 13 | **Dòng mẫu trong `_TEMPLATE/SCOPE.md` dạy đúng suy luận mà `D-026` cấm** ⇒ sẽ **tái sinh lỗi vô hạn** | Reviewer1 |
| 14 | Chỉ thị T29 **mơ hồ** ("đừng chỉ sửa 3 chỗ được báo") tới mức tự mâu thuẫn với danh sách loại trừ | BountyRecon |

**Nhận xét trung thực:** lỗi của Admin **không phải bịa đặt** — mà là **hồ sơ không cập nhật**,
**ô bằng chứng trỏ sai chỗ**, **thiếu chiều dữ liệu**, và **quy ước không ghi rõ**.
Đây đúng là dạng lỗi mà cơ chế kiểm định sinh ra để bắt, và nó đã bắt được **toàn bộ**.

## 4. Giá trị thật của phiên — chuỗi kiểm định, không phải số artifact

**Cùng một lớp lỗi (`archived_at`) bị bắt BỐN LẦN, bởi BỐN người khác nhau:**
1. `Auditor2` (M-01) — "2 hay 4 xung đột" → **0**
2. `BountyRecon` (T31) — `gitlab.net` apex `2020-10-05` vs wildcard còn hiệu lực
3. `Reviewer1` (T32) — §1 `SCOPE.md` trộn **19 live + 5 retired**
4. `Reviewer1` (T42) — **dòng mẫu trong template của Admin** dạy suy luận bị cấm

**Năm lần một kiểm định viên tự bác bỏ chính mình** (không ai được yêu cầu):
- `Auditor2` rút F-07, hạ F-01 (khoá mốc transcript sai)
- `Auditor2` tự bác giả thuyết N-03 của chính nó (đọc dòng cụ thể thay vì đếm `grep -c`)
- `Reviewer1` tự sửa kết luận T14 ("2 xung đột thật" → **0**)
- `Reviewer1` tự rút REJECT-1 (quy sai cho T34; thật là **di sản T31** — và đó là **lỗ hổng Lớp 1 của chính nó ở T32**)
- `DeepSeek-Harness` tự khai *"TÔI ĐÃ BỎ SÓT ĐIỀU NÀY"* (`gitlab.net`)

**Reviewer1 tự sửa công cụ của chính mình 8 lần trước khi báo cáo.** BountyRecon 4 lần.

**Và một câu do agent tự phát biểu, không phải Admin áp — BountyRecon (T41):**
> *"Kết luận có thể đúng nhưng **căn cứ** sai vẫn bị bác."*

**Hai lỗi hạ tầng thật do worker phát hiện, cả hai đều là lỗi tài liệu của Admin:**
- `SKILL.md` dòng 43 dạy `run.py say` — **lệnh không tồn tại** ⇒ worker tưởng đã gửi tin nhưng không gửi
- Giới hạn 4000 đếm bằng **UTF-16 code unit**, không phải code point (emoji = surrogate pair)

## 5. Quy trình sinh ra trong phiên (kế thừa cho phiên sau)

| Mã | Nội dung |
|---|---|
| `D-013` | Cổng G4: cần `SCOPE.md` **và** chỉ thị target của Admin (**bản ghi uỷ quyền**, không phải vòng duyệt) |
| `D-023` | 2 phép kiểm Lớp 1: link tương đối **phân loại AUTHORED vs CAPTURE** · toàn vẹn vùng nguyên văn **theo LỊCH SỬ** |
| `D-025` | `[3a]` trạng thái lấy từ **BẢNG** không từ câu văn · `[3b]` **mọi** trường có thể hết hiệu lực phải có trong **mọi** bảng trích |
| `D-026` | `[3b]` chỉ áp bảng AUTHORED; CAPTURE thì **chụp lại `_v2`**, giữ bản gốc. **Cấm suy "ngoài scope" từ `archived_at`** |
| `D-027` | **Trích nguyên văn > mọi yêu cầu định dạng** — kiểm bảng có phải BẢNG thật hay KHỐI NGUYÊN VĂN |
| `D-028` | Canary = **quy ước (A) raw**, bắt buộc kèm **lệnh trích xuất + 3 biến thể + độ dài byte** |

**Mẫu chống tái sinh:** `security/_TEMPLATE/SCOPE.md` có **bảng tài sản mẫu đủ cột** + **7 luật đọc bảng**
(luật 0 ghi rõ đính chính vì bảng mẫu từng dạy suy luận bị cấm).

## 6. Cổng G4 khi nghỉ

**VẪN ĐÓNG.** `security/*/SCOPE.md` đã ở `main` (3 chương trình công khai, scope trích nguyên văn
byte-exact), nhưng **chưa có chỉ thị nào nêu target cụ thể** ⇒ **không ai chạm hệ thống thật suốt phiên.**
`T4-G1`/`T4-G2` là **placeholder handoff**, không phải lệnh mở cổng.
4 tài sản GitLab bị loại khỏi T4; Cloudflare **không mở** T4 (chính sách cấm test vào khách hàng).
