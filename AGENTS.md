# Harmonic Coding Agent Instructions

This repository is the source of truth for the Harmonic Coding workflow system.

## Read order

Before major work, read these in order:

1. `vision.md`
2. `README.md`
3. `docs/guide/new-project-guide.md` when the task is about applying Harmonic Coding to a repository
4. `docs/guide/delivery-workflows.md` when the task is about planning, setup, review, or implementation flow
5. `docs/guide/aidd-gap-closure-plan.md` when the task is about closing the current AIDD-alignment gaps

## Core operating rules

- Preserve the current planning stack: repository map, objective, problem/users/success, scope, capability map, epics, phases, tickets, reviews.
- Do not jump straight to implementation when planning or setup artifacts are missing.
- Treat documentation, workflow prompts, and instruction files as production assets that must stay aligned.
- When a workflow changes, update the relevant guide and prompt file together.
- Do not mark work complete at "code written." Completion requires the documented validation and review loop.

## Repository context

- `docs/guide/` contains the main operational guides.
- `.github/prompts/` contains reusable workflow prompts.
- `.github/instructions/` contains path-scoped rules.
- `harmonic-custom/` contains the local override layer and reusable skill entrypoints.

## Task routing

- New project or repo-shaping task => use `docs/guide/new-project-guide.md`
- Planning stack task => use the matching workflow in `.github/prompts/`
- Setup / CI / branch / PR workflow task => use `.github/prompts/setup-project-workflow.prompt.md`
- Ticket delivery task => use `.github/prompts/implement-feature-workflow.prompt.md`
- Review / security / hotspot / PR-triage task => use the dedicated review workflows

## Review and repair rule

After a meaningful change:

1. compare the result against `vision.md`, the relevant prompt, and the relevant guide
2. fix blocking mismatches
3. only then move on

## Override layer

Read `harmonic-custom/AGENTS.md` after this file for repository-local overrides.
Use `harmonic-custom/config.yml` for workflow toggles.
Use `harmonic-custom/skills/index.md` to discover the reusable skill entrypoints.
