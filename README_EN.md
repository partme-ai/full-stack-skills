# Full Stack Skills (Alpha)

A grouped Agent Skills repository for Claude Code, Claude.ai, and compatible Agent Skills ecosystems.

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skill%20Docs](https://img.shields.io/badge/SKILL.md-421-orange)
![Skill%20Groups](https://img.shields.io/badge/Groups-42-blue)
![Marketplace%20Plugins](https://img.shields.io/badge/Plugins-40-brightgreen)

> **Note:** This repository is maintained as a grouped skills catalog. The current documentation follows the actual `skills/` directory layout and `.claude-plugin/marketplace.json` rather than older category-based packaging.

## What are Skills?

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete repeatable tasks in a reusable way, whether that means documentation workflows, frontend implementation, system design, testing, or delivery automation.

### More Information

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Agent Skills specification](https://agentskills.io/)

## About This Repository

This repository is PartMeAI’s grouped Agent Skills catalog. The current repository snapshot contains **42** skill-group directories and **421** `SKILL.md` files. `.claude-plugin/marketplace.json` currently publishes **40** plugins with **410** skill paths.

The main repo now covers frontend, backend, mobile, cross-platform development, testing, DevOps, documentation, OCR, Tauri, Stitch, Pencil, T2UI, OpenSpec, and Spec Kit workflows.

### Repository Snapshot

| Metric | Current Value |
|---|---:|
| Skill-group directories under `skills/` | 42 |
| `SKILL.md` files on disk | 421 |
| Plugins in `.claude-plugin/marketplace.json` | 40 |
| Published skill refs in Marketplace | 410 |
| Repo-only groups not published | 2 |

### Coverage Map

| Domain | Representative Groups | Scope |
|---|---|---|
| Frontend and UI | `vue-skills`, `react-skills`, `angular-skills`, `svelte-skills`, `antd-skills`, `vue-ui-skills`, `build-skills` | Frameworks, component libraries, build systems, UI implementation |
| Backend and cross-platform | `spring-skills`, `nodejs-skills`, `python-skills`, `go-skills`, `electron-skills`, `tauri-skills`, `uniapp-skills`, `flutter-skills` | Service development, desktop, mobile, hybrid delivery |
| Engineering delivery | `dev-utils-skills`, `ddd-skills`, `testing-skills`, `devops-skills`, `docker-skills`, `database-skills`, `nvm-skills` | Project scaffolding, architecture, test strategy, release workflows |
| Design and documents | `design-skills`, `document-skills`, `ocrmypdf-skills`, `drawio-skills`, `ascii-skills` | Design execution, documentation, OCR, diagramming, text visuals |
| Spec and design systems | `speckit-skills`, `openspec-skills`, `t2ui-skills`, `stitch-skills`, `pencil-skills` | Spec-driven delivery, UI generation, design workflows, structured handoff |
| Shared support | `social-skills`, `teaching-skills`, `utility-skills` | Communication, education, utility workflows |

### Publication Status

- `threejs-skills` exists in the repository with 18 skills and is not currently published in Marketplace.
- `vscode-skills` exists in the repository with 4 skills and is not currently published in Marketplace.
- `document-skills` has 5 skill directories on disk, while Marketplace still references 9 entries, including missing paths for `docx`, `pptx`, `pdf`, and `xlsx`.
- `tauri-skills` has 52 skill directories on disk, while Marketplace currently publishes 51 entries; `tauri-app-updater` remains repo-only.

### Recommended Reading Path

- **Start with repository scope**: read this README together with `docs/repository-map.md` to understand structure, publication state, and catalog drift.
- **Navigate by skill group**: if you already know the technical domain, move directly into `docs/skill-group-mapping.md` and the relevant `skills/<group>-skills/` subtree.
- **Navigate by delivery stage**: if you care about end-to-end flow, use `docs/pipeline-stage-to-skills.md` first.
- **Navigate by design workflow**: for design-system and spec-driven work, prioritize `stitch-skills`, `pencil-skills`, `t2ui-skills`, `speckit-skills`, and `openspec-skills`.

For the current source of truth, use:

- [docs/repository-map.md](docs/repository-map.md)
- [docs/skill-group-mapping.md](docs/skill-group-mapping.md)
- [docs/pipeline-stage-to-skills.md](docs/pipeline-stage-to-skills.md)
- [docs/skills-ecosystem.md](docs/skills-ecosystem.md)

### Disclaimer


**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

## How to Use

### Using in Claude Code

#### 1. Register Marketplace

Run the following command in Claude Code to register this repository as a Claude Code plugin marketplace:

```
/plugin marketplace add https://github.com/partme-ai/full-stack-skills.git
```

Or use the short form:

```
/plugin marketplace add partme-ai/full-stack-skills
```

#### 2. Install Plugins

There are two ways to install plugins:

**Method 1: Install via UI**

1. Select `Browse and install plugins`
2. Select `full-stack-skills`
3. Select the plugin you want to install (see available plugins list below)
4. Select `Install now`

**Method 2: Install via Command**

Install plugins directly using commands:

```
/plugin install vue-skills@full-stack-skills
/plugin install react-skills@full-stack-skills
/plugin install spring-skills@full-stack-skills
/plugin install dev-utils-skills@full-stack-skills
/plugin install testing-skills@full-stack-skills
/plugin install stitch-skills@full-stack-skills
/plugin install tauri-skills@full-stack-skills
```

#### 3. Use Skills

After installing plugins, you can use skills by simply mentioning them. Claude will automatically determine when to use a skill based on its description.

### Using in Claude.ai

These example skills are all already available to paid plans in Claude.ai.

To use any skill from this repository or upload custom skills, follow the instructions in [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b).

### Using in Claude API

You can use Anthropic's pre-built skills, and upload custom skills, via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for more.

### Using on Other Platforms

This repository now ships a **TypeScript standard converter**. It exports `skills/<group>/<skill>/` into standard skill directories and installs them into the project-level or global-level path required by each supported platform. The converter does not generate platform-specific plugin wrappers; it preserves the original skill directory and switches only the destination path.

#### Adapter overview

- **CLI name**: `fskill`
- **Location**: `adapters/`
- **Input layout**: `skills/<group>/<skill>/`
- **Output layout**: standard skill directories with `SKILL.md` and resource folders
- **Core commands**: `platforms`, `audit`, `convert`, `install`
- **Default install target**: current project `.agents/skills/`
- **Platform switch**: use `--platform` for the target platform and `--scope project|global` for install scope
- **Adapter rule**: preserve the original skill contents and change only the destination path

#### Adapter workflow

1. Run `fskill audit` to verify the repository skill inventory
2. Run `fskill platforms` to inspect supported platform IDs and install paths
3. Run `fskill convert --platform <id|all>` to generate distributable standard outputs
4. Run `fskill install` or `fskill install --platform <id>` to install directly into the target platform path

#### Common adapter commands

```bash
# List supported platforms and paths
fskill platforms

# Audit repository skills
fskill audit

# Export Cursor-compatible output
fskill convert --platform cursor --output ./adapters-output

# Install into the current project's Cursor path
fskill install --platform cursor --scope project

# Install into Cursor global path ~/.cursor/skills/
fskill install --platform cursor --scope global

# Install into the default .agents/skills/ path
fskill install
```

#### Cursor and other platforms

- **Cursor**: project-level `.agents/skills/`, global `~/.cursor/skills/`
- **Claude Code**: project-level `.claude/skills/`
- **OpenClaw**: project-level `skills/`
- **Antigravity**: project-level `.agents/skills/`, global `~/.gemini/antigravity/skills/`
- **Other platforms**: all managed through the unified platform registry exposed by `fskill platforms`

**Install and run commands**

```bash
git clone https://github.com/partme-ai/full-stack-skills.git
cd full-stack-skills
npm install -g ./adapters
fskill --version
fskill platforms
fskill audit
fskill convert --platform all --output ./adapters-output
fskill install
```

By default, `fskill install` installs into the current project's `.agents/skills/` directory, which is the standard Agent Skills-compatible path. Use `--platform` and `--scope` when you need a platform-specific destination.
For repository-local development, you can also run `npm install && npm link` inside `adapters/` and then call `fskill ...` directly.

**Platform coverage**

- **Shared `.agents/skills/` family**: `amp`, `kimi-cli`, `replit`, `universal`, `antigravity`, `cline`, `warp`, `codex`, `cursor`, `deepagents`, `gemini-cli`, `github-copilot`, `opencode`
- **Dedicated directory family**: `augment`, `claude-code`, `openclaw`, `codebuddy`, `command-code`, `continue`, `cortex`, `crush`, `droid`, `goose`, `junie`, `iflow-cli`, `kilo`, `kiro-cli`, `kode`, `mcpjam`, `mistral-vibe`, `mux`, `openhands`, `pi`, `qoder`, `qwen-code`, `roo`, `trae`, `trae-cn`, `windsurf`, `zencoder`, `neovate`, `pochi`, `adal`
- **Antigravity baseline**: project-level `.agents/skills/`, global `~/.gemini/antigravity/skills/`

For the full platform matrix, installation paths, and workflow details, see [PLATFORM_GUIDE.md](PLATFORM_GUIDE.md) and [adapters/README.md](adapters/README.md).

## Repository Governance

### Inventory Rules

- Treat `skills/` as the source of truth for what exists in the repository.
- Treat `.claude-plugin/marketplace.json` as the source of truth for what is published.
- Record any drift explicitly in README and `docs/repository-map.md` instead of hiding it.
- Prefer extending an existing group over introducing a new one unless the capability boundary is clearly independent.

## Available Plugins and Skills

The table below reflects the current `skills/` directory and `.claude-plugin/marketplace.json` state.

| Group | Skills on Disk | Published | Marketplace Refs | Notes |
|---|---:|---|---:|---|
| `angular-skills` | 1 | Yes | 1 | Aligned with current published surface |
| `antd-skills` | 4 | Yes | 4 | Aligned with current published surface |
| `ascii-skills` | 13 | Yes | 13 | Aligned with current published surface |
| `avue-skills` | 3 | Yes | 3 | Aligned with current published surface |
| `build-skills` | 6 | Yes | 6 | Aligned with current published surface |
| `chart-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `cocos-skills` | 1 | Yes | 1 | Aligned with current published surface |
| `database-skills` | 5 | Yes | 5 | Aligned with current published surface |
| `ddd-skills` | 6 | Yes | 6 | Aligned with current published surface |
| `design-skills` | 12 | Yes | 12 | Aligned with current published surface |
| `dev-utils-skills` | 13 | Yes | 13 | Aligned with current published surface |
| `devops-skills` | 6 | Yes | 6 | Aligned with current published surface |
| `docker-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `document-skills` | 5 | Yes | 9 | On-disk count differs from Marketplace refs; see repository-map |
| `drawio-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `electron-skills` | 3 | Yes | 3 | Aligned with current published surface |
| `flutter-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `go-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `mobile-native-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `nodejs-skills` | 4 | Yes | 4 | Aligned with current published surface |
| `nvm-skills` | 15 | Yes | 15 | Aligned with current published surface |
| `ocrmypdf-skills` | 5 | Yes | 5 | Aligned with current published surface |
| `openspec-skills` | 15 | Yes | 15 | Aligned with current published surface |
| `pencil-skills` | 28 | Yes | 28 | Aligned with current published surface |
| `python-skills` | 3 | Yes | 3 | Aligned with current published surface |
| `react-skills` | 6 | Yes | 6 | Aligned with current published surface |
| `social-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `speckit-skills` | 13 | Yes | 13 | Aligned with current published surface |
| `spring-skills` | 7 | Yes | 7 | Aligned with current published surface |
| `stitch-skills` | 28 | Yes | 28 | Aligned with current published surface |
| `svelte-skills` | 1 | Yes | 1 | Aligned with current published surface |
| `t2ui-skills` | 97 | Yes | 97 | Aligned with current published surface |
| `tauri-skills` | 52 | Yes | 51 | On-disk count differs from Marketplace refs; see repository-map |
| `teaching-skills` | 3 | Yes | 3 | Aligned with current published surface |
| `testing-skills` | 9 | Yes | 9 | Aligned with current published surface |
| `threejs-skills` | 18 | No | 0 | Present in repo, not currently published |
| `uniapp-skills` | 13 | Yes | 13 | Aligned with current published surface |
| `utility-skills` | 3 | Yes | 3 | Aligned with current published surface |
| `uview-skills` | 2 | Yes | 2 | Aligned with current published surface |
| `vscode-skills` | 4 | No | 0 | Present in repo, not currently published |
| `vue-skills` | 7 | Yes | 7 | Aligned with current published surface |
| `vue-ui-skills` | 4 | Yes | 4 | Aligned with current published surface |

### Current Consistency Notes

- Treat the `skills/` directory as the authoritative repository inventory.
- Treat `.claude-plugin/marketplace.json` as the authoritative published plugin surface.
- The two intentional states visible today are repo-only groups (`threejs-skills`, `vscode-skills`) and published catalog drift (`document-skills`, `tauri-skills`).
- The README tables above already reflect those differences explicitly, so the documentation matches the current repository state rather than masking discrepancies.

### Suggested Installation Paths

- For frontend and UI: `vue-skills`, `react-skills`, `build-skills`, `antd-skills`, `vue-ui-skills`
- For backend and cross-platform development: `spring-skills`, `nodejs-skills`, `python-skills`, `go-skills`, `tauri-skills`, `uniapp-skills`
- For design and documentation: `design-skills`, `document-skills`, `ocrmypdf-skills`, `drawio-skills`
- For engineering delivery: `dev-utils-skills`, `testing-skills`, `devops-skills`, `docker-skills`, `database-skills`, `nvm-skills`
- For spec-driven and design workflows: `speckit-skills`, `openspec-skills`, `t2ui-skills`, `stitch-skills`, `pencil-skills`

### Installation by Scenario

- **Frontend application delivery**: start with `vue-skills` or `react-skills`, then add `build-skills`, `antd-skills`, or `vue-ui-skills` as needed.
- **Backend and service development**: pair one runtime group such as `spring-skills`, `nodejs-skills`, `python-skills`, or `go-skills` with `testing-skills` and `database-skills`.
- **Desktop or hybrid product work**: use `tauri-skills`, `electron-skills`, `uniapp-skills`, or `flutter-skills` depending on delivery target.
- **Spec-first product workflows**: install `speckit-skills`, `openspec-skills`, `t2ui-skills`, `stitch-skills`, and `pencil-skills` together.
- **Documentation and diagramming**: combine `document-skills`, `ocrmypdf-skills`, `drawio-skills`, and `ascii-skills`.

### Domain Navigation Matrix

| Goal | Read First | Recommended Bundle |
|---|---|---|
| Web frontend delivery | `vue-skills`, `react-skills`, `build-skills` | `vue-skills` / `react-skills` + `build-skills` + `testing-skills` |
| Backend and platform services | `spring-skills`, `nodejs-skills`, `database-skills` | `spring-skills` / `nodejs-skills` + `database-skills` + `devops-skills` |
| Desktop and cross-platform apps | `tauri-skills`, `electron-skills`, `uniapp-skills`, `flutter-skills` | Choose 1–2 runtime groups, then add `testing-skills` |
| Spec-driven product work | `speckit-skills`, `openspec-skills`, `t2ui-skills` | `speckit-skills` + `openspec-skills` + `t2ui-skills` |
| Design-system and UI production | `stitch-skills`, `pencil-skills`, `design-skills` | `stitch-skills` + `pencil-skills` + `design-skills` |
| Documents, OCR, and diagrams | `document-skills`, `ocrmypdf-skills`, `drawio-skills`, `ascii-skills` | `document-skills` + `ocrmypdf-skills` + `drawio-skills` |


## Project Structure

```text
full-stack-skills/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace configuration
├── adapters/                     # TypeScript standard converter and platform registry
├── agents/                       # Agent roles and orchestration entry points
├── bundles/                      # Bundled or aggregated outputs
├── dist/                         # Distribution artifacts
├── docs/                         # Repo map, ecosystem docs, stage mapping
├── media/                        # Screenshots and visual assets
├── skills/                       # Grouped skills layout
│   ├── vue-skills/
│   │   └── vue3/
│   │       └── SKILL.md
│   ├── react-skills/
│   ├── spring-skills/
│   ├── tauri-skills/
│   └── ...
├── spec/                         # Specifications and standards references
├── template/                     # Skill templates
├── tools/                        # Helper tools
├── AGENTS.md                     # Repo-level agent instructions
├── README.md
└── README_EN.md
```

### Directory Model

- `skills/<group>-skills/<skill>/SKILL.md` is the primary storage model for every skill in this repository.
- `references/` is the preferred place for long-form technical context so that `SKILL.md` stays concise and load-efficient.
- `scripts/` should hold repeatable automation instead of embedding large inline command sequences in `SKILL.md`.
- `docs/` contains the current repository map, stage-to-skill mapping, and ecosystem documentation used to understand the catalog at the repo level.

## How to Create a New Skill

### Creating a Basic Skill

Skills are simple to create: add a skill under the correct group directory and include a `SKILL.md` file with YAML frontmatter and clear instructions. You can use the repository template as a starting point:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires only two fields:
- `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` - A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Claude will follow. For more details, see [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills).

### Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent (required)
- `examples/` - Focused usage examples (optional)
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)
- `assets/` - Resource files (optional)

### Authoring Rules

- Keep `SKILL.md` lean; move large reference material into `references/` when depth is required.
- Use a concrete `description` so the agent can activate the skill reliably.
- Match directory names, frontmatter names, and published Marketplace paths.
- Prefer task-oriented instructions over encyclopedic background text.
- Keep helper scripts deterministic and machine-friendly.

### Documentation Maintenance Rules

- Update README snapshot counts whenever group counts, `SKILL.md` totals, or Marketplace refs change.
- Update README and `docs/repository-map.md` together when repo-only groups or Marketplace drift changes.
- Use only real published plugin names in installation examples.
- Keep path examples aligned with `skills/<group>-skills/<skill>/`.

### Steps to Add a New Skill

#### 1. Create Skill Directory

Create a new skill directory under the correct group inside `skills/`:

```bash
mkdir -p skills/vue-skills/my-skill-name
```

#### 2. Create SKILL.md File

Each skill must contain a `SKILL.md` file with the format shown above.

#### 3. Update marketplace.json

Add the new skill path to the matching grouped plugin in `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "vue-skills",
      "description": "Vue ecosystem skills",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/vue-skills/my-skill-name"
      ]
    }
  ]
}
```

#### 4. Commit to GitHub

Commit and push changes to the GitHub repository:

```bash
git add .
git commit -m "Add skill: my-skill-name"
git push
```

## Marketplace Configuration File

The `.claude-plugin/marketplace.json` file defines the marketplace metadata and available plugins:

```json
{
  "name": "marketplace-name",        // Marketplace name
  "owner": {                         // Owner information
    "name": "Owner Name",
    "email": "owner@example.com"
  },
  "metadata": {                      // Metadata
    "description": "Marketplace description",
    "version": "1.0.0"
  },
  "plugins": [                       // Plugin list
    {
      "name": "plugin-name",         // Plugin name
      "description": "Plugin description",
      "source": "./",                // Source code path
      "strict": false,               // Strict mode
      "skills": [                    // Skills list
        "./skills/vue-skills/vue3",
        "./skills/react-skills/react-hooks"
      ]
    }
  ]
}
```

## How It Works

1. **Marketplace Registration**: When you run `/plugin marketplace add https://github.com/partme-ai/full-stack-skills.git`, Claude Code will:
   - Fetch the `.claude-plugin/marketplace.json` file from the GitHub repository
   - Parse the marketplace configuration
   - Add the marketplace to the available list

2. **Plugin Installation**: When you install a plugin, Claude Code will:
   - Download all skills defined in the plugin
   - Store skills locally
   - Make skills available to Claude

3. **Skill Usage**: When you use a skill, Claude will:
   - Determine whether to use the skill based on its description
   - Load the skill's `SKILL.md` file
   - Execute tasks according to the skill instructions

## Best Practices

### Skill Design

- **Clear Description**: The `description` field should clearly state when to use the skill
- **Concise Content**: Keep `SKILL.md` concise, avoid unnecessary verbosity (recommended under 500 lines)
- **Structured Organization**: Use clear sections and structure
- **Practical Examples**: Provide practical, usable examples
- **Progressive Disclosure**: Put detailed reference materials in separate files and load them as needed
- **Path Discipline**: Keep the repository path, frontmatter `name`, and Marketplace path aligned
- **Task Orientation**: Write instructions around workflows, trigger phrases, expected inputs, and outputs

### Marketplace Organization

- **Logical Grouping**: Organize related skills into the same plugin
- **Clear Naming**: Use clear, descriptive names
- **Version Management**: Maintain version numbers in `metadata`
- **Catalog Hygiene**: Audit published refs against `skills/` regularly to prevent drift

### Pre-Submission Checklist

- Confirm the skill directory, frontmatter `name`, and actual capability are aligned.
- Confirm `SKILL.md` is concise and large technical detail is moved into `references/`.
- Confirm scripts, examples, and resource paths resolve inside the repository.
- Confirm README, mapping docs, and Marketplace metadata do not introduce new drift.

## License

Many skills in this repository are licensed under Apache 2.0. Document processing skills in `skills/document-skills/docx`, `skills/document-skills/pdf`, `skills/document-skills/pptx`, and `skills/document-skills/xlsx` are source-available but not open source. See the corresponding license files for details.

## Contributing

Contributions of new skills are welcome! Please follow these steps:

1. Fork this repository
2. Create new skills or improve existing skills
3. Submit a Pull Request

## Partner Skills

Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

- **Notion** - [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)

## Reference Resources

- [Agent Skills specification](https://agentskills.io/)
- [Claude Skills documentation](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic Skills examples](https://github.com/anthropics/skills)
- [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill)
- [Agent Skills CLI](https://github.com/partme-ai/partme-cli)

## Contact

For questions or suggestions, please contact us via GitHub Issues.
