---
name: nvm-troubleshooting-linux
description: "Diagnose and fix nvm issues on Linux and WSL, including profile not loading, PATH errors, distro-specific differences, and Alpine compatibility problems. Use when the user reports nvm not found on Linux, nvm command not working in WSL, or distro-specific nvm issues."
license: Complete terms in LICENSE.txt
---

# nvm Troubleshooting (Linux/WSL)

Diagnose and fix common nvm problems on Linux distributions and Windows Subsystem for Linux.

## Workflow

1. **Run diagnostic checks:**
   ```bash
   echo "Shell: $SHELL"
   echo "NVM_DIR: $NVM_DIR"
   cat ~/.bashrc | grep -n nvm
   echo $PATH | tr ':' '\n' | grep nvm
   ```

2. **Identify the distro and shell:**
   ```bash
   cat /etc/os-release | head -2
   echo $SHELL
   # WSL check:
   uname -r | grep -i microsoft && echo "WSL detected"
   ```

3. **Fix profile loading issues** (most common problem):
   ```bash
   # Ensure these lines are in ~/.bashrc (not just ~/.profile):
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   ```

4. **Verify the fix:**
   ```bash
   source ~/.bashrc
   command -v nvm   # Should print "nvm"
   nvm --version
   ```

**Note:** Installation steps belong to nvm-install. For macOS issues, use nvm-troubleshooting-macos.

### Example file map

- `examples/troubleshooting-linux.md` - Linux-specific troubleshooting
- `examples/wsl-troubleshooting.md` - WSL-specific issues
- `examples/alpine-install.md` - Alpine Linux guidance
- `examples/problems.md` - Common problems and solutions
- `examples/compatibility-issues.md` - Known compatibility issues

## Keywords

linux, wsl, troubleshooting, PATH, profile, compatibility, alpine, nvm not found
