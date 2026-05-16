# Challenge 005: Security Basics Triage

Diese Challenge nutzt das vorhandene Docker-Lab `lab-advanced-security-basics`.

Du erzeugst einen Capture und untersuchst HTTP-Verkehr aus defensiver Security-Sicht.

## Challenge-Pfad

```text
challenges/challenge-005-security-basics-triage/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-advanced-security-basics/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-005-security-basics-triage.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- ob HTTP im Klartext sichtbar ist
- ob Basic Auth im Capture sichtbar ist
- ob Formularwerte im HTTP Body sichtbar sind
- ob synthetische Tokens sichtbar sind
- ob Beacon-ähnliche Requests sichtbar sind
- welche User-Agents verwendet wurden
- was dadurch belegt ist
- was ohne weiteren Kontext nicht belegt ist
- warum echte Captures mit solchen Daten geschützt werden müssen

## WCA-Bezug

Diese Challenge trainiert:

- HTTP-Analyse
- Display Filter
- Follow TCP Stream
- Security-Basics
- TShark
- Methodik
- Datenschutz und sichere Dokumentation
