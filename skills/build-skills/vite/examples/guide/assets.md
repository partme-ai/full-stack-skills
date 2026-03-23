## Instructions

- Import assets for hashed URLs.
- Use public/ for static un-hashed assets.
- Use query suffixes to control behavior.

### Example

```ts
import logoUrl from './logo.svg'
import textRaw from './readme.md?raw'
import dataUrl from './icon.png?inline'
```

### Example

```md
public/
  favicon.svg

<img src="/favicon.svg" />
```

### Notes

- Prefer module imports for cache-busted assets.

Reference: https://cn.vitejs.dev/guide/assets.html
