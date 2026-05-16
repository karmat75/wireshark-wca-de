# Challenge 002: TCP Handshake und Reset

Diese Challenge nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.

Du erzeugst einen Capture und analysierst zwei typische TCP-Situationen:

- eine erfolgreiche Verbindung zu einem Webserver
- einen Verbindungsversuch zu einem geschlossenen Port

## Challenge-Pfad

```text
challenges/challenge-002-tcp-handshake-reset/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-basic-dns-http/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-002-tcp-handshake-reset.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- welcher TCP Stream erfolgreich ist
- welche Frames den 3-Way Handshake bilden
- ob HTTP nach dem Handshake sichtbar ist
- welcher Verbindungsversuch aktiv abgelehnt wird
- wer RST/RST-ACK sendet
- welche Aussage dadurch belegbar ist
- welche Aussagen zu stark wären

## WCA-Bezug

Diese Challenge trainiert:

- TCP Flags
- TCP 3-Way Handshake
- TCP Stream
- HTTP über TCP
- RST/RST-ACK
- Display Filter
- TShark-Auswertung
- vorsichtige Troubleshooting-Bewertung
