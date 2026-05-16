#!/usr/bin/env bash
set -euo pipefail

echo "== Repository structure =="
python3 tools/quality/check_repo_structure.py

echo
echo "== Markdown fences =="
python3 tools/quality/check_markdown_fences.py

echo
echo "== Quiz validation =="
python3 tools/wwca/wwca.py quiz validate

echo
echo "== Exam validation =="
python3 tools/wwca/wwca.py exam validate

echo
echo "== MkDocs build =="
mkdocs build --strict

echo
echo "All quality checks passed."
