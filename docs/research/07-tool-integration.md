# Tool Integration: AIDD as Auto-Invoked Agent Tools

> The AIDD workflow normally requires the user to type slash commands: `/discover`, `/task`, `/aidd-fix`, etc. This document covers how to wire AIDD skills as automatically-selected tools in Copilot, OpenCode, Cursor, and Claude Code — so the agent picks the right AIDD workflow on its own based on user intent.

---

## The Core Technical Reality

Before getting into platform specifics, one fact changes the integration architecture entirely:

**AIDD slash commands are not shell executables.** They are markdown instruction files the LLM reads:

```
ai/commands/aidd-fix.md
# 🐛 /aidd-fix
Load and execute the skill at `ai/skills/aidd-fix/SKILL.md`.
Constraints { Before beginning, read and respect the constraints in /aidd-please. }
```

`/discover`, `/task`, `/execute`, `/review`, `/aidd-fix`, `/aidd-pr` — all of them are a few lines of prose that redirect the agent to a `SKILL.md` file. They are prompts, not programs.

**What is a real CLI tool**: `npx aidd churn` is the only command that runs executable code (git log parsing + LoC × complexity scoring). It can be wrapped in MCP directly.

This distinction matters because: the integration approach for each editor is not "wrap the CLI in MCP" — it is "teach the agent to load the right SKILL.md automatically."

---

## Platform 1: OpenCode — Native Support, Zero Code

OpenCode (previously `sst/opencode`, now `anomalyco/opencode`) has a **built-in `skill` tool** that was designed for exactly this.

### How it works

OpenCode discovers all `SKILL.md` files from these directories:
- `.opencode/skills/<name>/SKILL.md` — project-local
- `~/.config/opencode/skills/<name>/SKILL.md` — global
- `.claude/skills/<name>/SKILL.md` — Claude-compatible
- `.agents/skills/<name>/SKILL.md` — agent-compatible

The `skill` tool builds its description from all discovered skills and their frontmatter intent descriptions. When the LLM receives a user message, it reads the tool list, sees `skill` with all available skills listed, and decides when to call `skill({ name: "aidd-fix" })` based on user intent.

AIDD's `ai/skills/index.md` already has machine-readable "when to use" descriptions for all 35 skills:
```
aidd-fix - Fix a bug or implement review feedback following the AIDD fix process.
  Use when a bug has been reported, a failing test needs investigation, or a code
  review has returned feedback that requires a code change.
```

### Setup (two commands)

```bash
# In your project root (AIDD already installed via npx aidd --cursor)
mkdir -p .opencode
ln -s ../ai/skills .opencode/skills
```

That's it. OpenCode discovers all 35 AIDD skills automatically. When you say "fix this bug", it calls `skill({ name: "aidd-fix" })` and loads the full SKILL.md workflow.

### Add churn as a custom tool (optional)

Create `.opencode/tools/aidd_churn.ts`:

```typescript
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "Run AIDD churn analysis to find high-risk files by LoC × git churn × cyclomatic complexity. Use before any refactoring or when deciding where to focus technical debt work.",
  parameters: {
    days: tool.schema.number().describe("Days of git history to analyze").default(90),
    top: tool.schema.number().describe("Number of top files to return").default(20)
  },
  async execute(args) {
    const { $ } = await import("bun")
    const result = await $`npx aidd churn --days ${args.days} --top ${args.top} --json`.text()
    return JSON.parse(result)
  }
})
```

Now `npx aidd churn` is also auto-invokable by the agent when churn analysis is relevant.

### OpenCode `opencode.json` config

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514"
}
```

No special config needed for the skills symlink — it's discovered automatically.

---

## Platform 2: Cursor — Agent-Selected Rules, No Code

Cursor has a rule type called **"agent-selected"**: a rule with a `description:` frontmatter but no `alwaysApply: true` and no `globs:`. The Cursor agent reads all rule descriptions and decides which ones to apply based on user intent.

This is the Cursor-native equivalent of MCP tool auto-selection. No MCP server needed.

### How it works

File: `.cursor/rules/aidd-fix.mdc`
```markdown
---
description: Fix a bug using the AIDD TDD process. Use when a bug is reported, a test is failing, or review feedback requires a code change.
alwaysApply: false
---

Load and follow the workflow in `ai/skills/aidd-fix/SKILL.md`.
```

When the user says "there's a bug in auth.js", Cursor reads the rule description, matches it to user intent, and auto-injects the `aidd-fix` rule into the session context. The agent then follows the AIDD fix workflow without the user typing `/aidd-fix`.

### AIDD + Cursor already has the symlink

`npx aidd --cursor` creates a `.cursor` symlink pointing to `ai/`. This means `ai/skills/` is accessible as `.cursor/skills/` — but `.cursor/rules/` is what Cursor reads for agent-selected rules. Both can coexist.

### Rule files for key AIDD skills

**`.cursor/rules/aidd-fix.mdc`**
```markdown
---
description: Fix a bug using AIDD TDD process. Use when: bug reported, test failing, review feedback requires code change, error thrown in prod.
alwaysApply: false
---
Load and follow `ai/skills/aidd-fix/SKILL.md`.
```

**`.cursor/rules/aidd-discover.mdc`**
```markdown
---
description: Run product discovery for a feature or project area. Use when: starting a new feature, user wants personas/user journeys/pain points, or unclear what to build.
alwaysApply: false
---
Load and follow `ai/skills/aidd-please/SKILL.md` with the /discover command.
```

**`.cursor/rules/aidd-task.mdc`**
```markdown
---
description: Create a task epic for a feature. Use when: feature is defined and needs to be broken into requirements, user wants to spec out what to build before implementing.
alwaysApply: false
---
Load and follow `ai/skills/aidd-please/SKILL.md` with the /task command.
```

**`.cursor/rules/aidd-execute.mdc`**
```markdown
---
description: Implement a feature or task using AIDD TDD workflow. Use when: epic or spec is ready, user says implement/build/code this.
alwaysApply: false
---
Load and follow `ai/skills/aidd-please/SKILL.md` with the /execute command.
```

**`.cursor/rules/aidd-review.mdc`**
```markdown
---
description: Review code for quality, spec compliance, and completeness using AIDD standards. Use when: implementation is done, PR is ready, or user requests code review.
alwaysApply: false
---
Load and follow `ai/skills/review/SKILL.md`.
```

**`.cursor/rules/aidd-pr.mdc`**
```markdown
---
description: Triage and manage a pull request using AIDD PR workflow. Use when: user pastes a PR URL, PR needs review/triage/delegation, or changes need summarizing.
alwaysApply: false
---
Load and follow `ai/skills/aidd-pr/SKILL.md`.
```

**`.cursor/rules/aidd-rtc.mdc`**
```markdown
---
description: Use Reflective Thought Composition for structured reasoning. Use when: problem is ambiguous, tradeoffs need weighing, spec section is unclear, or deep analysis is needed.
alwaysApply: false
---
Load and follow `ai/skills/aidd-rtc/SKILL.md`.
```

**`.cursor/rules/aidd-churn.mdc`**
```markdown
---
description: Analyze codebase hotspots before refactoring or starting work on a complex area. Use when: user wants to know what to refactor, where debt lives, or before touching legacy code.
alwaysApply: false
---
Run: `npx aidd churn --days 90 --top 20` and summarize the highest-risk files.
```

### Always-on context rule

One rule that should always apply — the project-level AIDD awareness:

**`.cursor/rules/aidd-context.mdc`**
```markdown
---
alwaysApply: true
---
This project uses the AIDD framework. Skills are in `ai/skills/`. The vision document is `vision.md`.
Available AIDD workflows (load the corresponding SKILL.md to execute):
- Bug fixing: ai/skills/aidd-fix/SKILL.md
- Feature discovery: use /discover via ai/skills/aidd-please/SKILL.md
- Task epic creation: use /task via ai/skills/aidd-please/SKILL.md
- Implementation with TDD: use /execute via ai/skills/aidd-please/SKILL.md
- Code review: ai/skills/review/SKILL.md
- PR management: ai/skills/aidd-pr/SKILL.md
- Hotspot analysis: `npx aidd churn`
```

---

## Platform 3: Claude Code — MCP Server

Claude Code supports MCP (Model Context Protocol). All registered MCP tools are automatically available to the agent — it auto-selects them from tool name + description.

### What an AIDD MCP server would expose

```
aidd_skill_list    → returns ai/skills/index.md (all 35 skills with descriptions)
aidd_skill_load    → reads ai/skills/<name>/SKILL.md and returns content
aidd_churn         → runs npx aidd churn --json and returns parsed results
aidd_run_agent     → spawns npx aidd agent --prompt <text>
```

`aidd_skill_list` and `aidd_skill_load` are context injectors — they load SKILL.md content into the agent's context, and the agent then follows the workflow instructions. `aidd_churn` and `aidd_run_agent` execute real code.

### Why the two-step pattern

`aidd_skill_load("aidd-fix")` returns the full SKILL.md content. The agent then reads it and executes the workflow. This is how OpenCode's native `skill` tool works. The MCP server is just a delivery mechanism for what is ultimately a prompt injection.

### MCP server skeleton

```javascript
// aidd-mcp-server/index.js
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js"
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js"
import { readFileSync, existsSync } from "fs"
import { join } from "path"
import { spawn } from "child_process"

const server = new McpServer({ name: "aidd", version: "1.0.0" })
const PROJECT_ROOT = process.env.CLAUDE_PROJECT_DIR || process.cwd()
const SKILLS_DIR = join(PROJECT_ROOT, "ai", "skills")

server.tool("aidd_skill_list", "List all available AIDD skills with their intent descriptions. Call this to discover which skill applies to the current task.", {}, async () => {
  const index = readFileSync(join(SKILLS_DIR, "index.md"), "utf8")
  return { content: [{ type: "text", text: index }] }
})

server.tool("aidd_skill_load", "Load a specific AIDD skill workflow. Returns the full SKILL.md content — follow it as your next instructions.",
  { name: { type: "string", description: "Skill name (e.g. aidd-fix, review, aidd-pr, aidd-rtc)" } },
  async ({ name }) => {
    const path = join(SKILLS_DIR, name, "SKILL.md")
    if (!existsSync(path)) return { content: [{ type: "text", text: `Skill '${name}' not found` }] }
    return { content: [{ type: "text", text: readFileSync(path, "utf8") }] }
  }
)

server.tool("aidd_churn", "Run AIDD churn analysis to find high-risk files (LoC × git churn × complexity). Use before refactoring or to prioritize technical debt.",
  { days: { type: "number", description: "Days of git history", default: 90 },
    top: { type: "number", description: "Top N files", default: 20 } },
  async ({ days = 90, top = 20 }) => {
    return new Promise((resolve) => {
      const proc = spawn("npx", ["aidd", "churn", "--days", String(days), "--top", String(top), "--json"], { cwd: PROJECT_ROOT })
      let out = ""
      proc.stdout.on("data", d => out += d)
      proc.on("close", () => resolve({ content: [{ type: "text", text: out }] }))
    })
  }
)

const transport = new StdioServerTransport()
await server.connect(transport)
```

### Register in Claude Code

Create `.mcp.json` in project root:

```json
{
  "mcpServers": {
    "aidd": {
      "command": "node",
      "args": ["./aidd-mcp-server/index.js"],
      "env": {}
    }
  }
}
```

Or use a published package:
```json
{
  "mcpServers": {
    "aidd": {
      "command": "npx",
      "args": ["-y", "aidd-mcp-server"]
    }
  }
}
```

Claude Code picks it up automatically. When you say "fix this bug", the agent calls `aidd_skill_load({ name: "aidd-fix" })` and follows the workflow.

### Scaffold the MCP server in-IDE

Claude Code has a plugin that scaffolds MCP servers:
```
/plugin install mcp-server-dev@claude-plugins-official
/mcp-server-dev:build-mcp-server
```

---

## Platform 4: GitHub Copilot — Instructions Only (No Auto-Selection)

GitHub Copilot does not have MCP support as of mid-2026. There is no tool registry that auto-selects based on user intent. What is available:

### What works

**`AGENTS.md`** (already generated by `npx aidd`): Copilot reads this before every session. AIDD already writes good routing hints here — when a user intent matches what the AGENTS.md describes, Copilot will suggest the corresponding workflow.

**`.github/copilot-instructions.md`**: Same principle. Add AIDD workflow hints:

```markdown
## AIDD Workflow Integration

When fixing bugs: follow the workflow in `ai/skills/aidd-fix/SKILL.md`
When creating features: read `ai/skills/aidd-please/SKILL.md` and use /task
When reviewing code: follow `ai/skills/review/SKILL.md`
When analyzing risk: run `npx aidd churn --days 90`
```

This is instructions-based, not tool-based. Copilot will follow these instructions when it determines they're relevant — but it requires the user to communicate intent clearly in natural language.

### The limitation

Copilot will not autonomously decide to run a churn analysis or load an AIDD skill unless the user's message clearly implies it. There is no function-calling / tool auto-selection layer.

### What would unlock this: Copilot Extensions

A full Copilot Extension (GitHub App + deployed server) could expose AIDD as proper tools with auto-selection. The extension would:
- Expose an `@aidd` agent in Copilot Chat
- Handle all AIDD skill routing server-side
- Return rich responses with the skill workflow content

This is significant infrastructure (GitHub App registration, deployed HTTP server, Copilot Extension API). For teams already on GitHub Enterprise or with existing App infrastructure, it's the right long-term path.

---

## Comparison: Which Platform to Prioritize

| | OpenCode | Cursor | Claude Code | GitHub Copilot |
|--|----------|--------|-------------|----------------|
| **Auto-selects AIDD skills** | ✅ Native | ✅ Via rules | ✅ Via MCP | ⚠️ Instructions only |
| **Setup effort** | Minimal (symlink) | Minimal (config files) | Moderate (MCP server) | None extra needed |
| **Requires code** | No | No | Yes (MCP server) | No |
| **Runs AIDD churn natively** | Yes (custom tool) | Via rule hint | Yes (MCP tool) | Via instructions |
| **Works without changes to AIDD** | Yes | Yes | Yes | Yes |
| **Best for** | Most elegant | Most Cursor users | Claude Code users | Teams already on Copilot |

**Recommendation for new projects**: Use OpenCode or Cursor. Both require zero code and leverage existing AIDD files as-is. Cursor rules give you the most granular control over per-skill invocation. OpenCode's skill tool is the most elegant single-line discovery.

---

## The Incomplete Orchestrator Problem

AIDD's `ai/skills/aidd-agent-orchestrator/SKILL.md` has a dispatch table that routes user intent to skills:

```
Agents {
  please: when user says "please", use this guide for general assistance
  tdd: when implementing code changes, use this guide for systematic TDD
  ...
}
```

**Issue**: This table covers only 12 of 35 available skills (AIDD GitHub issue #210, open as of June 2026). If you rely on the orchestrator for routing, 23 skills will never be auto-selected.

**Fix**: The Cursor rules approach and OpenCode's `skill` tool both bypass this problem — they build routing from the complete `ai/skills/index.md` (all 35 entries), not from the incomplete orchestrator dispatch table.

For the MCP server approach: `aidd_skill_list` reads `ai/skills/index.md` directly, also bypassing the orchestrator.

---

## Quick Start: Cursor Setup (5 Minutes)

1. Install AIDD in your project: `npx aidd --cursor`
2. Create `.cursor/rules/` if it doesn't exist
3. Create a rule file for each AIDD skill you want auto-invoked (see rule files above)
4. Create `aidd-context.mdc` with `alwaysApply: true` for always-on project awareness

Result: Cursor agent reads all rule descriptions at inference time and auto-selects the right AIDD workflow based on your message. You never type `/aidd-fix` again — you just say "there's a bug" and the agent picks the right workflow.

## Quick Start: OpenCode Setup (2 Commands)

```bash
npx aidd --cursor          # installs ai/ directory
mkdir -p .opencode
ln -s ../ai/skills .opencode/skills
```

Result: All 35 AIDD skills are available as auto-invokable tools in OpenCode.
