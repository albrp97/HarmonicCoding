---
name: Replan When Necessary
description: Perform controlled change control only when material evidence shows the existing plan is no longer valid.
---

You have to decide whether `${PROJECT_OR_REPO}` truly needs replanning or change control.

This workflow is intentionally conservative. The default is to preserve the plan and fix the smallest affected layer unless there is material evidence that the plan is wrong.

## Why this workflow exists

Use it only when:
- a dependency assumption is false
- a phase or epic boundary is no longer valid
- a major risk, blocker, or scope conflict was discovered
- real delivery evidence shows the current plan cannot succeed as written

Do **not** use it for normal implementation feedback, routine ticket grooming, or minor corrections.

## Outcome

Produce one of these decisions:
- **no replan needed**
- **local adjustment only**
- **targeted layer update required**
- **formal replanning required**

Write the result to:
- `docs/planning/reviews/change-control.md`

## Decision checklist

Check:
1. what changed
2. whether the change is material
3. the smallest layer affected
4. whether local fixes are enough
5. whether future execution would be wrong if the plan stays unchanged

## Output structure

```markdown
# Change Control Decision

## Decision
- no replan needed / local adjustment only / targeted layer update required / formal replanning required

## Trigger
- ...

## Evidence
- ...

## Smallest Affected Layer
- ...

## Required Action
- ...

## Why Replanning Is or Is Not Necessary
- ...
```

## Rules

1. Replanning is exceptional, not routine.
2. Prefer the smallest possible correction.
3. Preserve strong upfront planning unless reality clearly invalidates it.
4. If only the backlog changed, do backlog grooming instead.
