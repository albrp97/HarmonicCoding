# Harmonic Coding

![Harmonic Coding](./harmonic-coding-banner.svg)

Advanced framework for human-directed AI engineering. Synthesizes spec-driven development, the AIDD framework, workflow orchestration, context architecture, automation patterns, and the economics of AI-assisted production work — sourced from production use, official guidance, and real case studies.

---

## Start Here

**→ [Ultimate Guide](./docs/guide/ultimate-guide.md)** — The master operations manual. New projects, existing projects, scale. Combines all research into one actionable reference.

**→ [AIDD Guide](./docs/guide/aidd-guide.md)** — Practical guide to the AIDD framework: setup, workflow commands, vision documents, hotspot analysis, custom skills.

**→ [Advanced Playbook](./docs/guide/advanced-playbook.md)** — SDD operations manual: repo setup, spec writing, implementation loops, quality gates, automation at scale.

**→ [Developer Guide](./docs/guide/developer-guide.md)** — Copilot-first workflow selection for Aider, AutoGen, LangGraph, Agno, CrewAI, Pydantic AI, and OpenHands/SWE-agent.

**→ [Setup Guide](./docs/guide/setup-guide.md)** — Baseline repo files, optional tool installs, and recommended context wiring.

**→ [New Project Guide](./docs/guide/new-project-guide.md)** — Strict step-by-step instructions for using Harmonic Coding on a new repository from planning and setup through implementation readiness and ticket delivery.

**→ [Delivery Workflows](./docs/guide/delivery-workflows.md)** — Reusable prompt workflows for project objective discovery, setup, CI/CD, PR flow, and ticket implementation loops.

**→ [AIDD Gap Closure Plan](./docs/guide/aidd-gap-closure-plan.md)** — Ordered roadmap for adding the missing runtime, review, testing, and eval layers that would bring Harmonic Coding closer to a full AIDD-class AI coding system.

---

## Research

### Phase 2 — AIDD Framework

| Document | What it covers |
|----------|----------------|
| [AIDD Framework](./docs/research/05-aidd-framework.md) | Complete AIDD intelligence: CLI, SudoLang, RTC, all 30+ skills, churn analysis, TDD rules, evals, server framework |
| [Synthesis: AIDD + SDD](./docs/research/06-synthesis.md) | Direct comparison of both methodologies: where they overlap, where they diverge, how to combine them |

### Phase 1 — Spec-Driven Development

| Document | What it covers |
|----------|----------------|
| [Spec-Driven Development](./docs/research/01-spec-driven-development.md) | The complete SDD discipline: spec anatomy, the 50-prompt iteration process, the factory/reuse pattern, Mermaid infrastructure, consistency techniques |
| [Context Engineering](./docs/research/02-context-engineering.md) | Maximizing model output quality: persistent context files, session priming, MCP servers, model selection by task, anti-patterns |
| [Automation Patterns](./docs/research/03-automation-patterns.md) | Copilot CLI, cloud agent, bulk operations, custom agents/skills, event-driven automations, multi-agent architecture |
| [Token Economics](./docs/research/04-token-economics.md) | Current model pricing, real cost of spec-driven cycles, breakeven analysis, optimization strategies, budget controls |
| [Workshop Intelligence](./docs/research/00-transcript-intelligence.md) | Extracted intelligence from an internal AI engineering workshop: case studies, numbers, direct quotes, techniques demonstrated in production |

### Phase 3 — Tool Integration

| Document | What it covers |
|----------|----------------|
| [Tool Integration](./docs/research/07-tool-integration.md) | Wiring AIDD as auto-invoked tools in OpenCode and Copilot — no slash commands needed |

### Phase 4 — Workflow Orchestration Tools

| Document | What it covers |
|----------|----------------|
| [Aider](./docs/research/08-aider.md) | Terminal pair-programming with git diffs and repo-aware edits |
| [AutoGen](./docs/research/09-autogen.md) | Multi-agent orchestration, MCP workbenches, and AutoGen Studio |
| [CrewAI](./docs/research/10-crewai.md) | Role-based crews, flows, and coding-agent skills |
| [LangGraph](./docs/research/11-langgraph.md) | Stateful step graphs, durable execution, human-in-the-loop control |
| [Pydantic AI](./docs/research/12-pydantic-ai.md) | Typed agent workflows, structured outputs, and approval gates |
| [Agno](./docs/research/13-agno.md) | Agent platform/runtime, scheduling, RBAC, and control plane |
| [OpenHands + SWE-agent](./docs/research/14-openhands-swe-agent.md) | Autonomous issue-to-fix execution and self-hosted agent control centers |

---

## Core Ideas

**The spec is the asset. The code is a build artifact.**

A specification written to sufficient quality can:
- Generate a working implementation
- Be adapted for different stacks by prompting (not by editing code)
- Serve as a factory template for similar systems in different countries, contexts, or languages
- Regenerate a codebase if it needs to be scrapped

**LLM failures are context failures.**

The model generates code. You design and maintain the system that determines what the model knows at inference time. Engineering skill shifts from code authorship to specification quality.

**The jackhammer problem.**

Having Copilot and using it like search or autocomplete is like operating an electric jackhammer manually. The tool requires learning. The gap between a Copilot user and a Copilot practitioner is context engineering.

---

## Contributors

- [@albrp97](https://github.com/albrp97)
