#!/usr/bin/env python3
"""Audit a DOCX academic response letter for common reply-letter issues.

This script is intentionally conservative. It does not judge scientific content;
it checks mechanical issues that often make a response letter look unfinished:

- response paragraphs not starting with the required courtesy convention;
- missing gray Chinese audit blocks after English responses;
- completed-looking responses that do not guide reviewers to blue revisions;
- inserted colored paragraphs whose indentation/font differs from nearby formal responses.
"""

from __future__ import annotations

import sys
from pathlib import Path


try:
    from docx import Document
except ImportError as exc:  # pragma: no cover - environment dependent
    raise SystemExit(
        "python-docx is required. Install it with: python3 -m pip install python-docx"
    ) from exc


RESPONSE_PREFIXES = ("Response: Thank you", "Response: Thanks")
CHINESE_PREFIXES = ("中文意见：", "回复意见中文版：")
ORANGE_MARKS = {"FF6600", "FFA500", "ED7D31"}


def color_hex(run) -> str | None:
    if run.font.color is not None and run.font.color.rgb is not None:
        return str(run.font.color.rgb)
    return None


def is_colored_response(paragraph) -> bool:
    text = paragraph.text.strip()
    if not text.startswith("Response:"):
        return False
    colors = {color_hex(run) for run in paragraph.runs}
    return bool(colors - {None})


def is_candidate_response(paragraph) -> bool:
    text = paragraph.text.strip()
    if not text.startswith("Response:"):
        return False
    colors = {color_hex(run) for run in paragraph.runs}
    return bool(colors & ORANGE_MARKS)


def paragraph_signature(paragraph) -> tuple:
    pf = paragraph.paragraph_format
    first_run = next((run for run in paragraph.runs if run.text.strip()), None)
    return (
        paragraph.style.name,
        pf.left_indent,
        pf.first_line_indent,
        pf.space_before,
        pf.space_after,
        pf.line_spacing,
        first_run.font.name if first_run else None,
        first_run.font.size if first_run else None,
        first_run.bold if first_run else None,
        first_run.italic if first_run else None,
    )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: audit_docx_reply_letter.py /path/to/reply_letter.docx")

    path = Path(sys.argv[1]).expanduser()
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    doc = Document(path)
    paragraphs = [p for p in doc.paragraphs if p.text.strip()]

    issues: list[str] = []
    colored_response_indices: list[int] = []
    all_response_count = 0

    for i, paragraph in enumerate(paragraphs):
        text = paragraph.text.strip()
        if text.startswith("Response:"):
            all_response_count += 1
            if is_candidate_response(paragraph):
                colored_response_indices.append(i)
                if not text.startswith(RESPONSE_PREFIXES):
                    issues.append(f"P{i}: candidate response does not start with required courtesy form")
                if "blue" not in text.lower() and "no separate manuscript change" not in text.lower():
                    issues.append(f"P{i}: candidate response does not point to blue-marked revision")

    for i in colored_response_indices:
        next_texts = [paragraphs[j].text.strip() for j in range(i + 1, min(i + 3, len(paragraphs)))]
        if not any(text.startswith("中文意见：") for text in next_texts):
            issues.append(f"P{i}: missing Chinese comment audit block after colored response")
        if not any(text.startswith("回复意见中文版：") for text in next_texts):
            issues.append(f"P{i}: missing Chinese response audit block after colored response")

    # Compare colored response formatting with the first non-colored formal response when possible.
    reference = None
    for paragraph in paragraphs:
        text = paragraph.text.strip()
        if text.startswith("Response:") and not is_candidate_response(paragraph):
            reference = paragraph_signature(paragraph)
            break

    if reference is not None:
        for i in colored_response_indices:
            signature = paragraph_signature(paragraphs[i])
            # Ignore font color by construction; compare layout/font basics only.
            if signature[:6] != reference[:6]:
                issues.append(f"P{i}: colored response paragraph layout differs from formal responses")

    print(f"Responses: {all_response_count}")
    print(f"Colored candidate responses: {len(colored_response_indices)}")

    if issues:
        print("Issues:")
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)

    print("OK: DOCX reply-letter audit passed")


if __name__ == "__main__":
    main()
