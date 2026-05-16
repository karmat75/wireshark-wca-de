# Basic Lab 030: TCP Handshake und Reset

Dieses Lab nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.

Du analysierst zwei TCP-Situationen:

1. eine erfolgreiche Verbindung zu einem Webserver auf TCP-Port 80
2. einen Verbindungsversuch zu einem geschlossenen TCP-Port

Dabei lernst du, einen erfolgreichen 3-Way Handshake und eine aktive Ablehnung per RST zu erkennen.

## Lab-Pfad

```text
labs/basic/lab-basic-030-tcp-handshake-reset/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-basic-dns-http/compose.yml
```

## Ziel

Du übst:

- TCP SYN, SYN/ACK und ACK zu erkennen
- einen TCP Stream zu isolieren
- HTTP über TCP Port 80 im Kontext zu sehen
- RST/RST-ACK bei geschlossenem Port einzuordnen
- saubere Aussagen zu formulieren
- TShark zur technischen Prüfung zu verwenden

## Ergebnisdatei

Lokal erzeugter Capture:

```text
pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

Diese Datei ist lokal und wird nicht committed.

## WCA-Bezug

Dieses Lab trainiert:

- TCP-Verbindungsaufbau
- TCP Flags
- TCP Streams
- geschlossene Ports
- RST-Bewertung
- Capture-Punkt und Belegbarkeit
- Display Filter und TShark
