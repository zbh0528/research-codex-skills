# Design Principles

This skill is built around response credibility rather than surface fluency.

## 1. Courtesy First, Then Evidence

Academic response letters conventionally begin with a courteous acknowledgment. The skill preserves that convention, but prevents the remainder of the response from becoming repetitive or inflated.

Good:

```text
Response: Thank you for pointing out this ambiguity. The paragraph after Eq. (5) now explains the numerator, denominator, and cost terms. The corresponding revision is marked in blue in the revised manuscript.
```

Weak:

```text
Response: Thank you for your valuable comment. The manuscript has been substantially improved.
```

## 2. No Evidence, No Completed Claim

The skill distinguishes five states:

- `complete`: the manuscript contains the change.
- `partial`: the manuscript contains related text, but the concern is not fully resolved.
- `pending`: the result, figure, table, or text is planned but unfinished.
- `missing`: no supporting manuscript evidence exists.
- `scoped/deferred`: the request is not implemented by design.

Completed-tense wording is only allowed for `complete` items.

## 3. Anchors Over Umbrella Claims

The response should guide reviewers to exact manuscript locations:

- section or subsection;
- table or figure;
- equation or symbol definition;
- appendix or supplementary file;
- explicit pending artifact.

Broad phrases such as "engineering interpretability" or "mathematical clarity" are acceptable only when followed by concrete anchors.

## 4. Internal Audit and Final Submission Are Different

Internal audit mode may preserve prior responses, add orange revised candidates, and include gray Chinese audit blocks.

Final submission mode should consolidate each item into one polished response and remove pending/internal notes unless intentionally retained.

## 5. DOCX Formatting Is Part of the Deliverable

In response letters, inconsistent indentation, font size, font family, or paragraph spacing makes the revision look careless. DOCX edits should inherit the surrounding formal response style, with only the requested highlight color changed.
