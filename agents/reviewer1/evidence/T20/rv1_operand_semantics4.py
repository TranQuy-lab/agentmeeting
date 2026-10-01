#!/usr/bin/env python3
"""Reviewer1 — PHIEN BAN 4 (sua tiep loi ban 3).
Loi ban 3: objdump in dich nhanh o dang HEX TRAN ('1070'), toi lai parse thanh THAP PHAN.
Ban 4: truyen co 'nguon' (capstone vs objdump) de parse dich cho dung quy uoc."""
import re, subprocess
from pathlib import Path
from collections import Counter
from capstone import CS_ARCH_X86, CS_MODE_64, Cs

W=Path("/tmp/rv1-operand4"); W.mkdir(exist_ok=True)
SRC=W/"bench_elf.c"
SRC.write_text(
 "/* Corpus vo hai do ForensicsMal tu viet cho T15-2. Chi de disassemble TINH. */\n"
 "int add(int a, int b) { return a + b; }\n"
 "long loop_sum(long n) {\n    long s = 0;\n    for (long i = 0; i < n; i++) s += i;\n    return s;\n}\n"
 "int classify(int x) {\n    if (x < 0) return -1;\n    if (x == 0) return 0;\n    return 1;\n}\n"
 "int main(void) { return classify(add(1, 2)) + (int)loop_sum(10); }\n")
BIN=W/"bench_elf"; TB=W/"bench_elf.text.bin"
subprocess.run(["gcc","-O1","-fno-asynchronous-unwind-tables","-fno-stack-protector","-o",str(BIN),str(SRC)],
               check=True,capture_output=True)
subprocess.run(["objcopy","-O","binary","--only-section=.text",str(BIN),str(TB)],check=True)
blob=TB.read_bytes()
h=subprocess.run(["readelf","-h",str(BIN)],capture_output=True,text=True).stdout
entry=int(re.search(r"Entry point address:\s+0x([0-9a-f]+)",h).group(1),16)
s=subprocess.run(["readelf","-S","-W",str(BIN)],capture_output=True,text=True).stdout
text_addr=int(re.search(r"\.text\s+\w+\s+([0-9a-f]+)",s).group(1),16)
print(f"entry=0x{entry:x} .text=0x{text_addr:x} blob={len(blob)} (DUNG co gcc tac gia)")
md=Cs(CS_ARCH_X86,CS_MODE_64)
cap=[(i.address,i.mnemonic,i.op_str) for i in md.disasm(blob,text_addr)]
od=subprocess.run(["objdump","-d","-M","intel","--section=.text",str(BIN)],capture_output=True,text=True).stdout
obj=[]
for ln in od.splitlines():
    mm=re.match(r"^\s*([0-9a-f]+):\s+((?:[0-9a-f]{2}\s)+)\s*(.*)$",ln)
    if not mm: continue
    rest=mm.group(3).strip()
    if rest:
        b=rest.split(None,1); obj.append((int(mm.group(1),16),b[0],b[1].strip() if len(b)>1 else ""))
print(f"capstone={len(cap)} objdump={len(obj)}")
print(f"[THO - dung quy tac tac gia] mnemonic={sum(1 for k in range(min(len(cap),len(obj))) if cap[k][1]!=obj[k][1])}"
      f" | toan hang={sum(1 for k in range(min(len(cap),len(obj))) if cap[k][2].replace(' ','')!=obj[k][2].replace(' ',''))}\n")
BRANCH=re.compile(r"^(j|call|loop)",re.I)
def norm(mnem,ops,src):
    s=ops.lower()
    s=re.sub(r"#.*$","",s); s=re.sub(r"<[^>]*>","",s)
    s=re.sub(r"\b(ptr|byte|word|dword|qword|xmmword|ymmword)\b","",s)
    s=re.sub(r"0x[0-9a-f]+",lambda m:str(int(m.group(0),16)),s)
    toks=s.split()
    if BRANCH.match(mnem) and len(toks)==1:
        t=toks[0]
        if re.fullmatch(r"0x[0-9a-f]+",t): s=str(int(t,16))
        elif re.fullmatch(r"[0-9a-f]+",t):
            # objdump in dich dang HEX TRAN; capstone in THAP PHAN
            s=str(int(t,16)) if src=="obj" else str(int(t,10))
    s=re.sub(r"\s+","",s)
    s=re.sub(r"\+0x0\]","]",s); s=re.sub(r"\+0\]","]",s)
    s=s.replace("*1]","]").replace("*1+","+")
    return s
rows=[]
for k in range(min(len(cap),len(obj))):
    ca,cm,co=cap[k]; oa,om,oo=obj[k]
    if (cm.lower(),co.replace(" ",""))==(om.lower(),oo.replace(" ","")): continue
    nc,no=norm(cm,co,"cap"),norm(om,oo,"obj")
    ncm,nom=cm.lower(),om.lower()
    if nc==no and ncm==nom: tag="CACH VIET (hex/dec, comment symbol, 'ptr' hoa/thuong)"
    elif ncm!=nom and (nc==no or re.sub(r"^(cs|data16)","",nc)==re.sub(r"^(cs|data16)","",no)): tag="TIEN TO/ALIAS — objdump tach token (cs/data16/xchg ax,ax)"
    elif nc==no: tag="CACH VIET"
    else: tag="KHAC NGU NGHIA THAT SU"
    rows.append((ca,cm,co,om,oo,nc,no,tag))
c=Counter(r[7] for r in rows)
print(f"=== TONG {len(rows)} dong con khac SAU CHUAN HOA (da tinh ca alias/tien to) ===")
for a,cm,co,om,oo,nc,no,tag in rows:
    print(f"  @0x{a:x} [{tag}]")
    print(f"      cap={cm} {co!r} -> {nc!r}")
    print(f"      obj={om} {oo!r} -> {no!r}")
print("\n=== TONG THEO NHOM ===")
for k,v in sorted(c.items(),key=lambda x:-x[1]): print(f"  {v:3}  {k}")
bad=c.get("KHAC NGU NGHIA THAT SU",0)
print("\n=== KET LUAN ===")
print("  ✅ KHONG co lech toan hang NGU NGHIA — moi khac biet la CACH VIET hoac TEN GOI." if bad==0
      else f"  ❌ {bad} dong con khac sau chuan hoa — PHAI xem tay.")
print("  => Khang dinh '41 lech toan hang thuan cach viet' cua ForensicsMal:",
      "DUNG ✅" if bad==0 else "SAI ❌")
