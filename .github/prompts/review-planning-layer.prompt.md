---
name: Review Planning Layer
description: Review a planning layer for completeness, consistency, evidence, and readiness before allowing the next layer to proceed.
---

You have to review the `${LAYER_NAME}` planning layer for `${PROJECT_OR_REPO}` before the workflow proceeds to the next layer.

This is a gate, not a rewrite pass by default. The goal is to decide whether the layer is good enough to approve, or whether it needs revision.

## Why this workflow exists

Use it to:
- catch contradictions between adjacent planning layers
- verify metadata, evidence, and boundaries are complete
- stop low-quality planning from propagating into later layers
- keep the system rigorous without forcing constant replanning

## Outcome

Produce one of these review decisions:
- **approved**
- **approved with notes**
- **needs revision**

Write the result to:
- `docs/planning/reviews/${LAYER_NAME}-review.md`

## Review inputs

Review the target layer against:
- the previous layer
- the next intended use of the layer
- the layer's required structure and metadata
- evidence and unresolved questions

## Review checklist

Check:
1. completeness
2. contradictions with earlier layers
3. boundary clarity
4. evidence quality
5. metadata completeness
6. readiness for the next layer

## Review output structure

```markdown
# Review: [Layer Name]

## Decision
- approved / approved with notes / needs revision

## Summary
- ...

## Checks
| Check | Result | Notes |
|---|---|---|
| Completeness | pass/fail | ... |
| Consistency | pass/fail | ... |
| Boundary clarity | pass/fail | ... |
| Evidence | pass/fail | ... |
| Metadata | pass/fail | ... |
| Next-layer readiness | pass/fail | ... |

## Required Revisions
1. ...

## Carry-Forward Notes
- ...
```

## Rules

1. Do not trigger replanning unless the issue is materially blocking.
2. Prefer fixing the current layer over rewriting upstream layers.
3. Only fail the review for real problems, not stylistic preferences.
