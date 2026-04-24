#!/usr/bin/env python3
"""Privacy-oriented repository scan for public research skills.

The default scan checks for common private-material markers without embedding
project-specific personal names in the public repository. For local stricter
checks, set RESEARCH_SKILLS_DENYLIST to a newline-separated denylist file.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TEXT_EXTENSIONS = {
    ".md",
    ".py",
    ".yml",
    ".yaml",
    ".txt",
    ".json",
}

FORBIDDEN_EXTENSIONS = {
    ".docx",
    ".pdf",
    ".tex",
    ".bib",
    ".zip",
}

GENERIC_PATTERNS = [
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"\b(distilled from|imitate|imitating|style of|writing style of)\b", re.I),
    re.compile(r"\b(supervisor|advisor|private corpus|internal corpus|unpublished manuscript)\b", re.I),
]


def iter_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__", ".venv", "venv"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def load_extra_denylist() -> list[str]:
    denylist_path = os.environ.get("RESEARCH_SKILLS_DENYLIST")
    if not denylist_path:
        return []
    path = Path(denylist_path).expanduser()
    if not path.exists():
        raise SystemExit(f"denylist file not found: {path}")
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    issues: list[str] = []
    extra_terms = load_extra_denylist()

    for path in iter_files():
        rel = path.relative_to(ROOT)
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            issues.append(f"{rel}: forbidden public-repo file type")
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {"LICENSE", ".gitignore"}:
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in GENERIC_PATTERNS:
            if pattern.search(text):
                issues.append(f"{rel}: matched privacy pattern {pattern.pattern}")
        lowered = text.lower()
        for term in extra_terms:
            if term.lower() in lowered:
                issues.append(f"{rel}: matched local denylist term")

    if issues:
        print("Privacy scan issues:")
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)

    print("OK: privacy scan passed")


if __name__ == "__main__":
    main()
