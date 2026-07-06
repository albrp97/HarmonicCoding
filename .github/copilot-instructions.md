# Harmonic Coding

## What This Repo Does

This repository defines the Harmonic Coding workflow system for planning, shaping, and delivering AI-assisted software projects through durable guides, prompts, and instruction files.

## Primary Files

- `vision.md` — project purpose, constraints, and success criteria
- `docs/guide/new-project-guide.md` — strict onboarding flow for applying Harmonic Coding to a repository
- `docs/guide/delivery-workflows.md` — workflow catalog and operating rules
- `docs/guide/aidd-gap-closure-plan.md` — live backlog for closing AIDD-alignment gaps in this repo
- `.github/prompts/` — reusable workflow prompts
- `.github/instructions/` — path-scoped instructions
- `harmonic-custom/skills/` — reusable skill entrypoints that load the workflow prompts

## Engineering Rules

- Read `vision.md` before major work.
- Preserve the existing planning stack; do not collapse it into a simpler discovery-only flow.
- Do not start normal implementation when the planning and setup baseline is missing.
- Keep prompt files and guides aligned when a workflow changes.
- Documentation updates are required when workflows, commands, setup, or done criteria change.

## Default Workflow

1. For new project usage, follow `docs/guide/new-project-guide.md`.
2. For repo shaping, use the matching prompt in `.github/prompts/`.
3. For ticket delivery, use `.github/prompts/implement-feature-workflow.prompt.md`.
4. For setup and CI/CD, use `.github/prompts/setup-project-workflow.prompt.md`.
5. For reviews, use the dedicated review workflows before treating work as done.

## Validation

- This repo is documentation-first.
- Validate changes by checking consistency across guides, prompts, instructions, and workflow contracts.
- When workflow evals exist, use them as the final consistency gate.
