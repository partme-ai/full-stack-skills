---
name: nvm-defaults-and-nvmrc
description: "Set default Node versions via nvm aliases, create .nvmrc files for project-specific versions, and configure shell auto-switching per directory. Use when the user asks about nvm alias default, .nvmrc configuration, auto-switching Node versions on directory change, or pinning a Node version for a project."
license: Complete terms in LICENSE.txt
---

# nvm Defaults and .nvmrc

Configure default Node versions and project-level version pinning with nvm.

## Workflow

1. **Set the default Node version** using an alias:
   ```bash
   nvm alias default 20
   # Or use an LTS alias
   nvm alias default lts/iron
   ```

2. **Create or update .nvmrc** in the project root:
   ```bash
   # Pin to a specific version
   echo "20.11.0" > .nvmrc
   # Or use an LTS alias
   echo "lts/iron" > .nvmrc
   ```

3. **Enable shell auto-switching** if requested (see auto-use examples per shell).

4. **Verify** the configuration works:
   ```bash
   # Open a new shell, then:
   nvm current        # Should show the default version
   cd /path/to/project
   node -v            # Should match .nvmrc version
   ```

**Important:** Keep .nvmrc consistent across team repos to avoid version drift. Basic install/use belongs to nvm-usage-basics.

### Example file map

- `examples/default-version.md` - Setting default aliases
- `examples/nvmrc.md` - .nvmrc file creation and usage
- `examples/auto-use-bash.md` - Auto-switching for bash
- `examples/auto-use-zsh.md` - Auto-switching for zsh
- `examples/auto-use-fish.md` - Auto-switching for fish

## Keywords

nvm alias, default version, .nvmrc, auto use, project version, defaults
