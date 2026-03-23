---
name: nvm-uninstall
description: Remove nvm cleanly, including NVM_DIR cleanup, profile edits, and PATH restoration.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Uninstalling or removing nvm
- Cleaning NVM_DIR or profile entries
- Restoring system node priority

**Trigger phrases include:**
- "uninstall nvm", "移除 nvm", "cleanup"
- "restore PATH", "恢复系统 Node"

## How to use this skill

**CRITICAL: This skill is for removal and cleanup only.** Installation or usage belongs to other nvm-* skills.

1. Remove NVM_DIR and delete nvm profile entries.
2. Restore PATH to prioritize the system Node.
3. Validate that nvm commands are no longer available.

### Example file map

- examples/uninstall.md
- examples/restore-path.md
- examples/system-node.md

## Keywords

nvm uninstall, remove, cleanup, PATH restore, system node, 卸载
