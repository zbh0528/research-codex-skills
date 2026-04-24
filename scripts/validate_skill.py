#!/usr/bin/env python3
"""Repository-level validation for the academic-reply-letter skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "academic-reply-letter" / "SKILL.md"


REQUIRED_PHRASES = [
    "No evidence, no completed claim",
    "Response: Thank you",
    "Response: Thanks",
    "中文意见：",
    "回复意见中文版：",
    "marked in blue",
    "Anchor Requirement",
    "If editing DOCX",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def main() -> None:
    if not SKILL.exists():
        fail(f"missing {SKILL.relative_to(ROOT)}")

    text = SKILL.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)

    if frontmatter.get("name") != "academic-reply-letter":
        fail("frontmatter name must be academic-reply-letter")
    if "description" not in frontmatter or len(frontmatter["description"]) < 80:
        fail("frontmatter description is missing or too short")

    text_lower = text.lower()
    missing = [phrase for phrase in REQUIRED_PHRASES if phrase.lower() not in text_lower]
    if missing:
        fail("missing required phrases: " + ", ".join(missing))

    print("OK: skill structure and core rules validated")


if __name__ == "__main__":
    main()
