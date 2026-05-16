# Modulprüfungen

Modulprüfungen sind der nächste Schritt nach einzelnen Quizfragen.

Sie ziehen Fragen aus vorhandenen Fragepools und simulieren eine fokussierte Prüfungssituation.

## Ziel

Modulprüfungen sollen helfen:

- Kursabschnitte gezielt zu wiederholen
- Wissenslücken sichtbar zu machen
- prüfungsähnlicher zu üben
- Erklärungen erst am Ende zu sehen
- Fortschritt lokal zu speichern
- Fragen aus mehreren Pools zu mischen

## Speicherort

```text
quizzes/exams/
```

Aktuelle Dateien:

```text
quizzes/exams/foundation-check.yml
quizzes/exams/module-basic.yml
quizzes/exams/module-advanced.yml
quizzes/exams/wca-practice-exam-01.yml
```

## Aktuelle Prüfungen

| Prüfung | Fragen | Bestehensgrenze | Inhalt |
|---|---:|---:|---|
| Foundation Check | 10 | 80 % | Foundation |
| Basic Module | 20 | 80 % | Foundation + Basic |
| Advanced Module | 20 | 80 % | Basic + Advanced |
| WCA Practice Exam 01 | 30 | 80 % | gemischt |

## Exam auflisten

```bash
python3 tools/wwca/wwca.py exam list
```

## Exam validieren

```bash
python3 tools/wwca/wwca.py exam validate
```

## Exam starten

```bash
python3 tools/wwca/wwca.py exam run module-basic
```

## Exam-Dateiformat

Beispiel:

```yaml
id: module-basic
title: "Basic Module Exam"
description: "Modulprüfung zum Basis-Kurs."
pass_score: 80
time_limit_minutes: 45
shuffle: true
sections:
  - pool: foundation
    count: 4
  - pool: basic
    count: 16
```

## Unterschied Quiz und Exam

| Quiz | Exam |
|---|---|
| Lernmodus | Prüfungsmodus |
| Erklärung nach jeder Frage | Erklärung am Ende |
| optional limit/shuffle per CLI | über YAML definiert |
| gut zum Wiederholen | gut zum Prüfen |
| meist ein Pool | mehrere Pools möglich |

## Keine echte WCA-Simulation

Die Modulprüfungen sind prüfungsnah, aber noch keine vollständige WCA-Simulation.

Dafür fehlen noch:

- mehr Fragen
- PCAP-basierte Fragen
- Zeitdruck mit hartem Timer
- stärkere Objective-Abdeckung
- automatische Auswertung nach Lernziel
- echte gemischte Probeprüfungen mit größerem Umfang

## Empfehlung

Nutze die Modulprüfungen erst, nachdem du die zugehörigen Kapitel und Labs bearbeitet hast.

Guter Ablauf:

1. Kapitel lesen
2. Lab bearbeiten
3. Quiz im Lernmodus machen
4. Fehler nacharbeiten
5. Modulprüfung starten
6. Ergebnis prüfen
7. falsche Themen gezielt wiederholen

## Merksatz

> Ein Quiz erklärt dir, was du noch nicht verstanden hast.  
> Eine Modulprüfung zeigt dir, ob du es unter prüfungsnäheren Bedingungen anwenden kannst.
