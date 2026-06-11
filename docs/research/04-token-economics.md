# Token Economics and Model Selection

> The economics of AI-assisted engineering are not obvious. The headline numbers look extraordinary. The real numbers, after accounting for iteration waste, context injection, and review time, are still compelling — but the calculation matters for team decisions.

---

## Current Model Pricing (June 2026)

### Anthropic Claude (Direct API)

| Model | Input / MTok | Output / MTok | Best For |
|-------|-------------|---------------|----------|
| **Claude Fable 5** | $10.00 | $50.00 | Newest flagship; parallel tool batching |
| **Claude Opus 4.8** | $5.00 | $25.00 | Complex spec work, architecture, debugging |
| **Claude Sonnet 4.6** | $3.00 | $15.00 | Feature implementation; production sweet spot |
| **Claude Haiku 4.5** | $1.00 | $5.00 | Boilerplate, tests, docs, batch jobs |
| Claude Opus 4 *(deprecated)* | $15.00 | $75.00 | **This is the "26x" model — being retired** |

**Prompt caching multipliers** (apply to base input price):
- 5-min cache write: 1.25× | cache hit: **0.1×** (pays off after a single hit)
- 1-hr cache write: 2.0× | cache hit: **0.1×** (pays off after 2 hits)

**Batch API**: 50% off on everything. Most batches complete in under an hour.

**⚠️ Tokenizer note**: Opus 4.7+ and Fable 5 use a new tokenizer that produces **up to 35% more tokens** for identical text. A 5,000-line spec that was 50K tokens on Sonnet 4.6 may be 67K+ tokens on Opus 4.8.

### GitHub Copilot AI Credits (Per 1M Tokens)

1 AI Credit = $0.01. Anthropic models are available in Copilot at the same prices above.

| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| GPT-5 nano | $0.20 | $1.25 | Cheapest |
| GPT-5 mini | $0.25 | $2.00 | Fast completions |
| MAI-Code-1-Flash | $0.75 | $4.50 | Good default |
| GPT-5.3-Codex | $1.75 | $14.00 | Agentic coding |
| GPT-5.4 | $2.50 | $15.00 | Deep reasoning |
| GPT-5.5 | $5.00 | $30.00 | Most powerful OpenAI |

**Critical**: Code completions and inline suggestions are **not billed as AI credits** on any paid plan. They're unlimited. Only chat, agent mode, and CLI usage consumes credits.

### Plan Credit Allowances

| Plan | Monthly | Credits | USD Value | Deep Opus Sessions |
|------|---------|---------|-----------|-------------------|
| Copilot Pro | $10 | 1,500 | $15 | ~20 |
| Copilot Pro+ | $39 | 7,000 | $70 | ~93 |
| Copilot Max | $100 | 20,000 | $200 | ~267 |
| Copilot Business | $19/user | 1,900/user | $19 | ~25 |
| Copilot Enterprise | $39/user | 3,900/user | $39 | ~52 |

*"Deep Opus session" = 150K input tokens on Opus 4.8 = 75 credits = $0.75*

**10% discount**: Auto model selection in Copilot Chat/CLI/agent gives 10% off all model costs. Use it for general sessions; override for specific high-quality tasks.

---

## The "26x Cost Increase" — Explained

The April 2025 workshop speaker said costs went 26× in 6 months. This is real, but refers to **Claude Opus 4 (original, now deprecated)** at $15/$75 per MTok vs. GitHub Copilot Enterprise flat rate.

**The math (April 2025):**
- Copilot Enterprise: $39/user/month (unlimited completions + chat)
- Heavy agent use, Claude Opus 4 API: 20M input + 10M output tokens/month
- Cost: 20M × $15 + 10M × $75 = $300 + $750 = **$1,050/month**
- Ratio: **~27× more expensive** ✓

**Why this is now obsolete:**

| Model | Same 20M in + 10M out | vs. Copilot Enterprise |
|-------|-----------------------|------------------------|
| Opus 4 *(deprecated)* | $1,050/month | **27×** |
| Opus 4.8 *(current)* | $350/month | **9×** |
| Sonnet 4.6 | $210/month | **5×** |
| Sonnet 4.6 + prompt caching | ~$80–100/month | **2–2.5×** |
| Haiku 4.5 | $70/month | **1.8×** |

The Opus 4 → Opus 4.8 transition is a 3× price cut for the same tier. With proper caching, Sonnet 4.6 for intensive spec-driven work costs roughly 2× Copilot Enterprise — a very different decision than "27×."

---

## What 1M Tokens Actually Produces

Rule: 1 token ≈ 4 characters; 1 source line ≈ 8–15 tokens

| Output tokens | Approx. lines of code | Cost (Opus 4.8) | Cost (Sonnet 4.6) |
|---------------|----------------------|-----------------|-------------------|
| 100K | 7,000–12,000 lines | $2.50 | $1.50 |
| 500K | 35,000–60,000 lines | $12.50 | $7.50 |
| 1M | 70,000–120,000 lines | $25.00 | $15.00 |

**Reality check**: In practice, agent loops involve 5–15× more input tokens than output tokens because context (spec + codebase + conversation history) is re-injected each turn. Generating 10,000 lines of real code might produce 200K output tokens but consume 1–2M input tokens.

---

## Real Cost of a Spec-Driven Iteration Cycle

### Token Profile of a 5,000-Line Spec Session

| Component | Tokens (Opus 4.7+ tokenizer) |
|-----------|------------------------------|
| Spec text (5K lines) | ~67,500 |
| System prompt + instructions | ~6,750 |
| Conversation history (10 turns) | ~67,500 |
| Codebase context (selective) | ~100,000–500,000 |
| **Total input per turn** | **~80K–175K** |
| Typical output per turn | ~2,000–8,000 |

### 10-Turn Implementation Cycle

| Phase | Turns | Input tokens | Output tokens |
|-------|-------|-------------|---------------|
| Spec planning + decomposition | 5 | 750,000 | 25,000 |
| Implementation | 3 | 450,000 | 30,000 |
| Review + refinement | 2 | 300,000 | 15,000 |
| **Total** | **10** | **1.5M** | **70K** |

### Cost per Cycle

| Model | Input | Output | **Total** |
|-------|-------|--------|-----------|
| Claude Opus 4.8 | $7.50 | $1.75 | **$9.25** |
| Claude Sonnet 4.6 | $4.50 | $1.05 | **$5.55** |
| Claude Haiku 4.5 | $1.50 | $0.35 | **$1.85** |

### With Prompt Caching (Opus 4.8)

The spec is static across all turns — ideal for caching:
- Without caching: $9.25/cycle
- With 1-hr cache on spec + system prompt (75K tokens): **~$7.10/cycle** (23% reduction)
- Over a full day of iterative spec work, caching compounds meaningfully

### Monthly Cost for a Team Running 2 Spec Cycles/Day

| Model | Per cycle | 40 cycles/month | vs. $39 Copilot Enterprise |
|-------|-----------|----------------|----------------------------|
| Opus 4.8 (with caching) | $7.10 | **$284/month** | 7× |
| Sonnet 4.6 (with caching) | $4.20 | **$168/month** | 4× |
| Sonnet 4.6 (Batch API) | $2.80 | **$112/month** | 3× |

The Belgium team's client check API cost "~500% usage cap" — roughly $500 total for the entire project. At $284/month for intensive daily spec work, the ROI depends on what the engineer would otherwise cost to do the same work.

---

## Model Selection Decision Framework

### By Task Type

| Task | Model | Reason |
|------|-------|--------|
| Spec writing / requirements decomposition | Claude Opus 4.8 | Reasoning-heavy; worth cost premium |
| Spec review and validation | Claude Sonnet 4.6 | Strong reasoning, 3× cheaper |
| Implementation from spec | Claude Sonnet 4.6 | Cost-efficient for mechanical work |
| Complex multi-file debugging | Claude Opus 4.8 | Multi-hop reasoning |
| Test generation | Claude Haiku 4.5 | Mechanical; Haiku is sufficient |
| Documentation generation | Claude Haiku 4.5 | Extractive task |
| Code review (security focus) | Claude Sonnet 4.6 | Reasoning about edge cases |
| Batch/async analysis | Any via Batch API | 50% discount; use for non-interactive |
| Quick inline suggestions | Haiku / GPT-5 mini | Speed > quality at this granularity |
| Long-horizon autonomous implementation | Claude Fable 5 | Parallel tool batching; first-attempt accuracy |

### By Context Size

| Context size | Approach |
|--------------|----------|
| < 50K tokens | Any model, no special handling |
| 50K–200K | Enable prompt caching for static parts (spec, instructions) |
| 200K–500K | Sonnet 4.6 or Opus 4.8 (1M window); enable caching + server-side compaction |
| > 500K | Selective context injection required; cannot load full codebase |

### Context Performance Cliff

Anthropic's data shows accuracy degradation as context fills:
- **0–200K tokens**: Near-optimal
- **200K–500K**: Moderate degradation on retrieval tasks; reasoning stays strong
- **500K–1M**: Meaningful accuracy degradation for long-range references

**Mitigation**: Place the most critical material (spec, current task) at the START and END of context. Primacy and recency effects apply.

### The Auto Setting Reality

GitHub Copilot's "auto" model routes based on task complexity heuristics. It gives a 10% discount on model costs. Use it for general chat and completion sessions.

**Do not use "auto" for**:
- Spec iteration sessions (you want consistent model for consistency)
- Security-sensitive code generation (want known-quality model)
- Critical architectural decisions

---

## Cost Optimization Strategies

### 1. Prompt Caching for Large Static Contexts

Put static content first in the prompt: system instructions → spec → relevant code → dynamic history. A 50K-token spec re-injected 10 times without caching costs $2.50 at Opus 4.8 pricing. With 5-min cache: $0.025 after the first hit. **90% reduction on the spec portion alone.**

### 2. Model Tiering

Route tasks to the right tier:
```
Inline completion / quick syntax → Haiku 4.5 ($1/$5)
Feature code + tests            → Sonnet 4.6 ($3/$15)
Spec writing + architecture     → Opus 4.8 ($5/$25)
Batch/async analysis            → Any model via Batch API (50% off)
```

A 5-tier workflow moving from Haiku to Opus only when needed reduces overall costs by 3–5× compared to using Opus for everything.

### 3. Output Format Discipline

- "Return ONLY the modified function, no explanation" → 30–60% fewer output tokens
- Use diff/patch format for large file modifications instead of full rewrites
  - 10K-line file patch: ~200 tokens vs. ~100K tokens for full rewrite
- Request numbered lists, not prose, for multi-step plans

### 4. Context Surgery

- Only inject files the current task touches — not the full codebase
- Strip test fixtures, migrations, and auto-generated files from context
- After resolving a problem, summarize conversation history instead of carrying verbatim turns
- Use semantic search (GitHub MCP, file system MCP) to identify minimal relevant context

### 5. Batch API for Non-Interactive Work

Documentation generation, code reviews, linting commentary, spec analysis — any task that doesn't need a real-time response is a Batch API candidate. 50% discount. Results within an hour. Max 100K requests or 256MB per batch.

```python
# Batch spec compliance checks across 100 modules
import anthropic
client = anthropic.Anthropic()

requests = []
for module_file in module_files:
    requests.append({
        "custom_id": f"check-{module_file.stem}",
        "params": {
            "model": "claude-sonnet-4-6",
            "max_tokens": 1024,
            "messages": [{
                "role": "user",
                "content": f"Check if {module_file.read_text()} implements requirements from spec..."
            }]
        }
    })

batch = client.messages.batches.create(requests=requests)
# Poll until complete; retrieve results
```

### 6. Extended Thinking Token Management

When using adaptive/extended thinking on Opus 4.8:
- Thinking tokens are billed as output tokens (at $25/MTok for Opus)
- BUT they're stripped from conversation history — they don't accumulate
- Use `effort: medium` or `low` for implementation tasks; reserve `high` for spec writing and debugging

### 7. Context Compaction

For long agentic sessions: enable server-side compaction (beta on Opus 4.8+). The model automatically summarizes earlier conversation portions to extend effective session length beyond the context limit. This prevents the session from failing mid-implementation on large specs.

---

## Breakeven: AI Cost vs. Engineer Time

### Baseline
- Senior engineer: ~$75–100/hour
- Mid-level engineer: ~$60–75/hour

### Scenario Comparisons

**Simple CRUD endpoint + tests:**
- Engineer: 2 hours = $150
- AI (Sonnet 4.6, 3 turns): ~$3–5
- **AI wins at >95% cost savings** — assuming spec is good

**Complex architectural refactor (5K-line module):**
- Engineer: 2 days = $1,200
- AI (Opus 4.8, 15 turns with caching) + 4hr human review: ~$50–80 + $300 = $380
- **AI wins at ~68% cost savings** — human review cost is the main factor

**New microservice from scratch (~3K lines):**
- Engineer: 1 week = $3,000
- Spec writing (human 4hr) + AI implementation (20 cycles) + integration (1 day): $300 + $150 + $600 = **$1,050**
- **65% cost savings**

**Batch documentation / test generation (50K files):**
- Engineer: infeasible in a sprint
- AI (Haiku + Batch API): ~$25–50
- **No practical comparison — AI wins unambiguously**

### The True Cost Model

Empirically: ~30–60% of AI-generated tokens are "wasted" on context re-injection, thinking, and discarded iteration output. The effective cost per usable line of code is 2–3× the raw token calculation.

Even with that factor applied, the cost advantage vs. engineer time is typically **5–20× for well-specified work**.

### Copilot Enterprise vs. Direct API

| Team profile | Best fit |
|-------------|---------|
| Mostly completions + occasional chat | Copilot Business/Enterprise — unlimited completions not metered |
| Heavy agentic spec-driven workflows | Direct API + caching + Batch — more control at scale |
| Code reviews + PR assistance | Copilot Enterprise — built-in, includes Actions minutes |
| Mixed usage (most teams) | Copilot Enterprise as baseline + direct API for intensive sessions |

The direct API premium vs. Copilot Enterprise ($39/user/month) is:
- **Real** if you're running intensive Opus-tier sessions daily
- **Manageable** with Sonnet 4.6 + caching (2–3× premium, but you control every parameter)
- **Often irrelevant** if completions drive most of the value (those are unlimited on paid plans)

---

## Monitoring and Budget Controls

### Setting Up Token Dashboard

GitHub Copilot provides:
1. **AI usage dashboard** — per-user credit consumption, model breakdown, time series
2. **Usage export CSV** — filterable by user, model, feature
3. **Budget controls** at four levels:
   - User-Level Budget (ULB): per-user cap per billing cycle
   - Cost Center budget: team/org cap on metered charges
   - Enterprise spending limit: total metered charges across enterprise
   - **Enable "Stop usage when budget limit reached"** — this is OFF by default

### Recommended Admin Workflow

1. Export usage CSV → identify top 10% credit consumers
2. Check model patterns: users driving high spend on Opus for simple tasks → apply model restrictions
3. Set ULB at ~2× per-license value (allows pooling, prevents outliers)
4. Individual ULB overrides for power users
5. Enterprise spending limit = max acceptable monthly overage; toggle "stop on limit reached" ON

### Model Policy Controls (Enterprise)

Configure which models are available per user tier:
- IC engineers: Sonnet-tier default; Opus available for opt-in
- Staff engineers: Opus-tier default
- Platform/infra: all models
- Automation accounts (CI/CD): Haiku/Sonnet only, no Opus

This prevents accidental Opus usage in CI pipelines which can spike costs dramatically.
