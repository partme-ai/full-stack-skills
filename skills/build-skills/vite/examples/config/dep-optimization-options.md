## Instructions

- Fine-tune dependency pre-bundling.
- Include missing deps to avoid errors.
- Exclude large or incompatible deps.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  optimizeDeps: {
    include: ['dayjs', 'lodash-es'],
    exclude: ['@my/large-lib']
  }
})
```

### Example

```sh
rm -rf node_modules/.vite
```

### Notes

- Changes require dev server restart.

Reference: https://cn.vitejs.dev/config/dep-optimization-options.html
