## Purpose

Harmonic Coding exists to turn AI-assisted software engineering into a repeatable delivery system. It packages the research, workflows, and operating guidance needed to shape repositories, plan work, run implementation loops, and keep AI coding disciplined instead of ad hoc.

## Primary Users

- engineers who want a strict workflow for using AI in real software delivery
- repo owners who need reusable planning, setup, review, and implementation procedures
- teams comparing or combining spec-driven and AIDD-style operating models

## Goals

1. Provide a durable workflow system that starts before coding and continues through PR repair.
2. Preserve strong upfront planning instead of letting AI invent scope during implementation.
3. Make the workflows reusable across repositories through stable instructions, prompts, and guides.

## Non-Goals

- replace project-specific product discovery with generic assumptions
- force one orchestration tool or model provider on every repository
- optimize for fast first-pass output at the cost of correctness or maintainability

## Constraints

- the framework should stay tool-agnostic enough to work with Copilot-first workflows
- the workflow stack should stay lean and avoid overlapping layers without clear value
- repository guidance must remain documentation-backed and reviewable

## Success Criteria

- a new repository can be shaped with a clear ordered workflow before implementation begins
- implementation follows documented ticket, testing, review, and PR loops
- repo-level instructions and workflow assets are discoverable without reconstructing the system from scattered docs
