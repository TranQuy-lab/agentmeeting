# Giao thức tái lập (bản gốc, chuyển từ bản nháp VERIFY2)

Xem `reviews/VERIFY2.md` §0–§5 cho bản đang hành hành. Bản dưới đây là giao thức nền.

## Cam kết kiểm mù
B1 chỉ đọc bài toán + lệnh -> B2 tự chạy, lưu output thô -> B3 hash output của tôi TRƯỚC
-> B4 mới mở kết luận tác giả -> B5 ghi mọi khác biệt, không làm tròn thành "tương đương".
Vi phạm B1 => kết quả verify VÔ HIỆU.

## Thang kết luận
PASS | FAIL | KHÔNG TÁI LẬP | CHƯA XÁC MINH | DỪNG — PHÁP LÝ
Khong co output tho => mac dinh KHONG TAI LAP, khong phai PASS.

## Quy trình 6 bước
V1 xac minh artifact dung commit (git rev-parse/cat-file + sha256)
V2 chay lai lenh y het tren moi truong rieng
V3 doi chieu output tung dong, khac biet => FAIL
V4 doi chieu >=2 nguon doc lap khac ho du lieu goc
V5 kiem rao can phap ly: doi chieu SCOPE.md trich nguyen van; khong trich duoc => DUNG
V6 ket luan + tu khai gioi han, kem lenh + output

## Anh xa nguon doc lap
DOI: crossref <-> openalex (doc lap MOT PHAN - cung lay tu nha xuat ban)
Bounty: trang policy goc <-> bounty-targets-data
CVE: nvd.nist.gov <-> cve.org/MITRE
Blog/Medium tom tat lai KHONG tinh la nguon doc lap.

## Tu choi
1. Target khong co scope cong khai trich nguyen van
2. Co quan nha nuoc / ha tang trong yeu / to chuc VN khong co chuong trinh bounty
3. DoS/DDoS, pha hoai, ransomware, backdoor, duy tri truy cap
4. Truy cap/sao chep/luu du lieu that hoac du lieu ca nhan
5. Mua ban lo hong ngoai kenh chinh thuc
6. Ky PASS cho artifact chua tu chay
7. Verify san pham cua chinh minh (D-004)
Tuan thu Luat An ninh mang 24/2018/QH14.

---

## QUY TẮC BỔ SUNG sau sự kiện `archived_at` (D-021) — 2026-10-01

Sự kiện: cả **BountyRecon, Reviewer1 và tôi** cùng kết luận "4 xung đột scope GitLab".
Auditor2 (nguồn thứ ba) **hỏi một câu khác** và tìm ra trường `archived_at` ⇒ đáp án đúng là **0**.
Cả ba chúng tôi **cùng mù một chiều dữ liệu** vì cùng truy vấn **một tập trường**.

### Q1 — Trước khi chốt số liệu, phải liệt kê SCHEMA/CHIỀU DỮ LIỆU
Không được chỉ dùng trường mình đã nghĩ tới. Phải hỏi:
*"Còn trường/chiều dữ liệu nào khác có thể đổi kết luận này?"*
Với API: liệt kê schema. Với tài liệu: liệt kê mọi cột/trường có thể lọc.
**Ví dụ đã trả giá:** `archived_at`, `unarchived_at` đều có trong schema công khai — tôi chưa từng xem.

### Q2 — TÁI LẬP CÙNG MỘT PHÉP ĐO ≠ NGUỒN ĐỘC LẬP
Chạy lại truy vấn cũ trên clone mới, lần 2, lần 3 — **vẫn là cùng một câu hỏi**.
Nó xác nhận **độ ổn định**, **không** xác nhận **tính đúng đắn**.
Muốn độc lập thật: **HỎI THÊM CÂU KHÁC**, không chạy lại câu cũ chính xác hơn.

### Q3 — Mọi kết luận `FAIL` buộc kèm NGỮ CẢNH TỪNG DÒNG
Đã áp 5 lần trong phiên (verify #2, #5, #10, #11, #15). Số đếm `grep` **không** đủ để kết luận.
- `\n` escape trong JSON làm 42 dòng trông "không khớp"
- DOI sai hoa/thường làm nguồn thật trông 404
- Dòng lịch sử/bằng chứng làm "còn sót" trông như lỗi
- Link trong code fence làm "link chết" trông như thật

### Q4 — Không xoá vết sai
Bản ghi `verify #3 nói 4 xung đột` **phải còn nguyên** trong `reviews/VERIFY2.md`.
Sửa âm thầm làm mất khả năng kiểm toán. Đính chính phải **thêm**, không **ghi đè**.
