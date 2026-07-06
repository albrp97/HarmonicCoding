# Harmonic Coding Local Overrides

These settings override the root `AGENTS.md` when a repository using Harmonic Coding needs stricter or more specific behavior.

## Override precedence

1. `AGENTS.md` defines the shared framework rules.
2. `harmonic-custom/AGENTS.md` overrides those rules for the local repository.
3. `.github/instructions/*.instructions.md` provide path-scoped detail for matching files.

## Local defaults

- prefer strong upfront planning over repeated replanning
- require documentation updates when workflows or setup expectations change
- keep implementation inside one active ticket at a time
- treat the AIDD gap plan as the live backlog for this repository when that work is active

## Skill discovery

Read `harmonic-custom/skills/index.md` to find the reusable skill entrypoints.
