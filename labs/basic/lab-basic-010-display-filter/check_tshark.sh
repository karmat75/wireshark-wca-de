#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/lab-basic-020-dns-http-docker.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash labs/basic/lab-basic-010-display-filter/check_tshark.sh <pcap-file>" >&2
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
    printf "OK   %-46s %s\n" "$label" "$count"
  else
    printf "FAIL %-46s %s expected >= %s\n" "$label" "$count" "$min_count"
    return 1
  fi
}

echo "PCAP: $PCAP"
echo

failures=0

check_count "DNS packets" "dns" 3 || failures=$((failures + 1))
check_count "DNS queries" "dns.flags.response == 0" 3 || failures=$((failures + 1))
check_count "DNS responses" "dns.flags.response == 1" 3 || failures=$((failures + 1))
check_count "DNS NXDOMAIN" "dns.flags.rcode == 3" 1 || failures=$((failures + 1))
check_count "TCP packets" "tcp" 3 || failures=$((failures + 1))
check_count "HTTP packets" "http" 2 || failures=$((failures + 1))
check_count "HTTP requests" "http.request" 1 || failures=$((failures + 1))
check_count "HTTP responses" "http.response" 1 || failures=$((failures + 1))
check_count "Client traffic" "ip.addr == 172.28.50.100" 3 || failures=$((failures + 1))
check_count "DNS name contains web" "dns.qry.name contains \"web\"" 1 || failures=$((failures + 1))

echo
echo "Suggested filter counts:"
for filter in   "dns"   "dns.flags.response == 0"   "dns.flags.response == 1"   "dns.flags.rcode == 3"   "http"   "http.request"   "http.response"   "tcp.port == 80"   "udp.port == 53"   "ip.addr == 172.28.50.100"   "(dns or http) and ip.addr == 172.28.50.100"
do
  count="$(tshark -r "$PCAP" -Y "$filter" 2>/dev/null | wc -l | tr -d ' ')"
  printf "%-55s %s\n" "$filter" "$count"
done

echo
echo "DNS queries:"
tshark -r "$PCAP" \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e dns.qry.name 2>/dev/null || true

echo
echo "HTTP responses:"
tshark -r "$PCAP" \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e http.response.code \
  -e http.response.phrase 2>/dev/null || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your filter table with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete or not from the DNS/HTTP Docker lab."
  exit 1
fi
