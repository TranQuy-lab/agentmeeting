#!/usr/bin/env python3
"""Reviewer1 — kiem archived_at cua TUNG BAN GHI RIENG (khong gop nhom)."""
import json, urllib.request
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125 Safari/537.36"
def gql(q):
    r=urllib.request.Request("https://hackerone.com/graphql",data=json.dumps({"query":q}).encode(),
      headers={"Content-Type":"application/json","Accept":"application/json","User-Agent":UA},method="POST")
    return json.loads(urllib.request.urlopen(r,timeout=60).read().decode())
Q='''query{team(handle:"gitlab"){structured_scopes(first:300){edges{node{
asset_identifier asset_type eligible_for_submission eligible_for_bounty max_severity archived_at instruction}}}}}'''
sc=[e["node"] for e in gql(Q)["data"]["team"]["structured_scopes"]["edges"]]
print(f"TONG scope: {len(sc)}")
live=[s for s in sc if not s.get("archived_at")]
arch=[s for s in sc if s.get("archived_at")]
print(f"  dang hieu luc: {len(live)} | da nghi huu: {len(arch)}")
print()
print("=== [1] MOI BAN GHI co identifier chua 'gitlab.net' hoac 'gitlap.com' ===")
for s in sorted([x for x in sc if "gitlab.net" in x["asset_identifier"] or "gitlap.com" in x["asset_identifier"]],
                key=lambda x:(x["asset_identifier"], str(x.get("archived_at")))):
    print(f"  {s['asset_identifier']:<24} type={s['asset_type']:<9} sub={str(s['eligible_for_submission']):<5} "
          f"bounty={str(s['eligible_for_bounty']):<5} sev={str(s.get('max_severity')):<7} archived_at={s.get('archived_at')}")
print()
print("=== [2] TACH theo muc 'archived_at' ===")
from collections import defaultdict
groups=defaultdict(list)
for s in arch:
    d=str(s["archived_at"])[:10]
    groups[d].append(s)
for d in sorted(groups):
    print(f"  --- moc {d} : {len(groups[d])} ban ghi ---")
    for s in groups[d]:
        print(f"      {s['asset_identifier']:<24} type={s['asset_type']:<9} sub={str(s['eligible_for_submission']):<5} {s.get('archived_at')}")
