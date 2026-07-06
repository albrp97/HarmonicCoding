---
name: Create Repository Map
description: Build a durable file and folder path map for the repository, with one simple sentence explaining what lives at each important path and how AI should use the map.
---

You have to create a repository map for `${PROJECT_OR_REPO}` before deep planning or implementation starts.

The goal is to give both humans and AI a durable, low-friction map of the repo structure so they do not have to rediscover the layout from scratch in every session.

## What this map is

The repository map is a file that lists repository paths and gives a single simple sentence for what exists there.

It should cover:
- important folders
- important top-level files
- major source areas
- test areas
- automation, CI/CD, and infrastructure paths
- docs and planning paths

It should not waste space on caches, generated artifacts, vendor directories, or other disposable paths unless they matter operationally.

## Outcome

Leave the repository with a durable path map at:
- `docs/planning/repo-map.md`

## Workflow

### 1. Inspect the actual repository structure

Read:
- top-level files and directories
- source directories
- test directories
- documentation directories
- infrastructure / deployment / workflow directories
- important config files

### 2. Decide what to include

Include:
- human-maintained paths
- paths that affect implementation, testing, deployment, or planning
- paths that a future engineer or AI agent is likely to need

Exclude or collapse:
- build outputs
- caches
- vendor directories
- generated artifacts
- trivial noise paths that do not help navigation

### 3. Write one simple sentence per path

Each entry should:
- use the exact path
- say what is there in one simple sentence
- avoid vague descriptions like "misc stuff"
- avoid explaining how the code works in detail

### 4. Structure the map

Create or update `docs/planning/repo-map.md` with this structure:

```markdown
# Repository Map: [Project Name]

## Metadata
| Field | Value |
|---|---|
| Status | ... |
| Last reviewed | ... |
| Derived from | ... |
| Coverage | ... |
| Open questions | ... |

## Top-Level Paths
| Path | Type | What Is Here |
|---|---|---|
| `README.md` | file | Entry point for the repository and project overview. |

## Source Paths
| Path | Type | What Is Here |
|---|---|---|
| `src/...` | directory | Main application source code. |

## Test Paths
| Path | Type | What Is Here |
|---|---|---|
| `tests/...` | directory | Automated test suites and fixtures. |

## Docs and Planning Paths
| Path | Type | What Is Here |
|---|---|---|
| `docs/planning/...` | directory | Planning artifacts such as phases, backlog, and reviews. |

## Automation and Infrastructure Paths
| Path | Type | What Is Here |
|---|---|---|
| `.github/workflows/...` | directory | CI/CD and repository automation workflows. |

## Notes
- ...
```

### 5. Explain how AI should use it

AI should use the repository map to:
- orient itself before broad file search
- identify the likely area for a task faster
- find planning, testing, CI/CD, and source locations consistently
- update the map when meaningful paths are added, removed, or renamed

AI should not treat the map as a substitute for reading the real files. It is a navigation aid and context accelerator.

## Rules

1. Use one simple sentence per path.
2. Prefer useful coverage over exhaustive noise.
3. Keep the map current when structure changes materially.
4. Include planning and workflow paths, not just source code.

## Deliverables

Produce:
1. `docs/planning/repo-map.md`
2. a clean path map with one-line descriptions
3. only the unresolved structural questions that truly block navigation
