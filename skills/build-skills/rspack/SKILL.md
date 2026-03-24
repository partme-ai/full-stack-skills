---
name: rspack
description: Provides comprehensive guidance for Rspack bundler including configuration, plugins, loaders, optimization, and Webpack compatibility. Use when the user asks about Rspack, needs to configure Rspack, optimize build performance, or migrate from Webpack.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Rspack in a new or existing project
- Configure Rspack for different environments
- Use built-in plugins or create custom plugins
- Migrate from Webpack to Rspack
- Optimize build performance
- Understand Rspack configuration options
- Use Rspack CLI or JavaScript API
- Write custom loaders
- Understand plugin API and hooks
- Configure entry points and output
- Set up code splitting and optimization
- Configure development server
- Handle assets and resources
- Use TypeScript with Rspack
- Troubleshoot Rspack issues

## How to use this skill

This skill is organized to match the Rspack official documentation structure (https://rspack.rs/zh/guide/start/introduction, https://rspack.rs/zh/config/, https://rspack.rs/zh/plugins/, https://rspack.rs/zh/api/). When working with Rspack:

1. **Identify the topic** from the user's request:
   - Getting started/快速上手 → `examples/guide/start/`
   - Configuration/配置 → `examples/config/`
   - Plugins/插件 → `examples/plugins/`
   - API → `examples/api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Guide (指南)** - `examples/guide/`:
   - `examples/guide/compatibility/plugin.md`
   - `examples/guide/features/asset-base-path.md`
   - `examples/guide/features/asset-module.md`
   - `examples/guide/features/builtin-lightningcss-loader.md`
   - `examples/guide/features/builtin-swc-loader.md`
   - `examples/guide/features/dev-server.md`
   - `examples/guide/features/esm.md`
   - `examples/guide/features/layer.md`
   - `examples/guide/features/lazy-compilation.md`
   - `examples/guide/features/loader.md`
   - `examples/guide/features/module-federation.md`
   - `examples/guide/features/module-resolution.md`
   - `examples/guide/features/plugin.md`
   - `examples/guide/features/web-workers.md`
   - `examples/guide/migration/cra.md`
   - `examples/guide/migration/rspack_0.x.md`
   - `examples/guide/migration/storybook.md`
   - `examples/guide/migration/webpack.md`
   - `examples/guide/optimization/analysis.md`
   - `examples/guide/optimization/code-splitting.md`
   - `examples/guide/optimization/lazy-barrel.md`
   - `examples/guide/optimization/production.md`
   - `examples/guide/optimization/profile.md`
   - `examples/guide/optimization/tree-shaking.md`
   - `examples/guide/optimization/use-rsdoctor.md`
   - `examples/guide/start/ecosystem.md`
   - `examples/guide/start/introduction.md`
   - `examples/guide/start/quick-start.md`
   - `examples/guide/tech/css.md`
   - `examples/guide/tech/json.md`
   - `examples/guide/tech/nestjs.md`
   - `examples/guide/tech/next.md`
   - `examples/guide/tech/preact.md`
   - `examples/guide/tech/react.md`
   - `examples/guide/tech/solid.md`
   - `examples/guide/tech/svelte.md`
   - `examples/guide/tech/typescript.md`
   - `examples/guide/tech/vue.md`

   **Configuration (配置)** - `examples/config/`:
   - `examples/config/cache.md`
   - `examples/config/context.md`
   - `examples/config/deprecated-options.md`
   - `examples/config/dev-server.md`
   - `examples/config/devtool.md`
   - `examples/config/entry.md`
   - `examples/config/experiments.md`
   - `examples/config/extends.md`
   - `examples/config/externals.md`
   - `examples/config/filename-placeholders.md`
   - `examples/config/index.md`
   - `examples/config/infrastructure-logging.md`
   - `examples/config/lazy-compilation.md`
   - `examples/config/mode.md`
   - `examples/config/module-rules.md`
   - `examples/config/module.md`
   - `examples/config/node.md`
   - `examples/config/optimization-optimizationsplitchunks.md`
   - `examples/config/optimization.md`
   - `examples/config/other-options.md`
   - `examples/config/output.md`
   - `examples/config/performance.md`
   - `examples/config/plugins.md`
   - `examples/config/resolve-loader.md`
   - `examples/config/resolve.md`
   - `examples/config/stats.md`
   - `examples/config/target.md`
   - `examples/config/watch.md`

   **Plugins (插件)** - `examples/plugins/`:
   - `examples/plugins/index.md`
   - `examples/plugins/rspack/circular-dependency-rspack-plugin.md`
   - `examples/plugins/rspack/copy-rspack-plugin.md`
   - `examples/plugins/rspack/css-chunking-plugin.md`
   - `examples/plugins/rspack/css-extract-rspack-plugin.md`
   - `examples/plugins/rspack/esm-library-plugin.md`
   - `examples/plugins/rspack/html-rspack-plugin.md`
   - `examples/plugins/rspack/lightning-css-minimizer-rspack-plugin.md`
   - `examples/plugins/rspack/subresource-integrity-plugin.md`
   - `examples/plugins/rspack/swc-js-minimizer-rspack-plugin.md`
   - `examples/plugins/rspack/virtual-modules-plugin.md`
   - `examples/plugins/webpack/banner-plugin.md`
   - `examples/plugins/webpack/case-sensitive-plugin.md`
   - `examples/plugins/webpack/context-replacement-plugin.md`
   - `examples/plugins/webpack/define-plugin.md`
   - `examples/plugins/webpack/dll-plugin.md`
   - `examples/plugins/webpack/dll-reference-plugin.md`
   - `examples/plugins/webpack/electron-target-plugin.md`
   - `examples/plugins/webpack/enable-chunk-loading-plugin.md`
   - `examples/plugins/webpack/enable-library-plugin.md`
   - `examples/plugins/webpack/enable-wasm-loading-plugin.md`
   - `examples/plugins/webpack/entry-plugin.md`
   - `examples/plugins/webpack/environment-plugin.md`
   - `examples/plugins/webpack/eval-source-map-dev-tool-plugin.md`
   - `examples/plugins/webpack/externals-plugin.md`
   - `examples/plugins/webpack/hot-module-replacement-plugin.md`
   - `examples/plugins/webpack/ignore-plugin.md`
   - `examples/plugins/webpack/index.md`
   - `examples/plugins/webpack/internal-plugins.md`
   - `examples/plugins/webpack/javascript-modules-plugin.md`
   - `examples/plugins/webpack/limit-chunk-count-plugin.md`
   - `examples/plugins/webpack/module-federation-plugin-v1.md`
   - `examples/plugins/webpack/module-federation-plugin.md`
   - `examples/plugins/webpack/no-emit-on-errors-plugin.md`
   - `examples/plugins/webpack/node-target-plugin.md`
   - `examples/plugins/webpack/node-template-plugin.md`
   - `examples/plugins/webpack/normal-module-replacement-plugin.md`
   - `examples/plugins/webpack/progress-plugin.md`
   - `examples/plugins/webpack/provide-plugin.md`
   - `examples/plugins/webpack/runtime-chunk-plugin.md`
   - `examples/plugins/webpack/source-map-dev-tool-plugin.md`
   - `examples/plugins/webpack/split-chunks-plugin.md`

   **API Reference** - `examples/api/`:
   - `examples/api/cli.md`
   - `examples/api/index.md`
   - `examples/api/javascript-api/browser.md`
   - `examples/api/javascript-api/cache.md`
   - `examples/api/javascript-api/compilation.md`
   - `examples/api/javascript-api/compiler.md`
   - `examples/api/javascript-api/index.md`
   - `examples/api/javascript-api/logger.md`
   - `examples/api/javascript-api/resolver.md`
   - `examples/api/javascript-api/stats-json.md`
   - `examples/api/javascript-api/stats.md`
   - `examples/api/javascript-api/swc.md`
   - `examples/api/loader-api/context.md`
   - `examples/api/loader-api/index.md`
   - `examples/api/loader-api/inline-match-resource.md`
   - `examples/api/loader-api/inline.md`
   - `examples/api/loader-api/writing-loaders.md`
   - `examples/api/plugin-api/compilation-hooks.md`
   - `examples/api/plugin-api/compiler-hooks.md`
   - `examples/api/plugin-api/context-module-factory-hooks.md`
   - `examples/api/plugin-api/index.md`
   - `examples/api/plugin-api/javascript-modules-plugin-hooks.md`
   - `examples/api/plugin-api/normal-module-factory-hooks.md`
   - `examples/api/plugin-api/runtime-plugin-hooks.md`
   - `examples/api/plugin-api/stats-hooks.md`
   - `examples/api/runtime-api/hmr.md`
   - `examples/api/runtime-api/module-methods.md`
   - `examples/api/runtime-api/module-variables.md`

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Rspack is compatible with most Webpack plugins and loaders
   - Configuration format is similar to Webpack
   - Rspack provides better performance than Webpack
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes parameters, returns, common errors, best practices, and scenarios

4. **Reference the official documentation** when needed:
   - Guide: https://rspack.rs/zh/guide/
   - Configuration: https://rspack.rs/zh/config/
   - Plugins: https://rspack.rs/zh/plugins/
   - API: https://rspack.rs/zh/api/

## Best Practices

1. **Use TypeScript for configuration**: Better type safety and autocomplete
2. **Leverage built-in plugins**: Use Rspack plugins when available
3. **Optimize for production**: Use production mode for builds
4. **Code splitting**: Use optimization.splitChunks for better performance
5. **Cache configuration**: Enable persistent caching for faster rebuilds
6. **Use HMR**: Enable Hot Module Replacement for better DX

## Resources

- **Official Documentation**: https://rspack.rs/zh/
- **Getting Started**: https://rspack.rs/zh/guide/start/introduction
- **Configuration**: https://rspack.rs/zh/config/
- **Plugins**: https://rspack.rs/zh/plugins/
- **API Reference**: https://rspack.rs/zh/api/
- **GitHub Repository**: https://github.com/web-infra-dev/rspack

## Keywords

Rspack, rspack, bundler, webpack, rust, build tool, bundling, code splitting, HMR, hot module replacement, loader, plugin, configuration, entry, output, optimization, development server, 打包工具, 构建工具, 代码分割, 热模块替换, 加载器, 插件, 配置, 入口, 输出, 优化, 开发服务器
