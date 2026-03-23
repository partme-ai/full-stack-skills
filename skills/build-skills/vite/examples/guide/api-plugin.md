## Instructions

- Use plugin hooks to resolve, load, and transform modules.
- Use enforce to control plugin order.
- Avoid heavy work in transform.

### Example

```ts
import type { Plugin } from 'vite'

export function virtualModulePlugin(): Plugin {
  const virtualId = 'virtual:env'
  const resolvedVirtualId = '\0' + virtualId

  return {
    name: 'virtual-module-plugin',
    resolveId(id) {
      if (id === virtualId) return resolvedVirtualId
    },
    load(id) {
      if (id === resolvedVirtualId) {
        return 'export const env = { mode: import.meta.env.MODE }'
      }
    }
  }
}
```

### Example

```ts
export function transformPlugin(): Plugin {
  return {
    name: 'transform-plugin',
    transform(code, id) {
      if (id.endsWith('.txt')) {
        return `export default ${JSON.stringify(code)}`
      }
    }
  }
}
```

### Notes

- Use this.addWatchFile for extra file deps.

Reference: https://cn.vitejs.dev/guide/api-plugin.html
