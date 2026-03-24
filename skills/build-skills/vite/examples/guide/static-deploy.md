## Instructions

- Set base for subpath deployments.
- Follow platform-specific hosting steps.
- Verify asset paths after deploy.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  base: '/my-app/'
})
```

### Example

```sh
vite build
# deploy dist/ to static host
```

### Notes

- Use preview to validate base path.

Reference: https://cn.vitejs.dev/guide/static-deploy.html
