## Instructions

- Use proxy for backend APIs in dev.
- Use middleware mode for backend integration.
- Align prod asset paths with backend hosting.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
```

### Example

```ts
import express from 'express'
import { createServer } from 'vite'

async function start() {
  const app = express()
  const vite = await createServer({ server: { middlewareMode: true } })
  app.use(vite.middlewares)
  app.listen(3000)
}

start()
```

### Notes

- Keep Vite middleware before backend routes if needed.

Reference: https://cn.vitejs.dev/guide/backend-integration.html
