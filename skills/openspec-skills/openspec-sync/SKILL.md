---
name: openspec-sync
description: Sync delta specs from a change into main specs using `/opsx:sync`, without archiving the change. Use when the user says "sync specs", "merge specs to main", "/opsx:sync", or needs to update main specs mid-change.
---

# OpenSpec Sync Skill

Use **`/opsx:sync`** to merge delta specs from a change into the main `openspec/specs/` directory without archiving the change. The change remains active after sync. This is optional — **openspec-archive** handles syncing automatically when archiving.

## When to Use

- Long-running change where the user wants specs in main before archiving.
- Multiple parallel changes need updated base specs.
- The user wants to review/preview the merge separately before archiving.

## Prerequisites

- **An active change** with delta specs in `specs/`.

## Workflow

1. **Run sync**
   - `/opsx:sync` — sync the current/inferred change.
   - `/opsx:sync add-dark-mode` — sync a specific change by name.

2. **What happens**
   - Reads delta specs from the change folder.
   - Parses ADDED / MODIFIED / REMOVED sections.
   - Merges changes into `openspec/specs/`.
   - Preserves existing content not mentioned in the delta.
   - The change remains active (not archived).

3. **Verify**
   - Review the updated specs in `openspec/specs/`.

## Outputs

- Updated `openspec/specs/` with delta changes merged.
- Change remains active in `openspec/changes/<name>/`.

## Next Steps

- Continue working on the change, or use **openspec-archive** when done.

## Troubleshooting

- **"No delta specs"**: The change has no `specs/` directory; create specs via **openspec-continue** or **openspec-ff** first.
- **Conflicts with other changes**: Sync handles merging at the requirement level; if two changes modify the same requirement, the latest sync wins.

## References

- [OpenSpec Commands: /opsx:sync](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
- [OpenSpec Concepts: Delta Specs](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)
