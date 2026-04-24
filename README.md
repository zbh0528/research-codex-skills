# Research Codex Skills

Research-oriented Codex skills for academic writing, reviewer response, paper analysis, reproducibility, and scholarly communication.

This repository is a curated skill hub rather than a dump of prompts. Each skill is expected to be:

- reusable across projects;
- explicit about its trigger conditions;
- supported by concrete examples or validation scripts when useful;
- careful about academic tone, evidence, and privacy;
- free of private manuscripts, reviewer letters, DOCX files, LaTeX sources, BibTeX files, and unpublished data.

## Available Skills

| Skill | Purpose | Status |
| --- | --- | --- |
| [`academic-reply-letter`](skills/academic-reply-letter/SKILL.md) | Draft, audit, and polish point-by-point academic response letters with evidence-linked manuscript anchors and bilingual internal audit blocks. | Ready |
| [`scientific-english-optimizer`](skills/scientific-english-optimizer/SKILL.md) | Polish scientific manuscript English by improving logic, precision, concision, and claim discipline without exposing author-specific writing sources. | Ready |

## Skill Design Standard

The current standard is built around one principle:

> No manuscript evidence, no completed claim.

A reviewer response should not merely say that the manuscript was improved. It should identify what changed, where it changed, whether the item is complete or pending, and how the reviewer can verify the marked revision.

For the `academic-reply-letter` skill, this means:

- each response starts with `Response: Thank you...` or `Response: Thanks...`;
- completed claims point to a section, equation, table, figure, appendix, or other concrete manuscript anchor;
- pending experiments, figures, tables, or baselines are not written as completed work;
- blue-marked manuscript revisions are explicitly mentioned when applicable;
- internal Chinese audit blocks can be added in gray after English responses;
- DOCX insertions must visually match the surrounding response-letter formatting.

See [docs/academic-reply-letter-design.md](docs/academic-reply-letter-design.md) for the design rationale.

The `scientific-english-optimizer` skill follows the same privacy-first standard. It exposes general scientific-writing principles rather than private corpora, identifiable author styles, or source-specific writing fingerprints. See [docs/scientific-english-optimizer-design.md](docs/scientific-english-optimizer-design.md).

## Install a Skill

Copy a skill folder into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/academic-reply-letter ~/.codex/skills/
cp -R skills/scientific-english-optimizer ~/.codex/skills/
```

Then restart Codex or reload skills.

## Validate

Run the repository-level skill check:

```bash
python3 scripts/validate_skill.py
```

Run the privacy scan before publishing new skills:

```bash
python3 scripts/privacy_scan.py
```

If you have a DOCX response letter and `python-docx` installed, run:

```bash
python3 scripts/audit_docx_reply_letter.py /path/to/reply_letter.docx
```

The DOCX audit checks response prefixes, candidate-response audit blocks, blue-revision guidance, and basic formatting consistency for inserted response paragraphs.

## Privacy Boundary

This repository intentionally does not include real manuscripts, reviewer reports, response letters, DOCX files, PDFs, `.tex`, `.bib`, or unpublished research data. Examples are anonymized and demonstrate structure only.

## Roadmap

Planned research skills may include:

- LaTeX manuscript consistency checker;
- academic translation and polishing workflow;
- related-work synthesis skill;
- reproducible experiment-report skill;
- paper-to-WeChat research communication skill.
