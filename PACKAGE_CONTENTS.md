# Paket 25: Modulprüfungen und Exam-Modus

Dieses Paket ergänzt den Quizbereich um Modulprüfungen und erweitert das lokale Tool `wwca`.

## Enthaltene Dateien

```text
mkdocs.yml
docs/50-quizzes/index.md
docs/50-quizzes/lokales-quiz-tool.md
docs/50-quizzes/modulpruefungen.md
quizzes/exams/foundation-check.yml
quizzes/exams/module-basic.yml
quizzes/exams/module-advanced.yml
quizzes/exams/wca-practice-exam-01.yml
tools/wwca/README.md
tools/wwca/wwca.py
```

## Ziel

Mit diesem Paket entsteht der nächste Schritt von Quizfragen zu prüfungsnaher Wiederholung:

- Modulprüfungen definieren
- Fragen aus bestehenden Quiz-Pools ziehen
- Exam-Modus im lokalen Tool
- Fragen mischen
- Erklärungen erst am Ende anzeigen
- Bestehensgrenze pro Prüfung
- einfache Zeitlimit-Information
- Fortschritt getrennt nach Quiz und Exam speichern

Das ist noch keine vollständige echte Prüfungssimulation, aber ein solider nächster Schritt.
