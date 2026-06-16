# Project AI Agent Guidelines (AGENTS.md)

This document establishes the canonical behavioral and operational boundaries for all AI coding assistants (Claude Code, Cursor, Antigravity, OpenCode, etc.) interacting with this repository.

> **AI Agent Directive:** You must read this file at the start of every session. Your actions must strictly adhere to the constraints defined below.

## 1. Operational Constraints (DO NOTS)

Based on empirical analysis of mature projects, these boundaries are absolute:

- **Never modify generated files**: Do not touch build outputs, compiled binaries, or auto-generated type definitions.
- **Never bypass type checking**: Do not use `any`, `unknown`, `@ts-ignore`, or unsafe casts to paper over broken types. Validate at runtime boundaries instead.
- **Never commit secrets**: Do not hardcode API keys, temporary tokens, or local `.env` values into tracked files.
- **Never leave debug artifacts**: Do not leave `console.log()` outputs, print statements, or one-off script modifications in finalized commits. Use structured loggers (e.g., `[ClassName] prefix`).
- **Never blindly override business logic**: Derive values in the correct use-case layer. Do not add business computation in proxy/routing layers.

## 2. Mandatory Validation Workflow

Before finalizing any slice of work, you must pass the following gates:

1. **Formatting & Linting**: Run `npm run lint` or the equivalent linter for this project.
2. **Type Checking**: Run strict type checks (e.g., `tsc --noEmit`).
3. **Unit Tests**: Run the associated test suite.
4. **Build Integrity**: Ensure the build command succeeds.

## 3. Architecture & Navigation

- **docs/concept/**: Contains the strategic vision, architectural blueprints, and `DESIGN.md`. Read these to understand the _intent_ before writing implementation logic.
- **Layered Guidance**: Subdirectories may contain their own localized `AGENTS.md` (e.g., `src/components/AGENTS.md`). In conflicts, the most deeply nested `AGENTS.md` takes precedence for that folder.
- **Separation of Concerns**: Visual design tokens and UI rationale are managed strictly in `DESIGN.md`. Do not invent UI tokens; use existing ones.

## 4. State Management (`BUILD_STATE.md`)

- If you are interrupted or experiencing token exhaustion, you MUST update `BUILD_STATE.md` with:
  1. What was just completed.
  2. The current exact state (broken tests, partial implementations).
  3. The immediate next step for the next agent session.
