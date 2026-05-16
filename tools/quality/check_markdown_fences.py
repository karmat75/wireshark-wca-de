#!/usr/bin/env python3
"""
Check Markdown files for unclosed fenced code blocks.

This is intentionally simple. It catches common mistakes such as opening
``` without closing it again.

It does not try to be a full Markdown parser.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, List, Tuple


IGNORE_DIRS = {
    ".git",
    ".venv",
    "site",
    "__pycache__",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        yield path


def fence_marker(line: str) -> str | None:
    stripped = line.lstrip()

    if stripped.startswith("```"):
        return "```"

    if stripped.startswith("~~~"):
        return "~~~"

    return None


def check_file(path: Path) -> List[str]:
    errors: List[str] = []

    open_fence: str | None = None
    open_line: int | None = None

    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            marker = fence_marker(line)
            if marker is None:
                continue

            if open_fence is None:
                open_fence = marker
                open_line = number
                continue

            if marker == open_fence:
                open_fence = None
                open_line = None
                continue

    if open_fence is not None:
        errors.append(f"{path}: unclosed fence {open_fence!r} opened at line {open_line}")

    return errors


def main() -> int:
    root = repo_root()
    errors: List[str] = []

    for path in iter_markdown_files(root):
        errors.extend(check_file(path))

    if errors:
        print("Markdown fence check failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Markdown fence check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
