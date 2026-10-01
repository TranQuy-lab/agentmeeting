#!/usr/bin/env python3
"""Reviewer1 — tai lap DOC LAP phat hien archived_at cua T28 (khong dung script/JSON cua BountyRecon)."""
import json, urllib.request
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125 Safari/537.36"
def gql(q):
    r=urllib.request.Request("https://hackerone.com/graphql",data=json.dumps({"query":q}).encode(),
      headers={"Content-Type":"application/json","Accept":"application/json","User-Agent":UA},method="POST")
    return json.loads(urllib.request.urlopen(r,timeout=60).read().decode())

print("=== [1] SCHEMA: truong 'archived_at' co trong StructuredScope khong? ===")
d=gql('{__type(name:"StructuredScope"){fields{name}}}')
f=[x["name"] for x in d["data"]["__type"]["fields"]]
print("  tong truong:", len(f))
print("  archived_at co trong schema?", "✅ CO" if "archived_at" in f else "❌ KHONG")
for k in ("asset_identifier","asset_type","eligible_for_submission","eligible_for_bounty","max_severity","archived_at"):
    print(f"    - {k}: {'✅' if k in f else '❌'}")

Q='''query{team(handle:"gitlab"){structured_scopes(first:300){edges{node{
asset_identifier asset_type eligible_for_submission eligible_for_bounty max_severity archived_at}}}}}'''
sc=[e["node"] for e in gql(Q)["data"]["team"]["structured_scopes"]["edges"]]
print(f"\n=== [2] TONG so scope (khong loc): {len(sc)}  (T14 cua toi do 63) ===")
live=[s for s in sc if not s.get("archived_at")]
arch=[s for s in sc if s.get("archived_at")]
print(f"  archived_at=None (dang hieu luc): {len(live)}   (ho khai archived:false -> 44)")
print(f"  archived_at!=None (da nghi huu) : {len(arch)}   (ho khai archived:true  -> 19)")
li={s["asset_identifier"] for s in live if s["eligible_for_submission"]}
lo={s["asset_identifier"] for s in live if not s["eligible_for_submission"]}
print(f"\n  TRONG tap DANG HIEU LUC: IN={len(li)} OUT={len(lo)}   (ho khai IN=19 OUT=25)")
print(f"  >>> GIAO NHAU (IN ∩ OUT) = {sorted(li & lo)}   (ho khai 0)")
ai={s["asset_identifier"] for s in arch if s["eligible_for_submission"]}
ao={s["asset_identifier"] for s in arch if not s["eligible_for_submission"]}
print(f"  TRONG tap DA NGHI HUU : IN={len(ai)} OUT={len(ao)}")
print(f"\n=== [3] 4 tai san trong tam: ve NAO co archived_at? ===")
for name in ("*.gitlab.net","*.gitlap.com","about.gitlab.com","docs.gitlab.com"):
    print(f"  --- {name} ---")
    for s in sc:
        if s["asset_identifier"]==name:
            print(f"      type={s['asset_type']:<9} sub={str(s['eligible_for_submission']):<5} "
                  f"bounty={str(s['eligible_for_bounty']):<5} sev={str(s.get('max_severity')):<7} "
                  f"archived_at={s.get('archived_at')}")
print("\n=== [4] So sanh VOI T14 (toi do nam 2026-10-01T14:05Z, KHONG hoi archived_at) ===")
print("  T14: 63 scope | IN=24 | OUT=39 | giao = 4 (about, docs, *.gitlab.net, *.gitlap.com)")
print(f"  Nay: {len(sc)} scope | IN(tat ca)={len(li|ai)} | OUT(tat ca)={len(lo|ao)}")
print("  => tong 63 KHOP T14; nhung khi tach theo archived_at thi giao = 0")
