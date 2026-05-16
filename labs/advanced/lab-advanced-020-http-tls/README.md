# Lab Advanced 020: HTTP und TLS

## Ziel

In diesem Lab analysierst du HTTP im Klartext und HTTPS/TLS in einer kontrollierten Docker-Umgebung.

Du erzeugst:

- HTTP Request/Response auf Port 80
- HTTPS/TLS Verbindung auf Port 443
- TLS Client Hello mit SNI
- optional einen TLS Alert durch Zertifikatsprüfung

## Voraussetzungen

Du brauchst:

- Docker
- Docker Compose
- Wireshark
- TShark
- Capture-Rechte auf dem Host

Prüfen:

```bash
docker --version
docker compose version
tshark --version
```

## Ergebnisdatei

Speichere den Capture lokal als:

```text
pcaps/generated/lab-advanced-020-http-tls.pcapng
```

Diese Datei soll nicht committed werden.

## Geschätzte Dauer

```text
60 Minuten
```

## WCA-Bezug

Dieses Lab übt:

- HTTP Request und Response
- TLS Client Hello
- SNI
- ALPN
- TLS Alerts
- TCP Port 80 und 443
- Display Filter
- TShark-Auswertung
- Analysebericht
