# Szenario

Ein Benutzer meldet:

```text
Der Download vom internen Webserver ist langsam und wirkt unruhig.
```

Du erhältst einen Capture aus dem Lab-Netz.

Deine Aufgabe ist eine TCP-Triage:

- Welche Verbindung ist relevant?
- Sind Retransmissions sichtbar?
- Sind Duplicate ACKs sichtbar?
- Gibt es Hinweise auf Fast Retransmit?
- Welche Richtung sendet die großen Datenmengen?
- Was ist durch diesen Capture belegbar?
- Was wäre als Ursache noch nicht ausreichend belegt?

## Lab-Netz

```text
172.28.60.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.60.100` | Client |
| `lab-web-loss` | `172.28.60.10` | Webserver mit absichtlichem Paketverlust |

## Erwartung

Der Download erfolgt per HTTP von:

```text
http://172.28.60.10/bigfile.bin
```

In der Lab-Umgebung ist absichtlicher Paketverlust eingebaut.

In einer echten Analyse würdest du das aber nicht vorher wissen.

Deshalb muss die Bewertung vorsichtig formuliert werden.
