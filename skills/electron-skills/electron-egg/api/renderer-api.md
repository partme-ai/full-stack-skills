# Renderer Process API

## API Reference

Electron EGG renderer process API.

### ipcRenderer

**ipcRenderer.send(channel, ...args)**
- Send message to main process

**ipcRenderer.sendSync(channel, ...args)**
- Send synchronous message to main process

**ipcRenderer.on(channel, listener)**
- Listen for IPC messages from main

**ipcRenderer.once(channel, listener)**
- Listen for IPC message once

**ipcRenderer.invoke(channel, ...args)**
- Invoke handler in main process (async)

**ipcRenderer.removeListener(channel, listener)**
- Remove IPC listener

**ipcRenderer.removeAllListeners(channel)**
- Remove all listeners for channel

### remote (deprecated)

**remote.require(module)**
- Require module from main process (deprecated in Electron 12+)

**remote.getCurrentWindow()**
- Get current window (deprecated)

### contextBridge (Electron 12+)

**contextBridge.exposeInMainWorld(apiKey, api)**
- Expose API to renderer process securely

**Example:**
```javascript
// Main process
const { contextBridge } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  send: (channel, data) => ipcRenderer.send(channel, data),
  on: (channel, callback) => ipcRenderer.on(channel, callback)
})
```

### DOM APIs

Renderer process has access to all standard DOM APIs:
- `document` - Document object
- `window` - Window object
- `localStorage` - Local storage
- `sessionStorage` - Session storage

**See also:** `examples/features/renderer-process.md` for detailed examples
