#!/usr/bin/env python3
"""Reviewer1 — fetch DOC LAP scope HackerOne (khong dung script/JSON cua BountyRecon).
Chi doc du lieu CONG KHAI qua GraphQL khong xac thuc. 1 request/program."""
import json, sys, urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
Q = """
query R($h:String!){team(handle:$h){handle name offers_bounties submission_state
 structured_scopes(first:200){edges{node{asset_identifier asset_type
 eligible_for_submission eligible_for_bounty max_severity instruction}}}}}
"""
def fetch(h):
    body=json.dumps({"query":Q,"variables":{"h":h}}).encode()
    r=urllib.request.Request("https://hackerone.com/graphql",data=body,
        headers={"Content-Type":"application/json","Accept":"application/json","User-Agent":UA},method="POST")
    with urllib.request.urlopen(r,timeout=60) as resp:
        return json.loads(resp.read().decode())

for h in sys.argv[1:]:
    try: d=fetch(h)
    except Exception as e:
        print(f"[{h}] FETCH ERROR {type(e).__name__}: {e}"); continue
    json.dump(d,open(f"/tmp/rv1_h1_{h}.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
    t=(d.get("data") or {}).get("team")
    if not t: print(f"[{h}] NO TEAM: {json.dumps(d)[:300]}"); continue
    sc=[e["node"] for e in (t.get("structured_scopes") or {}).get("edges",[])]
    ins=[s for s in sc if s.get("eligible_for_submission")]
    out=[s for s in sc if not s.get("eligible_for_submission")]
    print(f"[{h}] name={t.get('name')!r} bounties={t.get('offers_bounties')} state={t.get('submission_state')}")
    print(f"      tong scope={len(sc)} | IN={len(ins)} | OUT={len(out)} | policy_chars={len(t.get('policy') or '')}")
    # GIAO NHAU: cung asset_identifier xuat hien o CA HAI phia
    ki={ (s['asset_identifier'], s['asset_type']) for s in ins }
    ko={ (s['asset_identifier'], s['asset_type']) for s in out }
    inter=sorted(ki & ko)
    print(f"      >>> GIAO NHAU (cung identifier+type o CA HAI phia): {len(inter)}")
    for a in inter: print(f"          CONFLICT: {a[1]:<12} {a[0]}")
    # cung identifier nhung KHAC type
    ii={s['asset_identifier'] for s in ins}; oo={s['asset_identifier'] for s in out}
    only_name=sorted(ii & oo)
    if set(x[0] for x in inter)!=set(only_name):
        print("      (luu y) cung ten nhung khac asset_type:", sorted(set(only_name)-set(x[0] for x in inter)))
