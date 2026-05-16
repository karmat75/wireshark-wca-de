#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ ! -f .githooks/pre-commit ]]; then
  echo "Fehler: .githooks/pre-commit wurde nicht gefunden."
  exit 1
fi

chmod +x .githooks/pre-commit
git config core.hooksPath .githooks

echo "Git-Hooks sind aktiviert (core.hooksPath=.githooks)."
echo "Pre-Commit-Check: tools/quality/run_quality_checks.sh"
