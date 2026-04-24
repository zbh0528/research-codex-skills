# Scientific English Optimizer Design

This skill is designed for research-manuscript English polishing without author-style imitation.

## Public Design Boundary

The public skill must not contain:

- real manuscript paragraphs;
- private reviewer reports or response letters;
- author names used as style sources;
- affiliation-specific writing fingerprints;
- publication lists used as a corpus;
- profile links, email addresses, or internal project references.

The skill should describe reusable writing behavior, not the source from which that behavior was learned.

## Core Editing Philosophy

The skill optimizes scientific prose in this order:

1. preserve technical meaning;
2. repair the logical chain;
3. calibrate claims against evidence;
4. make comparison targets explicit;
5. compress redundant wording;
6. polish grammar and sentence rhythm.

## Claim Discipline

Scientific polishing should not make the paper sound stronger than the evidence allows. Common replacements:

- `proves` -> `shows`, `indicates`, or `suggests`, depending on evidence;
- `is superior` -> `outperforms [baseline] in [metric] under [condition]`;
- `robust` -> `stable across [runs/scenarios]`, if such evidence exists;
- `significantly` -> use only with a statistical test or clearly quantified effect.

## Privacy Rule

Do not publish private corpora or identifiable writing-source notes. If a private version contains author-derived observations, convert them into neutral principles before committing.
