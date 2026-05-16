# Quality Tools

Dieses Verzeichnis enthält kleine lokale Qualitätschecks für das Repository.

## Sammelcheck

Aus dem Repository-Root:

```bash
bash tools/quality/run_quality_checks.sh
```

## Als Pre-Commit-Hook aktivieren

Aus dem Repository-Root:

```bash
bash tools/quality/install_git_hooks.sh
```

Danach laufen die Quality Checks automatisch bei jedem `git commit`.

Hinweis: Git-Hooks sind lokal. Für verbindliche Durchsetzung im Team sollte zusätzlich CI mit Pflicht-Statuschecks genutzt werden.

## Teamweit erzwingen (GitHub)

In GitHub unter `Settings -> Branches` für `main` eine Branch-Protection-Regel setzen und mindestens aktivieren:

- `Require a pull request before merging`
- `Require status checks to pass before merging`
- Pflichtcheck: `Quality Checks / quality`

So ist der Check nicht nur lokal, sondern auch vor jedem Merge verbindlich.

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
