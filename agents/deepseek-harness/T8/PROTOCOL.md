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
