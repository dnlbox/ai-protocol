# Build State

Agent working area: the agents own this file, the user does not maintain it. A
fresh session reads it top to bottom, then follows the start protocol in
`prompt.md`. Keep it lean: prevention beats cleanup.

Rules:

- `Now` is replaced every checkpoint, never appended to. It is the single source
  of "where we are". If it is longer than a screen, it is wrong.
- `Decisions` and `Session log` are append-only and terse: one line each. The
  full detail lives in git, not here.
- Run `/consolidate-state` when `Now` exceeds one screen, logs sprawl, git/test
  reality contradicts state, a workspace Components table drifts, or three
  shipped slices have accumulated since the last archive. Completed milestones
  collapse to one-line summaries in `Archive`, and contradictions are reconciled
  against git and the test state.

## Now

- Milestone:
- Last verified checkpoint:   (commit + what is green)
- Next step (start here):
- Blockers:

## Decisions

<!-- one dated line each: "YYYY-MM-DD: chose X over Y because Z" -->

## Session log

<!-- one terse line per finished slice: "YYYY-MM-DD: slice N done + verified" -->

## Archive

<!-- completed milestones collapsed to one line each; git holds the full history -->
