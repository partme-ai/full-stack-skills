# Window API

## API Reference

Electron EGG window management API.

### BrowserWindow

**new BrowserWindow(options)**
- Create new browser window

**Options:**
- `width` - Window width
- `height` - Window height
- `minWidth` - Minimum width
- `minHeight` - Minimum height
- `title` - Window title
- `frame` - Show window frame
- `transparent` - Transparent window
- `resizable` - Resizable window
- `maximizable` - Maximizable window
- `minimizable` - Minimizable window

### Window Methods

**window.loadFile(path)**
- Load HTML file

**window.loadURL(url)**
- Load URL

**window.show()**
- Show window

**window.hide()**
- Hide window

**window.close()**
- Close window

**window.minimize()**
- Minimize window

**window.maximize()**
- Maximize window

**window.restore()**
- Restore window

### Window Events

**window.on('closed', callback)**
- Window closed event

**window.on('ready-to-show', callback)**
- Window ready to show event

**window.on('maximize', callback)**
- Window maximized event

**window.on('unmaximize', callback)**
- Window unmaximized event

**See also:** `examples/features/window-management.md` for detailed examples
