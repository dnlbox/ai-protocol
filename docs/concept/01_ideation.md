# Ideation Phase: Establishing the Canonical AI Workspace

## Objective

We are currently experiencing friction, token waste, and context loss when managing AI agents (like in `operio-studio`). To solve this, we are investigating more efficient ways to communicate intent, constraints, and project state to LLM-based coding assistants.

## Current Investigation Steps

1. **Analyze Mature Projects**: We are aggregating and analyzing how mature, established open-source projects organize their AI tooling.
2. **Benchmark Canonical Solutions**: We are collecting a dataset of top-starred GitHub repositories that have adopted the `https://agents.md/` standard. We will use advanced LLMs (like Anthropic Haiku and Google Gemini) to parse these files, bypassing rigid traditional ML clustering to extract nuanced intent, common rules, and generic constraints.
3. **Integrate DESIGN.md**: We are adding support for the `https://github.com/google-labs-code/design.md` specification to strictly separate visual identity (DESIGN) from behavioral constraints (AGENTS).
4. **Synthesize a Generic Structure**: Based on the benchmark data, we will build a generic project structure that natively supports cross-platform agent harnesses:
    - Claude Code
    - Antigravity
    - OpenCode
    - Codex
    - VSCode / Cursor
    - _Includes necessary harness settings (e.g., `.gemini/settings.json`) that explicitly point the agent to bootstrap its context from `AGENTS.md`._
5. **Develop Loop-Based Operations**: We are ideating a robust framework for loop-based agent operations. This involves designing the schema for a `BUILD_STATE.md` file (for state persistence) and `prompt.md` (for session kickoff) to work in tandem with the structural work defined in `docs/concept/`.

By grounding our architecture in empirical data from the top 100 `AGENTS.md` implementations, we ensure our approach is both canonical and battle-tested.
