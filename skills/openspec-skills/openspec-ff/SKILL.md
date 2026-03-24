---
name: openspec-ff
description: Fast-forward through artifact creation with `/opsx:ff`, generating all planning artifacts (proposal, specs, design, tasks) at once. Use when the user says "fast forward", "create all artifacts", "/opsx:ff", or has a clear picture of what to build.
---

# OpenSpec Fast-Forward Skill

Use **`/opsx:ff`** to fast-forward through all planning artifact creation at once. Creates all artifacts in dependency order (proposal -> specs -> design -> tasks) in a single pass.

## When to Use

- The user has a clear picture of what to build and does not need incremental review.
- The user says "fast forward", "create everything", "generate all planning docs".
- Small to medium features where step-by-step review is unnecessary.

## Prerequisites

- **An active change** exists (created via **openspec-new** or `/opsx:new`).
- Or use `/opsx:ff <change-name>` to create and fast-forward in one step.

## Workflow

1. **Run fast-forward**
   - `/opsx:ff` — fast-forward the current/inferred change.
   - `/opsx:ff <change-name>` — fast-forward a specific change.

2. **Artifacts are created in dependency order**
   - In the default `spec-driven` schema:
     1. `proposal.md` — why and what
     2. `specs/**/*.md` — delta specs (requirements and scenarios)
     3. `design.md` — technical approach
     4. `tasks.md` — implementation checklist
   - Each artifact reads its dependencies before being created.

3. **Review**
   - All planning artifacts are now available. The user can edit any of them before proceeding.

## Outputs

- All planning artifacts created in `openspec/changes/<name>/`:
  - `proposal.md`
  - `specs/**/*.md`
  - `design.md`
  - `tasks.md`

## Next Steps

- Review and edit artifacts if needed.
- Use **openspec-apply** to implement tasks.
- Or use **openspec-verify** after implementation to validate.

## Troubleshooting

- **"Change not found"**: Specify the name: `/opsx:ff add-dark-mode`.
- **Artifact quality issues**: Use `/opsx:continue` instead for more control; add project context in `openspec/config.yaml` (see **openspec-config**).

## References

- [OpenSpec Commands: /opsx:ff](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
