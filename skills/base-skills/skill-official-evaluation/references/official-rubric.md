# Official evaluating rubric

This file defines the “official rubric” used by `skill-official-evaluation`.

## 1) Spec compliance (must)

### 1.1 SKILL.md frontmatter

- name:
  - matches directory name
  - lowercase letters, numbers, hyphens only
  - 1–64 chars; no leading/trailing hyphen; no consecutive `--`
- description:
  - non-empty
  - describes what + when to use
  - not overly broad; includes clear triggers
- optional fields (if present):
  - license / compatibility / metadata / allowed-tools formatting is valid

### 1.2 Directory structure

- skill root contains `SKILL.md`
- optional directories follow conventions:
  - `scripts/` for executable automation
  - `references/` for on-demand docs
  - `assets/` for templates/resources

## 2) Progressive disclosure quality (should)

- SKILL.md body stays concise and actionable
- long explanations moved to `references/`
- references are linked with clear “when to read” triggers
- avoids deep chains of references

## 3) Trigger description quality (should)

- uses user-intent language (what users say)
- avoids implementation-only keywords
- contains both “should trigger” and “should not trigger” boundaries where needed

## 4) Script readiness (conditional)

If `scripts/` exists, apply [script-safety-checklist.md](script-safety-checklist.md) and verify:

- non-interactive CLI
- `--help` available
- clear error messages
- structured output option (json)
- safe defaults and idempotency considerations

## 5) Security hygiene (must)

- no secrets in skill files (keys/tokens/passwords)
- no suspicious downloads/exfiltration instructions
- risky operations require explicit user confirmation guidance

