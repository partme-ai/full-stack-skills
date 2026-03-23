## Instructions

- Use instances to manage per-runtime config.
- Separate lifecycle for each target.
- Avoid config leakage.

### Example

```md
- Create instance
- Apply env plugins
- Serve/build
- Dispose
```

### Notes

- Use instances for multi-target tooling.

Reference: https://cn.vitejs.dev/guide/api-environment-instances.html
