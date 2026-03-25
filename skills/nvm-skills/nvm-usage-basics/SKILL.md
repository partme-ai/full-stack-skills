---
name: nvm-usage-basics
description: "Manage Node.js versions with everyday nvm commands: install specific versions, switch active versions, list installed and remote versions, and use LTS releases. Use when the user asks about nvm install, nvm use, nvm ls, listing available Node versions, or switching between Node versions."
license: Complete terms in LICENSE.txt
---

# nvm Usage Basics

Install, switch, and list Node.js versions using core nvm commands.

## Workflow

1. **List available remote versions:**
   ```bash
   nvm ls-remote              # All available versions
   nvm ls-remote --lts        # Only LTS releases
   nvm ls-remote | grep v20   # Filter specific major version
   ```

2. **Install a Node version:**
   ```bash
   nvm install 20             # Latest v20.x
   nvm install 20.11.0        # Exact version
   nvm install --lts          # Latest LTS release
   nvm install node           # Latest current release
   ```

3. **Switch between versions:**
   ```bash
   nvm use 20                 # Switch to v20.x
   nvm use --lts              # Switch to latest LTS
   nvm use system             # Use system-installed Node
   ```

4. **List installed versions and verify:**
   ```bash
   nvm ls                     # Show installed versions
   nvm current                # Show active version
   node -v                    # Confirm active version
   ```

**Note:** For default version or .nvmrc, use the nvm-defaults-and-nvmrc skill. LTS is recommended for production stability.

### Example file map

- `examples/usage.md` - General usage overview
- `examples/install-version.md` - Version installation details
- `examples/use-version.md` - Switching versions
- `examples/list-versions.md` - Listing and filtering versions
- `examples/long-term-support.md` - LTS management
- `examples/system-node.md` - System Node usage
- `examples/iojs.md` - io.js compatibility

## Keywords

nvm use, nvm install, nvm ls, ls-remote, LTS, system node, node versions
