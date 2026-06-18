# AI Protocol: The Agnostic Agentic Reasoning Environment

This repository establishes a completely new paradigm for scaffolding and managing AI-assisted software projects. Instead of forcing a developer to choose a framework (like Next.js, FastAPI, or Django) before knowing exactly what they are building, this protocol scaffolds an **Agnostic Agentic Reasoning Environment**.

It forces you to define the product concept first, and allows your AI Staff Architect to decide the stack later.

## 🚀 Kickstarting a New Project

There are two ways to scaffold a new project using this environment.

### Option 1: The Zero-Dependency Bash Script (Recommended)
This approach works everywhere `bash` and `git` are installed, providing the complete guided experience.
```bash
bash <(curl -s https://raw.githubusercontent.com/dnlbox/ai-protocol/main/kickstart.sh) my-new-project
```

### Option 2: Using `npx degit`
If you already use Node.js and want to instantly clone just the template files without the wrapper script, you can use `degit`.
```bash
npx degit dnlbox/ai-protocol/template my-new-project
```

---

## 🧠 The Philosophy

### 1. Concept Before Stack
The most common mistake when starting an AI-assisted project is prematurely selecting a technology stack. Developers scaffold a Next.js app, then ask the AI to build a feature. We flip this: you write the concept in unstructured markdown, and the AI deduces the most optimal stack for your specific constraints.

### 2. Vendoring AI Skills at the Project Level
Many developers configure their AI tools (like custom instructions or MCP servers) globally in their editor. This creates the "it works in my harness" problem, where a project builds fine on one machine but fails for another collaborator because their AI lacks the required local context. 

This protocol **vendors AI skills into the project directory itself** (inside `.agents/skills/`). Every agent, regardless of the harness (Claude Code, Antigravity, Cursor, etc.), gets the exact same capabilities and constraints when it boots up in this repository.

## 🎯 Target Audience

This protocol is explicitly designed for **greenfield projects**. 

Legacy or highly mature projects will not benefit significantly from this protocol because retroactively backfilling concept documentation and state tracking into a moving target is rarely successful. If you are starting fresh, this is for you.

## 🛠 The Stages of Use

### Stage 1: Before Build (The Concept Phase)
After running the kickstart command, your project will have a `docs/concept/` folder. This is your playground. Write down what you want to build, the user journeys, and the non-functional constraints.

Once your concept is documented, ask your AI to run the `/sync-protocols` command. The AI will read your intent and lock in a technical stack by populating the Project Specifics section of your `AGENTS.md`.

### Stage 2: Building (The Execution Phase)
As you build, `AGENTS.md` acts as the universal rulebook enforcing validation gates (like linting and testing). Work should be delegated to subagents based on their capability tier:
* **Deep (Main Loop):** Architecture, integration, and final decisions.
* **Standard (Subagent):** Well-specified implementation against a clear contract.
* **Fast (Subagent):** Mechanical bulk work, refactors.
* **Explore (Subagent):** Read-only reconnaissance.

### Stage 3: Ejecting (The Maturation Phase)
When the project matures, the initial `docs/concept/` files might become outdated. You can safely "eject" from this pure conceptual state by relying heavily on standard tests and CI/CD. The `.agents/` folder and `AGENTS.md` can remain as a canonical guide for new AI agents entering the codebase.

## ⚙️ Self-Mechanics (The Gold)

The true power of this protocol lies in the **agent lifecycle rules** defined in `AGENTS.md`.

* **Sudden Death Survival:** AI sessions can crash, API tokens can exhaust, and context windows can fill up. To solve this, agents use `BUILD_STATE.md` as their persistent "save state." 
* **State Resumption:** Whenever a new session starts, the agent is instructed to read `AGENTS.md`, inventory the `.agents/` directory, read `BUILD_STATE.md`, and check `git log`. This allows it to instantly resume operations exactly where the previous session died.
* **Verifiable Checkpoints:** Agents are strictly forbidden from expanding scope or ending a session on a broken tree. Every implementation slice must end with a clean, validated checkpoint.
