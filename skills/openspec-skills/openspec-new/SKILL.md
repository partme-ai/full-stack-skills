---
name: openspec-new
description: Start a new OpenSpec change with `/opsx:new`, creating a change folder with metadata and scaffolding. Use when the user says "start a new change", "new feature", "/opsx:new", or "create an OpenSpec change".
---

# OpenSpec New Skill

Use **`/opsx:new`** to start a new change. This creates the change folder structure under `openspec/changes/<name>/` with metadata (`.openspec.yaml`) and prepares the first artifact for creation.

## When to Use

- Starting work on a new feature, bug fix, or refactor.
- The user says "start a change", "new feature", "new OpenSpec change".
- After exploring ideas with **openspec-explore** and deciding what to build.

## Prerequisites

- **OpenSpec initialized** in the project (see **openspec-initial**).

## Workflow

1. **Start the change**
   - `/opsx:new <change-name>` — e.g. `/opsx:new add-dark-mode`.
   - `/opsx:new <change-name> --schema <schema>` — use a specific workflow schema (default: `spec-driven`).
   - If no name is provided, the agent will prompt for one.

2. **What gets created**
   - `openspec/changes/<name>/` directory.
   - `openspec/changes/<name>/.openspec.yaml` — change metadata (schema, created date).

3. **Next action**
   - The agent shows the first artifact ready for creation (typically `proposal`).
   - Use **openspec-continue** to create one artifact at a time, or **openspec-ff** to create all planning artifacts at once.

## Naming Conventions

- Use descriptive names: `add-dark-mode`, `fix-login-bug`, `refactor-auth`.
- Avoid generic names: `update`, `changes`, `wip`.
- Use kebab-case.

## Outputs

- `openspec/changes/<name>/` directory with `.openspec.yaml`.

## Next Steps

- Use **openspec-continue** to create the next artifact incrementally.
- Or **openspec-ff** to fast-forward through all planning artifacts at once.

## Troubleshooting

- **"Change not found"**: Check the change name matches; run `openspec list` to see active changes.
- **"Schema not found"**: List available schemas with `openspec schemas`; see **openspec-schema** for custom schemas.

## References

- [OpenSpec Commands: /opsx:new](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
