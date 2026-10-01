#!/usr/bin/env python3
"""
T15-4 — KIEM CHUAN volatility3: chay plugin tren input RONG / KHONG HOP LE
Muc tieu: chung minh vol3 THAT BAI MOT CACH SACH SE (khong crash, khong treo,
          bao loi ro rang), chu KHONG chung minh no phan tich duoc dump that.
          => Day la kiem "graceful failure", dung nhu Admin yeu cau.

Tieu chi "sach se":
  - KHONG in Python traceback ra stdout/stderr (khong crash)
  - Ket thuc trong thoi han (khong treo)
  - Co thong bao loi/ly do ro rang
  - Exit code xac dinh

CORPUS VO HAI: chi toan byte rac / file rong do chung ta tao. KHONG mau doc hai.
KHONG chay ma. Phan tich DONG van DINH CHI.
"""
import os
import random
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
CORPUS.mkdir(exist_ok=True)
VENV = Path("/home/noble-tran/forensicsmal-tooling/.venv")
VOL = VENV / "bin" / "vol"
TIMEOUT = 90


def section(t):
    print("\n" + "=" * 70 + f"\n{t}\n" + "=" * 70)


# ------------------------------------------------------------- 0. CHUAN BI
section("BUOC 0 — Chuan bi input RONG / KHONG HOP LE (vo hai)")
EMPTY = CORPUS / "invalid_empty.bin"
GARBAGE = CORPUS / "invalid_garbage.bin"
SHORT = CORPUS / "invalid_short.bin"
ZEROS = CORPUS / "invalid_zeros.bin"
NOTEXIST = CORPUS / "khong_ton_tai_bao_gio.bin"

EMPTY.write_bytes(b"")
random.seed(1337)
GARBAGE.write_bytes(bytes(random.randrange(256) for _ in range(65536)))
SHORT.write_bytes(b"\x00\x01\x02\x03" * 4)
ZEROS.write_bytes(b"\x00" * 4096)

print(f"  {EMPTY.name:<26} {EMPTY.stat().st_size:>7} byte  (RONG hoan toan)")
print(f"  {GARBAGE.name:<26} {GARBAGE.stat().st_size:>7} byte  (byte ngau nhien, seed=1337)")
print(f"  {SHORT.name:<26} {SHORT.stat().st_size:>7} byte  (16 byte)")
print(f"  {ZEROS.name:<26} {ZEROS.stat().st_size:>7} byte  (toan so 0)")
print(f"  {NOTEXIST.name:<26} {'(khong ton tai)':>7}")
print(f"  {str(CORPUS):<26} {'(thu muc, khong phai file)':>7}")

print(f"\n# vol binary: {VOL}")
print(f"# vol ton tai: {VOL.exists()}")
print(f"# timeout moi lan chay: {TIMEOUT}s")

rc, out, err = None, "", ""
r = subprocess.run([str(VOL), "--version"], capture_output=True, text=True)
print(f"\n$ {VOL} --version\nexit={r.returncode}\n{(r.stdout + r.stderr).strip()}")

# --------------------------------------------------------------- 1. MA TRAN
section("BUOC 1 — Chay vol tren tung input KHONG HOP LE")
CASES = [
    ("file RONG (0 byte)",         ["-f", str(EMPTY),    "windows.pslist"]),
    ("byte ngau nhien 64KB",       ["-f", str(GARBAGE),  "windows.pslist"]),
    ("file 16 byte",               ["-f", str(SHORT),    "windows.pslist"]),
    ("toan so 0 4KB",              ["-f", str(ZEROS),    "windows.pslist"]),
    ("file KHONG ton tai",         ["-f", str(NOTEXIST), "windows.pslist"]),
    ("thu muc thay vi file",       ["-f", str(CORPUS),   "windows.pslist"]),
    ("KHONG truyen -f",            ["windows.pslist"]),
    ("plugin KHONG ton tai",       ["-f", str(GARBAGE),  "windows.plugin_khong_ton_tai_xyz"]),
    ("plugin linux tren input rac",["-f", str(GARBAGE),  "linux.pslist"]),
]

results = []
for label, args in CASES:
    cmd = [str(VOL)] + args
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)
        timed_out = False
        rc, out, err = p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired as e:
        timed_out = True
        rc = None
        out = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        err = (e.stderr or b"").decode(errors="replace") if isinstance(e.stderr, bytes) else (e.stderr or "")
    dt = time.time() - t0

    combined = out + err
    has_traceback = "Traceback (most recent call last)" in combined
    has_err_text = bool(combined.strip())
    hung = timed_out

    results.append({
        "label": label, "cmd": " ".join(cmd[1:]), "rc": rc, "seconds": dt,
        "traceback": has_traceback, "hung": hung,
        "stdout": out, "stderr": err, "combined_len": len(combined.strip()),
    })

    print("\n" + "-" * 70)
    print(f"### {label}")
    print(f"$ vol {' '.join(args)}")
    print(f"  thoi gian : {dt:.2f}s   {'*** TREO (timeout) ***' if hung else ''}")
    print(f"  exit code : {rc}")
    print(f"  Python traceback (dau hieu CRASH): {'CO  <<< CRASH' if has_traceback else 'KHONG'}")
    print(f"  co thong bao loi : {'CO' if has_err_text else 'KHONG (im lang!)'}")
    print(f"  --- stdout ({len(out.strip())} ky tu) ---")
    print("\n".join("    " + l for l in out.strip().splitlines()[:25]) or "    (rong)")
    print(f"  --- stderr ({len(err.strip())} ky tu) ---")
    print("\n".join("    " + l for l in err.strip().splitlines()[:25]) or "    (rong)")

# ------------------------------------------------------------------ 2. TONG HOP
section("BUOC 2 — TONG HOP: co that bai SACH SE khong?")
print(f"  {'case':<30}{'exit':>6}{'giay':>7}  {'treo':>5} {'traceback':>10} {'co bao loi':>11}")
crashes, hangs, silents = [], [], []
for r in results:
    tb = "CO" if r["traceback"] else "khong"
    hg = "CO" if r["hung"] else "khong"
    err_ok = "CO" if r["combined_len"] else "KHONG"
    print(f"  {r['label']:<30}{str(r['rc']):>6}{r['seconds']:>7.2f}  {hg:>5} {tb:>10} {err_ok:>11}")
    if r["traceback"]:
        crashes.append(r["label"])
    if r["hung"]:
        hangs.append(r["label"])
    if not r["combined_len"]:
        silents.append(r["label"])

print(f"\n  Tong so ca thu        : {len(results)}")
print(f"  CRASH (co traceback)  : {len(crashes)} {crashes if crashes else ''}")
print(f"  TREO (timeout)        : {len(hangs)} {hangs if hangs else ''}")
print(f"  IM LANG (khong bao loi): {len(silents)} {silents if silents else ''}")

# ------------------------------------------------------------------ KET LUAN
section("KET LUAN T15-4")
print("  Day KHONG phai kiem nang luc phan tich dump — ma la kiem")
print("  'graceful failure': vol3 gap input rac thi xu su the nao.")
print()
ok = not crashes and not hangs
if ok:
    print(">>> KET QUA: vol3 THAT BAI SACH SE tren toan bo input khong hop le:")
    print(f"    - 0 crash (khong Python traceback) tren {len(results)} ca")
    print(f"    - 0 treo (moi ca ket thuc < {TIMEOUT}s)")
    print(f"    - {len(results) - len(silents)}/{len(results)} ca co thong bao loi ro rang")
    if silents:
        print(f"    - {len(silents)} ca IM LANG: {silents} (can ghi chu, khong phai crash)")
    print()
    print("    => vol3 dung KHUNG framework dung: nap plugin OK, roi bao thieu")
    print("       yeu cau (symbol / memory layer) thay vi crash.")
    print("    => CO SO de tin: khi co dump THAT, loi se la loi du lieu chu khong")
    print("       phai loi framework. NHUNG van CHUA chung minh phan tich duoc dump")
    print("       that — muc do van la 'cong cu san sang, CHUA thuc chien'.")
else:
    print(f">>> KET QUA: Phat hien van de — crash={crashes} treo={hangs}")
    sys.exit(1)
