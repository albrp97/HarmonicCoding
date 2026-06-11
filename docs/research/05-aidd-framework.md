# AIDD Framework: Intelligence Document

> Deep analysis of the AIDD Framework by ParallelDrive (github.com/paralleldrive/aidd). Everything here is sourced directly from the codebase, installed and executed locally. Version 3.1.0.

---

## What AIDD Is

AIDD (AI-Driven Development) is a framework that installs a complete AI agent orchestration system into any project. It is not an AI model, not a plugin, and not a coding assistant. It is a **methodology encoded as a portable file system** — a collection of agent skills, workflow commands, SudoLang programs, and CLI tooling that gives any LLM-powered coding agent (Claude Code, Cursor, VS Code Copilot, ChatGPT) a structured operating procedure for building production software.

The problem AIDD solves is specifically stated in the README:

> *"GitClear tracked 211 million lines from 2020 to 2024 and found 8x more code duplication as AI adoption increased. Google's DORA report shows AI adoption correlates with 9% higher bug rates and degraded stability. Agents skip tests, couple modules, duplicate logic, and miss vulnerabilities."*

AIDD's answer: put high-quality software engineering processes on autopilot rails. Speed without discipline creates debt. AIDD is the discipline layer.

---

## Installation

```bash
# Bootstrap a new project (creates ai/ folder + .cursor symlink)
npx aidd --cursor my-project

# Add to an existing project (run from project root)
npx aidd --cursor

# Without Cursor integration
npx aidd

# Preview without copying
npx aidd --dry-run --verbose
```

What gets installed: the entire `ai/` directory tree into your project root. If `--cursor` is used, a `.cursor` symlink points to `ai/` so Cursor auto-discovers agent rules from `.cursor/rules/` — which is now the contents of `ai/`.

---

## The Complete File Structure Installed

```
ai/
  index.md                     # Root index (auto-generated from frontmatter)
  commands/                    # Workflow command shortcuts
    /discover, /task, /execute, /review, /log, /commit, /user-test, /run-test, ...
  skills/                      # 30+ reusable agent skills (SudoLang + Markdown)
    aidd-please/               # Master orchestrator — the "main entry point"
    aidd-tdd/                  # TDD process
    aidd-review/               # Code review
    aidd-task-creator/         # Task planning and execution
    aidd-requirements/         # Functional requirement writing
    aidd-product-manager/      # Product discovery, user stories, story maps
    aidd-churn/                # Hotspot analysis
    aidd-fix/                  # Bug fix process
    aidd-pr/                   # PR review comment triage
    aidd-parallel/             # Parallel sub-agent delegation
    aidd-agent-orchestrator/   # Multi-agent routing
    aidd-rtc/                  # Reflective Thought Composition
    aidd-javascript/           # JS/TS best practices
    aidd-react/                # React patterns
    aidd-stack/                # Next.js + React/Redux + Shadcn
    aidd-autodux/              # Redux autodux patterns
    aidd-upskill/              # How to create new skills
    aidd-user-testing/         # Human + AI test script generation
    aidd-sudolang-syntax/      # SudoLang cheat sheet
    aidd-log/                  # Activity log
    aidd-write/                # Writing assistance
    ... (30+ total)
  scaffolds/                   # Project templates (e.g. next-shadcn)

aidd-custom/                   # Project-specific customization (you edit this)
  AGENTS.md                    # Project overrides (higher priority than root)
  config.yml                   # Configuration flags
  skills/                      # Project-specific skills

AGENTS.md                      # Root agent instructions (auto-loaded by agents)
vision.md                      # (YOU create this) Project source of truth
```

---

## SudoLang: The Prompt Language

AIDD uses **SudoLang** — a pseudocode language specifically designed for prompting LLMs. All skills are written in a mix of Markdown (natural language) and SudoLang (structured logic).

### Why SudoLang works

1. **20-30% fewer tokens** than equivalent natural language prompts (demonstrated in research)
2. **Reduces structured output tokens by up to 85%** when using YAML/CSV format specifiers
3. **Deterministic control flow** for complex agent programs with state
4. **Typed interfaces** reduce malformed responses
5. **Pseudocode improves reasoning performance** vs natural language (arxiv:2305.11790)

### SudoLang syntax essentials

```sudolang
// Interfaces
UserStory {
  id: String
  persona: Persona
  jobToDo: String
  functionalRequirements
  priority = painPoint ~> impact * frequency  // computed property
}

// Constraints block
Constraints {
  A constraint in natural language
  (logic is deterministic) => CLI tool or compiled binary
  (logic requires judgment) => AI prompt
}

// Functions
fn think(input, options) {
  show work:
    🎯 restate |> 💡 ideate |> 🪞 reflectSelfCritically |>
    🔭 expandOrthogonally |> ⚖️ scoreRankEvaluate |> 💬 respond
}

// Semantic pattern matching
match (contextRequirements) {
  > 1 guide => use withCLI
  default => use directExecution
}

// Pipeline composition
analyze = collectHotspots |> interpretResults |> recommend
```

### When to use SudoLang vs natural language

> *"For most simple prompts, natural language is better. Use it. But if you need the AI to follow a program, obey constraints, keep track of complex state, or implement complex algorithms, SudoLang can be extremely useful."*

---

## The Core Workflow: `/discover → /task → /execute → /review → /commit`

### Phase 1: `/discover`

Activates `aidd-product-manager`. The PM agent conducts product discovery:
- Identifies user personas
- Maps user journeys (saved to `plan/story-map/`)
- Writes user stories in `As a $persona, I want $jobToDo, so that $benefit` format
- Generates functional requirements: `Given $situation, should $jobToDo`

**What the story map produces**: A structured YAML document with personas, journeys, and user stories with pain point severity × frequency scores for prioritization.

### Phase 2: `/task`

Activates `aidd-task-creator`. The task creator:
1. Reads the story and functional requirements
2. Assesses if specialized agent expertise is needed (routes to orchestrator if yes)
3. Decomposes into atomic, sequential tasks (each ~50 lines of code or less)
4. Creates an epic file in `tasks/` using this exact template:

```markdown
# ${EpicName} Epic

**Status**: 📋 PLANNED
**Goal**: ${briefGoal}

## Overview

${singleParagraphStartingWithWHY}

---

## ${TaskName}

${briefTaskDescription}

**Requirements**:
- Given ${situation}, should ${jobToDo}
- Given ${situation}, should ${jobToDo}
```

**Epic constraints**: No task numbering. No extra sections. Requirements in "Given X, should Y" format only. Overview starts with WHY.

### Phase 3: `/execute`

Activates `aidd-task-creator` in execution mode with `aidd-tdd`. The execution loop:

1. Read epic requirements
2. If complex → dispatch to `aidd-agent-orchestrator`
3. For each task: write failing test FIRST
4. Run test runner: watch fail
5. Implement ONLY enough code to pass the test
6. Run tests: fail → fix; pass → continue
7. Every 3 tasks: `/review` → `/commit`
8. Re-read epic to verify still on track
9. On completion: update status → move to `tasks/archive/YYYY-MM-DD-epic.md`

**Critical constraint**: Never implement before a failing test exists. This is the hardest rule and the most important one.

### Phase 4: `/review`

Activates `aidd-review`. The review process:

1. Run `aidd-churn` to identify hotspot files in the diff
2. For each relevant skill, read the SKILL.md before reviewing
3. Check: code quality, JS best practices (aidd-javascript), TDD coverage (aidd-tdd), React patterns, Redux, IO effects, OWASP Top 10, commit message quality
4. Cross-reference completed work vs. epic requirements
5. Cross-reference vs. epic task plan in `tasks/`
6. Output: actionable feedback with specific improvement suggestions

The review explicitly lists all 10 current OWASP categories and checks each.

### Phase 5: `/log` and `/commit`

`aidd-log` collects salient changes and writes to `activity-log.md`.

`/commit` uses conventional commit format. The commit message is generated by the agent from the diff — not written by hand.

---

## The Vision Document: Agent Ground Truth

The `vision.md` file is the single most important file in an AIDD project. All agents read it before starting any task.

```
AGENTS.md rule: "Before creating or running any task, agents MUST first read the vision document (vision.md) in the project root."
```

If a task conflicts with the vision document, the agent must stop, explain the conflict, and wait for user resolution. It never proceeds with a contradicting task.

### What a good vision document contains

```markdown
## Purpose
[1 paragraph: what problem, for whom, what makes it different]

## Goals
1. **Primary**: [specific, measurable outcome]
2. **Secondary**: [supporting goal]

## Non-Goals
- [Things this project intentionally will NOT do]

## Technical Constraints
- [Stack, deployment environment, version constraints]
- [Architectural decisions that are locked]

## Success Criteria
- [How you know the project succeeded]

## Key User Personas
- [Who uses this and what they care about]
```

**What makes it work**: The vision document is intentionally short (fits in context), stable (doesn't change for every feature), and constraint-focused. Agents use it to make aligned decisions without asking every time.

---

## AGENTS.md and Progressive Discovery

The root `AGENTS.md` instructs agents on how to use the `ai/` system:

```markdown
## Progressive Discovery

Agents should only consume the root index until they need subfolder contents:
- If the project is Python, skip JavaScript-specific folders
- If working on backend logic, skip frontend UI folders
- Only drill into subfolders when the task requires that specific domain knowledge

This approach minimizes context consumption and keeps agent responses focused.
```

Each `ai/` subdirectory has an auto-generated `index.md` (from frontmatter) — agents read the index, find the relevant skill, then load only that SKILL.md. Not everything at once.

### The import system

AGENTS.md uses `import @skills/index.md` to load the skills index. Skills then import their references on-demand:

```markdown
# SKILL.md
import references/process.md   # only loads when skill is active
import references/types.md
```

This progressive loading keeps context lean without losing depth.

### aidd-custom/ — The Override Layer

Project-specific customization lives here. `aidd-custom/AGENTS.md` is imported at the bottom of root `AGENTS.md` and its settings take precedence:

```yaml
# aidd-custom/config.yml
e2eBeforeCommit: true   # run e2e tests before every commit (default: false)
```

```markdown
# aidd-custom/AGENTS.md
[project-specific rules that override root AGENTS.md]
```

```
aidd-custom/skills/   # project-specific skills not in core
```

---

## `aidd-churn`: Hotspot Analysis

The churn command identifies the highest-risk files in a codebase by composite score:

**Formula**: `Score = LoC × churn × complexity (Cx)`

```bash
npx aidd churn                              # top 20, 90-day window, min 50 LoC
npx aidd churn --days 30 --top 10 --min-loc 100
npx aidd churn --json                       # machine-readable, for PR cross-reference
```

**Sample output from the AIDD repo itself:**
```
Score   LoC  Churn  Cx  Density  File
─────  ────  ─────  ──  ───────  ─────────────────────────────
46420   422      5  22      32%  lib/scaffold-resolver.js
42168  1506      4   7      15%  lib/scaffold-resolver.test.js
 9464   364      2  13      30%  lib/index-generator.js
```

**Signal interpretation:**
- **High LoC**: Large file — large blast radius when it changes
- **High Churn**: Frequently changed — instability risk
- **High Cx**: Complex branches — comprehension and test risk
- **Low Density**: Compresses heavily — structural repetition likely

**Use in review workflow**: The `/review` skill runs `aidd churn --json` at the start and cross-references against the PR diff. Files appearing in both get flagged for extra scrutiny.

**Threshold triggers automatic refactor analysis**: `Cx > 9 | LoC > 400 | density < 35%` → the skill walks through decomposition paths and recommends if the composite score drops >15%.

---

## RTC: Reflective Thought Composition

RTC is the thinking pipeline embedded in most skills. It forces structured reasoning before any response:

```
🎯 restate    → Restate the problem in own words (confirms understanding)
💡 ideate     → Generate multiple options or approaches
🪞 reflect    → Critically identify flaws in the ideation
🔭 expand     → Explore orthogonal considerations not yet covered
⚖️ score      → Rank/evaluate options against explicit criteria
💬 respond    → Final natural language response
```

**Two modes:**
- `--compact`: Internal reasoning pass (dense noun phrases, emojis as shortcuts, load-bearing tokens only). Every stage is compressed but causal — using `∵` (because) and `∴` (therefore) explicitly. Used when the RTC output feeds another step, not the user.
- `--depth N (1-10)`: User-facing explanation density. 1 = ELIF, 10 = PhD-level.

**Test: Pass/fail for compact mode:**
- ✅ Pass: Remove any word → lose meaning. Reflect/score show explicit causal chain.
- ❌ Fail: Consultant prose. Hedging. Filler. Conclusions without reasoning.

---

## The TDD Skill: Rules That Eliminate AI Code Debt

The `aidd-tdd` skill is where AIDD's quality guarantee lives. The rules are specific and non-negotiable:

### The `assert` type

Every test must answer 5 questions:
1. What is the unit under test? (named describe block)
2. What is the expected behavior? (`given` and `should` are adequate)
3. What is the actual output? (unit under test was exercised)
4. What is the expected output? (`expected` and/or `should` are adequate)
5. How can we find the bug? (implicitly answered if 1-4 are correct)

### Mocking rules (controversial and specific)

> *"Mocking is a code smell."*

When a mock is considered:
1. Build BOTH a mocked and an integration candidate
2. Run `aidd-churn` to compare total code impact
3. Winning approach must: (a) lower or match composite score AND (b) meaningfully exercise the functional requirement
4. Mocks are only justified when real integration is technically infeasible or prohibitively expensive (irrecoverable real-world side effects, physical infrastructure unavailable in CI, or per-run cost makes the test suite economically non-viable)

### Isolation rules
- Tests must not rely on external state
- Tests must not rely on other tests
- For integration tests: test integration with the real system
- **Never use `@testing-library/react`** (redundant with Riteway render + Playwright patterns)

---

## The Skills Library: Quick Reference

| Skill | What it does |
|-------|-------------|
| `aidd-please` | Master orchestrator — routes all commands, wraps every workflow |
| `aidd-tdd` | TDD process: failing test first, strict isolation, real integration > mocks |
| `aidd-review` | 10-step code review: churn analysis, OWASP Top 10, requirements cross-check |
| `aidd-task-creator` | Epic planning and execution: decompose, TDD, every-3-tasks review+commit |
| `aidd-requirements` | Write functional requirements: "Given $situation, should $jobToDo" |
| `aidd-product-manager` | Product discovery: personas, user journeys, story maps, user stories |
| `aidd-fix` | Bug fix process: reproduce → document requirement in epic → failing test → fix → commit |
| `aidd-churn` | Hotspot analysis: LoC × churn × Cx scoring, refactor recommendations |
| `aidd-pr` | PR triage: list open threads, resolve addressed ones, delegate fixes to sub-agents |
| `aidd-parallel` | Fan work to parallel sub-agents via /aidd-fix delegation prompts |
| `aidd-agent-orchestrator` | Route requests to right specialized agent |
| `aidd-rtc` | Reflective Thought Composition: structured reasoning pipeline |
| `aidd-upskill` | Guide for creating new skills (meta-skill) |
| `aidd-user-testing` | Generate human + AI agent test scripts from user journeys |
| `aidd-javascript` | JS/TS: functional, pure functions, no class/extends, DOT/YAGNI/KISS/DRY |
| `aidd-stack` | Next.js + React/Redux + Shadcn: container/presentation, autodux, sagas |
| `aidd-react` | React component patterns |
| `aidd-autodux` | Redux state management (autodux pattern, no RTK) |
| `aidd-javascript-io-effects` | Side effects via saga pattern |
| `aidd-log` | Activity log with emoji categorization |
| `aidd-sudolang-syntax` | SudoLang cheat sheet |
| `aidd-write` | Writing assistance |
| `aidd-pipeline` | Pipeline orchestration patterns |
| `aidd-service` | Service layer patterns |
| `aidd-layout` | Layout and design tokens |
| `aidd-ui` | UI/UX design |
| `aidd-jwt-security` | JWT auth (recommends opaque tokens over JWT) |
| `aidd-timing-safe-compare` | Timing-safe secret comparison |
| `aidd-error-causes` | Error cause patterns |
| `aidd-ecs` | Entity component system |
| `aidd-namespace` | Type namespace patterns |
| `aidd-structure` | Project structure patterns |
| `aidd-lit` | Lit web component patterns |

---

## User Testing Integration

AIDD uniquely integrates user testing into the AI workflow. The `/user-test` command generates two types of scripts from a user journey:

**Human scripts**: Think-aloud protocol with video recording instructions for manual testing

**AI agent scripts**: Executable test scripts with persona-based behavior and screenshot validation

```bash
/discover               # Create user journey → plan/story-map/
/user-test journey.yaml # Generate both scripts → plan/
/run-test agent-script  # Execute AI agent test in real browser
```

*Research basis*: Nielsen Norman Group found 3-5 users reveal 65-85% of usability problems.

---

## AI Evals: Testing Skill Quality

AIDD includes an eval framework for testing whether skills produce correct output:

```
ai-evals/
  aidd-review/review-skill-test.sudo
  aidd-upskill/caveman-test.sudo
  aidd-parallel/prompt-generation-test.sudo
  ...
```

Each `.sudo` file imports a skill and defines `Given X, should Y` assertions:

```sudolang
import 'ai/skills/aidd-review/SKILL.md'

userPrompt = """Run /review on fixtures/user-service.js"""

- Given user-service.js builds SQL queries with string concatenation, should flag SQL injection vulnerability
- Given user-service.js compares secrets with === operator, should flag timing-unsafe secret comparison
```

Run evals:
```bash
npm run test:ai-eval
# Uses: riteway ai "$f" --runs 1 --threshold 75 --timeout 600000 --agent claude
```

This is the mechanism for maintaining skill quality as models change — you can verify the skill still produces the expected outputs against new model versions.

---

## AIDD Server Framework

A lightweight Node.js server framework built for function composition:

```javascript
import { createRoute, withRequestId, createWithConfig, loadConfigFromEnv } from 'aidd/server';

// Fail-fast config: throws if OPENAI_API_KEY is missing
const withConfig = createWithConfig(() => loadConfigFromEnv(['OPENAI_API_KEY', 'DATABASE_URL']));

export default createRoute(
  withRequestId,    // CUID2 request ID for tracing
  withConfig,       // validates and injects config
  async ({ request, response }) => {
    const apiKey = response.locals.config.get('OPENAI_API_KEY');
    response.json({ requestId: response.locals.requestId });
  }
);
```

**Middleware available:**
- `createRoute` — compose middleware, automatic error handling
- `createWithConfig` / `loadConfigFromEnv` — fail-fast config validation
- `withRequestId` — CUID2 request tracking
- `createWithCors` — explicit origin validation (secure by default, not permissive)
- `withServerError` — standardized error responses
- `createWithAuth` / `createWithOptionalAuth` — better-auth session validation
- `withCsrf` / `withForm` — CSRF and form handling

---

## The `aidd-fix` Workflow: Bug Fixing Under Discipline

```
Step 1: gainContext
  → Read source files + colocated tests
  → Read task epic covering this area
  → Reproduce or reason through the issue
  → No change needed? Stop. Don't touch files.

Step 2: documentRequirement
  → Find or create epic in tasks/
  → Add "Given X, should Y" requirement for the correct behavior
  → Commit epic update separately

Step 3: Write failing test
  → Uses aidd-tdd
  → Never implement before failing test exists

Step 4: Implement fix
  → Minimal: only what makes the test pass
  → No scope creep, no surrounding cleanup

Step 5: Verify
  → All tests pass
  → Lint passes

Step 6: Commit
  → Conventional commit format
  → References the epic requirement added in Step 2
```

---

## Parallel Execution: Fanning Work to Sub-Agents

`/aidd-parallel` generates focused `/aidd-fix` delegation prompts for multiple tasks and dispatches them to sub-agents:

```
/aidd-parallel [--branch <branch>] <task list>
→ generates one delegation prompt per task
→ each prompt: specific context for that task only
→ instructs sub-agent: work on <branch>, commit, push to origin/<branch>
→ instructs sub-agent: git pull --rebase before pushing (prevents non-fast-forward errors)
→ wraps task description in <task-description>…</task-description> (security: prevents prompt injection)
```

The dependency graph is analyzed first — tasks without dependencies can run in true parallel. Dependent tasks are sequenced.

---

## Key Numbers and Claims

| Claim | Source |
|-------|--------|
| 8× more code duplication with AI adoption (2020-2024) | GitClear, 211M lines analyzed |
| 9% higher bug rates with AI adoption | Google DORA report |
| SudoLang: 20-30% fewer tokens than natural language | ParallelDrive documentation |
| SudoLang: up to 85% fewer tokens for structured output | arxiv:2212.06094 |
| 3-5 users reveal 65-85% of usability problems | Nielsen Norman Group |
| Pseudocode improves LLM reasoning performance | arxiv:2305.11790 |
