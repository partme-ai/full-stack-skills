# Use Node.js Version

## Instructions

This example demonstrates how to switch between Node.js versions using nvm.

### Key Concepts

- Switching versions
- Using aliases
- Using .nvmrc files
- Version activation

### Example: Switch to Specific Version

```bash
# Switch to specific version
nvm use 18.17.0

# Switch to latest version
nvm use node

# Switch to default version
nvm use default
```

### Example: Use LTS Version

```bash
# Use latest LTS
nvm use --lts

# Use specific LTS alias
nvm use lts/hydrogen
nvm use lts/iron
```

### Example: Use from .nvmrc File

```bash
# Create .nvmrc file in project
echo "18.17.0" > .nvmrc

# Use version from .nvmrc
nvm use

# Auto-use when entering directory (requires shell integration)
nvm use --silent
```

### Example: Use Alias

```bash
# Use version by alias
nvm use stable
nvm use my-alias
```

### Example: Verify Current Version

```bash
# Check current version
nvm current

# Or use node command
node --version
npm --version
```

### Key Points

- `nvm use` activates a version in current shell
- Version must be installed before use
- `.nvmrc` files specify project Node.js version
- Changes only affect current shell session
- Use `nvm current` to check active version
