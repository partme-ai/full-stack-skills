---
name: openspec-config
description: Configure OpenSpec project settings and global CLI configuration using `openspec/config.yaml` and `openspec config` commands. Use when the user says "configure OpenSpec", "project config", "add project context", or wants to set per-artifact rules.
---

# OpenSpec Config Skill

Manage OpenSpec configuration at two levels: **project config** (`openspec/config.yaml`) for project-specific context and rules, and **global CLI config** (`openspec config` subcommands) for user-level settings.

## When to Use

- The user wants to add project context to improve AI artifact quality.
- Setting per-artifact rules (e.g. "specs must use Given/When/Then").
- Changing the default schema for the project.
- Managing global CLI settings (telemetry, editor, etc.).

## Prerequisites

- **OpenSpec initialized** in the project (see **openspec-initial**).

## Project Configuration

### openspec/config.yaml

```yaml
# Default schema for new changes
schema: spec-driven

# Project context injected into all artifact instructions
context: |
  Tech stack: TypeScript, React, Node.js
  API conventions: RESTful, JSON responses
  Testing: Vitest for unit tests, Playwright for e2e
  Style: ESLint with Prettier, strict TypeScript

# Per-artifact rules
rules:
  proposal:
    - Include rollback plan
    - Identify affected teams
  specs:
    - Use Given/When/Then format for scenarios
  design:
    - Include sequence diagrams for complex flows
```

### Config Fields

| Field | Type | Description |
|-------|------|-------------|
| `schema` | string | Default schema for new changes (e.g. `spec-driven`) |
| `context` | string | Project context injected into all artifact instructions (max 50KB) |
| `rules` | object | Per-artifact rules, keyed by artifact ID |

### How It Works

- **Schema precedence** (highest to lowest): CLI flag -> change metadata -> project config -> default (`spec-driven`).
- **Context injection**: Prepended to every artifact's instructions in `<project-context>` tags.
- **Rules injection**: Only for matching artifacts, in `<project-rules>` tags, after context.

### Artifact IDs (spec-driven schema)

- `proposal` — Change proposal
- `specs` — Specifications
- `design` — Technical design
- `tasks` — Implementation tasks

## Global CLI Configuration

```bash
openspec config list          # Show all settings
openspec config get <key>     # Get a value
openspec config set <key> <value>  # Set a value
openspec config unset <key>   # Remove a key
openspec config reset --all --yes  # Reset to defaults
openspec config edit          # Open in $EDITOR
openspec config path          # Show config file location
```

### Common Settings

| Setting | Example |
|---------|---------|
| Disable telemetry | `openspec config set telemetry.enabled false` |
| Set user name | `openspec config set user.name "My Name" --string` |

## Outputs

- `openspec/config.yaml` with project context and rules.
- Improved AI artifact quality through context injection.

## Next Steps

- Start working with **openspec-new** or **openspec-explore**.
- Create a custom schema with **openspec-schema** and set it as default in config.

## Troubleshooting

- **"Unknown artifact ID in rules"**: Check artifact IDs match your schema; run `openspec schemas --json`.
- **Config not applied**: Ensure file is at `openspec/config.yaml` (not `.yml`); check YAML syntax.
- **Context too large**: Limit is 50KB; summarize or link to external docs.

## References

- [OpenSpec CLI: config](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [OpenSpec OPSX: Project Configuration](https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md)
