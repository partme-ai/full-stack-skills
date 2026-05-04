# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Full-Stack-Skills is an open-source Agent Skills marketplace repository — a collection of 421+ skills across 42 groups covering frontend, backend, DevOps, design, documentation, and spec-driven development. Skills are packaged as `SKILL.md` files that Claude Code (and other Agent Skills-compatible platforms) loads on demand to extend its capabilities for specific tasks.

The repository serves dual roles:
- **Authoring environment**: Where skills are created, edited, and maintained following the [Agent Skills specification](https://agentskills.io/)
- **Marketplace source**: Published via `.claude-plugin/marketplace.json` for installation through Claude Code's `/plugin` system

Language convention (inherited from parent workspace): **Chinese** for documentation, comments, and commit messages.

## Skill Directory Structure

Skills follow a strict two-level grouping:

```
skills/<group>-skills/<skill-name>/SKILL.md
```

Each skill directory may optionally contain:
- `examples/` — usage examples
- `references/` — longer reference material (keeps SKILL.md under 500 lines)
- `scripts/` — executable automation scripts
- `assets/` — images, templates, and other resources
- `templates/` — code templates

### Naming Conventions

- **Skill directory**: `kebab-case` (e.g., `vue3`, `spring-boot`, `tauri-app-creator`)
- **SKILL.md**: Always uppercase, exact filename `SKILL.md`
- **Scripts**: `kebab-case.sh` with `#!/bin/bash` shebang, `set -e`, status to stderr, machine-readable output to stdout
- **Zip files**: Must match directory name exactly (`{skill-name}.zip`)

## SKILL.md Format

Every skill file requires YAML frontmatter with `name` and `description`:

```markdown
---
name: {skill-name}
description: {One sentence describing trigger conditions. Be specific so Claude can determine when to activate.}
---

# {Skill Title}

{Brief description of what the skill does and when to use it.}
```

Key frontmatter rules:
- `name` must match the directory name
- `description` is the primary trigger mechanism — Claude uses it to decide whether to load the skill. Write it to describe *when* to use the skill, not just what it is
- Keep SKILL.md under 500 lines; move reference material to `references/`

## Marketplace Configuration

The file `.claude-plugin/marketplace.json` defines which skills are published. Each plugin maps to a skill group:

```json
{
  "name": "full-stack-skills",
  "plugins": [
    {
      "name": "vue-skills",
      "description": "...",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/vue-skills/vue2",
        "./skills/vue-skills/vue3"
      ]
    }
  ]
}
```

**Important distinction**: `skills/` directory is the source of truth for what exists in the repo; `marketplace.json` is the source of truth for what is published. Currently 2 groups exist in-repo but are not published: `threejs-skills` (18 skills) and `vscode-skills` (4 skills). When adding new skills, update both the directory and marketplace.json together.

The `docs/repository-map.md` tracks all known discrepancies between the directory and marketplace.

## Cross-Platform Adapter (`fskill`)

The `adapters/` directory contains a standalone TypeScript CLI (`fskill`) that exports skills for 43 platforms. It converts the repo's `skills/<group>/<skill>/` structure into standard skill directories placed in each platform's expected path.

### Development Commands

```bash
# Install the CLI globally from the adapters directory
npm install -g ./adapters

# Or for local development
cd adapters && npm install && npm link

# Build TypeScript
cd adapters && npm run build

# Audit skill counts and integrity
fskill audit

# List all 43 supported platforms
fskill platforms

# Export skills for all platforms (dry-run first)
fskill convert --platform all --output ./adapters-output --dry-run
fskill convert --platform all --output ./adapters-output

# Export for a single platform
fskill convert --platform claude-code --output ./adapters-output

# Install to current project (defaults to .agents/skills/)
fskill install

# Install to specific platform with scope
fskill install --platform cursor --scope project
fskill install --platform antigravity --scope global
```

### Adapter source files:
- `adapters/src/index.ts` — CLI entry point
- `adapters/src/platform-registry.ts` — 43-platform path matrix
- `adapters/src/skills.ts` — skill discovery and audit logic

## Key Documentation Files

- `README.md` — Full project README (Chinese, with marketplace tables, installation guides, scenario-based install paths)
- `README_EN.md` — English README
- `AGENTS.md` — Guidance for AI agents working in this repo (skill creation rules, directory conventions, zip packaging)
- `AGENTS_EN.md` — English version of AGENTS.md
- `AGENTS_PROMPT.md` — Role definitions and agent prompts for 50+ roles (product manager, architect, developer, etc.)
- `ROLE_DEFINITIONS.md` — Structured role definitions with responsibilities, tools, and skill assignments
- `PLATFORM_GUIDE.md` — Complete platform matrix with install paths for all 43 platforms
- `QUICKSTART.md` — 5-minute marketplace setup guide for users forking this repo
- `PLANNING_SKILL_CATEGORIES.md` — Skill category planning and classification
- `docs/repository-map.md` — Canonical snapshot of repo structure vs. marketplace state
- `docs/skill-group-mapping.md` — Mapping of skills to groups
- `docs/pipeline-stage-to-skills.md` — Pipeline stage (requirements → design → dev → test → deploy) to skills mapping
- `docs/skills-ecosystem.md` — Overview of the broader skills ecosystem across related repos

## Adding a New Skill

1. Create `skills/<group>-skills/<skill-name>/SKILL.md` with proper frontmatter
2. Add optional subdirectories (`references/`, `scripts/`, `examples/`, `assets/`)
3. If the group plugin already exists in `marketplace.json`, append the skill path to its `skills` array
4. If it's a new group, add both the plugin entry in `marketplace.json` and update `docs/repository-map.md`
5. Run `fskill audit` to verify the skill is discoverable
6. Update README snapshot numbers if counts changed

## Important Constraints

- `skills/pencil-skills/docs/` is treated as supporting documentation, not a skill directory — excluded from conversion
- The `.gitignore` excludes `.DS_Store`, `__pycache__/`, `.idea/`, `.vscode/`
- License: Apache 2.0 (repo-level), but `skills/document-skills/{docx,pptx,pdf,xlsx}` are source-available, not open source
- Skills use progressive disclosure: SKILL.md should be concise, reference material goes in separate files
- Script paths in SKILL.md should use the absolute mount path format: `/mnt/skills/user/{skill-name}/scripts/{script}.sh`
