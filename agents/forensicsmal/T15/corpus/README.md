# Corpus T15 — TỔNG HỢP VÔ HẠI, TỰ TẠO

**Mọi thứ trong thư mục này là vô hại và do ForensicsMal tự tạo.** Không có mã độc thật.

## Nguyên tắc

- Corpus **sinh ra từ script** trong `../scripts/`, **không** commit artifact nhị phân.
- Các file dưới đây **bị gitignore có chủ đích** (xem `.gitignore` trong thư mục này):
  binary build, `.bin`, `.pcap`. Chúng **tái lập được** bằng cách chạy lại script.
- Hash của **mọi** file (kể cả file không commit) được ghi tại
  `../EVIDENCE/t15_0_corpus_hashes.txt` ⇒ neo bằng chứng vẫn kiểm chứng được.

## Nguồn gốc từng nhóm

| File | Nguồn | Vô hại vì |
|---|---|---|
| `bench_elf.c` | **được commit** — người viết tự soạn | chương trình C tối giản (`add`/`loop_sum`/`classify`/`main`) |
| `bench_elf`, `bench_elf.text.bin` | `gcc` biên dịch từ `bench_elf.c` | ELF của chính chúng ta; **không commit** |
| `dns_harmless.pcap` | `t15_pcap_test.py` (scapy) | 1 truy vấn DNS cho `example.invalid` (TLD reserved, RFC 2606/6761); IP TEST-NET-1 (RFC 5737) |
| `t15_rules.yar` | **được commit** — người viết tự soạn | rule YARA cho chuỗi marker do ta đặt |
| `yara_A..D*.txt` | `t15_yara_test.py` | văn bản + marker do ta đặt |
| `yara_F_boundary.bin` | `t15_yara_test.py` | đệm `'A'` + marker đặt vắt mốc 4096 |
| `yara_G_wide.bin` | `t15_yara_test.py` | marker mã hoá UTF-16LE |
| `invalid_*.bin` | `t15_volatility_test.py` | file rỗng / byte ngẫu nhiên seed=1337 / số 0 |

`example.invalid` và `host.t15.invalid` dùng TLD `.invalid` — **không thể** phân giải trên
Internet thật. Không script nào gọi mạng: MAC/IP đặt tường minh nên scapy không ARP.

## Tái lập

```bash
V=/home/noble-tran/forensicsmal-tooling/.venv/bin/python
cd agents/forensicsmal/T15
$V scripts/t15_pcap_test.py
$V scripts/t15_elf_test.py
$V scripts/t15_yara_test.py       # cần bench_elf: chạy t15_elf_test.py trước
$V scripts/t15_volatility_test.py
```

## Cấm

❌ Đặt mã độc thật, mẫu thật, dump, hay dữ liệu cá nhân vào đây.
❌ Push artifact nhị phân (gitignore đã chặn — tôn trọng nghiêm ngặt).
