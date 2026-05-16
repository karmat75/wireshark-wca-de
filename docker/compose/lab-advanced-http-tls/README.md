# Docker-Lab: Advanced HTTP/TLS

Dieses Docker-Lab erzeugt einen Webserver mit HTTP und HTTPS.

## Dienste

| Dienst | IP | Zweck |
|---|---:|---|
| `lab-web-tls` | `172.28.70.10` | HTTP/HTTPS Webserver |
| `lab-client` | `172.28.70.100` | Client mit curl und Netzwerktools |

## Netzwerk

```text
172.28.70.0/24
```

## Hostname

Für SNI wird im Client `curl --resolve` verwendet:

```text
secure.lab.local -> 172.28.70.10
```

Es ist kein eigener DNS-Server nötig.

## Start

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml up -d --build
```

## Test

HTTP:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client \
  curl --noproxy '*' -I http://172.28.70.10/
```

HTTPS mit Zertifikatsprüfung deaktiviert:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client \
  curl --noproxy '*' -k --resolve secure.lab.local:443:172.28.70.10 -I https://secure.lab.local/
```

HTTPS ohne `-k`, erwarteter Zertifikatsfehler:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client \
  curl --noproxy '*' --connect-timeout 3 --resolve secure.lab.local:443:172.28.70.10 -I https://secure.lab.local/ || true
```

## Stop

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml down
```
