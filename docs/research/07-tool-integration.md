# Tool Integration: AIDD as Auto-Invoked Agent Tools

> The AIDD workflow normally requires typing slash commands: `/discover`, `/task`, `/aidd-fix`, etc. This document covers how to wire AIDD skills as automatically-selected tools in OpenCode and GitHub Copilot — so the agent picks the right AIDD workflow on its own based on what you say.

---

## The Core Technical Reality

One fact changes the integration architecture entirely:

**AIDD slash commands are not shell executables.** They are markdown instruction files the LLM reads:

```
ai/commands/aidd-fix.md
# 🐛 /aidd-fix
Load and execute the skill at `ai/skills/aidd-fix/SKILL.md`.
```

`/discover`, `/task`, `/execute`, `/review`, `/aidd-fix`, `/aidd-pr` — all are a few lines of prose that redirect the agent to a `SKILL.md` file. They are prompts, not programs.

**What is a real CLI tool**: `npx aidd churn` is the only command that runs executable code (git log parsing + LoC × complexity scoring). It wraps directly in any tool runner.

The integration strategy for both platforms: teach the agent to load the right `SKILL.md` automatically when the user's intent matches.

---

## Platform 1: OpenCode — Native Support, Zero Code

OpenCode (github: `anomalyco/opencode`, package: `opencode-ai`) has a **built-in `skill` tool** designed for exactly this.

### How it works

OpenCode discovers all `SKILL.md` files from these directories:
- `.opencode/skills/<name>/SKILL.md` — project-local
- `~/.config/opencode/skills/<name>/SKILL.md` — global

The `skill` tool builds its description from all discovered skills and their intent descriptions. When the LLM receives a user message, it reads the tool list, sees `skill` with all available skills listed, and calls `skill({ name: "aidd-fix" })` automatically.

AIDD's `ai/skills/index.md` already has machine-readable "when to use" descriptions for all 35 skills:
```
aidd-fix - Fix a bug or implement review feedback following the AIDD fix process.
  Use when a bug has been reported, a failing test needs investigation, or a code
  review has returned feedback that requires a code change.
```

### Setup

```bash
# AIDD already installed (npx aidd)
mkdir -p .opencode
ln -s ../ai/skills .opencode/skills
```

That's it. All 35 AIDD skills are auto-invokable. Say "fix this bug" → OpenCode calls `skill({ name: "aidd-fix" })` and loads the full TDD bug-fix workflow. No slash commands.

### Add churn as a custom tool (optional)

Create `.opencode/tools/aidd_churn.ts`:

```typescript
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "Run AIDD churn analysis to find high-risk files by LoC × git churn × cyclomatic complexity. Use before any refactoring or when deciding where to focus technical debt work.",
  parameters: {
    days: tool.schema.number().describe("Days of git history").default(90),
    top: tool.schema.number().describe("Top N files to return").default(20)
  },
  async execute(args) {
    const { $ } = await import("bun")
    const result = await $`npx aidd churn --days ${args.days} --top ${args.top} --json`.text()
    return JSON.parse(result)
  }
})
```

`npx aidd churn` becomes auto-invokable when risk/refactor analysis is relevant.

### OpenCode `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514"
}
```

No special config needed for the skills symlink — it's discovered automatically.

### OpenCode agents (optional)

Custom agents for specialized workflows via `.opencode/agents/aidd-review.md`:

```markdown
---
description: Review code for quality and spec compliance using AIDD standards
model: anthropic/claude-sonnet-4-20250514
---
You are a code reviewer. Load the AIDD review skill via the skill tool and apply it.
```

Users can `@aidd-review` to invoke manually, or the primary agent will delegate automatically when review is needed.

---

## Platform 2: GitHub Copilot — Instructions-Based Routing

GitHub Copilot (CLI + VS Code / GitHub.com) does not have MCP support or a tool auto-selection layer. What it has: context files that are read before every session. The strategy is to write routing instructions that are specific enough for Copilot to choose the right AIDD workflow from natural language.

### What AIDD already generates

`npx aidd` writes `AGENTS.md` to your project root. This is already read by Copilot. It includes the skills index and basic routing — but it's generic. The customization that makes it work is in the project-specific layer.

### Upgrade the routing instructions

In `.github/copilot-instructions.md`, add explicit AIDD routing after your project context:

```markdown
## AIDD Workflow Integration

This project uses the AIDD framework. Skills are in `ai/skills/`. Read `vision.md` before any task.

### When to use which workflow:

**Bug fixing** (bug reported, test failing, error in prod, review feedback needs code change):
→ Load and follow `ai/skills/aidd-fix/SKILL.md`

**Feature discovery** (new feature, need user journeys, unclear what to build):
→ Load `ai/skills/aidd-please/SKILL.md` and run /discover

**Task epic creation** (feature defined, needs requirements/spec before implementation):
→ Load `ai/skills/aidd-please/SKILL.md` and run /task

**Implementation** (epic or spec ready, user wants to build it):
→ Load `ai/skills/aidd-please/SKILL.md` and run /execute

**Code review** (implementation done, PR ready, quality check needed):
→ Load and follow `ai/skills/review/SKILL.md`

**PR triage** (user shares a PR URL, PR needs review or delegation):
→ Load and follow `ai/skills/aidd-pr/SKILL.md`

**Hotspot analysis** (refactoring, technical debt, where to focus):
→ Run `npx aidd churn --days 90 --top 20` and report findings

**Deep reasoning** (ambiguous problem, tradeoffs, architecture decision):
→ Load and follow `ai/skills/aidd-rtc/SKILL.md`
```

### The limitation

Copilot applies these instructions when intent is recognizable — but there is no function-calling layer. If the user's message is ambiguous, Copilot may not route to the right skill. The instructions reduce friction but do not eliminate it.

**For the sharpest results**: Be explicit in your message. "Fix the bug where X happens" will trigger `aidd-fix` routing. "Do something with this code" won't.

### Copilot CLI for unattended work

`gh copilot agent run` (cloud agent) can execute AIDD workflows unattended:

```bash
# Run AIDD fix workflow on a specific bug
gh copilot agent run \
  --task "Load ai/skills/aidd-fix/SKILL.md and fix the bug: [description]" \
  --repo [owner/repo]
```

```bash
# Bulk: run review on every changed file in a PR
gh copilot agent run \
  --task "Load ai/skills/review/SKILL.md and review all changed files in PR #42" \
  --repo [owner/repo]
```

```bash
# Scheduled churn analysis (via GitHub Actions)
gh copilot agent run \
  --task "Run npx aidd churn --days 90 --json, identify top 5 hotspots, create an issue summarizing refactor priorities" \
  --repo [owner/repo]
```

The cloud agent runs unattended, commits results, and opens PRs/issues — no session needed.

---

## Comparison

| | OpenCode | GitHub Copilot |
|--|----------|----------------|
| **Auto-selects AIDD skills** | ✅ Native `skill` tool | ⚠️ Instructions-based routing |
| **Setup effort** | 2 commands | Add routing block to copilot-instructions.md |
| **Runs AIDD churn natively** | Yes (custom tool, 10 lines) | Via instructions hint |
| **Unattended/bulk operations** | No | ✅ `gh copilot agent run` |
| **Works without modifying AIDD** | Yes | Yes |
| **Best for** | Interactive daily dev, zero-friction AIDD | Bulk/scheduled tasks, GitHub-native teams |

**Use both together**: OpenCode for interactive sessions (it auto-selects the right skill), Copilot CLI for unattended/bulk tasks (`gh copilot agent run` with explicit AIDD skill path).

---

## Quick Start

### OpenCode (2 commands)

```bash
npx aidd                               # install AIDD (creates ai/)
mkdir -p .opencode && ln -s ../ai/skills .opencode/skills
```

Done. All 35 AIDD skills are auto-invokable in OpenCode.

### Copilot

```bash
npx aidd                               # install AIDD (creates AGENTS.md)
```

Then add the routing block above to `.github/copilot-instructions.md`. The more explicit your routing instructions, the better Copilot's skill selection.
