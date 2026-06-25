# Aider

> Terminal pair-programming that edits code as git diffs.

Aider is the simplest fit when you want Copilot-style help but need every change to stay reviewable in git. It maps the codebase, can lint and test after edits, and works with cloud or local models.

## How it works

- Start inside a repo.
- Aider scans the codebase and builds a map.
- You ask for a change in the terminal.
- It writes diffs, can commit them, and keeps the review surface small.

## Where it fits in Harmonic Coding

- Use it after the spec or task plan already exists.
- Use it for narrow implementation slices, not for high-level discovery.
- Pair it with the existing AIDD and spec-driven docs so the model does not invent scope.

## Why it matters

- Reviewable output.
- Repo-aware editing.
- Good fit for small, controlled changes where Copilot is the UI and Aider is the executor.

## Setup shape

```bash
python -m pip install aider-install
aider-install
cd /path/to/project
aider --model sonnet
```

## References

- https://github.com/Aider-AI/aider
- https://aider.chat/docs/usage.html
