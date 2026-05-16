#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/lab-advanced-040-security-basics.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash labs/advanced/lab-advanced-040-security-basics/check_tshark.sh <pcap-file>" >&2
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

check_count "HTTP packets" "http" 8 || failures=$((failures + 1))
check_count "HTTP requests" "http.request" 8 || failures=$((failures + 1))
check_count "HTTP POST login" "http.request.method == \"POST\"" 1 || failures=$((failures + 1))
check_count "HTTP Authorization header" "http.authorization" 1 || failures=$((failures + 1))
check_count "Beacon requests" "http.request.uri contains \"/beacon\"" 5 || failures=$((failures + 1))
check_count "Beacon User-Agent" "http.user_agent contains \"BeaconSimulator\"" 5 || failures=$((failures + 1))
check_count "Synthetic token visible" "http contains \"LAB-TOKEN-12345\"" 1 || failures=$((failures + 1))
check_count "Synthetic password visible" "http contains \"LabPassword123\"" 1 || failures=$((failures + 1))

echo
echo "HTTP requests:"
tshark -r "$PCAP" \
  -Y "http.request" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.request.uri \
  -e http.user_agent 2>/dev/null || true

echo
echo "Authorization headers:"
tshark -r "$PCAP" \
  -Y "http.authorization" \
  -T fields \
  -e frame.number \
  -e http.authorization 2>/dev/null || true

echo
echo "POST data:"
tshark -r "$PCAP" \
  -Y "http.request.method == \"POST\"" \
  -T fields \
  -e frame.number \
  -e http.file_data 2>/dev/null || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your security triage with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete or the test traffic may not have been generated as expected."
  exit 1
fi
