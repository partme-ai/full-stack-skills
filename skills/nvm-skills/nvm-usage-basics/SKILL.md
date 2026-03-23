---
name: nvm-usage-basics
description: Cover everyday nvm usage for installing, switching, and listing Node versions, including LTS and system node.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Installing a Node version with nvm
- Switching active Node versions
- Listing installed or remote versions
- Using LTS or system node

**Trigger phrases include:**
- "nvm install", "nvm use", "nvm ls", "ls-remote"
- "LTS", "长期支持", "system node", "io.js"

## How to use this skill

**CRITICAL: This skill focuses on basic version management commands.** For default version or .nvmrc, use the defaults skill.

1. Select the required command: install, use, ls, or ls-remote.
2. Choose LTS or specific versions based on stability needs.
3. Confirm available versions before switching.
4. Use system node only when required by the OS.

**Important notes:**
- LTS is recommended for production stability.

### Example file map

- examples/usage.md
- examples/install-version.md
- examples/use-version.md
- examples/list-versions.md
- examples/long-term-support.md
- examples/system-node.md
- examples/iojs.md

## Keywords

nvm use, nvm install, nvm ls, ls-remote, LTS, system node, node versions, 日常使用
