#!/usr/bin/env python3
"""
T23 — CHUNG MINH C2 MOI BAT DUOC DUNG LOP LOI CUA T4 ("lop loi unicorn").

Boi canh: o T4, ket luan "thieu goi" duoc dua ra tu
    `pip list | grep -Ei '<danh sach viet tay>'`
ma KHONG `import` thu. Danh sach viet tay thi LUON thieu ten goi, va `grep`
thi LUON xac nhan cai nguoi viet da tin san => ket luan sai.

Script nay tai hien DUNG lop loi do tren mot goi THAT dang cai tren may,
roi cho thay C2(a)/(b) moi bat duoc sai khac.

KHONG mau doc hai. KHONG goi mang. Chi doc metadata + import.
"""
import importlib
import importlib.metadata as md
import subprocess
import sys
from pathlib import Path

VENV = "/home/noble-tran/forensicsmal-tooling/.venv"
PY = f"{VENV}/bin/python"
UV = "/home/noble-tran/.local/bin/uv"


def section(t):
    print("\n" + "=" * 70 + f"\n{t}\n" + "=" * 70)


# --------------------------------------------------- C2(a): KHONG LOC
section("C2(a) — Kiem ke KHONG LOC, luu NGUYEN output (khong grep, khong cat)")
cmd = [UV, "pip", "list", "--python", PY]
print(f"$ {' '.join(cmd)}")
r = subprocess.run(cmd, capture_output=True, text=True)
raw_list = r.stdout
print(raw_list.rstrip())
print(f"# => {len([l for l in raw_list.splitlines() if l.strip()]) - 2} goi. "
      f"Output NGUYEN VEN duoc luu vao EVIDENCE/ (khong loc dong nao).")

# Ghi ban tho ra file de lam bang chung
outdir = Path(__file__).resolve().parent.parent / "EVIDENCE"
outdir.mkdir(parents=True, exist_ok=True)
(outdir / "t23_unfiltered_inventory_raw.txt").write_text(
    "# RAW — uv pip list KHONG LOC (C2a)\n"
    f"# Interpreter: {PY}\n"
    f"# Lenh: {' '.join(cmd)}\n\n" + raw_list
)

# ------------------------------- TAI HIEN LOI: grep co NEO (anchored) => SAI
section("TAI HIEN LOI T4 — ket luan 'thieu' tu grep co neo, KHONG import thu")

# Danh sach VIET TAY, dung ten MODULE (day la cho de sai: ten goi != ten module)
HANDWRITTEN = ["pefile", "yara", "scapy", "capstone", "volatility3", "oletools",
               "msoffcrypto", "unicorn", "dissect", "pyelftools"]

print("# Gia dinh nguoi viet dung danh sach viet tay (ten MODULE) va grep co neo '^<ten> '")
print("# (neo dau dong + khoang trang => chi khop CHINH XAC ten do)")
print()
grep_verdict = {}
for name in HANDWRITTEN:
    g = subprocess.run(["grep", "-E", f"^{name} "], input=raw_list,
                       capture_output=True, text=True)
    found = bool(g.stdout.strip())
    grep_verdict[name] = found
    print(f"  grep '^{name} '  -> {'CO' if found else 'khong thay'}")

# ------------------------------- C2(b): import trong DUNG interpreter => THAT
section("C2(b) — Chay `import` trong DUNG interpreter dang xet => su that")
print(f"# Interpreter: {PY}")
print(f"# (bat buoc ghi ro interpreter — neu import o interpreter khac thi ket qua vo nghia)")
print()
import_verdict = {}
for name in HANDWRITTEN:
    code = f"import {name}"
    p = subprocess.run([PY, "-c", code], capture_output=True, text=True)
    ok = (p.returncode == 0)
    import_verdict[name] = ok
    err = p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ""
    print(f"  import {name:<14} -> {'THANH CONG' if ok else 'THAT BAI: ' + err}")

# --------------------------------------------------- SO SANH => TIM SAI KHAC
section("SO SANH — grep noi 'thieu' nhung import THANH CONG = KET LUAN SAI")
print(f"  {'goi/module':<16}{'grep co neo':>13}{'import':>10}   ket luan")
disagree = []
for name in HANDWRITTEN:
    g, i = grep_verdict[name], import_verdict[name]
    if g != i:
        verdict = "GREP SAI  <-- C2(a)/(b) BAT DUOC"
        disagree.append(name)
    else:
        verdict = "nhat quan"
    ga = "CO" if g else "thieu"
    ia = "OK" if i else "that bai"
    print(f"  {name:<16}{ga:>13}{ia:>10}   {verdict}")

print(f"\n  So ket luan SAI neu chi dung grep : {len(disagree)}  {disagree}")

# ------------------------------------------------------------------ KET LUAN
section("KET LUAN T23 — vi sao 3 o C2 moi la BAT BUOC")

if disagree:
    print(">>> TAI HIEN THANH CONG lop loi cua T4 tren goi THAT:")
    for name in disagree:
        # tim ten goi that su cung cap module nay
        pkg = None
        for dist in md.distributions():
            try:
                top = (dist.read_text("top_level.txt") or "").split()
            except Exception:
                top = []
            if name in top or name.replace("_", "-") in (dist.metadata["Name"] or "").lower():
                pkg = dist.metadata["Name"]
                break
        print(f"    - module `{name}`: grep co neo KHONG thay, nhung `import` THANH CONG"
              + (f" (goi that: `{pkg}`)" if pkg else ""))
    print()
    print("    Nguyen nhan: TEN GOI KHAC TEN MODULE. `pip list` liet ke TEN GOI")
    print("    (`yara-python`, `msoffcrypto-tool`), con `import` dung TEN MODULE")
    print("    (`yara`, `msoffcrypto`). Grep theo ten module se KHONG thay => ket luan")
    print("    'thieu' SAI.")
    print()
    print("    => C2(a) buoc phai luu inventory KHONG LOC (de khong tu tao diem mu).")
    print("    => C2(b) buoc phai `import` trong DUNG interpreter (de do su that).")
    print("    => Chi khi CA HAI duoc lam thi moi khong lap lai lop loi nay.")
    print()
    print("    !! GIOI HAN KHANG DINH: day la MOT co che THAT cua lop loi 'loc tay'")
    print("       va toi TAI HIEN duoc no. Toi KHONG khang dinh day la co che cu the")
    print("       da lam T4 ket luan sai ve `unicorn` — toi CHUA doc ban goc T4.")
else:
    print(">>> Khong tim thay sai khac tren may nay (moi truong hop deu nhat quan).")
    print("    => KHONG ket luan duoc rang C2 moi bat duoc loi — ghi 'chua xac minh'.")

print()
print("## CHUA XAC MINH")
print("  - chua xac minh: ban than script nay co bat duoc MOI lop loi loc tay khac khong;")
print("    no chi tai hien DUOC MOT co che (ten goi != ten module) da kiem chung.")
print("  - chua xac minh: chi tiet goc ve 'unicorn' o T4 — toi chua doc ban goc T4,")
print("    chi biet qua D-014/D-020. Khong suy dien them.")
