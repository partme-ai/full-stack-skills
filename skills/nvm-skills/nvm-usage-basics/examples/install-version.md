# Install Node.js Version

## Instructions

This example demonstrates how to install Node.js versions using nvm.

### Key Concepts

- Installing specific versions
- Installing latest version
- Installing LTS versions
- Installing from aliases

### Example: Install Specific Version

```bash
# Install specific version
nvm install 18.17.0

# Install and use immediately
nvm install 18.17.0 --default
```

### Example: Install Latest Version

```bash
# Install latest Node.js version
nvm install node

# Install latest and set as default
nvm install node --default
```

### Example: Install LTS Version

```bash
# Install latest LTS version
nvm install --lts

# Install specific LTS alias
nvm install lts/hydrogen
nvm install lts/iron
```

### Example: Install from Alias

```bash
# Install using alias
nvm install stable
nvm install iojs
```

### Example: Install and Reinstall npm

```bash
# Install version and reinstall npm
nvm install 18.17.0 --reinstall-packages-from=current

# Install and use npm version
nvm install 18.17.0 --latest-npm
```

### Example: Install with Custom Options

```bash
# Install with custom npm version
nvm install 18.17.0 --npm=9.0.0

# Install without npm
nvm install 18.17.0 --no-npm
```

### Key Points

- Each version installs with its bundled npm
- Use `--default` to set as default version
- LTS versions are recommended for production
- `node` alias refers to latest version
- `--reinstall-packages-from` copies packages from current version
