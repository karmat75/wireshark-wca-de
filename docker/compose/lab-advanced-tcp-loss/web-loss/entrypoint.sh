#!/bin/sh
set -eu

echo "Applying netem settings on eth0..."
tc qdisc replace dev eth0 root netem delay 25ms loss 5% || {
  echo "WARNING: could not apply netem settings. Retransmissions may not appear."
}

echo "Current qdisc:"
tc qdisc show dev eth0 || true

exec nginx -g 'daemon off;'
