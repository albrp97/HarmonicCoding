# Advanced Playbook: Human-Directed AI Engineering

> This is not a tutorial. It is an operations manual for engineering teams who want to treat AI tools as serious infrastructure rather than productivity gimmicks. Everything here is sourced from production use, official guidance, and workshop evidence. No beginner concepts.

---

## The Mental Model

### What you are operating

You are a **context architect**. The model generates code. You design and maintain the system that determines what the model knows, when it knows it, and what it is allowed to do.

LLM failures in production code generation are almost never model failures. They are context failures.

> *"Agent failures aren't only model failures; they are context failures."* — Philipp Schmid, Google DeepMind

Your leverage is in specification quality, context structure, and verification design — not in prompting cleverness.

### The shift from coding to specifying

| Yesterday | Today |
|-----------|-------|
| Write code | Write specs |
| Review others' code | Review agent output against spec |
| Debug | Diagnose context failures |
| Document (low priority) | Spec (highest priority — it drives everything) |
| Maintain codebase | Maintain spec + instructions files |

The spec is the asset. Code is a build artifact.

---

## Phase 1: Repository Infrastructure (One-Time Setup)

### Files to create before any AI work begins

```
.github/
  copilot-instructions.md     # persistent context for every Copilot session
  COPILOT_INSTRUCTIONS.md     # cloud agent contract (duplicate intent, agent-specific)
  instructions/
    *.instructions.md          # path-scoped rules
  agents/
    *.md                       # custom agent personas
  prompts/
    *.prompt.md                # reusable prompt templates
  skills/                      # custom skill implementations
  workflows/
    copilot-setup-steps.yml    # cloud agent environment baseline

CLAUDE.md                      # Claude Code / Claude-family sessions
AGENTS.md                      # cross-tool, any agent that follows the standard
docs/
  specs/
    shared/                    # reusable spec components
      coding-standards.md
      security-nonfunctionals.md
      api-design-contract.md
    projects/                  # per-project specs
```

### `.github/copilot-instructions.md` — the right structure

GitHub's official guidance says this file must be no longer than **2 pages** and must not contain task-specific instructions. The format they recommend (verbatim from their auto-generation prompt):

```markdown
# [Project Name]

## What This Repo Does
[One sentence. Tech stack, scale, what it produces.]

## Tech Stack
- Language: Python 3.11 (use f-strings, walrus operator, pattern matching)
- Framework: FastAPI 0.110
- DB: PostgreSQL 15 + SQLAlchemy 2.0 async
- Tests: pytest + pytest-asyncio + httpx AsyncClient
- Linting: ruff + mypy (strict)

## Build / Test / Run
```bash
# Always run after checkout:
pip install -e ".[dev]"

# Run tests (takes ~45 seconds):
pytest tests/ -v --tb=short

# Lint (must pass before commit):
ruff check src/ && mypy src/ --ignore-missing-imports
```

## Project Layout
src/
  api/          # FastAPI routers (no business logic here)
  services/     # business logic (no DB calls here)
  repositories/ # DB access only
  schemas/      # Pydantic request/response
  models/       # SQLAlchemy models
tests/
  unit/         # no DB
  integration/  # uses test DB
docs/
  specs/        # READ THESE before implementing anything

## When Adding a New Endpoint
Read docs/specs/api-design-contract.md first. Always in this order:
1. Schema → 2. Model → 3. Repository → 4. Service → 5. Router → 6. Tests

## Engineering Rules
- Type hints on all functions. No exceptions.
- Log with structlog. Never print().
- All datetimes UTC. Use datetime.now(UTC).
- SQL queries in repositories/ only. Never in services/ or api/.
- No bare except. Catch specific exceptions only.
```

**What to exclude**: Detailed API docs (link instead), file-by-file walkthroughs, obvious practices like "write clean code", anything that changes frequently.

### Path-scoped instructions (`.github/instructions/`)

Use these to avoid bloating the global instructions file:

```markdown
# .github/instructions/models.instructions.md
---
applyTo: "src/models/**/*.py"
---

All SQLAlchemy models must:
- Include `created_at` and `updated_at` timestamps (with auto-update trigger)
- Use UUID primary keys (not integer autoincrement)
- Never include business logic methods
- Soft-delete via `deleted_at` nullable field (never hard-delete)
```

```markdown
# .github/instructions/api.instructions.md
---
applyTo: "src/api/**/*.py"
---

API handlers:
- Validate all inputs with Pydantic before any processing
- Return standardized envelope: {"data": ..., "error": null, "status": 200}
- Never call repositories directly — always through services
- Authentication: check request.state.user before any resource access
```

### The `copilot-setup-steps.yml` (for cloud agent)

```yaml
name: "Copilot Setup Steps"
on:
  workflow_dispatch:
  push:
    paths: [.github/workflows/copilot-setup-steps.yml]

jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -e ".[dev]"
      - run: pytest tests/ --tb=short || true   # baseline: agent sees pre-existing failures
      - run: ruff check src/ || true
      - run: mypy src/ --ignore-missing-imports || true
```

The `|| true` is intentional and important: the agent reads this baseline output and knows which failures existed *before* it started.

---

## Phase 2: Spec Writing (Where Engineering Work Lives)

### The "Let Claude Interview You" Pattern

For any non-trivial system, don't write the spec yourself. Let the model interview you:

```
I want to build [brief 2-sentence description].

Interview me in detail using targeted questions. Ask about:
- Technical implementation choices and constraints
- Edge cases and failure modes I might not have considered
- Integration points and external dependencies
- Non-functional requirements (security, performance, resilience)
- What's out of scope

Ask one question at a time. Don't ask obvious questions. Dig into the hard parts.
Keep interviewing until you have enough to write a complete spec.
Then write the spec to SPEC.md.
```

After the spec is written: **start a fresh session to implement it**. The interview session's context is often messy — a clean session reads the spec as a primary document.

### Spec Structure for Production Work

A production-grade spec must include these sections. Missing any one produces consistent failure in that area:

```markdown
# Spec: [System Name]

## Problem Statement
What exists, what's missing, what pain it causes.

## Scope
### In Scope
- [Numbered list of what this spec covers]

### Out of Scope
- [Explicit list of what is excluded]

## Functional Requirements
FR-001: [VERB + NOUN]. Example: "The API MUST validate client_id is non-null before any query."
FR-002: ...
[Use RFC-2119: MUST / SHOULD / MAY / MUST NOT]

## Technical Architecture
- Tech stack and versions (exact)
- Directory structure (explicit — don't let the model choose)
- Data models (entity definitions, field types, constraints)

## Integration Contracts
For each external API: base URL, auth method, endpoints, request/response schemas.
If you don't specify this, the model invents the API shape. That's wrong.

## Test Requirements
- Framework, location, naming convention
TC-001: POST /endpoint with valid data returns 201
TC-002: POST /endpoint with missing field returns 400 with {"error": "field_required"}
TC-003: External API timeout returns 503 with retry-after header
[Enumerate the specific scenarios. "Write tests" without this produces happy-path only.]

## Non-Functional Requirements
- Performance: p99 < 200ms under 100 concurrent requests
- Security: Input validation per OWASP. No credentials in logs. Auth on all endpoints.
- Resilience: Circuit breaker on external APIs. Retry with exponential backoff.

## Coding Standards
Include inline or reference: docs/specs/shared/coding-standards.md

## Known Anti-Patterns (append as bugs are found)
[Initially empty — grows over time]
```

### Building the Spec via 50 Prompts

Charles' team wrote ~50 prompts to refine their spec. Each prompt adds a concern:

```
# Round 1-10: Bootstrap
"Draft an initial specification for [system]. Problem statement: [...] Core requirements: [...]"

# Round 11-35: Expansion (one prompt per concern)
"Add to the spec: automatic test case generation. Tests in /tests. pytest framework.
These scenarios MUST have dedicated test cases: [list]"

"Add to the spec: error handling. Every external API call catches timeout/4xx/5xx.
Errors logged with correlation IDs. User errors never expose stack traces."

"Add to the spec: security requirements. OWASP Top 10 explicitly addressed.
Rate limiting: 100 req/min per API key. JWT validation on all endpoints."

# Round 36-45: Stress testing
"Review the spec. Identify: ambiguous requirements, missing edge cases, integration gaps.
List them, then add the missing requirements."

# Round 46-50: Hardening
"Rewrite the spec for maximum consistency. Use RFC-2119 (MUST/SHOULD/MAY) throughout.
Every MUST requirement must have a corresponding test requirement."
```

### The Verification Criteria Principle

Every spec meant for autonomous implementation MUST include an end-state verification clause — something the agent can run without human input:

```markdown
## Verification
The implementation is complete when:
1. `pytest tests/ -v` passes with 0 failures
2. `ruff check src/` returns no errors
3. `mypy src/` returns no type errors
4. The following curl commands return the specified status codes:
   - `curl -X POST /api/clients -d '{"id": "123"}'` → 201
   - `curl -X POST /api/clients -d '{}'` → 400
   - `curl -X GET /api/clients/999` → 404
```

Without this, you need to watch the agent's session. With it, you walk away.

---

## Phase 3: Implementation

### The Execution Loop

Implementation is a loop, not a single command:

```
Session 1:
"Read the spec at docs/specs/client-check/spec.md.
Build a step-by-step implementation plan.
Implement steps 1 through 6. Run tests after each step."

[Agent implements, may stop early or report "incomplete"]

Session 2 (or continuation):
"Continue. You stopped at step 6. Complete steps 7-12 per the spec.
Reference the spec for any decisions."

[Repeat until verification clause passes]
```

The Belgium client check API required ~10 such cycles. Each cycle is bounded and verifiable.

### Context Loading Before Each Session

```markdown
# Session Primer (fill this before each implementation session)

**Spec**: docs/specs/client-check/spec.md (READ FIRST)
**Model**: Claude Opus 4.8 (use this explicitly — don't trust "auto" for spec work)

**Current Status**:
- ✅ Data models (src/models/)
- ✅ Repositories (src/repositories/)
- 🔄 Services — partial (client_service.py done, blacklist_service.py missing)
- ❌ API layer
- ❌ Tests

**This Session**: Implement blacklist_service.py per spec sections 4.2-4.3

**Decisions Already Made** (don't reconsider these):
- Blacklist lookup is sync (external API doesn't support async)
- Timeout error: raise BlacklistUnavailableError, not return None
- Test framework: pytest with mock.patch for external calls
```

### Model Selection for Implementation

| Phase | Model | Why |
|-------|-------|-----|
| Spec iteration | Claude Opus 4.8 | Reasoning-heavy; catches ambiguity |
| Large-system implementation | Claude Sonnet 4.6 | Cost-efficient; 1M context |
| Complex multi-file debugging | Claude Opus 4.8 | Multi-hop causal reasoning |
| Test generation | Claude Haiku 4.5 | Mechanical; Haiku is sufficient |
| Boilerplate / CRUD | Claude Haiku 4.5 | Pattern-matching task |
| Security review | Claude Sonnet 4.6 | Reasoning about edge cases |

Never use "auto" for spec-iteration or security-sensitive sessions. Specify the model explicitly.

### Plan Mode First (VS Code / CLI)

Before any implementation session in VS Code or Copilot CLI: invoke plan mode.

**VS Code**: Use the plan mode toggle in agent mode before hitting enter.

**Copilot CLI**: `Shift+Tab` in the interactive REPL to enter plan mode — the model asks clarifying questions and shows you the plan before touching any code.

**Claude Code**: Add `(plan first, do not implement yet)` to the end of any prompt:

```
"I want to add FRIS integration to the client check service.
Read the Dutch spec at docs/specs/nl-client-check/spec.md.
(Plan first, do not implement yet)"
```

Review the plan before proceeding. Change it via follow-up. Only then: "Execute the plan."

### The Anti-Overreach Rule

From Anthropic's Fable 5 guidance — add this to your CLAUDE.md/AGENTS.md:

```markdown
## Scope Discipline
- Don't add features, refactors, or abstractions beyond what the task explicitly requires
- A bug fix doesn't need surrounding cleanup
- Don't design for hypothetical future requirements
- Don't use feature flags when you can just change the code
- Before ending, review your last paragraph: if it's a plan or promise about work not done, do that work now
```

This prevents scope creep where the model "improves" things you didn't ask it to touch, breaking tests or changing behavior you depended on.

---

## Phase 4: Quality Gates

### The Spec Compliance Gate

Before any human review: validate generated code against the spec programmatically.

```bash
# Add to CI pipeline (runs before human PR review)
copilot \
  -p "Read docs/specs/client-check/spec.md.
      Read the implementation in src/.
      For each MUST requirement in the spec, verify it is implemented.
      Output: ✅ MUST-001 [description] | ❌ MUST-007 [missing: reason]
      Exit 1 if any MUST requirement is not implemented." \
  --allow-tool='shell(git:*)' \
  --no-ask-user -s
```

This gate catches the 20% of spec non-compliance that isn't caught by tests (usually non-functional requirements like error message format, logging, and security constraints).

### Tiered Review Strategy

| Change type | Review |
|-------------|--------|
| AI-generated boilerplate | Tests pass + spec gate = done |
| AI-generated business logic | Tests pass + spec gate + human reviews spec compliance |
| Security-sensitive | Tests pass + spec gate + human review + Copilot security scan |
| Architecture changes | Full human review regardless of tests |

The principle: if it's specified, tests can validate it. If it requires judgment, humans must validate it. Write specs precisely enough to eliminate judgment from the loop.

### Test Cases in the Spec

The highest-ROI addition to any spec. When test scenarios are explicitly listed in the spec:

1. The agent generates exactly those tests (not whatever it decides to test)
2. You validate the tests exist and pass — without reading implementation code
3. The spec compliance gate can cross-reference test existence vs. spec requirements

```markdown
## Test Requirements

### Mandatory Test Cases (MUST implement all)
TC-001: Valid screening request returns 200 with status field
TC-002: Unknown client_id returns 404
TC-003: Client on Moody's list returns 200 with status=BLOCKED, source=moody
TC-004: Client on ERSR list returns 200 with status=BLOCKED, source=ersr
TC-005: Client on no list returns 200 with status=CLEAR
TC-006: Moody's API timeout returns 503, circuit_breaker_open=true
TC-007: Invalid request body returns 400 with field-level error detail
```

---

## Phase 5: Spec Maintenance

### The Bug-Back-to-Spec Rule

Every production bug → spec update. No exceptions.

```markdown
## Known Anti-Patterns (add to spec on every bug found)

### AP-001: Null client_id crashes before validation
The implementation MUST validate client_id is non-null and non-empty BEFORE 
any downstream processing. Return {"error": "client_id_required", "status": 400}.

### AP-002: Circuit breaker not opened on timeout
When any blacklist API returns timeout OR connection refused:
1. Increment failure counter for that specific API
2. If failures >= 3 in 60 seconds: open circuit breaker for that API
3. Circuit-open response: {"status": "UNAVAILABLE", "source": "[api_name]"}
```

If you fix code without updating the spec: the next regeneration reproduces the bug.

### Auto-Memory System (Claude Code)

Claude Code maintains a per-repo auto-memory file separate from CLAUDE.md:
- **CLAUDE.md**: human-curated rules (your spec architecture)
- **auto-memory**: Claude's learned experience (build commands it discovered, debugging insights, preferences it learned)
- **CLAUDE.local.md**: personal overrides (gitignored — your local developer preferences)

Auto-memory is loaded first 200 lines / 25KB every session. Review it occasionally — Claude may have learned incorrect things. Correct or delete them.

### When to Re-Run Implementation from Spec

The bold decision to "throw the code away and start over" is rational when:
- Spec is at sufficient quality (it was good when you built it, and it's been maintained)
- Code has high cyclomatic complexity, low test coverage
- A new model with significantly better capabilities is available
- The feature delta between v1 and v2 is large enough that iterative change > fresh generation

> *"Something you would not do if you had to write every line manually."* — Charles, Belgium team

---

## Phase 6: Automation and Scale

### Bulk Operations (Copilot CLI)

```bash
# Document all services
for file in src/services/*.ts; do
  copilot -p "Generate JSDoc for all exported functions in $file. Write in-place." \
    --allow-tool='write' --no-ask-user -s
done

# Generate missing test files
for service in src/services/*.ts; do
  name=$(basename "$service" .ts)
  test_file="tests/unit/${name}.test.ts"
  [ ! -f "$test_file" ] && copilot \
    -p "Generate unit tests for $service → $test_file. Cover all public methods." \
    --allow-tool='write' --no-ask-user -s
done
```

### Scheduled Maintenance

```yaml
# .github/workflows/weekly-audit.yml
on:
  schedule: [{cron: '0 8 * * 1'}]   # Mondays 8am
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - run: npm install -g @github/copilot
      - run: |
          copilot -p "Analyze coverage gaps in tests/. 
            List the top 5 uncovered modules by risk.
            Create a GitHub issue for each with specific missing scenarios." \
            --allow-tool='shell(npm:*), shell(npx:*)' --no-ask-user -s
```

### The Factory Pattern (Multi-Country Reuse)

Belgium's client check spec → Netherlands version in one prompt:

```
This specification covers the Belgian client check service using ERSR.
I need a Dutch version using FRIS instead.

Rules:
- Replace all ERSR references with FRIS
- Update integration contracts to FRIS API schemas (attached below)
- Keep all other requirements identical
- Generate a new spec at docs/specs/nl-client-check/spec.md

FRIS API documentation: [paste Markdown version]
```

This scales: each country is a derived spec from the base. The base spec is the intellectual property. Country variants are one-shot derivations.

---

## Copilot Cloud Agent: Dispatching Autonomous Work

### Via GitHub Issue (simplest)

1. Create an issue: "Implement FRIS integration per docs/specs/nl-client-check/spec.md sections 3.1-3.5"
2. Assign to `@copilot`
3. Agent: runs `copilot-setup-steps.yml` → reads instructions → implements → opens PR
4. You: review the PR against the spec and test results

### Via API (programmatic dispatch)

```bash
TASK=$(gh api --method POST \
  -H "Accept: application/vnd.github+json" \
  /repos/OWNER/REPO/issues \
  --input - <<< '{
    "title": "Implement FRIS integration",
    "body": "Per docs/specs/nl-client-check/spec.md sections 3.1-3.5. Reuse Belgium client_check pattern.",
    "assignees": ["copilot-swe-agent[bot]"],
    "agent_assignment": {
      "target_repo": "OWNER/REPO",
      "base_branch": "main",
      "model": "claude-opus-4.8"
    }
  }')
echo "Task: $TASK"
```

### Running Partner Agents (Claude, Codex)

Assign issues to `@claude` or `@codex` instead of `@copilot`. All three use the same `copilot-setup-steps.yml` and COPILOT_INSTRUCTIONS.md. Enable at: Settings → Copilot → Coding agent → Partner Agents.

---

## Quick Reference: Spec Sizing

| Scope | Artifact | Lines | When |
|-------|----------|-------|------|
| Single task | In-session prompt | ≤50 | Bounded change, you'll review everything |
| Recurring codebase rules | CLAUDE.md / AGENTS.md | 100-200 | Repeated interactions with same repo |
| Greenfield feature | spec.md + prompt_plan.md | ~500 | Multi-phase, single team |
| Shared team workflow | Full AGENTS.md with doc links | 1000-2000 | Multi-contributor |
| Large system | Index AGENTS.md + docs/context/ | 2000-5000+ | Monorepo, multi-team, multi-agent |

**The 200-line CLAUDE.md rule** (Anthropic): longer files reduce rule adherence because instructions compete for attention in the context window. Use path-scoped rules and the import system (`@file.md`) to compose without bloat.

---

## Quick Reference: Decision Trees

### "Should I use a spec or a prompt?"

```
Is this a repeated interaction with the same codebase?
  → YES: Use CLAUDE.md / AGENTS.md (persistent context)
  → NO: Will someone else need to run this?
        → YES: Use spec.md (distributable)
        → NO: Is the task bounded to <2 files?
              → YES: In-session prompt is fine
              → NO: Write a spec
```

### "Which model?"

```
Is this spec writing or architectural decisions?
  → YES: Claude Opus 4.8 (invest the $5/MTok — worth it)

Is this feature code generation from a clear spec?
  → YES: Claude Sonnet 4.6 ($3/MTok, 1M context, production sweet spot)

Is this boilerplate, tests, or docs?
  → YES: Claude Haiku 4.5 ($1/MTok — fast, cheap, sufficient)

Is this a batch job (non-interactive: reviews, analysis, docs)?
  → YES: Any model via Batch API (50% off)
```

### "What context does the agent need?"

```
ALWAYS load:
  - .github/copilot-instructions.md (auto-loaded in VS Code)
  - Relevant spec file (reference it explicitly)

FOR IMPLEMENTATION:
  - Session primer (current status, this session's goal)
  - Similar existing implementation (one example, not the whole codebase)
  - Path-specific instruction files for the target subsystem

FOR DEBUGGING:
  - Minimal reproduction of the failure (exact input + exact output)
  - Relevant code only (not the whole file)
  - Any known constraints on the fix

NEVER load unnecessarily:
  - Auto-generated files
  - Test fixtures
  - Full codebase when only 2 files are relevant
```

---

## The Complete Workflow in One Picture

```
IDEA
  │
  ├─ [Let Claude interview you] → SPEC.md
  │
  ├─ [~50 prompt iterations] → production-grade spec
  │        ↓ verification clause
  │        ↓ test requirements
  │        ↓ coding standards reference
  │        ↓ anti-patterns section
  │
  ├─ [Fresh session: implement] → code + tests
  │        ↑ spec compliance gate (automated)
  │        ↑ test suite (specified)
  │
  ├─ [Bug found] → spec update (AP section) → re-generate
  │
  └─ [New country/variant] → one prompt → new spec → same implementation loop
```

---

## Sources

| Source | What it provides |
|--------|-----------------|
| `code.claude.com/docs/en/best-practices` | Anthropic's complete SDD workflow |
| `code.claude.com/docs/en/memory` | CLAUDE.md hierarchy, auto-memory, sizing rules |
| `developers.openai.com/codex/guides/agents-md` | AGENTS.md discovery chain, override system |
| `docs.github.com/en/copilot/.../add-custom-instructions` | copilot-instructions.md structure, path-scoped instructions |
| `docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli` | Programmatic CLI, bulk operations |
| `platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices` | XML structuring, instruction specificity, verification clauses |
| `platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5` | Long-horizon agent patterns, anti-overreach |
| `philschmid.de/context-engineering` | Context engineering definition and 7-component model |
| `harper.blog/2025/02/16/my-llm-codegen-workflow-atm` | Greenfield SDD: spec.md + prompt_plan.md pipeline |
| `github.com/agentsmd/agents.md` | AGENTS.md open standard |
| DSH Offsite Workshop (internal transcript) | Belgium production case studies; cost data; Symphony analysis |
