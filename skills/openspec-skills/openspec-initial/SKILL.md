---
name: openspec-initial
description: Run `openspec init` to initialize OpenSpec in a project directory, creating the openspec/ folder structure and configuring AI tool integrations. Use when the user says "initialize OpenSpec", "openspec init", or "set up OpenSpec in this project".
---

# OpenSpec Initial Skill

Run **openspec init** to initialize OpenSpec in a project: creates the `openspec/` directory (specs, changes, config) and configures AI tool integrations (skills and slash commands). This skill assumes the OpenSpec CLI is already installed; if not, direct the user to **openspec-install** first.

## When to Use

- First time enabling OpenSpec in a project ("initialize OpenSpec", "set up OpenSpec here").
- Adding AI tool integrations (Claude, Cursor, Windsurf, etc.) to an existing project.
- Re-initializing after changing tool selections.

## Prerequisites

- **OpenSpec CLI** installed (see **openspec-install**). If `openspec` is not in PATH, guide the user to run **openspec-install** before proceeding.

## Workflow

1. **Verify CLI**
   - If the user reports "openspec command not found", direct them to **openspec-install** first.

2. **Choose parameters**
   - **path** (optional): Target directory; defaults to current directory.
   - **--tools** (optional): Configure AI tools non-interactively. Values: `all`, `none`, or comma-separated list (e.g. `claude,cursor`).
   - **--force**: Auto-cleanup legacy files without prompting.

3. **Run the command**
   - Interactive: `openspec init`
   - Non-interactive with specific tools: `openspec init --tools claude,cursor`
   - All tools: `openspec init --tools all`
   - Specific directory: `openspec init ./my-project`

4. **Optionally create project config**
   - During init, the user may be prompted to create `openspec/config.yaml` with project context, schema defaults, and per-artifact rules. This is optional but recommended. See **openspec-config** for details.

5. **Confirm outputs**
   - After success: `openspec/` directory with `specs/`, `changes/`, and optionally `config.yaml`. Tool-specific directories (`.claude/skills/`, `.cursor/rules/`, etc.) are created based on selected tools.

## Supported Tools

`amazon-q`, `antigravity`, `auggie`, `claude`, `cline`, `codebuddy`, `codex`, `continue`, `costrict`, `crush`, `cursor`, `factory`, `gemini`, `github-copilot`, `iflow`, `kilocode`, `opencode`, `qoder`, `qwen`, `roocode`, `trae`, `windsurf`

## Outputs

- **openspec/**:
  - `specs/` — Specifications (source of truth)
  - `changes/` — Proposed changes
  - `config.yaml` — Project configuration (optional)
- **Tool configs**: `.claude/skills/`, `.cursor/rules/`, `.windsurf/skills/`, etc. based on selected tools.

## Next Steps

- Use **openspec-update** after upgrading the CLI to regenerate tool configs.
- Use **openspec-onboard** for a guided walkthrough of the complete workflow.
- Or start working: **openspec-explore** to think through ideas, **openspec-new** to start a change.

## Different Environments

| Scenario | Command |
|----------|---------|
| **Interactive** | `openspec init` |
| **Claude + Cursor** | `openspec init --tools claude,cursor` |
| **All tools** | `openspec init --tools all` |
| **Specific directory** | `openspec init ./my-project` |
| **CI / non-interactive** | `openspec init --tools claude --force` |
| **Skip tool config** | `openspec init --tools none` |

## Troubleshooting

- **"openspec: command not found"**: Use **openspec-install** first.
- **Legacy files detected**: Use `--force` to auto-cleanup, or follow the interactive prompts.
- **Tool not in list**: Check the [supported tools list](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md) for the correct ID.

## References

- [OpenSpec CLI: init](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [OpenSpec Supported Tools](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md)
