#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/lab-advanced-010-tcp-retransmission.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash labs/advanced/lab-advanced-010-tcp-retransmission/check_tshark.sh <pcap-file>" >&2
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

info_count() {
  local label="$1"
  local filter="$2"
  local count

  count="$(tshark -r "$PCAP" -Y "$filter" 2>/dev/null | wc -l | tr -d ' ')"
  printf "INFO %-52s %s\n" "$label" "$count"
}

echo "PCAP: $PCAP"
echo

failures=0

check_count "TCP packets in lab net" "tcp and ip.addr == 172.28.60.10" 50 || failures=$((failures + 1))
check_count "HTTP packets" "http and ip.addr == 172.28.60.10" 1 || failures=$((failures + 1))
check_count "TCP analysis flags" "tcp.analysis.flags" 1 || failures=$((failures + 1))
check_count "Retransmissions or fast retransmissions" "tcp.analysis.retransmission or tcp.analysis.fast_retransmission" 1 || failures=$((failures + 1))

info_count "Duplicate ACKs" "tcp.analysis.duplicate_ack"
info_count "Lost segment hints" "tcp.analysis.lost_segment"
info_count "Out-of-order hints" "tcp.analysis.out_of_order"

echo
echo "Top TCP conversations:"
tshark -r "$PCAP" -q -z conv,tcp 2>/dev/null || true

echo
echo "TCP analysis flags:"
tshark -r "$PCAP" \
  -Y "tcp.analysis.flags" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e _ws.col.Info 2>/dev/null | head -40 || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your written analysis with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete, netem may not be active, or the download may need to be repeated."
  exit 1
fi
