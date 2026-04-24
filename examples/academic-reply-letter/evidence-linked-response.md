# Evidence-Linked Response Example

This example is anonymized. It demonstrates the response structure rather than a field-specific answer.

## Reviewer Comment

The manuscript reports a small improvement over existing methods. Please explain why this magnitude is practically meaningful, and avoid overstating the conclusion.

## Weak Response

```text
Response: Thank you for your valuable comment. We have strengthened the discussion and improved the conclusion.
```

Why it is weak:

- It does not identify what changed.
- It does not point to a manuscript location.
- It claims improvement without evidence.
- It does not show whether the conclusion was moderated.

## Evidence-Linked Response

```text
Response: Thank you for this comment. The Performance Comparison subsection now interprets the reported improvement in application-scale terms by converting the objective-value gap into an estimated project-level effect. The first paragraph of the Conclusion also moderates the claim by describing the gain as modest but measurable under the tested setting, rather than as a broad guarantee. These revisions are marked in blue in the revised manuscript.
```

## Internal Chinese Audit Block

```text
中文意见：提升幅度较小，需要说明实际意义并避免夸大结论。[核验状态：已落实；证据：Performance Comparison 小节和 Conclusion 第一段均有蓝色修改。]

回复意见中文版：感谢您的意见。Performance Comparison 小节现在将报告的改进解释到应用尺度，并把目标值差异转换为项目层面的估计影响。结论第一段也将措辞收敛为在测试设置下 modest but measurable 的结果，而非广泛保证。相关修改已在修订稿中以蓝色标出。
```

## Pending-Item Response

Use pending language when the manuscript artifact is not ready.

```text
Response: Thank you for your suggestion. This item is being completed by adding two recent baselines to the main performance table, convergence figure, and supplementary parameter table. The missing artifacts are the final result entries and the corresponding statistical tests; they will be marked in blue after the additional runs are complete.
```

Do not write:

```text
Response: Thank you for your suggestion. The comparison has been extended by adding two recent baselines.
```

unless the result table and manuscript revisions already exist.
