# Concept Deep Dive

## Software 1.0, 2.0, 3.0

The workshop uses the common AI-era software model:

- **Software 1.0**: humans write explicit code.
- **Software 2.0**: models are trained to perform a task.
- **Software 3.0**: prompts and examples are used to steer models into producing useful outputs.

The practical implication is that natural language becomes part of the engineering interface.

## Prompt-driven development

Prompts are not just ad hoc instructions. In the workshop, they behave like:
- specs
- reusable templates
- automation inputs
- reviewable artifacts

That makes prompt writing closer to engineering than casual chatting.

## Spec-driven development

The transcript strongly suggests a spec-first workflow:
1. define the task clearly
2. capture constraints and acceptance criteria
3. ask the model to generate or transform code
4. review and refine

This reduces ambiguity and makes outputs more reusable.

## Copilot in VS Code

The transcript presents VS Code as the main practical environment:
- inline help
- chat-style guidance
- code explanation
- command assistance
- visualization of changes

The point is to keep the human in control while removing friction.

## Copilot CLI

The CLI is treated as a way to move from interactive prompting to repeatable automation.

Why it matters:
- prompts can be prewritten
- tasks can be standardized
- the same flow can be reused across projects
- it helps when you want a command-line or agent-like workflow

## Factory and reusable assets

The transcript talks about making generation scalable and reusable. In practice this means:
- create prompt templates
- create small reusable code generators
- package common workflows
- keep output consistent

That is the bridge between one-off prompting and an engineering system.

## What this means for the repo

Harmonic Coding should treat:
- specs as source material
- prompts as versioned assets
- examples as reusable patterns
- automation as part of the developer experience

