## Instructions

- Install plugins and register in vite.config.
- Order plugins to avoid conflicts.
- Prefer official plugins where possible.

### Example

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()]
})
```

### Example

```ts
import legacy from '@vitejs/plugin-legacy'

export default {
  plugins: [legacy({ targets: ['defaults', 'not IE 11'] })]
}
```

### Notes

- Keep plugin order deterministic.

Reference: https://cn.vitejs.dev/guide/using-plugins.html
