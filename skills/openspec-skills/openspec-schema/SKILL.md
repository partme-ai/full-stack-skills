---
name: openspec-schema
description: Create and manage custom workflow schemas using `openspec schema init/fork/validate/which`. Use when the user says "create a custom workflow", "custom schema", "fork a schema", or wants to define their own artifact types and dependencies.
---

# OpenSpec Schema Skill

Use **openspec schema** subcommands to create and manage custom workflow schemas. Schemas define what artifacts exist and their dependencies. The default `spec-driven` schema provides proposal -> specs -> design -> tasks, but custom schemas allow different workflows.

## When to Use

- The user wants a custom workflow (e.g. research-first, rapid iteration).
- The user says "create a schema", "custom workflow", "fork the spec-driven schema".
- Debugging schema resolution (`openspec schema which`).
- Validating a custom schema's structure.

## Prerequisites

- **OpenSpec CLI** installed (see **openspec-install**).

## Workflow

### Create a new schema from scratch

```bash
openspec schema init my-workflow
# Interactive: prompts for description, artifacts, default
# Non-interactive:
openspec schema init rapid --description "Rapid iteration" --artifacts "proposal,tasks" --default
```

Creates `openspec/schemas/my-workflow/` with `schema.yaml` and `templates/`.

### Fork an existing schema

```bash
openspec schema fork spec-driven my-workflow
```

Copies the `spec-driven` schema for customization.

### Validate a schema

```bash
openspec schema validate my-workflow
# Or validate all:
openspec schema validate
```

### Check schema resolution

```bash
openspec schema which spec-driven
# Shows: package, project, or user source
openspec schema which --all
```

## Schema Structure

```
openspec/schemas/<name>/
├── schema.yaml       # Artifact definitions and dependencies
└── templates/
    ├── proposal.md   # Template for each artifact
    ├── specs.md
    ├── design.md
    └── tasks.md
```

### Example schema.yaml

```yaml
name: research-first
artifacts:
  - id: research
    generates: research.md
    requires: []
  - id: proposal
    generates: proposal.md
    requires: [research]
  - id: tasks
    generates: tasks.md
    requires: [proposal]
```

## Schema Precedence

1. **Project**: `openspec/schemas/<name>/` (local, version controlled)
2. **User**: `~/.local/share/openspec/schemas/<name>/` (global)
3. **Package**: Built-in schemas (e.g. `spec-driven`)

## Outputs

- Custom schema in `openspec/schemas/<name>/` with `schema.yaml` and templates.

## Next Steps

- Use the schema with **openspec-new**: `/opsx:new my-change --schema my-workflow`.
- Or set as default in **openspec-config** (`openspec/config.yaml`).

## Troubleshooting

- **"Schema not found"**: Check `openspec schemas` for available schemas; check `openspec schema which <name>` for resolution.
- **Validation errors**: Run `openspec schema validate <name> --verbose` for details.
- **Unknown artifact IDs in rules**: Check `openspec schemas --json` for artifact IDs per schema.

## References

- [OpenSpec CLI: schema commands](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [OpenSpec Concepts: Schemas](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)
- [OpenSpec Customization](https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md)
