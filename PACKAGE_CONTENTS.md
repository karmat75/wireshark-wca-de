# Paket 23: Lokales Quiz-Tool

Dieses Paket ergänzt den Kurs um ein erstes lokales Quiz-Tool.

## Enthaltene Dateien

```text
mkdocs.yml
docs/50-quizzes/index.md
docs/50-quizzes/lokales-quiz-tool.md
tools/README.md
tools/wwca/README.md
tools/wwca/wwca.py
tools/wwca/wwca
```

## Ziel

Mit diesem Paket werden die YAML-Fragen aus `quizzes/questions/` erstmals praktisch nutzbar:

- verfügbare Quizzes auflisten
- Fragen-Dateien technisch validieren
- Quiz interaktiv im Terminal ausführen
- Fragen optional mischen oder begrenzen
- Ergebnisse lokal speichern
- Fortschritt anzeigen
- Fortschritt exportieren

Das Tool speichert Fortschritt lokal unter:

```text
~/.local/share/wireshark-wca-de/progress.json
```

Es benötigt Python 3 und PyYAML. PyYAML ist in vielen MkDocs-Umgebungen bereits als Abhängigkeit vorhanden.
