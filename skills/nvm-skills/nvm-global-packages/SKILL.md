---
name: nvm-global-packages
description: "Migrate npm global packages between Node versions using reinstall-packages-from, and define a default-packages file to auto-install globals on every new version. Use when the user asks about keeping global packages after switching Node versions, setting up default npm packages, or troubleshooting missing global packages after nvm install."
license: Complete terms in LICENSE.txt
---

# nvm Global Packages

Manage global npm packages across Node version switches to avoid losing tools like eslint, typescript, or pm2.

## Workflow

1. **Migrate global packages** when installing a new version:
   ```bash
   # Install Node 20 and copy global packages from Node 18
   nvm install 20 --reinstall-packages-from=18

   # Verify packages migrated
   npm list -g --depth=0
   ```

2. **Configure default-packages** for automatic installation on every new version:
   ```bash
   # Create the default-packages file
   cat > "$NVM_DIR/default-packages" << 'EOF'
   typescript
   eslint
   pm2
   nodemon
   EOF

   # New installs will auto-install these packages
   nvm install 22  # typescript, eslint, pm2, nodemon installed automatically
   ```

3. **Verify and validate** global packages:
   ```bash
   npm list -g --depth=0
   ```

**Warning:** Global packages are version-specific. Switching versions without `--reinstall-packages-from` means previously installed globals will not be available.

### Example file map

- `examples/migrate-global-packages.md` - Migration between versions
- `examples/default-global-packages.md` - Default packages file setup

## Keywords

global packages, default-packages, reinstall-packages-from, npm global, consistency
