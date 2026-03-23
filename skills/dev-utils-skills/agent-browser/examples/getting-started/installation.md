# Installation | 安装

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to install agent-browser CLI tool.

### Key Concepts

- npm global installation
- Installing browser binaries
- Building from source
- System dependencies
- Custom executable path

### Example: npm Installation (Recommended)

```bash
# Install agent-browser globally
npm install -g agent-browser

# Install browser binaries
agent-browser install
```

### Example: Building from Source

```bash
# Clone the repository
git clone https://github.com/vercel-labs/agent-browser.git
cd agent-browser

# Install dependencies
pnpm install

# Build the project
pnpm build

# For native builds
pnpm build:native

# Link globally (optional)
pnpm link --global
```

### Example: Linux System Dependencies

```bash
# Install with system dependencies (recommended)
agent-browser install --with-deps

# Or manually install Playwright dependencies
# Ubuntu/Debian
sudo apt-get install -y \
  libnss3 \
  libnspr4 \
  libatk1.0-0 \
  libatk-bridge2.0-0 \
  libcups2 \
  libdrm2 \
  libdbus-1-3 \
  libxkbcommon0 \
  libxcomposite1 \
  libxdamage1 \
  libxfixes3 \
  libxrandr2 \
  libgbm1 \
  libasound2

# Fedora
sudo dnf install -y \
  nss \
  nspr \
  atk \
  at-spi2-atk \
  cups-libs \
  libdrm \
  dbus \
  libxkbcommon \
  libXcomposite \
  libXdamage \
  libXfixes \
  libXrandr \
  mesa-libgbm \
  alsa-lib
```

### Example: Custom Executable Path

```bash
# Set custom browser executable path
export AGENT_BROWSER_EXECUTABLE_PATH=/path/to/chromium

# Or use --executable-path flag
agent-browser open example.com --executable-path /path/to/chromium
```

### Example: Verify Installation

```bash
# Check version
agent-browser --version

# Test basic command
agent-browser open example.com
```

### Key Points

- Install globally with `npm install -g agent-browser`
- Run `agent-browser install` to download browser binaries
- Install system dependencies on Linux
- Use custom executable path if needed
- Verify installation with `--version` flag
