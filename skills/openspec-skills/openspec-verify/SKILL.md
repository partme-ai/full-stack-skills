---
name: openspec-verify
description: Validate that implementation matches change artifacts using `/opsx:verify`, checking completeness, correctness, and coherence. Use when the user says "verify implementation", "check my work", "/opsx:verify", or wants quality validation before archiving.
---

# OpenSpec Verify Skill

Use **`/opsx:verify`** to validate that the implementation matches the change artifacts. Checks three dimensions — completeness, correctness, and coherence — and reports issues categorized as CRITICAL, WARNING, or SUGGESTION.

## When to Use

- After implementing tasks with **openspec-apply**, before archiving.
- The user says "verify", "check my work", "validate implementation".
- Quality gate before archiving a change.

## Prerequisites

- **Tasks implemented** (via **openspec-apply** or manual coding).

## Workflow

1. **Run verification**
   - `/opsx:verify` — verify the current/inferred change.
   - `/opsx:verify <change-name>` — verify a specific change.

2. **Three verification dimensions**

   | Dimension | What it validates |
   |-----------|-------------------|
   | **Completeness** | All tasks done, all requirements implemented, scenarios covered |
   | **Correctness** | Implementation matches spec intent, edge cases handled |
   | **Coherence** | Design decisions reflected in code, patterns consistent |

3. **Review the report**
   - **CRITICAL**: Must fix before archiving.
   - **WARNING**: Should address; does not block archive.
   - **SUGGESTION**: Optional improvements.

4. **Fix issues if needed**
   - Address critical issues, optionally fix warnings.
   - Run `/opsx:verify` again to confirm.

## Outputs

- Verification report with categorized issues (CRITICAL / WARNING / SUGGESTION).
- Summary: ready to archive or not.

## Next Steps

- If ready: use **openspec-archive** to archive the change.
- If issues found: fix code or update artifacts, then re-verify.

## Troubleshooting

- **Many false positives**: Add project context in `openspec/config.yaml` to help the agent understand conventions. See **openspec-config**.

## References

- [OpenSpec Commands: /opsx:verify](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
