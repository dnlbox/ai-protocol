# Playtest: Lumen (a Unity game)

A worked example of the protocol applied to a project that looks nothing like a
web app. It captures the state right after planning: the protocol files are
specialized to the stack and the project is ready to start building.

## The journey this captures

1. Scaffold the protocol into a fresh repo (the six areas plus the engine skills).
2. Write your ideas into `docs/concept/`. Here that is a single, deliberately
   unstructured `00_vision.md` brain-dump, no required format.
3. Run `/sync-protocols`. Without touching the universal baseline, it reads the
   concept and fills the Project Specifics of `AGENTS.md` and `DESIGN.md`,
   recommends stack skills, and seeds `BUILD_STATE.md`'s first `Now`.
4. Clear the session (or start a new one) and point only at `prompt.md`. From
   there the protocol breaks the concept into verified slices and keeps the
   project-specific information current as it builds.

This directory is the snapshot at the end of step 3: planned and ready to build.
The next session would start executing slice 1 from `BUILD_STATE.md`'s `Now`.

## What to look at

- `docs/concept/00_vision.md`: the raw input (messy on purpose).
- `AGENTS.md`: the baseline is byte-identical to a fresh scaffold; only Project
  Specifics changed, into a Unity toolchain (no `tsc`, `typecheck` dropped), a
  validation gate that is an observed playtest rather than a command, and stack
  rules inferred from the brain-dump (`.meta` files, scene-merge discipline).
- `DESIGN.md`: reshaped from web CSS tokens into a game art bible (cool nordic
  palette, one warm lantern accent).
- `BUILD_STATE.md`: seeded with the first milestone and next step.
