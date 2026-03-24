# Shell Configuration Templates

## Bash Configuration

**For `~/.bashrc` or `~/.bash_profile`:**

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

## Zsh Configuration

**For `~/.zshrc`:**

```zsh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

## Fish Shell Configuration

**For `~/.config/fish/config.fish`:**

```fish
set -gx NVM_DIR "$HOME/.nvm"
function nvm
    bass source "$NVM_DIR/nvm.sh" ';' nvm $argv
end
```

## Custom NVM_DIR

**If using custom installation directory:**

```bash
export NVM_DIR="$HOME/custom/path/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

## XDG_CONFIG_HOME Setup

**If using XDG_CONFIG_HOME:**

```bash
export XDG_CONFIG_HOME="$HOME/.config"
export NVM_DIR="$XDG_CONFIG_HOME/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

## Reload Configuration

After adding to shell config:

```bash
# For bash
source ~/.bashrc

# For zsh
source ~/.zshrc
```
