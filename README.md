# AI Protocol

When I start a new project now, I do not open with a prompt. I open with a blank concept folder.

This is a pragmatic experiment in building greenfield projects from a concept rather than from a chain of prompts. The code comes later: first you get the intent right, in plain markdown, where the agent can read it.

## The Problem

A chain of prompts feels productive. You ask an agent to "build a web app", it generates boilerplate, and you are moving within seconds.

Then the problems begins. Halfway through you realize the database was the wrong call. You switch libraries. You rewrite core logic. You spend more time correcting the agent's assumptions than building the product, all because the requirements were never broken down before the code started. Each prompt is a local decision with no shared plan behind it, so the project drifts.

## The Shift

This protocol flips the workflow. It is built on a simple thesis: if you do the rigorous thinking upfront in a concept document, you can largely hand off the execution to an AI agent.

You start with a blank concept folder. You write the problem statement and the constraints. You use the AI purely as a sounding board. You run theoretical pen tests and look for holes in your logic before a single line of code is written.

Because the protocol handles the mechanics of how work gets executed (slicing tasks, self-healing, and restarting exhausted sessions), the actual coding phase becomes mechanical. As a minor side effect, this also makes the project entirely harness agnostic—whether you boot up Cursor, Claude Code, or Antigravity, the agent reads the rules from the repo and gets to work.

## The Lifecycle

If you want to try this out, kickstart a project:

```bash
bash <(curl -s https://raw.githubusercontent.com/dnlbox/ai-protocol/main/kickstart.sh) my-project
```

Or via degit: `npx degit dnlbox/ai-protocol/template my-project`

Here is how the workflow operates.

### Stage 1: The Concept Phase

You start in `docs/concept/`. Spend real time here. There is no source code. You write out the problem statement, user journeys, and constraints in plain markdown. The AI acts as a sounding board to interrogate your design, not a typist to generate boilerplate.

### Stage 2: Lock-in

When the concept is solid, you run the `/sync-protocols` command. The AI reads the unstructured concept docs and proposes the most optimal stack for those specific constraints. It then compiles the `AGENTS.md` file, locking in the technical toolchain, the validation gates (how we test), and the operational rules.

### Stage 3: Building (The Mechanics)

This is where the protocol shines. The operational rules are not guesswork: the baseline was distilled from a benchmark of more than 60 `AGENTS.md` files across large open-source projects, then tightened into one lean contract. Because those rules are baked into the repository, execution becomes mostly mechanical. You just let the agent run.

The protocol dictates how to slice work and route each slice to the right model tier (a fast, cheap model for mechanical bulk, the deep model reserved for architecture and integration), how to self-heal failing tests, and how to cleanly restart when the context window exhausts. It uses `BUILD_STATE.md` as a persistent save state. If a session crashes, you start a new one. The incoming agent reads the state file, checks the git log, and picks up exactly where it left off.

### Stage 4: Ejecting

Eventually, the project matures. The initial concept documents become outdated. You can safely eject from this pure conceptual state. You rely heavily on standard tests and CI/CD pipelines. The `.agents/` folder and `AGENTS.md` just become a canonical onboarding guide for new AI agents entering the codebase.

## Target Audience

This is explicitly for greenfield projects. Do not try to backfill this rigor into legacy monoliths. Retroactively writing concept documentation to satisfy an agentic workflow rarely pays off.

This workflow cut down the friction in my own daily operations, but it is an ongoing experiment. Try it out, pull it apart, and see where it breaks for you.
