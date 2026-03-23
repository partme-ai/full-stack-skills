<div align="center">

# Speckit-Skills (Alpha)

**Agent Skills for Spec-Driven Development**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-13-orange)
![Plugins](https://img.shields.io/badge/Plugins-2-brightgreen)

</div>

## Introduction

**Speckit-Skills** is an open-source Agent Skills collection for **Spec-Driven Development**, aligned with [GitHub spec-kit](https://github.com/github/spec-kit) and [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills). **Part of the skills and content in this repository are derived from [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills).** It provides **13 skills** in **2 plugin categories**: core (install, init, check, then constitution → specify → clarify → plan → tasks → implement) and optional (baseline, analyze, checklist, taskstoissues).

This repository participates in the **product** and **development** stages of the「requirements → deployment」pipeline. For pipeline mapping and skills ecosystem, see [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) and [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md).

> **Note:** This project is in Alpha. Feedback is welcome.

## What are Skills?

Skills are folders of descriptions and resources that agents load on demand. They teach the agent to run structured workflows—e.g. creating a project constitution, writing a spec from natural language, generating a technical plan, breaking down tasks, and implementing from the plan.

### More information

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills Specification](https://agentskills.io/)

## About this repository

**Speckit-Skills** provides Agent Skills that implement the Spec Kit workflow so you can use constitution, specify, clarify, plan, tasks, and implement (and optional baseline, analyze, checklist, taskstoissues) from Claude Code, Cursor, or other Agent Skills–capable tools.

### Core features

- **Open source**: Apache 2.0; follows the Agent Skills Specification.
- **13 skills**: Install, init, check, then full Spec Kit workflow plus optional steps.
- **2 plugins**: speckit-core (9 skills), speckit-optional (4 skills).

### Project layout

```
speckit-skills/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── speckit-constitution/
│   ├── speckit-specify/
│   └── ...                     # 13 skills
├── spec/
│   └── agent-skills-spec.md
├── template/
│   └── SKILL.md
├── README.md
└── README_CN.md
```

**Plugin categories**

| Plugin          | Skills | Description                                      |
|-----------------|--------|--------------------------------------------------|
| speckit-core    | 9      | install, initial, check, constitution, specify, clarify, plan, tasks, implement |
| speckit-optional| 4      | baseline, analyze, checklist, taskstoissues     |

## Installation and environment

Before using the full Spec Kit flow (e.g. `.specify/` templates and slash commands), prepare the environment:

1. **Install Specify CLI** – Use skill **speckit-install** (or run `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`). Supports multiple OS, persistent or one-time (`uvx`), and corporate/restricted networks.
2. **Initialize the project** – Use skill **speckit-initial** (or run `specify init . --ai <agent>`). Supports multiple AI agents and `--script sh` / `--script ps`.
3. **Verify** – Use skill **speckit-check** (or run `specify check`) to confirm tools and agents are detected.

For multi-OS, multi-Agent, or corporate setups, see **speckit-install** and **speckit-initial** skill docs.

## Quick start

### Supported agents

- Claude Code, Cursor, Trae, Windsurf, GitHub Copilot, Continue, CodeBuddy, and others that support Agent Skills.

### Using in Claude Code

**1. Register marketplace**

```bash
/plugin marketplace add https://github.com/partme-ai/speckit-skills.git
```

Or: `/plugin marketplace add partme-ai/speckit-skills`

**2. Install plugins**

```bash
/plugin install speckit-core@speckit-skills
/plugin install speckit-optional@speckit-skills
```

**3. Use skills**

In conversation, ask for Spec Kit steps—e.g. “Create a project constitution”, “Write a spec for a photo album app”, “Generate a plan for Vue + SQLite”, “Break down into tasks”, “Implement from tasks.md”.

### Spec Kit environment

To use the full Spec Kit flow (e.g. `.specify/` templates and scripts), use **speckit-install** then **speckit-initial** (or run):

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init . --ai claude
```

Verify with **speckit-check** or `specify check`. For runtime-specific slash commands (Codex, Gemini, GitHub Copilot), see [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills) (`.claude/commands`, `.codex/`, `.gemini/`, `.github/`).

## Plugins and skills

### speckit-core

**Install:** `/plugin install speckit-core@speckit-skills`

- `speckit-install` – Install Specify CLI on the host (uv tool install or uvx; multi-OS, corporate/restricted network). *Corresponds to: install CLI.*
- `speckit-initial` – Run `specify init` in the project (pull `.specify/`, slash commands; multi-Agent, `--script sh`/`ps`). *Corresponds to: specify init.*
- `speckit-check` – Run `specify check` and interpret results (verify tools and agents). *Corresponds to: specify check.*
- `speckit-constitution` – Create or update project principles (`.specify/memory/constitution.md`).
- `speckit-specify` – Generate or update functional spec (what/why) from natural language.
- `speckit-clarify` – Resolve ambiguities in the spec (run before plan).
- `speckit-plan` – Produce technical plan (how, tech stack, architecture).
- `speckit-tasks` – Generate ordered task list from the plan.
- `speckit-implement` – Execute implementation from `tasks.md`.

### speckit-optional

**Install:** `/plugin install speckit-optional@speckit-skills`

- `speckit-baseline` – Generate spec from existing code (alternative entry).
- `speckit-analyze` – Cross-artifact consistency check (after tasks, before implement).
- `speckit-checklist` – Quality checklists for requirements/spec.
- `speckit-taskstoissues` – Turn tasks into issues (e.g. GitHub).

### Acknowledgements

Part of the code and skill definitions in this repository are derived from [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills). We thank the upstream project and its contributors.

### Disclaimer

These skills are for demonstration and education. Validate behavior in your own environment before relying on them for critical work.
