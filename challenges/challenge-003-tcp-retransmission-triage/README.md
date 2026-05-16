# Challenge 003: TCP Retransmission Triage

## Kurzbeschreibung

Ein Download von einem internen Webserver wirkt instabil.

Im Capture sollst du prüfen, ob TCP Retransmissions, Duplicate ACKs oder verwandte Analysehinweise sichtbar sind.

## Voraussetzungen

- Docker
- Docker Compose
- Wireshark
- TShark
- vorhandenes Docker-Lab `lab-advanced-tcp-loss`

## Ergebnis-PCAP

```text
pcaps/generated/challenge-003-tcp-retransmission-triage.pcapng
```

## Geschätzte Dauer

```text
60 Minuten
```

## Ablauf

1. Docker-Lab starten
2. Capture erzeugen
3. Download-Traffic erzeugen
4. ohne Lösung analysieren
5. Hinweise nur bei Bedarf lesen
6. TShark-Check ausführen
7. Lösung vergleichen
8. Kurzbericht verbessern
