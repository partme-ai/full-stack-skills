---
name: nvm-verify
description: Verify nvm installation and diagnose PATH or profile loading issues after setup.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Verifying nvm, node, or npm versions
- "nvm: command not found" after installation
- PATH or profile not updated

**Trigger phrases include:**
- "nvm --version", "node -v", "npm -v"
- "PATH 问题", "profile 未加载"
- "安装后不可用", "verify installation"

## How to use this skill

**CRITICAL: This skill is for verification and initial diagnostics only.** For deeper platform issues, use the troubleshooting skills.

1. Run verification checks for nvm, node, and npm.
2. If commands fail, inspect profile loading and PATH order.
3. Apply restore-path and common-problems guidance.
4. Re-open a new shell session and re-check.

**Important notes:**
- nvm is a shell function, so the profile must load correctly.

### Example file map

- examples/verify-installation.md
- examples/problems.md
- examples/restore-path.md
- examples/important-notes.md

## Keywords

nvm verify, nvm --version, node -v, npm -v, PATH, profile, verification
