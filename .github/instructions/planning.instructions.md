---
applyTo: "{docs/guide/delivery-workflows.md,docs/guide/new-project-guide.md,docs/guide/aidd-gap-closure-plan.md,.github/prompts/create-*.prompt.md,.github/prompts/review-planning-layer.prompt.md,.github/prompts/groom-backlog.prompt.md,.github/prompts/replan-when-necessary.prompt.md,.github/prompts/run-preimplementation-checklist.prompt.md}"
---

# Planning Workflow Rules

- Preserve the planning layer order: repository map -> objective -> problem/users/success -> scope -> capability map -> epics -> phases -> tickets -> reviews.
- Do not let planning prompts skip directly from goal to tickets without scope and capability logic.
- Keep change control exceptional; use backlog grooming for routine corrections.
- When adding a new planning workflow, document:
  - where the artifact is stored
  - what metadata it needs
  - how AI should use it
  - what "done" means for that layer
- When editing the planning system, update both the workflow prompt and the guide entry that explains it.
