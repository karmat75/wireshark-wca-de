# Challenge 001: DNS/HTTP Triage

Diese Challenge nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.

Du erzeugst einen Capture und analysierst ein einfaches, aber prüfungsnahes Szenario:

- zwei interne Webserver
- ein nicht existierender DNS-Name
- eine absichtliche HTTP-Verzögerung
- DNS- und HTTP-Auswertung mit Wireshark und TShark

## Challenge-Pfad

```text
challenges/challenge-001-dns-http-triage/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-basic-dns-http/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-001-dns-http-triage.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- welche Namen abgefragt wurden
- welcher Name nicht existiert
- welche Webserver erreichbar sind
- welcher Webserver langsam antwortet
- welche Aussagen durch den Capture belegbar sind
- welche Aussagen nicht belegt sind

## WCA-Bezug

Diese Challenge trainiert:

- DNS Query und DNS Response
- DNS Response Codes
- Display Filter
- HTTP Request und Response
- Zeitverhalten
- TShark-Auswertung
- Analysebericht mit Frame-Nummern
- vorsichtige Bewertung statt Bauchgefühl

## Vollständige Dateien

Siehe:

```text
challenges/challenge-001-dns-http-triage/
```
