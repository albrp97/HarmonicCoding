# Harmonic Coding Developer Guide

## Goal

Use AI coding tools to produce better software faster without losing design control.

## Core workflow

1. **Write the spec first**
   - define the task
   - state constraints
   - define what success looks like

2. **Turn the spec into prompts**
   - keep prompts reusable
   - separate instructions from data
   - version the prompt when it matters

3. **Use the right Copilot surface**
   - **VS Code** for interactive coding
   - **Copilot Chat** for explanation and refinement
   - **Copilot CLI** for repeatable terminal workflows

4. **Ask for small, reviewable changes**
   - generate one unit at a time
   - keep outputs diffable
   - prefer incremental changes over huge rewrites

5. **Review like an engineer**
   - check correctness
   - check architecture fit
   - check naming and consistency
   - check tests and edge cases

6. **Promote reusable assets**
   - prompt templates
   - task checklists
   - example specs
   - reusable generators

## How to use this repo

- Use the research docs to understand the methodology.
- Use the developer guide as the practical playbook.
- Store prompts and examples here when they are reusable.
- Treat the repo as a system for human-directed AI coding, not just notes.

## When to use which tool

| Tool | Best for |
|---|---|
| VS Code + Copilot | interactive implementation |
| Copilot Chat | explanation, refactor suggestions, debugging |
| Copilot CLI | repeatable scripted tasks |
| Spec docs | defining intent and constraints |
| Prompt templates | turning intent into reusable actions |

## Copilot CLI operating pattern

Use Copilot CLI when the work needs to be repeatable or automated:

1. Trust the directory only if you actually want Copilot to read and edit those files.
2. Start with a spec or task prompt.
3. Use `@path/to/file` when a prompt needs file context.
4. Use `/plan` before coding when the task is not yet fully shaped.
5. Use `/cwd` or `/add-dir` when the work lives outside the current folder.
6. Use `/compact` when the session gets too long.
7. Use `/mcp add` only when you need extra external integrations.

CLI features worth using:
- `!` for direct shell commands
- `/usage` and `/context` to watch token usage
- `/resume` to continue a previous session
- `/sandbox enable` or `--cloud` when you want a constrained environment

## Operating rules

- Human intent comes first.
- The model should work from clear context.
- Reuse what works.
- Keep every useful prompt as an artifact.
- Prefer small, inspectable iterations.
- Treat prompts and specs as versioned engineering assets.
