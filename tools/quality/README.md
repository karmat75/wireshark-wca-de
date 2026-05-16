# Quality Tools

Dieses Verzeichnis enthält kleine lokale Qualitätschecks für das Repository.

## Sammelcheck

Aus dem Repository-Root:

```bash
bash tools/quality/run_quality_checks.sh
```

## Einzelchecks

```bash
python3 tools/quality/check_repo_structure.py
python3 tools/quality/check_markdown_fences.py
python3 tools/wwca/wwca.py quiz validate
python3 tools/wwca/wwca.py exam validate
mkdocs build --strict
```

## Ziel

Die Checks sollen einfache Fehler früh finden:

- fehlende wichtige Verzeichnisse
- nicht geschlossene Markdown-Code-Fences
- ungültige Quizdateien
- ungültige Exam-Dateien
- MkDocs-Buildfehler

Sie ersetzen kein fachliches Review.
