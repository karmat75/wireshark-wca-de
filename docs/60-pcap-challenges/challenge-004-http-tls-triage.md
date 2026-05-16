# Challenge 004: HTTP/TLS Triage

Diese Challenge nutzt das vorhandene Docker-Lab `lab-advanced-http-tls`.

Du erzeugst einen Capture und untersuchst HTTP und HTTPS/TLS nebeneinander.

## Challenge-Pfad

```text
challenges/challenge-004-http-tls-triage/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-advanced-http-tls/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-004-http-tls-triage.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- welche Verbindung HTTP im Klartext nutzt
- welche Verbindung TLS nutzt
- ob SNI sichtbar ist
- ob ALPN sichtbar ist
- ob TLS Alerts sichtbar sind
- was bei HTTP lesbar ist
- was bei TLS nicht im Klartext lesbar ist
- welche Metadaten bei TLS trotzdem sichtbar bleiben

## WCA-Bezug

Diese Challenge trainiert:

- HTTP
- TLS
- TCP Port 80 und 443
- TLS Client Hello
- SNI
- ALPN
- TLS Alert
- Display Filter
- TShark
- Security- und Methodik-Grundlagen
