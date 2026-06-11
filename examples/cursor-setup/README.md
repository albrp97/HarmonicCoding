# Cursor Setup — AIDD Auto-Invocation

Drop these files into your project's `.cursor/rules/` directory to enable automatic AIDD skill selection in Cursor.

## What this does

Cursor has an "agent-selected" rule type: rules with a `description:` frontmatter are read by the Cursor agent at inference time, and the agent decides which rules apply based on user intent — without the user typing any slash commands.

These files map AIDD skills to natural-language intents:

| Rule file | Triggers when |
|-----------|---------------|
| `aidd-context.mdc` | Always (gives agent AIDD awareness) |
| `aidd-fix.mdc` | Bug reported, test failing, review feedback |
| `aidd-discover.mdc` | Starting a feature, need user journeys/personas |
| `aidd-task.mdc` | Feature defined, need epic/requirements |
| `aidd-execute.mdc` | Epic ready, user says build/implement |
| `aidd-review.mdc` | Implementation done, code review needed |
| `aidd-pr.mdc` | PR URL shared, PR triage/review |
| `aidd-rtc.mdc` | Ambiguous problem, tradeoff analysis needed |
| `aidd-churn.mdc` | Refactor planning, technical debt analysis |
| `aidd-parallel.mdc` | Large feature with independent sub-tasks |

## Setup

```bash
# 1. Install AIDD in your project (creates ai/ directory)
npx aidd --cursor

# 2. Copy these rule files to .cursor/rules/
cp -r path/to/HarmonicCoding/examples/cursor-setup/rules/* .cursor/rules/
```

## How to use after setup

Just describe what you want in natural language:

| You say | Cursor auto-invokes |
|---------|---------------------|
| "There's a bug in auth.js" | `aidd-fix` workflow |
| "I want to add a search feature" | `aidd-discover` → `aidd-task` |
| "Implement the epic we just wrote" | `aidd-execute` workflow |
| "Review this code" | `aidd-review` workflow |
| "Analyze PR #142" | `aidd-pr` workflow |
| "Where should I focus refactoring?" | `aidd-churn` → hotspot report |

## Prerequisites

- AIDD installed: `npx aidd --cursor` (creates `ai/skills/`)
- Cursor with agent mode enabled
- `vision.md` created at project root (see [ultimate-guide.md](../../docs/guide/ultimate-guide.md))
