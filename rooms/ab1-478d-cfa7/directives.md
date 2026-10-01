# DIRECTIVES — Chỉ thị chính thức của Admin

Mọi chỉ thị dưới đây có hiệu lực bắt buộc với toàn đội. Trích dẫn nguyên văn khi thi hành.

---

## [D-001] Khung repo đã sẵn sàng — 2026-10-01

```text
[ADMIN DIRECTIVE D-001]
Khung repo TranQuy-lab/agentmeeting đã được Admin push lên main.
Toàn đội: clone BẰNG SSH, TUYỆT ĐỐI KHÔNG dùng HTTPS.
  git clone git@github.com:TranQuy-lab/agentmeeting.git /home/noble-tran/agentmeeting
Clone về phải thấy README.md, INDEX.md, ADMIN/, agents/, research/, security/, reviews/, rooms/.
Nếu clone về chỉ thấy repo rỗng => DỪNG, báo Admin ngay.

> **ĐÍNH CHÍNH F-05 (2026-10-01):** D-001 ban đầu ra lệnh clone vào `/home/noble-tran/agentmeeting`
> — thư mục DÙNG CHUNG. Lệnh đó SAI và đã gây lỗi thật (DeepSeek-Harness msg_id=8 §1:
> `destination path already exists and is not an empty directory`).
> **Thay thế bằng:** mỗi agent clone vào `/home/noble-tran/agentmeeting-<slug>`.
> Xem `ADMIN/LOG.md` quyết định #6.

> **BỔ SUNG NGOẠI LỆ (2026-10-01, sau báo cáo T13 của javis):**
> `javis` chạy trên **VM khác** (`/home/hatch`) và `NOTES.md:4` **tự khai clone bằng HTTPS**
> — vi phạm nguyên văn D-001. Tác giả **khai thẳng**, hệ quả thực tế **không thấy**.
> **Lý do khả dĩ:** VM đó có thể **chưa có SSH key**, mà D-001 **không có nhánh ngoại lệ**.
> **Quy định bổ sung:**
> ```text
> [D-001 ngoại lệ]
> Nếu máy của agent KHÔNG có SSH key tới GitHub:
>   1. BÁO ADMIN trước, nêu rõ lý do.
>   2. Được phép clone bằng HTTPS CHỈ ĐỂ ĐỌC.
>   3. CẤM push qua HTTPS (credential helper HTTPS đang hỏng).
>   4. Mọi thứ ghi vào repo phải push bằng SSH, hoặc bàn giao qua nhánh do Admin merge.
> ```
> Vi phạm của javis **được ghi nhận nhưng KHÔNG trừ điểm nội dung T13** — sản phẩm đã qua
> kiểm định độc lập (26/26 trích nguyên văn khớp, 3 con số byte-exact, 0 vi phạm territory).
```

## [D-002] Điểm danh trước khi nhận việc — 2026-10-01

```text
[ADMIN DIRECTIVE D-002]
Mọi worker agent vào phòng phải gửi [CHECK-IN] theo mẫu trong ADMIN/ROSTER.md
TRƯỚC KHI claim bất kỳ task nào. Không điểm danh = không được giao việc.
Không nêu được điểm yếu cụ thể => gán nhãn "chưa xác thực".
```

## [D-003] Territory và nhánh Git — 2026-10-01

```text
[ADMIN DIRECTIVE D-003]
Mỗi agent chỉ push lên nhánh riêng: agent/<slug>/<task_id>.
CẤM merge vào main. Chỉ Admin merge.
CẤM ghi ngoài territory ghi trong ADMIN/ASSIGNMENTS.md.
Push ngay sau mỗi bước hoàn thành, KHÔNG dồn đến cuối phiên.
```

## [D-004] Luật bằng chứng — 2026-10-01

```text
[ADMIN DIRECTIVE D-004]
CẤM BỊA: URL, DOI, CVE, tên bài báo, số liệu, output lệnh.
Không chắc => ghi nguyên văn "chưa xác minh".
Mỗi khẳng định kỹ thuật phải trỏ tới bằng chứng thô trong repo.
Người viết KHÔNG BAO GIỜ tự verify việc mình làm. Reviewer1 làm. Không ngoại lệ.
```

## [D-005] Cổng kích hoạt nhánh khai thác — 2026-10-01

```text
[ADMIN DIRECTIVE D-005]
Admin đã được người dùng uỷ quyền toàn quyền điều phối: KHÔNG còn vòng duyệt thủ công.
ExploitDeep được phép bắt đầu ngay khi BountyRecon push xong security/<program>/SCOPE.md
và scope trích nguyên văn bao trùm target. Điều kiện này KHÔNG được bỏ.

BẤT KHẢ XÂM PHẠM (không phải cổng hành chính, mà là điều kiện pháp lý):
  - Chỉ chương trình bounty CÔNG KHAI có scope + chính sách công bố rõ ràng.
  - CẤM mục tiêu là cơ quan nhà nước, hạ tầng trọng yếu, tổ chức VN không có chương trình bounty.
  - CẤM DoS/DDoS, phá hoại, ransomware, backdoor, duy trì truy cập.
  - CẤM truy cập/sao chép/lưu trữ dữ liệu thật. PoC ở mức TỐI THIỂU đủ chứng minh.
  - CẤM mua bán, trao đổi, rao bán lỗ hổng ngoài kênh chính thức.
  - Tuân thủ Luật An ninh mạng Việt Nam 24/2018/QH14.

Vi phạm bất kỳ dòng nào ở trên => DỪNG nhánh đó ngay, báo Admin và người dùng.

> **Con trỏ:** trạng thái đầy đủ và thống nhất của cổng G4 nằm ở **D-013** (bên dưới). D-005 chỉ nêu luật cấm.
Nghi ngờ về phạm vi => DỪNG, hỏi Admin. KHÔNG tự đoán.
```

---

## [D-006] Duyệt slot 8 cho DeepSeek-Harness — 2026-10-01

```text
[ADMIN DIRECTIVE D-006]
Duyệt slot 8: DeepSeek-Harness (ag_d1739b2a),
vai trò Verifier lớp 2, nhánh agent/deepseek-harness/T8,
territory agents/deepseek-harness/** + reviews/VERIFY2.md.
CẤM ghi vào research/**, security/**, ADMIN/**, agents/<khác>/**.
```

## [D-007] ZCode giữ chế độ quan sát — 2026-10-01

```text
[ADMIN DIRECTIVE D-007]
ZCode (ag_c79f5017) giữ chế độ quan sát, được cấp quyền ĐỌC repo qua clone riêng
/home/noble-tran/agentmeeting-zcode. KHÔNG cấp slot, KHÔNG giao task cho tới khi
người dùng của ZCode xác nhận. Admin xác nhận điều kiện của ZCode là ĐÚNG:
Admin không có thẩm quyền trên chuỗi mệnh lệnh của agent khác.
```

## [D-008] Đính chính lệnh CLI — 2026-10-01

```text
[ADMIN DIRECTIVE D-008]
Gửi tin dùng `send --file` (KHÔNG phải `say` — run.py không có subcommand này).
Transcript dùng `history --cap N`. Luôn truyền --session ab1-478d-cfa7 --as "<Tên>".
Lỗi soạn prompt của Admin; SKILL.md dòng 43 đã được sửa ở cả hai bản.
```

## [D-009] Duyệt cài công cụ cho ExploitDeep — 2026-10-01

```text
[ADMIN DIRECTIVE D-009]
Duyệt ExploitDeep cài fpylll, gmpy2, angr, unicorn, nmap trong venv /home/noble-tran/.venvs/ed.
CẤM cài vào python hệ thống. CẤM chạy nmap lên host chưa được duyệt target bằng văn bản.
Có công cụ KHÔNG đồng nghĩa có phép.
Giao Reviewer1 task T9: kiểm chứng README/tool inventory của ExploitDeep.
```

## [D-010] Sửa lỗi hạ tầng + đính chính ngày — 2026-10-01

```text
[ADMIN DIRECTIVE D-010]
NGÀY HỆ THỐNG LÀ 2026-10-01 (date -> Thu Oct 1 08:56 PM +07 2026).
Admin đã ghi sai năm 2025 trong README, ADMIN/*, reviews/*, directives. Đã sửa toàn bộ trên main.
SKILL.md dòng 43 dạy `run.py say` là LỖI HẠ TẦNG: đã sửa thành `send --file` ở cả hai bản.
```

## [D-011] Task mới cho Reviewer1 — 2026-10-01

```text
[ADMIN DIRECTIVE D-011]
T10: kiểm chứng chéo T1 của DocWriter (nhánh agent/doc-writer/T1 commit 6977d36).
T11 (ƯU TIÊN CAO NHẤT): đọc TOÀN VĂN S29 (10.1109/ICICT63348.2025.10989392) và
S31 (arXiv:2603.11006v2); chấm lại tính mới T1/T2 của ResearchLead.
T14: kiểm chứng chéo T3 của BountyRecon, gồm xác minh 4 xung đột scope GitLab.
```

## [D-012] Cấp slot 9 và slot 10 — 2026-10-01

```text
[ADMIN DIRECTIVE D-012]
Slot 9 = Antigravity (ag_22c0202c): dựng testbed mạng mô phỏng.
  Nhánh agent/antigravity/T12, territory research/**/TESTBED.md + agents/antigravity/**.
  Lý do: ResearchLead khai KHÔNG có testbed mạng và KHÔNG có cụm K8s.
Slot 10 = javis (ag_3bef07fd): truy hồi 8 nguồn bị chặn.
  Nhánh agent/javis/T13, territory research/**/SOURCES_BROWSER.md + agents/javis/**.
  Lý do: ResearchLead có 8 URL fetch THẤT BẠI (MDPI 403 x3, ACM DL 403...).
CẢNH BÁO: javis ở VM khác (/home/hatch/workspace). Không clone được thì BÁO ADMIN,
KHÔNG ghi tạm sang máy khác.
```

## [D-013] TRẠNG THÁI THỐNG NHẤT CỦA CỔNG G4 — 2026-10-01

> Chỉ thị này thay thế mọi cách hiểu khác về cổng G4. Trước đó 4 tài liệu mâu thuẫn hai chiều
> (`ADMIN/LOG.md` #4, `README.md` hàng G4, `ADMIN/ASSIGNMENTS.md` hàng T4, `directives.md` D-005)
> — phát hiện F-03 của Auditor2.

```text
[ADMIN DIRECTIVE D-013]
Cổng G4 (ExploitDeep được chạm target) đòi ĐỦ HAI điều kiện:
  (1) security/<program>/SCOPE.md tồn tại, trích NGUYÊN VĂN scope phủ target đó;
  (2) Admin ban hành chỉ thị nêu rõ target + finding_id.

Điều kiện (2) là BẢN GHI UỶ QUYỀN, KHÔNG phải vòng chờ duyệt thủ công.
Admin cam kết ban hành ngay khi (1) đạt — không giữ lại, không chờ thêm.
Nhưng nếu thiếu (2), ExploitDeep KHÔNG được chạm target: không có bản ghi thì không có
cơ sở chứng minh hành vi được phép.

BỔ SUNG sau báo cáo T3 của BountyRecon:
  - 4 tài sản GitLab có XUNG ĐỘT SCOPE trong dữ liệu công bố của chính GitLab
    (*.gitlab.net, *.gitlap.com, about.gitlab.com, docs.gitlab.com) => LOẠI KHỎI T4.
    Cấm khai thác cho tới khi GitLab trả lời làm rõ. Đây là lựa chọn (a).

  ĐÍNH CHÍNH CẤP 2 (DISSENT-7 + M-01 của Auditor2 ở T24) — TIỀN ĐỀ ĐÃ SAI:
  Câu hỏi "4 hay 2 xung đột?" SAI TIỀN ĐỀ. Đáp án đúng là **0 XUNG ĐỘT HIỆU LỰC**.
  - Reviewer1 (T14) đúng khi nói chỉ 2 là cùng `asset_type`; DeepSeek-Harness nói 4.
  - NHƯNG biến quyết định KHÔNG phải `asset_type` — mà là **`archived_at`**, thứ mà
    **CẢ BA kiểm định viên** (BountyRecon, Reviewer1, DeepSeek-Harness) **đều không truy vấn**.
  - Bật `archived:false` (chính sách ĐANG hiệu lực): 44 entry, IN=19, OUT=25,
    **0 tài sản xuất hiện ở cả hai phía**. Cả 4 vế OUT đều `archived_at = 2022-07-21`.
  - Chính sách sống của GitLab ghi cả 4 tài sản là in-scope **và** eligible_for_bounty.

  QUYẾT ĐỊNH KHÔNG ĐỔI: vẫn loại cả 4 khỏi T4 — nay gọi đúng tên là
  **0 xung đột thật + 4 loại thận trọng**, không phải "2 thật + 2 thận trọng".

  BÀI HỌC BẮT BUỘC (M-01 khuyến nghị 2): **`archived_at` trở thành trường BẮT BUỘC**
  trong mẫu `security/<program>/SCOPE.md`. Hai kiểm định viên độc lập cùng truy vấn một tập
  trường thì **cùng mù một chiều dữ liệu** — đếm nguồn không bù được cho việc thiếu chiều.
  - Cloudflare: KHÔNG mở T4. Chính sách Cloudflare cấm test vào khách hàng của họ;
    chạm nhầm có thể bị loại vĩnh viễn và phát sinh trách nhiệm pháp lý.
  - G4 hiện vẫn ĐÓNG: chưa có chỉ thị nào nêu target cụ thể.
```

---

## [D-014] Vá lỗ hổng quy trình trong T5 + sửa sai số `capstone` — 2026-10-01

> Nguồn: Reviewer1, T21-A (PASS 5/6). Đây là lỗ hổng **thật** và đáng chú ý vì nó đúng
> **cùng loại lỗi** mà ExploitDeep đã mắc ở T4 và bị Reviewer1 bác bỏ.

```text
[ADMIN DIRECTIVE D-014]
1. VÁ C2 của agents/forensicsmal/T5/FORENSICS_PROCEDURE.md — thêm 3 ô:
   (a) "Kiểm kê công cụ đã dùng `pip freeze`/`pip list` KHÔNG LỌC và lưu nguyên output?"
   (b) "Mỗi kết luận 'THIẾU' đã chứng minh bằng `import <mod>` trong ĐÚNG interpreter
        đang xét, và ghi rõ interpreter đó?"
   (c) "Mỗi dòng phiên bản ghi rõ lấy từ METADATA hay `__version__`?"
2. SỬA sai số `capstone`: T5 ghi 5.0.9 ở 6 chỗ mà không nói nguồn. Thực tế BOTH ĐÚNG:
   metadata = 5.0.9, `__version__` = 5.0.7. Phải ghi rõ nguồn mỗi số.
3. Giao ForensicsMal T23. Không ai sửa hộ — agents/** là territory của họ.
```

---

## [D-022] Giới hạn tin nhắn là **UTF-16 code unit**, không phải code point — 2026-10-01

> Nguồn: `BountyRecon` (T28 §5). Đây là **sự cố hạ tầng thật**, cùng loại với lỗi `say`/`send`.

```text
[ADMIN DIRECTIVE D-022]
Giới hạn 4000 của AgentMeet đếm bằng UTF-16 CODE UNIT, KHÔNG phải code point.
Emoji là surrogate pair = 2 đơn vị. Tiếng Việt có dấu cũng có thể là 2 đơn vị.

Bằng chứng thô (BountyRecon T28):
  code points: 3999  |  UTF-16 units: 4001   =>  HTTP 422

CÁCH ĐẾM AN TOÀN (bắt buộc dùng trước khi gửi):
  python3 -c "s=open('tin.md',encoding='utf-8').read(); print(len(s.encode('utf-16-le'))//2)"

Ngưỡng an toàn khuyến nghị: <= 3900 đơn vị UTF-16 (chừa biên).
Mọi agent viết tiếng Việt + emoji đều dễ dính lỗi này.
```

---

## [D-023] Hai phép kiểm bắt buộc bổ sung cho Lớp 1 — 2026-10-01

> Nguồn: `Reviewer1` (T30 §"Bổ sung quy trình"). Admin **duyệt cả hai** và đưa vào Lớp 1.

```text
[ADMIN DIRECTIVE D-023]
[1] KIỂM LINK TƯƠNG ĐỐI — PHÂN LOẠI AUTHORED vs CAPTURE
    - Bóc code fence + inline code TRƯỚC khi quét.
    - Chỉ kết luận DEFECT trên file AUTHORED (file do người viết).
    - Tính đường dẫn từ THƯ MỤC CỦA FILE, không từ gốc repo.
    - Đối chiếu CẢ file LẪN thư mục (thư mục hợp lệ cũng là đích hợp lệ).
    Lý do: bộ quét ngây thơ cho 127 "lỗi" khi lỗi thật = 3 (tỉ lệ ~42:1).
    Reviewer1 TỰ MẮC đúng lỗi này ở T27 (22 -> 7 -> 0). Admin từng báo oan tương tự.

[2] KIỂM TOÀN VẸN VÙNG TRÍCH NGUYÊN VĂN — THEO LỊCH SỬ, KHÔNG CHỈ 2 ĐIỂM
    - Băm từng phần (pre / thân / suf) ở 2 điểm, VÀ
    - Kiểm `git log -p <merge-base>..<head>` cho MỌI commit.
    - GHI RÕ QUY ƯỚC RANH GIỚI (lệch 1 ký tự là lệch hash — Reviewer1 từng đo pre=8283 thay vì 8284).
    Lý do: phép so 2 điểm có kẽ hở K1 — commit trung gian "sửa rồi revert" sẽ LỌT.
    Đây chính là dạng kiểm Reviewer1 đã THIẾU ở T14 (GAP-0).
```

---

## [D-025] Nguyên tắc kiểm **TRẠNG THÁI** — nguồn sự thật là BẢNG, không phải câu văn — 2026-10-01

> Nguồn: `Reviewer1` T32 §"[MỚI 3]". Admin **duyệt cả hai** và đưa vào quy trình bắt buộc.

```text
[ADMIN DIRECTIVE D-025]
[3a] TRẠNG THÁI PHẢI LẤY TỪ BẢNG, KHÔNG TỪ CÂU VĂN
     Trích cặp (CHỦ THỂ, TRẠNG THÁI) theo CẢ HAI chiều ("chưa xong" / "đã xong"), rồi
     JOIN với nguồn sự thật dạng BẢNG:
       D-0xx  -> có chỉ thị MUỘN HƠN tuyên bố "thay thế" nó không?
       T<nn>  -> ADMIN/ASSIGNMENTS.md (cột Trạng thái) + ADMIN/SUMMARY.md §1
       asset  -> gọi lại API nguồn, đối chiếu `archived_at` CỦA TỪNG BẢN GHI RIÊNG
     Báo DELTA ("khẳng định nói X, bảng nói Y"). KHÔNG báo "thấy từ khoá cũ".
     Quét TOÀN territory, không chỉ file đang sửa.

[3b] MỌI TRƯỜNG CÓ THỂ "HẾT HIỆU LỰC" PHẢI CÓ TRONG MỌI BẢNG TRÍCH
     Đây là bản khái quát của lỗi `archived_at`. Áp dụng cho MỌI bảng tài sản/scope.

BẰNG CHỨNG ĐÃ BẮT ĐƯỢC (cùng một lớp lỗi, ba lần, ba người):
  - Auditor2 M-01: xung đột GitLab — 0 chứ không phải 2/4 (thêm chiều archived_at)
  - BountyRecon T31: gitlab.net apex (2020-10-05) vs wildcard (còn hiệu lực) — gộp nhầm
  - Reviewer1 T32: §1 SCOPE.md n=24 TRỘN 19 live + 5 retired; G2 đề xuất hành động trên
    license.gitlab.com ĐÃ retired 2022-03-21
```

---

## [D-026] Phân xử xung đột `[3b]` ⟂ "cấm sửa EVIDENCE" + mở rộng `[3b]` ra MỌI chương trình — 2026-10-01

> Nguồn: `Reviewer1` T35. Đây là **xung đột quy tắc thật**: hai luật của Admin **không thể tuân đồng thời**.

```text
[ADMIN DIRECTIVE D-026]
[PHÂN XỬ] Chọn phương án (a): `[3b]` CHỈ áp cho bảng AUTHORED.
  - Bảng AUTHORED  -> PHẢI thêm cột `archived_at` (sửa trực tiếp được).
  - Bảng CAPTURE (trong `EVIDENCE/**`) -> KHÔNG sửa. Thay vào đó CHỤP LẠI thành `<tên>_v2`
    CÓ kèm `archived_at`, GIỮ NGUYÊN bản gốc.
  Lý do: bản CAPTURE là BẰNG CHỨNG PHÁP LÝ (trích nguyên văn tại thời điểm chụp).
  Sửa nó là phá tính nguyên văn; xoá nó là phá vết. Chụp lại bản mới là cách duy nhất
  vừa có chiều `archived_at` vừa giữ được bản gốc.
  ⇒ LUẬT "cấm sửa EVIDENCE/**" KHÔNG bị nới lỏng. `[3b]` được làm rõ phạm vi.

[MỞ RỘNG] `[3b]` áp cho MỌI chương trình, không chỉ GitLab.
  Bằng chứng định lượng (Reviewer1 T35, GraphQL độc lập):
    GitLab     63 scope | 44 live | 19 archived | 5 archived&sub=True |   5 orphan
    GitHub    197 scope | 39 live | 158 archived | 156 archived&sub=True | 153 orphan
    Cloudflare 83 scope | 78 live |  5 archived | 4 archived&sub=True |   4 orphan
  `security/cloudflare/SCOPE.md` §1a liệt kê TRỰC TIẾP 2 trong 4 orphan:
    http://cloudflare.com/apps/ (archived 2023-03-01) · dash.teams.cloudflare.com (2023-05-08)
  Hai mục còn lại: Argo Tunnel · Durable Objects (2023-10-26).

[GIỚI HẠN — KHÔNG ĐƯỢC VƯỢT] KHÔNG kết luận 153 / 4 bản ghi là "ngoài scope".
  Chỉ được khẳng định: "bảng THIẾU chiều `archived_at` ⇒ KHÔNG PHÂN BIỆT ĐƯỢC".
  Việc loại khỏi T4 chỉ áp cho 4 tài sản GitLab đã có phán quyết (D-021).
```

---

## [D-027] ĐÍNH CHÍNH `T37` — chỉ **3** bảng AUTHORED cần `archived_at`; giữ nguyên văn là bất khả xâm phạm — 2026-10-01

> Nguồn: `Reviewer1` T38. **Admin đã liệt kê sai 3/5 vị trí** trong chỉ thị T37.

```text
[ADMIN DIRECTIVE D-027]
CHỈ 3 BẢNG AUTHORED cần cột `archived_at`:
  - security/gitlab/SCOPE.md §1   (24 dòng tài sản)
  - security/gitlab/SCOPE.md §2a  (10 dòng tài sản)
  - security/cloudflare/SCOPE.md §1a (12 dòng tài sản)

KHÔNG ĐƯỢC thêm cột vào 3 vị trí Admin đã liệt kê SAI:
  - security/github/SCOPE.md §1  = KHỐI NGUYÊN VĂN (0 dòng bảng) — thêm cột là BÓC XÉP
    khối trích nguyên văn, đúng loại việc D-026(a) và LOG #54 đang chống.
  - security/github/RECON.md     = KHÔNG có bảng scope — thêm cột là SAI NGỮ NGHĨA.
  - security/cloudflare/RECON.md = KHÔNG có bảng scope — thêm cột là SAI NGỮ NGHĨA.

CÁCH ĐÚNG cho GitHub: giữ nguyên khối nguyên văn §1, thêm MỤC AUTHORED MỚI
  `### 1b. Bảng tài sản GitHub kèm archived_at` — TÁCH *nguyên văn* khỏi *bảng tổng hợp*.

NGUYÊN TẮC RÚT RA (áp cho mọi lần sau):
  Trước khi yêu cầu "thêm cột vào mọi bảng", phải KIỂM bảng đó có phải BẢNG thật
  hay là KHỐI TRÍCH NGUYÊN VĂN. Trích nguyên văn > mọi yêu cầu định dạng.
```
