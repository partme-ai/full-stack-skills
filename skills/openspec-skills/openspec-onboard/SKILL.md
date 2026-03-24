---
name: openspec-onboard
description: Guided onboarding through the complete OpenSpec workflow using `/opsx:onboard`, walking the user through a real change in their codebase. Use when the user says "onboard me", "tutorial", "/opsx:onboard", "how does OpenSpec work", or is new to OpenSpec.
---

# OpenSpec Onboard Skill

Use **`/opsx:onboard`** for a guided, interactive tutorial through the complete OpenSpec workflow. The tutorial uses the user's actual codebase — finding real improvement opportunities, creating a real change, implementing it, and archiving it.

## When to Use

- First-time OpenSpec users who want a hands-on walkthrough.
- The user says "onboard", "tutorial", "show me how OpenSpec works".
- Learning the workflow before using it on real work.

## Prerequisites

- **OpenSpec initialized** in the project (see **openspec-initial**).

## Workflow

1. **Start onboarding**
   - Run `/opsx:onboard`.

2. **Tutorial phases**
   1. Welcome and codebase analysis.
   2. Finding an improvement opportunity (small, safe changes).
   3. Creating a change (`/opsx:new`).
   4. Writing the proposal.
   5. Creating specs.
   6. Writing the design.
   7. Creating tasks.
   8. Implementing tasks (`/opsx:apply`).
   9. Verifying implementation.
   10. Archiving the change.
   11. Summary and next steps.

3. **Interactive**
   - The agent explains each step as it happens.
   - The user chooses which improvement to work on.
   - The change created is real and can be kept or discarded.

## Outputs

- A complete change cycle (from proposal to archive) using the user's actual codebase.
- The user has first-hand experience with every OPSX command.

## Next Steps

- Start real work with **openspec-new** or **openspec-explore**.

## Troubleshooting

- **"Commands not recognized"**: Ensure OpenSpec is initialized (`openspec init`). See **openspec-initial**.
- **Takes too long**: The tutorial covers the full workflow; expect 15-30 minutes.

## References

- [OpenSpec Commands: /opsx:onboard](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
