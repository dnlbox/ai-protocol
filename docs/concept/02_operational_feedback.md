# Operational Feedback Loops

## Problem

The protocol can be mechanically present and still fail in practice. The Mycelia
dogfood retrospective exposed two failures:

- State files grew useful history until the current handoff became too expensive
  to read.
- Protocol sync was treated as a tool to remember, not a closeout gate tied to
  the kinds of changes that make protocol files stale.

Both failures are adoption failures, not syntax failures. The protocol must make
the healthy path the default path for agents that are tired, context-starved, or
resuming after another session.

## Consolidate state by trigger

`/consolidate-state` should run when there is observable evidence that state is
becoming less useful:

- `BUILD_STATE.md` `Now` exceeds one screen.
- Session logs sprawl past their intended scan budget.
- `git log`, validation output, or current files contradict `Now`.
- A workspace Components table drifted from a child project's real state.
- Three shipped slices have accumulated since the last archive.

The output is not a summary for its own sake. It preserves the next handoff,
keeps decisions append-only and terse, and pushes completed detail into
`Archive` where git can carry the full history.

## Sync protocols as closeout gate

`/sync-protocol` should run, or be simulated as a no-op audit, before closeout
when either source intent or project behavior changed:

- `docs/concept/` changed.
- Implementation changed the toolchain, validation gates, harness configuration,
  command surfaces, runtime assumptions, or any project-specific behavior that
  `AGENTS.md`, `DESIGN.md`, or `prompt.md` should teach future agents.

If the audit finds no file changes, record that result. Silent non-use is a
protocol failure because the next session cannot distinguish "checked and
current" from "forgotten".

## Roadmaps only when needed

Some projects need more than a current-state handoff. When `docs/concept/` implies
several planned slices, ordered phases, release gates, research/eval gates, or
go/no-go checkpoints, `/sync-protocol` should create or refresh `ROADMAP.md`.

`ROADMAP.md` is the execution strategy: phases, slice sequence, gate criteria,
and stop conditions. `BUILD_STATE.md` remains the current handoff: active roadmap
position, last verified checkpoint, next step, blockers, and gate evidence. If
future planning starts accumulating in `BUILD_STATE.md`, that is a signal to move
the plan into `ROADMAP.md`.

Do not add a blank roadmap to every scaffold. Tiny projects should not pay for the
extra file. The protocol introduces it only when the work is too large to keep
`BUILD_STATE.md` lean.

## Desired behavior

The protocol should make continuity boring:

- A new session can read `AGENTS.md`, `BUILD_STATE.md`, and `prompt.md` and know
  whether the state is trustworthy.
- If `ROADMAP.md` exists, the session can distinguish long-range execution
  strategy from the current handoff.
- A completed slice leaves protocol files synchronized with behavior, or records
  why no sync was needed.
- Templates carry these rules so new projects inherit the discipline without
  relying on user memory.
