# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Full-Stack-Skills is the **navigation hub and catalog** for 460+ Agent Skills across 42 independently installable packages. Originally a monorepo, all skills were migrated to individual repos in the [full-stack-skills](https://github.com/full-stack-skills) GitHub organization in June 2026. This repo now serves as:

- **Catalog**: README tables linking to all skill packages with install commands
- **Documentation**: Agent specs, platform guides, role definitions, ecosystem mappings
- **Quality gate**: CI workflows that review SKILL.md changes on PRs

There is no application code, build system, or test suite in this repo. It is a documentation-only repository.

## Repository Structure

```
full-stack-skills/
├── README.md              # Main catalog (Chinese) — skill tables, install commands, architecture
├── README.en.md           # English catalog
├── AGENTS.md              # Guidance for AI agents working in this repo (skill creation rules)
├── AGENTS_EN.md           # English version
├── AGENTS_PROMPT.md       # Role definitions and prompts for 50+ agent roles
├── ROLE_DEFINITIONS.md    # Structured role definitions with responsibilities and skill assignments
├── PLATFORM_GUIDE.md      # Platform matrix with install paths for all 43 platforms
├── QUICKSTART.md          # 5-minute marketplace setup guide
├── AWESOME_AGENT_SKILLS.md # Curated list of external agent skill collections
├── PLANNING_SKILL_CATEGORIES.md # Skill category planning and classification
├── SKILLS_INDEX.md        # Legacy index (paths reference old monorepo structure, now stale)
├── EVALUATION_REPORT.md   # Skill quality evaluation report
├── docs/                  # Detailed mapping and ecosystem documents
├── agents/                # Agent skill specs (agent-skills-spec.md, etc.)
├── spec/                  # Skill specification documents
├── media/                 # Screenshots and demo assets
└── .github/workflows/     # CI for SKILL.md quality review on PRs
```

## How Skills Are Installed

Skills are no longer in this repo. Users install from the individual package repos:

```bash
npx skills add full-stack-skills/vue-skills          # Install a full package
npx skills add full-stack-skills/vue-skills --skill vue3  # Install a single skill
```

Or via Claude Code's plugin system:
```
/plugin marketplace add partme-ai/full-stack-skills
```

## Ecosystem Map

| Repo | Role |
|------|------|
| **full-stack-skills** (this repo) | Catalog, docs, ecosystem mappings |
| [full-stack-skills/*](https://github.com/full-stack-skills) | 42 individual skill packages (vue-skills, tauri-skills, etc.) |
| [t2ui-skills](https://github.com/partme-ai/t2ui-skills) | PRD → ASCII UI translation, Stitch/Pencil design languages |
| [stitch-skills](https://github.com/partme-ai/stitch-skills) | Stitch design language → prototypes |
| [pencil-skills](https://github.com/partme-ai/pencil-skills) | Pencil design language → product diagrams (.pen) |
| [tauri-skills](https://github.com/partme-ai/tauri-skills) | Tauri cross-platform desktop/mobile development |

The pipeline stage → skill mapping is in `docs/pipeline-stage-to-skills.md`. External skill library discovery sources are in `docs/external-skills.md`.

## CI Workflows

Two GitHub Actions run on PRs that modify `**/SKILL.md` files:

1. **skill-review.yml** — Runs [tesslio/skill-review-and-optimize](https://github.com/tesslio/skill-review-and-optimize) to score SKILL.md quality and post AI-suggested improvements as a PR comment
2. **skill-optimize-apply.yml** — When a contributor comments `/apply-optimize` on a PR, commits the AI-suggested improvements directly to the branch

## When Working in This Repo

### Editing documentation
- Language convention: **Chinese** for README, comments, and commit messages. English versions exist as `*.en.md` or `*_EN.md` counterparts.
- README skill counts and package tables are the primary user-facing content — keep them accurate.
- `docs/repository-map.md` tracks discrepancies between what exists in-repo and what's in the marketplace (now mostly historical since migration).

### Creating or editing skills
Skills live in individual package repos now, not here. If you need to work on a skill:
1. Clone the relevant package repo (e.g., `git clone https://github.com/full-stack-skills/vue-skills`)
2. Skills follow the Agent Skills spec: `skills/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`)
3. SKILL.md must be under 500 lines; reference material goes in `references/`
4. `description` is the trigger mechanism — write it to describe *when* the skill activates, not just what it is

### Stale files
Several files reference the old monorepo structure and are no longer accurate:
- `SKILLS_INDEX.md` — references `skills/` paths that no longer exist
- `QUICKSTART.md` — references `.claude-plugin/marketplace.json` which was removed during migration
- `docs/repository-map.md` — describes pre-migration state (42 groups, 422 skills in-repo)

## Important Constraints

- License: Apache 2.0 (repo-level)
- `ruvector.db` and `agentdb.rvf` are generated artifacts (Ruflo code intelligence), not source files
- The `media/` directory contains demo screenshots referenced by README
- `.gitignore` excludes `.DS_Store`, `__pycache__/`, `.idea/`, `.vscode/`
