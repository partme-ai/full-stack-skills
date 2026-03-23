# Example: `specify check` output and interpretation

Below is a **sample** output. Actual output may vary by spec-kit version and OS.

## Sample output (success)

```
Spec Kit environment check
-------------------------
specify CLI:    OK (version 0.x.x)
git:            OK
cursor-agent:   OK
```

**Interpretation**: CLI, git, and the chosen agent (cursor-agent) are available. The user can proceed with **speckit-constitution** or **speckit-specify**.

---

## Sample output (missing agent)

```
Spec Kit environment check
-------------------------
specify CLI:    OK (version 0.x.x)
git:            OK
claude:         Not found (not in PATH)
```

**Interpretation**: The CLI and git are fine; the Claude agent is not detected (e.g. not installed or not on PATH). **Next steps**: Install the Claude agent / add it to PATH, or re-run **speckit-initial** with a different `--ai` (e.g. `cursor-agent`) or with `--ignore-agent-tools` if only templates are needed.

---

## Sample output (CLI missing)

If the user runs `specify check` but gets:

```
specify: command not found
```

**Interpretation**: Specify CLI is not installed. **Next step**: Use **speckit-install** to install the CLI, then run `specify check` again.
