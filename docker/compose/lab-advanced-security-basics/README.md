# Docker-Lab: Advanced Security Basics

Dieses Docker-Lab erzeugt kontrollierten HTTP-Traffic für defensive Security-Analyse.

## Dienste

| Dienst | IP | Zweck |
|---|---:|---|
| `lab-web-security` | `172.28.80.10` | einfacher HTTP-Server |
| `lab-client` | `172.28.80.100` | Client mit curl und Netzwerktools |

## Netzwerk

```text
172.28.80.0/24
```

## Start

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml up -d --build
```

## Testtraffic

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml exec lab-client sh -lc '
curl --noproxy "*" -A "WWCA-LabClient/1.0" http://172.28.80.10/
curl --noproxy "*" -u labuser:LabPassword123 http://172.28.80.10/basic
curl --noproxy "*" -X POST -d "username=labuser&password=LabPassword123&token=LAB-TOKEN-12345" http://172.28.80.10/login
for i in 1 2 3 4 5; do
  curl --noproxy "*" -A "WWCA-BeaconSimulator/1.0" "http://172.28.80.10/beacon?id=training-node-01&seq=$i"
  sleep 1
done
'
```

## Stop

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml down
```

## Hinweis

Alle Werte sind synthetisch und nur für das Lab gedacht.

Nicht mit echten Zugangsdaten nachbauen.
