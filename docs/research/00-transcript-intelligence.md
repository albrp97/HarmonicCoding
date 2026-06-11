# Transcript Intelligence: DSH Offsite — AI Engineering Workshop

> Distilled from a ~3-hour internal workshop. Speakers: Matej (host), Marek (business), Charles (Belgium — primary technical lead), Pavol/David/Filip (Model Factory demo). All techniques and numbers are directly from the session.

---

## The Paradigm Shift: What Actually Changed

### Software 1.0 → 2.0 → 3.0 (Karpathy's model)
- **1.0**: Engineers write deterministic code to execute tasks
- **2.0**: Neural networks trained to do tasks (ML/model training era)
- **3.0**: Prompt the model to accomplish the task directly

The consequence: everyone is now a software engineer. Natural language → software is real today.

### The Jackhammer Problem
> *"A guy with an electric jackhammer demolishing a wall manually — not using the electric function. Having an amazing tool and doing it 100% the wrong way."*

Having GitHub Copilot and using it like a search engine or autocomplete = the jackhammer problem. The tool requires learning, individually and as a team.

### The Typewriter Analogy
> *"Our grandparents had a typewriter sitting next to them, not using it themselves. Today CEOs use a typewriter — a computer. I wonder if this session should not also be useful for CEOs."*

AI coding tools will follow the same trajectory: an engineer-only capability today, a general professional tool within a decade.

---

## Spec-Driven Development: What Charles' Team Actually Did

### The Core Mental Model
**The spec sheet is the asset. Not the code.**

The code is disposable. The spec is permanent. If you can regenerate the code from the spec, the code has no intrinsic value. The spec is the artifact you maintain, version, and reuse.

### How Symphony Changed the Frame
OpenAI released **Symphony** — a ~2000-line spec sheet, not an executable. To get the tool:
- You put the spec into your preferred coding agent in your language of choice
- The agent builds the tool for you
- OpenAI designed the spec to produce consistent results across agents

> *"They believe that today they're at the point where people can just get and put this prompt in their coding agent and they will get the tool."*

**What OpenAI did next**: Charles took the Symphony spec (originally integrated with Luminary/GitLab) and told the agent: *"I have a great specification but it's linked with Luminary. Adapt whatever needs to be adapted to rewrite it for Azure DevOps."* The agent rewrote the spec. The adapted tool worked.

### The Belgium Client Check API: Proof of Concept

**What they built**: An overarching API for client screening against:
- Moody's international blacklist
- ERSR (Belgian internal blacklist)  
- ER Desire (Belgian internal blacklist)
- Insurance blacklist (NN Belgium specific)
- With reporting capabilities

**Process:**
1. All external documentation → Markdown (Moody's docs, regulatory docs, API contracts)
2. High-level planning → Markdown
3. Detailed analysis (few hundred lines) → Markdown
4. **~50 prompts iterating the spec sheet** to build it to completion
5. Implementation command: `implement this` → agent generates 12-step plan → executes
6. Agent says "I'm done but didn't complete" → re-prompt: `continue, complete the work`
7. Repeat ~10 times until done
8. Review test cases (which were specified in the spec), check non-functionals

**Numbers:**
- Spec sheet: ~5,000 lines
- Generated code: ~15,000 lines
- Token cost: ~500% usage cap (not crazy by subscription standards)
- 1M in + 1M out tokens ≈ 4 EUR at the time (Opus 4.7)
- Engineer hours vs cost: "Way, way, way cheaper than paying for a person"

**What they bold-decided**: Existing v1 client check API in production for 2 years — spaghetti, no integrated tests. They scrapped it and started over. You only take that decision if regeneration is free.

> *"Something you would not do if you had to write every line manually."*

### The Leaked Credential Scanner: The Other End of the Spectrum

A security tool scanning all accessible repos for leaked credentials. Built with:
- ~7 lines of prompt (not a 5000-line spec)
- Opus 4.8 on release day
- "It was a funny test to see how good it was"

**What this proves**: You don't always need a massive spec. Short spec = more freedom for the agent to choose. The range is:
- **7-line prompt** → quick tool, agent has freedom, good for self-contained utilities
- **5000-line spec** → production API, no ambiguity, consistent re-runs, reusable as asset

### The Reuse Pattern (Belgium Address API)

Client check spec was for Belgium. The Netherlands needs the same but uses FRIS instead of ERSR.

Prompt: *"This looks great. It's using ERSR. I want it to use FRIS. Generate another spec sheet based on this one but using FRIS."*

Result: New country-specific spec, generated in one prompt. **This is the factory pattern.**

> *"This is basically spec-driven development — spending a lot of time writing a spec sheet. And then in a world where you make reusable assets, the value becomes even bigger."*

---

## Copilot CLI: The Automation Layer

### What It Actually Is
`copilot -p "..." ` is what's happening behind the button in their SQL query tool. The CLI executes Copilot prompts programmatically.

### The SQL Query Tool (Belgium)
Problem: Colleagues receiving database queries. Schema is complex. They don't want to write SQL.

Solution: A UI with a source selector + text input. Behind a button: a Copilot CLI call that:
1. Reads the repo (the schema is in the codebase)
2. Takes the natural language query
3. Writes the SQL query
4. Returns it to the UI

Engineers pre-wrote the prompt. Non-engineers use natural language. **The prompt is hidden infrastructure.**

### The 100-Repo Documentation Pattern
You want to document 100 repositories. With CLI:
1. Retrieve all repos via CLI
2. Select target repos
3. Click button
4. CLI iterates: checkout → prompt → commit → PR for each

> *"Automation of AI can be easily done through Copilot CLI."*

### The Document Converter Tool
Belgium built a tool that converts Word/Excel/PowerPoint → Markdown. The tool itself was built spec-driven. It enables teams to feed legacy documentation into the AI pipeline.

---

## Context Engineering: What They Recommended

### Markdown-First Infrastructure
> *"Markdown files — it's pure text. Text is something AI can easily ingest. Word documents, Excel files, or zipped XML — slightly more difficult."*

Belgium mandate: all documentation in Markdown. Including:
- External regulatory docs (Moody's, ERSR)
- Planning (Mermaid Gantt charts)
- Process flows (Mermaid state diagrams)
- Specs, analyses, coding standards

### Mermaid Diagrams for Everything Structural
State diagrams, Gantt charts, flow diagrams — all in Mermaid because:
1. AI-generated (you just prompt: "create a Mermaid diagram of DevOps statuses")
2. AI-readable (feeds cleanly back into agent context)
3. Natively rendered in Azure DevOps, VS Code, GitHub
4. **Prompt-updatable**: "The whole project is delayed 2 weeks. Update the planning." → one prompt changes all dates

> *"I don't need to click 100 times in a PowerPoint to move all the blocks."*

### Coding Standards as Spec Header
Belgium's .NET coding standards → Markdown file → added to every spec sheet header. The spec inherits the standards. The agent respects them.

> *"I'm pretty convinced it will respect everything written here."*

This is the reusable asset model at the micro level: a header spec, a menu spec, a security spec — composable building blocks.

### GitHub Copilot Context Features Mentioned
- **Agents and files**: enriching context for complex repos
- **Custom instructions**: skills, coding standards, tone
- **Agent tool use**: running CLI commands, reading files from within the editor
- **Reasoning models**: added to Copilot (changed how powerful it became mid-2024)
- **Expanded context windows**: another inflection point mid-2024
- **Automated PR review**: Copilot can review generated code, reducing human bottleneck

---

## The Human Bottleneck Problem

> *"You will have LLM generating a whole bunch of code, but then you end up being the bottleneck — you're not able to get all of that reviewed."*

The chain breaks at human review if:
- Volume of AI-generated code outpaces review capacity
- Team still uses manual PR review processes
- No automated validation pipeline exists

Solutions mentioned:
- Automated PR review via Copilot
- Test cases specified in spec (so tests validate without reading all code)
- Non-functional requirements in spec (security, performance — so agent bakes them in)

---

## The Spec Sheet Lifecycle: Maintenance and Quality

### Bug Flow
When a bug is found: **go back to the spec sheet first**.

> *"If you see a bug in all of it, you should go back to your spec sheet and say, avoid the bug that is causing this embedded bug. Because then if you re-execute the spec sheet, you won't have that issue."*

Code fix without spec fix = tech debt in the spec. Next regeneration will reproduce the bug.

### Consistency Across Runs
Charles' assertion:
- 100% identical output: no
- 95% of the job consistent: yes
- OpenAI likely ran Symphony through 10 different agents and iterated until results converged

### The Spec Sprawl Risk
> *"If you are still, maybe some of the bigger ones are nice, but 50,000 points and then there is no single person who really knows what's inside."*

Mitigation: keep specs modular. Header spec, menu spec, component spec — compose at build time. 5000 lines is manageable. 50,000 is not.

### Spec Sheet ≠ Always Big
- **Very complex production API**: 5000-line spec
- **Quick internal tool**: 7-line prompt
- **Standard feature**: component spec + shared header spec

### Standards Problem
There are no NN-wide standards for what constitutes a good spec sheet. Belgium used:
- Their own .NET coding standards file
- GitHub Copilot community prompt library (hundreds of language-specific security/quality prompts)
- Their own reusable header component spec

> *"From NN the answer is no [no spec standards]. But from GitHub Copilot, you will see hundreds of prompts in every language — standard security practices you can add on top."*

---

## Models and Tools State (Workshop Date, ~April/May 2025)

### Models Removed from GitHub Copilot
- Claude Opus (removed, cost 26x in 6 months)
- GPT-4 / GPT-4o removed
- Automatic/Codex remained as preferred

### Models Used in Belgium Case Studies
- **Claude Opus 4.7** for the client check API (primary implementation)
- **Claude Opus 4.8** for the leaked credential scanner (test on release)
- Cost at Opus 4.7 pricing: 1M in + 1M out ≈ 4 EUR

### GitHub Copilot Access
> *"Microsoft has closed the doors. You cannot get GitHub Copilot anymore since more than a month."* (still closed at workshop time)

---

## OpenSpec: The Structured Middle Ground

For teams not ready to write raw specs: OpenSpec is a conversational tool that:
1. Asks you questions about your application
2. Builds up user stories in Markdown format
3. Implements them through an agent

Mentioned as useful "3-6 months ago" when models were less capable at multi-step reasoning. Today's models (Sonnet 4+, Opus 4.8) can handle much larger single prompts.

> *"Today, the bigger ones like [Sonnet/Opus] are so powerful and can do much more at once."*

---

## Team Dynamics and Adoption

### Why Individual Adoption Is Not Enough
> *"If we don't do it as a whole team, you are going to have an individual who is using it but the rest of the team will be basically stuck."*

The productivity gap between an AI-using engineer and one who doesn't will widen to the point of dysfunction.

### Recommended Adoption Path (Per Workshop)
1. Start: Prerequisites (VS Code, Copilot, basic usage)
2. Learn: Spec-driven development methodology
3. Practice: Build something in your backlog with teams of 2-3
4. Observe: Model Factory demo — factory/reuse patterns at scale
5. Scale: Team-level standards, shared spec assets, CI integration

---

## Key Direct Quotes

| Quote | Speaker | Context |
|-------|---------|---------|
| *"The spec sheet is so good that we know whoever executes it — whether it's the latest version or older version of GPT — will get the same result."* | Charles | On OpenAI's Symphony quality bar |
| *"We threw everything away or improved it. So they begin with a spec sheet. Anyone can use it."* | Charles | Client check development process |
| *"Something you would not do if you had to write every line manually."* | Charles | Decision to scrap v1 and rebuild |
| *"If you have any questions about this project, you can just ask AI."* | Charles | On code ownership in spec-driven world |
| *"The role that we are all having will evolve. It is purely right and good."* | Charles | On engineering role transformation |
| *"It won't happen overnight. There is a whole route to it."* | Charles | On pace of transition |
