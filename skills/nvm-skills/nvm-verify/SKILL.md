---
name: nvm-verify
description: "Verify nvm installation is working correctly by checking nvm, node, and npm commands, diagnosing PATH order, and inspecting profile loading. Use when the user reports nvm command not found, wants to verify nvm is installed, or needs to diagnose why nvm is not loading in new terminal sessions."
license: Complete terms in LICENSE.txt
---

# Verify nvm Installation

Run diagnostic checks to confirm nvm is installed and loading correctly.

## Workflow

1. **Check nvm, node, and npm:**
   ```bash
   nvm --version    # Should print nvm version (e.g., 0.40.1)
   node -v          # Should print Node version
   npm -v           # Should print npm version
   command -v nvm   # Should print "nvm" (it's a shell function)
   ```

2. **If nvm is not found, inspect the profile:**
   ```bash
   # Check which profile is loaded
   echo $SHELL
   # Inspect for nvm lines:
   grep -n "nvm" ~/.bashrc ~/.zshrc ~/.profile 2>/dev/null
   ```

3. **Check PATH and NVM_DIR:**
   ```bash
   echo "NVM_DIR=$NVM_DIR"
   echo $PATH | tr ':' '\n' | grep nvm
   ls -la "$NVM_DIR/nvm.sh" 2>/dev/null && echo "nvm.sh exists" || echo "nvm.sh NOT FOUND"
   ```

4. **Fix and verify** in a new terminal session:
   ```bash
   # After fixing profile, open a new terminal:
   command -v nvm && echo "nvm OK" || echo "nvm still broken"
   ```

**Important:** nvm is a shell function, not a binary, so the profile must load correctly. For deeper platform issues, use nvm-troubleshooting-macos or nvm-troubleshooting-linux.

### Example file map

- `examples/verify-installation.md` - Full verification checklist
- `examples/problems.md` - Common problems and solutions
- `examples/restore-path.md` - PATH restoration
- `examples/important-notes.md` - Key things to know about nvm

## Keywords

nvm verify, nvm --version, node -v, npm -v, PATH, profile, verification, nvm not found
