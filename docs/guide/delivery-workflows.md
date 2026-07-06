# Delivery Workflows

> Reusable discovery, setup, and implementation workflows for turning Harmonic Coding into an actual repo delivery system.

This guide adds the missing operational layer between the research/manuals in this repo and the day-to-day work of defining, setting up, and shipping software. It is built around twenty-three reusable prompt files:

- `.github/prompts/create-repository-map.prompt.md`
- `.github/prompts/discover-project-objective.prompt.md`
- `.github/prompts/discover-problem-users-success.prompt.md`
- `.github/prompts/define-project-scope.prompt.md`
- `.github/prompts/create-capability-map.prompt.md`
- `.github/prompts/create-epics.prompt.md`
- `.github/prompts/create-phases.prompt.md`
- `.github/prompts/create-tickets.prompt.md`
- `.github/prompts/review-planning-layer.prompt.md`
- `.github/prompts/review-phase-feedback.prompt.md`
- `.github/prompts/groom-backlog.prompt.md`
- `.github/prompts/replan-when-necessary.prompt.md`
- `.github/prompts/run-preimplementation-checklist.prompt.md`
- `.github/prompts/setup-project-workflow.prompt.md`
- `.github/prompts/implement-feature-workflow.prompt.md`
- `.github/prompts/review-pr-workflow.prompt.md`
- `.github/prompts/review-security-workflow.prompt.md`
- `.github/prompts/review-hotspots-workflow.prompt.md`
- `.github/prompts/triage-pr-comments-workflow.prompt.md`
- `.github/prompts/create-user-test-scripts.prompt.md`
- `.github/prompts/run-user-test-workflow.prompt.md`
- `.github/prompts/run-markdown-pipeline.prompt.md`
- `.github/prompts/pilot-runtime-workflow.prompt.md`

Use the repository-map workflow first, then objective, problem/users/success, scope, capability map, epics, phases, tickets, and review gates. The master pre-implementation checklist ties those together before feature work starts. Use the setup workflow when a repository still needs its branch strategy, CI/CD, quality gates, and release flow defined. Use the feature workflow when a ticket is already defined and the job is to deliver it through code, tests, PR, and post-push feedback loops. Use the dedicated review, user-testing, pipeline, and pilot workflows once the runtime layer is active and the repository needs stricter operational discipline.

## What these workflows are for

### 1. Repository map workflow

This workflow is for creating a durable map of the repository structure before deeper planning starts.

It forces the agent to:
- inspect the actual path layout
- record important files and folders
- write one simple sentence for what exists at each path
- create a reusable navigation artifact for both humans and AI

### 2. Project objective workflow

This workflow is for the first pass on a repository, before epics, phases, setup, or delivery automation.

It forces the agent to:
- extract the objective from evidence instead of assumptions
- identify where the real source of truth lives
- write the result to a durable repo document
- capture metadata, confidence, and open questions
- make non-goals explicit before the backlog expands

### 3. Problem, users, and success workflow

This workflow is for the second planning pass, after the high-level objective exists but before the backlog tree is decomposed.

It forces the agent to:
- define the actual pain being solved
- identify the primary user and affected secondary users
- define the outcome that matters most
- turn vague goals into success criteria and outcome signals
- surface the missing admin inputs that cannot be inferred safely

### 4. Scope workflow

This workflow is for fixing the delivery boundary before decomposition starts.

It forces the agent to:
- define the current horizon explicitly
- separate in-scope, out-of-scope, and deferred work
- capture assumptions, dependencies, constraints, and risks
- write a durable scope file plus a short summary in `vision.md`
- surface only the scope questions that truly need admin confirmation

### 5. Capability map workflow

This workflow is for turning approved scope into a structured set of system abilities that can later become epics and tickets.

It forces the agent to:
- map approved scope to concrete capabilities
- group capabilities into coherent domains
- distinguish now vs later capability
- link each capability back to user value or operational need
- produce a durable capability file instead of jumping straight to tickets

### 6. Epic workflow

This workflow is for turning the capability map into outcome-based workstreams that AI and humans can actually plan around.

It forces the agent to:
- group related capabilities by user or operational outcome
- define the boundary and validation intent of each epic
- make dependencies and risks visible before ticketing
- record how the epic should be used for later phase and ticket planning
- avoid turning the plan into technology buckets or premature tickets

### 7. Phase workflow

This workflow is for turning outcome-based epics into ordered milestone slices that guide delivery.

It forces the agent to:
- sequence epics into a practical delivery path
- define what each milestone is supposed to achieve
- capture entry and exit conditions for each phase
- preserve rollout, dependency, and risk logic before ticketing starts
- record how AI should stay inside the active phase boundary

### 8. Ticket workflow

This workflow is for turning phase and epic plans into one-ticket-at-a-time execution units.

It forces the agent to:
- create the backlog order explicitly
- define each ticket's scope, objective, and acceptance boundary
- record previous/next sequencing and dependencies
- store tickets in a durable backlog structure
- keep implementation work aligned with one ticket at a time

### 9. Layer review workflow

This workflow is for reviewing any planning layer before the next one proceeds.

It forces the agent to:
- check completeness, consistency, and readiness
- compare the layer against adjacent layers
- approve or reject the layer explicitly
- catch problems early without defaulting to large rewrites

### 10. Phase feedback workflow

This workflow is for reviewing a completed or partially completed phase and capturing lessons.

It forces the agent to:
- compare planned vs actual delivery
- capture lessons, drift, and newly discovered risks
- update downstream planning only when warranted
- decide whether change control is actually necessary

### 11. Backlog grooming workflow

This workflow is for keeping the backlog executable while work continues.

It forces the agent to:
- identify the next ready ticket
- detect blocked, stale, duplicate, or oversized tickets
- keep ticket ordering and dependencies healthy
- fix routine backlog issues without escalating to replanning

### 12. Replanning / change-control workflow

This workflow is for exceptional cases where real evidence shows the plan is no longer valid.

It forces the agent to:
- prove that a material change exists
- identify the smallest affected planning layer
- prefer local adjustment over broad replanning
- preserve the upfront plan unless reality clearly invalidates it

### 13. Master pre-implementation checklist

This workflow is the ordered list of workflows to follow before implementation begins.

It forces the agent to:
- run the repo-shaping workflows in the correct order
- confirm the required output files exist
- stop implementation from starting before the planning and setup baseline is real

### 14. Project setup workflow

This workflow is for the first serious pass on a project or for retrofitting an existing repo that has partial automation.

It forces the agent to:
- understand what the project does
- inspect the actual stack before choosing tools
- choose a lean baseline instead of stacking fashionable tools
- wire the branch, commit, PR, CI/CD, test, and release flow together
- finish with executable docs and working repo changes

### 15. Feature implementation workflow

This workflow is for ticket delivery after the repo already has a baseline engineering system.

It forces the agent to:
- review the ticket before coding
- baseline the current product with tests first
- implement the smallest complete change
- update the relevant documentation when behavior or workflows changed
- re-run local gates before push
- create the branch and PR cleanly
- stay in the CI/review loop until the PR is actually merge-ready

### 16. PR review workflow

This workflow is for reviewing a PR or change set against scope, validation, docs, and merge readiness.

It forces the agent to:

- review against requirements first
- check tests and documentation, not just source changes
- separate blockers from non-blocking suggestions
- make merge-readiness explicit

### 17. Security review workflow

This workflow is for focused security review of a code, setup, or workflow change.

It forces the agent to:

- identify the real security surface
- review relevant auth, secret, input, logging, and workflow risk
- report concrete findings by severity

### 18. Hotspot review workflow

This workflow is for prioritizing review effort around risky files.

It forces the agent to:

- identify high-risk files using size, churn, complexity, and recency signals
- explain the dominant risk signal
- recommend the right level of scrutiny

### 19. PR comment triage workflow

This workflow is for classifying review comments into already-addressed versus still-open work.

It forces the agent to:

- read the review context before assuming resolution
- keep unresolved issues visible
- turn remaining review feedback into explicit repair items

### 20. User-test script workflow

This workflow is for deriving human-run and agent-run user tests from journeys, phases, epics, tickets, or release candidates.

It forces the agent to:

- start from the user path
- define expected outcomes in observable language
- create durable scripts and evidence expectations

### 21. Run user-test workflow

This workflow is for executing user tests and turning findings into follow-up work.

It forces the agent to:

- capture evidence instead of only a pass/fail label
- classify results clearly
- feed failures back into planning or backlog work

### 22. Markdown pipeline workflow

This workflow is for running a markdown checklist or task list as a strict ordered pipeline.

It forces the agent to:

- parse steps carefully
- execute one step at a time
- stop on blockers instead of skipping
- keep task text treated as untrusted data

### 23. Runtime pilot workflow

This workflow is for piloting the current Harmonic Coding runtime on real work and hardening it.

It forces the agent to:

- test the runtime on actual setup or implementation work
- capture friction and ambiguity
- propose the smallest useful tightening changes

## Repository map workflow: what good looks like

This workflow should leave a repo with:

1. A durable path map.
2. Important files and folders listed by path.
3. One simple sentence explaining each important path.
4. A navigation artifact AI can consult before broad search.

## Objective workflow: what good looks like

The objective workflow should leave a repo with:

1. A `vision.md` or equivalent source-of-truth file.
2. A clear statement of purpose, user, scope, and success criteria.
3. Explicit non-goals.
4. Evidence showing where the objective came from.
5. Confidence and open questions captured as metadata instead of hidden uncertainty.

## Problem/users/success workflow: what good looks like

This workflow should leave a repo with:

1. A concrete problem statement, not just a solution label.
2. One clearly ranked primary user and any relevant secondary users.
3. A stated desired outcome.
4. Measurable or at least observable success criteria.
5. Metadata showing confidence, source files, and unresolved questions.

## Scope workflow: what good looks like

This workflow should leave a repo with:

1. A defined delivery horizon such as MVP, phase, pilot, or release.
2. A crisp in-scope list.
3. A crisp out-of-scope list.
4. A separate deferred/later list.
5. Assumptions, constraints, dependencies, and risks recorded in one place.

## Capability map workflow: what good looks like

This workflow should leave a repo with:

1. A readable set of capability groups.
2. Capabilities written as system abilities, not implementation tasks.
3. A priority distinction between now, later, and optional capability.
4. A link from each capability to user value or operational need.
5. Enough structure to derive epics cleanly.

## Epic workflow: what good looks like

This workflow should leave a repo with:

1. A small, readable set of outcome-based epics.
2. Every in-scope capability assigned to an epic.
3. Clear epic boundaries, dependencies, and risks.
4. A validation idea for each epic.
5. Enough structure to derive phases and tickets cleanly.

## Phase workflow: what good looks like

This workflow should leave a repo with:

1. A small, readable set of ordered phases.
2. Every in-scope epic assigned to a phase.
3. A clear milestone outcome for each phase.
4. Entry and exit conditions that explain readiness.
5. Enough sequencing structure to derive tickets cleanly.

## Ticket workflow: what good looks like

This workflow should leave a repo with:

1. An ordered backlog.
2. One coherent execution unit per ticket.
3. Every ticket tied to a phase and an epic.
4. Previous/next, dependency order, and priority made explicit.
5. Scope, objective, acceptance, and validation defined for each ticket.

## Layer review workflow: what good looks like

This workflow should leave a repo with:

1. An explicit approve / revise decision for each reviewed layer.
2. The specific problems recorded instead of implied.
3. A clean handoff to the next layer only when the current layer is ready.

## Phase feedback workflow: what good looks like

This workflow should leave a repo with:

1. A comparison of planned vs actual phase outcome.
2. Lessons learned and risks captured.
3. A clear decision on whether downstream planning changes are actually needed.

## Backlog grooming workflow: what good looks like

This workflow should leave a repo with:

1. A clear next-ready ticket.
2. Blocked, stale, or oversized tickets identified.
3. Backlog order corrected without unnecessary replanning.

## Replanning / change-control workflow: what good looks like

This workflow should leave a repo with:

1. A documented decision on whether replanning is needed.
2. The smallest affected layer identified.
3. Plan changes made only when material evidence justifies them.

## Master pre-implementation checklist: what good looks like

This workflow should leave a repo with:

1. The full planning and setup sequence completed in order.
2. The required planning artifacts present.
3. A clear implementation-readiness decision before feature work starts.

## Project definition layer map

Use these layers in order:

| Layer | Purpose | Preferred file/output | Stability |
|---|---|---|---|
| Repository map | Navigation map of important repo paths | `docs/planning/repo-map.md` | Medium |
| Objective | Why the project exists | `vision.md` | Stable |
| Problem / users / success | What pain matters, for whom, and what winning looks like | `vision.md` | Stable |
| Scope | What is in and out for the current horizon | `vision.md` or `docs/specs/project-scope.md` | Stable per phase |
| Capability map | What the system must be able to do | `docs/specs/capability-map.md` | Medium |
| Epics | Outcome-based workstreams | `docs/planning/epics.md` or issues/milestones | Medium |
| Phases | Delivery order and milestone grouping | `docs/planning/phases.md` or roadmap board | Medium |
| Tickets | Executable implementation work | `docs/planning/backlog.md` + `docs/planning/tickets/` or tracker issues / project board | Volatile |
| Reviews | Approval, feedback, and change decisions | `docs/planning/reviews/` | Volatile |

The first two layers belong in `vision.md` because they should stay short, durable, and available to every implementation session.

## Repository map layer: where to record it and how to structure it

Record:
- the full map in `docs/planning/repo-map.md`

Use this structure:

| Section | Purpose |
|---|---|
| Metadata | Status, coverage, evidence, open questions |
| Top-Level Paths | Main files and folders at the repo root |
| Source Paths | Main source-code areas |
| Test Paths | Main test areas |
| Docs and Planning Paths | Documentation and planning paths |
| Automation and Infrastructure Paths | CI/CD, infra, deployment, and automation paths |
| Notes | Structural caveats or exclusions |

## Scope layer: where to record it and how to structure it

Record:
- a short scope summary in `vision.md`
- the full boundary in `docs/specs/project-scope.md`

Use this structure:

| Section | Purpose |
|---|---|
| Metadata | Status, horizon, confidence, evidence, open questions |
| Scope Summary | One-paragraph boundary statement |
| In Scope Now | What must be delivered in the current horizon |
| Out of Scope Now | What is explicitly excluded |
| Deferred / Later | Useful but intentionally postponed work |
| Assumptions | Statements the scope depends on |
| Dependencies | External systems, approvals, teams, or data |
| Constraints | Timing, legal, cost, staffing, or technical limits |
| Risks to Scope | What could force scope change |
| Evidence | Files/issues/tests that justify the boundary |

## Capability map layer: where to record it and how to structure it

Record:
- the full map in `docs/specs/capability-map.md`

Use this structure:

| Section | Purpose |
|---|---|
| Metadata | Status, coverage, confidence, evidence, open questions |
| Capability Groups | Main domains of system ability |
| Capability Table | Capability ID, description, user served, outcome supported, priority, dependency, evidence |
| Coverage Check | Confirms all in-scope areas are represented |
| Deferred / Later Capabilities | Recognized but postponed abilities |
| Open Questions | Capability ambiguities that still require clarification |

## Epic layer: where to record it and how to structure it

Record:
- the full epic breakdown in `docs/planning/epics.md`

Use this structure:

| Section | Purpose |
|---|---|
| Metadata | Status, coverage, confidence, evidence, open questions |
| Epic Index | Quick scan of epic IDs, outcomes, users, dependencies, priority |
| Epic Details | Full breakdown of each epic |
| Capabilities Included | Shows what the epic owns |
| In Scope / Out of Scope | Prevents epic drift |
| Dependencies | Shows sequencing and blocking relationships |
| Risks / Assumptions | Captures planning risk early |
| Validation | Defines how the epic will later be checked |
| Suggested First Ticket Areas | Gives AI a safe starting point for ticket generation |
| Coverage Check | Confirms all in-scope capabilities are assigned |
| Open Questions | Unresolved grouping or sequencing questions |

## Phase layer: where to record it and how to structure it

Record:
- the full phase plan in `docs/planning/phases.md`

Use this structure:

| Section | Purpose |
|---|---|
| Metadata | Status, sequencing strategy, coverage, confidence, evidence, open questions |
| Phase Index | Quick scan of phase IDs, milestone outcomes, epics, dependencies |
| Phase Details | Full breakdown of each phase |
| Epics Included | Shows what the phase owns |
| Entry Conditions | What must be true before the phase starts |
| Exit Conditions | What must be true before the phase is considered complete |
| Dependencies | Shows sequence and blocking relationships |
| Risks | Captures rollout and delivery risk |
| Validation Focus | Defines what must be proven at this milestone |
| Suggested Ticket Sequencing | Gives AI a safe path for decomposition |
| Coverage Check | Confirms all in-scope epics are assigned |
| Open Questions | Unresolved sequencing or milestone questions |

## Ticket layer: where to record it and how to structure it

Record:
- the ordered backlog in `docs/planning/backlog.md`
- the ticket details in `docs/planning/tickets/TICKET-xxx.md`

For very small repos, a single `docs/planning/tickets.md` file is acceptable, but the default should be:
- one backlog index
- one file per ticket

Use this structure:

| Section | Purpose |
|---|---|
| Backlog Metadata | Active phase, confidence, evidence, open questions |
| Backlog Order | Rank, priority label, phase, epic, status, dependencies, next ticket, priority reason |
| Phase Views | Quick ticket grouping by phase |
| Blocked / Deferred | Tickets not ready for execution |
| Ticket Metadata | Status, priority rank, priority label, priority reason, phase, epic, capability links, prev/next, confidence |
| Objective | What this ticket is supposed to achieve |
| Why This Ticket Exists | How it supports the epic and phase |
| Scope / Out of Scope | Hard execution boundary |
| Inputs / Dependencies | What must exist before starting |
| Acceptance Criteria | What must be true for completion |
| Validation | Which tests/evidence prove the ticket is done |
| Implementation Steps | Suggested execution sequence |
| Risks / Notes | Important caveats or blockers |

## Review layer: where to record it and how to structure it

Record:
- planning layer reviews in `docs/planning/reviews/<layer>-review.md`
- phase feedback in `docs/planning/reviews/PHASE-xxx-review.md`
- backlog grooming notes optionally in `docs/planning/reviews/backlog-grooming.md`
- change-control decisions in `docs/planning/reviews/change-control.md`

Use this structure:

| Review Type | Core sections |
|---|---|
| Layer review | decision, checks, required revisions, carry-forward notes |
| Phase feedback | planned vs delivered, lessons, follow-up actions, planning impact |
| Backlog grooming | next-ready ticket, blocked/stale items, split/merge/resequence actions |
| Change control | decision, trigger, evidence, smallest affected layer, required action |

## How to do the repository map well

1. Start from the actual repo tree, not assumptions.
2. Include important human-maintained files and folders.
3. Use one simple sentence per path.
4. Exclude or collapse noisy generated paths unless they matter operationally.
5. Update the map when the repo structure changes materially.

## How to do the scope layer well

1. Start from `vision.md` and the problem/users/success layer.
2. Tie the scope to a concrete horizon.
3. Convert vague ambition into explicit in-scope commitments.
4. Make out-of-scope items explicit to prevent backlog bloat.
5. Separate "later" from "never" or "not now."
6. Record why the boundary exists: assumptions, dependencies, constraints, risks.
7. Do not move to capabilities until the scope boundary is crisp.

## How to do the capability map well

1. Start from the approved scope, not from implementation ideas.
2. Extract abilities the system must provide.
3. Group those abilities into a small number of coherent domains.
4. Write each capability at the right level: what the system can do.
5. Mark each capability as now, later, or optional.
6. Check that every in-scope area is represented at least once.
7. Refine the map until it can cleanly produce epics.

## How to do the epic layer well

1. Start from the approved capability map, not from engineering tasks.
2. Group capabilities by delivered outcome, not by stack layer.
3. Keep each epic large enough to matter but small enough to reason about.
4. Define what belongs inside and outside each epic.
5. Record dependencies before phase planning starts.
6. Attach a validation idea so the epic has a real done boundary.
7. Refine the epics until phases and tickets can be derived without guesswork.

## How to do the phase layer well

1. Start from approved epics, not raw capabilities.
2. Choose and state the sequencing strategy explicitly.
3. Group epics into milestone slices that make delivery sense.
4. Define what each phase proves or unlocks.
5. Record entry and exit conditions so readiness is explicit.
6. Keep later-phase tickets out of early-phase planning by default.
7. Refine the phases until ticket generation can follow the sequence without guesswork.

## How to do the ticket layer well

1. Start from the active phase and its epics, not from random capability fragments.
2. Break work into one coherent execution unit at a time.
3. Give every ticket a hard scope and out-of-scope boundary.
4. Record previous/next, dependency, and priority relationships explicitly.
5. Order tickets by readiness, dependencies, value, risk reduction, and milestone impact.
6. Define acceptance and validation before implementation starts.
7. Prefer one ticket per file once the backlog stops being trivial.
8. Refine ticket size until each item can be implemented, reviewed, and merged cleanly.

## How to order and prioritize tickets

Use this default ordering rule:

1. ready tickets before blocked tickets
2. current phase before later phases
3. dependency-enabling tickets before dependent tickets
4. tickets that unlock more work before isolated work
5. tickets that create earlier user value or retire major delivery risk before lower-impact work
6. if still tied, prefer the smaller coherent ticket that advances the phase sooner

Use explicit labels:

| Label | Meaning |
|---|---|
| P0 | Critical path / unblocker / must-do now |
| P1 | High priority in the active phase |
| P2 | Important but not next |
| P3 | Later, optional, or low urgency |

## How to do the review workflows well

1. Put a review gate after each major planning layer.
2. Review for blocking issues, not style preference.
3. Capture lessons after phases before starting major downstream work.
4. Use backlog grooming for routine execution hygiene.
5. Use change control only when material evidence shows the plan is wrong.
6. Prefer local corrections over broad replanning.
7. Protect the upfront planning effort instead of rewriting the plan constantly.

## Master pre-implementation checklist

Before serious implementation starts, run these workflows in order:

1. Repository map
2. Objective
3. Problem / users / success
4. Scope
5. Capability map
6. Epics
7. Phases
8. Tickets / backlog
9. Review gates
10. Setup / CI/CD
11. Backlog grooming
12. Final implementation-readiness check

Required outputs:
- `docs/planning/repo-map.md`
- `vision.md`
- `docs/specs/project-scope.md`
- `docs/specs/capability-map.md`
- `docs/planning/epics.md`
- `docs/planning/phases.md`
- `docs/planning/backlog.md`
- `docs/planning/tickets/`
- `docs/planning/reviews/`

## What epics are and why AI needs them

Epics are the bridge between **capabilities** and **execution planning**.

They are useful because they:
- preserve user value when decomposition starts
- prevent AI from mixing unrelated work in one branch or ticket set
- give later workflows a stable planning unit for sequencing and validation
- make it easier to detect missing capabilities, hidden dependencies, or oversized tickets

AI should use epics to:
- choose which workstream it is decomposing
- generate tickets only inside the selected epic boundary
- inherit the epic's outcome, dependencies, and validation intent
- keep implementation and PR work aligned with the intended slice of value

## What the repository map is and why AI needs it

The repository map is the bridge between **raw repo structure** and **all later planning and implementation work**.

It is useful because it:
- reduces blind searching
- shows where planning, source, tests, and automation live
- gives future sessions a fast orientation artifact

AI should use it to:
- orient itself before broad search
- identify likely working areas faster
- update the map when major structural changes happen

## What phases are and why AI needs them

Phases are the bridge between **epics** and **ticket sequencing**.

They are useful because they:
- turn a set of epics into an ordered milestone plan
- prevent AI from generating later-work tickets too early
- make rollout and dependency logic explicit
- provide a milestone-level done boundary before implementation begins

AI should use phases to:
- identify the active delivery milestone
- constrain ticket generation to the active or approved next phase
- inherit phase sequencing, readiness, and validation expectations
- avoid planning work that belongs to later rollout stages unless explicitly requested

## What tickets are and why AI needs them

Tickets are the bridge between **phase planning** and **actual implementation work**.

They are useful because they:
- give AI one safe execution unit at a time
- keep scope small enough for coding, testing, review, and PR flow
- make backlog order and dependencies explicit
- define the done boundary at the level where implementation actually happens

AI should use tickets to:
- pick the highest-ranked ready ticket from the backlog
- stay inside that ticket's scope and acceptance criteria
- inherit epic and phase intent automatically
- use previous/next and dependency metadata to avoid sequencing mistakes
- finish validation before marking the ticket done

## What the review workflows are and why AI needs them

Review workflows are the bridge between **planning quality** and **execution reliability**.

They are useful because they:
- stop weak planning from propagating downstream
- capture lessons without forcing constant plan churn
- keep the backlog healthy during execution
- make replanning a controlled exception instead of a habit

AI should use them to:
- pause between layers and verify readiness
- compare planned vs actual outcomes after phases
- keep choosing the next ready ticket from a groomed backlog
- trigger change control only when routine fixes are no longer enough

## What data matters for the problem/users/success layer

Prioritize:
- user-facing pain points and support signals
- business or operational workflow bottlenecks
- acceptance criteria already present in issues or specs
- existing e2e/functional tests that imply what "working" means
- analytics, event names, dashboards, alerts, and SLAs if present
- persona names, consumer systems, or operator roles already named in docs/code
- deployment context and environment constraints that shape success

Do not let implementation details replace the problem definition.

## Metadata for the problem/users/success layer

Capture at minimum:

| Field | Why it matters |
|---|---|
| Status | Shows whether the layer is draft or trusted |
| Last reviewed | Prevents stale planning assumptions |
| Derived from | Preserves the evidence trail |
| Primary user | Forces prioritization |
| Secondary users | Makes tradeoffs explicit |
| Success horizon | Clarifies which release or timeframe matters |
| Outcome type | Distinguishes business vs operational vs technical wins |
| Confidence | Signals whether follow-up discovery is still needed |
| Open questions | Stops hidden uncertainty from leaking into epics |

## Recommended lean defaults

The point is not to install every possible platform. The point is to choose the smallest baseline that gives reliable delivery.

| Concern | Default | Add more only when needed |
|---|---|---|
| CI | GitHub Actions | Another CI system only when the host platform or org already requires it |
| Branching | Protected `main` + short-lived feature branches | Trunk-only flow only if the team already works that way |
| Commits | Existing repo convention | Conventional Commits when automated releases/changelogs benefit from them |
| PR governance | PR template + required checks + review requirement | Extra bots and approval layers only for real org needs |
| JS/TS formatting and linting | Biome for new repos, or keep ESLint + Prettier if already established | Separate overlapping tools only when migration is not worth it |
| JS/TS tests | Vitest | Add more runners only for a distinct gap |
| Browser functional tests | Playwright | Cypress only if already embedded in the team/tooling |
| Python quality | Ruff + pytest + mypy/pyright | Separate formatter/linter stacks only when already standardized |
| Static analysis | SonarQube when the org already uses it or needs centralized reporting | Skip it for small repos where CI + tests already cover the signal |
| Versioning | Manual semver tags for apps, Changesets for packages | Fully automated release tooling only when releases are frequent enough to justify it |

## Project setup workflow: what good looks like

The setup workflow should leave a repo with:

1. A short explanation of what the project is and how it ships.
2. Local commands for install, lint, test, and build.
3. A branch and PR convention that people can follow without tribal knowledge.
4. CI jobs for pull requests and pushes to the protected branch.
5. The right test layers for the product: unit, integration, and functional/end-to-end where they matter.
6. Release/versioning only when the repo actually publishes something.
7. A repair loop: when checks fail, the work continues until the system is green or genuinely blocked.

## Feature implementation workflow: what good looks like

The implementation workflow should leave a ticket at one of only three valid end states:

1. The PR is merge-ready.
2. The PR is merged.
3. A real external blocker exists and everything else has already been completed.

Anything earlier is only progress, not completion.

The completed work should include related documentation when the ticket changed:
- behavior
- setup
- commands
- configuration
- APIs or integrations
- operator/user-facing workflows

## Additional operational workflows: what good looks like

These workflows should leave a repo with:

1. clear PR review decisions
2. focused security findings when security-relevant work changed
3. hotspot-aware review prioritization
4. a repair loop for unresolved PR comments
5. user-test scripts and recorded results where usability matters
6. runnable markdown pipelines for ordered operations
7. pilot feedback that hardens the runtime before broader use

## Prompt usage

These files are meant to be reused directly in Copilot or adapted into project-local instructions:

- `.github/prompts/discover-project-objective.prompt.md`
- `.github/prompts/discover-problem-users-success.prompt.md`
- `.github/prompts/define-project-scope.prompt.md`
- `.github/prompts/create-capability-map.prompt.md`
- `.github/prompts/create-epics.prompt.md`
- `.github/prompts/create-phases.prompt.md`
- `.github/prompts/create-tickets.prompt.md`
- `.github/prompts/create-repository-map.prompt.md`
- `.github/prompts/review-planning-layer.prompt.md`
- `.github/prompts/review-phase-feedback.prompt.md`
- `.github/prompts/groom-backlog.prompt.md`
- `.github/prompts/replan-when-necessary.prompt.md`
- `.github/prompts/run-preimplementation-checklist.prompt.md`
- `.github/prompts/setup-project-workflow.prompt.md`
- `.github/prompts/implement-feature-workflow.prompt.md`
- `.github/prompts/review-pr-workflow.prompt.md`
- `.github/prompts/review-security-workflow.prompt.md`
- `.github/prompts/review-hotspots-workflow.prompt.md`
- `.github/prompts/triage-pr-comments-workflow.prompt.md`
- `.github/prompts/create-user-test-scripts.prompt.md`
- `.github/prompts/run-user-test-workflow.prompt.md`
- `.github/prompts/run-markdown-pipeline.prompt.md`
- `.github/prompts/pilot-runtime-workflow.prompt.md`

Use them as:
- prompt templates in editors that surface `.prompt.md` files
- copy/paste workflow prompts in Copilot Chat or Copilot CLI
- starting points for custom skills when a team wants stricter automation or routing
- the source workflows loaded by the local skill entrypoints in `harmonic-custom/skills/`

## When to turn a workflow into a skill

Keep the prompt file when the workflow is mostly guidance and repository inspection.

Turn it into a skill when you need:
- a permanent trigger description
- a repeatable instruction contract
- project-specific constraints
- integration with a larger skill-routing system such as AIDD or OpenCode

In that case, keep the same sequence:
1. research or review first
2. execute the change
3. run the checks
4. stay in the review/repair loop until the quality bar is met

## Admin clarification question bank

Ask these only when the repository, docs, backlog, and delivery context do not answer them with enough confidence.

### Objective

- What is the single most important reason this project exists?
- What would make this project a failure even if the code works?
- What is explicitly out of scope for the current horizon?

### Problem / users / success

- What pain is urgent enough that this project must solve it now?
- Who is the primary user or consuming system if there are several candidates?
- What would the admin call "success" after the first meaningful release?
- Which metric, workflow improvement, or operational signal matters most?
- What tradeoff wins if user convenience conflicts with internal implementation convenience?

### Scope

- What must be included in the first meaningful release?
- What is intentionally deferred even if it sounds useful?
- Are there legal, operational, or dependency boundaries that limit scope?

### Capability map

- Which capabilities are must-have, should-have, and later?
- Which user journeys are mission-critical?
- Which integrations are mandatory vs optional?

### Epics

- What are the main outcome-based workstreams?
- Which epic delivers user value first?
- Which epics depend on external teams or systems?

### Phases

- What delivery milestone defines phase 1?
- Are there fixed deadlines, pilots, or rollout windows?
- Which risks must be retired earlier than others?

### Tickets

- What acceptance criteria make this ticket complete?
- What evidence or tests must exist before the ticket can close?
- Does the ticket depend on another ticket, migration, integration, or approval?

### Reviews / change control

- Is this issue serious enough to justify changing the plan, or is local correction enough?
- Which layer is the smallest one that actually needs to change?
- What lesson from the completed phase must be carried into later work?
- Which ticket is truly next-ready right now?
