# Renderer Process

**官方文档**: https://www.kaka996.com/,


## Instructions

This example demonstrates renderer process usage in Electron EGG.

### Key Concepts

- Renderer process entry
- UI rendering
- IPC communication
- DOM manipulation

### Example: Renderer Process Entry

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

### Example: UI Rendering

```javascript
// renderer/src/index.js
document.addEventListener('DOMContentLoaded', () => {
  const app = document.getElementById('app')
  app.innerHTML = '<h1>Hello Electron EGG</h1>'
})
```

### Example: IPC Communication

```javascript
// renderer/src/index.js
const { ipcRenderer } = require('electron')

// Send message to main process
ipcRenderer.send('message', { data: 'Hello' })

// Listen for reply
ipcRenderer.on('reply', (event, data) => {
  console.log('Received:', data)
})
```

### Example: DOM Manipulation

```javascript
// renderer/src/index.js
const button = document.getElementById('button')
button.addEventListener('click', () => {
  console.log('Button clicked')
})
```

### Key Points

- Renderer process runs in browser
- Use HTML/CSS/JavaScript
- Communicate via IPC
- Access DOM APIs
- Limited Node.js access
