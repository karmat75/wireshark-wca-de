#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/challenge-002-tcp-handshake-reset.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash challenges/challenge-002-tcp-handshake-reset/check_tshark.sh <pcap-file>" >&2
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
    printf "OK   %-48s %s\n" "$label" "$count"
  else
    printf "FAIL %-48s %s expected >= %s\n" "$label" "$count" "$min_count"
    return 1
  fi
}

echo "PCAP: $PCAP"
echo

failures=0

check_count "TCP packets" "tcp" 5 || failures=$((failures + 1))
check_count "TCP port 80 traffic" "tcp.port == 80" 3 || failures=$((failures + 1))
check_count "SYN to port 80" "tcp.flags.syn == 1 and tcp.flags.ack == 0 and tcp.dstport == 80" 1 || failures=$((failures + 1))
check_count "SYN/ACK from port 80" "tcp.flags.syn == 1 and tcp.flags.ack == 1 and tcp.srcport == 80" 1 || failures=$((failures + 1))
check_count "HTTP response from port 80" "http.response and tcp.srcport == 80" 1 || failures=$((failures + 1))
check_count "TCP port 81 traffic" "tcp.port == 81" 1 || failures=$((failures + 1))
check_count "RST packets" "tcp.flags.reset == 1" 1 || failures=$((failures + 1))

echo
echo "SYN packets:"
tshark -r "$PCAP" \
  -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e tcp.stream 2>/dev/null || true

echo
echo "RST packets:"
tshark -r "$PCAP" \
  -Y "tcp.flags.reset == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e tcp.stream 2>/dev/null || true

echo
echo "HTTP responses:"
tshark -r "$PCAP" \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.response.code \
  -e http.response.phrase 2>/dev/null || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your written analysis with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete or the test traffic may not have been generated as expected."
  exit 1
fi
