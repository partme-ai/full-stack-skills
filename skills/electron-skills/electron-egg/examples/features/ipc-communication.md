# IPC Communication

**官方文档**: https://www.kaka996.com/,


## Instructions

This example demonstrates IPC communication in Electron EGG.

### Key Concepts

- IPC channels
- Message sending
- Message receiving
- Event handling

### Example: Main Process IPC

```javascript
// main/index.js
const { ipcMain } = require('electron')

// Listen for messages
ipcMain.on('message', (event, data) => {
  console.log('Received:', data)
  
  // Reply to renderer
  event.reply('reply', { status: 'success' })
})

// Handle synchronous messages
ipcMain.on('sync-message', (event, data) => {
  event.returnValue = 'Response'
})
```

### Example: Renderer Process IPC

```javascript
// renderer/src/index.js
const { ipcRenderer } = require('electron')

// Send message to main process
ipcRenderer.send('message', { data: 'Hello' })

// Listen for reply
ipcRenderer.on('reply', (event, data) => {
  console.log('Received:', data)
})

// Send synchronous message
const result = ipcRenderer.sendSync('sync-message', { data: 'Hello' })
console.log('Result:', result)
```

### Example: IPC Channels

```javascript
// Define IPC channels
const IPC_CHANNELS = {
  GET_DATA: 'get-data',
  SET_DATA: 'set-data',
  NOTIFY: 'notify'
}

// Main process
ipcMain.on(IPC_CHANNELS.GET_DATA, (event) => {
  event.reply(IPC_CHANNELS.GET_DATA, { data: 'value' })
})

// Renderer process
ipcRenderer.send(IPC_CHANNELS.GET_DATA)
ipcRenderer.on(IPC_CHANNELS.GET_DATA, (event, data) => {
  console.log('Data:', data)
})
```

### Key Points

- Use ipcMain in main process
- Use ipcRenderer in renderer process
- Define IPC channels
- Handle async and sync messages
- Proper error handling
