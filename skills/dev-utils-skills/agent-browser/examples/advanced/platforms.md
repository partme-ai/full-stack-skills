# Platforms | 平台支持

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example lists the supported platforms for agent-browser.

### Key Concepts

- Platform support matrix
- Native Rust binary availability
- Node.js fallback
- Platform-specific considerations

### Platform Support

| Platform | Binary | Fallback |
|----------|--------|----------|
| macOS ARM64 | Native Rust | Node.js |
| macOS x64 | Native Rust | Node.js |
| Linux ARM64 | Native Rust | Node.js |
| Linux x64 | Native Rust | Node.js |
| Windows x64 | Native Rust | Node.js |

### Installation by Platform

**macOS:**
```bash
npm install -g agent-browser
agent-browser install
```

**Linux:**
```bash
npm install -g agent-browser
agent-browser install --with-deps  # Install system dependencies
```

**Windows:**
```bash
npm install -g agent-browser
agent-browser install
```

### Platform-Specific Notes

**macOS:**
- Native Rust binary available for ARM64 and x64
- Falls back to Node.js if binary unavailable
- No additional system dependencies required

**Linux:**
- Native Rust binary available for ARM64 and x64
- Requires system dependencies (install with `--with-deps`)
- Falls back to Node.js if binary unavailable

**Windows:**
- Native Rust binary available for x64
- Falls back to Node.js if binary unavailable
- No additional system dependencies required

### Key Points

- Native Rust binary available for all major platforms
- Node.js fallback ensures compatibility
- Linux requires system dependencies
- All platforms support headless and headed modes
- Cross-platform compatibility maintained
