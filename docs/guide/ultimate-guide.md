# The Ultimate Guide to Human-Directed AI Engineering

> This is the operations manual for advanced AI-assisted development. Not a tutorial — a reference system for practitioners who want the maximum yield from every AI interaction. Applies whether you are starting from zero or retrofitting an existing codebase.

---

## Core Principle

**You are the engineer. The AI is the force multiplier.**

The patterns in this guide exist to solve one problem: LLMs produce garbage when context is garbage. Everything here — specs, vision documents, AGENTS.md files, TDD rules, churn analysis — is context engineering. Structure the input precisely, and the output becomes predictable, reviewable, and reusable.

Speed is not the goal. **Sustainable, compounding leverage is the goal.** A bad spec completed in one hour creates three days of debugging. A good spec completed in two hours ships production code that runs unchanged for years.

---

## Part I: Starting a New Project

### Phase 0: Repository Infrastructure (Before Writing a Single Line of Code)

This takes 30 minutes. It saves hundreds of hours.

#### 1. Create the AGENTS.md stack

Every agent reads this file before every session. Make it authoritative.

```markdown
# AGENTS.md

## Project Context
[1-2 sentence description of what this project does and why it exists]

## Architecture
- Stack: [your stack]
- Database: [your database]
- Auth: [your auth pattern]
- Deployment target: [where it runs]

## Coding Standards
- Language: [versions, settings]
- Formatter: [eslint/prettier/etc config location]
- Test runner: [jest/vitest/etc with config location]

## File Structure
[key directories and what they contain — 5-10 entries max]

## Non-Obvious Rules
- [constraint that prevents a class of bugs]
- [performance rule that isn't in the standard linter]
- [security requirement that must never be bypassed]

## Workflow
- Never implement before a failing test exists
- All public interfaces must have JSDoc
- Migrations are append-only
```

**Locations**: Write this as both `AGENTS.md` (cross-tool agent spec, read by OpenCode and most agents) and `.github/copilot-instructions.md` (GitHub Copilot) — same content, different file names. Both serve the same function.

#### 2. Create the vision.md (AIDD)

```markdown
## Purpose
[Why this project exists. One paragraph. What problem does it solve? Who has the problem?]

## Users
[2-3 user personas with their most important need. Not demographics — behaviors and goals.]

## Technical Constraints
[Hard constraints only: hosting, budget, existing integrations, security requirements]

## Success Metrics
[How you will know the project worked. Observable, not aspirational.]

## Out of Scope
[What this project deliberately does not do. Prevents scope creep from the first session.]
```

Vision.md is stable. It does not change when you add features. It changes when the project's fundamental purpose changes — which is rare.

#### 3. Path-Scoped Rules

For each major subsystem:

```
.github/instructions/api.instructions.md      → /api/** routes
.github/instructions/auth.instructions.md     → /lib/auth/**
.github/instructions/migrations.instructions.md → /migrations/**
```

**Pattern for auth specifically**:
```markdown
# Authentication Rules (applies to /lib/auth/**)

- Never log tokens, passwords, or any auth material — log correlation IDs only
- Session tokens are opaque — no information should be extractable from the token itself  
- Password hashing: bcrypt minimum 12 rounds
- Token refresh: always issue new refresh token on refresh (rotation)
- Never store plaintext passwords even in tests
```

#### 4. Install AIDD

```bash
npx aidd  # Creates ai/ directory
```

This copies 30+ skills into your project. The skills are yours — commit them, customize them.

#### 5. Project-level AIDD customization

Create `aidd-custom/AGENTS.md` to override framework defaults with project-specific rules:

```markdown
# Project Agent Rules (overrides ai/AGENTS.md)

## Vision
See vision.md — read before every task.

## Stack-Specific Rules
[any overrides to AIDD's default assumptions]

## Custom Skills
[list any skills added to aidd-custom/skills/]
```

#### 6. Baseline quality gate

In CI (GitHub Actions or equivalent):
```yaml
- name: Churn analysis
  run: npx aidd churn --json > churn-report.json
  # Save as artifact — track over time
  
- name: Test coverage
  run: npx jest --coverage
  # Minimum 80% line coverage for changed files
```

---

### Phase 1: Discovery (AIDD)

Before writing a line of code or spec for any feature:

```
/discover [feature or project area]
```

This generates:
- User personas with needs
- User journeys (as-is and to-be)
- Pain points with severity × frequency scoring
- Story map grouped by value

Read the output. Adjust. This is your requirements source of truth for the next phase.

**When to go deeper**: If the feature touches 3+ user personas or crosses system boundaries, expand the discovery output into a user interview guide and run it with real users before writing specs.

---

### Phase 2: Epic Creation (AIDD)

For each story in the story map:

```
/task [feature description from story map]
```

AIDD generates an epic file. Review and edit it:

**Epic must include**:
```markdown
## Overview
[Single paragraph starting with WHY. Not what, not how — WHY.]

## In Scope
[Exact list of what this epic covers]

## Out of Scope  
[Exact list of what it does not cover]

## Requirements
Given [context], should [behavior]
Given [error condition], should [specific error handling]
Given [edge case], should [expected result]

## Anti-Patterns (grows over time)
AP-001: [pattern that caused a bug here]
```

**When to escalate to a full SDD spec**: If the feature requires external API integration, involves a compliance requirement, or will be reused/derived multiple times — write a full SDD spec sheet instead of (or alongside) the epic. See Phase 2a below.

---

### Phase 2a: SDD Spec Sheet (For Complex Features)

For integrations, compliance-sensitive features, or factory-pattern reuse:

```markdown
# [Feature] — Spec Sheet v1.0

## Functional Requirements
FR-001: The system MUST [exact behavior] when [exact condition]
FR-002: The API MUST return [status code] with [exact payload shape] when [condition]
FR-003: The system SHALL NOT [prohibited behavior] under any circumstances

## Non-Functional Requirements
NFR-001: Response time MUST be under 200ms at P95 under 10,000 req/s
NFR-002: The auth module cyclomatic complexity MUST stay below 10

## Integration Contracts
### [External API Name]
- Base URL: [exact URL]
- Authentication: [method, where credentials come from]
- Endpoints used:
  - GET /endpoint → [what it returns, when to call it]
  - POST /endpoint → [request shape, response shape, error codes]
- Timeout: [ms]
- Retry policy: [max retries, backoff]

## Test Cases
TC-001: [Condition] → [exact expected result]
TC-002: [Error condition] → [exact error response]

## Verification
[Exact commands to verify the implementation is correct]
curl -X POST [endpoint] -H "..." -d '...' | jq [expected output shape]

## Anti-Patterns
AP-001: [Known bad approach and why it fails]

## Out of Scope
[Explicit list]
```

The spec sheet is the implementation asset. When a bug is found:
1. Add `AP-XXX` to the spec sheet
2. Write a failing test that captures the bug  
3. Fix the code
4. The fix is never "just fix the code" — the spec and test both update

---

### Phase 3: Implementation (AIDD + TDD)

```
/execute
```

AIDD drives implementation with these non-negotiable rules:

**The TDD contract**:
1. Write a failing test. Run it. Watch it fail.
2. Write the minimum code to make it pass. Nothing else.
3. Refactor with the test green. Never with it red.
4. Commit: failing test → green test → refactor (separate commits or one, but never merge them conceptually).

**Test quality checklist** (every test must answer these):
- [ ] What is the input given?
- [ ] What behavior is being tested?
- [ ] What is the actual output?
- [ ] What is the expected output?
- [ ] If this test fails, where is the bug?

**The mocking question**: Before mocking a dependency, run `aidd churn` on both the mock candidate and the real implementation. If the real implementation scores low (stable, simple, small), use the real thing. Mock only when integration is expensive (network, database) AND the candidate is stable.

---

### Phase 4: Review and Quality Gate

After implementation:

```
/review
npx aidd churn --days 7
```

Review catches: spec compliance, test coverage, error handling, edge cases, naming.

Churn shows: which files in this sprint became hotspots. If any file's score crossed a threshold (`Cx > 9`, `LoC > 400`, or composite score > 10,000), the epic is not done — refactor before marking complete.

```
/aidd-pr [PR URL]
```

For PR automation: triage, risk assessment, change summary, delegation plan for inline fixes.

---

### Phase 5: Validation

```
/user-test
```

Generates a user testing script from the epic's user journeys. Two versions:
- Human tester script (for stakeholders)
- AI agent test script (automated)

Run both before merge. This is the final gate between "tests pass" and "feature ships".

---

### Phase 6: Commit and Log

```
/log
/commit
```

`/log` updates the project change log in `ai/docs/log/`. Each entry links to the epic.
`/commit` generates a conventional commit message from the diff.

---

## Part II: Applying to an Existing Project

### Step 1: Hotspot Audit

Before touching anything:

```bash
cd [project root]
npx aidd churn --json --days 90 --top 20 | tee churn-baseline.json
```

Read the output. The top files by composite score are your highest-risk areas. Anything with:
- `Cx > 9` (cyclomatic complexity): cognitive bottleneck, bugs live here
- `LoC > 400`: too large, find the seams
- Composite score > 10,000: touched constantly AND complex AND large — a systemic problem

**Critical rule**: Do not add AI assistance to high-churn files without first reducing their complexity. AI amplifies existing patterns — if the file is tangled, AI makes it more tangled, faster.

**Sprint 0 for any existing project**:
```
1. Run churn analysis
2. Pick top 3 files
3. Write SDD spec sheets for them (what they DO, not what you want them to do)
4. Extract complexity with TDD: write tests for existing behavior, then refactor
5. Re-run churn — score must drop before moving to new features
```

### Step 2: Install AIDD

```bash
npx aidd
```

```markdown
# [Project Name] Agent Rules

## Context
This is an existing [age]-year-old codebase. Legacy patterns exist. Do not refactor unless explicitly tasked.

## Priority Rules
1. Tests first — this project has [X]% test coverage. Do not reduce it.
2. Migrations are append-only — existing tables are never modified, only extended
3. [specific legacy constraint]

## Known Debt
- [file] is not tested — do not call its functions without mocking at the call site
- [module] uses [old pattern] — do not extend it, queue for spec-driven rewrite
```

### Step 3: Create vision.md Retroactively

This is harder than greenfield but essential:

```markdown
## Purpose
[What this project actually does today — not what you wish it did]

## Users
[Who actually uses it — observed behavior, not aspirations]

## Technical Constraints
[Current real constraints: hosting lock-in, DB choices, auth system, etc.]

## Technical Debt
[Top 3 architectural decisions that constrain new development]

## Success Metrics
[Current KPIs — latency, availability, conversion, revenue. Real numbers.]
```

Use RTC to help write this:
```
/aidd-rtc --compact
Given this codebase [paste key files], what is its actual purpose and who are its users?
```

### Step 4: Retrofit Context Engineering

For each major subsystem, create path-scoped instruction files:

```
.github/instructions/[module].instructions.md
```

Use the churn report to prioritize which modules to spec first — highest churn first.

### Step 5: Apply AIDD Workflow to New Features Only

**Do not rewrite the whole codebase.** That's a trap.

For new features: full AIDD workflow from `/discover` to `/commit`.
For bug fixes: `/aidd-fix` only.
For refactors: only when churn score justifies it AND there's a spec sheet.

The existing code becomes SDD-compliant over time, one spec sheet at a time.

---

## Part III: Operating at Scale

### Parallel Execution

For large features with independent modules:

```
/aidd-parallel [feature description]
```

This generates a parallel execution plan: which sub-tasks can run concurrently (no shared state, independent interfaces), which must be sequential (dependency order), and the integration points.

**Manual parallel pattern** (for multi-model or multi-agent setups):
1. Epic → decompose into N independent tasks
2. Assign each task to a separate agent session (separate context windows)
3. Integration task runs last, pulls from shared branch

### Automation Patterns

**Copilot cloud agent** for unattended work:
```bash
gh copilot agent run --task "Document all public APIs in /api/v2/**"
# Runs unattended, commits results to branch
```

**Bulk operations** (via Copilot CLI):
```bash
# Apply spec sheet to N microservices
for service in services/*; do
  gh copilot suggest "Apply auth-spec.md to $(basename $service)" --cwd $service
done
```

**Scheduled operations** (via GitHub Actions):
```yaml
on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday 9am
jobs:
  churn-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx aidd churn --json > churn-$(date +%Y%m%d).json
      - uses: actions/upload-artifact@v4
        with:
          name: churn-report
          path: churn-*.json
```

### Custom Skills

Build skills for patterns you use repeatedly. A skill is permanent leverage — written once, available to every agent on every project.

```bash
/aidd-upskill create [skill-name]
```

High-value custom skills to build:
- `spec-review` — validates a spec sheet against the spec sheet format, flags missing sections
- `migration-gen` — generates append-only DB migrations from a spec sheet's data model
- `api-contract` — extracts integration contracts from OpenAPI specs into spec sheet format
- `pr-risk` — scores PRs by change surface × hotspot overlap

### Model Selection by Task

| Task | Model | Reasoning |
|------|-------|-----------|
| Spec writing (complex) | Claude Opus 4.8 or Sonnet 4.6 | Multi-step reasoning required |
| Implementation (standard) | Sonnet 4.6 | Best cost/quality for coding |
| Bulk documentation | Haiku 4.5 | Simple output, high volume |
| PR review | Sonnet 4.6 | Context window + coding quality |
| Discovery / ideation | Opus 4.8 | Breadth of reasoning |
| Churn-guided refactor | Sonnet 4.6 | Structural code changes |

**Token economics** (current rates):
- Opus 4.8: $5/$25 per MTok (in/out)
- Sonnet 4.6: ~$3/$15 per MTok  
- Haiku 4.5: ~$0.25/$1.25 per MTok
- Copilot Enterprise flat: $39/user/month

For volume work (documentation, bulk operations): Haiku.
For complex single-session work (spec writing, architecture): Opus 4.8.
For daily development: Sonnet 4.6 — best ROI.
With prompt caching: Sonnet 4.6 effective cost drops 40-60% for repeated context.

---

## Part III-B: Tool Integration — Eliminating Manual Slash Commands

By default, AIDD requires typing `/aidd-fix`, `/task`, `/discover`, etc. This section shows how to configure OpenCode and Copilot so the agent selects the right AIDD workflow based on what you say in plain language.

**Note**: AIDD commands are markdown instruction files — prompts the LLM follows, not shell executables. Only `npx aidd churn` is a real CLI command. The integration strategy is: teach the agent to load the right `SKILL.md` automatically.

### OpenCode — Zero Code (Native Skill Discovery)

OpenCode has a built-in `skill` tool that auto-discovers and loads `SKILL.md` files. Setup is two commands:

```bash
npx aidd                               # installs ai/ directory
mkdir -p .opencode && ln -s ../ai/skills .opencode/skills
```

All 35 AIDD skills are now auto-invokable. OpenCode reads skill descriptions from `ai/skills/index.md` and selects the right skill when your message matches. Say "fix this bug" → it loads `aidd-fix` workflow automatically.

### GitHub Copilot — Instructions-Based Routing

Copilot has no tool auto-selection layer. Best available: explicit routing instructions in `.github/copilot-instructions.md`:

```markdown
## AIDD Workflow Routing
When fixing bugs: load and follow `ai/skills/aidd-fix/SKILL.md`
When building features: load `ai/skills/aidd-please/SKILL.md` and run /task
When reviewing code: load `ai/skills/review/SKILL.md`
When analyzing risk: run `npx aidd churn --days 90`
When deep reasoning needed: load `ai/skills/aidd-rtc/SKILL.md`
```

Copilot follows these when intent is clear. For unattended/bulk work, `gh copilot agent run` can be given an explicit skill path — see `docs/research/07-tool-integration.md`.

### Summary

| | OpenCode | GitHub Copilot |
|--|----------|----------------|
| **Auto-selects AIDD skills** | ✅ Native `skill` tool | ⚠️ Instructions-based |
| **Setup** | 2 commands | Add routing block to copilot-instructions.md |
| **Unattended/bulk ops** | No | ✅ `gh copilot agent run` |
| **Best for** | Interactive daily dev | Bulk/scheduled tasks |

---



### The Spec Anti-Pattern Checklist

Before handing a spec to an agent, verify:

- [ ] Every requirement uses RFC-2119 language: MUST, SHALL, SHOULD, MAY (not "should try to" or "ideally")
- [ ] Every external API has a full integration contract (not just "call the Stripe API")
- [ ] Every error condition has a specified response (not "handle errors appropriately")
- [ ] Verification clause: a runnable command that proves it works
- [ ] Anti-patterns section: at least empty (populated on first bug)
- [ ] Out of scope: explicit, not implicit
- [ ] Test cases: at minimum one per functional requirement, one per error path

### The AGENTS.md Anti-Pattern Checklist

- [ ] Not a list of general software engineering principles (agents know those)
- [ ] Contains non-obvious project-specific rules only
- [ ] References concrete file paths (not "put tests in the test directory")
- [ ] Has security rules for this specific domain
- [ ] Less than 300 lines (longer = not read properly)

### The Epic Anti-Pattern Checklist

- [ ] Overview starts with WHY, not WHAT
- [ ] Requirements use "Given X, should Y" — no other format
- [ ] No numbered tasks (that's the agent's job)
- [ ] In Scope and Out of Scope are explicit
- [ ] Anti-patterns section exists

### TDD Checklist (per implementation session)

- [ ] First action was to write a failing test (not to open the source file)
- [ ] Test was run and observed to fail before writing implementation
- [ ] No implementation exists without a corresponding test
- [ ] No test mocks an in-process dependency without churn justification
- [ ] All tests are independent (no shared state, no execution order dependency)
- [ ] Each test answers: given, should, actual, expected, how-to-debug

---

## Quick Reference: Command Map

| Goal | Command | Source |
|------|---------|--------|
| New feature discovery | `/discover [feature]` | AIDD |
| Create feature epic | `/task [description]` | AIDD |
| Implement with TDD | `/execute` | AIDD |
| Code review | `/review` | AIDD |
| Find hotspots | `npx aidd churn --days 30` | AIDD |
| Fix a bug | `/aidd-fix [description]` | AIDD |
| Review a PR | `/aidd-pr [url]` | AIDD |
| Parallel tasks | `/aidd-parallel [feature]` | AIDD |
| Generate user tests | `/user-test` | AIDD |
| Commit with conventional message | `/commit` | AIDD |
| Think through a problem | `/aidd-rtc --compact --depth 5` | AIDD |
| Create custom skill | `/aidd-upskill create [name]` | AIDD |
| Bulk operations | Copilot CLI / cloud agent | SDD Automation |
| Large spec engineering | SDD spec sheet format | SDD |
| Token cost analysis | See 04-token-economics.md | SDD |
| Context window management | See 02-context-engineering.md | SDD |

---

## The Three Commitments

If this guide reduces to three principles:

**1. Specs are the asset.** Code is generated. Specs are curated. Every bug, every edge case, every architectural decision goes into a spec file. When you rewrite the code, you keep the spec. The spec is the company's IP, not the code.

**2. Context before execution.** No agent session starts without a context review. AGENTS.md current? Vision.md accurate? Spec complete? Path-scoped instructions loaded? Thirty seconds of context check prevents thirty minutes of hallucinated output.

**3. Churn-first prioritization.** Before adding any AI acceleration to any file, run `aidd churn`. Complexity compounds faster with AI speed than without it. Apply AI to clean, tested, simple files. Refactor complex files first. Always.
