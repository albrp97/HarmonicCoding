# Harmonic Coding New Project Guide

> Strict instructions for using Harmonic Coding when starting a new project from zero or when shaping an existing repository before serious implementation begins.

This is the **operating sequence** for applying Harmonic Coding to a real project.

Use this guide when:

- you are creating a new repository
- you are adopting Harmonic Coding in an existing repository
- you want a strict order for planning, setup, implementation, and review

Do **not** start normal implementation before this guide says the repository is ready.

## What this guide is for

Harmonic Coding is not one prompt and not one tool. It is a **working system** made of:

1. context files
2. planning artifacts
3. workflow prompts
4. setup and CI/CD decisions
5. implementation and review loops

This guide tells you:

- what to read first
- what files to create
- what workflows to run
- what order to follow
- when the repository is ready for implementation

## Current operating model

The current Harmonic Coding runtime for this repository is made of:

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `harmonic-custom/AGENTS.md`
- `harmonic-custom/config.yml`
- `harmonic-custom/skills/`
- `docs/guide/setup-guide.md`
- `docs/guide/delivery-workflows.md`
- `.github/prompts/*.prompt.md`
- `ai-evals/workflow-contracts.json`

Use those files as the current execution system.

The runtime maintenance record and gap-closure history live in:

- `docs/guide/aidd-gap-closure-plan.md`

That plan remains the architectural record for the runtime layer. The starting point for a new project is the workflow below.

## Quick start

If you want the shortest correct setup path for a new repository, do this:

1. copy or create the baseline files:
   - `README.md`
   - `vision.md`
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
   - `.github/instructions/`
   - `.github/prompts/`
   - `docs/planning/`
   - `docs/specs/`
   - `harmonic-custom/`
2. read `README.md`, `docs/guide/setup-guide.md`, and `docs/guide/delivery-workflows.md`
3. run the planning stack from repository map through backlog
4. run the planning reviews
5. run the setup / CI workflow
6. run the pre-implementation checklist
7. only then implement one ticket using the feature workflow

If any of those steps is missing, the repo is not ready for normal implementation.

## Non-negotiable rule

**Do not write implementation code before the repository has the minimum planning and setup baseline.**

Minimum baseline means:

1. the project intent is documented
2. the repository structure is mapped
3. the delivery scope is defined
4. the backlog exists
5. the validation approach is clear
6. the repo has at least a workable setup and quality loop

## The strict order

Follow these phases in order:

1. prepare the repository context
2. create the planning baseline
3. review the planning layers
4. define setup, quality, and CI/CD
5. confirm implementation readiness
6. implement one ticket at a time
7. keep the backlog and review loops healthy

## Phase 0 — Read the right docs first

Before creating project artifacts, read these in order:

1. `README.md`
2. `docs/guide/setup-guide.md`
3. `docs/guide/delivery-workflows.md`
4. `docs/guide/developer-guide.md`
5. the most relevant research guide only if you need deeper context

### Why this comes first

This prevents starting from random prompts or mixing incompatible workflows.

### Done when

- you know which guide controls setup
- you know which guide controls planning and implementation
- you know which workflow prompts will be used

## Phase 1 — Create the repository baseline files

Before deeper planning, create or confirm these files and folders:

- `README.md`
- `vision.md`
- `docs/planning/`
- `docs/specs/`
- `.github/prompts/`

Recommended baseline additions for a real project repo:

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/`
- `harmonic-custom/`

### Why this matters

If the repo has nowhere durable to store context, planning will collapse back into chat history.

### What each path is for

| Path | Purpose |
|---|---|
| `README.md` | entry point for humans and agents |
| `vision.md` | stable project purpose, users, constraints, success |
| `docs/planning/` | repository map, epics, phases, backlog, tickets, reviews |
| `docs/specs/` | scope and capability artifacts |
| `.github/prompts/` | reusable workflow prompts |
| `AGENTS.md` / `.github/copilot-instructions.md` | persistent behavior rules for agent sessions |
| `harmonic-custom/` | local overrides, workflow toggles, and skill entrypoints |

### Done when

- the repo has durable places for planning and instructions

## Phase 2 — Create the project definition baseline

Run the planning workflows in this exact order:

1. repository map
2. objective
3. problem / users / success
4. scope
5. capability map
6. epics
7. phases
8. tickets / backlog

These are not optional if you want Harmonic Coding to work correctly on non-trivial projects.

### Required workflow files

Use these prompt files:

1. `.github/prompts/create-repository-map.prompt.md`
2. `.github/prompts/discover-project-objective.prompt.md`
3. `.github/prompts/discover-problem-users-success.prompt.md`
4. `.github/prompts/define-project-scope.prompt.md`
5. `.github/prompts/create-capability-map.prompt.md`
6. `.github/prompts/create-epics.prompt.md`
7. `.github/prompts/create-phases.prompt.md`
8. `.github/prompts/create-tickets.prompt.md`

### Required output files

By the end of this phase, the repo should contain:

- `docs/planning/repo-map.md`
- `vision.md`
- `docs/specs/project-scope.md`
- `docs/specs/capability-map.md`
- `docs/planning/epics.md`
- `docs/planning/phases.md`
- `docs/planning/backlog.md`
- `docs/planning/tickets/`

### How to run this phase

Use the local runtime in one of these ways:

1. **Prompt-first:** open the matching file in `.github/prompts/` and use it directly in Copilot Chat or Copilot CLI.
2. **Skill-first:** use the matching entrypoint in `harmonic-custom/skills/` when you want a durable reusable operation.
3. **Guide-first:** read the matching section in `docs/guide/delivery-workflows.md` when you need the full artifact structure and explanation.

Practical pattern:

1. choose the matching workflow
2. provide the target repository or project area
3. let the agent inspect the repo and produce the required artifact
4. review the artifact before moving to the next planning layer

### How to execute the workflows in practice

Use this mapping:

| Need | Primary entrypoint | Supporting source |
|---|---|---|
| full planning bootstrap | `harmonic-custom/skills/planning-bootstrap/SKILL.md` | `.github/prompts/create-*.prompt.md` |
| setup / CI / PR baseline | `harmonic-custom/skills/setup-delivery-workflow/SKILL.md` | `.github/prompts/setup-project-workflow.prompt.md` |
| readiness check | `harmonic-custom/skills/preimplementation-checklist/SKILL.md` | `.github/prompts/run-preimplementation-checklist.prompt.md` |
| ticket delivery | `harmonic-custom/skills/implement-ticket/SKILL.md` | `.github/prompts/implement-feature-workflow.prompt.md` |
| planning review | `harmonic-custom/skills/planning-layer-review/SKILL.md` | `.github/prompts/review-planning-layer.prompt.md` |
| backlog maintenance | `harmonic-custom/skills/groom-backlog/SKILL.md` | `.github/prompts/groom-backlog.prompt.md` |
| phase feedback | `harmonic-custom/skills/phase-feedback/SKILL.md` | `.github/prompts/review-phase-feedback.prompt.md` |
| change control | `harmonic-custom/skills/change-control/SKILL.md` | `.github/prompts/replan-when-necessary.prompt.md` |
| PR review | `harmonic-custom/skills/review-pr/SKILL.md` | `.github/prompts/review-pr-workflow.prompt.md` |
| security review | `harmonic-custom/skills/review-security/SKILL.md` | `.github/prompts/review-security-workflow.prompt.md` |
| hotspot review | `harmonic-custom/skills/review-hotspots/SKILL.md` | `.github/prompts/review-hotspots-workflow.prompt.md` |
| PR comment triage | `harmonic-custom/skills/triage-pr-comments/SKILL.md` | `.github/prompts/triage-pr-comments-workflow.prompt.md` |
| user-test creation | `harmonic-custom/skills/create-user-test-scripts/SKILL.md` | `.github/prompts/create-user-test-scripts.prompt.md` |
| user-test execution | `harmonic-custom/skills/run-user-test/SKILL.md` | `.github/prompts/run-user-test-workflow.prompt.md` |
| markdown pipeline execution | `harmonic-custom/skills/run-markdown-pipeline/SKILL.md` | `.github/prompts/run-markdown-pipeline.prompt.md` |
| runtime pilot and hardening | `harmonic-custom/skills/pilot-runtime/SKILL.md` | `.github/prompts/pilot-runtime-workflow.prompt.md` |

### Important rule

Do not jump from project idea straight to tickets. The scope and capability layers exist specifically to stop chaotic backlog creation.

### Done when

- the project has a documented planning stack from objective down to backlog

## Phase 3 — Review the planning layers before setup

After the planning artifacts exist, run the review workflows:

1. `.github/prompts/review-planning-layer.prompt.md`
2. `.github/prompts/review-phase-feedback.prompt.md` when phase-level review becomes relevant
3. `.github/prompts/groom-backlog.prompt.md` for backlog hygiene
4. `.github/prompts/replan-when-necessary.prompt.md` only when material evidence invalidates the plan

### Why this matters

Harmonic Coding is designed to invest effort upfront. Review gates protect that effort and prevent weak planning from leaking into implementation.

### Rules

1. use backlog grooming for routine fixes
2. use change control only when truly necessary
3. do not replan broadly when a small local correction is enough

### Required review outputs

- `docs/planning/reviews/`
- layer review files
- phase review files when applicable
- backlog grooming notes when useful
- change-control notes only when needed

### Done when

- the planning layers are coherent enough to support setup and execution

## Phase 4 — Define setup, validation, and CI/CD

Only after the planning baseline exists, run the setup workflow:

- `.github/prompts/setup-project-workflow.prompt.md`

### What this workflow must cover

1. project and stack understanding
2. branch strategy
3. commit strategy
4. pull request flow
5. local quality commands
6. CI workflow shape
7. test layers
8. release or versioning only if the project needs it

### What to document during setup

- install commands
- lint, format, type-check, test, and build commands
- branch naming convention
- commit convention
- PR expectations
- release flow if relevant
- which starter workflow templates or eval workflows are being used

### Important rule

Do not overengineer the pipeline. Choose the smallest effective baseline for the actual stack and delivery risk.

### Done when

- the repo has a coherent local and CI quality loop
- another engineer can understand how work is validated

## Phase 5 — Run the master readiness check

Before feature implementation begins, run:

- `.github/prompts/run-preimplementation-checklist.prompt.md`

### What this check is confirming

1. the planning outputs exist
2. the backlog order is clear
3. the active phase is clear
4. the review gates did not leave blocking issues
5. the repo has a usable setup and validation baseline

### Do not proceed if any of these are missing

- no `vision.md`
- no backlog
- no clear next ticket
- no usable validation path
- no agreed scope boundary

### Done when

- the repository is officially ready for implementation

## Phase 6 — Implement one ticket at a time

When the repo is ready, use:

- `.github/prompts/implement-feature-workflow.prompt.md`

### Strict implementation sequence

1. read the ticket
2. restate objective, scope, acceptance, and risks
3. inspect affected code and tests
4. run the best existing validation baseline
5. implement the smallest complete change
6. update docs if behavior, config, commands, workflows, or APIs changed
7. rerun the relevant gates
8. prepare branch and commit
9. push and open the PR
10. stay in the PR repair loop until merge-ready

### Important rules

1. do not implement from memory when the ticket already defines scope
2. do not mix unrelated work into the same ticket
3. do not call a ticket done at "code written"
4. done means merge-ready, merged, or externally blocked after everything else is complete

### Done when

- one ticket has been delivered through code, docs, checks, PR, and repair loop

## Phase 7 — Keep the system healthy during execution

Once implementation starts, keep using these workflows repeatedly:

| Workflow | When to use it |
|---|---|
| `groom-backlog.prompt.md` | before choosing the next ticket or when the backlog gets stale |
| `review-phase-feedback.prompt.md` | after meaningful phase progress or phase completion |
| `replan-when-necessary.prompt.md` | only when evidence shows the current plan is no longer valid |
| `implement-feature-workflow.prompt.md` | for every ticket delivery loop |
| `review-pr-workflow.prompt.md` | when deciding whether work is merge-ready |
| `review-security-workflow.prompt.md` | when auth, secrets, validation, workflows, or risky integrations changed |
| `review-hotspots-workflow.prompt.md` | when the review surface is large or risky |
| `triage-pr-comments-workflow.prompt.md` | when review feedback must be turned into a repair loop |
| `create-user-test-scripts.prompt.md` | when usability or operator flow needs explicit validation |
| `run-user-test-workflow.prompt.md` | when user testing is part of release or acceptance proof |
| `run-markdown-pipeline.prompt.md` | when an ordered markdown checklist should be executed step by step |
| `pilot-runtime-workflow.prompt.md` | when hardening the runtime after a real run |

### Why this matters

Harmonic Coding is not a one-time planning ritual. It is a sustained delivery system. The repo only stays healthy if the backlog, reviews, and readiness logic continue during execution.

## What a new project should look like before normal coding begins

Use this as the minimum readiness checklist:

| Area | Must exist |
|---|---|
| Purpose | `vision.md` |
| Repo orientation | `docs/planning/repo-map.md` |
| Instruction stack | `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/` |
| Local override layer | `harmonic-custom/AGENTS.md`, `harmonic-custom/config.yml`, `harmonic-custom/skills/` |
| Scope | `docs/specs/project-scope.md` |
| Capabilities | `docs/specs/capability-map.md` |
| Delivery structure | `docs/planning/epics.md`, `docs/planning/phases.md` |
| Execution structure | `docs/planning/backlog.md`, `docs/planning/tickets/` |
| Review system | `docs/planning/reviews/` |
| Validation baseline | setup/CI/CD workflow outputs, local commands, and workflow evals where used |

If these do not exist, the repository is not ready for serious AI-assisted implementation.

## How the guides fit together

| Guide | Use it for |
|---|---|
| `README.md` | top-level orientation |
| `docs/guide/setup-guide.md` | baseline repo files and tool setup |
| `docs/guide/delivery-workflows.md` | the full workflow system and prompt list |
| `docs/guide/developer-guide.md` | choosing the right workflow tool |
| `docs/guide/advanced-playbook.md` | deeper spec-driven operating model |
| `docs/guide/ultimate-guide.md` | broader operational reference |
| `docs/guide/security-rules.md` | reusable security review rules |
| `docs/guide/hotspot-review-guide.md` | hotspot review signals and fallback heuristic |
| `docs/guide/aidd-gap-closure-plan.md` | runtime backlog and AIDD-alignment record |

## What not to do

1. do not skip the planning layers and jump straight into feature coding
2. do not create tickets before scope and capability logic exist
3. do not overbuild CI/CD before understanding the project and stack
4. do not treat documentation as optional after implementation starts
5. do not replan constantly; use change control only when the evidence is strong
6. do not stop at the first working-looking pass when tests, docs, or PR state still disagree

## Recommended first-time adoption pattern

If this is the first time using Harmonic Coding on a real repo:

1. start with one repo
2. complete the planning baseline fully
3. set up the lean validation and CI workflow
4. implement one ticket using the feature workflow
5. run PR review, security review, and user-testing where relevant
6. repair the rough edges in the docs, prompts, and instructions only after that real run

This is the fastest way to make the system real without overengineering it from theory alone.

## Final rule

Harmonic Coding works best when you treat:

- the **spec and planning artifacts** as the durable asset
- the **instructions** as the control layer
- the **workflow prompts** as the operating procedure
- the **implementation loop** as a validation exercise, not just a coding exercise

If you keep that order, the system stays coherent as the project grows.
