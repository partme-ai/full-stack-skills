# Installation

## Instructions

This example demonstrates how to install nvm on your system.

### Key Concepts

- Installation methods (curl, wget, manual)
- Environment setup
- Shell configuration
- Verification

### Example: Install using curl

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

### Example: Install using wget

```bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

### Example: Manual Installation

```bash
# Clone the repository
git clone https://github.com/nvm-sh/nvm.git ~/.nvm

# Checkout latest release
cd ~/.nvm
git checkout v0.39.0

# Source nvm
. ./nvm.sh
```

### Example: Shell Configuration

After installation, add the following to your shell profile:

**For bash** (`~/.bashrc` or `~/.bash_profile`):
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

**For zsh** (`~/.zshrc`):
```zsh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

### Example: Verify Installation

```bash
# Reload shell configuration
source ~/.bashrc  # or source ~/.zshrc

# Verify nvm is installed
command -v nvm

# Check nvm version
nvm --version
```

### Example: Custom Installation Directory

```bash
# Set custom NVM_DIR before installation
export NVM_DIR="$HOME/custom/path/nvm"
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

### Key Points

- Installation script automatically adds nvm to your shell profile
- Reload your shell or source the profile after installation
- Use `command -v nvm` to verify installation
- Custom `NVM_DIR` can be set before installation
- Manual installation requires sourcing nvm.sh in each shell session
