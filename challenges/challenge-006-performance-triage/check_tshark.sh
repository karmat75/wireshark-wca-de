#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/challenge-006-performance-triage.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash challenges/challenge-006-performance-triage/check_tshark.sh <pcap-file>" >&2
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
    printf "OK   %-52s %s\n" "$label" "$count"
  else
    printf "FAIL %-52s %s expected >= %s\n" "$label" "$count" "$min_count"
    return 1
  fi
}

echo "PCAP: $PCAP"
echo

failures=0

check_count "DNS packets" "dns" 2 || failures=$((failures + 1))
check_count "HTTP packets" "http" 4 || failures=$((failures + 1))
check_count "HTTP web-ok traffic" "ip.addr == 172.28.50.10 and http" 2 || failures=$((failures + 1))
check_count "HTTP web-slow traffic" "ip.addr == 172.28.50.20 and http" 2 || failures=$((failures + 1))
check_count "HTTP responses" "http.response" 2 || failures=$((failures + 1))
check_count "TCP SYN packets" "tcp.flags.syn == 1 and tcp.flags.ack == 0" 2 || failures=$((failures + 1))

echo
echo "HTTP request/response timeline:"
tshark -r "$PCAP" \
  -Y "http.request or http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.response.code \
  -e http.response.phrase 2>/dev/null || true

echo
echo "DNS timeline:"
tshark -r "$PCAP" \
  -Y "dns" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.flags.response \
  -e dns.qry.name 2>/dev/null || true

echo
echo "TCP SYN timeline:"
tshark -r "$PCAP" \
  -Y "tcp.flags.syn == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e tcp.flags.syn \
  -e tcp.flags.ack \
  -e tcp.stream 2>/dev/null || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your performance triage with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete or the test traffic may not have been generated as expected."
  exit 1
fi
