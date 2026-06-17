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

- Milestone: vertical slice, lantern movement plus one light puzzle in a single
  hand-painted scene, holding 60fps.
- Last verified checkpoint: none yet (fresh project; no Unity project created).
- Next step (start here): pin the Unity Editor version
  (`ProjectSettings/ProjectVersion.txt`), add the Unity `.gitignore` and Git LFS
  attributes for binary art, and a `BuildScript.Run` for headless
  StandaloneWindows64 builds. Then slice 1: lantern plus player movement in a test
  scene, behind an input-abstraction layer.
- Blockers: Unity version not yet chosen and pinned. FMOD audio and Switch input
  are deferred (later targets, not this slice).

## Decisions

- 2026-06-17: bootstrapped from `docs/concept/00_vision.md` by `/sync-protocols`.

## Session log

- 2026-06-17: scaffold initialized and specialized for the Unity stack.

## Archive

<!-- completed milestones collapsed to one line each; git holds the full history -->
