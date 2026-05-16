# Basic Lab 010: Display Filter

Dieses Lab trainiert Display Filter systematisch.

Es ist bewusst vor den tieferen Protokoll-Labs einsortiert, weil Filter in fast jeder Analyse gebraucht werden.

## Lab-Pfad

```text
labs/basic/lab-basic-010-display-filter/
```

## Ziel

Du übst:

- einfache Protokollfilter
- IP-, Port- und Hostfilter
- DNS Query und Response Filter
- DNS Response Codes
- HTTP Request und Response Filter
- TCP Stream Filter
- logische Operatoren
- Klammern
- `contains`
- Negation
- TShark als Gegenprüfung

## Benötigte PCAP

Empfohlen ist eine lokale PCAP aus dem Docker-DNS/HTTP-Lab:

```text
pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

Alternativ kannst du im Lab eine neue Datei erzeugen:

```text
pcaps/generated/lab-basic-010-display-filter.pcapng
```

## WCA-Bezug

Dieses Lab trainiert eine Kernkompetenz:

> passende Pakete finden, ohne den Capture zu verändern.

Display Filter sind kein Nebenthema. Sie sind eines der wichtigsten Werkzeuge für Wireshark-Analyse.
