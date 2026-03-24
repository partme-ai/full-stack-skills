## Instructions

- Run vite build for production output.
- Use preview to validate build.
- Adjust build options as needed.

### Example

```sh
vite build
vite preview
```

### Example

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    target: 'es2018',
    sourcemap: true,
    outDir: 'dist'
  }
})
```

### Notes

- Use build.target to control compatibility.

Reference: https://cn.vitejs.dev/guide/build.html
