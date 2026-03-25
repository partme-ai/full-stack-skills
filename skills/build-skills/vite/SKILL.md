---
name: vite
description: "Guidance for Vite using the official Guide, Config Reference, and Plugins pages. Use when the user needs Vite setup, configuration, or plugin selection details."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Follow Vite Guide topics from getting started to performance
- Configure Vite using the official config reference
- Select or understand Vite plugins from the official plugins page
- Use Vite CLI, HMR API, or JavaScript API
- Handle SSR, backend integration, or deployment scenarios in Vite

## How to use this skill

1. **Identify the topic** from the user request.
2. **Open the matching guide example** file in `examples/guide/`.
3. **If configuration is needed**, open the matching file in `examples/config/`.
4. **If plugin selection is needed**, open `examples/plugins.md`.
5. **Follow official docs verbatim** and keep output consistent with the referenced page.
6. **Validate**: Run `npm run build` to verify config changes compile; `npm run preview` to test production output.

### Guide mapping (one-to-one with https://cn.vitejs.dev/guide/)

**Introduction**
- `examples/guide/getting-started.md` → https://cn.vitejs.dev/guide/
- `examples/guide/philosophy.md` → https://cn.vitejs.dev/guide/philosophy.html
- `examples/guide/why-vite.md` → https://cn.vitejs.dev/guide/why.html

**Guide**
- `examples/guide/features.md` → https://cn.vitejs.dev/guide/features.html
- `examples/guide/cli.md` → https://cn.vitejs.dev/guide/cli.html
- `examples/guide/using-plugins.md` → https://cn.vitejs.dev/guide/using-plugins.html
- `examples/guide/dep-pre-bundling.md` → https://cn.vitejs.dev/guide/dep-pre-bundling.html
- `examples/guide/assets.md` → https://cn.vitejs.dev/guide/assets.html
- `examples/guide/build.md` → https://cn.vitejs.dev/guide/build.html
- `examples/guide/static-deploy.md` → https://cn.vitejs.dev/guide/static-deploy.html
- `examples/guide/env-and-mode.md` → https://cn.vitejs.dev/guide/env-and-mode.html
- `examples/guide/ssr.md` → https://cn.vitejs.dev/guide/ssr.html
- `examples/guide/backend-integration.md` → https://cn.vitejs.dev/guide/backend-integration.html
- `examples/guide/troubleshooting.md` → https://cn.vitejs.dev/guide/troubleshooting.html
- `examples/guide/performance.md` → https://cn.vitejs.dev/guide/performance.html
- `examples/guide/migration.md` → https://cn.vitejs.dev/guide/migration.html

**APIs**
- `examples/guide/api-plugin.md` → https://cn.vitejs.dev/guide/api-plugin.html
- `examples/guide/api-hmr.md` → https://cn.vitejs.dev/guide/api-hmr.html
- `examples/guide/api-javascript.md` → https://cn.vitejs.dev/guide/api-javascript.html

**Environment API**
- `examples/guide/api-environment.md` → https://cn.vitejs.dev/guide/api-environment.html
- `examples/guide/api-environment-instances.md` → https://cn.vitejs.dev/guide/api-environment-instances.html
- `examples/guide/api-environment-plugins.md` → https://cn.vitejs.dev/guide/api-environment-plugins.html
- `examples/guide/api-environment-frameworks.md` → https://cn.vitejs.dev/guide/api-environment-frameworks.html
- `examples/guide/api-environment-runtimes.md` → https://cn.vitejs.dev/guide/api-environment-runtimes.html

### Config mapping (one-to-one with https://cn.vitejs.dev/config/)

- `examples/config/configuring-vite.md` → https://cn.vitejs.dev/config/
- `examples/config/shared-options.md` → https://cn.vitejs.dev/config/shared-options.html
- `examples/config/server-options.md` → https://cn.vitejs.dev/config/server-options.html
- `examples/config/build-options.md` → https://cn.vitejs.dev/config/build-options.html
- `examples/config/preview-options.md` → https://cn.vitejs.dev/config/preview-options.html
- `examples/config/dep-optimization-options.md` → https://cn.vitejs.dev/config/dep-optimization-options.html
- `examples/config/ssr-options.md` → https://cn.vitejs.dev/config/ssr-options.html
- `examples/config/worker-options.md` → https://cn.vitejs.dev/config/worker-options.html

### Plugins mapping (one-to-one with https://cn.vitejs.dev/plugins/)

- `examples/plugins.md` → https://cn.vitejs.dev/plugins/

### Inline Quick Start

```bash
# Create a new Vite project
npm create vite@latest my-app -- --template react-ts

# Install and run
cd my-app && npm install
npm run dev      # Dev server with HMR
npm run build    # Production build
npm run preview  # Preview production build
```

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': 'http://localhost:8080',
    },
  },
  build: {
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: { vendor: ['react', 'react-dom'] },
      },
    },
  },
});
```

## Best Practices

- Use `defineConfig` for TypeScript type hints and autocomplete
- Configure proxy in `server.proxy` for API calls during development
- Use `build.rollupOptions.output.manualChunks` for vendor splitting
- Enable source maps in development; disable in production for smaller builds
- Use `import.meta.env` for environment variables (prefix with `VITE_`)

## Resources
- Guide: https://cn.vitejs.dev/guide/
- Config: https://cn.vitejs.dev/config/
- Plugins: https://cn.vitejs.dev/plugins/

## Keywords
Vite, build tool, dev server, HMR, config, plugins, SSR, CLI, dependency pre-bundling, assets
