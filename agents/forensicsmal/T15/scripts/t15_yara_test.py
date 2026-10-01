#!/usr/bin/env python3
"""
T15-3 — KIEM CHUAN YARA: kiem CA am tinh gia (false negative), khong chi duong tinh.
Muc tieu: chung minh yara-python phan loai DUNG tren mot corpus CO NHAN ground-truth.

Phuong phap: dung ma tran nham lan (confusion matrix) TP/TN/FP/FN
  - TP (true positive)  : rule PHAI khop, va CO khop
  - TN (true negative)  : rule PHAI KHONG khop, va KHONG khop
  - FP (duong tinh gia) : rule PHAI KHONG khop, nhung CO khop   <- bug rule
  - FN (am tinh gia)    : rule PHAI khop, nhung KHONG khop      <- bug rule / miss

CORPUS VO HAI 100% do chinh chung ta tao. KHONG co mau doc hai.
KHONG co `yara` CLI tren may => scan qua API yara-python (ghi ro de nguoi doc biet).
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
CORPUS.mkdir(exist_ok=True)

import yara  # noqa: E402
import importlib.metadata as md  # noqa: E402


def section(t):
    print("\n" + "=" * 70 + f"\n{t}\n" + "=" * 70)


# ------------------------------------------------------- 1. TAO CORPUS VO HAI
section("BUOC 1 — Tao corpus VO HAI co NHAN ground-truth")

A = CORPUS / "yara_A_marker_upper.txt"
B = CORPUS / "yara_B_url.txt"
C = CORPUS / "yara_C_lowercase.txt"
D = CORPUS / "yara_D_clean.txt"
E = CORPUS / "bench_elf"          # ELF do T15-2 bien dich (tai su dung)
F = CORPUS / "yara_F_boundary.bin"
G = CORPUS / "yara_G_wide.bin"

FILES = {
    "A_marker_upper": A,
    "B_url": B,
    "C_lowercase": C,
    "D_clean": D,
    "E_elf_binary": E,
    "F_boundary": F,
    "G_wide_utf16": G,
}

A.write_bytes(b"corpus T15 vo hai\nFORENSICSMAL_T15_MARKER_ALPHA\nhet\n")
B.write_bytes(b"corpus T15 vo hai\nhttps://host.t15.invalid/path?x=1\nhet\n")
C.write_bytes(b"corpus T15 vo hai\nforensicsmal_t15_marker_alpha\nhet\n")
D.write_bytes(b"corpus T15 vo hai\nkhong co chi bao nao o day\nchi la van ban sach\n")

# F: marker STRADDLE ranh gioi chunk 4KB cua YARA (4KB block + 4KB overlap).
# Day la bay AM TINH GIA that su: neu YARA khong xu ly overlap dung thi se miss.
MARK = b"FORENSICSMAL_T15_MARKER_ALPHA"
buf = bytearray(b"\x41" * 16384)               # nen 'A' vo hai
start = 4096 - 10                               # bat dau truoc moc 4096 dung 10 byte
buf[start:start + len(MARK)] = MARK
print(f"  [F] marker dat tai offset {start}..{start+len(MARK)-1} "
      f"(STRADDLE moc chunk 4096: {start} < 4096 < {start+len(MARK)})")
F.write_bytes(bytes(buf))

# G: cung marker nhung ma hoa UTF-16LE ("wide") — bay AM TINH GIA thu 2.
G.write_bytes("corpus T15 vo hai\n".encode() + MARK.decode().encode("utf-16-le") + b"\n")

for name, p in FILES.items():
    if not p.exists():
        print(f"  [!] THIEU {p} — can chay T15-2 truoc de co ELF.")
        sys.exit(1)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print(f"  {name:<16} {p.name:<28} {p.stat().st_size:>6} byte  sha256={h[:16]}...")
print("\n  'host.t15.invalid' dung TLD .invalid (RFC 2606) => khong the phan giai that.")

# ------------------------------------------------------------- 2. VIET RULES
section("BUOC 2 — Bo rule YARA (co y do ro rang cho tung rule)")
RULES = r"""
/* T15 — bo rule kiem chuan. Corpus VO HAI do ForensicsMal tu tao. */

rule t15_marker_alpha
{
    meta:
        y_don_do = "PHAI khop A; PHAI KHONG khop B/C/D/E (case-sensitive)"
    strings:
        $m = "FORENSICSMAL_T15_MARKER_ALPHA"
    condition:
        $m
}

rule t15_url_invalid
{
    meta:
        y_don_do = "PHAI khop B; PHAI KHONG khop A/C/D"
    strings:
        $u = /https?:\/\/[a-z0-9.\-]+\.invalid(\/[^\s]*)?/
    condition:
        $u
}

rule t15_case_insensitive
{
    meta:
        y_don_do = "PHAI khop CA A va C (nocase); PHAI KHONG khop D"
    strings:
        $m = "forensicsmal_t15_marker_alpha" nocase
    condition:
        $m
}

rule t15_absent_string
{
    meta:
        y_don_do = "KHONG duoc khop BAT KY file nao (bay bat duong tinh gia)"
    strings:
        $x = "THIS_MARKER_MUST_NOT_EXIST_ANYWHERE_T15"
    condition:
        $x
}

rule t15_mz_header_pe
{
    meta:
        y_don_do = "KHONG duoc khop file van ban nao (bay duong tinh gia); corpus khong co PE"
    condition:
        uint16(0) == 0x5A4D
}

rule t15_elf_magic
{
    meta:
        y_don_do = "PHAI khop E (ELF); KHONG khop file van ban"
    condition:
        uint32(0) == 0x464C457F
}

rule t15_boundary_marker
{
    meta:
        y_don_do = "PHAI khop F (marker STRADDLE moc chunk 4KB) — bay AM TINH GIA"
    strings:
        $m = "FORENSICSMAL_T15_MARKER_ALPHA"
    condition:
        $m
}

rule t15_wide_marker
{
    meta:
        y_don_do = "PHAI khop G (UTF-16LE); KHONG khop A (ASCII)"
    strings:
        $m = "FORENSICSMAL_T15_MARKER_ALPHA" wide
    condition:
        $m
}
"""
RULEFILE = CORPUS / "t15_rules.yar"
RULEFILE.write_text(RULES)
(h, ) = (hashlib.sha256(RULEFILE.read_bytes()).hexdigest(),)
print(f"# rule file: {RULEFILE.name} ({RULEFILE.stat().st_size} byte) sha256={h}")
print(RULES)

print(f"# yara-python: package metadata = {md.version('yara-python')}; "
      f"module __version__ = {getattr(yara, '__version__', '(khong co)')}")
print(f"# LUU Y: KHONG co `yara` CLI tren may nay => scan qua API yara-python.")

# ------------------------------------------------- 3. MA TRAN MONG DOI (nhan)
section("BUOC 3 — Ma tran MONG DOI (ground truth do nguoi viet dat ra)")
EXPECT = {
    "t15_marker_alpha":     {"A_marker_upper": True,  "B_url": False, "C_lowercase": False, "D_clean": False, "E_elf_binary": False, "F_boundary": True,  "G_wide_utf16": False},
    "t15_url_invalid":      {"A_marker_upper": False, "B_url": True,  "C_lowercase": False, "D_clean": False, "E_elf_binary": False, "F_boundary": False, "G_wide_utf16": False},
    "t15_case_insensitive": {"A_marker_upper": True,  "B_url": False, "C_lowercase": True,  "D_clean": False, "E_elf_binary": False, "F_boundary": True,  "G_wide_utf16": False},
    "t15_absent_string":    {"A_marker_upper": False, "B_url": False, "C_lowercase": False, "D_clean": False, "E_elf_binary": False, "F_boundary": False, "G_wide_utf16": False},
    "t15_mz_header_pe":     {"A_marker_upper": False, "B_url": False, "C_lowercase": False, "D_clean": False, "E_elf_binary": False, "F_boundary": False, "G_wide_utf16": False},
    "t15_elf_magic":        {"A_marker_upper": False, "B_url": False, "C_lowercase": False, "D_clean": False, "E_elf_binary": True,  "F_boundary": False, "G_wide_utf16": False},
    "t15_boundary_marker":  {"A_marker_upper": True,  "B_url": False, "C_lowercase": False, "D_clean": False, "E_elf_binary": False, "F_boundary": True,  "G_wide_utf16": False},
    "t15_wide_marker":      {"A_marker_upper": False, "B_url": False, "C_lowercase": False, "D_clean": False, "E_elf_binary": False, "F_boundary": False, "G_wide_utf16": True},
}
hdr = f"  {'rule':<24}" + "".join(f"{k.split('_')[0]:>4}" for k in FILES)
print(hdr)
for r, exp in EXPECT.items():
    print(f"  {r:<24}" + "".join(f"{('M' if exp[k] else '.'):>4}" for k in FILES))
print("  (M = PHAI khop; . = PHAI KHONG khop)")

# ------------------------------------------------------------------ 4. SCAN
section("BUOC 4 — Chay scan that bang yara-python")
rules = yara.compile(filepath=str(RULEFILE))
ACTUAL = {}
for rname in EXPECT:
    ACTUAL[rname] = {}
    for fkey, fpath in FILES.items():
        m = rules.match(str(fpath))
        ACTUAL[rname][fkey] = rname in [x.rule for x in m]

cmd_desc = (f'$ python3 -c "import yara; r=yara.compile(filepath=\'{RULEFILE.name}\'); '
            f'r.match(<file>)"')
print(cmd_desc + "\n")

print("  --- Ket qua THO tung file (rule nao khop) ---")
for fkey, fpath in FILES.items():
    m = rules.match(str(fpath))
    hits = sorted(x.rule for x in m)
    print(f"  {fkey:<16} {fpath.name:<28} -> {hits if hits else 'KHONG rule nao khop'}")

# ------------------------------------------------------- 5. DOI CHIEU TP/TN/FP/FN
section("BUOC 5 — Doi chieu: TP / TN / FP (duong tinh gia) / FN (AM TINH GIA)")
TP = TN = FP = FN = 0
fp_list, fn_list = [], []
print(f"  {'rule':<24}{'file':<16}{'mong doi':>9}{'thuc te':>9}   ket qua")
for rname, exp in EXPECT.items():
    for fkey in FILES:
        want = exp[fkey]
        got = ACTUAL[rname][fkey]
        if want and got:
            verdict, TP = "TP", TP + 1
        elif not want and not got:
            verdict, TN = "TN", TN + 1
        elif not want and got:
            verdict, FP = "FP  <-- DUONG TINH GIA", FP + 1
            fp_list.append((rname, fkey))
        else:
            verdict, FN = "FN  <-- AM TINH GIA", FN + 1
            fn_list.append((rname, fkey))
        print(f"  {rname:<24}{fkey:<16}{('KHOP' if want else 'khong'):>9}"
              f"{('KHOP' if got else 'khong'):>9}   {verdict}")

print(f"\n  TONG: TP={TP}  TN={TN}  FP(duong tinh gia)={FP}  FN(AM TINH GIA)={FN}")
print(f"  Tong so phep kiem: {len(EXPECT)*len(FILES)}")
if fp_list:
    print(f"\n  DUONG TINH GIA (rule khop khi khong duoc phep): {fp_list}")
if fn_list:
    print(f"\n  AM TINH GIA (rule KHONG khop khi phai khop): {fn_list}")

# ------------------------------------------------------------------ KET LUAN
section("KET LUAN T15-3")
acc = (TP + TN) / (TP + TN + FP + FN) * 100
print(f"  Do chinh xac tren corpus co nhan: {acc:.1f}%  ({TP+TN}/{TP+TN+FP+FN})")
print(f"  Rule PHAI khop, da khop (TP)          : {TP}")
print(f"  Rule PHAI KHONG khop, da khong khop   : {TN}")
print(f"  DUONG TINH GIA (FP)                   : {FP}")
print(f"  AM TINH GIA (FN)                      : {FN}")
if FP == 0 and FN == 0:
    print("\n>>> KET QUA: 0 duong tinh gia, 0 AM TINH GIA tren "
          f"{len(EXPECT)*len(FILES)} phep kiem.")
    print("    => yara-python phan loai DUNG ca hai chieu tren corpus co nhan.")
    print("    => Rule t15_absent_string va t15_mz_header_pe la BAY duong tinh gia:")
    print("       ca hai deu KHONG khop file nao — neu khop thi la bug.")
    print("    => Rule t15_case_insensitive khop CA chu HOA (A) va chu thuong (C),")
    print("       con t15_marker_alpha chi khop chu HOA => kiem duoc CA hai chieu")
    print("       cua tinh phan biet chu hoa/thuong.")
    print("    => BAY AM TINH GIA THAT SU (khong de):")
    print("       F: marker STRADDLE moc chunk 4KB cua YARA -> t15_boundary_marker")
    print("          PHAI khop; neu YARA xu ly overlap sai thi day chinh la FN.")
    print("       G: marker ma hoa UTF-16LE -> t15_wide_marker PHAI khop G")
    print("          va PHAI KHONG khop A (ASCII) => kiem ca hai chieu cua 'wide'.")
else:
    print("\n>>> KET QUA: CO LOI — xem FP/FN o tren.")
    sys.exit(1)
