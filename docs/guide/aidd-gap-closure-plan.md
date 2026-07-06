# AIDD Gap Closure Plan

> Ordered plan for turning Harmonic Coding from a strong workflow documentation system into a more complete AI coding runtime.

**Status:** Complete. The phases below are now implemented in this repository and should be treated as the closed record of this gap-closure effort unless new gaps are identified later.

Harmonic Coding already has a stronger planning and repo-shaping system than AIDD in key areas:

- repository map
- objective
- problem / users / success
- scope
- capability map
- epics
- phases
- tickets / backlog
- review gates
- conservative change control

Do **not** replace that system. The goal is to **preserve the current planning stack** and add the missing operational layer around it.

## Target outcome

After this plan, Harmonic Coding should have:

1. always-loaded repo instructions
2. executable workflow commands or skills
3. stricter implementation and review enforcement
4. prompt and workflow evaluation in CI
5. user-testing and PR-repair workflows
6. a practical runtime for AI coding, not just a guide about how it should work

## Ordering rule

Build this in order:

1. **Foundation first** — persistent context and runtime structure
2. **Execution second** — implementation, review, and PR loops
3. **Validation third** — evals, CI gates, and user testing
4. **Scale last** — orchestration, templates, and upgrade-safe customization

Do not jump to parallel agents, prompt evals, or advanced automation before the instruction stack and execution rules are real.

## Phase status

| Phase | Status |
|---|---|
| 1. Always-loaded instruction stack | Complete |
| 2. Project override layer | Complete |
| 3. Executable commands or skills | Complete |
| 4. Strict TDD mode | Complete |
| 5. Dedicated review workflows | Complete |
| 6. Hotspot and churn analysis workflow | Complete |
| 7. First-class security rules | Complete |
| 8. User-testing workflows | Complete |
| 9. Prompt and workflow evals in CI | Complete |
| 10. Executable markdown pipelines and orchestration baseline | Complete |
| 11. Starter CI and release templates | Complete |
| 12. Pilot, review, and harden workflow | Complete |
| 13. Final repo and guide documentation for new-project usage | Complete |

## Phase 1 — Create the always-loaded instruction stack

### Why this comes first

This is the biggest gap versus AIDD. Right now Harmonic Coding explains the workflows well, but the rules are not yet loaded automatically at the start of every implementation session.

### What to create

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/`
  - `planning.instructions.md`
  - `implementation.instructions.md`
  - `testing.instructions.md`
  - `review.instructions.md`
  - `security.instructions.md`

### What these files should do

- make `vision.md` mandatory context before major work
- point agents to `docs/guide/delivery-workflows.md`
- point agents to the current planning artifacts
- define the implementation loop, review loop, and done criteria
- define when to stop and ask for human input
- define security and testing rules that must not be skipped

### Steps

1. Create `AGENTS.md` as the cross-tool root instruction file.
2. Mirror the same core rules into `.github/copilot-instructions.md`.
3. Split path-scoped or domain-scoped rules into `.github/instructions/*.instructions.md`.
4. Keep the root files short and stable; move detailed rules into the path-scoped files.
5. Add explicit references to `vision.md`, `docs/planning/`, and `docs/guide/delivery-workflows.md`.

### Done when

- a new session can orient itself from the instruction stack without opening multiple guides manually
- the same baseline rules apply across Copilot and other agent tools

## Phase 2 — Add a project override layer

### Why this matters

AIDD is stronger because it separates framework defaults from project-specific overrides. Harmonic Coding needs the same concept so the system can be reused without hardcoding every repo's rules into the root instructions.

### What to create

- `harmonic-custom/AGENTS.md`
- `harmonic-custom/config.yml`
- `harmonic-custom/skills/`

### What this layer should do

- override default workflow behavior per project
- store project-local switches such as stricter test gates
- hold project-specific skills without polluting the framework-level docs

### Steps

1. Define the override precedence: root instructions first, then `harmonic-custom/AGENTS.md` overrides.
2. Create a small `config.yml` schema for repo-level toggles.
3. Document which concerns belong in the shared framework and which belong in the local override layer.
4. Keep this layer upgrade-safe so future framework changes do not overwrite project rules.

### Done when

- Harmonic Coding can be reused across repos without forking the whole instruction stack

## Phase 3 — Turn the workflows into executable commands or skills

### Why this matters

Today the workflows are strong but mostly document-driven. AIDD is ahead because an agent can invoke a command or skill directly instead of reinterpreting a long guide every time.

### What to create

- a thin command or skill entrypoint for each major workflow
- index files that list the available commands and skills

### Minimum command set

1. planning bootstrap
2. pre-implementation checklist
3. setup / CI baseline
4. ticket implementation
5. planning-layer review
6. backlog grooming
7. phase feedback
8. change control

### Steps

1. Keep the existing `.github/prompts/*.prompt.md` files as the source workflows.
2. Create a command or skill layer that loads those workflows intentionally.
3. Make each command short; put the heavy logic in the reusable workflow body.
4. Add an index so agents can discover available commands without searching the whole repo.
5. Document the invocation pattern in one place.

### Done when

- the workflows are reusable as operations, not only as documents

## Phase 4 — Strengthen the implementation workflow with strict TDD mode

### Why this matters

The current implementation workflow correctly requires tests before and after changes, but AIDD is stricter about the failing-test-first loop. Harmonic Coding should add that option without forcing it where it does not fit.

### What to improve

- `.github/prompts/implement-feature-workflow.prompt.md`
- related implementation instructions in the new runtime stack

### What to add

- a default failing-test-first rule when the task is code behavior changeable through tests
- a rule for tiny, coherent execution slices
- a rule for periodic self-review during longer implementations
- a clearer rule for when integration or functional tests must be preferred over unit-only proof

### Steps

1. Add a strict TDD mode section to the implementation workflow.
2. Define when that mode is mandatory and when it is not practical.
3. Require the feature workflow to restate the proving test or validation target before coding.
4. Add a short review checkpoint for longer multi-step changes.

### Done when

- implementation sessions consistently prove behavior instead of relying on code inspection alone

## Phase 5 — Create dedicated review workflows

### Why this matters

This is one of the clearest AIDD advantages. Harmonic Coding has review ideas, but it does not yet have distinct operational workflows for hotspot review, security review, PR comment triage, and PR repair.

### What to create

- `review-pr-workflow.prompt.md`
- `review-security-workflow.prompt.md`
- `review-hotspots-workflow.prompt.md`
- `triage-pr-comments-workflow.prompt.md`

### What each one should do

| Workflow | Purpose |
|---|---|
| PR review | Review changed work against requirements, tests, docs, and architecture |
| Security review | Check auth, secrets, unsafe comparisons, injection risk, and high-confidence security mistakes |
| Hotspot review | Identify risky files using git history and complexity signals before merging |
| PR triage | Separate already-fixed review comments from still-open issues and drive the repair loop |

### Steps

1. Define the review inputs for each workflow.
2. Define the output format: findings, severity, file path, rationale, required action.
3. Reuse repo instructions instead of duplicating standards in every review workflow.
4. Make the PR triage flow branch-safe and non-destructive.

### Done when

- review becomes a repeatable system instead of a generic "check the PR" instruction

## Phase 6 — Add hotspot and churn analysis

### Why this matters

AIDD uses quantitative signals before qualitative review. Harmonic Coding should add a lean version of this so large, unstable, complex files get extra scrutiny.

### What to create

- a hotspot-analysis workflow
- documentation for the scoring inputs and interpretation

### Steps

1. Define the initial signal set: file size, churn, complexity, and recency.
2. Decide the smallest practical implementation for this repo.
3. Feed the results into PR review and refactor decisions.
4. Use it as extra scrutiny, not as an automatic rewrite trigger.

### Done when

- reviewers can identify high-blast-radius files before merging

## Phase 7 — Add security rules as first-class workflow inputs

### Why this matters

AIDD does not leave security as a vague expectation. It encodes review rules and domain-specific checks. Harmonic Coding should do the same.

### What to create

- a security guide for repo rules
- security-focused instructions for relevant paths
- a dedicated security review workflow if not already created in Phase 5

### Steps

1. Define a short set of non-negotiable security rules.
2. Encode path-specific security instructions where applicable.
3. Make the review workflows invoke the security rules explicitly.
4. Keep the rules concrete and high-signal; avoid a large generic checklist with little relevance.

### Done when

- security requirements are reusable and visible before PR review starts

## Phase 8 — Add user-testing workflows

### Why this matters

AIDD connects discovery outputs to human or agent-driven user testing. Harmonic Coding already values functional validation, so this is a natural extension.

### What to create

- `create-user-test-scripts.prompt.md`
- `run-user-test-workflow.prompt.md`

### What these should do

- derive test scripts from journeys, phases, epics, or tickets
- create both human-run and agent-run variants when practical
- capture evidence, screenshots, notes, and observed failures

### Steps

1. Define what the input artifact is: journey, ticket, feature, or release candidate.
2. Define the output format for test scripts and findings.
3. Connect the results back to backlog grooming, bug tickets, or phase feedback.
4. Require user-testing for releases or tickets where usability is part of the goal.

### Done when

- there is a direct path from planned user outcome to real usability validation

## Phase 9 — Add prompt and workflow evals in CI

### Why this matters

This is the most advanced missing capability. AIDD evaluates the prompt and skill system itself in CI. Harmonic Coding should add this only after the runtime and workflows are stable enough to test.

### What to create

- eval fixtures for important workflows
- CI jobs that run those evals
- a threshold or pass/fail rule

### Recommended first eval targets

1. pre-implementation checklist
2. setup / CI workflow
3. ticket implementation workflow
4. PR review workflow
5. PR triage workflow

### Steps

1. Start with a few high-value evals, not a huge suite.
2. Test the workflow behavior, not prose style.
3. Separate unit-like workflow evals from end-to-end evals.
4. Save outputs as artifacts for inspection.
5. Expand only after the first evals are stable and useful.

### Done when

- workflow regressions can be detected in CI instead of after bad agent runs

## Phase 10 — Add executable markdown pipelines and orchestration

### Why this matters

Once the runtime is stable, Harmonic Coding should be able to execute a checklist or pipeline document step by step, and later coordinate multiple agents safely.

### What to create

- a markdown pipeline runner
- optional parallel or orchestration workflows

### Steps

1. Start with sequential execution only.
2. Treat pipeline step text as untrusted input.
3. Stop on blockers instead of skipping steps silently.
4. Add parallel execution only when step independence is explicit.
5. Add safe delegation rules for shared-branch or shared-file work.

### Done when

- a workflow document can be executed as an operation instead of manually reinterpreted each time

## Phase 11 — Add starter CI and release templates

### Why this matters

Harmonic Coding already has better guidance than AIDD for choosing a lean CI/CD baseline. The missing piece is a small set of reusable templates that make the guidance faster to apply.

### What to create

- PR test workflow template
- protected-branch workflow template
- release workflow template
- optional workflow-eval template

### Steps

1. Use the existing setup workflow as the design source of truth.
2. Keep the templates minimal and stack-aware.
3. Avoid generating workflows for tools the repo does not actually use.
4. Document when each template should and should not be applied.

### Done when

- repo setup is both well-reasoned and faster to apply in practice

## Phase 12 — Pilot, review, and harden

### Why this comes last

Do not scale the system until it has been exercised on real work. The goal is not to copy AIDD mechanically. The goal is to absorb what is useful and keep Harmonic Coding cleaner where it already has stronger ideas.

### Steps

1. Pilot the new runtime on one real repository setup flow.
2. Pilot it again on one real ticket implementation plus PR loop.
3. Capture friction, missing context, and repetition.
4. Tighten the instructions, commands, and review workflows.
5. Only then expand the eval suite and orchestration layer further.

### Done when

- the system works on real delivery work without excessive manual steering

## Phase 13 — Document the final operating model in the repo guides

### Why this is last

This work should happen **after** the runtime, review, validation, and orchestration gaps are closed. The final user-facing guide should describe the real finished operating system, not a halfway state that will immediately become outdated.

### What this phase should produce

- a strict end-to-end new-project onboarding guide
- updated README entry points
- updated setup, delivery, developer, and ultimate guides where needed
- clear instructions for how to use Harmonic Coding on a new repository from zero

### What to document

1. which files must exist before implementation starts
2. which instruction files are always loaded
3. which workflows are planning workflows versus execution workflows
4. the exact order to follow for new projects
5. how setup, CI/CD, testing, review, and PR repair fit into the flow
6. which parts are framework defaults versus project-local overrides
7. how to know a repo is ready for normal ticket implementation

### Steps

1. Re-read the final runtime structure after the earlier phases are complete.
2. Update the strict onboarding guide so it reflects the finished system instead of the transitional state.
3. Update the main repo entry points so a new user can find the right guide immediately.
4. Remove or rewrite any instructions that only applied before the runtime layer was complete.
5. Verify that the final documentation teaches the real sequence without forcing the reader to reconstruct it from multiple guides.

### Current note

`docs/guide/new-project-guide.md` already exists as the **current-state onboarding guide**. After the earlier AIDD-gap phases are finished, it should be revised as part of this final phase so it describes the completed Harmonic Coding runtime and not just the present transitional workflow.

## Recommended implementation order summary

1. instruction stack
2. override layer
3. executable commands or skills
4. strict TDD mode
5. dedicated review workflows
6. hotspot analysis
7. security rules
8. user-testing workflows
9. prompt and workflow evals
10. pipeline runner and orchestration
11. starter CI and release templates
12. pilot and harden
13. final repo and guide documentation for new-project usage

## What not to do

- Do not replace the current planning stack with AIDD's simpler discovery model.
- Do not build multi-agent orchestration before the instruction stack is stable.
- Do not add eval CI before the workflows are executable enough to test meaningfully.
- Do not create broad overlapping tools when one clear workflow is enough.
- Do not turn every idea into a mandatory gate; keep the system lean and high-signal.

## Success criteria

This plan is successful when Harmonic Coding keeps its current planning advantage and adds the missing runtime layer so that:

1. agents load the right instructions automatically
2. workflows are executable and discoverable
3. implementation is test-led and review-led
4. PR loops are operational, not aspirational
5. prompt and workflow regressions are testable
6. the system is reusable across repositories without rewriting the framework
