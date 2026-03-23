# IPC API

## API Reference

Electron EGG IPC communication API.

### Main Process (ipcMain)

**ipcMain.on(channel, listener)**
- Listen for IPC messages from renderer

**ipcMain.once(channel, listener)**
- Listen for IPC message once

**ipcMain.handle(channel, listener)**
- Handle IPC requests (async)

**ipcMain.removeListener(channel, listener)**
- Remove IPC listener

**ipcMain.removeAllListeners(channel)**
- Remove all listeners for channel

### Renderer Process (ipcRenderer)

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

### Event Object

**event.sender**
- WebContents that sent the message

**event.reply(channel, ...args)**
- Reply to sender

**event.returnValue**
- Return value for synchronous messages

**See also:** `examples/features/ipc-communication.md` for detailed examples
