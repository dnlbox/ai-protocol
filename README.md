# AI Protocol

This is a pragmatic experiment in managing AI-assisted software projects. It attempts to solve the friction I keep hitting when switching between different AI harnesses or starting fresh repositories. 

## The Problem

Right now, we suffer from the "it works in my harness" problem. If you start a project in Cursor, switch to Claude Code, and then try Antigravity, the AI loses its mind. The context is broken. This happens because we rely on hidden global system prompts and editor-specific settings to teach the AI how we like to work.

We also have a scaffolding problem. Most CLI tools force you to pick a technology stack (Next.js, FastAPI, Rust) before you even know what the product is. We lock ourselves into architectural decisions before the requirements exist.

## The Philosophy

This protocol introduces two shifts in how we start projects.

First, we vendor AI behavior at the project level. Just like `package.json` tracks code dependencies so any developer can run `npm install`, this protocol places the AI's operational rules directly inside the repository. Any agent that boots up in this folder gets the exact same capabilities, constraints, and context.

Second, we force the concept phase. We do not scaffold frameworks. We scaffold a reasoning environment where the AI is forced to understand the product before it is allowed to write code.

## The Lifecycle

If you want to try this out, kickstart a project:
```bash
bash <(curl -s https://raw.githubusercontent.com/dnlbox/ai-protocol/main/kickstart.sh) my-project
```
Or via degit: `npx degit dnlbox/ai-protocol/template my-project`

Here is how the workflow operates.

### Stage 1: The Concept Phase
You start in `docs/concept/`. There is no source code. You write out the problem statement, user journeys, and constraints in plain markdown. You run theoretical pen tests with the AI. You poke holes in the idea. The AI acts as a sounding board, not a typist.

### Stage 2: Lock-in
When the concept is solid, you run the `/sync-protocols` command. The AI reads the unstructured concept docs and deduces the most optimal stack for those specific constraints. It then compiles the `AGENTS.md` file, locking in the technical toolchain, the validation gates (how we test), and the operational rules.

### Stage 3: Building
Now you build. You write prompts to kick off slices of work. The protocol dictates the mechanics. The AI writes code, runs the validation gates defined in `AGENTS.md`, and self-heals when tests fail. 

Crucially, it uses `BUILD_STATE.md` as a persistent save state. If a session crashes, an API token exhausts, or context window fills up, you just start a new session. The incoming agent reads the state file, checks the git log, and picks up exactly where the dead session left off. 

### Stage 4: Ejecting
Eventually, the project matures. The initial concept documents become outdated. You can safely eject from this pure conceptual state. You rely heavily on standard tests and CI/CD pipelines. The `.agents/` folder and `AGENTS.md` just become a canonical onboarding guide for new AI agents entering the codebase.

## Target Audience

This is explicitly for greenfield projects. Do not try to backfill this rigor into legacy monoliths. Retroactively writing concept documentation to satisfy an agentic workflow rarely pays off.

This workflow cut down the friction in my own daily operations, but it is an ongoing experiment. Try it out, pull it apart, and see where it breaks for you.
