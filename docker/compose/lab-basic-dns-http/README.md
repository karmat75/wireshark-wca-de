# Docker-Lab: Basic DNS/HTTP

Dieses Docker-Lab erzeugt eine kleine, kontrollierte Umgebung für DNS- und HTTP-Analyse.

## Dienste

| Dienst | IP | Zweck |
|---|---:|---|
| `lab-dns` | `172.28.50.53` | CoreDNS für `lab.local` |
| `lab-web-ok` | `172.28.50.10` | normaler Webserver |
| `lab-web-slow` | `172.28.50.20` | Webserver mit absichtlicher Verzögerung |
| `lab-client` | `172.28.50.100` | Client mit Netzwerktools |

## Namen

| Name | Ziel |
|---|---|
| `web-ok.lab.local` | `172.28.50.10` |
| `web-slow.lab.local` | `172.28.50.20` |
| `dns.lab.local` | `172.28.50.53` |

## Start

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml up -d
```

## Status

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml ps
```

## Test

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client dig web-ok.lab.local
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client dig does-not-exist.lab.local
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client curl -I http://web-ok.lab.local
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client curl -I http://web-slow.lab.local
```

## Stop

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```

## Netzwerk

Das Lab verwendet ein eigenes Docker-Netz:

```text
172.28.50.0/24
```

Für Captures auf dem Host kann ein Capture Filter hilfreich sein:

```text
net 172.28.50.0/24
```
