---
name: nvm-uninstall
description: "Remove nvm completely by deleting NVM_DIR, cleaning nvm lines from shell profiles, and restoring system Node PATH priority. Use when the user asks to uninstall nvm, remove node version manager, clean up nvm installation, or restore their system to use the system-installed Node."
license: Complete terms in LICENSE.txt
---

# Uninstall nvm

Completely remove nvm and restore the system to its pre-nvm state.

## Workflow

1. **Remove the nvm directory:**
   ```bash
   rm -rf "$NVM_DIR"
   # Usually: rm -rf ~/.nvm
   ```

2. **Remove nvm lines from shell profile** (`~/.bashrc`, `~/.zshrc`, or `~/.profile`):
   ```bash
   # Delete these lines from your profile:
   # export NVM_DIR="$HOME/.nvm"
   # [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   # [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
   ```

3. **Verify nvm is removed:**
   ```bash
   # Open a new terminal, then:
   command -v nvm    # Should return nothing
   which node        # Should show system Node path (e.g., /usr/local/bin/node)
   node -v           # Should show system Node version
   ```

**Warning:** This permanently removes all nvm-managed Node versions. Back up any global packages first with `npm list -g --depth=0`.

### Example file map

- `examples/uninstall.md` - Step-by-step uninstall guide
- `examples/restore-path.md` - PATH restoration details
- `examples/system-node.md` - Switching to system Node

## Keywords

nvm uninstall, remove, cleanup, PATH restore, system node
