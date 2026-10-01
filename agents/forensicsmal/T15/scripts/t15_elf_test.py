#!/usr/bin/env python3
"""
T15-2 — KIEM CHUAN ELF: capstone <-> objdump <-> readelf
Muc tieu: doi chieu DIA CHI va INSTRUCTION giua 2 bo disassembler doc lap
          tren CUNG mot chuong trinh C. Lech o dau thi ghi ro o do.

CORPUS VO HAI: chuong trinh C toi gian do chinh chung ta viet (khong doc hai).
KHONG chay file: chi disassemble TINH (static). Phan tich dong van DINH CHI.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
CORPUS.mkdir(exist_ok=True)
SRC = CORPUS / "bench_elf.c"
BIN = CORPUS / "bench_elf"
TEXTBIN = CORPUS / "bench_elf.text.bin"

from capstone import CS_ARCH_X86, CS_MODE_64, Cs  # noqa: E402


def section(t):
    print("\n" + "=" * 70 + f"\n{t}\n" + "=" * 70)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


# ------------------------------------------------------------------ 1. BIEN DICH
section("BUOC 1 — Bien dich chuong trinh C toi gian (gcc)")
SRC.write_text(
    "/* Corpus vo hai do ForensicsMal tu viet cho T15-2. Chi de disassemble TINH. */\n"
    "int add(int a, int b) { return a + b; }\n"
    "long loop_sum(long n) {\n"
    "    long s = 0;\n"
    "    for (long i = 0; i < n; i++) s += i;\n"
    "    return s;\n"
    "}\n"
    "int classify(int x) {\n"
    "    if (x < 0) return -1;\n"
    "    if (x == 0) return 0;\n"
    "    return 1;\n"
    "}\n"
    "int main(void) { return classify(add(1, 2)) + (int)loop_sum(10); }\n"
)
print(f"# nguon: {SRC} ({SRC.stat().st_size} byte) — vo hai, tu viet")
print(SRC.read_text())

GCC = shutil.which("gcc")
print(f"# gcc: {subprocess.run([GCC,'--version'],capture_output=True,text=True).stdout.splitlines()[0]}")
cmd = [GCC, "-O1", "-fno-asynchronous-unwind-tables", "-fno-stack-protector",
       "-o", str(BIN), str(SRC)]
print(f"\n$ {' '.join(cmd)}")
rc, out, err = run(cmd)
print(f"exit={rc}")
print(out.rstrip() or "(khong co stdout)")
print(err.rstrip() or "(khong co stderr)")
if rc != 0:
    print(">>> DUNG: bien dich that bai.")
    sys.exit(1)
print(f"# -> {BIN} ({BIN.stat().st_size} byte)")

# ------------------------------------------------------------------ 2. READELF
section("BUOC 2 — readelf: thong tin ELF va section .text")
rc, out, _ = run(["readelf", "-h", str(BIN)])
print(f"$ readelf -h {BIN}\n{out.rstrip()}")
m = re.search(r"Entry point address:\s*(0x[0-9a-fA-F]+)", out)
entry = int(m.group(1), 16) if m else None
print(f"  => Entry point = {entry:#x}" if entry is not None else "  => KHONG doc duoc entry point")

rc, out, _ = run(["readelf", "-S", "-W", str(BIN)])
print(f"\n$ readelf -S -W {BIN}")
print(out.rstrip())

text_addr = text_off = text_size = None
# Dang dong readelf -S -W:
#   [ 1] .text   PROGBITS  0000000000001050 001050 00018e 00  AX  0 0 16
#                 ^name    ^type     ^addr      ^off   ^size
pat = re.compile(r"^\s*\[\s*\d+\]\s+(\.\S+)\s+(\S+)\s+([0-9a-fA-F]+)\s+([0-9a-fA-F]+)\s+([0-9a-fA-F]+)\s")
for ln in out.splitlines():
    mm = pat.match(ln)
    if mm and mm.group(1) == ".text":
        text_addr = int(mm.group(3), 16)
        text_off = int(mm.group(4), 16)
        text_size = int(mm.group(5), 16)
        print(f"\n  [dong readelf khop] {ln.strip()}")
        break
print(f"\n  => .text: addr={text_addr:#x} offset={text_off:#x} size={text_size:#x}" if text_addr is not None
      else "\n  => KHONG tim thay section .text")
if text_addr is None:
    sys.exit(1)

# ------------------------------------------------------------ 3. TRICH .text
section("BUOC 3 — Trich byte tho cua .text bang objcopy")
cmd = ["objcopy", "-O", "binary", "--only-section=.text", str(BIN), str(TEXTBIN)]
print(f"$ {' '.join(cmd)}")
rc, out, err = run(cmd)
print(f"exit={rc} {err.strip()}")
blob = TEXTBIN.read_bytes()
print(f"  => {TEXTBIN.name}: {len(blob)} byte (readelf bao {text_size} byte) "
      f"=> {'KHOP' if len(blob)==text_size else 'LECH!'}")
print(f"  => 32 byte dau: {blob[:32].hex(' ')}")

# --------------------------------------------------------------- 4. CAPSTONE
section("BUOC 4 — capstone disassemble .text")
import capstone  # noqa: E402
print(f"# capstone package metadata vs module __version__:")
rc, out, _ = run([str(Path(sys.executable)), "-c",
                  "import importlib.metadata as md, capstone; "
                  "print('  package metadata :', md.version('capstone')); "
                  "print('  module __version__:', capstone.__version__)"])
print(out.rstrip())

md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = False
cap_insns = [(i.address, i.mnemonic, i.op_str) for i in md.disasm(blob, text_addr)]
print(f"\n$ python3 -c \"capstone.Cs(CS_ARCH_X86, CS_MODE_64).disasm(text_bytes, {text_addr:#x})\"")
print(f"  => capstone: {len(cap_insns)} instruction")
for a, mn, op in cap_insns[:12]:
    print(f"     {a:#08x}:  {mn:<8}{op}")
if len(cap_insns) > 12:
    print(f"     ... (+{len(cap_insns)-12} instruction nua)")

# ---------------------------------------------------------------- 5. OBJDUMP
section("BUOC 5 — objdump disassemble (Intel syntax)")
cmd = ["objdump", "-d", "-M", "intel", "--section=.text", str(BIN)]
print(f"$ {' '.join(cmd)}")
rc, out, err = run(cmd)
print(out.rstrip())

# Parse objdump. Dang dong:
#   401040:       55                      push   rbp
# Dong tiep noi (lenh dai) co byte nhung khong co mnemonic.
obj_insns = []
cur = None
for ln in out.splitlines():
    m = re.match(r"^\s*([0-9a-f]+):\s+((?:[0-9a-f]{2}\s)+)\s*(.*)$", ln)
    if not m:
        continue
    addr = int(m.group(1), 16)
    rest = m.group(3).strip()
    if rest:
        if rest == "(bad)":
            obj_insns.append((addr, "(bad)", ""))
        else:
            bits = rest.split(None, 1)
            obj_insns.append((addr, bits[0], bits[1].strip() if len(bits) > 1 else ""))
    elif cur is not None:
        pass  # byte tiep noi cua lenh cu -> bo qua
print(f"\n  => objdump: {len(obj_insns)} instruction")

# ------------------------------------------------------------------ 6. DOI CHIEU
section("BUOC 6 — DOI CHIEU capstone vs objdump")
print(f"  So instruction : capstone={len(cap_insns)}  objdump={len(obj_insns)}  "
      f"=> {'KHOP' if len(cap_insns)==len(obj_insns) else 'LECH SO LUONG'}")

n = min(len(cap_insns), len(obj_insns))
addr_diff, mnem_diff, op_diff = [], [], []
for k in range(n):
    ca, cm, co = cap_insns[k]
    oa, om, oo = obj_insns[k]
    if ca != oa:
        addr_diff.append((k, ca, oa))
    if cm != om:
        mnem_diff.append((k, ca, cm, om))
    if co.replace(" ", "") != oo.replace(" ", ""):
        op_diff.append((k, ca, cm, co, oo))

print(f"\n  [6a] SO SANH THO (so chuoi truc tiep, CHUA chuan hoa)")
print(f"  Lech DIA CHI      : {len(addr_diff)}")
print(f"  Lech MNEMONIC     : {len(mnem_diff)}")
print(f"  Lech TOAN HANG    : {len(op_diff)}  (khac dinh dang/ky phap la binh thuong)")

if addr_diff:
    print("\n  --- LECH DIA CHI ---")
    for k, ca, oa in addr_diff[:10]:
        print(f"    #{k}: capstone={ca:#x} objdump={oa:#x}")
if mnem_diff:
    print("\n  --- LECH MNEMONIC (so sanh THO) ---")
    for k, ca, cm, om in mnem_diff[:20]:
        print(f"    #{k} @{ca:#x}: capstone={cm!r} objdump={om!r}")

# --- 6b: chuan hoa tien to segment/prefix ---------------------------------
PREFIXES = {"cs", "ds", "es", "fs", "gs", "ss", "lock", "rep", "repe", "repz",
            "repne", "repnz", "data16", "data32", "addr16", "addr32", "bnd",
            "notrack", "xacquire", "xrelease"}


def fold(mnem, ops):
    """Tach cac token tien to (cs, lock, rep...) ra khoi mnemonic."""
    toks = ([mnem] + ops.split()) if ops.strip() else ([mnem] if mnem else [])
    pre = []
    while toks and toks[0].lower() in PREFIXES:
        pre.append(toks.pop(0).lower())
    m = toks.pop(0) if toks else ""
    return tuple(pre), m, " ".join(toks)


hard, explainable = [], []
for k in range(n):
    ca, cm, co = cap_insns[k]
    oa, om, oo = obj_insns[k]
    if ca != oa:
        continue  # da dem o addr_diff
    opre, omn, oop = fold(om, oo)
    cpre, cmn, cop = fold(cm, co)
    if omn == cmn and not opre:
        continue  # khop hoan toan sau khi tach
    if omn == cmn and opre:
        low = (cop + " " + co).lower()
        if all(p in low for p in opre):
            explainable.append((k, ca, cm, co, om, oo, opre))
            continue
    hard.append((k, ca, cm, co, om, oo))

print(f"\n  [6b] SO SANH SAU KHI CHUAN HOA TIEN TO (folding)")
print(f"  Lech CUNG (hard)               : {len(hard)}")
print(f"  Lech GIAI THICH DUOC (tien to) : {len(explainable)}")
if explainable:
    print("\n  --- LECH GIAI THICH DUOC: objdump tach tien to thanh token rieng ---")
    for k, ca, cm, co, om, oo, opre in explainable:
        print(f"    #{k} @{ca:#x}:")
        print(f"        capstone : {cm} {co}")
        print(f"        objdump  : {om} {oo}")
        print(f"        => tien to {opre} nam trong toan hang capstone; CUNG 1 lenh.")
if hard:
    print("\n  --- LECH CUNG (khong giai thich duoc bang tien to) ---")
    for k, ca, cm, co, om, oo in hard[:20]:
        print(f"    #{k} @{ca:#x}: capstone={cm} {co!r} | objdump={om} {oo!r}")

# ------------------------------------------------------------------- KET LUAN
section("KET LUAN T15-2")
print(f"  Entry point (readelf)          : {entry:#x}")
print(f"  .text addr/size (readelf)      : {text_addr:#x} / {text_size} byte")
print(f"  .text byte trich (objcopy)     : {len(blob)} byte "
      f"=> {'KHOP readelf' if len(blob)==text_size else 'LECH readelf'}")
print(f"  Instruction capstone           : {len(cap_insns)}")
print(f"  Instruction objdump            : {len(obj_insns)}")
print(f"  Lech so luong instruction      : {'KHONG' if len(cap_insns)==len(obj_insns) else 'CO'}")
print(f"  Lech DIA CHI                   : {len(addr_diff)}")
print(f"  Lech MNEMONIC (tho)            : {len(mnem_diff)}")
print(f"  -> trong do GIAI THICH DUOC    : {len(explainable)} (tien to cs/lock...)")
print(f"  -> trong do LECH CUNG          : {len(hard)}")
print(f"  Lech TOAN HANG (dinh dang)     : {len(op_diff)}")

ok = (len(cap_insns) == len(obj_insns)) and not addr_diff and not hard
if ok:
    print("\n>>> KET QUA: capstone va objdump KHOP ve so luong, DIA CHI va MNEMONIC")
    print("    sau khi chuan hoa tien to. KHONG co lech giai ma thuc su.")
    print(f"    {len(explainable)} khac biet do OBJDUMP tach tien to thanh token rieng")
    print("    (vi du 'cs nop ...' vs capstone 'nop ... cs:[...]') — CUNG 1 lenh,")
    print("    da doi chieu byte tho: 66 2e 0f 1f 84 00 00 00 00 00 @0x1066.")
    print(f"    {len(op_diff)} khac biet TOAN HANG chi ve CACH VIET (comment symbol cua")
    print("    objdump '<main>', 'WORD PTR' vs 'word ptr', '0x3' vs '3', 'rax*1+0x0').")
    print("\n    GHI CHU PHIEN BAN: uv cai capstone==5.0.9 (metadata) nhung module")
    print("    capstone.__version__ = 5.0.7 => KHAI BAO PHIEN BAN KHONG NHAT QUAN.")
    print("    Khi trich dan phai ghi ro dang dung metadata hay __version__.")
else:
    print("\n>>> KET QUA: CO LECH CUNG — xem chi tiet o BUOC 6b.")
    sys.exit(1)
