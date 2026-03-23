# Configuration

**官方文档**: https://www.kaka996.com/,


## Instructions

This example demonstrates how to configure Electron EGG.

### Key Concepts

- Configuration files
- App info configuration
- Window configuration
- Plugin configuration

### Example: Configuration Files

```javascript
// config/config.default.js
module.exports = {
  appInfo: {
    name: 'my-app',
    baseDir: __dirname,
    env: 'local',
    home: process.env.HOME,
    root: process.cwd(),
    appUserDataDir: ''
  }
}
```

### Example: App Info Configuration

```javascript
module.exports = {
  appInfo: {
    name: 'my-app',           // App name
    baseDir: __dirname,        // Base directory
    env: 'local',              // Environment
    home: process.env.HOME,    // Home directory
    root: process.cwd(),       // Root directory
    appUserDataDir: ''        // User data directory
  }
}
```

### Example: Window Configuration

```javascript
module.exports = {
  mainWindow: {
    width: 1200,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    title: 'My App',
    frame: true,
    transparent: false
  }
}
```

### Example: Plugin Configuration

```javascript
module.exports = {
  addons: {
    tray: {
      enable: true
    },
    security: {
      enable: true
    },
    autoUpdater: {
      enable: false
    }
  }
}
```

### Key Points

- Configure in config files
- Support multiple environments
- Window configuration options
- Plugin enable/disable
- Environment-specific configs
