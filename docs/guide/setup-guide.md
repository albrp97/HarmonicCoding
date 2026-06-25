# Harmonic Coding Setup Guide

> Baseline setup for a Copilot-centered Harmonic Coding workflow.

This guide is for the repo-level setup that makes the research and developer workflow usable in practice.

## Baseline files

For a real code repository using this workflow, keep these files in place:

- `README.md` as the entry point
- `AGENTS.md` or `.github/copilot-instructions.md` for persistent context
- `vision.md` for the project purpose and constraints
- `docs/research/` for tool research
- `docs/guide/` for practical workflow docs

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

## Suggested order

1. Read the Harmonic Coding README.
2. Read the relevant research doc.
3. Read the developer guide.
4. Install only the workflow tool you need.
5. Start with the smallest possible task.
