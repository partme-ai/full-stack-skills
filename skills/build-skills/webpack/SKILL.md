---
name: webpack
description: Provides comprehensive guidance for Webpack bundler including configuration, loaders, plugins, code splitting, optimization, and development setup. Use when the user asks about Webpack, needs to configure Webpack, set up build pipelines, optimize bundles, or work with Webpack plugins.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Webpack 打包 JS/CSS/资源、配置 loader、plugin 与优化
- 处理多入口、代码分割、缓存与 dev server

## How to use this skill

1. **配置**：entry、output、module.rules（babel、css、file）；plugins（HtmlWebpackPlugin、MiniCssExtract）。
2. **进阶**：splitChunks、懒加载、devtool、HMR；环境变量与 mode。
3. **参考**：https://webpack.js.org/

## Best Practices

- loader 顺序与 exclude；生产压缩与 tree-shaking。
- 大项目考虑 Vite 或 Rspack；缓存与构建速度。

## Keywords

webpack, 打包, loader, plugin, 代码分割
