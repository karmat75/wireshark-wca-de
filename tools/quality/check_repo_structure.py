#!/usr/bin/env python3
"""
Check that important repository directories and files exist.

This is a lightweight sanity check, not a full repository validator.
"""

from __future__ import annotations

from pathlib import Path


REQUIRED_PATHS = [
    "mkdocs.yml",
    "docs",
    "docs/index.md",
    "docs/00-orientierung",
    "docs/01-lern-und-uebungsumgebung",
    "docs/02-linux-grundlagen-fuer-den-kurs",
    "docs/03-wireshark-erster-kontakt",
    "docs/10-basis-kurs",
    "docs/20-advanced-kurs",
    "docs/30-wca-vorbereitung",
    "docs/40-labs-und-uebungen",
    "docs/50-quizzes",
    "docs/60-pcap-challenges",
    "docs/90-referenz",
    "labs",
    "challenges",
    "docker/compose",
    "quizzes/questions",
    "quizzes/exams",
    "tools/wwca/wwca.py",
    "templates",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> int:
    root = repo_root()
    missing = []

    for rel in REQUIRED_PATHS:
        path = root / rel
        if not path.exists():
            missing.append(rel)

    if missing:
        print("Repository structure check failed:")
        for rel in missing:
            print(f"  - missing: {rel}")
        return 1

    print("Repository structure check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
