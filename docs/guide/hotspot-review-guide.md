# Hotspot Review Guide

> Lightweight hotspot analysis for prioritizing review effort around risky files.

Use this guide when the repository does not yet have a dedicated churn-analysis CLI but still needs a consistent way to identify high-risk files.

## Purpose

Hotspot review is a prioritization layer. It tells you where review attention should go first.

It does **not** automatically mean:

- rewrite the file
- split the PR
- block the change

## Signal order

Use these signals in order:

1. **Size** — large files create larger review surface and blast radius
2. **Churn** — frequently changed files are more likely to hide regressions or unstable design
3. **Complexity** — branch-heavy or responsibility-heavy files are harder to reason about safely
4. **Recency / instability** — files touched repeatedly in a short period may deserve extra scrutiny

## Fallback heuristic

If no automated metric exists, review files as higher risk when they combine:

- unusually broad responsibility
- recent repeated edits
- large changed surface area
- known fragility or past bug concentration

## Review actions

| Risk level | What to do |
|---|---|
| Low | normal review is enough |
| Medium | read the full affected file and cross-check validation |
| High | review carefully, verify tests/docs, and consider reducing scope before merge |

## Reporting format

For each hotspot:

1. file path
2. dominant signal
3. why it matters to the current change
4. required review action
