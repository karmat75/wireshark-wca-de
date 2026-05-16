# Lab Basic 030: TCP Handshake und Reset

## Ziel

In diesem Lab analysierst du TCP-Verbindungsaufbau und TCP-Reset in einer kontrollierten Docker-Umgebung.

Du erzeugst:

- eine erfolgreiche HTTP-Verbindung zu `web-ok.lab.local:80`
- einen Verbindungsversuch zu einem geschlossenen Port `172.28.50.10:81`

## Voraussetzungen

Du brauchst:

- Docker
- Docker Compose
- Wireshark
- TShark
- vorhandenes Docker-Lab `lab-basic-dns-http`

Prüfen:

```bash
docker --version
docker compose version
tshark --version
```

## Ergebnisdatei

Speichere den Capture lokal als:

```text
pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

Diese Datei soll nicht committed werden.

## Geschätzte Dauer

```text
45 Minuten
```

## WCA-Bezug

Dieses Lab übt:

- TCP 3-Way Handshake
- TCP Stream Filter
- TCP Flags
- RST/RST-ACK
- HTTP über TCP
- TShark-Auswertung
- Analysebericht mit Frame-Nummern
