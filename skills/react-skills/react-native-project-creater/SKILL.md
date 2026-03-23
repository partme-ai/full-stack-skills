---
name: react-native-project-creater
description: Provides one-command project creation for React Native including project initialization, configuration, and template generation. Use when the user asks about creating React Native projects, needs to initialize a new React Native project, or generate React Native project structure.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 React Native CLI 或模板创建新 RN 项目、选择模板与配置
- 初始化依赖、Metro 与原生工程

## How to use this skill

1. **创建**：npx @react-native-community/cli init ProjectName；选 TypeScript、模板。
2. **结构**：App.tsx、android/、ios/、metro；依赖与 Pod install。
3. **参考**：https://reactnative.dev/docs/environment-setup

## Best Practices

- 命名与包名规范；先跑通默认模板再改。
- 锁定 Node 与 RN 版本；CI 环境一致。

## Keywords

react native init, 项目创建, 跨平台
