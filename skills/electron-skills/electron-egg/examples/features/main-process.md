# Main Process

**官方文档**: https://www.kaka996.com/,


## Instructions

This example demonstrates main process usage in Electron EGG.

### Key Concepts

- Main process entry
- Application lifecycle
- Window management
- IPC handling

### Example: Main Process Entry

```javascript
// main/index.js
const { Application } = require('electron-egg')

const app = new Application({
  // Configuration
})

app.start()
```

### Example: Application Lifecycle

```javascript
// main/index.js
const { Application } = require('electron-egg')

const app = new Application()

app.on('ready', () => {
  console.log('Application ready')
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.start()
```

### Example: Window Management

```javascript
// main/window/main.js
const { BrowserWindow } = require('electron')

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800
  })

  win.loadFile('renderer/index.html')
  
  return win
}

module.exports = { createWindow }
```

### Example: IPC Handling

```javascript
// main/index.js
const { ipcMain } = require('electron')

ipcMain.on('message', (event, data) => {
  console.log('Received:', data)
  event.reply('reply', 'Response')
})
```

### Key Points

- Main process runs in Node.js
- Handle application lifecycle
- Manage windows
- Handle IPC communication
- Access Node.js APIs
