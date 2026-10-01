# BLIND — Lớp 3: Kiểm tra mù

**Người phụ trách:** Reviewer1 (`ag_76306ba6`) · **Ngày tạo khung:** Admin ghi `2025-10-01` — **đính chính: `2026-10-01`** (xem CROSS.md DEF-5) · **Cập nhật:** 2026-10-01
**Trạng thái:** Giao thức đã hoàn thiện — **CHƯA thực thi bài kiểm mù nào** (lý do ở §6, nói thẳng)

---

## 1. Giao thức bắt buộc

1. Reviewer1 **CHỈ** được xem: đề bài/dữ liệu thô + tiêu chí đúng/sai.
2. **TUYỆT ĐỐI KHÔNG** mở `REPORT.md`, không xem kết luận, không xem danh tính tác giả trước khi làm xong.
3. Tự làm độc lập, ra kết quả riêng, **RỒI MỚI** mở kết quả gốc để so.
4. Lệch nhau ⇒ mở điều tra. Khớp ⇒ ghi nhận đã kiểm mù.
5. **CẤM** dùng lại artifact, log, ghi chú của tác giả.

---

## 2. Cơ chế ly thân (isolation) — thực hiện được bằng lệnh, không chỉ bằng lời hứa

Kiểm mù chỉ có giá trị nếu chứng minh được **đã không nhìn**. Vì vậy mỗi bài kiểm mù phải để lại
**bằng chứng ly thân**, không chỉ lời khai.

| Bước | Việc làm | Bằng chứng bắt buộc nộp |
|---|---|---|
| I1 | **Chốt "gói mù" TRƯỚC khi làm.** Gói mù = đề bài + dữ liệu thô + tiêu chí đúng/sai, do Admin đóng gói. | Danh sách đường dẫn file trong gói mù + `sha256sum` từng file |
| I2 | **Kiểm tra gói mù không chứa kết luận.** Quét chính gói mù tìm dấu hiệu kết luận/bản quả. | `grep -rniE "REPORT\|kết luận\|ket luan\|flag\{\|nghiệm thu\|PASS\|FAIL" <gói mù>` — phải cho kết quả đã ghi lại nguyên văn |
| I3 | **Làm trong thư mục riêng, sạch.** `/home/noble-tran/agentmeeting-reviewer1/blind/<task_id>/` — không clone chung, không copy file tác giả. | `pwd` + `ls -la` trước khi bắt đầu |
| I4 | **Không mở `REPORT.md`/kết luận.** Không `cat`, không `read`, không `git show` nhánh tác giả trước khi có kết quả riêng. | Nhật ký lệnh đã chạy (danh sách lệnh, theo thứ tự) |
| I5 | **Chốt kết quả riêng + hash.** Ghi kết quả của mình ra file, băm SHA256, **rồi mới** bắt đầu mở bản gốc. | `sha256sum <kết quả riêng>` + timestamp |
| I6 | **Mở bản gốc và so.** Chỉ sau I5. | Diff/so sánh từng tiêu chí |
| I7 | **Nếu lệch ⇒ điều tra tới cùng**, không kết luận "chắc do môi trường". Nêu rõ nguyên nhân gốc hoặc ghi `chưa xác minh`. | Lệnh điều tra + output |

**Dấu hiệu bài kiểm mù KHÔNG hợp lệ (phải làm lại):** không có hash kết quả riêng · kết quả riêng
được ghi *sau* khi mở bản gốc · thư mục làm việc dùng chung với tác giả · có bằng chứng đã đọc
`REPORT.md` trước I5.

---

## 3. Phiếu yêu cầu gói mù (Admin điền khi giao task)

```text
[TASK MÙ] task_id:
Đề bài (nguyên văn, KHÔNG kèm hướng giải):
Dữ liệu thô (đường dẫn + sha256 từng file):
Tiêu chí đúng/sai (danh sách kiểm được, không mơ hồ):
Định dạng kết quả Reviewer1 phải nộp:
Hạn nộp kết quả riêng (trước khi mở bản gốc):
```

**Reviewer1 từ chối nhận gói mù nếu:** gói chứa sẵn kết luận/tên tác giả · tiêu chí "đúng/sai" không
kiểm được (ví dụ "phân tích tốt") · không có dữ liệu thô mà chỉ có mô tả.

---

## 4. Bảng kết quả kiểm mù

| Task | Kết quả tự làm (mù) | sha256 kết quả riêng | Kết quả tác giả | Khớp? | Xử lý |
|---|---|---|---|---|---|
| — | *(chưa có bài kiểm mù nào)* | — | — | — | — |

---

## 5. Bảng mẫu — cấm bỏ trống cột hash

| Task | Kết quả tự làm (mù) | sha256 kết quả riêng | Kết quả tác giả | Khớp? | Xử lý |
|---|---|---|---|---|---|
| `T?/<slug>` | `<giá trị>` | `<sha256>` | `<giá trị>` | ✅/❌ | `<hành động>` |

---

## 6. Trạng thái thật — nói thẳng

**CHƯA có bài kiểm mù nào được thực thi.** Lý do cụ thể, không phải cái cớ:

1. **Chưa tồn tại đối tượng để kiểm mù.** Lớp 3 chỉ áp dụng cho artifact có **kết luận độc lập**
   (ví dụ `research/<slug>/REPORT.md` của T2, `security/**/FINDING.md` của T4, `**/FORENSICS.md` của T5).
   Tại thời điểm kiểm (2026-10-01), **chưa nhánh nào push artifact loại này**: `research/` và `security/`
   trên `origin/main` **chỉ có `.gitkeep`**; quét **cả 5 nhánh remote** không tìm thấy `REPORT.md`,
   `FINDING.md` hay `FORENSICS.md` nào. File duy nhất khớp mẫu tên là
   `agents/exploitdeep/T4/EVIDENCE/msg-report.md` — kiểm nội dung thì đây là **bản dump tin nhắn phòng**,
   **không phải báo cáo kết luận** (bằng chứng: `git ls-tree -r --name-only origin/agent/exploit-deep/T4`).
   Bằng chứng thô: `agents/reviewer1/evidence/T6/07-doi-tuong-kiem-mu.txt`.
2. **T0/`abe0c3e` KHÔNG phải đối tượng kiểm mù hợp lệ.** Nó là commit dựng khung — "đáp án" chính là
   cây thư mục, không có kết luận kỹ thuật nào để tự làm lại độc lập. Ép nó vào Lớp 3 sẽ là **giả tạo
   quy trình**, đúng thứ tôi phải chống. Vì vậy T0 đã được kiểm bằng **Lớp 1 (CROSS)** + **Lớp 2 (RECONCILE)**,
   và tôi **không** ghi nó vào bảng §4.
3. **Điều kiện sẵn sàng:** khi Admin giao artifact đầu tiên có kết luận thật (T2/T4/T5), tôi nhận
   gói mù theo §3 và nộp kết quả riêng kèm `sha256` **trước** khi mở bản gốc.

> Ghi rõ để không ai hiểu nhầm: **không có mục nào ở Lớp 3 được chấm PASS.** Bảng §4 để trống có chủ ý.

---

## 7. Đã kiểm những mục nào (bắt buộc — cấm báo "OK" chung chung)

- **Đã kiểm mù: 0 mục.** (Không có đối tượng — xem §6.)
- **Đã kiểm sự tồn tại của đối tượng kiểm mù: 3 mục** —
  (a) `research/` trên `origin/main` → chỉ `.gitkeep`;
  (b) `security/` trên `origin/main` → chỉ `.gitkeep`;
  (c) quét **cả 5 nhánh remote** (`main`, `agent/auditor-2/T7`, `agent/deepseek-harness/T8`, `agent/doc-writer/T1`, `agent/exploit-deep/T4`) → 0 file `REPORT.md`/`FINDING.md`/`FORENSICS.md` thật.
- **Đã hoàn thiện giao thức: 7 bước ly thân (I1-I7)** + phiếu yêu cầu gói mù (§3) + 4 tiêu chí
  vô hiệu hóa bài kiểm mù (§2).
- **Chưa kiểm:** mọi kết luận của T2/T4/T5 — **chưa tồn tại**.
