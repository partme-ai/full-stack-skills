## Instructions

- Use defineConfig for type safety.
- Keep config minimal and explicit.
- Use mode-based config when needed.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig(({ mode }) => ({
  base: mode === 'production' ? '/prod/' : '/',
  server: { port: 5173 }
}))
```

### Example

```ts
export default {
  root: 'src',
  publicDir: '../public'
}
```

### Notes

- Use functional config when reading mode.

Reference: https://cn.vitejs.dev/config/
