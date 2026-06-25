# OpenHands + SWE-agent

> Autonomous execution layer for issue fixing, automation, and self-hosted agent control.

OpenHands is the broader control center. SWE-agent is the issue-fixing agent. Together they cover the "let the system keep going" side of the workflow spectrum.

## How it works

- OpenHands can run local, Docker, VM, or cloud backends.
- It can host OpenHands itself or other agents like Claude Code and Codex.
- It supports automations, schedules, webhooks, and ACP-compatible agents.
- SWE-agent takes a GitHub issue and tries to fix it with tool use.

## Where it fits in Harmonic Coding

- Use it when a workflow needs to run longer than a chat session.
- Use it for unattended issue triage, automation, and issue-to-PR loops.
- Use it when you want a developer control center rather than a terminal assistant.

## Notes

- SWE-agent is the research-heavy version; its maintainers now recommend mini-swe-agent for simpler use.
- OpenHands is the better fit when you want a control plane around multiple agent backends.

## Setup shape

```bash
npm install -g @openhands/agent-canvas
agent-canvas
```

## References

- https://github.com/OpenHands/OpenHands
- https://github.com/SWE-agent/SWE-agent
- https://github.com/SWE-agent/mini-swe-agent
