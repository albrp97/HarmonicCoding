# LangGraph

> Low-level orchestration for stateful agents and long-running workflows.

LangGraph is the strongest match for "break this into ordered steps and keep state." It is designed for durable execution, human-in-the-loop control, memory, and production deployment.

## How it works

- Build workflows as graphs of nodes and edges.
- Persist state across failures and resumptions.
- Interrupt the flow for human review when needed.
- Use LangSmith for debugging and traces.

## Where it fits in Harmonic Coding

- Use it when the workflow order matters more than the chat UX.
- Use it for research -> plan -> implement -> review pipelines.
- Use it when the task may pause, resume, or need state across steps.

## Why it matters

- It gives the clearest "ordered steps" model in this stack.
- It is a good default for the workflow layer the user was asking about.

## Setup shape

```bash
pip install -U langgraph
```

## References

- https://github.com/langchain-ai/langgraph
- https://docs.langchain.com/oss/python/langgraph/overview
