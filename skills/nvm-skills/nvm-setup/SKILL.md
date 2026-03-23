---
name: nvm-setup
description: Configure shell initialization and environment variables so nvm loads correctly across bash, zsh, and fish.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Loading nvm in a new shell session
- Setting NVM_DIR or sourcing nvm.sh
- Bash/zsh/fish profile configuration
- XDG_CONFIG_HOME profile location differences

**Trigger phrases include:**
- "nvm not found", "nvm 命令找不到", "source nvm.sh"
- "NVM_DIR", "profile", "bashrc", "zshrc", "fish"
- "--no-use", "手动加载"

## How to use this skill

**CRITICAL: This skill focuses on shell initialization and environment variables.** For installation or version usage, use other nvm-* skills.

1. Identify the active shell and the correct profile file path.
2. Add NVM_DIR and nvm.sh sourcing lines from the template.
3. Add bash completion or optional config as needed.
4. Start a new shell session and verify nvm loads.

**Important notes:**
- XDG_CONFIG_HOME changes the expected profile path.
- Use --no-use when you only want nvm loaded without switching versions.

### Example file map

- templates/shell-config.md
- examples/environment-variables.md
- examples/bash-completion.md
- examples/bash-completion-usage.md

## Keywords

nvm setup, NVM_DIR, nvm.sh, profile, bash, zsh, fish, XDG_CONFIG_HOME, shell init
