---
name: openspec-continue
description: Create the next artifact in the dependency chain with `/opsx:continue`, building up a change incrementally. Use when the user says "continue the change", "create next artifact", "/opsx:continue", or wants step-by-step artifact creation.
---

# OpenSpec Continue Skill

Use **`/opsx:continue`** to create the next artifact in the dependency chain. This builds a change incrementally — one artifact at a time — giving the user control to review and edit before proceeding.

## When to Use

- The user wants incremental, step-by-step artifact creation.
- After creating a change with **openspec-new** and wanting to build artifacts one at a time.
- The user says "continue", "next artifact", "create specs", "create design".

## Prerequisites

- **An active change** exists (created via **openspec-new** or `/opsx:new`).

## Workflow

1. **Query the dependency graph**
   - Run `openspec status --change <name> --json` to see which artifacts are done, ready, or blocked.

2. **Identify ready artifacts**
   - In the default `spec-driven` schema: `proposal` -> `specs` / `design` -> `tasks`.
   - Dependencies are enablers: once a dependency is done, its dependents become "ready".

3. **Create one artifact**
   - Read dependency files for context.
   - Run `openspec instructions <artifact> --change <name> --json` to get enriched instructions and templates.
   - Create the first ready artifact (e.g. proposal, then specs, then design, then tasks).

4. **Show what's unlocked**
   - After creating an artifact, report what becomes available next.

5. **Repeat**
   - User reviews, optionally edits, then runs `/opsx:continue` again for the next artifact.

## Artifact Dependency Graph (spec-driven schema)

```
proposal (root, no dependencies)
    |
    +---> specs (requires: proposal)
    |
    +---> design (requires: proposal)
            |
            +---> tasks (requires: specs + design)
```

## Outputs

- One artifact file created per invocation (e.g. `proposal.md`, `specs/**/*.md`, `design.md`, `tasks.md`).

## Next Steps

- Run `/opsx:continue` again for the next artifact.
- When all planning artifacts are done: use **openspec-apply** to implement tasks.
- Or use **openspec-ff** to fast-forward remaining artifacts.

## Troubleshooting

- **"No artifacts ready"**: All artifacts are either complete or blocked. Check `openspec status --change <name>`.
- **"Change not found"**: Specify the change name explicitly: `/opsx:continue add-dark-mode`.

## References

- [OpenSpec Commands: /opsx:continue](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
- [OpenSpec Concepts: Artifacts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)
