# Context Engineering: Maximizing Model Output Quality

> The model is only as good as what it knows at inference time. Context engineering is the discipline of maximizing what the model knows — about your codebase, your standards, your intent, your constraints — at the moment it generates code.

---

## Why Context Engineering Is Underused

Most engineers use Copilot in one of two ways:
1. Tab-complete acceptance in the editor
2. Chat with vague prompts ("write a function to do X")

Neither leverages the full context window or the ecosystem of context-enrichment tools available. The difference between a Copilot user and a Copilot practitioner is context engineering.

---

## Layer 1: Persistent Context Files

### `.github/copilot-instructions.md`

Automatically loaded into every Copilot conversation in VS Code. This is your ground truth about the project.

**Anatomy of a high-value instructions file:**

```markdown
# Project: [Name]

## Tech Stack
- Runtime: Python 3.11 (use f-strings, walrus operator, match statements)
- Framework: FastAPI 0.110+
- ORM: SQLAlchemy 2.0 with async support
- Testing: pytest + pytest-asyncio + httpx AsyncClient
- DB: PostgreSQL 15

## Project Structure
src/
  api/          # FastAPI routers
  models/       # SQLAlchemy models
  services/     # Business logic (no DB calls here)
  repositories/ # DB access layer only
  schemas/      # Pydantic request/response models
tests/
  unit/         # Isolated, no DB
  integration/  # Uses test DB
  e2e/          # Uses test client against full app

## Engineering Standards
- All functions must have type hints
- All public functions must have docstrings (Google style)
- No bare `except:` — catch specific exceptions
- All datetimes are UTC; use `datetime.now(UTC)` not `datetime.utcnow()`
- Logging: use `structlog`, never `print()`
- Configuration: always from `src/config.py`, never from `os.environ` directly
- Errors: use custom exception classes from `src/exceptions.py`

## Anti-Patterns (Do Not Generate)
- ORM queries outside repositories/
- Business logic in routers
- Hardcoded strings that belong in config
- Synchronous DB calls in async context
- Tests that touch the real database (use fixtures)

## When Adding a New Endpoint
1. Pydantic schema in schemas/
2. Repository method in repositories/
3. Service method in services/
4. Router in api/
5. Unit test for service, integration test for repository, e2e test for endpoint
```

**What this file eliminates:** Every conversation about standards. The model already knows.

### `AGENTS.md` / `CLAUDE.md`

For agentic sessions (Claude Code, Copilot agent mode, Cursor). Higher-level orchestration instructions:

```markdown
# Agent Instructions

## Before Starting Any Task
1. Read the relevant spec file in docs/specs/
2. Check what tests already exist for the area you're working on
3. Look at existing similar implementations before writing new ones

## When You Encounter Ambiguity
- Do not assume. Stop and list the ambiguous requirements.
- Propose two options with trade-offs. Ask which to proceed with.

## Implementation Order (Always)
1. Data models and schemas
2. Repository layer (DB access)
3. Service layer (business logic)
4. API layer (routing)
5. Tests for each layer

## What You Must Not Do
- Modify shared infrastructure (auth, logging, config) without explicit instruction
- Delete existing tests
- Change database schema without creating a migration
- Commit to main branch directly

## Definition of Done
A task is complete when:
- All specified test cases pass
- No new linting errors
- The spec file is updated if behavior changed
```

### `docs/specs/shared/` — Reusable Spec Components

Keep these as small, focused Markdown files. Reference them in project specs:

```markdown
<!-- In project spec -->
## Standards and Constraints

This project MUST comply with all requirements in:
- `docs/specs/shared/security-nonfunctionals.md`
- `docs/specs/shared/dotnet-coding-standards.md`  
- `docs/specs/shared/api-design-contract.md`
```

The agent reads all referenced files. You never repeat standards across project specs.

---

## Layer 2: Session Context Engineering

### The Session Primer

At the start of a complex agent session, prime the model with current state:

```markdown
## Session Context — [Date]

**Project**: Client Check API  
**Spec**: docs/specs/client-check/spec.md (READ THIS FIRST)  
**Current implementation status**: 
- ✅ Data models and schemas (src/models/, src/schemas/)  
- ✅ Repository layer (src/repositories/)  
- 🔄 Service layer — 60% complete (src/services/client_service.py exists, missing: blacklist_service.py, report_service.py)  
- ❌ API layer (not started)  
- ❌ Tests (not started)

**This session**: Implement blacklist_service.py and report_service.py per spec sections 4.2 and 4.3

**Decisions already made**:
- Blacklist lookup is synchronous (not async) — external API doesn't support async
- Error on blacklist timeout: raise `BlacklistUnavailableError`, caller handles retry
```

This prevents the agent from re-examining already-decided areas and re-implementing what's done.

### Explicit File References in Prompts

Don't say "look at the existing services." Say:

```
Implement blacklist_service.py.
Reference: 
- The spec at docs/specs/client-check/spec.md sections 4.2-4.3
- The existing client_service.py for pattern reference
- The repository interface at src/repositories/blacklist_repository.py
Follow the exact same structure as client_service.py.
```

Explicit beats implicit. Always.

### Context Window Management

Large codebases + large specs can exhaust context windows. Strategies:

**Chunked implementation**: Implement one module at a time with full context for that module only. Do not try to implement the entire system in one session.

**State handoff**: At the end of a session, ask the agent to produce a state summary:
```
Summarize what was implemented this session, what's remaining per the spec,
and any decisions made. Output in the session context format above.
```

Paste this as the primer in the next session.

**Context pruning**: In long sessions, explicitly remove resolved context:
```
We've completed the models and repositories. For this message forward,
focus only on the service layer. You can reference models by name without
re-reading their implementation.
```

---

## Layer 3: Model Selection by Task

Not all tasks need the most capable model. Using the right model reduces cost and often improves speed without sacrificing quality.

### Decision Matrix

| Task | Recommended Model | Why |
|------|------------------|-----|
| Spec sheet iteration | Claude Sonnet or Opus | Requires careful reasoning and long context |
| Boilerplate implementation | Fast model (Codex, Haiku) | Deterministic, pattern-matching |
| Complex algorithm from spec | Claude Opus / GPT-5 | Reasoning + correctness matters |
| Test generation | Fast model | High pattern repetition, low reasoning |
| Code review | Sonnet | Good enough, much cheaper than Opus |
| Debugging obscure issues | Opus | Complex causal reasoning |
| Documentation generation | Any fast model | Extractive, not creative |
| Security audit | Sonnet+ | Reasoning about edge cases matters |
| SQL query generation | Sonnet | Schema awareness + SQL reasoning |
| Mermaid diagram generation | Any model | Highly structured output |

### The "Auto" Setting Trap

Copilot's "auto" model selection is a cost-optimization tool, not a quality-optimization tool. It will route simple completions to fast/cheap models and complex requests to capable ones — but its heuristic for "complex" may not match yours.

For spec-driven implementation sessions: explicitly select the model. Use Sonnet or above. The spec is the most important prompt you'll ever write for a project — don't route it to the cheapest available model.

---

## Layer 4: MCP Servers

Model Context Protocol servers give the agent new capabilities beyond its training. These are the highest-leverage additions to a spec-driven workflow.

### GitHub MCP Server
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "..." }
    }
  }
}
```

What it enables:
- Agent creates PRs directly
- Agent reads issue descriptions and comments
- Agent creates/updates branch protection rules
- Agent queries PR review status

Workflow with GitHub MCP:
```
"Read the requirements from GitHub issue #47.
Implement them per our spec and coding standards.
Create a PR with a descriptive title and link it to the issue."
```

Zero manual steps between issue and PR.

### Database MCP Server
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "POSTGRES_CONNECTION_STRING": "..." }
    }
  }
}
```

What it enables:
- Agent reads actual schema (not your description of the schema)
- Agent generates queries against the real table structures
- Agent identifies schema changes needed for new features
- Agent validates that generated queries would work against the real DB

Eliminates the entire class of "model invented a column that doesn't exist" errors.

### File System MCP (for large repos)
For repos too large to load into context: the agent can navigate the file system on-demand rather than having everything loaded upfront. Useful for:
- Legacy codebases where only a subset is relevant
- Monorepos where a service boundary is clear
- Documentation search across many files

### Fetch/HTTP MCP
```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

Agent can fetch API documentation directly from URLs. Instead of pasting 200 pages of API docs into the spec — paste the URL. Agent fetches and reads.

---

## Layer 5: Repository Archaeology

Before writing any spec for modification of an existing codebase, the agent needs to understand the existing system. Do this deliberately:

```
Before implementing, analyze the existing codebase.
1. What is the current architecture? Describe the layers and their responsibilities.
2. What patterns are used for [the area I'm modifying]? Show examples.
3. What tests exist for this area? Are they unit, integration, or E2E?
4. What external dependencies does this area have?
5. What would break if I change [the component]?

Output a summary. I will confirm before you implement.
```

This one prompt can prevent hours of integration debugging.

---

## Anti-Patterns in Context Engineering

### The "You Know What I Mean" Anti-Pattern
Assuming the model knows your conventions because you asked it something similar last week. It doesn't. It has no memory between sessions. The context file is your institutional memory.

### The Giant Prompt Anti-Pattern
Cramming everything into one message hoping the model sorts it out. Context should be layered and structured — instructions file for always-on context, session primer for current state, explicit prompt for the task.

### The Follow-Up Ambiguity Anti-Pattern
Letting the model make assumptions mid-session rather than clarifying. If the model says "I assumed X" and proceeds: stop, validate X, correct if wrong. Assumptions compound.

### The Context Drift Anti-Pattern
Long sessions where the model gradually loses track of earlier constraints. Solution: at decision points, restate critical constraints explicitly.

```
"Reminder: we are NOT using async in the blacklist service 
(as decided earlier). Continue implementing blacklist_service.py."
```

### The Stale Instructions Anti-Pattern
`.github/copilot-instructions.md` not updated when the stack changes. The model follows the instructions file, not the actual code. If the file says FastAPI but you migrated to Django, you'll get FastAPI-style code in a Django project.

---

## Practical Setup Checklist

### New Project
- [ ] `.github/copilot-instructions.md` with stack, standards, anti-patterns
- [ ] `AGENTS.md` with agentic session rules
- [ ] `docs/specs/shared/` with reusable components (security, coding standards, API contract)
- [ ] First spec file created from bootstrap prompt
- [ ] MCP servers configured: GitHub + database at minimum

### Ongoing Project
- [ ] Instructions file updated when stack or standards change
- [ ] Spec updated when bugs found in production
- [ ] Session primer template ready (fill before each agent session)
- [ ] Mermaid diagrams in spec for all stateful processes

### Before a Large Implementation Session
- [ ] Spec reviewed and current (no outdated sections)
- [ ] Session context primer written (current status, this session's goal)
- [ ] Correct model selected (not "auto" for complex implementation)
- [ ] Relevant MCP servers active
- [ ] Git branch created before session starts
