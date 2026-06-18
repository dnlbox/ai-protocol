# ai-protocol

**Start with a concept, not a stack.**

An agnostic agentic reasoning environment: a small, standardized set of files you
drop into a new repository so that any AI coding agent (Claude Code, Codex, Cursor,
Gemini / Antigravity, opencode) boots up with the same context, the same
constraints, and the same memory.

Most AI-assisted projects begin by choosing a framework, then asking the agent to
build a feature. This flips that. You describe *what* you are building in plain
markdown; the agent infers the *how* (the stack, the toolchain, the validation
gates) and writes it down where every future session can read it.

## The idea

The expensive failures in AI-assisted work happen when you build before the
requirements are broken down. Halfway through, you are switching libraries or
rewriting core logic. So the protocol pushes the hard thinking to the front.

You spend your time in `docs/concept/`. The agent compiles that intent into a
contract it can execute against, then builds in small, verified slices, surviving
crashes, token exhaustion, and context resets without losing its place.

Two layers, and the split is the whole point:

- A **universal baseline** that never changes: the guardrails, the workflow, the
  continuity rules.
- A **project layer** compiled from your concept: the stack, the commands, the
  gates. A web app, an ML pipeline, a Unity game, and a Rust binary each get a
  layer that fits them, off the same baseline.

## Quickstart

```bash
# zero-dependency, works anywhere bash + git exist
bash <(curl -s https://raw.githubusercontent.com/dnlbox/ai-protocol/main/kickstart.sh) my-project

# or, if you already use node
npx degit dnlbox/ai-protocol/template my-project
```

Then four moves:

1. **Describe.** Write what you want to build into `docs/concept/`. Unstructured
   is fine: dump everything in your head.
2. **Compile.** Ask your agent to run `/sync-protocols`. It reads your intent and
   locks the stack into `AGENTS.md` (and your design tokens into `DESIGN.md`).
3. **Build.** Point a fresh session at `prompt.md`. The agent breaks the concept
   into verified slices and tracks progress in `BUILD_STATE.md`.
4. **Resume.** If a session dies, the next one reads `BUILD_STATE.md` and
   `git log`, then continues exactly where it stopped.

## What is in the box

| File | Role |
| ---- | ---- |
| `docs/concept/` | The source of truth: your intent, maintained by hand. |
| `AGENTS.md` | The contract every agent reads first: universal baseline plus a compiled project layer. |
| `DESIGN.md` | Design tokens and rationale, for projects with a UI. |
| `BUILD_STATE.md` | The save state: where we are, what is next, how it was verified. |
| `prompt.md` | The static session kickstart. |
| `.agents/skills/` | Vendored skills, committed, so every harness and every clone gets the same capabilities. |

Three engine skills ship with it: `sync-protocols` (compile concept into contract),
`consolidate-state` (keep the save state lean), and `find-skills` (vendor new
capabilities into the repo).

## Why it survives long runs

The mechanics are the point. Because the protocol encodes how to slice work, how to
get back to green when a check fails, and how to restart cleanly when the context
window fills, the execution phase becomes mostly mechanical. Every slice ends on a
clean, validated checkpoint, so the tree is never more than about an hour from a
green commit. You put the deliberate work into the concept, then let the agent run
the build.

## Who it is for

Greenfield projects. Backfilling concept docs and state tracking into a large,
moving codebase rarely pays off. If you are starting fresh, this is for you.

## This is an experiment

I built this to cut the friction in my own workflow, and I am sharing it to learn
how it breaks for other people. If you try it, I want to hear what worked and what
did not. Open an [issue](https://github.com/dnlbox/ai-protocol/issues) with a rough
edge, a result, or an idea.
