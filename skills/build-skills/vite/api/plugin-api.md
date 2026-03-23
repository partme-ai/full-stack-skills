# Plugin API

## API Reference

Vite plugin development API and hooks.

### Plugin Structure

```typescript
interface Plugin {
  name: string
  enforce?: 'pre' | 'post'
  buildStart?: (this: PluginContext) => void | Promise<void>
  resolveId?: (id: string, importer?: string) => Promise<string | null> | string | null
  load?: (id: string) => Promise<string | null> | string | null
  transform?: (code: string, id: string) => Promise<TransformResult> | TransformResult
  buildEnd?: (err?: Error) => void | Promise<void>
  // ... more hooks
}
```

### Plugin Hooks

#### resolveId

Resolve module IDs.

```typescript
resolveId(id: string, importer?: string): string | null | { id: string }
```

#### load

Load module content.

```typescript
load(id: string): string | null | { code: string, map?: SourceMap }
```

#### transform

Transform module code.

```typescript
transform(code: string, id: string): { code: string, map?: SourceMap } | null
```

#### buildStart

Called at the start of the build.

```typescript
buildStart(): void | Promise<void>
```

#### buildEnd

Called at the end of the build.

```typescript
buildEnd(err?: Error): void | Promise<void>
```

### Example: Custom Plugin

```javascript
export default function myPlugin() {
  return {
    name: 'my-plugin',
    enforce: 'pre',
    resolveId(id) {
      if (id === 'virtual-module') {
        return id
      }
    },
    load(id) {
      if (id === 'virtual-module') {
        return 'export default "Virtual content"'
      }
    }
  }
}
```

**See also:** `examples/plugins.md`
