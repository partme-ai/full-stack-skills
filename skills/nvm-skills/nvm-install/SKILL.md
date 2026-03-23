---
name: nvm-install
description: Provide comprehensive guidance for installing and updating nvm from the official README, including install scripts, profile selection, and required environment variables.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Installing nvm for the first time
- Updating nvm using install.sh
- PROFILE, NVM_DIR, or NVM_SOURCE configuration
- Choosing curl vs wget installation

**Trigger phrases include:**
- "install nvm", "安装 nvm", "update nvm", "升级 nvm"
- "install.sh", "PROFILE", "NVM_DIR", "NVM_SOURCE"
- "curl 安装", "wget 安装", "脚本安装"

## How to use this skill

**CRITICAL: This skill only covers installation and update workflows.** Redirect usage, .nvmrc, or troubleshooting to the relevant nvm-* skills.

1. Identify platform and shell (macOS, Linux, WSL, Alpine; bash/zsh/fish).
2. Select the install path: script install, git install, or manual install.
3. Follow the official install/update steps and note profile write behavior.
4. Verify PROFILE selection and required environment variables.
5. If upgrading, follow install script update or manual upgrade steps.

**Important notes:**
- The install script writes to the detected profile unless PROFILE is explicitly set.
- For restricted networks, use the mirror/auth skill instead.

### Example file map

- examples/installation.md
- examples/install-update-script.md
- examples/install-additional-notes.md
- examples/git-install.md
- examples/manual-install.md
- examples/manual-upgrade.md
- examples/alpine-install.md

## Keywords

nvm install, install.sh, PROFILE, NVM_DIR, NVM_SOURCE, curl, wget, manual install, update, 安装, 升级
