## Instructions

- Configure worker builds and format.
- Use worker plugins if needed.
- Apply when using web workers.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  worker: { format: 'es' }
})
```

### Example

```ts
// usage
const worker = new Worker(new URL('./worker.ts', import.meta.url))
```

### Notes

- Workers use separate build pipeline.

Reference: https://cn.vitejs.dev/config/worker-options.html
