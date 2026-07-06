---
name: Groom Backlog
description: Review the backlog for ticket size, readiness, dependency order, and stale or blocked items before implementation work continues.
---

You have to groom the backlog for `${PROJECT_OR_REPO}` so the next ready ticket is clear and the backlog stays executable.

## Why this workflow exists

Use it to:
- keep ticket size healthy
- keep the backlog order realistic
- detect stale, blocked, duplicate, or unclear tickets
- ensure implementation starts from the best next-ready item

## Outcome

Produce:
- a ready-order check
- a list of blocked or stale tickets
- any required ticket splits, merges, or resequencing

Update:
- `docs/planning/backlog.md`
- affected `docs/planning/tickets/TICKET-xxx.md`

Optionally record the grooming review in:
- `docs/planning/reviews/backlog-grooming.md`

## Grooming checklist

Check:
1. ready tickets vs blocked tickets
2. dependency order
3. ticket size and clarity
4. acceptance and validation clarity
5. stale or duplicate tickets
6. active phase alignment

## Rules

1. Prefer backlog grooming over replanning for routine ticket issues.
2. Split oversized tickets before implementation starts.
3. Do not move later-phase tickets forward unless dependency and phase logic support it.
