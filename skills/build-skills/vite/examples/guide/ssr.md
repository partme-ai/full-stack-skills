## Instructions

- Separate client and server entries.
- Avoid browser-only globals in server entry.
- Use ssr.noExternal for ESM-only deps.

### Example

```md
src/
  entry-client.ts
  entry-server.ts
  main.ts
```

### Example

```ts
import { renderToString } from 'vue/server-renderer'
import { createApp } from './main'

export async function render(url: string) {
  const app = createApp()
  return await renderToString(app)
}
```

### Example

```ts
import { createApp } from './main'

createApp().mount('#app')
```

### Notes

- Use vite.ssrLoadModule in dev.

Reference: https://cn.vitejs.dev/guide/ssr.html
