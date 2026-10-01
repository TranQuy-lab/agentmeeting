# VERIFY2 — Giao thức tái lập độc lập (Verifier lớp 2)

**Người lập:** DeepSeek-Harness (`ag_d1739b2a`) — slot 8, vai trò Verifier lớp 2 (D-006)
**Phòng:** `ab1-478d-cfa7` · **Nhánh:** `agent/deepseek-harness/T8` · **Nền:** `main` @ `879d69d`
**Ngày:** 2025-10-01 · **Trạng thái:** GIAO THỨC ĐÃ DỰNG — chưa có artifact để chạy

---

## 0. Cam kết kiểm mù (blind verification)

```text
[CAM KẾT BẮT BUỘC]
Tôi KHÔNG đọc phần "Kết luận", "Kết quả", "PASS/FAIL" hay bảng tóm tắt của tác giả
TRƯỚC KHI tôi tự chạy xong và tự ghi lại output thô của mình.

Quy trình bắt buộc:
  B1. Chỉ đọc: mô tả bài toán, môi trường, lệnh cần chạy, artifact đóng băng.
  B2. Tự chạy lại từ đầu trên máy tôi; lưu output thô vào agents/deepseek-harness/T8/EVIDENCE/.
  B3. BẤM GIỜ + HASH output của tôi (sha256) TRƯỚC KHI mở phần kết luận tác giả.
  B4. Chỉ sau đó mới đọc kết luận tác giả và so khớp.
  B5. Ghi rõ mọi điểm KHÁC BIỆT. Khác biệt không được làm tròn thành "tương đương".

Vi phạm B1 (đọc kết luận trước khi chạy) => kết quả verify của tôi VÔ HIỆU, phải khai báo và làm lại.
```

**Lý do phải cam kết:** nếu tôi đọc kết luận trước, tôi sẽ vô thức chạy theo hướng dẫn đến kết quả
đó (anchoring). Khi ấy tôi không còn là nguồn độc lập thứ hai, chỉ là người thứ hai gật đầu.

---

## 1. Môi trường tái lập — phải ghi lại chính xác

Mỗi lần verify, ghi ĐỦ các mục sau vào `agents/deepseek-harness/T8/EVIDENCE/<finding_id>_env.txt`:

```bash
# Khối lệnh bắt buộc chạy và dán output thô
uname -a
python3 --version
git --version
gcc --version | head -1          # nếu có
sha256sum --version | head -1
echo "--- clone ---"
cd /home/noble-tran/agentmeeting-deepseek && git log --oneline -1 && git status --porcelain
echo "--- venv (nếu PoC cần) ---"
ls /home/noble-tran/.venvs/ 2>/dev/null || echo "khong co venv"
```

**Nguyên tắc:** môi trường của tôi KHÁC môi trường tác giả (clone riêng, venv riêng).
Đó là **điểm mạnh** — tái lập trên cây làm việc khác là bằng chứng mạnh hơn chạy lại trên chính máy tác giả.

---

## 2. Quy trình 6 bước cho mỗi artifact được giao verify

| Bước | Việc làm | Bằng chứng bắt buộc | Nếu thất bại |
|---|---|---|---|
| V1 | Xác minh artifact tồn tại đúng commit | `git rev-parse <commit>^{tree}`, `git cat-file -p <blob>` + sha256 file | Ghi `KHÔNG TÁI LẬP ĐƯỢC — artifact không tồn tại ở commit khai báo` |
| V2 | Chạy lại lệnh y hệt trên môi trường tôi | Output thô full, không cắt | Ghi `LỖI MÔI TRƯỜNG` tách khỏi `LỖI KỸ THUẬT` |
| V3 | Đối chiếu output tôi vs output tác giả | Diff từng dòng; nêu rõ dòng khác | Khác biệt ⇒ FAIL, không làm tròn |
| V4 | Đối chiếu nguồn độc lập (với khẳng định học thuật/scope) | ≥2 nguồn khác họ, có URL truy được | Thiếu nguồn thứ 2 ⇒ `CHƯA XÁC MINH`, không phải PASS |
| V5 | Kiểm tra rào cản pháp lý (nếu là finding bảo mật) | Đối chiếu SCOPE.md **trích nguyên văn** | Không trích được scope ⇒ **DỪNG**, báo Admin |
| V6 | Kết luận + tự khai giới hạn | Bảng PASS/FAIL kèm lệnh + output | Không có output thô ⇒ không được ghi PASS |

---

## 3. Thang kết luận (không dùng "OK" suông)

```text
PASS          — tôi chạy lại được, output KHỚP tác giả, có output thô dán kèm.
FAIL          — tôi chạy lại được nhưng output KHÁC tác giả. Ghi rõ khác ở đâu.
KHÔNG TÁI LẬP  — tôi không chạy lại được (thiếu tool/quyền/artifact). Ghi rõ thiếu gì.
CHƯA XÁC MINH  — không đủ nguồn/không đủ dữ liệu để kết luận. KHÔNG được coi là PASS.
DỪNG — PHÁP LÝ — phát hiện dấu hiệu ngoài scope. Dừng ngay, báo Admin + người dùng.
```

**Luật chống lạm dụng:** tôi **cấm** dùng `PASS` khi không có output thô. Nếu tác giả nộp kết luận
mà không kèm lệnh+output, kết quả mặc định của tôi là `KHÔNG TÁI LẬP`, không phải PASS.

---

## 4. Ánh xạ nguồn độc lập (dùng cho T2/T3 — tránh "2 nguồn cùng gốc")

Hai nguồn được coi là **độc lập** chỉ khi khác họ dữ liệu gốc. Ví dụ:

| Khẳng định | Nguồn 1 | Nguồn 2 hợp lệ | Nguồn 2 KHÔNG hợp lệ |
|---|---|---|---|
| DOI bài báo tồn tại | `api.crossref.org/works/<doi>` | `api.openalex.org/works/doi:<doi>` | một blog trích lại chính DOI đó |
| Chương trình bounty in-scope | trang policy gốc của chương trình | dữ liệu `bounty-targets-data` (đối chiếu chéo) | bài Medium tóm tắt lại policy |
| CVE tồn tại | `nvd.nist.gov/vuln/detail/<CVE>` | `cve.org` / MITRE record | diễn đàn nhắc lại mã CVE |

> Crossref và OpenAlex cùng lấy metadata từ nhà xuất bản ⇒ tôi ghi rõ đây là **độc lập một phần**,
> không tuyên bố "hai nguồn hoàn toàn độc lập".

---

## 5. Việc tôi TỪ CHỐI làm (ghi trước để không mặc cả sau)

```text
TỪ CHỐI 1: Tái lập PoC trên target không có scope công khai trích nguyên văn.
TỪ CHỐI 2: Target là cơ quan nhà nước / hạ tầng trọng yếu / tổ chức VN không có chương trình bounty.
TỪ CHỐI 3: DoS/DDoS, phá hoại, ransomware, backdoor, duy trì truy cập.
TỪ CHỐI 4: Truy cập, sao chép, lưu trữ dữ liệu thật hoặc dữ liệu cá nhân.
TỪ CHỐI 5: Mua bán/trao đổi lỗ hổng ngoài kênh chính thức.
TỪ CHỐI 6: Ký PASS cho artifact tôi chưa tự chạy.
TỪ CHỐI 7: Verify sản phẩm của chính tôi (D-004).
Tuân thủ Luật An ninh mạng Việt Nam 24/2018/QH14. Nghi ngờ phạm vi => DỪNG, hỏi Admin.
```

---

## 6. Sổ đăng ký verify (cập nhật dần)

| # | Artifact | Tác giả | Commit | Ngày nhận | Kết quả | Bằng chứng |
|---|---|---|---|---|---|---|
| — | *chưa có artifact nào được giao* | — | — | — | — | — |

**Trạng thái hiện tại:** T3 (`SCOPE.md`) và T4 (PoC) chưa xong ⇒ **chưa có gì để tái lập.**
Tôi không tạo việc giả để trông bận. Theo D-006 §2.4: báo Admin và giữ vòng poll.

---

## 7. Tự khai giới hạn của chính giao thức này

1. Giao thức này **chưa từng chạy trên artifact thật** — mọi bảng biểu ở §2/§3 là thiết kế, không phải kết quả.
2. Tôi **không có tài khoản bug bounty** ⇒ không tự đăng nhập kiểm chứng phần cần phiên đăng nhập.
3. Tôi **không tự verify file này**. Cần Reviewer1 hoặc Auditor2 kiểm độc lập; nếu hai bên bất đồng,
   **Auditor2** chốt (tôi không tự chốt vì tôi có lợi ích liên quan).
