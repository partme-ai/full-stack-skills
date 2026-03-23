---
name: nvm-troubleshooting-macos
description: Diagnose common nvm issues on macOS, including profile loading, PATH priority, and permissions.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- nvm not working on macOS after installation
- zsh/bash profile not loading
- PATH priority or permission issues on macOS

**Trigger phrases include:**
- "macOS nvm not found", "zshrc", "bash_profile"
- "PATH 优先级", "权限问题", "兼容性"

## How to use this skill

**CRITICAL: This skill is macOS-specific troubleshooting.** General verification belongs to nvm-verify.

1. Confirm the active shell and profile load order.
2. Follow macOS troubleshooting steps to locate the failure.
3. Apply compatibility issue guidance when needed.
4. Re-test in a new shell session.

### Example file map

- examples/troubleshooting-macos.md
- examples/macos-troubleshooting.md
- examples/problems.md
- examples/compatibility-issues.md

## Keywords

macos, zsh, bash, PATH, permissions, troubleshooting, profile
