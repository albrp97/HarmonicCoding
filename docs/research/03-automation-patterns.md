# Automation Patterns: Copilot CLI, Agent Mode, and Team-Scale AI

> The difference between "using AI" and "operating AI infrastructure" is automation. This document covers how to move from interactive Copilot usage to scripted, scheduled, and programmatic AI workflows.

---

## The Tool Landscape (2025–2026)

### Important: `gh copilot` Is Retired

The old `gh copilot explain` / `gh copilot suggest` extension is retired. It has been replaced by the **GitHub Copilot CLI** — a standalone binary with full agent capabilities.

```bash
npm install -g @github/copilot
copilot   # interactive REPL
copilot -p "your task" --no-ask-user -s   # programmatic/non-interactive
```

### What Copilot CLI Can Actually Do

Two modes that matter:

**Interactive REPL** — full context management, plan mode, model switching, MCP servers, `/every` scheduling:
```bash
copilot
> Refactor the authentication module to use the new TokenService class
> /model claude-opus-4.8
> Shift+Tab   # plan mode: shows plan before executing
```

**Programmatic (non-interactive)** — single-shot execution for scripts and CI:
```bash
copilot \
  -p "Fix all ESLint errors in src/" \
  --allow-tool='write, shell(npm:*), shell(npx:*), shell(git:*)' \
  --no-ask-user \
  -s    # silent: clean output for capture
```

---

## Core Automation Patterns

### Pattern 1: Loop-Based Bulk Operations

The Belgium "document 100 repos" pattern. Any repetitive per-file or per-repo operation:

```bash
#!/bin/bash
# Document all service files
for file in src/services/*.ts; do
  echo "=== Processing $file ==="
  copilot \
    -p "Generate comprehensive JSDoc for all exported functions in $file. Write in-place." \
    --allow-tool='write' \
    --no-ask-user \
    -s
done
echo "Done. Review changes with: git diff src/services/"
```

```bash
# Mass migration: update all React class components to hooks
for file in $(git grep -l "extends Component" src/); do
  copilot \
    -p "Convert the React class component in $file to a functional component with hooks.
        Preserve all behavior. Do not change the component's public API." \
    --allow-tool='write' \
    --no-ask-user \
    -s
  echo "Migrated: $file"
done
```

```bash
# Generate test files for all services missing them
for service in src/services/*.ts; do
  name=$(basename "$service" .ts)
  test_file="tests/unit/${name}.test.ts"
  if [ ! -f "$test_file" ]; then
    copilot \
      -p "Generate comprehensive unit tests for $service.
          Output to $test_file. Use Jest + TypeScript.
          Cover all public methods and edge cases." \
      --allow-tool='write' \
      --no-ask-user \
      -s
  fi
done
```

### Pattern 2: Conditional AI Logic

Capture output and branch on AI response:

```bash
# Only deploy if AI confirms no security issues
result=$(copilot \
  -p "Analyze the diff in git staging area for security vulnerabilities.
      Reply with SAFE or UNSAFE and one line of explanation." \
  --allow-tool='shell(git:*)' \
  --no-ask-user \
  -s)

if echo "$result" | grep -qi "^SAFE"; then
  echo "✅ Security check passed: $result"
  git push && gh pr create --fill
else
  echo "❌ Security issue detected: $result"
  exit 1
fi
```

```bash
# Check if breaking change before merging
breaking=$(copilot \
  -p "Does this diff contain a breaking change to any public API? Reply YES or NO only." \
  --allow-tool='shell(git:*)' \
  --no-ask-user -s)

[ "$breaking" = "YES" ] && echo "BREAKING" >> .release-notes
```

### Pattern 3: Scheduled Prompts in Interactive Session

Inside the Copilot CLI REPL:
```bash
/every 1h run the test suite and summarize any new failures
/every 4h check git log for new commits and summarize what changed
/after 30m verify that the address validation works correctly on the test cases
```

For unattended cron-style operations, use the programmatic mode from a system cron or GitHub Actions schedule:
```yaml
# .github/workflows/daily-coverage.yml
on:
  schedule:
    - cron: '0 8 * * 1'  # Mondays at 8am
jobs:
  coverage-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - run: npm install -g @github/copilot
      - run: |
          copilot \
            -p "Run the test suite, analyze coverage gaps, and open a GitHub issue
                listing the top 5 uncovered modules ranked by risk." \
            --allow-tool='shell(npm:*), shell(npx:*)' \
            --no-ask-user -s
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Pattern 4: Tool Permission Granularity

The `--allow-tool` / `--deny-tool` flags are your safety boundary in automation:

```bash
# Read-only audit (safe for any codebase)
copilot -p "Audit all SQL queries for SQL injection risks" \
  --allow-tool='shell(git:*)' \
  --deny-tool='write' \
  --no-ask-user -s

# Allow everything except dangerous operations
copilot -p "Implement the feature" \
  --allow-all-tools \
  --deny-tool='shell(rm)' \
  --deny-tool='shell(git push)' \
  --no-ask-user

# Specific MCP server tools only
copilot -p "Create a PR for these changes" \
  --allow-tool='GitHub-MCP-Server' \
  --deny-tool='GitHub-MCP-Server(delete_repository)' \
  --no-ask-user -s
```

### Pattern 5: ACP Server for CI/CD Integration

The Agent Client Protocol (ACP) server embeds Copilot CLI into any orchestration system:

```bash
# Start as stdio server (for subprocess embedding)
copilot --acp --stdio

# Start as TCP server (for microservice integration)
copilot --acp --port 3000
```

This allows your CI/CD pipeline, custom tools, or multi-agent orchestration to call Copilot CLI as an agent via a standard protocol — not as a shell command.

---

## Copilot Cloud Agent: Plan-then-Execute Architecture

### The Two-Phase Model

The cloud agent (formerly Workspace) separates **your setup** from **agent execution**:

```
Phase 1: copilot-setup-steps.yml  (your YAML, your control)
  → checkout → install deps → baseline test run → baseline lint

Phase 2: Agent's autonomous work  (agent's control)
  → reads COPILOT_INSTRUCTIONS.md
  → explores codebase
  → edits files, runs tests, fixes failures
  → pushes branch, opens PR
```

Both phases run in the same container. You control Phase 1. The agent controls Phase 2.

### The `copilot-setup-steps.yml`

The most important file for cloud agent reliability:

```yaml
name: "Copilot Setup Steps"
on:
  workflow_dispatch:
  push:
    paths: [.github/workflows/copilot-setup-steps.yml]

jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5
      
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests (baseline)
        run: pytest tests/ -v --tb=short || true
        # || true: agent sees pre-existing failures, doesn't treat them as its fault
      
      - name: Run linters (baseline)
        run: |
          ruff check src/ || true
          mypy src/ --ignore-missing-imports || true
```

**Why `|| true` matters**: The agent reads the baseline output and knows which tests were already failing. It won't try to fix pre-existing failures as part of your requested task, and it won't report them as new failures from its changes.

### COPILOT_INSTRUCTIONS.md — The Agent Contract

Located at `.github/COPILOT_INSTRUCTIONS.md` or `.github/copilot-instructions.md`. Read by the agent before every session.

```markdown
# Agent Instructions

## Project Context
This is a FastAPI service for client screening. See docs/specs/client-check/spec.md for the full specification.

## Before Starting Any Task
1. Read the spec file relevant to what you're working on
2. Check existing tests for the area you'll modify
3. Find similar existing implementations and follow their patterns

## Branch Naming
feature/{issue-number}-{short-description}
fix/{issue-number}-{short-description}
Never commit directly to main.

## Pre-Commit Checks (Run Every Time)
```bash
black src/ tests/
ruff check src/ tests/
mypy src/ --ignore-missing-imports
pytest tests/ -v --tb=short
```

## Boundaries
- You may modify: src/, tests/, docs/
- You may NOT modify: .github/workflows/, infrastructure/, migrations/ (create new only)
- You may NOT install packages without adding to pyproject.toml

## Security Rules
- No `eval()`, `exec()`, `os.system()`
- No hardcoded secrets, tokens, or credentials
- All user inputs must be validated before use
- SQL queries must use parameterized statements

## Definition of Done
A task is complete when:
- All pre-commit checks pass cleanly
- New tests cover the new behavior
- The spec file is updated if behavior changed
- PR description explains what changed and why
```

### Assigning Tasks to Copilot Agent

**Via GitHub Issue:**
1. Create an issue describing the task
2. Assign to `@copilot` (or `@claude`, `@codex`)
3. Agent picks it up, runs setup steps, implements, opens PR

**Via GitHub API (programmatic dispatch):**
```bash
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /repos/OWNER/REPO/issues \
  --input - <<< '{
    "title": "Implement FRIS integration per spec",
    "body": "See docs/specs/nl-client-check/spec.md. Implement sections 3.1-3.5.",
    "assignees": ["copilot-swe-agent[bot]"],
    "agent_assignment": {
      "target_repo": "OWNER/REPO",
      "base_branch": "main",
      "custom_instructions": "Use prompt caching for the spec context. Follow the existing client-check pattern.",
      "model": "claude-opus-4.8"
    }
  }'
```

**Via Cloud Agent REST API:**
```bash
# Dispatch programmatically
TASK_ID=$(curl -s -X POST \
  -H "Authorization: Bearer $GH_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/agents/repos/OWNER/REPO/tasks \
  -d '{"prompt": "Add FRIS integration", "base_ref": "main", "create_pull_request": true}' \
  | jq -r '.id')

# Poll status
watch -n 30 "curl -s -H 'Authorization: Bearer $GH_TOKEN' \
  https://api.github.com/agents/repos/OWNER/REPO/tasks/$TASK_ID | jq '.state'"
# state: queued | in_progress | completed | failed | waiting_for_user | timed_out
```

---

## Custom Agents and Skills: The Belgium Pattern at Scale

### Custom Agent Files (`.github/agents/`)

Custom agents give non-engineers targeted AI capabilities without writing prompts:

```markdown
# .github/agents/sql-query-helper.md
---
name: SQL Query Helper
description: Generates SQL queries for the analytics database from plain English.
tools: [read_file, create_file]
---

You are a SQL expert for our PostgreSQL analytics database.
The schema is defined in docs/schema.sql. Read it before every query.

Rules:
- Always use CTEs, never inline subqueries
- Add EXPLAIN ANALYZE hints for reports
- Never use SELECT * in production queries
- Always specify column aliases for calculated fields
```

Use in Copilot Chat: `@sql-query-helper show me last week's policy renewals by country`

**Scope tiers:**
| Location | Scope |
|----------|-------|
| `~/.copilot/agents/` | Personal, all projects |
| `.github/agents/NAME.md` | Repo-wide |
| `.github-private/agents/NAME.md` | Org-wide (enterprise) |

### Community Skills from `github/awesome-copilot`

The official Copilot skills and instructions community hub. Install directly:

```bash
gh skill search documentation
gh skill install github/awesome-copilot documentation-writer
gh skill install github/awesome-copilot security-reviewer
gh skill install github/awesome-copilot test-generator
gh skill update --all
```

### Prompt Files for Reusable Templates

```markdown
# .github/prompts/generate-api-endpoint.prompt.md
---
name: Generate API Endpoint
description: Scaffold a complete FastAPI endpoint with service, repository, tests
---
Create a new API endpoint for: ${ENDPOINT_DESCRIPTION}

Follow the pattern in src/api/clients.py exactly.
Create:
1. Pydantic schema in src/schemas/
2. Repository method in src/repositories/
3. Service method in src/services/
4. Router endpoint in src/api/
5. Unit test for service
6. E2E test for endpoint

Reference the spec at docs/specs/api-design-contract.md for all design decisions.
```

Available in VS Code via the Copilot prompt picker.

---

## Copilot Automations: Event-Triggered AI

The highest leverage automation: Copilot reacts to repository events automatically.

Configure at: **Repo Settings → Copilot → Automations**

### Example Automations

**Auto-generate SQL from issues:**
```
Trigger: Issue created
Filter: Label contains "sql-request"
Action: Generate SQL query from issue body using the analytics schema.
        Post the query as a comment on the issue.
Model: Claude Sonnet 4.6
```

**Auto-review PRs for security:**
```
Trigger: PR opened
Filter: Files changed include src/**
Action: Review the diff for security vulnerabilities.
        If any found, post a review comment and request changes.
        Focus on: SQL injection, XSS, auth bypass, hardcoded secrets.
Model: Claude Sonnet 4.6
```

**Weekly documentation update:**
```
Trigger: Schedule (every Monday 9:00)
Action: Diff any changes since last week. Update CHANGELOG.md.
        Identify any undocumented public API changes and create issues.
Model: Claude Haiku 4.5 (cheap, mechanical task)
```

**Auto-assign stale issues:**
```
Trigger: Issue created with label "spec-implementation"
Action: Analyze the issue, check the relevant spec section,
        create a task branch, and begin implementation.
        Open a draft PR when implementation starts.
```

---

## Multi-Agent Architecture (Advanced)

### The ant3869/AgenticWorkflow Pattern

A production-validated multi-role agentic framework:

```
Issue/Spec Input
      │
      ▼
[Architect Agent]
  - Decomposes task
  - Identifies files to modify
  - Creates step plan
      │
      ▼
[Implementer Agent]
  - Executes plan steps
  - Writes code
  - Runs tests
      │
      ▼
[Debugger Agent]  ◄─ loops back on test failure
  - Analyzes failures
  - Identifies root cause
  - Proposes fix
      │
      ▼
[Reviewer Agent]
  - Reviews implementation vs spec
  - Checks coding standards
  - Approves or requests changes
      │
      ▼
[Historian Agent]
  - Updates spec with any decisions made
  - Updates changelog
  - Creates final PR
```

Implement this via:
- Custom agent files for each role
- AGENTS.md that defines the handoff protocol
- Copilot CLI ACP server as the orchestration runtime

### BYO Model Provider for Agent Pipelines

For teams with enterprise model contracts outside GitHub:

```bash
# Use Azure OpenAI endpoint
COPILOT_PROVIDER_BASE_URL=https://mycompany.openai.azure.com \
COPILOT_PROVIDER_TYPE=openai \
COPILOT_PROVIDER_API_KEY=$AZURE_OPENAI_KEY \
COPILOT_MODEL=gpt-4o \
copilot -p "Implement the spec" --no-ask-user -s
```

This enables routing different tasks to different providers without changing tooling.

---

## The Human Bottleneck: PR Review at Scale

When AI generates code at scale, human PR review becomes the constraint. Mitigations:

### Automated PR Review (GitHub Copilot Code Review)

Enable in repository settings. Copilot reviews every PR automatically:
- Security vulnerabilities
- Logic errors
- Test coverage gaps
- Spec compliance (if spec is in context)

Best practice: configure Copilot as a **required reviewer** so the AI check must pass before human review is requested. This filters trivially incorrect AI output before humans see it.

### Spec-Based Validation (Automated Quality Gate)

The most powerful approach: validate generated code against the spec automatically.

```bash
# In CI pipeline (post-implementation, pre-human-review)
copilot \
  -p "Read docs/specs/client-check/spec.md.
      Read the implementation in src/.
      For each MUST requirement in the spec, verify it is implemented.
      Output a checklist: ✅ MUST-001 implemented, ❌ MUST-007 missing: [reason]
      If any MUST requirements are missing, exit 1." \
  --allow-tool='shell(git:*)' \
  --no-ask-user -s
```

This creates a spec compliance gate — the AI validates its own output against the spec before humans review it.

### Tiered Review Strategy

| Change type | Review approach |
|-------------|----------------|
| AI-generated boilerplate | Copilot auto-review only; human spot-check 10% |
| AI-generated business logic | Copilot auto-review + human review spec compliance |
| Architecture changes | Full human review mandatory |
| Security-sensitive changes | Full human review + Copilot security scan |
| Spec-compliant implementations | Test suite pass + spec gate is sufficient for >70% of cases |

---

## Production Setup Checklist

### Per Repository
- [ ] `.github/copilot-instructions.md` — always-on context
- [ ] `.github/AGENTS.md` — agentic session rules
- [ ] `copilot-setup-steps.yml` — cloud agent baseline
- [ ] `.github/agents/` — custom agents for non-engineers
- [ ] `.github/prompts/` — reusable prompt templates
- [ ] `.github/skills/` — custom skill implementations
- [ ] Copilot automations configured for common triggers

### Per Team
- [ ] `github/awesome-copilot` skills installed and pinned to versions
- [ ] Copilot Code Review enabled and configured as required reviewer
- [ ] Budget controls and User-Level Budgets set
- [ ] Model policy for premium models (which roles/people can use Opus-tier)

### Per Engineer
- [ ] `~/.copilot/agents/` — personal agent definitions
- [ ] Copilot CLI installed and authenticated
- [ ] Preferred model configured for different task types
- [ ] Plan mode (Shift+Tab) used habitually before large tasks
