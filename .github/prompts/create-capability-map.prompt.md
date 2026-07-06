---
name: Create Capability Map
description: Break the approved scope into a durable capability map that can be used to derive epics, phases, and tickets without mixing planning layers.
---

You have to build the capability map for `${PROJECT_OR_REPO}` after the objective, problem/users/success layer, and scope layer are defined.

The capability map is the structured list of what the system must be able to do within the approved scope. It is not yet the epic list and not yet the ticket list.

## Outcome

Leave the repository with a durable capability map that:
- covers the approved scope
- groups related capabilities coherently
- distinguishes must-have from later capability
- links each capability back to user value or operational need
- is detailed enough to derive epics and phases cleanly

Write the result to `docs/specs/capability-map.md`.

## Where this layer belongs

This workflow comes after:
- objective discovery
- problem / users / success discovery
- scope definition

This workflow comes before:
- epics
- phases
- tickets

## Required source order

Use sources in this order of trust:

1. `vision.md`
2. `docs/specs/project-scope.md`
3. specs, roadmap docs, acceptance criteria, milestone plans
4. existing tests, demo flows, support runbooks, and integration contracts
5. current code structure, route names, domain models, UI areas, integrations
6. direct admin clarification

If sources conflict, prefer the scope-approved source and record the mismatch.

## Workflow

### 1. Gather capability evidence

Inspect:
- `vision.md`
- `docs/specs/project-scope.md`
- relevant specs and contracts
- issues and milestone descriptions
- existing functional/e2e tests
- product surfaces in code: modules, pages, APIs, services, integrations

Extract:
- user-visible outcomes the system must support
- operational workflows the system must enable
- data or integration behaviors that are essential
- administrative/support capabilities that are required for the approved scope

### 2. Define capability groups

Group capabilities into a small number of coherent domains such as:
- user-facing workflows
- admin/operator workflows
- data/integration capabilities
- platform/reliability capabilities

Do not over-segment. The map should stay readable.

### 3. Write capabilities at the right level

Each capability should describe an ability, not an implementation task.

Good:
- "Users can submit and track delivery requests"
- "Operators can resolve routing exceptions"
- "The system can synchronize stop updates with the external planning API"

Bad:
- "Create `DeliveryRequestService`"
- "Add database table"
- "Write endpoint"

### 4. Prioritize capabilities

Mark each capability with a planning priority:
- **Now**: required for the current scope horizon
- **Later**: recognized but intentionally deferred
- **Optional**: nice-to-have, not required for the current horizon

### 5. Link capabilities back to value

For each capability, record:
- the user or system it serves
- the problem or outcome it supports
- any dependency or prerequisite capability

### 6. Define the metadata

The capability map must include:

| Field | Meaning |
|---|---|
| Status | draft, confirmed, or needs-review |
| Scope horizon | the horizon inherited from scope |
| Last reviewed | date capability map was updated |
| Derived from | files/issues/tests/contracts used |
| Coverage | whether the map covers all in-scope areas |
| Confidence | high, medium, or low |
| Open questions | unresolved capability gaps or overlaps |

### 7. Write the durable capability file

Create or update `docs/specs/capability-map.md` with this structure:

```markdown
# Capability Map: [Project Name]

## Metadata
| Field | Value |
|---|---|
| Status | ... |
| Scope horizon | ... |
| Last reviewed | ... |
| Derived from | ... |
| Coverage | complete / partial |
| Confidence | ... |
| Open questions | ... |

## Capability Groups

### Group: [Name]
Purpose: [why this group exists]

| Capability ID | Capability | Serves | Outcome Supported | Priority | Depends on | Evidence |
|---|---|---|---|---|---|---|
| CAP-001 | ... | ... | ... | Now | ... | ... |

## Coverage Check
- Which in-scope areas are covered
- Any in-scope area not yet represented

## Deferred / Later Capabilities
- ...

## Open Questions
- ...
```

### 8. Ask admin questions only when needed

Only escalate when the repo cannot answer:
- Which capability is absolutely required for the first useful release?
- Which capability looks desirable but should be pushed later?
- Which admin/operator/internal capabilities are required even if not visible to end users?
- Are there hidden business workflows or integrations the repo does not reveal yet?

### 9. Repair ambiguity before moving on

- If a capability sounds like a task, rewrite it at the capability level.
- If a capability is outside approved scope, move it to later or remove it.
- If a capability group overlaps another, merge or rename until the map is clean.

## Rules

1. Capabilities describe what the system must be able to do, not how it will be coded.
2. Every in-scope area should map to at least one capability.
3. Keep "later" capabilities visible but separate from "now."
4. Do not jump directly from problem statement to tickets without this layer.
5. If the capability map cannot support epic creation cleanly, refine it first.

## Deliverables

Produce:
1. `docs/specs/capability-map.md`
2. a capability coverage check against the approved scope
3. only the unresolved admin questions that truly block epic creation
