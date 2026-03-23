# Configuration Templates

## Basic Configuration

```javascript
// config/config.default.js
module.exports = {
  appInfo: {
    name: 'my-app',
    baseDir: __dirname,
    env: 'local'
  }
}
```

## Window Configuration

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

## Plugin Configuration

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

## Environment-Specific Configuration

```javascript
// config/config.prod.js
module.exports = {
  appInfo: {
    env: 'prod'
  },
  mainWindow: {
    width: 1400,
    height: 900
  }
}
```
