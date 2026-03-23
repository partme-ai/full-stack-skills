# Configuration API

## API Reference

Electron EGG configuration API.

### Configuration Files

Configuration files are in the `config/` directory:
- `config.default.js` - Default configuration
- `config.local.js` - Local development configuration
- `config.prod.js` - Production configuration

### App Info Configuration

```javascript
appInfo: {
  name: string,           // App name
  baseDir: string,        // Base directory
  env: string,            // Environment
  home: string,           // Home directory
  root: string,           // Root directory
  appUserDataDir: string  // User data directory
}
```

### Window Configuration

```javascript
mainWindow: {
  width: number,          // Window width
  height: number,         // Window height
  minWidth: number,       // Minimum width
  minHeight: number,      // Minimum height
  title: string,          // Window title
  frame: boolean,         // Show frame
  transparent: boolean    // Transparent window
}
```

### Plugin Configuration

```javascript
addons: {
  tray: {
    enable: boolean       // Enable system tray
  },
  security: {
    enable: boolean       // Enable security
  },
  autoUpdater: {
    enable: boolean       // Enable auto updater
  }
}
```

### Environment Variables

- `NODE_ENV` - Node environment
- `ELECTRON_EGG_ENV` - Electron EGG environment

**See also:** `examples/guide/configuration.md` for detailed examples
