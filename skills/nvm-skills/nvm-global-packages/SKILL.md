---
name: nvm-global-packages
description: Migrate global packages between Node versions and define a default global packages file for consistency.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Reinstalling global packages while installing a new version
- Using a default-packages file
- Keeping global package consistency across versions

**Trigger phrases include:**
- "reinstall-packages-from", "迁移全局包"
- "default-packages", "默认全局包文件"

## How to use this skill

**CRITICAL: This skill handles global packages strategy.** Version install/use belongs to usage basics.

1. Use reinstall-packages-from to migrate global packages.
2. Configure default-packages file and validate scope.
3. Call out risks of conflicting global packages across versions.

### Example file map

- examples/migrate-global-packages.md
- examples/default-global-packages.md

## Keywords

global packages, default-packages, reinstall-packages-from, npm global, consistency
