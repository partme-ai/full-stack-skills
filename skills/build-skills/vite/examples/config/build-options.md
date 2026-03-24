## Instructions

- Configure build output size and format.
- Use rollupOptions for chunking.
- Enable sourcemaps for debugging.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    sourcemap: true,
    target: 'es2018',
    rollupOptions: {
      output: {
        manualChunks: { vendor: ['react', 'react-dom'] }
      }
    }
  }
})
```

### Notes

- Use build.minify to control minifier.

Reference: https://cn.vitejs.dev/config/build-options.html
