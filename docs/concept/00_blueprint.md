# Project Blueprint: The Self-Organizing Agentic Workspace

## Vision

The ultimate vision is to create a seamless, replicable project structure that naturally supports and orchestrates loop-based AI agent operations. When starting a new project, developers should be able to instantly drop in a standardized directory and file structure that primes any supported AI agent harness (e.g., Claude Code, Antigravity, OpenCode, Codex, VSCode) for maximum efficiency and context awareness.

By standardizing how we communicate intent to AI tools, we aim to drastically reduce token waste, prevent recursive loop traps (going back and forth on the same feature), and maintain state perfectly even across session breaks.

## Core Architectural Components

To achieve this, the workspace will center around the following foundational files:

1. **`docs/concept/`**: The strategic brain of the project. Contains the long-term vision, ideation, and architectural blueprints. Agents read this to understand the _why_ before they figure out the _how_.
2. **`AGENTS.md`**: The behavioral rulebook. A single, standardized file that details exact environmental constraints, coding styles, prohibited actions, and workflow nuances.
3. **`DESIGN.md`**: The visual identity rulebook. A hybrid of machine-readable design tokens (YAML) and human-readable rationale (Markdown) that gives agents a persistent, structured understanding of the design system.
4. **Harness-Specific Configs**: E.g., `.gemini/settings.json`, `.cursorrules`, or similar configurations that point the specific agent tool to prioritize `AGENTS.md` as its primary context.
5. **`prompt.md`**: The dynamic kickstart. When a session begins, this file acts as the explicit immediate instruction set to get the agent self-organizing the next slice of work.
6. **`BUILD_STATE.md`**: The state machine. A living document tracking exact progress, completed slices, current bugs, and next steps. If a session breaks or tokens exhaust, the next agent reads this file to seamlessly resume operations without losing context.

## The Ideal Workflow

1. **Scaffold**: Copy this core structure into a new repository.
2. **Describe**: Articulate the project's goals inside `docs/concept/`.
3. **Kickstart**: Provide initial directives in `prompt.md`.
4. **Operate**: The agent reads the context, adheres to `AGENTS.md` constraints, executes the work, and continuously updates `BUILD_STATE.md`.
5. **Resume**: If interrupted, the agent picks up exactly where it left off using `BUILD_STATE.md`.
