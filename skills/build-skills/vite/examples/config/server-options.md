## Instructions

- Configure dev server port/host/proxy.
- Set strictPort when needed.
- Tune HMR settings in containers.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: true,
    port: 5173,
    strictPort: true,
    proxy: { '/api': 'http://localhost:3000' }
  }
})
```

### Example

```ts
export default {
  server: {
    hmr: { host: 'localhost', port: 24678 }
  }
}
```

### Notes

- Use hmr.host when using Docker/VM.

Reference: https://cn.vitejs.dev/config/server-options.html
