#!/usr/bin/env python3
"""Reviewer1 — tai lap phep bam vung theo CA HAI quy uoc ranh gioi (A: khong \\n cuoi, B: co \\n cuoi)."""
import subprocess, hashlib, difflib
MB="6d47749"; HEAD="ecce293"
def show(rev,f): return subprocess.run(["git","show",f"{rev}:{f}"],capture_output=True,text=True).stdout
def h(s): return hashlib.sha256(s.encode()).hexdigest()[:8]
def regions(old,new):
    ol=old.splitlines(); nl=new.splitlines()
    sm=difflib.SequenceMatcher(None,ol,nl,autojunk=False)
    changed=set()
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag!="equal":
            for k in range(i1,i2): changed.add(k)
    # vung KHONG DOI = cac doan dong lien tiep khong nam trong 'changed'
    out=[];start=None
    for k in range(len(ol)):
        if k not in changed:
            if start is None: start=k
        else:
            if start is not None: out.append((start+1,k)); start=None
    if start is not None: out.append((start+1,len(ol)))
    res=[]
    for a,b in out:
        A="\n".join(ol[a-1:b])          # quy uoc A: KHONG \n cuoi
        B=A+"\n"                         # quy uoc B: CO \n cuoi
        res.append((a,b,h(A),h(B),A))
    return res
for f in ("security/gitlab/RECON.md","agents/bountyrecon/tasks/T3/CANDIDATES.md"):
    o=show(MB,f); n=show(HEAD,f)
    print(f"=== {f} ===")
    print(f"  blob {subprocess.run(['git','rev-parse',f'{MB}:{f}'],capture_output=True,text=True).stdout.strip()[:8]}"
          f" -> {subprocess.run(['git','rev-parse',f'{HEAD}:{f}'],capture_output=True,text=True).stdout.strip()[:8]}"
          f"  | dong {len(o.splitlines())} -> {len(n.splitlines())}")
    for i,(a,b,ha,hb,txt) in enumerate(regions(o,n)):
        empty = " (chuoi RONG)" if txt=="" else ""
        print(f"    V{i} dong {a}..{b}   A={ha}  B={hb}{empty}")
    print()
