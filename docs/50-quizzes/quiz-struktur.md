# Quiz-Struktur

Die Quizfragen werden als YAML-Dateien abgelegt.

Dadurch bleiben sie:

- versionierbar
- gut lesbar
- später maschinenlesbar
- unabhängig von einem zentralen Server
- einfach erweiterbar

## Speicherorte

```text
quizzes/
├── questions/
│   ├── foundation.yml
│   └── basic.yml
├── exams/
│   └── .gitkeep
└── objectives/
    └── .gitkeep
```

## Grundstruktur

Eine Quizdatei besteht aus Metadaten und Fragen.

```yaml
id: foundation
title: "Foundation Quiz"
description: "Wiederholung zu Umgebung, Oberfläche und TShark."
questions:
  - id: q-foundation-001
    type: single-choice
    objective: wireshark-ui
    question: "Welche Aussage beschreibt einen Display Filter korrekt?"
    answers:
      - text: "Er verändert nur die Anzeige vorhandener Pakete."
        correct: true
      - text: "Er entscheidet, welche Pakete überhaupt mitgeschnitten werden."
        correct: false
    explanation: "Display Filter wirken auf bereits vorhandene Pakete."
    references:
      - docs/10-basis-kurs/02-display-filter.md
```

## Fragetypen

Aktuell vorgesehen:

| Typ | Zweck |
|---|---|
| `single-choice` | genau eine richtige Antwort |
| `multiple-choice` | mehrere richtige Antworten |
| `true-false` | schnelle Wahr/Falsch-Prüfung |
| `ordering` | Reihenfolge herstellen |
| `matching` | Begriffe zuordnen |
| `filter-task` | passenden Filter auswählen |
| `pcap-question` | Frage zu einem Capture beantworten |
| `short-answer` | kurze freie Antwort |
| `report-task` | Analysebericht schreiben |

## Pflichtfelder

Jede Frage sollte enthalten:

| Feld | Bedeutung |
|---|---|
| `id` | eindeutige Frage-ID |
| `type` | Fragetyp |
| `objective` | Lernziel |
| `question` | Frage |
| `answers` | Antwortoptionen bei Auswahlfragen |
| `explanation` | Erklärung der richtigen Lösung |
| `references` | passende Kurskapitel |

## Qualität guter Fragen

Gute Fragen prüfen nicht nur Definitionen.

Sie prüfen:

- Verständnis
- Einordnung
- Belegbarkeit
- typische Fehlinterpretationen
- Analyseverhalten

Schlecht:

```text
Was ist TCP?
```

Besser:

```text
Im Capture sind mehrere SYN-Pakete vom Client sichtbar, aber kein SYN/ACK. Welche Aussage ist durch diesen Capture belegbar?
```

## WCA-nahe Formulierung

WCA-nahe Fragen sollten häufig szenariobasiert sein:

- kurze Ausgangslage
- konkrete Beobachtung
- mehrere plausible Antworten
- eine oder mehrere belegbare Aussagen

Wichtig:

> Die richtige Antwort sollte nicht nur technisch stimmen, sondern durch die Beobachtung belegbar sein.

## Lokale Auswertung

Später soll ein lokales Tool die YAML-Fragen ausführen.

Geplante Befehle:

```bash
wwca quiz run foundation
wwca quiz run basic
wwca exam start module-basic
wwca progress
```

Bis dahin dienen die YAML-Dateien als strukturierte Fragensammlung.
