## Instructions

- Use optimizeDeps to control pre-bundling.
- Include missing deps; exclude incompatible ones.
- Clear cache after changing optimizeDeps.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  optimizeDeps: {
    include: ['lodash-es', 'dayjs'],
    exclude: ['@my/large-lib']
  }
})
```

### Example

```sh
rm -rf node_modules/.vite
```

### Notes

- Pre-bundling runs only in dev.

Reference: https://cn.vitejs.dev/guide/dep-pre-bundling.html
