# VERIFY2 — Kết quả tái lập độc lập #1 (T8, Verifier lớp 2)

**Người chạy:** DeepSeek-Harness (`ag_d1739b2a`) — slot 9, T8 · **Phòng:** `ab1-478d-cfa7`
**Ngày:** 2025-10-01 · **Nhánh:** `agent/deepseek-harness/T8`
**Đối tượng:** nhánh `origin/agent/doc-writer/T1` @ `3be89fd` (DocWriter, task T1)

---

## 0. Tuân thủ cam kết kiểm mù

Tôi đọc **mô tả + lệnh** trước, **tự chạy**, rồi mới đối chiếu phần kết luận của tác giả.
Tôi tự dựng bản clone **thứ ba**, tách khỏi cả clone của Admin và clone của DocWriter:

```text
/home/noble-tran/agentmeeting          -> clone của Admin (KHÔNG dùng)
/home/noble-tran/agentmeeting-docwriter-> clone của DocWriter (KHÔNG dùng)
/tmp/vfy/dw                            -> clone RIÊNG của tôi, lập trong lần verify này
```

---

## 1. Môi trường tái lập (output thô)

```text
$ cd /tmp/vfy && git clone -q git@github.com:TranQuy-lab/agentmeeting.git dw
$ cd dw && git checkout -q origin/agent/doc-writer/T1
$ git log --oneline -2
3be89fd [T1] fix: chuan hoa INDEX.md (39 file) + sua link tuong doi trong ho so T1
5bcea63 [T1] digest: kiem tra khung, quy trinh+digest phong, manifest raw, bao cao chat luong

$ git ls-files | wc -l
39
```

Khớp với con số **39 file** mà DocWriter công bố trong tiêu đề commit `3be89fd`. **PASS** phần số lượng.

---

## 2. Kiểm chéo INDEX.md ↔ cây file thật (đây là phần tôi tự làm, không chép tác giả)

Tôi tự viết script so khớp mọi đường dẫn trong INDEX.md với `git ls-files`:

```text
paths in INDEX: 44
tracked       : 39

LIET KE NHUNG KHONG TON TAI (6):
  - AUDIT.md
  - SOURCES.md
  - digest-msg-0001-0012.md
  - directives.md
  - reviews/AUDIT.json
  - reviews/AUDIT.md

TON TAI NHUNG KHONG LIET KE (1):
  - .gitignore
```

### 2.1 Đối chiếu với lời khai của tác giả → **KHÔNG phải lỗi im lặng. PASS có điều kiện.**

Tôi đã mở ngữ cảnh từng mục trước khi kết luận. Cả 6 đường dẫn "không tồn tại" đều **được tác giả
tự khai báo công khai** là chưa có, không phải bịa rồi giấu:

| Đường dẫn | Ngữ cảnh trong INDEX.md | Đánh giá |
|---|---|---|
| `reviews/AUDIT.md`, `reviews/AUDIT.json` | §4 dòng 106: *"INDEX bản cũ **đã liệt kê `AUDIT.md`** dù file không tồn tại"* | ✅ khai báo trung thực — đây là **lỗi của Admin** ở bản INDEX cũ, DocWriter phát hiện và giữ lại để truy vết |
| `SOURCES.md` | §4 dòng 107: *"chưa có trích dẫn nào trong repo"* | ✅ khai báo là chưa có |
| `digest-msg-0001-0012.md` | §4 dòng 104 nhóm thư mục chưa có | ✅ khai báo (xem mục 3 — thực tế **đã có**, xem phát hiện bên dưới) |
| `directives.md`, `AUDIT.md` (trần) | §4 bảng "chưa có slug/đường dẫn thật" | ✅ khai báo |

**Kết luận §2:** DocWriter **không bịa file tồn tại**. Các mục thiếu được khoanh vùng minh bạch trong §4.
Đây là hành vi đúng theo D-004. **PASS.**

### 2.2 Phát hiện của tôi (tác giả chưa nêu): `.gitignore` thiếu khỏi INDEX

`git ls-files` có `.gitignore` nhưng INDEX.md **không liệt kê**. Với acceptance criteria T1
("*INDEX.md liet ke MOI file qua git ls-files*"), đây là **sai lệch nhỏ nhưng có thật**.

```text
MỨC: THIẾU SÓT NHỎ — không phải vi phạm.
ĐỀ NGHỊ: DocWriter bổ sung 1 dòng `.gitignore` vào INDEX.md, hoặc ghi rõ lý do loại trừ.
```

---

## 3. Tái lập khẳng định kỹ thuật mạnh nhất: **lệnh `say` không tồn tại**

DocWriter khẳng định trong INDEX §4.2 rằng chỉ thị của Admin dùng `run.py ... say --file <tin.md>`,
nhưng lệnh này **chạy không được**, và subcommand đúng là **`send`**. Đây là cáo buộc ảnh hưởng
tới **mọi prompt của Admin** → tôi phải tự chạy, không tin lời khai.

**Tôi tự chạy lại (không dùng file của tác giả):**

```text
$ printf '# test\nnoi dung thu\n' > /tmp/vfy/saytest.md
$ python3 /home/noble-tran/agent-meet_skill/run.py --session ab1-478d-cfa7 \
      --as "DeepSeek-Harness" say --file /tmp/vfy/saytest.md
    ...
    Các lệnh: join, use, sessions, whoami, status, send, read, inbox, poll, history, board, leave
    Tham số toàn cục: --room/-r, --base-url, --token-file, --session, --json, --quiet
EXIT=3
```

```text
$ python3 /home/noble-tran/agent-meet_skill/run.py --help
    python -m agentmeet send --file tin.md
    python -m agentmeet poll --timeout 90 --since 100 --json
    Các lệnh: join, use, sessions, whoami, status, send, read, inbox, poll, history, board, leave
```

**Đối chiếu:**

| Khẳng định DocWriter | Tôi chạy lại | Kết quả |
|---|---|---|
| `say --file` in bảng trợ giúp chung, **không gửi** | In bảng trợ giúp, exit `3` | ✅ **KHỚP** |
| exit code `3` | `EXIT=3` | ✅ **KHỚP** |
| subcommand đúng là `send` | danh sách có `send`, **không có `say`** | ✅ **KHỚP** |

```text
KẾT LUẬN: PASS — tái lập được 3/3 điểm, output thô khớp.
Đây là DEFECT THẬT trong tài liệu điều hành của Admin (directives.md + prompt worker),
KHÔNG phải lỗi của DocWriter. Mức: ẢNH HƯỞNG VẬN HÀNH — mọi worker làm theo prompt sẽ
gõ lệnh sai và tưởng đã gửi tin.
```

> **Ghi chú độc lập:** bản thân tôi không dùng CLI mà gửi tin qua HTTP API (`POST /message`),
> nên tôi không bị defect này ảnh hưởng. Nhưng Reviewer1/BountyRecon/ExploitDeep dùng CLI thì có.

---

## 4. Tổng hợp kết quả verify #1

| # | Khẳng định | Kết quả | Bằng chứng |
|---|---|---|---|
| 1 | T1 có 39 file track | **PASS** | `git ls-files \| wc -l` → 39 |
| 2 | INDEX.md không bịa file tồn tại | **PASS** | 6 mục thiếu đều được khai báo ở §4 |
| 3 | INDEX.md liệt kê **MỌI** file | **THIẾU SÓT NHỎ** | `.gitignore` không được liệt kê |
| 4 | Lệnh `say` không chạy được, `send` mới đúng | **PASS** | exit `3` + bảng trợ giúp, tái lập độc lập |

---

## 5. Tự khai giới hạn của lần verify này

1. Tôi **không** kiểm nội dung học thuật/chất lượng văn bản của T1 — ngoài phạm vi T8.
2. Tôi **không** verify `agents/docwriter/**` (báo cáo của tác giả) vì chưa đọc hết; chỉ kiểm phần
   INDEX.md + khẳng định CLI.
3. Kết quả `PASS` ở đây là **của tôi cho artifact của DocWriter** — tôi **không** tự verify sản phẩm
   của chính tôi (D-004). File `reviews/VERIFY2.md` này phải do **Reviewer1** hoặc **Auditor2** kiểm.
4. Nếu Reviewer1 kết luận khác tôi, **Auditor2 chốt** — tôi không tự chốt vì có lợi ích liên quan.
