---
name: scientific-english-optimizer
description: Polish and rewrite scientific English for research manuscripts, including abstracts, introductions, related work, methods, experiments, results, conclusions, captions, highlights, and cover-letter-style summaries. Use when the user asks to improve SCI/IEEE/journal/conference manuscript English, strengthen logical flow, calibrate claims, translate Chinese research text into academic English, condense verbose writing, or make scientific prose clearer, more rigorous, and less promotional.
---

# Scientific English Optimizer

## Core Standard

Optimize scientific English by improving logic, precision, concision, and claim discipline before surface grammar. Preserve the user's technical meaning, notation, citations, variables, equations, labels, and experimental facts unless the user explicitly asks for substantive rewriting.

This skill is not an author-style imitation tool. Do not copy, mimic, or reproduce any living author's identifiable voice. Treat all style guidance as general scientific-writing practice.

## Workflow

1. Identify the section type: title, abstract, introduction, related work, method, experiment, result, conclusion, caption, highlight, or cover-letter-style summary.
2. Diagnose the rhetorical chain before editing:
   `problem -> limitation/gap -> proposed idea -> mechanism -> validation -> scoped implication`.
3. Repair macro-level issues first: unclear subject, missing contrast, weak novelty axis, unsupported overclaim, method/result mismatch, or loose paragraph order.
4. Sharpen technical expression: replace vague nouns with technical objects, quantify where facts are provided, and make comparison targets explicit.
5. Polish sentence-level English: tighten subjects and verbs, reduce noun piles, clarify antecedents, define acronyms once, and make transitions causal rather than decorative.
6. Return the polished text first. Add a short edit rationale only when it helps the user evaluate the change.

## Section Patterns

- Abstract: context/challenge -> specific limitation -> proposed method/model -> key mechanism -> validation setting -> measured or qualitative finding -> scoped implication.
- Introduction: broad importance -> persistent challenge -> limits of existing studies -> research objective -> proposed solution -> main contributions.
- Related work: organize by taxonomy or limitation, not by a flat author-by-author list; end each cluster with the unresolved issue that motivates the paper.
- Method: state the design objective first; define inputs, assumptions, variables, and constraints; explain each component by the limitation it addresses.
- Experiments/results: name datasets, benchmarks, baselines, metrics, and protocols; separate setup from findings; pair each claim with evidence.
- Conclusion: restate what was solved, by what mechanism, and under what evidence; avoid unsupported new claims.

## Writing Moves

- Open with a concrete research challenge rather than a generic field slogan.
- Use contrastive logic: "Although existing methods achieve X, they remain limited by Y under Z."
- Make novelty structural: identify whether the contribution is a new formulation, model, algorithm, mechanism, objective, taxonomy, theorem, dataset, or evaluation protocol.
- Explain mechanisms, not labels. Replace "an improved algorithm is proposed" with what information the algorithm uses, what operation changes, and why that addresses the limitation.
- Use restrained claim verbs. Prefer "outperforms under [metric/scenario]" to "is superior"; prefer "is competitive with" when the advantage is partial.
- Use enumerated contributions only when each item has a distinct technical object and evidence hook.
- Keep domain terms stable across the manuscript. Do not alternate among near-synonyms for core constructs.

## Precision Pass

Apply this pass after the logical structure is sound:

- Keep one sentence to one rhetorical function. Split sentences that mix context, gap, method, and result without clear hierarchy.
- Prefer precise technical subjects: use "fixed mutation strategies", "wake-model uncertainty", "population diversity", or "residency-time constraints" instead of "some problems", "many factors", or "the situation".
- Replace vague evaluations with scoped evidence: "performs well" -> "reduces RMSE on [dataset]" or "improves hypervolume under [scenario]".
- Delete low-information modifiers: "very", "quite", "obviously", "greatly", "good", "bad", "excellent", "many", and "various" unless they are quantified or technically defined.
- Convert bloated nominalizations into verbs: "the realization of optimization" -> "optimize"; "the improvement of accuracy" -> "improves accuracy".
- Avoid stacked nouns when relationships matter. Rewrite "wind farm yaw optimization algorithm performance improvement method" as "a method for improving yaw-optimization performance in wind farms".
- State comparison targets explicitly. Do not write "better"; write "higher than [baseline] in [metric]" or "more stable under [condition]".
- State scope limits. Prefer "under the tested scenarios" to an unrestricted claim about all possible settings.

Use this precision ladder when revising claims:

1. Object: What exactly is improved, modeled, predicted, controlled, or optimized?
2. Mechanism: What information, constraint, operator, model, or theorem causes the improvement?
3. Condition: Under what dataset, scenario, assumption, or system class?
4. Evidence: Which metric, baseline, proof, ablation, or experiment supports it?
5. Scope: What can be concluded without overclaiming?

## Language Transform Rules

- "This problem is very important" -> "This problem is critical for [application] because [specific consequence]."
- "Existing methods are not good" -> "Existing methods remain limited by [failure mode], especially under [condition]."
- "We propose a novel method" -> "This work proposes [method], which [mechanism] to [effect]."
- "The results are better" -> "The results show that [method] improves [metric] over [baseline] on [dataset/scenario]."
- "This paper has three contributions" -> "The main contributions are as follows: [object + novelty axis + validation hook]."
- "It is obvious that" -> remove it and state the evidence.
- "A lot of experiments" -> "Experiments on [number/type] benchmarks/scenarios..."

## Output Modes

- For short text, provide a polished version and optionally a concise edit rationale.
- For long manuscripts, work section by section and preserve headings, numbering, equations, citations, and labels.
- For Chinese-to-English academic rewriting, translate meaning first, then restructure into English scientific rhetoric; do not mirror Chinese sentence order when it weakens clarity.
- For title/abstract optimization, provide 2-3 alternatives only if the user asks for alternatives; otherwise provide one refined version.
- For claims that appear unsupported, mark them with a short note such as `[needs evidence]` rather than fabricating support.

## Final Quality Check

- Technical meaning, notation, citations, equations, and labels are preserved.
- Claims are calibrated to the evidence provided by the user.
- The rewritten text is more precise and concise, not merely more ornate.
- No datasets, metrics, baselines, statistical tests, citations, or novelty claims are invented.
- No identifiable author style, private corpus, personal name, affiliation, or source-specific writing fingerprint is exposed.
