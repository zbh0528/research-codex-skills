---
name: academic-reply-letter
description: Draft, revise, diagnose, and polish any academic reviewer-response material, including response letters, rebuttals, point-by-point replies, editor replies, revised-response addenda, and existing reply-letter optimization in DOCX/TEX/text. Use whenever the user provides reviewer/editor comments, asks how to respond to comments, asks to improve an existing response, or asks to make the tone more professional, restrained, accurate, humble, concise, or less AI-like.
---

# Academic Reply Letter

## Core Standard

This skill is global for academic review-response work. It is not tied to any one manuscript, journal, project, or research topic.

Write replies as a careful author, not as a promotional agent. The tone should be courteous first, then specific, restrained, and accurate. Every response must answer the exact comment, state what changed or why a change was not made, and avoid overclaiming.

Prefer short, concrete replies. Use longer responses only when a reviewer raises a methodological challenge, fairness concern, missing experiment, or modeling assumption.

Trigger this skill whenever the user asks to draft, revise, polish, diagnose, compare, or update academic responses to editors or reviewers.

Academic reply-letter convention matters: each answer should normally begin with `Response: Thank you...` or `Response: Thanks...`. Do not remove this courtesy opening merely to reduce repetition. The goal is not to eliminate politeness; the goal is to avoid empty, inflated, or repetitive content after the polite opening.

When the revised manuscript uses colored text to mark changes, each response should guide the reviewer to that convention. For the current preferred convention, mention that the corresponding revisions are marked in blue in the revised manuscript. This reminder should be attached to the concrete change location rather than inserted as an isolated formulaic sentence.

For user review, every English response in a reply letter should be followed by a gray Chinese audit block unless the user explicitly says not to include it. The block contains:
1. `中文意见：` a concise Chinese rendering of the corresponding reviewer/editor comment.
2. `回复意见中文版：` a faithful Chinese rendering of the English response.

The Chinese audit block is for internal checking and should be visually distinguishable from the formal English response. In DOCX files, use gray font for the Chinese audit block. In Markdown/text drafts, wrap the Chinese audit block in an HTML span or otherwise mark it clearly as gray/internal review text if the output format supports styling.

## Workflow

1. Split the editor/reviewer text into individual actionable comments.
2. For each comment, classify its type using the categories below.
3. Build a traceability record before drafting or polishing the response:
   - `Comment`: the exact reviewer/editor concern.
   - `Required action`: clarification, experiment, comparison, limitation, formatting correction, etc.
   - `Manuscript evidence`: section, paragraph, equation, table, figure, appendix, or marked revision that actually addresses the concern.
   - `Status`: `complete`, `partial`, `pending`, `missing`, or `scoped/deferred`.
   - `Allowed wording`: completed-tense wording, provisional wording, or limitation wording.
4. Apply the evidence rule: no evidence, no completed claim. A response may say that a revision "has been added" only when the manuscript evidence is available. If the action is not complete, use provisional wording only in an internal draft, or mark the item as a manuscript/reply-letter to-do.
5. Draft a direct response with three parts when applicable: a courteous `Response: Thank you/Thanks...` opening, the revision or rationale, and where the change appears.
6. When manuscript revisions are color-marked, state that the relevant changes are marked in blue in the revised manuscript, preferably together with the section/table/figure location.
7. After each English response, add the gray Chinese audit block with `中文意见：` and `回复意见中文版：`, unless the user explicitly requests English-only output.
8. Ensure every numbered or bullet comment has a visible response. Do not hide unanswered comments inside broad combined replies unless the user explicitly asks for a combined response.
9. Remove repetitive openings, unsupported claims, and AI-like filler before finalizing.

## Evidence and Status Rules

Reviewer responses must be tied to the actual manuscript state, not to intended revisions. This is especially important when the user provides a revised manuscript, marked-up TEX, tables, figures, or a partially completed experiment.

Use these statuses internally:

- `complete`: the manuscript or supplementary file already contains the change. Completed-tense wording is allowed.
- `partial`: the manuscript contains a related change, but the reviewer concern is not fully addressed. The response must be narrowed, and a to-do should be flagged.
- `pending`: data, figures, tables, or text are planned but not yet finished. Use provisional wording only in an internal draft; do not use it in a final submission letter.
- `missing`: no corresponding manuscript evidence is available. Do not write a final response claiming the issue was addressed.
- `scoped/deferred`: the request is not implemented by design. Give a restrained rationale and add a limitation or future-work statement when appropriate.

### Anchor Requirement

Every nontrivial response must contain a concrete anchor. A concrete anchor is one of:

- a section/subsection name, such as `Section III-B` or `the Economic Performance Metric subsection`;
- a table or figure number/name, such as `Table IV`, `Fig. 2`, or `the hyper-parameter table in the Supplementary File`;
- an equation number or symbol group, such as `Eq. (5)` or the coordinate-mapping equations;
- a manuscript location plus marked change, such as `the blue-marked paragraph after Eq. (5)`;
- a pending action with exact missing artifact, such as `the RPSO/MjSO result table is still pending`.

Do not rely on broad phrases such as "engineering interpretability", "mathematical clarity", "benchmark coverage", or "scope alignment" unless they are immediately followed by a concrete anchor. If a response cannot name where the change appears, it must be marked as `pending`, `partial`, or `missing` in the internal audit block.

Use this default response structure:

`Response: Thank you for [comment/suggestion]. [Direct action or rationale]. Specifically, [anchor: section/table/figure/equation/appendix] now [what changed]. The corresponding revision is marked in blue in the revised manuscript.`

For incomplete work:

`Response: Thank you for [comment/suggestion]. This item is being completed by [exact action]. The missing artifact is [table/figure/result/parameter entry], and it will be marked in blue after [condition].`

When the response letter is being prepared for the user's internal review, the gray Chinese audit block should include the status and evidence when useful:

`中文意见：...[核验状态：已落实/部分落实/待落实/缺少证据/范围说明；证据：Section/Fig./Table/Appendix ...]`

`回复意见中文版：...`

When the response letter is being prepared for final submission, remove internal status notes unless the user explicitly wants to keep them. The final English response should still contain enough location information for the editor/reviewer to verify the change.

### Internal Draft Mode vs Final Submission Mode

Internal draft mode:
- Preserve existing text when the user asks to keep prior content.
- Add revised candidate responses in the requested color.
- Add gray Chinese audit blocks after candidate English responses.
- Explicitly mark `pending`, `partial`, and `missing` items in the Chinese audit text so the user can decide what to revise next.

Final submission mode:
- Do not leave duplicated old and revised English responses unless the journal form explicitly requires it.
- Consolidate each item into one polished response.
- Remove provisional language such as "is being added" or "will be updated" unless the submission is intentionally incomplete.
- Ensure all completed claims have manuscript anchors.

## Tone Rules

Use a courteous response opening for every item. Vary the noun after "Thank you" rather than deleting the thanks:
- "Response: Thank you for your comment."
- "Response: Thank you for your suggestion."
- "Response: Thank you for pointing out this issue."
- "Response: Thanks for your constructive comment."
- "Response: Thank you for this question."
- "Response: Thank you for kindly pointing out this error."

After the opening, move quickly to the action:
- "The corresponding description has been revised..."
- "The revised text now states that..."
- "This point is now clarified in the revised manuscript."
- "We acknowledge this limitation and have added it to the discussion."
- "This analysis is beyond the scope of the present study; however, the manuscript now clarifies..."
- "The relevant revision is marked in blue in [Section/Table/Fig./Appendix]."
- "The added explanation is shown in blue in the revised manuscript."

Avoid:
- responses that omit `Response: Thank you...` or `Response: Thanks...` unless the user explicitly asks for a different style;
- repetitive "We have..." sentence openings after the courtesy phrase;
- "important/helpful/valuable/insightful" in nearly every reply;
- "we agree" unless the response genuinely accepts a criticism;
- promotional language such as "clearly demonstrates", "superior", "robustly proves", or "significantly enhances" unless directly supported;
- defensive language such as "obviously", "as already explained", or "the reviewer misunderstood";
- future-tense claims for work not yet completed unless the user explicitly wants a provisional draft.

## Response Patterns

### Positive Summary With No Request

Keep it brief. Do not invent a revision.

`Response: Thank you very much for your summary of our work. No additional technical revision is required for this comment; the specific issues raised below are addressed point by point.`

### Minor Typo, Label, Figure, or Formatting Issue

Use one sentence when possible.

`Response: Thank you for kindly pointing out this error. The label has been corrected in the revised figure.`

For multiple small errors:

`Response: Thank you for identifying these errors. The listed typographical and notation issues have been corrected throughout the revised manuscript.`

### Request for Clarification

Answer the technical question first, then state the manuscript change.

`Response: Thank you for this question. [Direct explanation]. To avoid ambiguity, the corresponding description has been revised in [section/figure/table].`

### Missing Equation or Definition Explanation

`Response: Thank you for pointing out this ambiguity. In the revised manuscript, [symbol/equation] is now defined as [definition]. The surrounding text has also been expanded to clarify [role/operation].`

### Missing Experiment or Baseline

Completed:

`Response: Thank you for your suggestion. The comparison has been extended by adding [methods]. These algorithms were evaluated under the same [budget/data/settings], and the results are reported in [table/figure]. The corresponding revisions are marked in blue in the revised manuscript.`

Pending draft:

`Response: Thank you for your suggestion. The benchmark is being extended by adding [methods]. The corresponding tables and figures will be updated after the additional runs are complete.`

Representative method instead of exact requested method:

`Response: Thank you for your suggestion. We considered [requested family] and selected [method] as a recent representative of this line, while also adding [directly relevant method]. This choice balances methodological relevance with direct relevance to [application/domain].`

### Fairness, Reproducibility, or Parameter Tuning

`Response: Thank you for raising this concern. The revised manuscript now clarifies that all algorithms use the same [problem/data/model/budget]. Algorithm-specific parameters follow the original publications when available, and the adopted values are summarized in [table/appendix].`
When revisions are color-marked, add: `The relevant text and parameter table are marked in blue in the revised manuscript and Supplementary File.`

### Practical Significance

Accept the limited effect size and translate it carefully.

`Response: Thank you for this comment. The performance discussion has been revised to frame the improvement more carefully. The reported percentage gain is modest, but the corresponding [unit] difference can translate into [engineering/economic implication] at the project scale. The conclusion has also been moderated to avoid overstating the result.`
When revisions are color-marked, add: `These changes are marked in blue in the performance discussion and conclusion.`

### Scope or Generalization

`Response: Thank you for raising this point. The revised manuscript now states that the validation is limited to [cases/settings]. The conclusions are therefore framed as evidence under the tested conditions, not as a universal guarantee. Extensions to [broader setting] are identified as future work.`
When revisions are color-marked, add: `The corresponding limitation statement is marked in blue in the conclusion/future-work section.`

### Sensitivity Analysis or More Complex Modeling

If not doing it, give a methodological reason and add a limitation.

`Response: Thank you for this comment. The point is well taken. In this study, [parameter/model] is treated as part of the prescribed evaluation model and is kept fixed for all algorithms to ensure a controlled comparison. A full sensitivity analysis would shift the focus from [main contribution] to [uncertainty/modeling issue]. The limitation and possible extension have been added to the discussion.`

### Journal Scope

Position the contribution, not the application alone.

`Response: Thank you for this question. The manuscript has been revised to emphasize that the main contribution is [methodological/system-level contribution], with [application] serving as a representative testbed. This positioning aligns the work with [journal scope themes], including [theme 1], [theme 2], and [theme 3].`

## Final Quality Check

- Each editor/reviewer comment has a visible response.
- Each response starts with `Response: Thank you...` or `Response: Thanks...` unless the user explicitly requests another convention.
- Each English response is followed by a gray Chinese audit block containing `中文意见：` and `回复意见中文版：`, unless the user explicitly requests otherwise.
- Combined responses are used only for duplicated comments and still mention both comment numbers.
- The letter does not sound self-congratulatory.
- Limitations are acknowledged where reviewers question scope or assumptions.
- Claims match manuscript evidence and current experiment status.
- Every completed claim is backed by a concrete manuscript anchor such as a section, paragraph, equation, table, figure, or appendix.
- When the manuscript marks revisions in blue, each completed response guides the reviewer to the blue-marked change without using a detached, repetitive boilerplate sentence.
- No table, figure, result, experiment, baseline, or statistical conclusion is claimed as completed before the corresponding manuscript item exists.
- Pending language is acceptable only in internal drafts and must be removed before final submission.
- Broad umbrella claims such as "the manuscript has been substantially revised" are avoided unless followed by specific changes.
- Table and figure numbers are not fabricated. If a figure asset cannot be inspected, state the change more cautiously or flag it for verification.
- Repetitive openings and AI-like filler have been removed.
- If editing DOCX, preserve original content unless the user explicitly requests rewriting; mark additions in the requested color/style.
- If editing DOCX, newly inserted or rewritten response paragraphs must visually match the surrounding formal response paragraphs: same paragraph style, indentation, first-line indent, font family, font size, bold/italic state, line spacing, and before/after spacing. Only the requested marking color should differ. Chinese audit blocks should also use consistent indentation and spacing, with gray font unless the user requests another style.
