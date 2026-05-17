# Quizzes

Dieser Bereich sammelt Wiederholungsfragen und Modulprüfungen.

Die Quizzes sind keine echten WCA-Prüfungsfragen.

Sie sind eigene Kursfragen, die helfen sollen, Wissen, Bedienung und Analysefähigkeit zu festigen.

## Ziel

Quizzes sollen helfen:

- Begriffe zu wiederholen
- typische Denkfehler zu erkennen
- Display Filter sicherer zu verwenden
- Protokolle besser einzuordnen
- Analysefragen prüfungsnah zu beantworten
- Lücken vor Labs und PCAP-Challenges sichtbar zu machen

## Aktuelle Quizbereiche

| Quiz | Inhalt | Datei |
|---|---|---|
| [Foundation-Quiz](foundation-quiz.md) | Umgebung, Wireshark-Oberfläche, TShark, Linux-Grundlagen | `quizzes/questions/foundation.yml` |
| [Basic-Quiz](basic-quiz.md) | Display Filter, Ethernet, ARP, IP, ICMP, UDP, DNS, DHCP, TCP | `quizzes/questions/basic.yml` |
| [Advanced-Quiz](advanced-quiz.md) | TCP Deep Dive, Performance, HTTP/TLS, Methodik, Security | `quizzes/questions/advanced.yml` |
| [Interface-Counter-Quiz](interface-counter-quiz.md) | Errors, Discards, Monitoring-Korrelation und Wireshark-Grenzen | `quizzes/questions/interface-counters.yml` |
| [WCA-Practice-Quiz](wca-practice-quiz.md) | gemischte szenariobasierte Fragen | `quizzes/questions/wca-practice.yml` |

## Modulprüfungen

Modulprüfungen ziehen Fragen aus vorhandenen Fragepools.

Siehe:

```text
docs/50-quizzes/modulpruefungen.md
```

Aktuell definiert:

| Exam | Zweck | Datei |
|---|---|---|
| Foundation Check | Grundlagenprüfung | `quizzes/exams/foundation-check.yml` |
| Basic Module | Basis-Kurs-Prüfung | `quizzes/exams/module-basic.yml` |
| Advanced Module | Advanced-Kurs-Prüfung | `quizzes/exams/module-advanced.yml` |
| WCA Practice Exam 01 | gemischte Probeprüfung | `quizzes/exams/wca-practice-exam-01.yml` |
| Interface Counter Module | Interface-Counter-Praxisblock | `quizzes/exams/module-interface-counters.yml` |

## Aktueller Umfang

```text
Foundation:    12 Fragen
Basic:         18 Fragen
Advanced:      20 Fragen
Interface:     12 Fragen
WCA Practice:  15 Fragen
Gesamt:        77 Fragen
```

## Lokales Quiz-Tool

Die YAML-Fragen können lokal im Terminal ausgeführt werden.

Beispiel:

```bash
python3 tools/wwca/wwca.py quiz list
python3 tools/wwca/wwca.py quiz run advanced --limit 10 --shuffle
python3 tools/wwca/wwca.py exam list
python3 tools/wwca/wwca.py exam run module-basic
```

## Keine Exam Dumps

!!! warning "Keine echten Prüfungsfragen"
    Dieser Kurs enthält keine echten WCA-Prüfungsfragen und keine Exam Dumps.  
    Die Fragen sind eigene Lernfragen, die auf Verständnis und Analysefähigkeit zielen.

## Geplante Ausbaustufen

| Stufe | Ziel |
|---|---|
| 1 | YAML-Fragen sammeln |
| 2 | einfache lokale Auswertung per Python |
| 3 | Modulprüfungen definieren |
| 4 | Fortschritt lokal speichern |
| 5 | PCAP-basierte Fragen einbinden |
| 6 | WCA-nahe Probeprüfung ausbauen |
