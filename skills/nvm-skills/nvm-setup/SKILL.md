---
name: nvm-setup
description: "Configure shell initialization files so nvm loads correctly in bash, zsh, and fish. Covers NVM_DIR, nvm.sh sourcing, profile file selection, XDG_CONFIG_HOME, and bash completion. Use when the user reports nvm not found after installation, needs to configure shell profiles, or wants to set up nvm environment variables."
license: Complete terms in LICENSE.txt
---

# nvm Shell Setup

Configure shell profiles so nvm loads automatically on every new terminal session.

## Workflow

1. **Identify the shell and profile file:**
   - bash: `~/.bashrc` (or `~/.bash_profile` on macOS)
   - zsh: `~/.zshrc`
   - fish: `~/.config/fish/config.fish`
   - With XDG_CONFIG_HOME: `$XDG_CONFIG_HOME/bash/bashrc` etc.

2. **Add nvm initialization** to the correct profile:
   ```bash
   # Required lines for bash/zsh:
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
   ```

3. **Optional: Load nvm without switching versions** (faster shell startup):
   ```bash
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" --no-use
   ```

4. **Verify nvm loads** in a new shell:
   ```bash
   # Open a new terminal, then:
   command -v nvm    # Should print "nvm"
   nvm --version     # Should print version number
   ```

**Notes:**
- XDG_CONFIG_HOME changes the expected profile path.
- Use `--no-use` when you only want nvm loaded without switching versions.
- For installation, use the nvm-install skill. For version usage, use nvm-usage-basics.

### Example file map

- `templates/shell-config.md` - Profile configuration templates
- `examples/environment-variables.md` - Environment variable reference
- `examples/bash-completion.md` - Bash completion setup
- `examples/bash-completion-usage.md` - Completion usage examples

## Keywords

nvm setup, NVM_DIR, nvm.sh, profile, bash, zsh, fish, XDG_CONFIG_HOME, shell init
