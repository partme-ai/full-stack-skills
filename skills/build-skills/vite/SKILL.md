---
name: vite
description: Guidance for Vite using the official Guide, Config Reference, and Plugins pages. Use when the user needs Vite setup, configuration, or plugin selection details.
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

## Resources
- Guide: https://cn.vitejs.dev/guide/
- Config: https://cn.vitejs.dev/config/
- Plugins: https://cn.vitejs.dev/plugins/

## Keywords
Vite, build tool, dev server, HMR, config, plugins, SSR, CLI, dependency pre-bundling, assets
