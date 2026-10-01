#!/usr/bin/env python3
"""Fetch PUBLIC HackerOne program policy + structured scopes via the
unauthenticated public GraphQL endpoint. Read-only, single request per program."""
import json
import sys
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
ENDPOINT = "https://hackerone.com/graphql"

QUERY = """
query Prog($h: String!) {
  team(handle: $h) {
    id
    handle
    name
    offers_bounties
    submission_state
    policy
    structured_scopes(first: 200) {
      edges {
        node {
          asset_identifier
          asset_type
          eligible_for_submission
          eligible_for_bounty
          max_severity
          instruction
        }
      }
    }
  }
}
"""


def fetch(handle):
    payload = json.dumps({"query": QUERY, "variables": {"h": handle}}).encode()
    req = urllib.request.Request(
        ENDPOINT, data=payload,
        headers={"Content-Type": "application/json",
                 "Accept": "application/json",
                 "User-Agent": UA},
        method="POST")
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    for handle in sys.argv[1:]:
        try:
            data = fetch(handle)
        except Exception as e:  # noqa: BLE001
            print(f"[{handle}] ERROR {type(e).__name__}: {e}")
            continue
        with open(f"h1_{handle}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        team = (data.get("data") or {}).get("team")
        if not team:
            print(f"[{handle}] NO TEAM -> {json.dumps(data)[:300]}")
            continue
        scopes = [e["node"] for e in
                  (team.get("structured_scopes") or {}).get("edges", [])]
        ins = [s for s in scopes if s.get("eligible_for_submission")]
        print(f"[{handle}] name={team.get('name')!r} "
              f"bounties={team.get('offers_bounties')} "
              f"state={team.get('submission_state')} "
              f"scopes={len(scopes)} in_scope={len(ins)} "
              f"policy_chars={len(team.get('policy') or '')}")
        for s in ins:
            print(f"    - {s['asset_type']:<12} {s['asset_identifier']}"
                  f"  bounty={s['eligible_for_bounty']}"
                  f"  max_sev={s.get('max_severity')}")


if __name__ == "__main__":
    main()
