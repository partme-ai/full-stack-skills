<div align="center">

# OpenSpec-Skills (Alpha)

**Agent Skills for OpenSpec Spec-Driven Development**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-15-orange)
![Plugins](https://img.shields.io/badge/Plugins-3-brightgreen)

</div>

## Introduction

**OpenSpec-Skills** is an open-source Agent Skills collection for [OpenSpec](https://github.com/Fission-AI/OpenSpec) — the fluid, iterative spec-driven development framework for AI coding assistants. It provides **15 skills** in **3 plugin categories**: environment setup (install, init, update), core OPSX workflow (explore, new, continue, ff, apply, verify, archive), and optional/advanced (sync, bulk-archive, onboard, schema, config).

This repository participates in the **product** and **development** stages of the "requirements -> deployment" pipeline. For pipeline mapping and skills ecosystem, see [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) and [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md).

> **Note:** This project is in Alpha. Feedback is welcome.

## What are Skills?

Skills are folders of descriptions and resources that agents load on demand. They teach the agent to run structured workflows — e.g. starting a change, creating artifacts, implementing tasks, verifying completeness, and archiving.

### More information

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills Specification](https://agentskills.io/)

## About this repository

**OpenSpec-Skills** provides Agent Skills that implement the OpenSpec OPSX workflow so you can use explore, new, continue, ff, apply, verify, archive (and optional sync, bulk-archive, onboard, schema, config) from Claude Code, Cursor, or other Agent Skills-capable tools.

### Core features

- **Open source**: Apache 2.0; follows the Agent Skills Specification.
- **15 skills**: Full OpenSpec OPSX workflow plus environment setup and optional/advanced features.
- **3 plugins**: openspec-env (3 skills), openspec-core (7 skills), openspec-optional (5 skills).

### Project layout

```
openspec-skills/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── openspec-install/
│   ├── openspec-initial/
│   └── ...                     # 15 skills
├── spec/
│   └── agent-skills-spec.md
├── template/
│   └── SKILL.md
├── README.md
└── README_CN.md
```

**Plugin categories**

| Plugin           | Skills | Description                                                              |
|------------------|--------|--------------------------------------------------------------------------|
| openspec-env     | 3      | install, initial, update                                                 |
| openspec-core    | 7      | explore, new, continue, ff, apply, verify, archive                      |
| openspec-optional| 5      | sync, bulk-archive, onboard, schema, config                             |

## Installation and environment

Before using the OpenSpec workflow, prepare the environment:

1. **Install OpenSpec CLI** — Use skill **openspec-install** (or run `npm install -g @fission-ai/openspec@latest`). Supports npm, pnpm, yarn, bun, nix.
2. **Initialize the project** — Use skill **openspec-initial** (or run `openspec init`). Supports 20+ AI tools via `--tools`.
3. **Update after upgrade** — Use skill **openspec-update** (or run `openspec update`) after upgrading the CLI.

## Quick start

### Supported agents

- Claude Code, Cursor, Windsurf, GitHub Copilot, Cline, CodeBuddy, Codex, Continue, Gemini, RooCode, Trae, and [20+ more](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md).

### Using in Claude Code

**1. Register marketplace**

```bash
/plugin marketplace add https://github.com/partme-ai/openspec-skills.git
```

Or: `/plugin marketplace add partme-ai/openspec-skills`

**2. Install plugins**

```bash
/plugin install openspec-env@openspec-skills
/plugin install openspec-core@openspec-skills
/plugin install openspec-optional@openspec-skills
```

**3. Use skills**

In conversation, ask for OpenSpec steps — e.g. "Install OpenSpec", "Initialize OpenSpec in this project", "Explore ideas for auth improvements", "Start a new change for dark mode", "Fast-forward all artifacts", "Implement the tasks", "Verify and archive".

### OpenSpec environment

To use the full OpenSpec OPSX flow, install the CLI and initialize:

```bash
npm install -g @fission-ai/openspec@latest
openspec init --tools claude,cursor
```

Then use the OPSX commands: `/opsx:explore`, `/opsx:new`, `/opsx:ff`, `/opsx:apply`, `/opsx:verify`, `/opsx:archive`.

## Plugins and skills

### openspec-env

**Install:** `/plugin install openspec-env@openspec-skills`

- `openspec-install` — Install the OpenSpec CLI globally (npm/pnpm/yarn/bun/nix). *Corresponds to: npm install -g @fission-ai/openspec.*
- `openspec-initial` — Run `openspec init` to initialize a project (create openspec/, configure AI tools). *Corresponds to: openspec init.*
- `openspec-update` — Run `openspec update` to regenerate tool configs after CLI upgrade. *Corresponds to: openspec update.*

### openspec-core

**Install:** `/plugin install openspec-core@openspec-skills`

- `openspec-explore` — Think through ideas, investigate problems, clarify requirements. *Corresponds to: /opsx:explore.*
- `openspec-new` — Start a new change (create change folder and metadata). *Corresponds to: /opsx:new.*
- `openspec-continue` — Create the next artifact based on the dependency graph. *Corresponds to: /opsx:continue.*
- `openspec-ff` — Fast-forward: create all planning artifacts at once. *Corresponds to: /opsx:ff.*
- `openspec-apply` — Implement tasks, writing code and checking off items. *Corresponds to: /opsx:apply.*
- `openspec-verify` — Validate implementation matches artifacts (completeness, correctness, coherence). *Corresponds to: /opsx:verify.*
- `openspec-archive` — Archive a completed change, merging delta specs into main. *Corresponds to: /opsx:archive.*

### openspec-optional

**Install:** `/plugin install openspec-optional@openspec-skills`

- `openspec-sync` — Sync delta specs to main without archiving (for long-running changes). *Corresponds to: /opsx:sync.*
- `openspec-bulk-archive` — Archive multiple completed changes at once, handling conflicts. *Corresponds to: /opsx:bulk-archive.*
- `openspec-onboard` — Guided tutorial through the complete workflow using real code. *Corresponds to: /opsx:onboard.*
- `openspec-schema` — Create and manage custom workflow schemas (init, fork, validate, which). *Corresponds to: openspec schema.*
- `openspec-config` — Project configuration (context, per-artifact rules, default schema). *Corresponds to: openspec/config.yaml + openspec config.*

## Acknowledgements

This skills collection is built for and aligned with [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec). We thank the OpenSpec project and its contributors.

## Disclaimer

These skills are for demonstration and education. Validate behavior in your own environment before relying on them for critical work.
