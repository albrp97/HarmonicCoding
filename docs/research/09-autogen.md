# AutoGen

> Multi-agent framework for autonomous or human-assisted workflows.

AutoGen is built for multi-agent conversations and tool use. It can act autonomously, but it is now in maintenance mode, so new projects should treat it as a reference point rather than the default choice.

## How it works

- Agents are composed with assistant/tool patterns.
- MCP workbenches let agents browse and use tools.
- AutoGen Studio gives a no-code way to prototype workflows.
- The framework supports multi-agent orchestration through agent-to-agent tools.

## Where it fits in Harmonic Coding

- Use it when you need explicit roles like researcher, planner, and coder.
- Use it for experiments, prototypes, or existing AutoGen codebases.
- For a brand-new build, Microsoft recommends Microsoft Agent Framework instead.

## Why it matters

- It formalized the multi-agent pattern many newer tools copied.
- It is useful for comparing workflow architecture, even if it is not the final choice.

## Setup shape

```bash
pip install -U "autogen-agentchat" "autogen-ext[openai]"
pip install -U "autogenstudio"
```

## References

- https://github.com/microsoft/autogen
- https://microsoft.github.io/autogen/
