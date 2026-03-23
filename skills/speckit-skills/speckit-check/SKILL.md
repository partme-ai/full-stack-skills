---
name: speckit-check
description: Run `specify check` to verify that Spec Kit required tools (git, claude, gemini, code, cursor-agent, windsurf, qwen, opencode, codex, shai, qoder, etc.) are installed and available; interpret results and suggest next steps. Use when the user says "check Spec Kit environment", "specify not working", or "slash commands not showing".
---

# Spec Kit Check Skill

Run **specify check** to verify that the Spec Kit CLI and required tools (git, AI agents, editors) are installed and detectable. Use this after **speckit-install** or **speckit-initial** to confirm the environment, or when the user reports that slash commands are missing or `specify` does not work.

## When to Use

- After initializing a project with **speckit-initial** to confirm the environment.
- When slash commands do not appear or the user says "specify not working".
- In CI or scripts to ensure dependencies are present before running Spec Kit steps.

## Prerequisites

- **Specify CLI** must be installed (see **speckit-install**). If `specify` is not in PATH, direct the user to **speckit-install** before running `specify check`.

## Workflow

1. **Ensure CLI is available**
   - If the user has not installed the CLI or reports "specify: command not found", direct them to **speckit-install** first. Do not run `specify check` until `specify` is available.

2. **Run the check**
   - From the project root (or target directory): `specify check`
   - The command reports which tools are detected (e.g. git, claude, gemini, code, cursor-agent, windsurf, qwen, opencode, codex, shai, qoder) and which are missing or not in PATH.

3. **Interpret the output**
   - **All required tools present**: Environment is ready; suggest proceeding with **speckit-constitution** or **speckit-specify**.
   - **CLI missing**: Direct to **speckit-install**.
   - **Agent or editor missing**: Suggest installing the corresponding Agent/editor or adding its executable to PATH. If the user only needs templates and `.specify/` (no slash commands), suggest re-running **speckit-initial** with `--ignore-agent-tools`.

4. **Summarize and recommend**
   - Provide a short summary: what is OK, what is missing.
   - Give concrete next steps: install CLI (**speckit-install**), re-init with different agent (**speckit-initial**), or fix PATH / install Agent.

## Outputs

- **Summary**: Which tools are detected and which are missing.
- **Recommendations**: List of next actions (install CLI, run init, install Agent, add to PATH, or use `specify init --ignore-agent-tools`).

## Next Steps

- If something is missing: use **speckit-install** (for CLI) or **speckit-initial** (to re-init or use `--ignore-agent-tools`), or install the missing Agent/editor.
- If check passes: proceed with **speckit-constitution** or **speckit-specify**.

## Example Output (reference)

See `examples/sample-output.md` for an example of `specify check` output and how to interpret it.

## Troubleshooting

- **"specify: command not found"**: Use **speckit-install**.
- **Agent reported as missing**: Ensure the Agent app is installed and its CLI or executable is on PATH; or use `specify init --ignore-agent-tools` if only templates are needed.
- **Git missing**: Install git or run `specify init --no-git` if git is not required for the workflow.

## References

- [GitHub spec-kit](https://github.com/github/spec-kit) — CLI: specify check
