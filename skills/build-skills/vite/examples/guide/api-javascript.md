## Instructions

- Use createServer for programmatic dev server.
- Use build for programmatic builds.
- Use ssrLoadModule for SSR in dev.

### Example

```ts
import { createServer } from 'vite'

async function start() {
  const server = await createServer({ server: { port: 5173 } })
  await server.listen()
  server.printUrls()
}

start()
```

### Example

```ts
import { build } from 'vite'

await build({ build: { outDir: 'dist' } })
```

### Example

```ts
import { createServer } from 'vite'

const server = await createServer({ server: { middlewareMode: true } })
const { render } = await server.ssrLoadModule('/src/entry-server.ts')
```

### Notes

- Use middlewareMode when embedding in backend.

Reference: https://cn.vitejs.dev/guide/api-javascript.html
