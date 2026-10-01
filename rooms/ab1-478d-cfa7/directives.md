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
Nghi ngờ về phạm vi => DỪNG, hỏi Admin. KHÔNG tự đoán.
```
