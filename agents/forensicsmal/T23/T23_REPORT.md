# T23_REPORT.md — Vá C2 của T5 + sửa sai số `capstone`

**Task:** T23 (thi hành **D-014**) · **Ngày:** 2025-10-01 (UTC 2026-10-01) · **Tác giả:** ForensicsMal (`ag_82f7cb07`)
**Nhánh:** `agent/forensics-mal/T23` · **Nền:** `agent/forensics-mal/T5` @ `ee97c37`

> **Vì sao nền là T5 chứ không phải `main`:** T5 **chưa merge** vào `main` (D-020 §4 xác nhận;
> `main` hiện chỉ có T15). Nếu tôi rẽ nhánh từ `main` thì T23 sẽ chứa **toàn bộ** T5 như file mới,
> và khi cả hai cùng merge sẽ **xung đột / nhân đôi**. Rẽ từ T5 giữ đúng quan hệ "sửa tiếp":
> merge T23 là ra **T5 + bản vá** trong một lần. Nếu Admin muốn cách khác, tôi làm lại theo chỉ thị.

---

## 1. Lỗ hổng được vá (D-014 mục 1)

**Lỗ hổng (Reviewer1 T21-A, Q2):** T5 dạy *"kết luận không có bộ ba công cụ + phiên bản + lệnh thì
không được đưa vào báo cáo"*, và C2 có ô cấm suy diễn khi thiếu công cụ. **Nhưng T5 không chặn
đúng lỗi ExploitDeep đã mắc ở T4:** chạy `pip list | grep -Ei '<danh sách viết tay>'`
rồi kết luận "thiếu" mà **không `import` thử**.

⇒ **Người làm đúng theo T5 vẫn lặp lại y nguyên lỗi đó.** Reviewer1 grep `"grep|lọc|KHONG LOC"`
trên cả 6 file T5 → **0 dòng khớp**. Đây là lỗ hổng trong chính sản phẩm của tôi.

**Đã vá:** thêm **3 ô bắt buộc** vào `agents/forensicsmal/T5/FORENSICS_PROCEDURE.md` §C2:

| Ô | Nội dung |
|---|---|
| **C2a** | Kiểm kê công cụ đã dùng `pip freeze`/`pip list` **KHÔNG LỌC** và lưu **nguyên output**? |
| **C2b** | Mỗi kết luận **"THIẾU"** đã chứng minh bằng `import <mod>` trong **ĐÚNG interpreter đang xét**, và **ghi rõ interpreter đó**? |
| **C2c** | Mỗi dòng **phiên bản** ghi rõ lấy từ **metadata** hay **`__version__`**? |

Kèm theo, tôi bổ sung phần giải thích **vì sao** ba ô này tồn tại (nêu thẳng cơ chế sai: danh sách
viết tay **luôn** thiếu tên gói, nên `grep` **luôn** xác nhận điều người viết đã tin sẵn), một
**câu tự vấn** trước khi được viết chữ "thiếu", và **quy ước ghi phiên bản** đặt ngay tại Bước 3 —
nơi phiên bản công cụ được ghi lần đầu.

**Điều chỉnh cho đúng thực tế máy này:** máy **không có `pip`** ⇒ C2a ghi rõ lệnh tương đương
`~/.local/bin/uv pip list --python <interpreter>`, để ô kiểm **hành động được**, không phải câu
chữ chết.

---

## 2. Chứng minh C2 mới BẮT ĐƯỢC lỗi (không chỉ là câu chữ)

Tôi **tái hiện lớp lỗi T4** trên gói **thật** đang cài — thay vì chỉ tuyên bố checklist sẽ chặn.
Script: `scripts/t23_c2_gap_demo.py` · output thô: `EVIDENCE/t23_c2_gap_demo_raw.txt`.

**Cách làm:** lấy danh sách viết tay 10 tên **module**, grep **có neo** (`^<tên> `) trên inventory,
rồi `import` từng tên trong **đúng** interpreter; so hai kết quả.

**Kết quả — 2 kết luận SAI nếu chỉ dùng grep:**

| module | grep có neo | `import` | Kết luận |
|---|---|---|---|
| `yara` | "thiếu" | **THÀNH CÔNG** | **grep SAI** (gói thật: `yara-python`) |
| `msoffcrypto` | "thiếu" | **THÀNH CÔNG** | **grep SAI** (gói thật: `msoffcrypto-tool`) |
| `pefile`, `scapy`, `capstone`, `volatility3`, `oletools` | có | OK | nhất quán |
| `unicorn`, `dissect`, `pyelftools` | "thiếu" | thất bại | nhất quán |

**Nguyên nhân:** **tên gói khác tên module**. `pip list` liệt kê **tên gói** (`yara-python`),
còn `import` dùng **tên module** (`yara`). Grep theo tên module sẽ không thấy ⇒ kết luận "thiếu" sai.

⇒ **Đây là bằng chứng rằng C2a + C2b là bắt buộc**, không phải nghi thức: nếu chỉ grep, tôi đã
báo sai rằng `yara` "thiếu" **trong khi chính T15 của tôi đã chạy được `yara-python`**.

> ⚠️ **Giới hạn khẳng định (tôi không vượt bằng chứng):** đây là **một** cơ chế thật của lớp lỗi
> "lọc tay" và tôi **tái hiện được** nó. Tôi **KHÔNG** khẳng định đây là cơ chế cụ thể đã làm T4
> kết luận sai về `unicorn` — tôi **chưa đọc bản gốc T4**, chỉ biết qua D-014/D-020.

---

## 3. Sửa sai số `capstone` (D-014 mục 2)

**Sự thật (tôi tự đo lại, không tin trí nhớ hay báo cáo trước):**

```
interpreter                              = /home/noble-tran/forensicsmal-tooling/.venv/bin/python
importlib.metadata.version("capstone")   = 5.0.9
capstone.__version__                     = 5.0.7
hai số có bằng nhau không                = False
```

⇒ **Cả hai đều THẬT, cùng một gói, và khác nhau.** T5 bản đầu ghi `5.0.9` ở 6 chỗ mà **không nói
nguồn** — đó là sai sót. Bằng chứng thô: `EVIDENCE/t23_capstone_version_recheck_raw.txt`.

**Đã sửa đủ 6 chỗ** (mỗi chỗ nay ghi rõ nguồn):

| File | Dòng cũ | Dòng mới | Nội dung mới |
|---|---|---|---|
| `T5/FORENSICS_PROCEDURE.md` | 94 | 110 | `capstone` **5.0.9 (metadata)** / **5.0.7 (`__version__`)** |
| `T5/FORENSICS_PROCEDURE.md` | 291 | 340 | bảng năng lực: `5.0.9 metadata / 5.0.7 __version__` |
| `T5/CHECKIN.md` | 45 | 46 | mục điểm mạnh: ghi rõ hai nguồn |
| `T5/CHECKIN.md` | 91 | 92 | bảng 6b: cột phiên bản ghi rõ hai nguồn |
| `T5/CHECKIN.md` | 144 | 145 | bảng sẵn sàng: ghi rõ hai nguồn |
| `T5/README.md` | 26 | 26 | ghi rõ hai nguồn |

Thêm một ghi chú ngay tại chỗ trong `FORENSICS_PROCEDURE.md` giải thích **vì sao có hai số** và
trỏ tới bằng chứng thô — để người sau không tưởng là mâu thuẫn.

**Kiểm chứng sau khi sửa:** `grep -rn "5\.0\.9"` trên 3 file tài liệu ⇒ **không còn dòng nào ghi số
trần thiếu nguồn** (dòng duy nhất còn lại là câu *mô tả* sai sót cũ, có chủ đích).
`EVIDENCE/tooling_bootstrap_raw.txt` **giữ nguyên** — đó là bằng chứng thô, **cấm sửa**
(dòng 13 = `5.0.9` từ `uv pip list`; dòng 32 = `5.0.7` từ `__version__`).

> **`chưa xác minh`:** số nào mới là phiên bản "đúng" về mặt phát hành. Tôi **không** tự phán quyết
> — Reviewer1/Auditor2 kiểm độc lập.

---

## 4. Artifact

| Tệp | Nội dung |
|---|---|
| `T23/EVIDENCE/t23_capstone_version_recheck_raw.txt` | Output thô đo lại hai nguồn phiên bản + inventory **không lọc** |
| `T23/EVIDENCE/t23_c2_gap_demo_raw.txt` | Output thô tái hiện lớp lỗi T4 + 2 kết luận sai bị bắt |
| `T23/EVIDENCE/t23_unfiltered_inventory_raw.txt` | Inventory **nguyên văn, không lọc** (theo chính C2a) |
| `T23/scripts/t23_c2_gap_demo.py` | Script tái hiện (sha256 `fc1c74d2…`) |
| `T5/FORENSICS_PROCEDURE.md`, `T5/CHECKIN.md`, `T5/README.md` | 3 file T5 đã vá |

---

## 5. CHƯA XÁC MINH

- **chưa xác minh** — số `capstone` nào là phiên bản "đúng" về phát hành.
- **chưa xác minh** — chi tiết gốc vụ `unicorn` ở T4: tôi **chưa đọc bản gốc T4**.
- **chưa xác minh** — script demo có bắt được **mọi** cơ chế của lớp lỗi "lọc tay" hay không;
  nó mới tái hiện **một** cơ chế (tên gói ≠ tên module).
- **chưa xác minh** — C2 mới có thực sự ngăn được lỗi trong tương lai hay chỉ mô tả đúng;
  **chỉ dùng thật mới biết**. Đây là hạn chế của mọi checklist.
- **chưa xác minh** — việc rẽ nhánh T23 từ T5 (thay vì `main`) có đúng ý Admin không;
  tôi đã nêu lý do ở đầu báo cáo và **sẵn sàng làm lại** nếu Admin chọn cách khác.

## 6. Ràng buộc đã tuân thủ

- ✅ Chỉ ghi trong territory `agents/forensicsmal/**`; **không** merge `main`.
- ✅ Không sửa bằng chứng thô (`tooling_bootstrap_raw.txt` giữ nguyên).
- ✅ Không bịa; chỗ không chắc ghi nguyên văn `chưa xác minh`.
- ✅ Không có mẫu/mã độc; không chạy mẫu; phân tích động vẫn đình chỉ.
- ✅ Theo D-004: **tôi không tự verify việc mình làm** — Reviewer1 verify lại (Admin đã nói vậy).
