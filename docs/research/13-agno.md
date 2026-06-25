# Agno

> Agent platform SDK with runtime, storage, scheduling, and a control plane.

Agno is the likely match for the "apex" package the user was trying to name. It is not just an agent wrapper; it is an agent platform with production runtime features.

## How it works

- Build agents or multi-agent teams.
- Run them as services with tracing, scheduling, RBAC, and audit logs.
- Keep session state, memory, and context in your own database.
- Expose agents through an AgentOS control plane.

## Where it fits in Harmonic Coding

- Use it when you want persistent agent infrastructure, not just one-off help.
- Use it when the workflow needs storage, approval, or a UI/control plane.
- Use it when the project evolves from "coding assistant" to "agent platform."

## Why it matters

- It moves the conversation from prompts to operationalized agents.
- It is a good fit for the user's "step-by-step system" idea once the workflow needs state and control.

## Setup shape

```bash
uv pip install -U agno openai
uv pip install -U 'agno[os]'
```

## References

- https://github.com/agno-agi/agno
- https://docs.agno.com
- https://docs.agno.com/coding-agents
