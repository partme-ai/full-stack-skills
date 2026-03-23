# Different History Modes | 不同的历史模式

**官方文档**: https://router.vuejs.org/guide/essentials/history-mode.html


## Instructions

This example demonstrates the different history modes available in Vue Router: hash mode, HTML5 history mode, and memory mode.

### Key Concepts

- Hash mode (`createWebHashHistory`)
- HTML5 history mode (`createWebHistory`)
- Memory mode (`createMemoryHistory`)
- When to use each mode
- Server configuration for HTML5 history mode

### Example: Hash Mode

```javascript
// router/index.js
import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// URLs will look like: http://example.com/#/home
```

### Example: HTML5 History Mode

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes
})

// URLs will look like: http://example.com/home
```

### Example: HTML5 History with Base Path

```javascript
const router = createRouter({
  history: createWebHistory('/my-app/'),
  routes
})

// URLs will look like: http://example.com/my-app/home
```

### Example: Memory Mode

```javascript
// router/index.js
import { createRouter, createMemoryHistory } from 'vue-router'

const router = createRouter({
  history: createMemoryHistory(),
  routes
})

// Used in SSR or testing environments
```

### Example: Server Configuration for HTML5 History

**Nginx:**
```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

**Apache (.htaccess):**
```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```

**Express:**
```javascript
const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname, 'dist')))

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'))
})
```

### Example: Choosing the Right Mode

```javascript
// Development: Use hash mode for simplicity
const router = createRouter({
  history: process.env.NODE_ENV === 'development' 
    ? createWebHashHistory() 
    : createWebHistory(),
  routes
})
```

### Key Points

- **Hash mode**: Works without server configuration, URLs have `#`, good for simple deployments
- **HTML5 history mode**: Clean URLs, requires server configuration, better for production
- **Memory mode**: No URL changes, used in SSR and testing
- Hash mode is easier to deploy but has less clean URLs
- HTML5 history mode requires server fallback to `index.html`
- Choose based on deployment environment and requirements
