## Instructions

- Apply plugins to specific environments.
- Avoid side effects across envs.
- Keep order per environment.

### Example

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  environments: {
    client: { plugins: [vue()] },
    server: { plugins: [] }
  }
})
```

### Notes

- Use separate plugin lists for clarity.

Reference: https://cn.vitejs.dev/guide/api-environment-plugins.html
