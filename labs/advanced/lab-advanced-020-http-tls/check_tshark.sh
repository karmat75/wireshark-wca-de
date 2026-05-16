#!/usr/bin/env bash
set -euo pipefail

PCAP="${1:-pcaps/generated/lab-advanced-020-http-tls.pcapng}"

if [ ! -f "$PCAP" ]; then
  echo "ERROR: PCAP not found: $PCAP" >&2
  echo "Usage: bash labs/advanced/lab-advanced-020-http-tls/check_tshark.sh <pcap-file>" >&2
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

check_count "HTTP packets" "http" 2 || failures=$((failures + 1))
check_count "HTTP requests" "http.request" 1 || failures=$((failures + 1))
check_count "HTTP responses" "http.response" 1 || failures=$((failures + 1))
check_count "TLS packets" "tls" 3 || failures=$((failures + 1))
check_count "TLS Client Hello" "tls.handshake.type == 1" 1 || failures=$((failures + 1))
check_count "SNI secure.lab.local" "tls.handshake.extensions_server_name contains \"secure.lab.local\"" 1 || failures=$((failures + 1))
check_count "Traffic port 80" "tcp.port == 80" 2 || failures=$((failures + 1))
check_count "Traffic port 443" "tcp.port == 443" 2 || failures=$((failures + 1))

info_count "ALPN fields" "tls.handshake.extensions_alpn_str"
info_count "TLS alerts" "tls.alert_message"
info_count "TLS application data" "tls.app_data"

echo
echo "HTTP summary:"
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
echo "TLS SNI:"
tshark -r "$PCAP" \
  -Y "tls.handshake.extensions_server_name" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.handshake.extensions_server_name 2>/dev/null || true

echo
echo "TLS alerts:"
tshark -r "$PCAP" \
  -Y "tls.alert_message" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.alert_message.desc 2>/dev/null || true

echo
if [ "$failures" -eq 0 ]; then
  echo "Result: basic technical checks passed."
  echo "Now compare your written analysis with solution.md."
else
  echo "Result: $failures check(s) failed."
  echo "The capture may be incomplete or the test traffic may not have been generated as expected."
  exit 1
fi
