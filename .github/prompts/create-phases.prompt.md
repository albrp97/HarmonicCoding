---
name: Create Phases
description: Turn the approved epic set into ordered delivery phases with milestone intent, sequencing logic, and AI-safe execution boundaries.
---

You have to create the phases for `${PROJECT_OR_REPO}` after the objective, problem/users/success, scope, capability map, and epic layers are complete.

A phase is an ordered delivery milestone that groups one or more epics into a sequence that makes sense for dependency management, rollout safety, validation, and user value delivery. It is not a ticket and not just a calendar label.

## What a phase is

A phase is:
- a milestone-oriented delivery slice
- a sequencing decision built from epic dependencies and rollout logic
- a statement of what should be delivered before the next major step begins

A phase is not:
- a single ticket
- a technology layer
- an arbitrary time box with no delivery meaning

## Why phases exist

Use phases to:
- order epics into a practical delivery path
- identify what must come first for value, risk reduction, or dependency reasons
- control rollout scope and validation burden
- give AI a stable milestone boundary before ticket generation and implementation planning
- prevent "everything now" planning that ignores sequencing reality

## Outcome

Leave the repository with a durable phase plan that:
- sequences epics into meaningful delivery milestones
- explains why the ordering exists
- defines what is expected at the end of each phase
- records dependencies, risks, and validation expectations
- can be used as the parent structure for ticket generation and delivery tracking

Write the result to `docs/planning/phases.md` unless the repository already has an established equivalent planning file.

## Where this layer belongs

This workflow comes after:
- objective discovery
- problem / users / success discovery
- scope definition
- capability map creation
- epic creation

This workflow comes before:
- tickets
- feature implementation planning

## Required source order

Use sources in this order of trust:

1. `vision.md`
2. `docs/specs/project-scope.md`
3. `docs/specs/capability-map.md`
4. `docs/planning/epics.md`
5. roadmap docs, milestone plans, release constraints, rollout plans
6. tests, demo flows, deployment or integration dependencies
7. direct admin clarification

If sources conflict, prefer the approved epic/source-of-truth planning layer and record the mismatch.

## Workflow

### 1. Gather sequencing inputs

Inspect:
- `vision.md`
- `docs/specs/project-scope.md`
- `docs/specs/capability-map.md`
- `docs/planning/epics.md`
- roadmap docs or milestone plans
- deployment, integration, and validation constraints

Extract:
- epic dependencies
- which epics unlock later work
- which epics reduce the most risk early
- which epics create the first meaningful user value
- which rollout, data, compliance, or integration factors force ordering

### 2. Define the phase strategy

Choose the sequencing principle that best matches the project:
- value-first
- dependency-first
- risk-first
- rollout-first
- integration-first

You may combine them, but state the dominant rule clearly.

### 3. Group epics into ordered phases

Create phases by grouping epics that should be delivered together because they:
- unlock the same milestone
- share the same release or rollout boundary
- depend on the same readiness conditions
- should be validated together before moving forward

Each phase should answer:
- what milestone it achieves
- which epics it contains
- why it comes before the next phase

### 4. Define the phase boundary and completion meaning

For every phase record:
- **Phase ID**
- **Title**
- **Milestone outcome**
- **Epics included**
- **Why this phase exists**
- **Entry conditions**
- **Exit conditions**
- **Dependencies**
- **Risks**
- **Validation focus**

### 5. Define the metadata

The phase document must include:

| Field | Meaning |
|---|---|
| Status | draft, confirmed, or needs-review |
| Scope horizon | inherited from scope |
| Sequencing strategy | value-first, risk-first, etc. |
| Last reviewed | date phases were updated |
| Derived from | files/tests/contracts/issues used |
| Coverage | whether all in-scope epics are assigned |
| Confidence | high, medium, or low |
| Open questions | unresolved sequencing or milestone questions |

### 6. Write the durable phase file

Create or update `docs/planning/phases.md` with this structure:

```markdown
# Phases: [Project Name]

## Metadata
| Field | Value |
|---|---|
| Status | ... |
| Scope horizon | ... |
| Sequencing strategy | ... |
| Last reviewed | ... |
| Derived from | ... |
| Coverage | complete / partial |
| Confidence | ... |
| Open questions | ... |

## Phase Index
| Phase ID | Title | Milestone Outcome | Epics Included | Depends on |
|---|---|---|---|---|
| PHASE-001 | ... | ... | ... | ... |

## Phase Details

### PHASE-001: [Title]
**Milestone outcome:** ...
**Why this phase exists:** ...

**Epics included**
- EPIC-...

**Entry conditions**
- ...

**Exit conditions**
- ...

**Dependencies**
- ...

**Risks**
- ...

**Validation focus**
- ...

**Suggested ticket sequencing**
- ...

## Coverage Check
- Which in-scope epics are assigned to phases
- Any epic not yet assigned

## Open Questions
- ...
```

### 7. Explain how AI should use the phases

The phase document should be used by AI to:
- choose the current milestone before generating tickets
- avoid creating tickets for later phases too early
- inherit sequencing and validation expectations when planning implementation
- understand which dependencies must be satisfied before starting work
- keep PR and ticket execution aligned with the active phase boundary

AI should not ignore phases when they exist. Tickets and implementation prompts should default to the current active phase unless explicitly told otherwise.

### 8. Ask admin questions only when needed

Only escalate when the repo cannot answer:
- Which milestone should come first if value and dependency logic conflict?
- Is there a pilot, launch, or release boundary that defines a phase?
- Which epic must land early to reduce delivery risk the most?
- Are there rollout, compliance, migration, or partner constraints that force a different sequence than the repo implies?

### 9. Repair ambiguity before moving on

- If a phase contains too many unrelated epics, split it by milestone.
- If a phase has no clear milestone outcome, rewrite it or merge it.
- If an epic is assigned to a later phase despite being a hard dependency for an earlier one, fix the sequence.
- If the phase order cannot explain itself, refine the sequencing strategy.

## Rules

1. Phases are milestone boundaries, not arbitrary calendar buckets.
2. Every in-scope epic should map to a phase.
3. Each phase must have a clear exit condition.
4. Keep the number of phases small enough to reason about.
5. If the phase plan cannot guide ticket sequencing cleanly, refine it first.

## Deliverables

Produce:
1. `docs/planning/phases.md`
2. a coverage check against the epic map
3. only the unresolved admin questions that truly block ticket creation
