# Quick Start

**官方文档**: https://www.kaka996.com/,


## Instructions

This example provides a quick start guide for Electron EGG.

### Key Concepts

- Project structure
- Start development
- Build application
- Basic configuration

### Example: Project Structure

```
electron-egg/
├── main/              # Main process
├── renderer/          # Renderer process
├── public/            # Static resources
├── config/            # Configuration files
├── build/             # Build scripts
└── package.json
```

### Example: Start Development

```bash
# Start development server
npm run dev

# Or using yarn
yarn dev

# Or using pnpm
pnpm dev
```

### Example: Build Application

```bash
# Build for production
npm run build

# Or using yarn
yarn build

# Or using pnpm
pnpm build
```

### Example: Basic Configuration

```javascript
// config/config.default.js
module.exports = {
  appInfo: {
    name: 'my-app',
    baseDir: __dirname,
    env: 'local'
  },
  mainWindow: {
    width: 1200,
    height: 800
  }
}
```

### Key Points

- Use npm run dev for development
- Use npm run build for production
- Configure in config files
- Follow project structure
- Support hot reload in development
