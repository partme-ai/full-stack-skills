---
name: nvm-shell-integration
description: Enable deeper shell integration and auto-switching for nvm across bash, zsh, and fish.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Deeper shell integration
- Auto "nvm use" when entering a directory
- Restoring PATH or deactivating nvm

**Trigger phrases include:**
- "shell integration", "深度集成", "auto use"
- "PATH 恢复", "nvm deactivate"

## How to use this skill

**CRITICAL: This skill is for deeper shell integration and auto-switching.** Base shell loading belongs to nvm-setup.

1. Pick the target shell and enable deeper integration steps.
2. Add auto-use logic for directory changes.
3. Restore PATH or deactivate nvm when needed.

### Example file map

- examples/shell-integration.md
- examples/auto-use-bash.md
- examples/auto-use-zsh.md
- examples/auto-use-fish.md
- examples/restore-path.md

## Keywords

shell integration, auto use, PATH restore, nvm deactivate, 自动切换
