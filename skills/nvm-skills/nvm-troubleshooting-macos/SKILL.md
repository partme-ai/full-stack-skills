---
name: nvm-troubleshooting-macos
description: "Diagnose and fix nvm issues on macOS, including zsh/bash profile not loading, PATH priority conflicts, permission errors, and Homebrew Node conflicts. Use when the user reports nvm not found on macOS, nvm command not working in zsh or Terminal, or PATH priority issues after macOS updates."
license: Complete terms in LICENSE.txt
---

# nvm Troubleshooting (macOS)

Diagnose and fix common nvm problems on macOS including profile loading and PATH conflicts.

## Workflow

1. **Run diagnostic checks:**
   ```bash
   echo "Shell: $SHELL"
   echo "NVM_DIR: $NVM_DIR"
   cat ~/.zshrc | grep -n nvm
   echo $PATH | tr ':' '\n' | head -10
   ```

2. **Check profile load order** (macOS zsh reads these in order):
   - `~/.zshenv` (always)
   - `~/.zprofile` (login shells)
   - `~/.zshrc` (interactive shells)

3. **Fix the most common issue** (nvm lines missing from `~/.zshrc`):
   ```bash
   # Add to ~/.zshrc:
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
   ```

4. **Verify the fix:**
   ```bash
   source ~/.zshrc
   command -v nvm   # Should print "nvm"
   nvm --version
   node -v
   ```

**Note:** General verification belongs to nvm-verify. For Linux/WSL issues, use nvm-troubleshooting-linux.

### Example file map

- `examples/troubleshooting-macos.md` - macOS-specific troubleshooting
- `examples/macos-troubleshooting.md` - Additional macOS guidance
- `examples/problems.md` - Common problems and solutions
- `examples/compatibility-issues.md` - Known compatibility issues

## Keywords

macos, zsh, bash, PATH, permissions, troubleshooting, profile, nvm not found
