# Build State

Agent working area: the agents own this file, the user does not maintain it. A
fresh session reads it top to bottom, then follows the start protocol in
`prompt.md`. Keep it lean: prevention beats cleanup.

Rules:

- `Now` is replaced every checkpoint, never appended to. It is the single source
  of "where we are". If it is longer than a screen, it is wrong.
- `Decisions` and `Session log` are append-only and terse: one line each. The
  full detail lives in git, not here.
- When the logs cross their budget, run `/consolidate-state` (or it runs from the
  start protocol): completed milestones collapse to a one-line summary in
  `Archive`, and contradictions are reconciled against git and the test state.

## Now

- Milestone: nesting is first-class. Baseline defines workspace/child semantics;
  README positions the protocol against the "loop" term; the separate workspace
  scaffold has been retired.
- Last verified checkpoint: docs-only change; baselines verified identical across
  `AGENTS.md` and `template/AGENTS.md` (above the Project Specifics marker) bar
  the shared new Nesting section.
- Next step (start here): continue folding real workspace exercise feedback into
  the root protocol and production `template/`.
- Blockers: none.

## Decisions

<!-- one dated line each: "YYYY-MM-DD: chose X over Y because Z" -->
- 2026-06-25: Nesting via composition + lazy skills, not symlinks or blanket
  vendoring. Workspace holds generic skills, child holds specific; a child sees
  both (child wins on clash); workspace lazy-loads a child's skills only when work
  turns to it. Implemented as protocol semantics so it holds on any harness.
- 2026-06-25: Tested a separate workspace template beside `template/`, then later
  retired it because the extra template path did not carry its weight.
- 2026-06-25: Positioned ai-protocol relative to "loop": it is the concept +
  contract + state layer a loop runs against, not an agent loop or interval runner.

## Session log

<!-- one terse line per finished slice: "YYYY-MM-DD: slice N done + verified" -->
- 2026-06-25: moved into forge workspace; added nesting baseline + README "loop"
  and nesting sections.

## Archive

<!-- completed milestones collapsed to one line each; git holds the full history -->
