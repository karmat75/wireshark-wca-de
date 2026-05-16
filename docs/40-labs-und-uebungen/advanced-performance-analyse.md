# Advanced Lab 030: Performanceanalyse

Dieses Lab trainiert eine der wichtigsten praktischen Fähigkeiten in Wireshark:

> Wartezeit nicht nur sehen, sondern sauber einordnen.

Du vergleichst einen normalen Webserver und einen absichtlich langsamen Webserver aus dem vorhandenen Docker-Lab.

## Lab-Pfad

```text
labs/advanced/lab-advanced-030-performance-analyse/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-basic-dns-http/compose.yml
```

## Ziel

Du übst:

- DNS-, TCP- und HTTP-Zeitabschnitte zu trennen
- schnellen und langsamen Webserver zu vergleichen
- Zeitspalten in Wireshark sinnvoll zu nutzen
- Time Reference zu setzen
- Conversations und Protocol Hierarchy einzusetzen
- I/O Graphs zur Orientierung zu verwenden
- TShark-Ausgaben mit Zeitstempeln zu erzeugen
- vorsichtig zu formulieren, wo die Wartezeit sichtbar entsteht

## Ergebnisdatei

Lokal erzeugter Capture:

```text
pcaps/generated/lab-advanced-030-performance-analyse.pcapng
```

Diese Datei ist lokal und wird nicht committed.

## WCA-Bezug

Dieses Lab trainiert:

- Performanceanalyse
- Request/Response-Zeit
- DNS-Zeit
- TCP-Verbindungsaufbau
- HTTP-Zeitverhalten
- Conversations
- I/O Graphs
- TShark
- Fehleranalyse-Methodik
