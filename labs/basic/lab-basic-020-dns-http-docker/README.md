# Lab Basic 020: DNS und HTTP im Docker-Lab

## Ziel

In diesem Lab analysierst du DNS, NXDOMAIN, HTTP und einfache Wartezeit in einer kontrollierten Docker-Umgebung.

## Voraussetzungen

Du brauchst:

- Docker
- Docker Compose
- Wireshark
- TShark
- funktionierende Capture-Rechte auf dem Host

Prüfen:

```bash
docker --version
docker compose version
tshark --version
```

## Ergebnisdatei

Speichere den Capture lokal als:

```text
pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

Diese Datei soll nicht committed werden.

## Geschätzte Dauer

```text
45 Minuten
```

## WCA-Bezug

Dieses Lab übt:

- Display Filter
- DNS Query und Response
- DNS Response Codes
- HTTP Request und Response
- TCP-Port 80
- Zeitverhalten
- TShark-Auswertung
- Analysebericht mit Frame-Nummern
