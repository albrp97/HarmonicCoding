---
name: Run Pre-Implementation Checklist
description: Execute the full ordered repository-shaping workflow before feature implementation starts.
---

You have to prepare `${PROJECT_OR_REPO}` for implementation by running the full pre-implementation workflow in order.

This is the master checklist to follow before building features seriously.

## Outcome

Leave the repository with:
- a repository map
- project objective and problem framing
- scope, capability map, epics, phases, and tickets
- review gates and backlog hygiene
- setup and CI/CD baseline
- a clear decision that the repo is ready for feature implementation

## Ordered workflow

Run these workflows in order:

1. Create repository map
2. Discover project objective
3. Discover problem / users / success
4. Define project scope
5. Create capability map
6. Create epics
7. Create phases
8. Create tickets / backlog
9. Review each planning layer
10. Set up project delivery workflow
11. Groom backlog
12. Confirm implementation readiness

## Required outputs

Before calling the repo ready, confirm these exist:
- `docs/planning/repo-map.md`
- `vision.md`
- `docs/specs/project-scope.md`
- `docs/specs/capability-map.md`
- `docs/planning/epics.md`
- `docs/planning/phases.md`
- `docs/planning/backlog.md`
- `docs/planning/tickets/`
- `docs/planning/reviews/`
- CI/CD and local quality workflow docs/config where applicable

## Readiness rule

Do not start normal ticket implementation until:
- the active ticket exists
- the backlog order is clear
- the active phase is clear
- review gates have not flagged blocking planning issues
- the setup/CI baseline is coherent enough to validate work

## Rules

1. Prefer strong upfront planning over repeated replanning.
2. Use review gates between major layers.
3. Use change control only when material evidence shows the plan is no longer valid.
