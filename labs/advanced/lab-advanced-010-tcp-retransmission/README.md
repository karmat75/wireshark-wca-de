# Lab Advanced 010: TCP Retransmission

## Ziel

In diesem Lab analysierst du TCP Retransmissions in einer kontrollierten Docker-Umgebung.

Das Lab erzeugt einen größeren HTTP-Download und baut auf der Serverseite absichtlichen Paketverlust ein.

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
pcaps/generated/lab-advanced-010-tcp-retransmission.pcapng
```

Diese Datei soll nicht committed werden.

## Geschätzte Dauer

```text
60 Minuten
```

## WCA-Bezug

Dieses Lab übt:

- TCP Retransmissions
- Duplicate ACKs
- Fast Retransmit
- TCP Stream Analyse
- TCP Sequence und ACK
- Wireshark Analysefelder
- TShark-Auswertung
- methodische Bewertung
