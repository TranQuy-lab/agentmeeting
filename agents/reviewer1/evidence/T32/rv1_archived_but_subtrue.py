#!/usr/bin/env python3
"""Reviewer1 — MO RONG: co ban ghi DA NGHI HUU nhung van eligible_for_submission=True khong?
Va chung co nam trong danh sach IN-SCOPE ma SCOPE.md §1 trich khong?"""
import json, urllib.request, subprocess, re
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125 Safari/537.36"
def gql(q):
    r=urllib.request.Request("https://hackerone.com/graphql",data=json.dumps({"query":q}).encode(),
      headers={"Content-Type":"application/json","Accept":"application/json","User-Agent":UA},method="POST")
    return json.loads(urllib.request.urlopen(r,timeout=60).read().decode())
Q='''query{team(handle:"gitlab"){structured_scopes(first:300){edges{node{
asset_identifier asset_type eligible_for_submission eligible_for_bounty max_severity archived_at}}}}}'''
sc=[e["node"] for e in gql(Q)["data"]["team"]["structured_scopes"]["edges"]]
a_sub=[s for s in sc if s.get("archived_at") and s["eligible_for_submission"]]
print(f"=== [1] Ban ghi DA NGHI HUU nhung eligible_for_submission=TRUE: {len(a_sub)} ===")
for s in sorted(a_sub,key=lambda x:str(x["archived_at"])):
    print(f"  {s['asset_identifier']:<56} type={s['asset_type']:<11} sev={str(s.get('max_severity')):<7} archived_at={s['archived_at']}")
print()
ids={s["asset_identifier"] for s in sc}
live_ids={s["asset_identifier"] for s in sc if not s.get("archived_at")}
print("=== [2] Trong so do, cai nao CON mot ban ghi DANG HIEU LUC cung identifier? ===")
for s in sorted(a_sub,key=lambda x:str(x["archived_at"])):
    i=s["asset_identifier"]
    print(f"  {i:<56} {'CO ban live (dual)' if i in live_ids else '❌ KHONG con ban live nao'}")
print()
print("=== [3] SCOPE.md §1 (IN-SCOPE nguyen van) @ ecce293 co liet ke chung khong? ===")
try:
    txt=subprocess.run(["git","show","ecce293:security/gitlab/SCOPE.md"],capture_output=True,text=True).stdout
except Exception as e:
    print("  (khong doc duoc)",e); raise SystemExit
m=re.search(r"## 1\. TRÍCH NGUYÊN VĂN — IN SCOPE.*?```text(.*?)```", txt, re.S)
sec1=m.group(1) if m else ""
for s in sorted(a_sub,key=lambda x:str(x["archived_at"])):
    i=s["asset_identifier"]
    hit = i in sec1
    print(f"  {'⚠️ CO trong §1' if hit else '   khong trong §1'}  {i}")
print()
print("  --- §1 co cot archived_at khong? ---")
print("   ", "CO" if "archived_at" in sec1 else "❌ KHONG co cot archived_at")
