---
name: openspec-update
description: Run `openspec update` to regenerate AI tool instruction files after upgrading the OpenSpec CLI. Use when the user says "update OpenSpec", "openspec update", or "refresh OpenSpec skills/commands".
---

# OpenSpec Update Skill

Run **openspec update** to regenerate AI tool configuration files (skills, commands, rules) after upgrading the OpenSpec CLI package. This ensures your project uses the latest slash commands and skill instructions.

## When to Use

- After upgrading the OpenSpec CLI (`npm install -g @fission-ai/openspec@latest`).
- When slash commands or skills seem outdated or missing.
- After changing tool selections and wanting to refresh configs.

## Prerequisites

- **OpenSpec CLI** installed (see **openspec-install**).
- **Project initialized** with `openspec init` (see **openspec-initial**).

## Workflow

1. **Upgrade the CLI first** (if not already done)
   - `npm install -g @fission-ai/openspec@latest` (or pnpm/yarn/bun equivalent).

2. **Run update**
   - `openspec update` — regenerates AI tool config files.
   - `openspec update --force` — force update even when files are up to date.
   - `openspec update ./my-project` — target a specific directory.

3. **Verify**
   - Check that `.claude/skills/`, `.cursor/rules/`, or other tool directories have been refreshed.
   - Restart your AI tool to pick up new skills if needed.

## Outputs

- Regenerated tool-specific config files (skills, commands, rules) matching the new CLI version.

## Next Steps

- Continue your workflow with **openspec-new**, **openspec-explore**, etc.

## Troubleshooting

- **"openspec: command not found"**: Use **openspec-install** first.
- **"Project not initialized"**: Run **openspec-initial** (`openspec init`) first.
- **Skills not appearing after update**: Restart your AI tool (Claude Code, Cursor, etc.) to reload skills.

## References

- [OpenSpec CLI: update](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
