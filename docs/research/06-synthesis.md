# Synthesis: AIDD Framework + Spec-Driven Development

> A direct comparison of two complementary methodologies for AI-assisted engineering. AIDD and SDD are not competitors — they operate at different scales and different stages. Understanding where each excels, where they overlap, and how to combine them is the key to the most effective AI engineering workflow.

---

## The Fundamental Difference

| | AIDD Framework | Spec-Driven Development (SDD) |
|-|----------------|-------------------------------|
| **Scale** | Task-level (features, bugs, PRs) | System-level (services, APIs, products) |
| **Primary artifact** | Epic file (100-500 lines of requirements) | Spec sheet (500-5000 lines of full system spec) |
| **Primary discipline** | TDD + workflow rails | Context engineering + spec quality |
| **Primary tool** | Claude Code / Cursor agent | GitHub Copilot agent mode / Claude Code |
| **Stack bias** | JavaScript / Next.js optimized | Stack-agnostic |
| **Origin** | ParallelDrive open source framework | Belgium engineering team (Charles) + Anthropic/GitHub guidance |
| **Installed as** | Files copied into your project (`npx aidd`) | Patterns you adopt and implement |
| **Agent contract** | AGENTS.md + vision.md | `.github/copilot-instructions.md` + CLAUDE.md |

---

## Where They Solve the Same Problem

Both frameworks address the same root cause: **AI agents fail when context fails**.

### The Vision Document ≈ The Spec Sheet (Different Scales)

**AIDD Vision Document** (1-2 pages):
```markdown
## Purpose
TaskFlow helps remote teams ship faster via AI-assisted task breakdown.

## Technical Constraints
- Stack: Next.js 14 + PostgreSQL
- Deployment: Vercel
```

**SDD Spec Sheet** (500-5000 lines):
```markdown
## FR-001: The API MUST return 201 when POST /tasks receives valid data
## FR-002: The API MUST return 400 when task_name is empty
## TC-001: POST /tasks valid → 201 with task_id
## Integration Contract: Moody's API base URL, auth method, endpoints...
```

The vision document tells the agent WHAT the project is and its constraints. The spec sheet tells the agent HOW a specific system should work in complete detail. Both are necessary — at different points in the development lifecycle.

**Together**: Vision document → sprint-level epics (AIDD) → full spec sheet (SDD for complex systems) → implementation.

### The Epic ≈ The Spec Sheet (For Task-Sized Work)

For a single feature or module, AIDD's epic file and SDD's spec sheet converge:

| | AIDD Epic | SDD Spec (task-sized) |
|-|-----------|-----------------------|
| Requirements | "Given X, should Y" | FR-001: MUST do X |
| Test spec | Implicit (TDD generates from requirements) | Explicit TC-001, TC-002 |
| Scope | "In scope"/"Out of scope" section | Explicit scope boundaries |
| Anti-patterns | Not standard (gets added after bugs) | Anti-patterns section from start |
| Verification | Tests pass = done | Verification clause + specific curl commands |

The SDD spec is more explicit and self-sufficient (a contractor could implement it cold). The AIDD epic assumes an agent that asks follow-up questions and has the vision document as background context.

**Best of both**: Write AIDD-style epics for standard features. Escalate to full SDD specs for complex integrations, reusable assets, or multi-country/multi-team deployments.

### AGENTS.md / CLAUDE.md / copilot-instructions.md — All the Same Idea

All three frameworks converge on the same architectural decision: persistent context files that agents read before every session.

| File | Framework | Scope |
|------|-----------|-------|
| `AGENTS.md` | AIDD (+ OpenAI Codex standard) | Cross-tool, every session |
| `CLAUDE.md` | Anthropic Claude Code | Claude-family sessions |
| `.github/copilot-instructions.md` | GitHub Copilot | Copilot sessions |
| `aidd-custom/AGENTS.md` | AIDD project layer | Project overrides |
| `.github/instructions/*.instructions.md` | GitHub Copilot | Path-scoped overrides |
| `.claude/rules/*.md` | Claude Code | Path-scoped overrides |

The pattern is identical. The implementation details differ slightly. **Write all of them** — they're the same content in different syntax, targeting different agents.

---

## Where AIDD Goes Deeper

### TDD Discipline

AIDD has the strongest TDD position of any AI framework:
- **Never implement before a failing test** — hard constraint, not a suggestion
- **Mocking is a code smell** — evaluate mock vs. integration on composite score (churn + correctness), not convenience
- **Test isolation rules** — tests must not share state, must not rely on each other
- **The 5 questions every test must answer** — gives, should, actual, expected, how-to-debug

The SDD/Copilot research mentions TDD but doesn't specify how to implement it. AIDD provides the exact rules.

**Integration into your SDD workflow**: Add the AIDD TDD rules to your spec sheet's "Test Requirements" section and to your `.github/copilot-instructions.md`. Agents following either framework will respect the same test quality standard.

### Hotspot Analysis (Churn)

AIDD's `npx aidd churn` provides a mathematical basis for refactoring decisions:

`Score = LoC × churn × complexity` — files that are large, frequently changed, AND complex are highest risk.

No equivalent exists in the SDD/Copilot framework. This is a pure AIDD contribution.

**Where it fits in SDD workflow**: Run `aidd churn --json` before writing any spec that modifies existing code. If the target files are hotspots, the spec should explicitly address complexity reduction (extract modules, reduce Cx). Add to the spec's "Non-Functional Requirements":

```markdown
## Technical Debt Requirements
- lib/auth/session.js currently scores 46420 on churn analysis (LoC × churn × Cx)
- This implementation MUST reduce the score by at least 20% by extracting
  the token refresh logic to a separate module
```

### Product Discovery Layer

AIDD's `/discover` command gives the agent PM capabilities: personas, user journeys, pain point severity × frequency, story maps. SDD/Copilot research jumps straight to technical specs.

The discovery layer answers: **what should we build and why?** The spec answers: **exactly how should it work?**

**Full workflow with both**: `/discover` → story map → SDD spec sheet → AIDD epic → `/execute`

### User Testing Integration

AIDD uniquely generates both human and AI agent testing scripts from user journeys. No equivalent in SDD/Copilot research.

**Where it fits**: After implementation, before marking an epic complete, run `/user-test` to generate the validation script. Add the test script output to the spec's verification clause.

### SudoLang for Skill Authoring

AIDD's skills are written in SudoLang — a token-efficient pseudocode. 20-30% fewer tokens than equivalent natural language for the same specification.

This matters for teams building custom skills or MCP server integrations. Writing your own custom agent skills (`.github/agents/`, `aidd-custom/skills/`) in SudoLang notation rather than pure natural language will reduce context consumption and improve specification precision.

---

## Where SDD Goes Deeper

### Large-Scale Spec Engineering

SDD addresses the production reality of 5000-line specs that generate 15,000 lines of production code. AIDD doesn't have equivalent guidance for this scale.

The 50-prompt spec iteration process, the factory/reuse pattern (Belgium → Netherlands via one prompt), and spec maintenance (bugs flow back to spec, anti-patterns section) are AIDD gaps.

**What AIDD lacks**:
- How to build a spec that works across multiple agent runs and model versions
- The factory pattern: how to derive country/variant specs from a base spec
- The spec maintenance discipline: AP-001, AP-002 anti-pattern sections

### Token Economics and Model Selection

The SDD/Copilot research has detailed cost analysis: model pricing tables, cost per spec cycle, caching strategies, breakeven vs. engineer time.

AIDD doesn't address economics at all. For teams making buy/build decisions on AI tooling, the token economics document is essential context that AIDD doesn't provide.

### Context Window Management

SDD research covers: context overflow handling, the performance cliff (0-200K normal, 200K-500K degraded, 500K-1M poor), selective file injection, the context surgery patterns, and prompt caching strategies.

AIDD's progressive discovery (only read what you need) is a good instinct but doesn't give teams the quantitative framework for managing large-codebase context.

### Automation at Scale

The SDD/Copilot research documents Copilot CLI automation patterns: bulk operations (document 100 repos), scheduled operations, CI/CD integration, the cloud agent REST API, and Copilot Automations (event-triggered).

AIDD's `/aidd-parallel` addresses parallel task execution but doesn't cover unattended bulk operations or CI/CD integration.

---

## Where They Complement Each Other

### The Combined Stack for Maximum Coverage

```
Product Layer:      AIDD /discover → story map → user stories
Requirements:       AIDD epic format ("Given X, should Y") 
                    + SDD functional requirements (RFC-2119 MUST/SHOULD)
Context Layer:      AIDD AGENTS.md + aidd-custom/AGENTS.md
                    + SDD .github/copilot-instructions.md + path-scoped instructions
Implementation:     AIDD /execute with TDD discipline
                    + SDD spec sheet for complex integrations
Code Quality:       AIDD /review + aidd-churn
                    + SDD spec compliance gate (automated CI check)
Maintenance:        AIDD /aidd-fix (bug → epic → failing test → fix)
                    + SDD bug-back-to-spec rule (AP-001, AP-002)
Scale:              AIDD /aidd-parallel for concurrent tasks
                    + SDD Copilot CLI for bulk/automated operations
Economics:          SDD token economics (AIDD doesn't cover this)
Validation:         AIDD /user-test + /run-test (SDD doesn't cover this)
```

### The RTC + Spec Pattern

AIDD's Reflective Thought Composition is the best structured reasoning framework for spec writing:

```
/aidd-rtc --compact
Problem: This spec section is ambiguous — "handle errors appropriately"

🎯 restate: spec says handle errors, no specifics on what errors, what response codes, what log
💡 ideate: (a) specify per endpoint (b) global error handler spec (c) enumerate all external error sources
🪞 reflect: ∵ Belgium case study: missing error spec → timeout handling bug in production ∴ (c) needed
🔭 expand: non-functional: GDPR → no error messages leak PII; observability: correlation IDs on all errors
⚖️ score: (c) + GDPR + correlation IDs wins; (a) is maintenance burden; (b) incomplete
💬 respond: Add error specification section: enumerate external APIs, define timeout/4xx/5xx responses per source, correlation IDs mandatory, PII scrubbing required
```

Use RTC (`/aidd-rtc --compact`) when iterating spec sections. It surfaces the reasoning chain, not just the conclusion.

### Vision Document → Spec Sheet Cascade

The AIDD vision document is the precursor to SDD spec sheets:

```
vision.md (1-2 pages, project-level)
  ↓
AIDD epic (100-500 lines, feature-level)
  ↓
SDD spec sheet (500-5000 lines, complex systems)
  ↓
Implementation (15,000+ lines of code)
```

Each level is appropriate for its scope. Don't write a 5000-line spec for a CRUD endpoint. Don't write a 2-page vision document for a multi-country compliance API. The cascade ensures each level is right-sized.

---

## Practical Synthesis: What to Use When

### Starting a New Project

```
1. Create vision.md (AIDD)
2. Run /discover (AIDD) → story map
3. For each major feature:
   a. /task (AIDD) → epic
   b. If feature is complex/integrates external APIs:
      → escalate to SDD spec sheet
      → add verification clause
      → add integration contracts
   c. /execute (AIDD) → TDD implementation
4. /review + aidd churn (AIDD)
5. For reusable components: use SDD factory pattern
```

### Fixing a Bug

```
/aidd-fix [description] → (AIDD)
  - adds Given/Should to epic
  - writes failing test
  - minimal fix
  - adds AP-XXX to spec sheet if relevant (SDD)
```

### Bulk Operations / Automation

```
Copilot CLI or cloud agent automation (SDD research)
  → document 100 repos
  → scheduled operations
  → CI/CD pipelines
```

AIDD's `/aidd-parallel` for real-time parallel agent work.
Copilot CLI patterns for unattended/batch operations.

### PR Review

```
/aidd-pr [PR URL] (AIDD) → triage, resolve, delegate fixes
Copilot automated PR review (SDD) → security scan, spec compliance gate
Both together: human sees only what passed both filters
```

### Writing New Agent Skills

```
/aidd-upskill create [name] (AIDD)
  → uses SudoLang syntax (AIDD)
  → follows same principle as .github/agents/*.md (SDD/Copilot)
  → validate with skills-ref or validate-skill (AIDD)
```

---

## The Key Insights Combining Both

**1. The spec is always the asset** — Both AIDD (epic as source of truth, vision.md as ground truth) and SDD (spec sheet as the asset, code as build artifact) agree on this. Code is disposable. Specifications are permanent.

**2. Context failure = agent failure** — Both frameworks' deepest insight. SDD's `.github/copilot-instructions.md` and AIDD's `AGENTS.md` + vision.md are both solving the same problem: agents need to know before they act.

**3. TDD makes AI code sustainable** — AIDD is explicit about this, SDD mentions it. The 8× code duplication increase with AI adoption is the problem; TDD is the structural countermeasure. Without test-first discipline, AI speed creates debt.

**4. Hotspot-informed development** — Running `aidd churn` before writing specs or starting work prevents the most common trap: applying AI speed to already-complex code and making it worse. Churn data should inform spec requirements.

**5. The factory matters more than any single implementation** — Belgium's ERSR → FRIS derivation via one prompt is the same principle as AIDD's skill system (write a skill once, use in any project). The reuse pattern — specs, skills, vision templates, epic templates — is where the leverage compounds.
