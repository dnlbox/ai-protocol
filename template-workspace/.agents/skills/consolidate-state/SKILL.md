---
name: consolidate-state
description: Keep BUILD_STATE.md lean and self-consistent. Use when BUILD_STATE.md has grown large, Now exceeds one screen, logs sprawl, git/test reality contradicts Now, a workspace Components table drifts, or three shipped slices have accumulated since the last archive. Mirrors consolidate-memory, but for the agent working state.
---

# Consolidate State

`BUILD_STATE.md` is append-prone: over a long project the logs sprawl and the
`Now` block drifts out of sync with what actually happened. This skill is the cure.
Prevention lives in the execution protocol (every slice replaces `Now` and adds one
terse log line); this skill is the periodic deep clean.

## When it runs

- Manually, when you notice rot.
- Automatically, when the start protocol in `prompt.md` finds the file over budget
  or self-contradictory.
- As a closeout hygiene trigger after three shipped slices since the last archive.
- Whenever `git log`, validation state, or a workspace Components dashboard
  contradicts `Now`.

## Procedure

1. Reconcile `Now` against reality: `git log --oneline -20`, the test state, and
   the running app. Rewrite `Now` so it matches what is actually true and points at
   one clear next step. Resolve contradictions in favour of reality, not the stale
   text.
2. Compact the logs: collapse completed milestones in `Decisions` and `Session log`
   into a one-line summary each, moved to `Archive`. The full detail already lives
   in git, so do not preserve it here.
3. If `Now` is carrying several future slices, ordered phases, or go/no-go gates,
   do not compress that plan into state. Move it to an existing `ROADMAP.md`, or
   flag that `/sync-protocols` should create one, then leave `BUILD_STATE.md`
   pointing at the active roadmap position.
4. Verify the budget: `Now` is at most a screen; `Decisions` and `Session log` hold
   only the current milestone's lines; any older finished work has a one-line
   `Archive` entry.
5. Present the before/after as a diff and get approval before writing.

## Rules

- Never invent history. If git and the file disagree, git wins.
- Keep one line per archived milestone, not per slice.
- Do not touch the protocol files (that is `sync-protocols`).
- This is housekeeping, not progress: do not change the planned next step except to
  correct it against reality.
