---
name: nvm-install
description: "Install and update nvm (Node Version Manager) using curl/wget scripts, git clone, or manual methods. Covers profile selection, NVM_DIR configuration, and Alpine Linux support. Use when the user asks to install nvm, update nvm, set up nvm for the first time, or troubleshoot nvm installation scripts."
license: Complete terms in LICENSE.txt
---

# Install and Update nvm

Install or upgrade nvm from the official source using script, git, or manual methods.

## Workflow

1. **Identify platform and shell** (macOS, Linux, WSL, Alpine; bash/zsh/fish).

2. **Install via curl or wget:**
   ```bash
   # Using curl
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

   # Using wget
   wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
   ```

3. **Verify the profile was updated** (the script writes to `~/.bashrc`, `~/.zshrc`, or `~/.profile`):
   ```bash
   # Required lines in your profile:
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
   ```

4. **Verify installation:**
   ```bash
   # Restart terminal, then:
   nvm --version
   ```

5. **Override PROFILE** if the auto-detection picked the wrong file:
   ```bash
   PROFILE=/path/to/custom/profile curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
   ```

**Notes:**
- The install script writes to the detected profile unless PROFILE is explicitly set.
- For restricted networks, use the nvm-mirror-and-auth skill instead.
- Usage, .nvmrc, or troubleshooting belong to other nvm-* skills.

### Example file map

- `examples/installation.md` - Standard installation
- `examples/install-update-script.md` - Updating existing nvm
- `examples/install-additional-notes.md` - Platform-specific notes
- `examples/git-install.md` - Git-based installation
- `examples/manual-install.md` - Manual installation
- `examples/manual-upgrade.md` - Manual upgrade steps
- `examples/alpine-install.md` - Alpine Linux installation

## Keywords

nvm install, install.sh, PROFILE, NVM_DIR, NVM_SOURCE, curl, wget, manual install, update
