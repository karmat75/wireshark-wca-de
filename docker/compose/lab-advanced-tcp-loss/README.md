# Docker-Lab: Advanced TCP Loss

Dieses Docker-Lab erzeugt TCP-Verkehr mit absichtlichem Paketverlust.

## Dienste

| Dienst | IP | Zweck |
|---|---:|---|
| `lab-web-loss` | `172.28.60.10` | Webserver mit absichtlichem Paketverlust auf egress |
| `lab-client` | `172.28.60.100` | Client mit curl und Netzwerktools |

## Netzwerk

```text
172.28.60.0/24
```

## Start

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml up -d --build
```

## Status

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml ps
```

## Test

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml exec lab-client \
  curl -o /tmp/bigfile.bin http://172.28.60.10/bigfile.bin
```

## Stop

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml down
```

## Hinweis

Der Webserver-Container nutzt `tc netem`, um auf seinem Interface Paketverlust und leichte Verzögerung einzubauen.

Dafür braucht der Container `NET_ADMIN`.

Wenn keine Retransmissions sichtbar sind, kann der Test erneut ausgeführt werden oder die Verlustquote in `entrypoint.sh` für lokale Experimente angepasst werden.
