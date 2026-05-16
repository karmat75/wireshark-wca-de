# Challenge 004: HTTP/TLS Triage

## Kurzbeschreibung

Ein interner Webdienst ist über HTTP und HTTPS erreichbar.

Du sollst im Capture zeigen, welche Informationen im Klartext sichtbar sind und welche bei TLS geschützt sind.

## Voraussetzungen

- Docker
- Docker Compose
- Wireshark
- TShark
- vorhandenes Docker-Lab `lab-advanced-http-tls`

## Ergebnis-PCAP

```text
pcaps/generated/challenge-004-http-tls-triage.pcapng
```

## Geschätzte Dauer

```text
60 Minuten
```

## Ablauf

1. Docker-Lab starten
2. Capture erzeugen
3. HTTP- und HTTPS-Traffic erzeugen
4. ohne Lösung analysieren
5. Hinweise nur bei Bedarf lesen
6. TShark-Check ausführen
7. Lösung vergleichen
8. Kurzbericht verbessern
