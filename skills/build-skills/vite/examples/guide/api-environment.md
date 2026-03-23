## Instructions

- Define per-environment behavior.
- Isolate plugins and config per environment.
- Use for client/server/custom targets.

### Example

```md
- client: browser
- server: SSR
- worker: web worker
```

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  environments: {
    client: {},
    server: {}
  }
})
```

### Notes

- Do not apply browser-only plugins to server.

Reference: https://cn.vitejs.dev/guide/api-environment.html
