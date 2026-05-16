# wwca

`wwca` ist ein kleines lokales Hilfswerkzeug für den Kurs.

Aktuell unterstützt es:

- Quizzes auflisten
- Quizfragen validieren
- Quizzes interaktiv ausführen
- Modulprüfungen auflisten
- Modulprüfungen validieren
- Modulprüfungen interaktiv ausführen
- Fortschritt lokal speichern
- Fortschritt anzeigen
- Fortschritt exportieren

## Beispiele

```bash
python3 tools/wwca/wwca.py quiz list
python3 tools/wwca/wwca.py quiz validate
python3 tools/wwca/wwca.py quiz run foundation
python3 tools/wwca/wwca.py quiz run basic --limit 10 --shuffle

python3 tools/wwca/wwca.py exam list
python3 tools/wwca/wwca.py exam validate
python3 tools/wwca/wwca.py exam run module-basic

python3 tools/wwca/wwca.py progress
```

Wrapper:

```bash
tools/wwca/wwca quiz list
tools/wwca/wwca exam run wca-practice-exam-01
```

## Fortschritt

Der Fortschritt wird lokal gespeichert:

```text
~/.local/share/wireshark-wca-de/progress.json
```
