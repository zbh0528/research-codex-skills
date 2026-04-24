#!/usr/bin/env python3
"""Repository-level validation for research Codex skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


GLOBAL_REQUIRED_FRONTMATTER = ["name", "description"]

REPLY_LETTER_REQUIRED_PHRASES = [
    "No evidence, no completed claim",
    "Response: Thank you",
    "Response: Thanks",
    "中文意见：",
    "回复意见中文版：",
    "marked in blue",
    "Anchor Requirement",
    "If editing DOCX",
]

SCIENTIFIC_ENGLISH_REQUIRED_PHRASES = [
    "Preserve the user's technical meaning",
    "not an author-style imitation tool",
    "claim discipline",
    "Precision Pass",
    "No datasets, metrics, baselines, statistical tests, citations, or novelty claims are invented",
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
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        fail("no skills found under skills/*/SKILL.md")

    for skill in skill_files:
        text = skill.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)

        for key in GLOBAL_REQUIRED_FRONTMATTER:
            if key not in frontmatter:
                fail(f"{skill.relative_to(ROOT)} missing frontmatter field: {key}")
        if len(frontmatter["description"]) < 80:
            fail(f"{skill.relative_to(ROOT)} description is too short")

        text_lower = text.lower()
        name = frontmatter["name"]
        if name == "academic-reply-letter":
            required = REPLY_LETTER_REQUIRED_PHRASES
        elif name == "scientific-english-optimizer":
            required = SCIENTIFIC_ENGLISH_REQUIRED_PHRASES
        else:
            required = []

        missing = [phrase for phrase in required if phrase.lower() not in text_lower]
        if missing:
            fail(f"{skill.relative_to(ROOT)} missing required phrases: " + ", ".join(missing))

    print(f"OK: {len(skill_files)} skill(s) validated")


if __name__ == "__main__":
    main()
