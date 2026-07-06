---
name: Create Tickets
description: Turn the approved phase and epic plan into an ordered backlog and per-ticket execution units with scope, dependencies, acceptance criteria, and AI-safe sequencing.
---

You have to create the tickets or user stories for `${PROJECT_OR_REPO}` after the objective, problem/users/success, scope, capability map, epic, and phase layers are complete.

A ticket is the smallest planning unit that should move into implementation as a single coherent item of work. It is not the whole epic, not the whole phase, and not just a vague reminder note.

## What a ticket is

A ticket is:
- an executable unit of work
- small enough to build, test, review, and merge coherently
- tied to a specific phase and epic
- explicit about scope, dependencies, validation, and next/previous sequencing

A ticket can be written as a **user story** if the repo prefers that style, but it still needs the same execution metadata.

## Why tickets exist

Use tickets to:
- turn the planning layers into actionable work
- keep work small enough for implementation, review, and PR flow
- make dependencies and sequence explicit
- make priority explicit instead of implied
- define done boundaries, acceptance criteria, and validation expectations
- give AI a safe unit for one-ticket-at-a-time execution

## Outcome

Leave the repository with:
- an ordered backlog
- clearly defined tickets
- one execution boundary per ticket
- enough metadata for AI or humans to pick up the next ticket safely

Use this storage model by default:
- `docs/planning/backlog.md` for the backlog index
- `docs/planning/tickets/TICKET-xxx.md` for one ticket per file

For very small projects, a single `docs/planning/tickets.md` file is acceptable, but the default should be:
- one backlog index
- one file per ticket

## Where this layer belongs

This workflow comes after:
- objective discovery
- problem / users / success discovery
- scope definition
- capability map creation
- epic creation
- phase creation

This workflow comes before:
- implementation of individual tickets
- branch / PR execution for a specific ticket

## Required source order

Use sources in this order of trust:

1. `vision.md`
2. `docs/specs/project-scope.md`
3. `docs/specs/capability-map.md`
4. `docs/planning/epics.md`
5. `docs/planning/phases.md`
6. specs, acceptance criteria, test expectations, rollout constraints
7. direct admin clarification

If sources conflict, prefer the approved phase/epic planning layer and record the mismatch.

## Workflow

### 1. Gather ticket inputs

Inspect:
- `vision.md`
- `docs/specs/project-scope.md`
- `docs/specs/capability-map.md`
- `docs/planning/epics.md`
- `docs/planning/phases.md`
- relevant specs, contracts, and test expectations

Extract:
- the active phase boundaries
- the epic and capability boundaries inside each phase
- the smallest coherent slices of work that can be built and validated
- dependencies that force ordering
- acceptance expectations that must be preserved

### 2. Define the backlog strategy

Organize tickets so they can be taken **one by one**.

Default ordering logic:
1. current phase before later phases
2. epic dependencies before dependent epics
3. enabling tickets before consumer tickets
4. highest-value or highest-risk items first when dependency order allows it
5. shortest path to a usable milestone when ties still remain

### 2A. Define priority explicitly

Every ticket must have both:
- a **priority rank** in the backlog
- a **priority reason** explaining why it sits there

Use this priority decision order:
1. blocked tickets cannot be higher than ready tickets
2. current-phase tickets come before later-phase tickets
3. hard dependencies come before dependent work
4. tickets that unlock many others move up
5. tickets that deliver early user value move up
6. tickets that retire high delivery risk move up
7. if still tied, prefer the smaller coherent ticket that advances the milestone sooner

Use these labels:
- **P0**: critical path / unblocker / must-do now
- **P1**: high priority in the active phase
- **P2**: important but not next
- **P3**: later or optional

### 3. Break work into ticket-sized units

Create tickets that are:
- small enough to implement and review coherently
- large enough to deliver one meaningful step
- narrow enough that acceptance can be tested

Avoid tickets that are:
- full epics
- mixed across unrelated epics
- vague placeholders like "do backend" or "finish phase 1"

### 4. Define the information every ticket needs

For every ticket record:
- **Ticket ID**
- **Title**
- **Priority rank**
- **Priority label**
- **Priority reason**
- **Phase**
- **Epic**
- **Objective**
- **Scope**
- **Out of scope**
- **Why this ticket exists**
- **Inputs / dependencies**
- **Previous ticket**
- **Next ticket**
- **Acceptance criteria**
- **Validation / tests**
- **Implementation steps**
- **Risks / notes**
- **Status**

### 5. Define the metadata

The backlog and ticket files must include:

| Field | Meaning |
|---|---|
| Status | todo, ready, in-progress, blocked, done |
| Priority rank | execution order within the backlog |
| Priority label | P0, P1, P2, or P3 |
| Priority reason | why this ticket is ordered here |
| Phase | owning phase |
| Epic | owning epic |
| Capability links | supporting capability IDs |
| Last reviewed | date ticket was updated |
| Depends on | prerequisite tickets or external blockers |
| Previous | immediately preceding ticket if sequence matters |
| Next | immediately following ticket if sequence matters |
| Confidence | high, medium, or low |
| Open questions | unresolved execution uncertainty |

### 6. Write the backlog index

Create or update `docs/planning/backlog.md` with this structure:

```markdown
# Backlog: [Project Name]

## Metadata
| Field | Value |
|---|---|
| Status | ... |
| Active phase | ... |
| Ordering rule | ... |
| Last reviewed | ... |
| Derived from | ... |
| Confidence | ... |
| Open questions | ... |

## Backlog Order
| Rank | Ticket ID | Title | Priority | Phase | Epic | Status | Depends on | Next | Priority Reason |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TICKET-001 | ... | P0 | PHASE-001 | EPIC-001 | ready | ... | TICKET-002 | ... |

## Phase Views

### PHASE-001
- TICKET-001
- TICKET-002

## Blocked / Deferred
- ...
```

### 7. Write one file per ticket

Create or update `docs/planning/tickets/TICKET-xxx.md` with this structure:

```markdown
# TICKET-001: [Title]

## Metadata
| Field | Value |
|---|---|
| Status | todo / ready / in-progress / blocked / done |
| Priority rank | ... |
| Priority label | P0 / P1 / P2 / P3 |
| Priority reason | ... |
| Phase | PHASE-... |
| Epic | EPIC-... |
| Capability links | CAP-... |
| Last reviewed | ... |
| Depends on | TICKET-... |
| Previous | TICKET-... |
| Next | TICKET-... |
| Confidence | ... |
| Open questions | ... |

## Objective
[What this ticket is supposed to achieve]

## Why This Ticket Exists
[How it supports the epic/phase outcome]

## Scope
- ...

## Out of Scope
- ...

## Inputs / Dependencies
- ...

## Acceptance Criteria
1. ...

## Validation
- Unit/integration/functional checks
- Evidence expected when done

## Implementation Steps
1. ...
2. ...
3. ...

## Risks / Notes
- ...
```

### 8. Explain how AI should use the tickets

AI should use the backlog and ticket files to:
- select the **highest-ranked ready** ticket unless told otherwise
- stay inside the ticket scope boundary
- inherit phase and epic intent automatically
- respect previous/next and dependency order
- run the validation required by the ticket before calling it done

AI should not:
- mix multiple unrelated tickets in one implementation pass
- jump to later-phase tickets without approval
- ignore out-of-scope boundaries defined in the ticket

### 9. Ask admin questions only when needed

Only escalate when the repo cannot answer:
- Should this work be one ticket or split into two?
- Which ticket should be first when several are technically possible?
- What acceptance evidence is required for this ticket to count as done?
- Are there business or rollout reasons to keep two seemingly related tasks separate?

### 10. Repair ambiguity before moving on

- If a ticket is too large, split it.
- If two tickets cannot be executed independently, merge or resequence them.
- If a ticket has no clear validation, refine it before adding it to the ready backlog.
- If a ticket crosses epic or phase boundaries without good reason, fix the boundary.

## Rules

1. Tickets are execution units, not mini-epics.
2. Every ticket must belong to a phase and an epic.
3. Every ticket needs explicit scope and out-of-scope boundaries.
4. Tickets should be executable one by one in backlog order.
5. If the backlog order is unclear, fix sequencing before implementation starts.
6. Priority must be explicit, not guessed from file position alone.

## Deliverables

Produce:
1. `docs/planning/backlog.md`
2. `docs/planning/tickets/TICKET-xxx.md` files
3. only the unresolved admin questions that truly block execution planning
