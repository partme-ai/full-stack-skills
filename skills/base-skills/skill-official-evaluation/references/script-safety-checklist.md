# Script safety checklist

Use this checklist when the target skill contains executable scripts or instructs the agent to run shell commands.

## Required

- Non-interactive
  - No prompts waiting for stdin/TTY
  - All inputs via flags/env/stdin explicitly
- Clear help
  - `--help` prints usage + examples
- Clear errors
  - errors say what failed + what to try next
- No secrets
  - no hardcoded tokens/keys/passwords
  - no logging of secrets
- Safe defaults
  - destructive ops require explicit `--force` / `--confirm`
  - prefer dry-run flags where applicable

## Recommended

- Structured output
  - `--format json` (or `--output <file>`)
  - diagnostics to stderr, data to stdout
- Idempotency
  - repeated runs do not corrupt state
- Predictable output size
  - defaults to summary; supports pagination flags if needed

