# Build State (workspace)

Agent working area for the workspace: the agents own this file, the user does not
maintain it. A coordinating session reads it top to bottom, then the relevant
child's `BUILD_STATE.md`. Keep it lean. Children own their own state; this file
never duplicates their detail.

Rules:

- `Now` is replaced every checkpoint, never appended to. It holds the workspace's
  current cross-cutting focus, not any child's internals.
- `Components` is a live dashboard: one line per child, reconciled against that
  child's git/tests. Detail lives in the child's `BUILD_STATE.md`, not here.
- `Decisions` and `Session log` are append-only and terse: one line each. The full
  detail lives in git.
- When the logs cross their budget, run `/consolidate-state`.

## Now

- Cross-cutting focus: [what the workspace is coordinating right now].
- Next step (start here): [the next cross-cutting action, or "pick a component"].
- Blockers:

## Components

At-a-glance map of child projects. The child's own `BUILD_STATE.md` is the detail.

| Component | Status | Last verified |
| --------- | ------ | ------------- |
| _example_ | scaffolded | — |

## Decisions

<!-- one dated line each: "YYYY-MM-DD: chose X over Y because Z" -->

## Session log

<!-- one terse line per finished cross-cutting slice -->

## Archive

<!-- completed milestones collapsed to one line each; git holds the full history -->
