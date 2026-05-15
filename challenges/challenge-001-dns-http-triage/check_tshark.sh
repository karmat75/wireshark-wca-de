#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/challenge-001-dns-http-triage.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash challenges/challenge-001-dns-http-triage/check_tshark.sh <pcap-file>" >&2
  exit 2
fi

if ! command -v tshark >/dev/null 2>&1; then
  echo "ERROR: tshark not found in PATH" >&2
  exit 2
fi

check_count() {
  local label="$1"
  local filter="$2"
  local min_count="$3"
  local count

  count="$(tshark -r "$PCAP" -Y "$filter" 2>/dev/null | wc -l | tr -d ' ')"

  if [ "$count" -ge "$min_count" ]; then
    printf "OK   %-45s %s\n" "$label" "$count"
  else
    printf "FAIL %-45s %s expected >= %s\n" "$label" "$count" "$min_count"
    return 1
  fi
}

echo "PCAP: $PCAP"
echo

failures=0

check_count "DNS packets" "dns" 3 || failures=$((failures + 1))
check_count "DNS query web-ok.lab.local" "dns.flags.response == 0 and dns.qry.name == \"web-ok.lab.local\"" 1 || failures=$((failures + 1))
check_count "DNS query web-slow.lab.local" "dns.flags.response == 0 and dns.qry.name == \"web-slow.lab.local\"" 1 || failures=$((failures + 1))
check_count "DNS NXDOMAIN" "dns.flags.rcode == 3" 1 || failures=$((failures + 1))
check_count "HTTP packets" "http" 2 || failures=$((failures + 1))
check_count "HTTP responses" "http.response" 2 || failures=$((failures + 1))
check_count "HTTP traffic web-ok" "ip.addr == 172.28.50.10 and http" 1 || failures=$((failures + 1))
check_count "HTTP traffic web-slow" "ip.addr == 172.28.50.20 and http" 1 || failures=$((failures + 1))

echo
echo "DNS responses:"
tshark -r "$PCAP"   -Y "dns.flags.response == 1"   -T fields   -e frame.number   -e frame.time_relative   -e ip.src   -e ip.dst   -e dns.qry.name   -e dns.flags.rcode   -e dns.a 2>/dev/null || true

echo
echo "HTTP responses:"
tshark -r "$PCAP"   -Y "http.response"   -T fields   -e frame.number   -e frame.time_relative   -e ip.src   -e ip.dst   -e http.response.code   -e http.response.phrase 2>/dev/null || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your written analysis with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete or the test traffic may not have been generated as expected."
  exit 1
fi
