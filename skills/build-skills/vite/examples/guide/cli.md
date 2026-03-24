## Instructions

- Use CLI for dev/build/preview.
- Prefer flags for quick experiments.
- Use --mode to load env files.

### Example

```sh
vite --host 0.0.0.0 --port 5173
vite build --mode staging
vite preview --port 4173
```

### Example

```sh
vite --config ./configs/vite.custom.ts
```

### Notes

- Use --strictPort to fail when port is busy.

Reference: https://cn.vitejs.dev/guide/cli.html
