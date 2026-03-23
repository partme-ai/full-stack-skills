## Instructions

- Use preview to verify production builds.
- Set port and host as needed.
- Keep preview aligned with deployment.

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  preview: { port: 4173, host: true }
})
```

### Example

```sh
vite preview --port 4173
```

### Notes

- Preview serves the built output from dist/.

Reference: https://cn.vitejs.dev/config/preview-options.html
