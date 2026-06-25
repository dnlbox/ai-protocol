# Session kickstart (workspace)

Static, do not edit per session. What to build lives in `docs/concept/` (intent);
current state lives in `BUILD_STATE.md` (the agent working area). This is a
workspace scaffold, so the first job is to locate the level you are working at.

## Start protocol

1. Find your contract: the nearest `AGENTS.md` above your working path. If it is
   this workspace `AGENTS.md`, you are coordinating across children. If it is a
   child's, you are building that child: follow the child's `prompt.md` and treat
   the rest of this file as context only.
2. Read this `AGENTS.md`, then inventory `.agents/` so workspace skills are
   available. A child's skills compose on top when work turns to that child.
3. Read `BUILD_STATE.md`. Reconcile `Now` and the `Components` table against
   reality (each child's `git log --oneline -10` and test state). Fix them before
   doing anything else. If the file is over budget, run `/consolidate-state` first.
4. To work on a child: make it the active scope, read its `AGENTS.md` and
   `BUILD_STATE.md`, exercise its last checkpoint to confirm it is real, then
   continue from its `Now`. Record intent before the slice; verify and checkpoint
   after. Never end a child on a broken tree.
5. Cross-cutting work stays at the workspace: stage it child by child, each verified
   against its own gates, and update the `Components` table when a child's state
   moves.

To (re)specialize the protocols after editing `docs/concept/`, run
`/sync-protocols`, then clear the session and start again from this file.
