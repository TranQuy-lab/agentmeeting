#!/usr/bin/env python3
"""Reviewer1 — PHIEN BAN 2: dung DUNG co gcc cua tac gia de co CUNG binary.
Cau hoi: 41 lech toan hang co cai nao NGU NGHIA khong?"""
import re, shutil, subprocess
from pathlib import Path
from capstone import CS_ARCH_X86, CS_MODE_64, Cs

W = Path("/tmp/rv1-operand2"); W.mkdir(exist_ok=True)
SRC = W/"bench_elf.c"
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
 "int main(void) { return classify(add(1, 2)) + (int)loop_sum(10); }\n")
BIN=W/"bench_elf"; TB=W/"bench_elf.text.bin"
# ==== DUNG DUNG CO CUA TAC GIA (khong them -no-pie) ====
cmd=["gcc","-O1","-fno-asynchronous-unwind-tables","-fno-stack-protector","-o",str(BIN),str(SRC)]
r=subprocess.run(cmd,capture_output=True,text=True)
print("$"," ".join(cmd)); print("exit=",r.returncode, r.stderr.strip()[:200])
subprocess.run(["objcopy","-O","binary","--only-section=.text",str(BIN),str(TB)],check=True)
blob=TB.read_bytes()
h=subprocess.run(["readelf","-h",str(BIN)],capture_output=True,text=True).stdout
entry=int(re.search(r"Entry point address:\s+0x([0-9a-f]+)",h).group(1),16)
s=subprocess.run(["readelf","-S","-W",str(BIN)],capture_output=True,text=True).stdout
m=re.search(r"\.text\s+\w+\s+([0-9a-f]+)\s+([0-9a-f]+)",s)
text_addr=int(m.group(1),16); text_size=int(m.group(2),16)
print(f"entry=0x{entry:x} | .text=0x{text_addr:x} size={text_size} | blob={len(blob)} byte")

md=Cs(CS_ARCH_X86,CS_MODE_64)
cap=[(i.address,i.mnemonic,i.op_str) for i in md.disasm(blob,text_addr)]
od=subprocess.run(["objdump","-d","-M","intel","--section=.text",str(BIN)],capture_output=True,text=True).stdout
obj=[]
for ln in od.splitlines():
    mm=re.match(r"^\s*([0-9a-f]+):\s+((?:[0-9a-f]{2}\s)+)\s*(.*)$", ln)
    if not mm: continue
    rest=mm.group(3).strip()
    if rest:
        bits=rest.split(None,1)
        obj.append((int(mm.group(1),16), bits[0], bits[1].strip() if len(bits)>1 else ""))
print(f"capstone={len(cap)} objdump={len(obj)}")

# --- dem THO theo DUNG quy tac tac gia: co.replace(' ','') != oo.replace(' ','')
raw_op=sum(1 for k in range(min(len(cap),len(obj)))
           if cap[k][2].replace(" ","")!=obj[k][2].replace(" ",""))
raw_mn=sum(1 for k in range(min(len(cap),len(obj))) if cap[k][1]!=obj[k][1])
raw_ad=sum(1 for k in range(min(len(cap),len(obj))) if cap[k][0]!=obj[k][0])
print(f"\n[THO - dung quy tac tac gia] dia chi={raw_ad} | mnemonic={raw_mn} | toan hang={raw_op}")

def norm_ops(s):
    s=s.lower()
    s=re.sub(r"#.*$","",s)                      # bo comment symbol
    s=re.sub(r"<[^>]*>","",s)                   # bo <main>
    s=re.sub(r"\b(ptr|byte|word|dword|qword|xmmword|ymmword)\b","",s)
    def toi(mm):
        return str(int(mm.group(0),16))
    s=re.sub(r"0x[0-9a-f]+",toi,s)              # hex co 0x -> dec
    s=re.sub(r"\s+","",s)
    s=re.sub(r"\+0\]","]",s); s=re.sub(r"\+0x0\]","]",s)
    s=s.replace("*1]","]").replace("*1+","+")
    return s

# --- phan loai SAU khi chuan hoa manh
res=[]
for k in range(min(len(cap),len(obj))):
    ca,cm,co=cap[k]; oa,om,oo=obj[k]
    ncm,nom=cm.lower(),om.lower()
    if (ncm,co.replace(" ",""))==(nom,oo.replace(" ","")): continue
    res.append((ca,cm,co,om,oo,norm_ops(co),norm_ops(oo)))
print(f"\n[Sau chuan hoa manh] con lai {len(res)} dong khac:")
buckets={"hex/dec+comment (cach viet)":0,"tien to (data16/cs)":0,"alias cung ma lenh":0,
         "toan hang an (*1, +0)":0,"KHAC NGU NGHIA THAT SU":0}
for ca,cm,co,om,oo,nc,no in res:
    if nc==no and cm.lower()==om.lower(): tag="hex/dec+comment (cach viet)"
    elif nc==no: tag="alias cung ma lenh"
    elif nc.replace("cs:","")==no.replace("cs","").replace("[","[") and "cs" in (nc+no): tag="tien to (data16/cs)"
    elif re.sub(r"[*+ ]1|\+0","",nc)==re.sub(r"[*+ ]1|\+0","",no): tag="toan hang an (*1, +0)"
    else: tag="KHAC NGU NGHIA THAT SU"
    buckets[tag]+=1
    print(f"  @0x{ca:x} [{tag}]")
    print(f"      cap: {cm} {co!r} -> {nc!r}")
    print(f"      obj: {om} {oo!r} -> {no!r}")
print("\n=== TONG KET PHAN LOAI ===")
for k,v in buckets.items(): print(f"  {v:3}  {k}")
print("\n=== KET LUAN ===")
if buckets["KHAC NGU NGHIA THAT SU"]==0:
    print("  ✅ KHONG co lech toan hang nao NGU NGHIA. Moi khac biet deu la CACH VIET /")
    print("     TEN GOI CUA CUNG MA LENH / TIEN TO BI TACH TOKEN. Khang dinh cua tac gia DUNG.")
else:
    print("  ❌ CO lech NGU NGHIA THAT SU -> khang dinh cua tac gia SAI o muc nay.")
