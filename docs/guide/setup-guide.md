# Harmonic Coding Setup Guide

> Baseline setup for a Copilot-centered Harmonic Coding workflow.

This guide is for the repo-level setup that makes the research and developer workflow usable in practice.

If you want the **full strict order** for applying Harmonic Coding to a new project, read `docs/guide/new-project-guide.md` first, then use this guide for the setup-specific parts of that process.

## Minimum Harmonic Coding setup for a new repo

If you are setting up a fresh repository to use Harmonic Coding, the minimum recommended baseline is:

- `vision.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/`
- `.github/prompts/`
- `docs/planning/`
- `docs/specs/`
- `harmonic-custom/`

If the repository does not have these, add them before expecting consistent AI-assisted delivery behavior.

## Baseline files

For a real code repository using this workflow, keep these files in place:

- `README.md` as the entry point
- `AGENTS.md` or `.github/copilot-instructions.md` for persistent context
- `vision.md` for the project purpose and constraints
- `docs/planning/repo-map.md` for the repository path map
- `docs/planning/` for epics, phases, backlog, tickets, and reviews
- `docs/research/` for tool research
- `docs/guide/` for practical workflow docs
- `harmonic-custom/` for local overrides, workflow toggles, and skill entrypoints
- `ai-evals/` when the repo uses workflow contract evals

## Recommended environment

- Git
- Python 3.10+ for the Python workflow tools
- Node.js/npm for tools that ship CLI or agent canvas integrations
- API keys for the model provider you actually use

## Tool setup ladder

### Aider

```bash
python -m pip install aider-install
aider-install
```

### LangGraph

```bash
pip install -U langgraph
```

### AutoGen

```bash
pip install -U "autogen-agentchat" "autogen-ext[openai]"
pip install -U "autogenstudio"
```

### CrewAI

Use the official CrewAI docs and skills package for the agent you run.

```bash
npx skills add crewaiinc/skills
```

For Claude Code, CrewAI also documents a plugin-based install flow in the README.

### Pydantic AI

```bash
pip install -U pydantic-ai
```

### Agno

```bash
uv pip install -U agno openai
uv pip install -U 'agno[os]'
```

### OpenHands

```bash
npm install -g @openhands/agent-canvas
agent-canvas
```

## Copilot setup

- Keep the docs repo as the context source.
- Put the project intent in `vision.md`.
- Keep instructions short and stable.
- Use the workflow docs to choose the right tool before you start editing.
- Add a review/repair loop to `AGENTS.md` or `.github/copilot-instructions.md`: after each phase, compare the current state against the spec or benchmark, patch blocking gaps, and rerun checks before stopping.

## How to use the local runtime

Use the runtime in this order:

1. `AGENTS.md` for the shared rules
2. `.github/copilot-instructions.md` for Copilot-specific baseline context
3. `.github/instructions/*.instructions.md` for path-scoped detail
4. `harmonic-custom/AGENTS.md` for local overrides
5. `harmonic-custom/skills/` for reusable workflow entrypoints
6. `.github/prompts/` as the source workflow bodies behind those entrypoints

## Suggested order

1. Read the Harmonic Coding README.
2. Read the relevant research doc.
3. Read the developer guide.
4. Run the repository map and pre-implementation workflows.
5. Install only the workflow tool you need.
6. Start with the smallest possible task.
7. Review the result against the instructions, then repair and re-review until it matches.
