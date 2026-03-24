# Project Structure

**官方文档**: https://www.kaka996.com/,


## Instructions

This example explains Electron EGG project structure.

### Key Concepts

- Directory structure
- File organization
- Configuration files
- Process separation

### Example: Directory Structure

```
project/
├── main/                    # Main process
│   ├── index.js            # Main entry
│   ├── window/             # Window management
│   ├── menu/               # Menu
│   └── tray/               # System tray
├── renderer/               # Renderer process
│   ├── src/                # Source code
│   ├── public/             # Static files
│   └── index.html          # Entry HTML
├── config/                 # Configuration
│   ├── config.default.js   # Default config
│   └── config.prod.js      # Production config
├── build/                  # Build scripts
├── public/                 # Public resources
└── package.json
```

### Example: Main Process Files

```javascript
// main/index.js
const { Application } = require('electron-egg')

const app = new Application({
  // Configuration
})

app.start()
```

### Example: Renderer Process Files

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

### Key Points

- Separate main and renderer processes
- Organize files by process
- Configuration in config directory
- Build scripts in build directory
- Follow project structure conventions
