#!/bin/sh
set -eu

mkdir -p /etc/nginx/certs

if [ ! -f /etc/nginx/certs/secure.lab.local.crt ]; then
  echo "Generating self-signed certificate for secure.lab.local..."
  openssl req -x509 -nodes -newkey rsa:2048 -days 365 \
    -keyout /etc/nginx/certs/secure.lab.local.key \
    -out /etc/nginx/certs/secure.lab.local.crt \
    -subj "/CN=secure.lab.local" \
    -addext "subjectAltName=DNS:secure.lab.local,DNS:lab-web-tls,IP:172.28.70.10"
fi

exec nginx -g 'daemon off;'
