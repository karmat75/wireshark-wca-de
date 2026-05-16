#!/usr/bin/env bash
set -euo pipefail

if [[ -x .venv/bin/python ]]; then
	PYTHON=".venv/bin/python"
else
	PYTHON="python3"
fi

if [[ -x .venv/bin/mkdocs ]]; then
	MKDOCS=".venv/bin/mkdocs"
else
	MKDOCS="mkdocs"
fi

if ! command -v "$PYTHON" >/dev/null 2>&1; then
	echo "Fehler: Python wurde nicht gefunden ($PYTHON)."
	exit 1
fi

echo "== Repository structure =="
"$PYTHON" tools/quality/check_repo_structure.py

echo
echo "== Markdown fences =="
"$PYTHON" tools/quality/check_markdown_fences.py

echo
echo "== Quiz validation =="
"$PYTHON" tools/wwca/wwca.py quiz validate

echo
echo "== Exam validation =="
"$PYTHON" tools/wwca/wwca.py exam validate

echo
echo "== MkDocs build =="
if ! command -v "$MKDOCS" >/dev/null 2>&1; then
	echo "Fehler: mkdocs wurde nicht gefunden. Installiere die Abhaengigkeiten, z. B. mit:"
	echo "  python3 -m pip install -r requirements.txt"
	exit 1
fi
"$MKDOCS" build --strict

echo
echo "All quality checks passed."
