# Harmonic Coding Developer Guide

> A Copilot-first guide for choosing the right workflow tool.

Harmonic Coding already covers the spec-driven and AIDD layer. This guide is the missing bridge between "what to build" and "which workflow engine should carry the work."

## Default rule

Start with the existing Harmonic Coding docs.

1. Use spec-driven development when scope or contracts matter.
2. Use AIDD when you need discovery, task breakdown, or a disciplined execution loop.
3. Add one of the workflow tools below only when the task genuinely needs it.

Before implementation starts, use `docs/guide/delivery-workflows.md` as the repo-shaping checklist:
- objective
- problem / users / success
- scope
- capability map
- epics
- phases
- tickets / backlog
- review gates
- setup / CI/CD

## Tool selection

| Need | Use | Why |
|---|---|---|
| Small repo-aware code edits | Aider | Git diffs stay reviewable and local |
| Ordered step pipeline | LangGraph | Best fit for stateful, step-by-step workflows |
| Role-based multi-agent work | AutoGen or CrewAI | Good for planner/reviewer/researcher patterns |
| Typed structured outputs | Pydantic AI | Keeps outputs schema-safe |
| Agent platform/runtime | Agno | Adds storage, scheduling, RBAC, and a control plane |
| Autonomous issue fixing | OpenHands or mini-SWE-agent | Best when the workflow should keep running |

## Recommended Harmonic Coding stack

- **Copilot** as the primary interface.
- **AIDD/spec docs** as the source of truth.
- **Aider** for controlled implementation loops.
- **LangGraph** when the task must happen in explicit steps.
- **Pydantic AI** when the output must be typed and validated.
- **AutoGen/CrewAI** when several agent roles are useful.
- **Agno** when the workflow becomes a platform.
- **OpenHands/SWE-agent** when the task should be more autonomous.

## Practical workflow

1. Read the relevant research doc and the current spec/guide.
2. Write or refresh the spec before coding.
3. Prefer the repo-local skill or workflow entrypoint first when `harmonic-custom/skills/` or `.github/prompts/` already describes the task.
4. Pick the smallest external workflow tool that fits the task when the local workflow layer is not enough.
5. Keep changes small and reviewable.
6. Validate against tests, not just chat output.

## Review and repair loop

When the task is supposed to be finished, do not stop at the first working pass.

1. Compare the current implementation against the spec, `vision.md`, and repo instructions.
2. Run the relevant tests, lint, and build checks.
3. If you are comparing workflows, compare the result against the same benchmark or instructions in both variants.
4. Fix blocking mismatches before moving on.
5. Repeat until the implementation matches the requirements or you have a real blocker.

## What not to do

- Do not use a full orchestration stack for a one-file fix.
- Do not replace Copilot with another tool just because it exists.
- Do not let the workflow tool invent scope that the spec did not define.
- Do not stop while a blocking mismatch still exists between the code and the instructions.

## Related docs

- `docs/guide/delivery-workflows.md`
- `docs/research/01-spec-driven-development.md`
- `docs/research/05-aidd-framework.md`
- `docs/research/08-aider.md`
- `docs/research/09-autogen.md`
- `docs/research/10-crewai.md`
- `docs/research/11-langgraph.md`
- `docs/research/12-pydantic-ai.md`
- `docs/research/13-agno.md`
- `docs/research/14-openhands-swe-agent.md`
