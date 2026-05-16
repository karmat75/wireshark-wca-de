# Lab Advanced 030: Performanceanalyse

## Ziel

In diesem Lab analysierst du Wartezeiten in einem kontrollierten Docker-Lab.

Du vergleichst:

- `web-ok.lab.local`
- `web-slow.lab.local`

Der langsame Webserver wartet absichtlich vor der Antwort.

Deine Aufgabe ist, im Capture zu zeigen, wo die Wartezeit sichtbar entsteht.

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
pcaps/generated/lab-advanced-030-performance-analyse.pcapng
```

Diese Datei soll nicht committed werden.

## Geschätzte Dauer

```text
60 Minuten
```

## WCA-Bezug

Dieses Lab übt:

- Performanceanalyse
- DNS-, TCP- und HTTP-Zeitabschnitte
- Conversations
- Protocol Hierarchy
- I/O Graphs
- Time Reference
- TShark-Auswertung
- vorsichtige Ursachenbewertung
