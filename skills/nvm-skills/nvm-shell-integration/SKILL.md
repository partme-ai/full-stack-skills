---
name: nvm-shell-integration
description: "Configure automatic nvm version switching when changing directories, using shell hooks for bash, zsh, and fish. Covers auto-use on cd, PATH restoration, and nvm deactivate. Use when the user wants automatic Node version switching per project, nvm use to run on directory change, or needs to deactivate nvm and restore system PATH."
license: Complete terms in LICENSE.txt
---

# nvm Shell Integration

Add automatic `nvm use` on directory changes so the correct Node version activates per project.

## Workflow

1. **Add auto-switching for bash** (append to `~/.bashrc`):
   ```bash
   cdnvm() {
     command cd "$@" || return $?
     nvm_path="$(nvm_find_up .nvmrc | command tr -d '\n')"
     if [ -n "$nvm_path" ]; then
       local nvm_node_version=$(nvm version "$(cat "$nvm_path/.nvmrc")")
       if [ "$nvm_node_version" = "N/A" ]; then
         nvm install
       elif [ "$nvm_node_version" != "$(nvm version)" ]; then
         nvm use
       fi
     fi
   }
   alias cd='cdnvm'
   ```

2. **Deactivate nvm and restore PATH** when needed:
   ```bash
   nvm deactivate   # Removes nvm from PATH, restores system node
   nvm use system   # Switch to system-installed Node
   ```

3. **Verify auto-switching works:**
   ```bash
   echo "20" > /tmp/test-project/.nvmrc
   cd /tmp/test-project   # Should auto-switch to Node 20
   node -v                # Should show v20.x.x
   ```

**Note:** Base shell loading belongs to nvm-setup. This skill adds deeper integration on top.

### Example file map

- `examples/shell-integration.md` - Overview of integration options
- `examples/auto-use-bash.md` - Bash auto-switching hook
- `examples/auto-use-zsh.md` - Zsh auto-switching hook
- `examples/auto-use-fish.md` - Fish auto-switching hook
- `examples/restore-path.md` - PATH restoration and nvm deactivate

## Keywords

shell integration, auto use, PATH restore, nvm deactivate, auto switch, cdnvm
