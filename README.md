# Harmonic Coding

![Harmonic Coding](./harmonic-coding-banner.svg)

Advanced framework for human-directed AI engineering. Spec-driven development, context architecture, automation patterns, and the economics of AI-assisted production work — sourced from production use, official guidance, and real case studies.

---

## Start Here

**→ [Advanced Playbook](./docs/guide/advanced-playbook.md)** — The operations manual. Phase-by-phase: repo setup, spec writing, implementation loops, quality gates, automation at scale.

---

## Research

| Document | What it covers |
|----------|----------------|
| [Transcript Intelligence](./docs/research/00-transcript-intelligence.md) | Extracted intelligence from an internal AI engineering workshop: case studies, numbers, direct quotes, techniques that were demonstrated in production |
| [Spec-Driven Development](./docs/research/01-spec-driven-development.md) | The complete SDD discipline: spec anatomy, the 50-prompt iteration process, the factory/reuse pattern, Mermaid infrastructure, consistency techniques |
| [Context Engineering](./docs/research/02-context-engineering.md) | Maximizing model output quality: persistent context files, session priming, MCP servers, model selection by task, anti-patterns |
| [Automation Patterns](./docs/research/03-automation-patterns.md) | Copilot CLI, cloud agent, bulk operations, custom agents/skills, event-driven automations, multi-agent architecture |
| [Token Economics](./docs/research/04-token-economics.md) | Current model pricing, real cost of spec-driven cycles, breakeven analysis, optimization strategies, budget controls |

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

## Source Material

- [Workshop transcript](./docs/source/dsh-offsite-office-day.vtt) — ~3hr internal AI engineering session with production Belgium case studies

---

## Contributors

- [@albrp97](https://github.com/albrp97)
