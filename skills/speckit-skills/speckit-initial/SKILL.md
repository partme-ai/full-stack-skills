---
name: speckit-initial
description: Run `specify init` in the current or target directory to bootstrap a Spec Kit project (pull .specify/ and slash commands); supports multiple AI agents and --script sh/ps. Use when the user says "initialize Spec Kit project", "specify init", or "set up Spec Kit in this repo".
---

# Spec Kit Initial Skill

Run **specify init** to initialize a Spec Kit project: pull `.specify/` (memory, scripts, templates, specs) and register `/speckit.*` slash commands with the chosen AI Agent. This skill assumes the Specify CLI is already installed; if not, direct the user to **speckit-install** first.

## When to Use

- First time enabling Spec Kit in a project ("initialize Spec Kit", "set up Spec Kit here").
- Switching AI Agent (e.g. from Claude to Cursor or Gemini).
- Initializing in a new or existing directory.
- Need PowerShell scripts on Windows (`--script ps`).

## Prerequisites

- **Specify CLI** installed (see **speckit-install**). If `specify` is not in PATH, guide the user to run **speckit-install** before proceeding.
- **Git** (optional; use `--no-git` if the project is not a git repo or you want to skip git-related setup).

## Workflow

1. **Verify CLI**
   - If the user reports "specify command not found" or has not installed the CLI, direct them to **speckit-install** first. Otherwise proceed.

2. **Choose parameters**
   - **--ai** (required for slash commands): `claude` | `cursor-agent` | `gemini` | `copilot` | `windsurf` | `qwen` | `opencode` | `codex` | `qoder` | `amp` | `shai` | `bob` | `kilocode` | `auggie` | `roo` | `codebuddy` — pick the agent the user will use in this project.
   - **--script**: `sh` (default, Bash) or `ps` (PowerShell). Use `ps` on Windows when the user needs PowerShell scripts.
   - **Target**: `specify init .` or `specify init --here` for current directory; or `specify init <project_name>` for a new subdirectory.
   - **--force**: Overwrite existing `.specify/` if present (use with care).
   - **--no-git**: Skip git-related setup.
   - **--ignore-agent-tools**: Do not install or check agent-specific tools; only pull templates and `.specify/` structure.
   - **--github-token** or `GITHUB_TOKEN`: For private repos or rate-limited access.

3. **Run the command**
   - Give a concrete command for the user's OS and chosen agent. Examples:
     - Current dir, Cursor: `specify init . --ai cursor-agent`
     - Current dir, Claude: `specify init . --ai claude`
     - Windows, Copilot, PowerShell scripts: `specify init . --ai copilot --script ps`
     - New subdir: `specify init my-app --ai gemini`

4. **Confirm outputs**
   - After success: project contains `.specify/` (memory, scripts, templates, specs) and the Agent has `/speckit.*` slash commands available.

## Outputs

- **Project**: `.specify/` directory with memory, scripts, templates, and specs.
- **Agent**: Slash commands (e.g. `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`) available in the chosen AI Agent.

## Next Steps

- Run **speckit-check** to verify the environment (optional but recommended).
- Then use **speckit-constitution** or **speckit-specify** to start the Spec Kit workflow.

## Different Environments

| Environment | Example |
|-------------|---------|
| **Linux / macOS, Cursor** | `specify init . --ai cursor-agent` |
| **Linux / macOS, Claude** | `specify init . --ai claude` |
| **Windows, Copilot, PowerShell** | `specify init . --ai copilot --script ps` |
| **New subdirectory** | `specify init my-project --ai gemini` |
| **Overwrite existing .specify** | `specify init . --ai claude --force` |
| **No git** | `specify init . --ai claude --no-git` |
| **Templates only (no agent tools)** | `specify init . --ai claude --ignore-agent-tools` |

## Troubleshooting

- **"specify: command not found"**: Use **speckit-install** first.
- **Windows slash commands not appearing**: Ensure you used `--script ps` if the agent expects PowerShell, and that the agent is configured to load commands from the project.
- **Private repo / rate limit**: Set `GITHUB_TOKEN` or pass `--github-token <token>` as documented by spec-kit.

## References

- [GitHub spec-kit](https://github.com/github/spec-kit) — Get Started: Initialize your project
