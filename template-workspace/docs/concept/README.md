# docs/concept

This folder is the source of truth for *what gets built*. It is the one thing you
maintain by hand: dump everything in your head here, in whatever structure suits
you. There is no required file layout and no required filenames.

The agent reads all of it and infers your stack, goals, and constraints. Then
`/sync-protocols` reconciles that intent into the protocol files (the Project
Specifics regions of `AGENTS.md` and `DESIGN.md`). After you change anything here,
run `/sync-protocols`, then clear the session and resume from `prompt.md`.

## Suggested structure (optional)

Numbered files read in order. A common shape:

- `00_vision.md` — the north star: what this is, who it is for, why it matters.
- `01_requirements.md` — scope, features, constraints.
- `02_architecture.md` — high-level shape and key decisions.
- `0X_technical_spec.md` — the stack and tooling (drives the AGENTS.md Toolchain).

Use as many or as few as you like. Prose, bullets, or diagrams all work. The
technical spec is just the highest-signal input; the agent does not require it.

## A starting point

Staring at a blank folder? Create `00_vision.md` with something like:

```md
# Vision

## What this is
One or two sentences on the product or project.

## Who it is for
The user and the problem being solved.

## What "done" looks like
The outcome that means this succeeded.

## Constraints
Stack preferences, non-negotiables, things to avoid.
```
