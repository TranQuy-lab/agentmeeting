#!/usr/bin/env python3
"""Reviewer1 — kiem DOC LAP cau hoi: 41 lech TOAN HANG giua capstone va objdump
co cai nao THUC SU NGU NGHIA khong, hay chi la cach viet?

Phuong phap: chuan hoa MANH hon tac gia (bo comment symbol, bo 'ptr', gop hex/thap phan,
bo khoang trang, ha chu thuong) roi so LAI. Bat ky dong nao con khac => NGHI NGU NGHIA.
"""
import re, shutil, subprocess, sys
from pathlib import Path
from capstone import CS_ARCH_X86, CS_MODE_64, Cs

W = Path("/tmp/rv1-operand"); W.mkdir(exist_ok=True)
SRC = W/"b.c"; BIN = W/"b"; TB = W/"b.text.bin"
SRC.write_text(
 "int add(int a,int b){return a+b;}\n"
 "long loop_sum(long n){long s=0;for(long i=0;i<n;i++)s+=i;return s;}\n"
 "int classify(int x){if(x<0)return -1;if(x==0)return 0;return 1;}\n"
 "int main(void){return classify(add(1,2))+(int)loop_sum(10);}\n")
gcc=shutil.which("gcc")
r=subprocess.run([gcc,"-O1","-fno-asynchronous-unwind-tables","-fno-stack-protector",
                  "-no-pie","-o",str(BIN),str(SRC)],capture_output=True,text=True)
print("gcc rc:",r.returncode, r.stderr.strip()[:200])
subprocess.run(["objcopy","-O","binary","--only-section=.text",str(BIN),str(TB)],check=True)
blob=TB.read_bytes()
# doc entry + .text addr
h=subprocess.run(["readelf","-h",str(BIN)],capture_output=True,text=True).stdout
entry=int(re.search(r"Entry point address:\s+0x([0-9a-f]+)",h).group(1),16)
s=subprocess.run(["readelf","-S","-W",str(BIN)],capture_output=True,text=True).stdout
m=re.search(r"\.text\s+\w+\s+([0-9a-f]+)\s+([0-9a-f]+)\s+([0-9a-f]+)",s)
text_addr=int(m.group(1),16); text_size=int(m.group(2),16)
print(f"entry=0x{entry:x} .text=0x{text_addr:x} size={text_size} blob={len(blob)}")

md=Cs(CS_ARCH_X86,CS_MODE_64)
cap={i.address:(i.mnemonic, i.op_str) for i in md.disasm(blob, text_addr)}
od=subprocess.run(["objdump","-d","-M","intel","--section=.text",str(BIN)],
                  capture_output=True,text=True).stdout
obj={}
for ln in od.splitlines():
    mm=re.match(r"\s*([0-9a-f]+):\s+(?:[0-9a-f]{2}\s+)+\s*([a-z][a-z0-9.]*)\s*(.*)$", ln)
    if mm:
        obj[int(mm.group(1),16)]=(mm.group(2), mm.group(3).strip())
print("capstone:",len(cap)," objdump:",len(obj))
assert set(cap)==set(obj), "tap dia chi khac nhau!"

def norm(mn, ops):
    s=ops.lower()
    s=re.sub(r"#.*$","",s)                 # bo comment symbol cua objdump
    s=re.sub(r"<[^>]*>","",s)              # bo <main>
    s=re.sub(r"\b(ptr|byte|xmmword|dword|qword|word)\b","",s)
    s=re.sub(r"0x([0-9a-f]+)",lambda m:str(int(m.group(1),16)),s)  # hex -> dec
    s=re.sub(r"\s+","",s)
    s=s.replace("+0]","]").replace("-0]","]").replace("*1+","+").replace("*1]","]")
    return mn.lower(), s

raw_diff=[]; sem_diff=[]
for a in sorted(cap):
    cm,co=cap[a]; om,oo=obj[a]
    if (cm,co)!=(om,oo): raw_diff.append(a)
    if norm(cm,co)!=norm(om,oo): sem_diff.append((a,cm,co,om,oo,norm(cm,co),norm(om,oo)))
print(f"\nLECH THO (raw)        : {len(raw_diff)}")
print(f"LECH SAU CHUAN HOA MANH: {len(sem_diff)}  <-- con lai moi la NGHI NGU NGHIA")
for a,cm,co,om,oo,nc,no in sem_diff:
    print(f"  @0x{a:x}")
    print(f"     capstone: {cm} {co}   -> norm: {nc!r}")
    print(f"     objdump : {om} {oo}   -> norm: {no!r}")
print("\n--- 41 lech tho: liet ke toan bo mnemonic+operand 2 ben ---")
for a in raw_diff:
    cm,co=cap[a]; om,oo=obj[a]
    print(f"  @0x{a:x} | cap={cm} {co!r} | obj={om} {oo!r}")
