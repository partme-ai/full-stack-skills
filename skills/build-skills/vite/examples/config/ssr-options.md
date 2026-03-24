## Instructions

- Configure SSR externalization and bundling.
- Use noExternal for ESM-only deps.
- Test SSR output after changes.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  ssr: {
    noExternal: ['some-esm-only-package'],
    external: ['some-cjs-only-package']
  }
})
```

### Example

```sh
vite build --ssr
```

### Notes

- Use ssr.target for non-node runtimes.

Reference: https://cn.vitejs.dev/config/ssr-options.html
