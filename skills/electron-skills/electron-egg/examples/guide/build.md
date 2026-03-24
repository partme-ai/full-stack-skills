# Build and Package

**官方文档**: https://www.kaka996.com/,


## Instructions

This example demonstrates how to build and package Electron EGG applications.

### Key Concepts

- Build process
- Package configuration
- Platform-specific builds
- Distribution

### Example: Build Process

```bash
# Build for production
npm run build

# Build for specific platform
npm run build:win
npm run build:mac
npm run build:linux
```

### Example: Package Configuration

```json
{
  "build": {
    "appId": "com.example.myapp",
    "productName": "My App",
    "directories": {
      "output": "dist"
    },
    "files": [
      "main/**/*",
      "renderer/**/*",
      "config/**/*"
    ]
  }
}
```

### Example: Platform-Specific Builds

```bash
# Windows
npm run build:win

# macOS
npm run build:mac

# Linux
npm run build:linux

# All platforms
npm run build:all
```

### Example: Distribution

After building, distribution files are in the `dist` directory:
- Windows: `.exe` installer
- macOS: `.dmg` or `.pkg`
- Linux: `.AppImage` or `.deb`

### Key Points

- Use npm run build for production
- Configure build options
- Support multiple platforms
- Output to dist directory
- Follow platform conventions
