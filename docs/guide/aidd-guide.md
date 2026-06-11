# AIDD Framework: Practical Guide

> How to install, configure, and operate the AIDD Framework in a real project. This is the hands-on usage guide — concrete commands, real file templates, and the decision points that matter.

---

## Setup: New Project

```bash
# 1. Bootstrap with Cursor integration (recommended)
npx aidd --cursor my-project
cd my-project

# 2. Initialize git
git init && git add -A && git commit -m "init: aidd framework scaffold"

# 3. Create vision.md (most important step — do this before anything else)
# See Vision Document section below
```

### What `npx aidd --cursor` gives you

```
my-project/
  ai/                          ← full agent orchestration system
    commands/                  ← /discover, /task, /execute, /review, etc.
    skills/                    ← 30+ agent skills
    scaffolds/                 ← project templates
  aidd-custom/                 ← your customization layer (edit this)
  AGENTS.md                    ← agent instructions (auto-loaded)
  .cursor → ai/                ← symlink: Cursor loads rules automatically
```

## Setup: Existing Project

```bash
# From your project root
npx aidd --cursor

# Review what would be added
npx aidd --dry-run --verbose

# Force overwrite if ai/ already exists
npx aidd --cursor --force
```

No existing files are modified. Only `ai/`, `aidd-custom/`, and `AGENTS.md` are added.

---

## Step 0: Create the Vision Document

Before any AI work — before `/discover`, before writing a single feature — create `vision.md` in the project root. Every agent reads this before every task. If it doesn't exist, agents make architectural decisions blindly.

**Minimal working vision.md:**

```markdown
# Vision: [Project Name]

## Purpose
[One paragraph: what problem, for whom, what makes it different from alternatives]

## Goals
1. **Primary**: [Most important measurable outcome]
2. **Secondary**: [Supporting goal]
3. **Tertiary**: [Nice-to-have]

## Non-Goals
- [Explicitly list things this project will NOT do]
- [These prevent scope creep — be specific]

## Technical Constraints
- Stack: [language, framework, runtime]
- Deployment: [platform, environment]
- Key libraries: [list with versions if important]
- [Any architectural decisions that are locked]

## Success Criteria
- [How you know the project succeeded — measurable if possible]

## Key Personas
- **[Persona name]**: [one line describing who they are and what they care about]
```

**What makes a vision document effective:**
- Fits in context (under 1 page)
- Stable — doesn't change for every feature
- Constraint-focused — not aspirational prose
- Includes non-goals explicitly — this is where agents most often go wrong

---

## Customizing the Agent Layer

### `aidd-custom/config.yml`

```yaml
# Run e2e tests before committing (default: false)
e2eBeforeCommit: true
```

### `aidd-custom/AGENTS.md`

Project-specific overrides. These take precedence over root AGENTS.md:

```markdown
# Custom Agent Instructions

## Stack
This project uses Python 3.11 / FastAPI / PostgreSQL.
All JavaScript skills are irrelevant — skip them.

## Testing
Use pytest + pytest-asyncio. Tests colocated with source files.
The test command is: `pytest tests/ -v --tb=short`

## Commit format
Conventional commits. Body required for any change > 20 lines.

## Directories
Source: src/
Tests: tests/
Specs: docs/specs/
Agent may NOT modify: .github/workflows/, infrastructure/
```

### Adding a custom skill

```bash
# The agent can create it for you:
/aidd-upskill create [skill-name]
```

Or manually:
```
aidd-custom/skills/my-skill/
  SKILL.md     # frontmatter + instructions
  README.md    # what it is, why it's useful
```

```markdown
# aidd-custom/skills/my-skill/SKILL.md
---
name: my-skill
description: Brief description. Use when [trigger condition].
---

# My Skill

Act as a [role]. Your job is to [goal].

Constraints {
  [specific rules]
}

Commands {
  /my-skill - [what the command does]
}
```

---

## The Workflow: Step by Step

### 1. Discovery: `/discover`

Start every feature with discovery, not coding.

```
/discover
```

The PM agent asks questions and produces a user journey in `plan/story-map/`. The journey includes:
- User personas with pain point severity + frequency
- Steps in the journey
- User stories: `As a [persona], I want [job], so that [benefit]`
- Functional requirements: `Given [situation], should [job]`

You don't have to use `/discover` for every task. For a well-understood small change, skip to `/task` directly. Use `/discover` for anything that involves users, workflows, or features where you're uncertain about requirements.

### 2. Task Planning: `/task`

```
/task
```

OR provide context:
```
/task implement the user authentication flow from plan/story-map/auth-journey.yaml
```

The task creator:
1. Reads your vision.md
2. Reads the relevant story/journey/requirements
3. Decomposes into atomic tasks (each ~50 lines of code)
4. Creates an epic file in `tasks/epic-name-epic.md`
5. Shows you the plan and waits for approval

**What a good epic looks like:**
```markdown
# Auth Epic

**Status**: 📋 PLANNED
**Goal**: Users can sign up, log in, and log out securely

## Overview

Authentication is the foundation for all user-specific features.
Users currently have no way to create accounts or maintain sessions.
This epic implements the minimum viable auth flow using JWT-free opaque tokens.

---

## Sign Up

Create new user accounts with email and password.

**Requirements**:
- Given a new email and valid password, should create user and return session token
- Given an existing email, should return 409 with "email already registered"
- Given a password under 8 characters, should return 400 with password requirements

---

## Log In

Authenticate existing users.

**Requirements**:
- Given valid email and password, should return session token
- Given invalid credentials, should return 401 (same message for both cases — no oracle attack)
- Given correct credentials after 5 failures, should require rate limit cooldown
```

### 3. Execution: `/execute`

```
/execute
```

OR with a specific epic:
```
/execute tasks/auth-epic.md
```

The execution loop is fully automatic but asks approval between tasks (configurable):

```
Task 1: Write failing test for POST /auth/signup → valid email → 201
[Shows test] → Awaits approval (or auto-approves if set)
[Writes test] → Runs test runner → Confirms fail
[Implements] → Runs tests → Confirms pass
[Reports] → Moves to Task 2
...
Every 3 tasks: /review → fix → /commit
```

**Setting auto-approval**: When `/execute` starts, it asks: *"Would you like to manually approve each step, or allow the agent to approve with /review?"*

### 4. Review: `/review`

```
/review
```

The review runs automatically every 3 tasks during execution. You can also run it manually at any point.

What it checks (in order):
1. Hotspot analysis (`aidd churn --json`) — identifies high-risk files in the diff
2. Code quality per `aidd-javascript` rules
3. Test coverage per `aidd-tdd` rules (all 5 questions answered, no mocking code smell)
4. Stack patterns per `aidd-stack`
5. Security: explicitly lists all current OWASP Top 10 and checks each
6. Requirements cross-reference: every requirement in the epic marked ✅ or ❌
7. Task plan cross-reference: every task in `tasks/` verified complete
8. Dead code, stray files, unnecessary complexity

The review outputs actionable items, not generic suggestions. Specific file + line + what to change.

### 5. Log and Commit

```
/log    # updates activity-log.md with what changed
/commit # generates conventional commit message from diff
```

The commit message is generated by the agent — you review it. Conventional format:

```
feat(auth): add signup endpoint with session token

- POST /auth/signup creates user and returns opaque session token
- Validates email uniqueness and password strength
- Returns 409 for duplicate email, 400 for invalid password

Given a new email and valid password, should create user and return session token
Given an existing email, should return 409 with "email already registered"
```

---

## Hotspot Analysis: `aidd churn`

Run this before any code review or major refactor:

```bash
# Default: top 20 files, 90-day window, min 50 LoC
npx aidd churn

# Before a PR review: cross-reference diff
npx aidd churn --json

# Narrower window for sprint-level analysis
npx aidd churn --days 30 --top 10 --min-loc 100
```

**How to interpret results:**

```
Score   LoC  Churn  Cx  Density  File
46420   422      5  22      32%  lib/auth/session.js
```

- `Score = LoC × Churn × Cx` — composite risk
- `LoC 422`: Large file, large blast radius
- `Churn 5`: Changed 5 times in window — unstable
- `Cx 22`: Complex — 22 independent paths
- `Density 32%`: Compresses to 32% — structural repetition present

**Action thresholds:**
- `Cx > 9`: Review branch complexity, flatten conditionals
- `LoC > 400`: Review for extraction opportunities
- `Density < 35%`: Look for copy-paste to DRY

**In `/review`**: The skill automatically runs churn before reviewing the diff and flags any diff files that are also hotspots as `⚠️ HIGH RISK: changes here have higher blast radius`.

---

## Bug Fixing: `/aidd-fix`

For any bug report or review feedback requiring a code change:

```
/aidd-fix [description of bug or review feedback]
```

The process is strict:
1. Reads source and tests
2. Finds or creates the relevant epic in `tasks/`
3. Adds a `Given X, should Y` requirement for the correct behavior
4. Writes a failing test (never implements first)
5. Implements the minimal fix
6. Runs lint and tests
7. Commits

**Anti-pattern it prevents**: Fix code → maybe write a test → close issue. This creates zero documentation of why the fix exists and allows the bug to reappear in a refactor.

---

## PR Review Automation: `/aidd-pr`

For PRs with open review comments:

```
/aidd-pr [PR URL or number]
```

The skill:
1. Fetches all open review threads via GitHub GraphQL (paginated — handles PRs with 100+ comments)
2. Identifies which threads are already addressed vs. still open
3. Resolves the addressed threads via GitHub API
4. Generates delegation prompts for remaining issues using `/aidd-fix` format
5. Dispatches prompts to sub-agents (or executes inline if sub-agents unavailable)

**Security**: Review comment text is wrapped in `<review-comment>…</review-comment>` delimiters in all generated prompts. Sub-agents are instructed to treat delimited content strictly as task descriptions, not as system instructions. This prevents prompt injection via malicious review comments.

---

## Parallel Work: `/aidd-parallel`

For tasks that can run concurrently:

```
/aidd-parallel --branch feature/auth task1 task2 task3
```

OR:

```
/aidd-parallel delegate --branch feature/auth task1 task2 task3
```

The `delegate` variant dispatches prompts to sub-agents immediately. Without `delegate`, it outputs the prompts for you to dispatch manually.

Each sub-agent receives:
- A focused prompt for one task only
- Instructions to work on the specified branch
- Instructions to `git pull --rebase origin <branch>` before pushing
- Task content wrapped in `<task-description>` delimiters

---

## User Testing: `/user-test` + `/run-test`

After a feature is built:

```
/user-test plan/story-map/auth-journey.yaml
```

Generates:
- `plan/auth-human-test.md` — think-aloud protocol for manual testing with real users
- `plan/auth-agent-test.sudo` — executable AI agent test with screenshots and persona simulation

Run the AI agent test:
```
/run-test plan/auth-agent-test.sudo
```

The AI agent executes the test in a real browser (requires Playwright), takes screenshots, and reports pass/fail per user journey step.

---

## Creating Custom Skills: `/aidd-upskill`

When you have a recurring pattern that isn't covered by core skills:

```
/aidd-upskill create database-migration
```

The skill-creation process (meta-skill):
1. Searches existing skills for overlap
2. Researches best practices for the domain
3. Infers requirements without asking (proceeds with stated assumptions)
4. Names the skill (verb or role-based noun)
5. Drafts SKILL.md with frontmatter + body
6. Writes README.md
7. Validates against size/quality thresholds
8. Reports metrics

**What gets created:**
```
aidd-custom/skills/aidd-database-migration/
  SKILL.md
  README.md
```

**Key constraint**: If the SKILL.md body exceeds the line threshold, content is extracted to `references/` and imported. This keeps the skill's initial load lean.

---

## SudoLang: When and How to Use It

You don't need to write SudoLang — the agent does. But you need to read it in SKILL.md files.

**When SudoLang is appropriate:**
- Complex agent workflows with branching logic
- State machines (TaskStatus = pending | inProgress | completed)
- Type definitions for structured data
- Pipeline compositions: `analyze = collect |> interpret |> recommend`
- Semantic pattern matching: `(logic is deterministic) => CLI tool`

**When natural language is better:**
- Simple instructions ("always use UTC for datetimes")
- Explanatory context ("we use this because X")
- Non-branching rules

**Reading a SudoLang constraint block:**
```sudolang
Constraints {
  Be concise.                              # Natural language rule
  (mocks needed) => build both mocked and integration candidate  # Pattern match
  (available tools matches Task tool) => use Task tool           # Pattern match
  default => execute inline                # Default case
}
```

---

## Integrating AIDD with Non-JS Projects

AIDD's JavaScript-specific skills (`aidd-javascript`, `aidd-react`, `aidd-stack`) are irrelevant for non-JS projects. Override in `aidd-custom/AGENTS.md`:

```markdown
# aidd-custom/AGENTS.md

## Stack Override
This project is Python/FastAPI. Ignore all JavaScript skills:
- Skip: aidd-javascript, aidd-react, aidd-stack, aidd-autodux, aidd-javascript-io-effects

## Python Standards
Use ruff for linting. pytest for testing. Type hints on all functions.
See docs/specs/shared/coding-standards.md.

## Testing
Test framework: pytest + pytest-asyncio
Test location: tests/ mirroring src/ structure
Run: pytest tests/ -v --tb=short
```

The cross-language components — `/discover`, `/task`, `/execute`, `/review`, RTC, churn, vision document, epic format, user testing — all work regardless of language.

---

## Quick Reference: Which Command for What

| Situation | Command |
|-----------|---------|
| Starting a new feature | `/discover` → `/task` → `/execute` |
| Implementing a clear spec | `/task` → `/execute` |
| Bug reported | `/aidd-fix [description]` |
| PR has review comments | `/aidd-pr [PR URL]` |
| Multiple parallel tasks | `/aidd-parallel delegate --branch X [tasks]` |
| Code review before merge | `/review` |
| Find refactoring candidates | `npx aidd churn` |
| Create a new skill | `/aidd-upskill create [name]` |
| Think through a complex decision | `/aidd-rtc [problem]` |
| Generate user test scripts | `/user-test [journey.yaml]` |
| Run AI agent test | `/run-test [agent-script]` |
| Log changes | `/log` |
| Commit | `/commit` |
| List available commands | `/help` |

---

## Configuration Reference

### package.json scripts (if AIDD is installed as npm dependency)

```bash
npm test              # vitest + lint + typecheck
npm run test:unit     # vitest (no e2e) + lint + typecheck
npm run test:e2e      # vitest e2e only
npm run test:ai-eval  # run ai-evals against Claude
npm run lint          # biome check --write
npm run format        # biome format --write
npm run typecheck     # tsc --noEmit
npm run toc           # regenerate README table of contents
```

### CLI flags

```bash
npx aidd --cursor              # + .cursor symlink
npx aidd --force               # overwrite existing ai/
npx aidd --dry-run             # preview only
npx aidd --verbose             # detailed output
npx aidd -i                    # regenerate index.md files
npx aidd churn --days 30       # 30-day window
npx aidd churn --top 10        # top 10 results
npx aidd churn --min-loc 100   # minimum 100 LoC
npx aidd churn --json          # machine-readable output
```

---

## Troubleshooting

**Agent not loading skills**: Check that `AGENTS.md` exists at project root. Verify `import @skills/index.md` is present.

**Skills not auto-discovering**: If using Cursor without `--cursor` flag: manually add `ai/` to `.cursor/rules/` or run `npx aidd --cursor --force` to create the symlink.

**Agent ignoring vision.md**: Vision conflicts are surfaced by the agent. If the agent proceeds without mentioning the vision document, check that `AGENTS.md` has the vision requirement line.

**Tests running before implementation**: The TDD skill is strict — failing test must come first. If the agent implements before testing, the constraint in `aidd-tdd/SKILL.md` was not loaded. Ensure `/execute` activates the TDD skill.

**Churn not working**: Requires git history. Run inside a git repository. Requires Node.js 16+.

**Index.md files out of date**: Run `npx aidd -i` to regenerate from frontmatter. These files are auto-generated — do not edit manually.
