# Harmonic Coding

![Harmonic Coding](./harmonic-coding-banner.svg)

> A repository-based runtime for disciplined AI-assisted software delivery.

Harmonic Coding is not just research about AI engineering. It is now a **working repo runtime** made of:

- persistent instruction files
- reusable workflow prompts
- local skill entrypoints
- planning and delivery guides
- review, user-testing, and pipeline workflows
- lightweight workflow contract evals

The goal is to make AI-assisted development behave like a repeatable engineering system instead of an ad hoc chat habit.

## Skills and workflows included

The runtime already includes a usable operating set of **skills** and **workflow prompts**.

### Current skill entrypoints

- planning bootstrap
- pre-implementation checklist
- setup delivery workflow
- implement ticket
- planning review and backlog shaping
- PR, security, and hotspot review
- PR comment triage
- user-test creation and execution
- markdown pipeline execution
- runtime pilot workflows

### Current workflow families

- planning workflows
- setup / CI / branch / PR workflows
- feature delivery workflows
- review and security workflows
- user-testing workflows
- runtime and documentation operations

The detailed catalog lives later in this README and in:

- `harmonic-custom/skills/index.md`
- `docs/guide/delivery-workflows.md`

## Feature set and target outcome

### What the repo already has

| Feature area | What exists in the repo |
|---|---|
| instruction stack | root `AGENTS.md`, Copilot instructions, and path-scoped instruction files |
| project intent | `vision.md` for purpose, constraints, and success criteria |
| workflow prompt library | planning, setup, implementation, review, security, user-test, pipeline, and pilot prompts |
| skill entrypoints | local `harmonic-custom/skills/` wrappers for the main workflows |
| planning system | workflows for repo map, objective, problem, scope, capabilities, epics, phases, tickets, backlog shaping, phase feedback, and change control |
| delivery system | setup-delivery workflow, pre-implementation checklist, and ticket implementation workflow |
| review system | PR review, security review, hotspot review, and PR comment triage |
| user validation system | workflows to create user-test scripts and run user-test passes |
| documentation system | setup, onboarding, workflow, security, hotspot, and broader operating guides |
| workflow templates | reusable GitHub workflow templates in `.github/workflow-templates/` |
| eval scaffolding | workflow contract spec, eval script, generated reports, and CI workflow checks |
| override layer | `harmonic-custom/` config and local operating overrides for repo-specific behavior |
| research base | research and synthesis docs that explain where the runtime came from |

### What Harmonic Coding is trying to achieve

- turn AI-assisted coding into a **repeatable repo operating system**
- let a new project go from **idea -> planning -> implementation -> validation -> PR -> merge** with a consistent workflow
- make planning durable so the agent works from repo memory instead of only from chat context
- make feature work stricter through checklists, reviews, repair loops, and user-test passes
- make setup of CI/CD, review, and delivery expectations part of the operating model, not an afterthought
- keep the system **portable** so the runtime can be copied into a fresh repository and used quickly
- keep the system **inspectable** because the rules, prompts, skills, and guides all live in versioned files
- keep the system **lightweight** with contract-style evals instead of heavy overengineered orchestration

---

## What it is

Harmonic Coding combines:

1. **context engineering** — instructions, source-of-truth files, and stable repo context
2. **planning discipline** — repository map, objective, scope, capability map, epics, phases, tickets, and review gates
3. **delivery workflows** — setup, implementation, PR review, security review, user-testing, and repair loops
4. **runtime structure** — local skills, prompt entrypoints, path-scoped rules, and workflow eval scaffolding

It is designed for repos that want to:

- shape the project before coding
- keep AI work aligned with scope
- avoid weak planning and random implementation jumps
- preserve a durable operating model across sessions

---

## What it is not

Harmonic Coding is **not**:

- a single prompt
- a model-specific plugin
- a packaged CLI product
- a replacement for engineering judgment

It is a **repo-centered workflow system** that you can use directly, copy into another repository, or adapt into stricter tooling later.

---

## Current runtime status

This repository already includes the runtime baseline.

### Runtime layer

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`
- `harmonic-custom/AGENTS.md`
- `harmonic-custom/config.yml`
- `harmonic-custom/skills/`

### Workflow layer

- `.github/prompts/*.prompt.md`

### Guide layer

- `docs/guide/*.md`

### Eval layer

- `ai-evals/workflow-contracts.json`
- `tools/eval_workflows.py`
- `.github/workflows/workflow-evals.yml`

---

## How it works

Harmonic Coding works in layers.

| Layer | Purpose |
|---|---|
| `vision.md` | stable purpose, constraints, and success criteria |
| `AGENTS.md` | cross-tool runtime rules |
| `.github/copilot-instructions.md` | Copilot-specific always-on instructions |
| `.github/instructions/` | path-scoped detail |
| `.github/prompts/` | reusable workflow bodies |
| `harmonic-custom/skills/` | stable skill entrypoints that load those workflows |
| `docs/guide/` | explanations, onboarding, and operating sequences |
| `ai-evals/` | workflow contract checks |

The normal sequence is:

1. load the instructions
2. orient through the guides
3. run the planning stack
4. set up validation and delivery workflow
5. implement one ticket at a time
6. review, test, and repair until the work is actually ready

---

## How to use it on a new project

If you want to apply Harmonic Coding to a repository, start here:

1. **Read:** `docs/guide/new-project-guide.md`
2. **Set up the baseline files:** `vision.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.github/prompts/`, `docs/planning/`, `docs/specs/`, `harmonic-custom/`
3. **Run the planning stack:** repository map -> objective -> problem/users/success -> scope -> capability map -> epics -> phases -> tickets
4. **Run the planning reviews**
5. **Run the setup / CI / delivery workflow**
6. **Run the pre-implementation readiness check**
7. **Only then implement tickets**

If you want the short practical sequence, use:

- `docs/guide/new-project-guide.md`

If you want the detailed workflow catalog, use:

- `docs/guide/delivery-workflows.md`

---

## Start here

| Need | Read first |
|---|---|
| **New Project Guide** | [`docs/guide/new-project-guide.md`](./docs/guide/new-project-guide.md) |
| strict onboarding for a new repo | [`docs/guide/new-project-guide.md`](./docs/guide/new-project-guide.md) |
| full workflow catalog | [`docs/guide/delivery-workflows.md`](./docs/guide/delivery-workflows.md) |
| repo baseline and setup files | [`docs/guide/setup-guide.md`](./docs/guide/setup-guide.md) |
| workflow/tool selection | [`docs/guide/developer-guide.md`](./docs/guide/developer-guide.md) |
| broader operating reference | [`docs/guide/ultimate-guide.md`](./docs/guide/ultimate-guide.md) |
| deeper spec-driven operating model | [`docs/guide/advanced-playbook.md`](./docs/guide/advanced-playbook.md) |
| AIDD comparison and runtime history | [`docs/guide/aidd-gap-closure-plan.md`](./docs/guide/aidd-gap-closure-plan.md) |

---

## Available workflow families

The current repo includes workflow prompts for:

### Planning

- repository map
- objective
- problem / users / success
- scope
- capability map
- epics
- phases
- tickets
- planning-layer review
- backlog grooming
- phase feedback
- change control
- pre-implementation checklist

### Delivery

- setup / CI / branch / PR baseline
- ticket implementation

### Review

- PR review
- security review
- hotspot review
- PR comment triage

### Validation

- create user-test scripts
- run user-test workflow
- workflow contract evals

### Runtime operations

- run markdown pipeline
- pilot the runtime on real work

---

## Available skill entrypoints

The local skill layer currently exposes:

- `planning-bootstrap`
- `preimplementation-checklist`
- `setup-delivery-workflow`
- `implement-ticket`
- `planning-layer-review`
- `groom-backlog`
- `phase-feedback`
- `change-control`
- `review-pr`
- `review-security`
- `review-hotspots`
- `triage-pr-comments`
- `create-user-test-scripts`
- `run-user-test`
- `run-markdown-pipeline`
- `pilot-runtime`

See:

- `harmonic-custom/skills/index.md`

---

## Important guides

### Core guides

- [`docs/guide/new-project-guide.md`](./docs/guide/new-project-guide.md)
- [`docs/guide/delivery-workflows.md`](./docs/guide/delivery-workflows.md)
- [`docs/guide/setup-guide.md`](./docs/guide/setup-guide.md)
- [`docs/guide/developer-guide.md`](./docs/guide/developer-guide.md)
- [`docs/guide/security-rules.md`](./docs/guide/security-rules.md)
- [`docs/guide/hotspot-review-guide.md`](./docs/guide/hotspot-review-guide.md)

### Reference and background

- [`docs/guide/ultimate-guide.md`](./docs/guide/ultimate-guide.md)
- [`docs/guide/advanced-playbook.md`](./docs/guide/advanced-playbook.md)
- [`docs/guide/aidd-gap-closure-plan.md`](./docs/guide/aidd-gap-closure-plan.md)

---

## Research library

The repo still includes the research base that informed the runtime:

### Spec-driven and context engineering

- [`docs/research/01-spec-driven-development.md`](./docs/research/01-spec-driven-development.md)
- [`docs/research/02-context-engineering.md`](./docs/research/02-context-engineering.md)
- [`docs/research/03-automation-patterns.md`](./docs/research/03-automation-patterns.md)
- [`docs/research/04-token-economics.md`](./docs/research/04-token-economics.md)
- [`docs/research/00-transcript-intelligence.md`](./docs/research/00-transcript-intelligence.md)

### AIDD and synthesis

- [`docs/research/05-aidd-framework.md`](./docs/research/05-aidd-framework.md)
- [`docs/research/06-synthesis.md`](./docs/research/06-synthesis.md)
- [`docs/guide/aidd-guide.md`](./docs/guide/aidd-guide.md)

### Tool integration and orchestration

- [`docs/research/07-tool-integration.md`](./docs/research/07-tool-integration.md)
- [`docs/research/08-aider.md`](./docs/research/08-aider.md)
- [`docs/research/09-autogen.md`](./docs/research/09-autogen.md)
- [`docs/research/10-crewai.md`](./docs/research/10-crewai.md)
- [`docs/research/11-langgraph.md`](./docs/research/11-langgraph.md)
- [`docs/research/12-pydantic-ai.md`](./docs/research/12-pydantic-ai.md)
- [`docs/research/13-agno.md`](./docs/research/13-agno.md)
- [`docs/research/14-openhands-swe-agent.md`](./docs/research/14-openhands-swe-agent.md)

---

## Repo layout

| Path | Purpose |
|---|---|
| `AGENTS.md` | cross-tool runtime rules |
| `vision.md` | project purpose and constraints |
| `.github/prompts/` | reusable workflow prompts |
| `.github/instructions/` | path-scoped rules |
| `harmonic-custom/` | local overrides and skill entrypoints |
| `docs/guide/` | practical operating guides |
| `docs/research/` | background research and comparisons |
| `ai-evals/` | workflow contract checks |
| `tools/` | small runtime support utilities |

---

## Current state

The AIDD-alignment gap plan has been completed in this repository.

That means the repo now contains:

- the instruction stack
- the local override layer
- the workflow prompts
- the skill entrypoints
- the review and user-testing workflow set
- the workflow eval scaffolding
- the onboarding and setup documentation

The gap plan remains useful as a **historical and architectural record**, but the runtime itself is already present.

---

## Contributors

- [@albrp97](https://github.com/albrp97)
