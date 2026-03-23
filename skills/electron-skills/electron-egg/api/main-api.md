# Main Process API

## API Reference

Electron EGG main process API.

### Application Class

**new Application(options)**
- Create new application instance

**app.start()**
- Start the application

**app.on(event, callback)**
- Listen to application events

### BrowserWindow

**new BrowserWindow(options)**
- Create new browser window

**window.loadFile(path)**
- Load HTML file

**window.loadURL(url)**
- Load URL

**window.webContents.send(channel, ...args)**
- Send message to renderer

### ipcMain

**ipcMain.on(channel, listener)**
- Listen for IPC messages

**ipcMain.handle(channel, listener)**
- Handle IPC requests

**ipcMain.removeListener(channel, listener)**
- Remove IPC listener

### app

**app.quit()**
- Quit the application

**app.getPath(name)**
- Get application path

**app.on(event, callback)**
- Listen to app events

**See also:** `examples/features/main-process.md` for detailed examples
