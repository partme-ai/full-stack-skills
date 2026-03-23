---
name: openspec-bulk-archive
description: Archive multiple completed changes at once with `/opsx:bulk-archive`, handling spec conflicts between changes. Use when the user says "archive all changes", "bulk archive", "/opsx:bulk-archive", or has multiple completed changes.
---

# OpenSpec Bulk Archive Skill

Use **`/opsx:bulk-archive`** to archive multiple completed changes at once. Validates each change, detects spec conflicts across changes, and resolves them by checking what is actually implemented.

## When to Use

- Multiple changes are completed and ready to archive.
- The user says "archive all", "bulk archive", "clean up finished changes".
- After a sprint or batch of parallel work.

## Prerequisites

- **Multiple active changes** with completed tasks.

## Workflow

1. **Run bulk archive**
   - `/opsx:bulk-archive` — lists all completed changes and prompts to select.
   - `/opsx:bulk-archive <name1> <name2> ...` — archive specific changes.

2. **What happens**
   - Lists all completed changes.
   - Validates each change before archiving.
   - Detects spec conflicts across changes (e.g. two changes touch the same spec file).
   - Resolves conflicts by checking what is actually implemented in the codebase.
   - Archives in chronological order (by creation date).

3. **Confirm**
   - The agent shows the list and conflict resolution plan; the user confirms.

## Outputs

- All selected changes archived to `openspec/changes/archive/`.
- Delta specs merged into `openspec/specs/` in chronological order.

## Next Steps

- Start new changes with **openspec-new**.

## Troubleshooting

- **Spec conflicts**: The agent inspects the codebase to resolve; review the resolution before confirming.
- **Incomplete changes**: Bulk archive warns about incomplete tasks but does not block.

## References

- [OpenSpec Commands: /opsx:bulk-archive](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
