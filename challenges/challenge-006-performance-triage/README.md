# Challenge 006: Performance Triage

## Kurzbeschreibung

Zwei interne Webdienste sind erreichbar.

Einer fühlt sich langsam an.

Du sollst mit Wireshark prüfen, in welchem Abschnitt die sichtbare Wartezeit entsteht:

- DNS
- TCP
- HTTP Request/Response
- Datenübertragung
- oder unsicher/nicht belegbar

## Voraussetzungen

- Docker
- Docker Compose
- Wireshark
- TShark
- vorhandenes Docker-Lab `lab-basic-dns-http`

## Ergebnis-PCAP

```text
pcaps/generated/challenge-006-performance-triage.pcapng
```

## Geschätzte Dauer

```text
60 Minuten
```

## Ablauf

1. Docker-Lab starten
2. Capture erzeugen
3. Testtraffic erzeugen
4. ohne Lösung analysieren
5. Hinweise nur bei Bedarf lesen
6. TShark-Check ausführen
7. Lösung vergleichen
8. Kurzbericht verbessern
