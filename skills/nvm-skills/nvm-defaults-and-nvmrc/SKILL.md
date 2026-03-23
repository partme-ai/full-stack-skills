---
name: nvm-defaults-and-nvmrc
description: Define default Node versions and manage project-specific versions with .nvmrc and auto-use flows.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Setting a default Node version or alias
- Creating or using a .nvmrc file
- Auto-switching versions per directory

**Trigger phrases include:**
- "nvm alias default", "默认版本", ".nvmrc"
- "auto use", "进入目录自动切换"

## How to use this skill

**CRITICAL: This skill is about defaults and .nvmrc.** Basic install/use belongs to nvm-usage-basics.

1. Set the default alias or LTS target.
2. Create or update .nvmrc with the required version or alias.
3. Enable shell auto-use logic if requested.
4. Verify switching behavior in a new shell session.

**Important notes:**
- Keep .nvmrc consistent across team repos to avoid version drift.

### Example file map

- examples/default-version.md
- examples/nvmrc.md
- examples/auto-use-bash.md
- examples/auto-use-zsh.md
- examples/auto-use-fish.md

## Keywords

nvm alias, default version, .nvmrc, auto use, project version, defaults
