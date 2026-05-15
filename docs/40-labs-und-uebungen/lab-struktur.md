# Lab-Struktur

Alle Labs sollen möglichst einheitlich aufgebaut sein.

Das hilft Lernenden, Mitwirkenden und später auch automatisierten Checks.

## Standardstruktur

Ein Lab liegt unterhalb von `labs/<track>/<lab-id>/`.

Beispiel:

```text
labs/basic/lab-basic-020-dns-nxdomain/
├── README.md
├── scenario.md
├── tasks.md
├── hints.md
├── solution.md
├── metadata.yml
├── check.py
└── files/
    └── capture.pcapng
```

Nicht jedes Lab braucht von Anfang an alle Dateien.

Für einfache Labs reichen:

```text
README.md
scenario.md
tasks.md
hints.md
solution.md
metadata.yml
```

## Dateien

| Datei | Zweck |
|---|---|
| `README.md` | Einstieg, Ziel, Voraussetzungen, Ablauf |
| `scenario.md` | Ausgangslage und Problemstellung |
| `tasks.md` | konkrete Aufgaben |
| `hints.md` | gestufte Hinweise |
| `solution.md` | Musterlösung mit Belegen |
| `metadata.yml` | maschinenlesbare Lab-Informationen |
| `check.py` | optionaler automatisierter Check |
| `files/` | Lab-Dateien, z. B. PCAPs oder Konfigurationen |

## Lab-ID

Lab-IDs sollen eindeutig und sprechend sein.

Format:

```text
lab-<track>-<nummer>-<kurzer-name>
```

Beispiele:

```text
lab-foundation-001-first-capture
lab-basic-010-display-filter
lab-basic-020-dns-nxdomain
lab-basic-030-tcp-handshake
lab-advanced-010-tcp-retransmission
```

## Metadaten

Jedes Lab bekommt eine `metadata.yml`.

Beispiel:

```yaml
id: lab-basic-020-dns-nxdomain
title: "DNS NXDOMAIN analysieren"
track: basic
level: foundation
estimated_time: 30m
wca_objectives:
  - dns
  - display-filters
  - packet-details
tools:
  - wireshark
  - tshark
  - dig
requires:
  - lab-foundation-001-first-capture
outputs:
  - analysis-report
  - quiz
```

## Hinweise

Hinweise sollen gestuft sein.

Ein guter Hinweis hilft weiter, verrät aber nicht sofort die Lösung.

Beispiel:

```text
Hinweis 1:
Prüfe zuerst, ob DNS-Pakete im Capture vorhanden sind.

Hinweis 2:
Nutze den Filter `dns.flags.response == 1`.

Hinweis 3:
Der Response Code ist der Schlüssel zur Bewertung.
```

## Musterlösung

Eine gute Musterlösung enthält:

- verwendete Filter
- relevante Frame-Nummern
- Beobachtung
- Bewertung
- Einschränkungen
- nächsten sinnvollen Schritt

Nicht ausreichend:

```text
DNS ist kaputt.
```

Besser:

```text
Mit dem Filter `dns.flags.rcode == 3` wird Frame 42 gefunden.  
Dort beantwortet der DNS-Server die Anfrage nach `app.example.local` mit NXDOMAIN.  
Damit ist belegt, dass dieser DNS-Server den Namen nicht kennt.  
Nicht belegt ist, ob ein anderer DNS-Server den Namen auflösen könnte.
```

## WCA-Bezug

Jedes Lab soll einen WCA-Bezug haben.

Dabei geht es nicht darum, Prüfungsfragen zu kopieren.

Es geht darum, die geübte Kompetenz zu benennen.

Beispiele:

- Display Filter anwenden
- TCP Streams isolieren
- DNS Query und Response bewerten
- Capture-Punkt einordnen
- Analyse mit Frame-Nummern dokumentieren

## Qualitätskriterien

Ein gutes Lab ist:

- reproduzierbar
- nicht zu groß
- klar im Ziel
- fachlich korrekt
- mit Lösung nachvollziehbar
- nicht abhängig von produktiven Systemen
- ohne sensible Daten
- WCA-nah, aber ohne Exam-Dumps
