# Challenge 005: Security Basics Triage

## Kurzbeschreibung

Ein HTTP-basierter Lab-Dienst erzeugt mehrere Security-relevante Muster:

- Basic Auth
- Formularwerte im HTTP Body
- synthetischer Token
- regelmäßige Beacon-ähnliche Requests

Deine Aufgabe ist eine defensive Triage mit Wireshark.

## Voraussetzungen

- Docker
- Docker Compose
- Wireshark
- TShark
- vorhandenes Docker-Lab `lab-advanced-security-basics`

## Ergebnis-PCAP

```text
pcaps/generated/challenge-005-security-basics-triage.pcapng
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

## Hinweis

Alle Werte in dieser Challenge sind synthetische Lab-Werte.

Keine echten Zugangsdaten verwenden.
