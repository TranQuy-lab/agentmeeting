# INDEX — Mục lục toàn kho

**Người duy trì:** DocWriter (`ag_da78519d`)
**Ngày lập bản này:** 2026-10-01 — **Admin đã chốt mốc ngày** (`date` → `Thu Oct 1 08:56 PM +07 2026`); xem phán quyết DISSENT-4
**Bản gốc do Admin viết** ở `abe0c3e`, DocWriter **tiếp quản và viết lại toàn bộ** ở T1 (phán quyết DISSENT-2). Bản này là lần viết lại **thứ hai**, ở T22, theo mốc `main` hiện tại.
**Nhánh:** `agent/doc-writer/T22` · **Mốc đối chiếu:** `main` @ `0f41ebb` — **157 file**
**Trạng thái:** đã tiếp quản từ Admin; **chờ Reviewer1 kiểm định**

> Bảng dưới đây là **nguồn sự thật duy nhất về artifact trong kho**.
> Bảng được lập bằng cách đối chiếu **`git ls-files`** — **KHÔNG đoán**.
>
> ⚠️ **CẢNH BÁO PHẠM VI (cập nhật ở T22):** bảng §2 nay mô tả **`main` @ `0f41ebb` với 157 file**.
> Ở T1 bảng từng chỉ mô tả **nhánh `agent/doc-writer/T1` với 39 file**; nhánh đó **đã được merge**
> vào `main` tại `c4a7fae`. **Mâu thuẫn phạm vi cũ nay đã hết**: con số trong bảng **chính là** con
> số của `main` tại mốc ghi ở trên. Mốc `39 file` chỉ còn **giá trị lịch sử**, được giữ nguyên
> (không xoá) tại [`agents/docwriter/tasks/T1/`](agents/docwriter/tasks/T1/).

---

## 1. Quy ước

**Tác giả** = người *tạo ra* file, lấy **máy móc** từ commit **thêm file lần đầu**
(`git log --diff-filter=A --format=%an -- <file>`, lấy dòng **cũ nhất**) — **KHÔNG đoán tên**.
**Chủ trì** = người *chịu trách nhiệm cập nhật*, suy từ **territory** trong `ADMIN/ASSIGNMENTS.md`.

**Quy ước trạng thái:** ⏳ chờ · 🔄 đang làm · 🔄 chờ kiểm định · ✅ đã nghiệm thu (lớp 1) · ✅ hoàn tất · ❌ bị trả lại · ⛔ chặn · — không áp dụng

**Quy ước loại:** `Khung` · `Điều hành` · `Nghiên cứu` · `An ninh` · `Kiểm định` · `Pháp y` · `Digest` · `Dữ liệu thô` · `Bằng chứng` · `Mẫu vô hại` · `Artifact` · `Hạ tầng` · `Dữ liệu` · `Giữ thư mục`

**Quy ước reviewer:** mọi sản phẩm → **Reviewer1**; `ADMIN/**`, `reviews/**` → **Auditor2**;
`reviews/AUDIT.*` và `reviews/AUDIT2.*` → **`Người dùng`** — giá trị này **không phải vi phạm**:
`ADMIN/ASSIGNMENTS.md` **T7** và **T17** ghi thẳng reviewer là *"Người dùng"*, nên đây là
**reviewer do Admin khai báo**. (Ở T1 DocWriter từng xếp `Người dùng` vào nhóm "ngoài quy ước";
nay ghi nhận là **giá trị hợp lệ theo phân công** — **không** tự đổi giá trị.)

**Cách hiểu cột "Trạng thái" (quan trọng):** `✅ đã nghiệm thu (lớp 1)` nghĩa là **commit sửa cuối**
cùng của file thuộc một task **đã có trong danh sách nghiệm thu** của `ADMIN/SUMMARY.md` §1
(T1, T3, T6, T7, T11, T15, T16, T17, T19, T20). Đây là **suy ra từ `SUMMARY.md`**, **không phải**
DocWriter đọc nội dung từng file để chấm. Xem giới hạn ở §2.1.

## 2. Bảng đầy đủ — 157 file (mốc `main` @ `0f41ebb`)

| # | Đường dẫn | Tác giả (thêm file) | Chủ trì | Loại | Trạng thái | Reviewer | Commit thêm | Sửa cuối / Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1 | `.gitignore` | Admin AgentMeet | Admin | Hạ tầng | ✅ hoàn tất | Reviewer1 | `abe0c3e` | `[T0] dd0fc3c` |
| 2 | `ADMIN/.gitkeep` | Admin AgentMeet | Admin | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 3 | `ADMIN/ASSIGNMENTS.md` | Admin AgentMeet | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | `[T0] a1e026f` |
| 4 | `ADMIN/DISSENT.md` | Admin AgentMeet | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | `[T0] a1e026f` |
| 5 | `ADMIN/LOG.md` | Admin AgentMeet | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | `[T0] 0f41ebb` |
| 6 | `ADMIN/ROSTER.md` | Admin AgentMeet | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | `[T0] 0f41ebb` |
| 7 | `ADMIN/SUMMARY.md` | Admin AgentMeet | Admin | Điều hành | 🔄 đang làm | Auditor2 | `abe0c3e` | `[T0] 0f41ebb` |
| 8 | `INDEX.md` | Admin AgentMeet | DocWriter | Khung | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `abe0c3e` | `[T1] c4a7fae` |
| 9 | `README.md` | Admin AgentMeet | DocWriter | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | `[T0] 02c90bf` |
| 10 | `agents/auditor2/README.md` | Admin AgentMeet | Auditor2 | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | `[T0] abe0c3e` |
| 11 | `agents/auditor2/checkin.md` | Auditor2 | Auditor2 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `bc51cee` | `[T7] bc51cee` |
| 12 | `agents/auditor2/tasks/.gitkeep` | Admin AgentMeet | Auditor2 | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 13 | `agents/bountyrecon/README.md` | Admin AgentMeet | BountyRecon | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | `[T0] abe0c3e` |
| 14 | `agents/bountyrecon/tasks/.gitkeep` | Admin AgentMeet | BountyRecon | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 15 | `agents/bountyrecon/tasks/T3/CANDIDATES.md` | BountyRecon | BountyRecon | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 16 | `agents/bountyrecon/tasks/T3/EVIDENCE/bounty_meta.json` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 17 | `agents/bountyrecon/tasks/T3/EVIDENCE/fetch_h1.py` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 18 | `agents/bountyrecon/tasks/T3/EVIDENCE/gh_bounty.html` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 19 | `agents/bountyrecon/tasks/T3/EVIDENCE/gh_ineligible.html` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 20 | `agents/bountyrecon/tasks/T3/EVIDENCE/gh_ineligible.txt` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 21 | `agents/bountyrecon/tasks/T3/EVIDENCE/gh_report-quality.html` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 22 | `agents/bountyrecon/tasks/T3/EVIDENCE/gh_rewards.html` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 23 | `agents/bountyrecon/tasks/T3/EVIDENCE/h1_cloudflare.json` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 24 | `agents/bountyrecon/tasks/T3/EVIDENCE/h1_github.json` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 25 | `agents/bountyrecon/tasks/T3/EVIDENCE/h1_gitlab.json` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 26 | `agents/bountyrecon/tasks/T3/EVIDENCE/h1_security.json` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 27 | `agents/bountyrecon/tasks/T3/EVIDENCE/policy_cloudflare.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 28 | `agents/bountyrecon/tasks/T3/EVIDENCE/policy_github.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 29 | `agents/bountyrecon/tasks/T3/EVIDENCE/policy_gitlab.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 30 | `agents/bountyrecon/tasks/T3/EVIDENCE/policy_security.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 31 | `agents/bountyrecon/tasks/T3/EVIDENCE/recon.sh` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 32 | `agents/bountyrecon/tasks/T3/EVIDENCE/recon_cloudflare.txt` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 33 | `agents/bountyrecon/tasks/T3/EVIDENCE/recon_github.txt` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 34 | `agents/bountyrecon/tasks/T3/EVIDENCE/recon_gitlab.txt` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 35 | `agents/bountyrecon/tasks/T3/EVIDENCE/scope_cloudflare.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 36 | `agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 37 | `agents/bountyrecon/tasks/T3/EVIDENCE/scope_gitlab.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 38 | `agents/bountyrecon/tasks/T3/EVIDENCE/scope_security.md` | BountyRecon | BountyRecon | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 39 | `agents/docwriter/README.md` | Admin AgentMeet | DocWriter | Khung | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `abe0c3e` | `[T1] 5bcea63` |
| 40 | `agents/docwriter/tasks/.gitkeep` | Admin AgentMeet | DocWriter | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 41 | `agents/docwriter/tasks/T1/BAO-CAO-CHAT-LUONG.md` | DocWriter | DocWriter | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 3be89fd` |
| 42 | `agents/docwriter/tasks/T1/KIEM-TRA-KHUNG.md` | DocWriter | DocWriter | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 6977d36` |
| 43 | `agents/exploitdeep/README.md` | Admin AgentMeet | ExploitDeep | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | `[T0] abe0c3e` |
| 44 | `agents/exploitdeep/T16/EVIDENCE/inventory_per_interpreter_raw.txt` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 45 | `agents/exploitdeep/T16/EVIDENCE/msg-ask-gate-T4-G1.md` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `741aee6` | `[T16] 741aee6` |
| 46 | `agents/exploitdeep/T16/EVIDENCE/msg-report-T16-1.md` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `7dec622` | `[T16] 7dec622` |
| 47 | `agents/exploitdeep/T16/EVIDENCE/msg-report-T16-2.md` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `7dec622` | `[T16] 7dec622` |
| 48 | `agents/exploitdeep/T16/EVIDENCE/msg-report-T16.md` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `7dec622` | `[T16] 7dec622` |
| 49 | `agents/exploitdeep/T16/EVIDENCE/pip-freeze-SYSTEM.txt` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 50 | `agents/exploitdeep/T16/EVIDENCE/pip-freeze-VENV_ED.txt` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 51 | `agents/exploitdeep/T16/EVIDENCE/pip-list-SYSTEM.txt` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 52 | `agents/exploitdeep/T16/EVIDENCE/pip-list-VENV_ED.txt` | ExploitDeep | ExploitDeep | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 53 | `agents/exploitdeep/T16/README.md` | ExploitDeep | ExploitDeep | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 54 | `agents/exploitdeep/T16/inventory_per_interpreter.sh` | ExploitDeep | ExploitDeep | Hạ tầng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `ded6675` | `[T16] ded6675` |
| 55 | `agents/exploitdeep/T4/EVIDENCE/msg-checkin.md` | ExploitDeep | ExploitDeep | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `2cbe90a` | `[T4] 2cbe90a` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 56 | `agents/exploitdeep/T4/EVIDENCE/msg-report-1.md` | ExploitDeep | ExploitDeep | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `2cbe90a` | `[T4] 2cbe90a` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 57 | `agents/exploitdeep/T4/EVIDENCE/msg-report-2.md` | ExploitDeep | ExploitDeep | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `2cbe90a` | `[T4] 2cbe90a` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 58 | `agents/exploitdeep/T4/EVIDENCE/msg-report.md` | ExploitDeep | ExploitDeep | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `2cbe90a` | `[T4] 2cbe90a` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 59 | `agents/exploitdeep/T4/EVIDENCE/tool_inventory_raw.txt` | ExploitDeep | ExploitDeep | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `be70eed` | `[T4] be70eed` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 60 | `agents/exploitdeep/T4/READINESS.md` | ExploitDeep | ExploitDeep | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `be70eed` | `[T16] ded6675` |
| 61 | `agents/exploitdeep/tasks/.gitkeep` | Admin AgentMeet | ExploitDeep | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 62 | `agents/forensicsmal/README.md` | Admin AgentMeet | ForensicsMal | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | `[T0] abe0c3e` |
| 63 | `agents/forensicsmal/T15/EVIDENCE/t15_0_corpus_hashes.txt` | ForensicsMal | ForensicsMal | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 64 | `agents/forensicsmal/T15/EVIDENCE/t15_1_pcap_raw.txt` | ForensicsMal | ForensicsMal | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 65 | `agents/forensicsmal/T15/EVIDENCE/t15_2_elf_raw.txt` | ForensicsMal | ForensicsMal | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 66 | `agents/forensicsmal/T15/EVIDENCE/t15_3_yara_raw.txt` | ForensicsMal | ForensicsMal | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 67 | `agents/forensicsmal/T15/EVIDENCE/t15_4_volatility_raw.txt` | ForensicsMal | ForensicsMal | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 68 | `agents/forensicsmal/T15/T15_REPORT.md` | ForensicsMal | ForensicsMal | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 78c0464` |
| 69 | `agents/forensicsmal/T15/corpus/.gitignore` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 70 | `agents/forensicsmal/T15/corpus/README.md` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 71 | `agents/forensicsmal/T15/corpus/bench_elf.c` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 72 | `agents/forensicsmal/T15/corpus/t15_rules.yar` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 73 | `agents/forensicsmal/T15/corpus/yara_A_marker_upper.txt` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 74 | `agents/forensicsmal/T15/corpus/yara_B_url.txt` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 75 | `agents/forensicsmal/T15/corpus/yara_C_lowercase.txt` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 76 | `agents/forensicsmal/T15/corpus/yara_D_clean.txt` | ForensicsMal | ForensicsMal | Mẫu vô hại | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 77 | `agents/forensicsmal/T15/scripts/t15_elf_test.py` | ForensicsMal | ForensicsMal | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 78 | `agents/forensicsmal/T15/scripts/t15_pcap_test.py` | ForensicsMal | ForensicsMal | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 79 | `agents/forensicsmal/T15/scripts/t15_volatility_test.py` | ForensicsMal | ForensicsMal | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 80 | `agents/forensicsmal/T15/scripts/t15_yara_test.py` | ForensicsMal | ForensicsMal | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `6feaf99` | `[T15] 6feaf99` |
| 81 | `agents/forensicsmal/tasks/.gitkeep` | Admin AgentMeet | ForensicsMal | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 82 | `agents/researchlead/README.md` | Admin AgentMeet | ResearchLead | Khung | 🔄 chờ kiểm định | Reviewer1 | `abe0c3e` | `[T0] abe0c3e` |
| 83 | `agents/researchlead/tasks/.gitkeep` | Admin AgentMeet | ResearchLead | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 84 | `agents/researchlead/tasks/checkin.md` | ResearchLead | ResearchLead | Artifact | 🔄 chờ kiểm định | Reviewer1 | `a23c004` | `[T2] a23c004` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 85 | `agents/reviewer1/README.md` | Admin AgentMeet | Reviewer1 | Khung | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `abe0c3e` | `[T11] 956f615` |
| 86 | `agents/reviewer1/evidence/T10/t10-verify.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 87 | `agents/reviewer1/evidence/T11/t11-fetch-s29-s31.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 88 | `agents/reviewer1/evidence/T11/t11-phuluc-N03-INDEX.md.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `85ea56f` | `[T11] 85ea56f` |
| 89 | `agents/reviewer1/evidence/T11/t11-s31-toanvan.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 90 | `agents/reviewer1/evidence/T14/rv1_h1_refetch.py` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 91 | `agents/reviewer1/evidence/T14/t14-refetch-scope.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 92 | `agents/reviewer1/evidence/T20/rv1_operand_semantics.py` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 93 | `agents/reviewer1/evidence/T20/rv1_operand_semantics2.py` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 94 | `agents/reviewer1/evidence/T20/rv1_operand_semantics3.py` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 95 | `agents/reviewer1/evidence/T20/rv1_operand_semantics4.py` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 96 | `agents/reviewer1/evidence/T20/t20-operand-semantics.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 97 | `agents/reviewer1/evidence/T20/t20-t15-rerun.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 98 | `agents/reviewer1/evidence/T20/t20-t16-verify.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 99 | `agents/reviewer1/evidence/T6/01-clone-va-commit-goc.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 100 | `agents/reviewer1/evidence/T6/02-show-stat-va-ton-tai-file.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 101 | `agents/reviewer1/evidence/T6/03-quet-ro-ri-credential.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 102 | `agents/reviewer1/evidence/T6/04-log-doi-chieu-thuc-te.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 103 | `agents/reviewer1/evidence/T6/05-summary-kiem-ket-luan.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 104 | `agents/reviewer1/evidence/T6/06-readme-index-vs-thuc-te.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 105 | `agents/reviewer1/evidence/T6/07-doi-tuong-kiem-mu.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 106 | `agents/reviewer1/evidence/T6/08-main-tien-hoa-kiem-lai.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 107 | `agents/reviewer1/evidence/T9/t9-raw-verify.txt` | Reviewer1 | Reviewer1 | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 108 | `agents/reviewer1/tasks/.gitkeep` | Admin AgentMeet | Reviewer1 | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 109 | `agents/reviewer1/tasks/T10/T10.md` | Reviewer1 | Reviewer1 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 110 | `agents/reviewer1/tasks/T11/T11.md` | Reviewer1 | Reviewer1 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 111 | `agents/reviewer1/tasks/T14/T14.md` | Reviewer1 | Reviewer1 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `956f615` | `[T11] 956f615` |
| 112 | `agents/reviewer1/tasks/T20/T20.md` | Reviewer1 | Reviewer1 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f2afb08` | `[T20] f2afb08` |
| 113 | `agents/reviewer1/tasks/T6/T6.md` | Reviewer1 | Reviewer1 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 114 | `agents/reviewer1/tasks/T9/T9.md` | Reviewer1 | Reviewer1 | Artifact | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `78180ca` | `[T6] 78180ca` |
| 115 | `research/.gitkeep` | Admin AgentMeet | ResearchLead | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 116 | `research/EVIDENCE/FETCH_STATUS.md` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `a23c004` | `[T2] a23c004` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 117 | `research/EVIDENCE/T19_checks.txt` | ResearchLead | ResearchLead | Bằng chứng | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `8b236bf` | `[T19] 8b236bf` |
| 118 | `research/EVIDENCE/arxiv_lookups.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `a23c004` | `[T2] a23c004` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 119 | `research/EVIDENCE/crossref_lookups.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 120 | `research/EVIDENCE/openalex_authors.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 121 | `research/EVIDENCE/openalex_doi_lookup.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 122 | `research/EVIDENCE/openalex_title_filters.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 123 | `research/EVIDENCE/quote_extracts.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 124 | `research/RANKING.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `a23c004` | `[T19] 8b236bf` |
| 125 | `research/ebpf-microsegmentation/BLINDCHECK.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `a23c004` | `[T19] 8b236bf` |
| 126 | `research/ebpf-microsegmentation/EVIDENCE/openalex_queries.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 127 | `research/ebpf-microsegmentation/LITREVIEW.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `a23c004` | `[T19] 8b236bf` |
| 128 | `research/ebpf-microsegmentation/PROPOSAL.md` | ResearchLead | ResearchLead | Nghiên cứu | 🔄 chờ kiểm định | Reviewer1 | `a23c004` | `[T2] a23c004` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 129 | `research/ebpf-microsegmentation/SOURCES.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `a23c004` | `[T19] 8b236bf` |
| 130 | `research/pqc-tls-migration/BLINDCHECK.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f06e806` | `[T19] 8b236bf` |
| 131 | `research/pqc-tls-migration/EVIDENCE/openalex_queries.txt` | ResearchLead | ResearchLead | Bằng chứng | 🔄 chờ kiểm định | Reviewer1 | `f06e806` | `[T2] f06e806` — **đã merge nhưng KHÔNG thấy trong danh sách nghiệm thu** `ADMIN/SUMMARY.md` §1 |
| 132 | `research/pqc-tls-migration/LITREVIEW.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f06e806` | `[T19] 8b236bf` |
| 133 | `research/pqc-tls-migration/PROPOSAL.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f06e806` | `[T19] 8b236bf` |
| 134 | `research/pqc-tls-migration/SOURCES.md` | ResearchLead | ResearchLead | Nghiên cứu | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `f06e806` | `[T19] 8b236bf` |
| 135 | `reviews/.gitkeep` | Admin AgentMeet | Reviewer1 | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 136 | `reviews/AUDIT.json` | Auditor2 | Auditor2 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Người dùng | `bc51cee` | `[T7] 97d338f` |
| 137 | `reviews/AUDIT.md` | Auditor2 | Auditor2 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Người dùng | `bc51cee` | `[T7] 97d338f` |
| 138 | `reviews/AUDIT2.json` | Auditor2 | Auditor2 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Người dùng | `0ac28f9` | `[T17] 0ac28f9` |
| 139 | `reviews/AUDIT2.md` | Auditor2 | Auditor2 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Người dùng | `0ac28f9` | `[T17] 0ac28f9` |
| 140 | `reviews/BLIND.md` | Admin AgentMeet | Reviewer1 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Auditor2 | `abe0c3e` | `[T6] 78180ca` |
| 141 | `reviews/CROSS.md` | Admin AgentMeet | Reviewer1 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Auditor2 | `abe0c3e` | `[T11] 85ea56f` |
| 142 | `reviews/RECONCILE.md` | Admin AgentMeet | Reviewer1 | Kiểm định | ✅ đã nghiệm thu (lớp 1) | Auditor2 | `abe0c3e` | `[T11] 956f615` |
| 143 | `rooms/ab1-478d-cfa7/README.md` | DocWriter | DocWriter | Khung | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 5bcea63` |
| 144 | `rooms/ab1-478d-cfa7/digest/.gitkeep` | Admin AgentMeet | DocWriter | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 145 | `rooms/ab1-478d-cfa7/digest/README.md` | DocWriter | DocWriter | Digest | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 5bcea63` |
| 146 | `rooms/ab1-478d-cfa7/digest/digest-msg-0001-0012.md` | DocWriter | DocWriter | Digest | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 6977d36` |
| 147 | `rooms/ab1-478d-cfa7/directives.md` | Admin AgentMeet | Admin | Điều hành | 🔄 đang làm | Reviewer1 | `abe0c3e` | `[T0] a1e026f` |
| 148 | `rooms/ab1-478d-cfa7/raw/.gitkeep` | Admin AgentMeet | DocWriter | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 149 | `rooms/ab1-478d-cfa7/raw/MANIFEST.md` | DocWriter | DocWriter | Dữ liệu thô | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 3be89fd` |
| 150 | `rooms/ab1-478d-cfa7/raw/raw-msg-0001-0012.jsonl` | DocWriter | DocWriter | Dữ liệu thô | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `5bcea63` | `[T1] 5bcea63` |
| 151 | `security/.gitkeep` | Admin AgentMeet | BountyRecon | Giữ thư mục | — | — | `abe0c3e` | `[T0] abe0c3e` |
| 152 | `security/cloudflare/RECON.md` | BountyRecon | BountyRecon | An ninh | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 153 | `security/cloudflare/SCOPE.md` | BountyRecon | BountyRecon | An ninh | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |
| 154 | `security/github/RECON.md` | BountyRecon | BountyRecon | An ninh | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 155 | `security/github/SCOPE.md` | BountyRecon | BountyRecon | An ninh | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 03d304b` |
| 156 | `security/gitlab/RECON.md` | BountyRecon | BountyRecon | An ninh | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `03d304b` | `[T3] 03d304b` |
| 157 | `security/gitlab/SCOPE.md` | BountyRecon | BountyRecon | An ninh | ✅ đã nghiệm thu (lớp 1) | Reviewer1 | `71f0bf8` | `[T3] 71f0bf8` |

### 2.1 Cách lập bảng này và GIỚI HẠN của nó (đọc trước khi tin bảng)

Bảng trên **không** phải kết quả đọc 157 file. Nó lấy **máy móc** từ Git:

```bash
# danh sách: git ls-files
# Tác giả + Commit thêm : git log --diff-filter=A --format='%h|%an' -- <file>   (lấy dòng cũ nhất)
# Sửa cuối              : git log -1 --format='%h|%s' -- <file>                (lấy tiền tố [T..])
```

| # | Giới hạn — nói thẳng |
|---|---|
| 1 | **Tác giả = người commit**, không nhất thiết là người viết nội dung. Nếu ai đó commit hộ file của người khác, bảng ghi **người commit**. |
| 2 | **Trạng thái suy từ `ADMIN/SUMMARY.md` §1**, không từ việc đọc file. File có thể đã hỏng nội dung mà vẫn mang nhãn ✅. |
| 3 | Cột "Loại" và "Chủ trì" là **phân loại theo đường dẫn** của DocWriter, không phải số đo máy móc. |
| 4 | **Không** file nào phải ghi `chưa xác minh` về tác giả: cả **157/157** đều truy được commit thêm file lần đầu. |
| 5 | Bảng phản ánh **mốc `0f41ebb`**. `main` đang tiến; bảng sẽ lạc hậu ngay sau khi có commit mới. |

## 3. Tổng hợp (đếm lại bằng lệnh — xem §6)

| Chỉ số | Giá trị | Lệnh đã kiểm |
|---|---|---|
| Tổng file được track | **157** | `git ls-files \| wc -l` |
| `.md` | **71** | `git ls-files '*.md' \| wc -l` |
| `.txt` | **45** | `git ls-files '*.txt' \| wc -l` |
| `.gitkeep` | **13** | `git ls-files '*.gitkeep' \| wc -l` |
| `.py` | **10** | `git ls-files '*.py' \| wc -l` |
| `.json` | **7** | `git ls-files '*.json' \| wc -l` |
| `.html` | **4** | |
| `.sh` | **2** | `git ls-files '*.sh' \| wc -l` |
| `.c` / `.yar` / `.jsonl` | **1** mỗi loại | |
| `.gitignore` | **2** | (gốc + trong `corpus/`) |
| Số thư mục chứa file | **52** | `git ls-files \| grep '/' \| sed 's\|/[^/]*$\||' \| sort -u \| wc -l` |

**Kiểm tổng theo đuôi file:** 71 + 45 + 13 + 10 + 7 + 4 + 2 + 2 + 1 + 1 + 1 = **157** ✅ khớp.

### 3.1 Theo tác giả (commit thêm file lần đầu)

| Tác giả | Số file |
|---|---|
| Admin AgentMeet | **32** |
| BountyRecon | **30** |
| Reviewer1 | **28** |
| ResearchLead | **20** |
| ForensicsMal | **18** |
| ExploitDeep | **17** |
| DocWriter | **7** |
| Auditor2 | **5** |

**Kiểm tổng:** 32 + 30 + 28 + 20 + 18 + 17 + 7 + 5 = **157** ✅ khớp.

> **DocWriter chỉ tạo 7 file** — đó đúng là 7 file của T1. `INDEX.md` và `README.md` tuy thuộc
> territory DocWriter nhưng **tác giả vẫn là Admin** (Admin viết bản gốc ở `abe0c3e`) — bảng ghi
> đúng sự thật đó, không gán công cho DocWriter.

### 3.2 Theo trạng thái

| Trạng thái | Số file |
|---|---|
| ✅ đã nghiệm thu (lớp 1) | **115** |
| 🔄 chờ kiểm định | **22** |
| — không áp dụng (`.gitkeep`) | **13** |
| 🔄 đang làm (Admin cập nhật liên tục) | **6** |
| ✅ hoàn tất | **1** (`.gitignore`) |

**Kiểm tổng:** 115 + 22 + 13 + 6 + 1 = **157** ✅ khớp.

### 3.3 Theo loại

| Loại | Số mục |
|---|---|
| Bằng chứng (mọi `EVIDENCE/`, `evidence/`) | **74** |
| Artifact | **18** |
| Giữ thư mục | **13** |
| Khung | **10** |
| Nghiên cứu | **9** |
| Mẫu vô hại (`corpus/`) | **8** |
| Kiểm định | **7** |
| Điều hành | **6** |
| An ninh | **6** |
| Hạ tầng | **2** |
| Digest | **2** |
| Dữ liệu thô | **2** |

**Kiểm tổng:** 74 + 18 + 13 + 10 + 9 + 8 + 7 + 6 + 6 + 2 + 2 + 2 = **157** ✅ khớp.

### 3.4 Theo task của commit SỬA CUỐI

| Task | Số file | Task | Số file |
|---|---|---|---|
| `[T3]` BountyRecon | **30** | `[T19]` ResearchLead | **9** |
| `[T0]` Admin | **26** | `[T20]` Reviewer1 | **8** |
| `[T15]` ForensicsMal | **18** | `[T4]` ExploitDeep | **5** |
| `[T16]` ExploitDeep | **12** | `[T7]` Auditor2 | **3** |
| `[T11]` Reviewer1 | **12** | `[T17]` Auditor2 | **2** |
| `[T6]` Reviewer1 | **12** | | |
| `[T2]` ResearchLead | **11** | | |
| `[T1]` DocWriter | **9** | | |

**Kiểm tổng:** 30+26+18+12+12+12+11+9+9+8+5+3+2 = **157** ✅ khớp.

## 4. Việc còn thiếu và VẤN ĐỀ MỞ (đã kiểm bằng lệnh)

### 4.1 🆕 `ADMIN/SUMMARY.md` §3 dẫn 3 đường dẫn bằng chứng KHÔNG TỒN TẠI trên `main`

`ADMIN/SUMMARY.md` dòng 46 và 51 dùng cột "Bằng chứng" trỏ tới:

```text
agents/forensicsmal/T5/EVIDENCE/tooling_bootstrap_raw.txt   (SUMMARY.md dòng 46)
agents/forensicsmal/T5/scripts/bootstrap_tools.sh           (SUMMARY.md dòng 46)
agents/forensicsmal/T5/FORENSICS_PROCEDURE.md               (SUMMARY.md dòng 51)
```

Kiểm bằng `os.path.exists` trên **toàn bộ 71 file `.md`** được track: **cả 3 đường dẫn đều KHÔNG tồn tại.**
**Nguyên nhân đã xác minh:** nhánh **`agent/forensics-mal/T5` chưa được merge** (D-019 §1 ghi rõ).
⇒ **Cột "Bằng chứng" của `SUMMARY.md` đang trỏ vào thứ không có trong kho**, nên 2 dòng rủi ro đó
**không kiểm chứng được từ repo**. **Đây là file của Admin — DocWriter không sửa**, chỉ báo cáo.
**Đề nghị Admin:** hoặc merge T5, hoặc ghi rõ trong `SUMMARY.md` rằng bằng chứng nằm ở nhánh chưa merge.

### 4.2 🆕 3 link tương đối SAI ĐỘ SÂU trong `agents/bountyrecon/tasks/T3/CANDIDATES.md`

| Dòng | Link đang ghi | Giải ra thực tế | Đúng phải là |
|---|---|---|---|
| 27 | `../../../security/github/RECON.md` | `agents/security/github/RECON.md` ❌ | `../../../../security/github/RECON.md` |
| 39 | `../../../security/gitlab/RECON.md` | `agents/security/gitlab/RECON.md` ❌ | `../../../../security/gitlab/RECON.md` |
| 50 | `../../../security/cloudflare/RECON.md` | `agents/security/cloudflare/RECON.md` ❌ | `../../../../security/cloudflare/RECON.md` |

File ở `agents/bountyrecon/tasks/T3/` cần **4** cấp `../` mới tới gốc, không phải 3.
`ls -d agents/security` → **không tồn tại**, nên cả 3 link **chết**.
**Territory BountyRecon — DocWriter không sửa.** Đáng chú ý: T3 **đã PASS kiểm định lớp 1 (T14)**,
nhưng T14 kiểm **nội dung `SCOPE.md`**, không kiểm link trong `CANDIDATES.md`
⇒ **đây là khoảng trống phạm vi kiểm định**, không phải cáo buộc Reviewer1 sai.

### 4.3 🆕 3 link thiếu scheme trong `agents/bountyrecon/tasks/T3/EVIDENCE/scope_github.md`

Dòng 185 có nguyên văn dạng *dấu-ngoặc-vuông bọc `lgtm-com.pentesting.semmle.net`, rồi
dấu-ngoặc-đơn chứa đúng chuỗi hostname đó* — và 2 chỗ tương tự cho
`backend-dot-lgtm-penetration-testing.appspot.com` và `downloads.lgtm.com`.

> (T22 ghi mô tả thay vì chép lại cặp ngoặc literal, vì chép lại sẽ **tạo thêm link chết ngay
> trong chính `INDEX.md`** — DocWriter đã tự phát hiện lỗi này ở bản nháp và sửa.)

Đây là **trích nguyên văn từ trang chính sách GitHub**, nơi URL gốc viết thiếu `https://`.
Markdown render thành link hỏng, **nhưng sửa lại sẽ phá tính nguyên văn** của bản trích.
⇒ DocWriter **không tự sửa**; **Admin quyết**: giữ nguyên văn, hay bọc trong code span để không render thành link.

### 4.4 🆕 16 file đã merge nhưng task nguồn KHÔNG có trong danh sách nghiệm thu

Các file sau có commit sửa cuối mang tiền tố **`[T2]`** (11 file) và **`[T4]`** (5 file),
**đã nằm trên `main`**, nhưng `ADMIN/SUMMARY.md` §1 **không** liệt kê T2 hay T4 là đã nghiệm thu,
và `ADMIN/ASSIGNMENTS.md` vẫn để **T2 = `⏳ todo`**, **T4 = `⏸ chờ T3`**:

```text
[T2] agents/researchlead/tasks/checkin.md
[T2] research/EVIDENCE/FETCH_STATUS.md            [T2] research/EVIDENCE/arxiv_lookups.txt
[T2] research/EVIDENCE/crossref_lookups.txt       [T2] research/EVIDENCE/openalex_authors.txt
[T2] research/EVIDENCE/openalex_doi_lookup.txt    [T2] research/EVIDENCE/openalex_title_filters.txt
[T2] research/EVIDENCE/quote_extracts.txt         [T2] research/ebpf-microsegmentation/EVIDENCE/openalex_queries.txt
[T2] research/ebpf-microsegmentation/PROPOSAL.md  [T2] research/pqc-tls-migration/EVIDENCE/openalex_queries.txt
[T4] agents/exploitdeep/T4/EVIDENCE/{msg-checkin,msg-report,msg-report-1,msg-report-2}.md
[T4] agents/exploitdeep/T4/EVIDENCE/tool_inventory_raw.txt
```

⇒ **Trạng thái của 16 file này trong bảng §2 là `🔄 chờ kiểm định`** — DocWriter **không** gán ✅
cho chúng. **Đề nghị Admin làm rõ:** T2/T4 đã qua lớp 1 chưa, hay đang ở `main` mà chưa được kiểm?

### 4.5 Đường dẫn còn thiếu (đã kiểm, chưa có trên `main`)

| # | Đường dẫn | Lý do | Ai làm |
|---|---|---|---|
| 1 | `reviews/VERIFY2.md` | nhánh **T8 chưa merge** (D-019 §1) | DeepSeek-Harness |
| 2 | `agents/deepseek-harness/**` | cùng lý do — **thư mục chưa tồn tại** | DeepSeek-Harness |
| 3 | `agents/forensicsmal/T5/**` | nhánh **T5 chưa merge** | ForensicsMal |
| 4 | `agents/javis/**`, `research/**/SOURCES_BROWSER.md` | nhánh **T13 chưa merge** | javis |
| 5 | `agents/antigravity/**`, `research/**/TESTBED.md` | **chưa có nhánh `agent/antigravity/T12`** | Antigravity (câu hỏi D-019 §4) |
| 6 | `security/**/FINDING.md`, `security/**/POC/**`, `security/**/EVIDENCE/**` | T4 chưa có `SCOPE.md` đạt điều kiện khai thác | ExploitDeep |

### 4.6 ✅ ĐÃ GIẢI QUYẾT — lệnh `say` (không còn là vấn đề mở)

Đính chính T1 của DocWriter đã được Admin xác nhận và **sửa xong**. DocWriter **đã tự kiểm lại**
trên máy này, không chỉ tin lời:

```bash
grep -n 'say' /home/noble-tran/agent-meet_skill/SKILL.md            # -> KHÔNG còn kết quả
sed -n '43p'  /home/noble-tran/agent-meet_skill/SKILL.md            # -> run.py send ... --file hello.md
grep -n 'say\|send' ~/.agents/skills/agentmeet/SKILL.md | head -1   # -> send --file  (bản thứ hai cũng đã sửa)
```

⇒ **Cả hai bản `SKILL.md` đều đã dùng `send --file`.** Mục này **đóng**.

### 4.7 ✅ ĐÃ GIẢI QUYẾT — lệch ngày và hai danh tính Admin

- **Ngày:** Admin chốt **`2026-10-01`** (DISSENT-4) — DocWriter từng **từ chối phán bên nào**, và
  việc chốt là **thẩm quyền Admin** (mục 4.3 bản T1).
- **Hai `agent_id` tên "Admin":** `ag_9026ba92` **bị `kicked`**, join lại `ag_cd389846`
  (`ADMIN/LOG.md` **#5**). Bảng §2 phản ánh qua cột tác giả: cả hai danh tính đều ghi
  **`Admin AgentMeet`** (đó là `%an` thật của commit).

## 5. Cảnh báo phạm vi

- INDEX này mô tả **trạng thái trình bày và trạng thái kiểm định theo `SUMMARY.md`**, **không**
  xác nhận **tính đúng đắn kỹ thuật** của bất kỳ file nào.
- **Chưa được Reviewer1 kiểm định.** DocWriter không tự verify theo luật D-004.
- Cột "Reviewer" là **theo phân công**, **không** phải "đã kiểm xong". Bảng §3.2 đếm nhãn
  `✅ đã nghiệm thu` **theo `SUMMARY.md`**, không theo việc DocWriter đọc file.
- **`reviews/CROSS.md` đã được điền** (last commit `[T11] 85ea56f`) — khác với mốc T1 khi file còn rỗng.

## 6. Lệnh kiểm chứng bảng này

```bash
cd /home/noble-tran/agentmeeting-docwriter
git ls-files | wc -l                      # phải ra 157 (mốc 0f41ebb)
git ls-files '*.md' | wc -l               # phải ra 71
git ls-files '*.txt' | wc -l              # phải ra 45
git ls-files '*.gitkeep' | wc -l          # phải ra 13
git ls-files '*.py' | wc -l               # phải ra 10
git ls-files '*.json' | wc -l             # phải ra 7
git ls-files '*.sh' | wc -l               # phải ra 2
git ls-files | grep '/' | sed 's|/[^/]*$||' | sort -u | wc -l   # phải ra 52
git log --oneline -1                      # phải ra 0f41ebb
# tác giả từng file (lấy commit thêm file lần đầu):
for f in $(git ls-files); do git log --diff-filter=A --format='%an' -- "$f" | tail -1; done | sort | uniq -c
# phải khớp bảng §3.1
# đếm lại bảng §2 (không được thiếu/thừa dòng, không dòng trống giữa bảng):
grep -c '^| [0-9]' INDEX.md               # phải ra 157
```

Nếu bất kỳ lệnh nào cho kết quả khác bảng ⇒ **bảng sai, phải sửa bảng**.
