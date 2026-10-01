#!/usr/bin/env python3
"""Reviewer1 — PHIEN BAN 3 (da sua loi chuan hoa cua chinh toi o ban 2).
Loi ban 2: objdump in dich cua jmp/call KHONG co tien to '0x' (vd 'je 1098'),
nen regex '0x...' khong doi duoc -> bao OAN 16 dong la 'khac ngu nghia'.
Ban 3: voi lenh NHANH/GỌI, chuan hoa dich ve so nguyen (ca hai dang)."""
import re, subprocess
from pathlib import Path
from capstone import CS_ARCH_X86, CS_MODE_64, Cs

W=Path("/tmp/rv1-operand3"); W.mkdir(exist_ok=True)
SRC=W/"bench_elf.c"
SRC.write_text(
 "/* Corpus vo hai do ForensicsMal tu viet cho T15-2. Chi de disassemble TINH. */\n"
 "int add(int a, int b) { return a + b; }\n"
 "long loop_sum(long n) {\n    long s = 0;\n    for (long i = 0; i < n; i++) s += i;\n    return s;\n}\n"
 "int classify(int x) {\n    if (x < 0) return -1;\n    if (x == 0) return 0;\n    return 1;\n}\n"
 "int main(void) { return classify(add(1, 2)) + (int)loop_sum(10); }\n")
BIN=W/"bench_elf"; TB=W/"bench_elf.text.bin"
cmd=["gcc","-O1","-fno-asynchronous-unwind-tables","-fno-stack-protector","-o",str(BIN),str(SRC)]
subprocess.run(cmd,check=True,capture_output=True)
subprocess.run(["objcopy","-O","binary","--only-section=.text",str(BIN),str(TB)],check=True)
blob=TB.read_bytes()
h=subprocess.run(["readelf","-h",str(BIN)],capture_output=True,text=True).stdout
entry=int(re.search(r"Entry point address:\s+0x([0-9a-f]+)",h).group(1),16)
s=subprocess.run(["readelf","-S","-W",str(BIN)],capture_output=True,text=True).stdout
m=re.search(r"\.text\s+\w+\s+([0-9a-f]+)\s+([0-9a-f]+)",s)
text_addr=int(m.group(1),16)
print(f"entry=0x{entry:x} .text=0x{text_addr:x} blob={len(blob)}  (DUNG co gcc cua tac gia)")
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
raw_op=sum(1 for k in range(min(len(cap),len(obj))) if cap[k][2].replace(" ","")!=obj[k][2].replace(" ",""))
raw_mn=sum(1 for k in range(min(len(cap),len(obj))) if cap[k][1]!=obj[k][1])
print(f"[THO - dung quy tac tac gia] mnemonic={raw_mn} | toan hang={raw_op}\n")

BRANCH=re.compile(r"^(j|call|loop)",re.I)
def val(x):
    x=x.lower()
    if re.fullmatch(r"0x[0-9a-f]+",x): return int(x,16)
    if re.fullmatch(r"[0-9]+",x):      return int(x)        # capstone in thap phan
    return None
def norm(mnem,ops):
    s=ops.lower()
    s=re.sub(r"#.*$","",s); s=re.sub(r"<[^>]*>","",s)
    s=re.sub(r"\b(ptr|byte|word|dword|qword|xmmword|ymmword)\b","",s)
    s=re.sub(r"0x[0-9a-f]+",lambda m:str(int(m.group(0),16)),s)
    if BRANCH.match(mnem):                                  # <-- FIX: dich nhanh/gọi
        toks=s.split()
        if len(toks)==1:
            v=val(toks[0])
            if v is None and re.fullmatch(r"[0-9a-f]+",toks[0]): v=int(toks[0],16)
            if v is not None: s=str(v)
    s=re.sub(r"\s+","",s)
    s=re.sub(r"\+0x0\]","]",s); s=re.sub(r"\+0\]","]",s)
    s=s.replace("*1]","]").replace("*1+","+")
    return s

rows=[]
for k in range(min(len(cap),len(obj))):
    ca,cm,co=cap[k]; oa,om,oo=obj[k]
    if (cm.lower(),co.replace(" ",""))==(om.lower(),oo.replace(" ","")): continue
    nc,no=norm(cm,co),norm(om,oo)
    ncm,nom=cm.lower(),om.lower()
    # goi y phan loai
    if nc==no and ncm==nom: tag="CACH VIET (hex/thap phan, comment symbol, 'ptr')"
    elif nc.replace("cs:","").replace("cs","")==no.replace("cs:","").replace("cs","").replace("*1",""): tag="TIEN TO bi tach token (cs/data16) — CUNG 1 lenh"
    elif ncm!=nom and nc==no: tag="ALIAS cung ma lenh (nop/xchg ax,ax)"
    elif re.sub(r"[+]0$|[+]0\]","]",nc)==re.sub(r"[+]0$|[+]0\]","]",no): tag="TOAN HANG AN (+0, *1)"
    else: tag="KHAC NGU NGHIA THAT SU"
    rows.append((ca,cm,co,om,oo,nc,no,tag))
from collections import Counter
c=Counter(r[7] for r in rows)
print("=== PHAN LOAI %d DONG CON KHAC SAU CHUAN HOA ==="%len(rows))
for a,cm,co,om,oo,nc,no,tag in rows:
    print(f"  @0x{a:x} [{tag}]")
    print(f"      cap={cm} {co!r} -> {nc!r}")
    print(f"      obj={om} {oo!r} -> {no!r}")
print("\n=== TONG ===")
for k,v in sorted(c.items(),key=lambda x:-x[1]): print(f"  {v:3}  {k}")
bad=c.get("KHAC NGU NGHIA THAT SU",0)
print("\n=== KET LUAN ===")
print("  ✅ KHONG co lech toan hang NGU NGHIA." if bad==0 else f"  ❌ {bad} dong NGHI NGU NGHIA — can xem tay.")
print("  => Khang dinh '41 lech toan hang thuan cach viet' cua tac gia:",
      "DUNG" if bad==0 else "SAI")
