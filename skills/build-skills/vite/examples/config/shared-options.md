## Instructions

- Configure root, base, resolve, and define.
- Use alias for import paths.
- Use define for compile-time constants.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  resolve: { alias: { '@': '/src' } },
  define: { __APP_VERSION__: JSON.stringify('1.0.0') }
})
```

### Notes

- Prefer absolute aliases for clarity.

Reference: https://cn.vitejs.dev/config/shared-options.html
