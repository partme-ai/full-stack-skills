---
name: rollup
description: Provides comprehensive guidance for Rollup bundler including configuration, plugins, code splitting, tree shaking, and library bundling. Use when the user asks about Rollup, needs to bundle libraries, optimize output, or configure Rollup for production builds.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Rollup 打包库或应用、Tree-shaking、多格式输出（ESM/CJS）
- 配置 input、output、plugin 与外部依赖

## How to use this skill

1. **配置**：rollup.config.js；input、output.format、output.file/dir；plugins（node-resolve、commonjs、terser）。
2. **模式**：库打包多格式；应用可与 Vite 或配合其他工具。
3. **参考**：https://rollupjs.org/

## Best Practices

- 库声明 external；保留 sourcemap 便于调试。
- 大依赖外部化；按需用 code-splitting。

## Keywords

rollup, 打包, ESM, tree-shaking
