#!/usr/bin/env bash
# Passive / non-intrusive surface check for a bug-bounty program.
# Only: public DNS records, robots.txt, public HTTP headers, public security.txt.
# No scanning, no fuzzing, no payloads, no enumeration beyond a fixed small list.
# Usage: recon.sh <slug> <primary_host> <extra_domain...>
set -u
SLUG="$1"; shift
HOST="$1"; shift
OUT="recon_${SLUG}.txt"
: > "$OUT"

log() { echo "$@" | tee -a "$OUT"; }
run() {                      # run <description> <command...>
  local desc="$1"; shift
  log ""
  log "\$ $*"
  log "--- output ---"
  timeout 30 "$@" 2>&1 | tee -a "$OUT"
  log "--- end (rc=${PIPESTATUS[0]}) ---"
}

log "================================================================"
log "PASSIVE RECON — program: ${SLUG}"
log "UTC timestamp: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
log "Local timestamp: $(date '+%Y-%m-%d %H:%M:%S %Z')"
log "Host under check: ${HOST}"
log "Method: public DNS + robots.txt + public HTTP response headers +"
log "        public /.well-known/security.txt. NO active scanning."
log "================================================================"

for d in "$HOST" "$@"; do
  log ""
  log "########## DNS: ${d} ##########"
  run "dig ${d} NS"        dig +noall +answer +time=5 +tries=1 "${d}" NS
  run "dig ${d} A"         dig +noall +answer +time=5 +tries=1 "${d}" A
  run "dig ${d} AAAA"      dig +noall +answer +time=5 +tries=1 "${d}" AAAA
  run "dig ${d} MX"        dig +noall +answer +time=5 +tries=1 "${d}" MX
  run "dig ${d} TXT"       dig +noall +answer +time=5 +tries=1 "${d}" TXT
  run "dig ${d} CAA"       dig +noall +answer +time=5 +tries=1 "${d}" CAA
  run "dig _dmarc.${d} TXT" dig +noall +answer +time=5 +tries=1 "_dmarc.${d}" TXT
  sleep 1
done

log ""
log "########## PUBLIC WEB SURFACE: ${HOST} ##########"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

run "curl -sSI (public headers)" \
  curl -sS -I --max-time 20 -A "$UA" "https://${HOST}/"
sleep 2
run "curl robots.txt" \
  curl -sS --max-time 20 -A "$UA" "https://${HOST}/robots.txt"
sleep 2
run "curl .well-known/security.txt" \
  curl -sS --max-time 20 -A "$UA" "https://${HOST}/.well-known/security.txt"
sleep 2
run "curl security.txt (root fallback)" \
  curl -sS --max-time 20 -A "$UA" "https://${HOST}/security.txt"
sleep 2
run "one TLS handshake -> certificate SANs (no scan)" \
  bash -c "echo | timeout 20 openssl s_client -connect ${HOST}:443 -servername ${HOST} 2>/dev/null | openssl x509 -noout -subject -issuer -dates -ext subjectAltName"

log ""
log "================================================================"
log "END PASSIVE RECON — ${SLUG}"
log "================================================================"
wc -l "$OUT"
