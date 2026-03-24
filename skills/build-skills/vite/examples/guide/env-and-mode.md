## Instructions

- Use .env files for environment config.
- Expose only VITE_ prefixed vars.
- Switch modes with --mode.

### Example

```env
# .env
VITE_API_BASE=https://api.example.com

# .env.staging
VITE_API_BASE=https://staging.example.com
```

### Example

```ts
console.log(import.meta.env.MODE)
console.log(import.meta.env.VITE_API_BASE)
```

### Example

```sh
vite --mode staging
vite build --mode production
```

### Notes

- Restart dev server after env changes.

Reference: https://cn.vitejs.dev/guide/env-and-mode.html
