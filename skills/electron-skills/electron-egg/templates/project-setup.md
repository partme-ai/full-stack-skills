# Project Setup Templates

## Basic Project Structure

```
project/
├── main/                    # Main process
│   ├── index.js
│   └── window/
├── renderer/               # Renderer process
│   ├── src/
│   └── index.html
├── config/                 # Configuration
│   └── config.default.js
├── build/                  # Build scripts
└── package.json
```

## Main Process Entry

```javascript
// main/index.js
const { Application } = require('electron-egg')

const app = new Application({
  // Configuration
})

app.start()
```

## Renderer Process Entry

```html
<!-- renderer/index.html -->
<!DOCTYPE html>
<html>
<head>
  <title>My App</title>
</head>
<body>
  <div id="app"></div>
  <script src="./src/index.js"></script>
</body>
</html>
```

## Configuration File

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

## package.json Scripts

```json
{
  "scripts": {
    "dev": "electron-egg dev",
    "build": "electron-egg build",
    "start": "electron-egg start"
  }
}
```
