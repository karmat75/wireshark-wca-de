# Paket 39: Qualitätssicherung und CI

Dieses Paket ergänzt das Repository um lokale Qualitätschecks und eine GitHub Actions Pipeline.

## Enthaltene Dateien

```text
mkdocs.yml
docs/90-referenz/index.md
docs/90-referenz/qualitaetssicherung-und-ci.md
.github/workflows/ci.yml
tools/quality/README.md
tools/quality/check_markdown_fences.py
tools/quality/check_repo_structure.py
tools/quality/run_quality_checks.sh
```

## Ziel

Der Kurs ist inzwischen groß genug, dass einfache Qualitätsprüfungen wichtig werden.

Dieses Paket ergänzt:

- lokale Qualitätschecks
- Prüfung der Markdown-Code-Fences
- Prüfung wichtiger Repository-Verzeichnisse
- MkDocs Build in CI
- Quiz- und Exam-Validierung in CI
- reproduzierbare Befehle für lokale Prüfung
- GitHub Actions Workflow für Pull Requests und Pushes

Damit wird aus „sieht lokal gut aus“ ein sauberer, wiederholbarer Prüfpfad.
