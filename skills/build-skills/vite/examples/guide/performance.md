## Instructions

- Minimize heavy plugin work.
- Tune optimizeDeps for faster dev.
- Use manual chunks for caching.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom']
        }
      }
    }
  }
})
```

### Example

```ts
import type { Plugin } from 'vite'

export function narrowTransformPlugin(): Plugin {
  return {
    name: 'narrow-transform',
    transform(code, id) {
      if (!id.endsWith('.md')) return
      return `export default ${JSON.stringify(code)}`
    }
  }
}
```

### Notes

- Avoid transforming node_modules unless required.

Reference: https://cn.vitejs.dev/guide/performance.html
