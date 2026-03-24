---
name: detox
description: Provides comprehensive guidance for Detox mobile testing framework including React Native testing, E2E testing, and test synchronization. Use when the user asks about Detox, needs to test React Native applications, write E2E tests for mobile apps, or configure Detox.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 为 React Native 应用编写或调试 Detox E2E 测试
- 配置构建、启动模拟器与断言；CI 集成

## How to use this skill

1. **环境**：安装 Detox、配置 .detoxrc；iOS 需 Xcode 与模拟器；Android 需 SDK 与模拟器。
2. **用例**：element(by.id)、tap、typeText、expect；异步等待与同步。
3. **CI**：build 与 test 步骤；Artifacts 保存日志与截图。

## Best Practices

- 用 testID 稳定定位；避免依赖文本与耗时动画。
- 构建与设备配置一致；失败时保留 artifacts。
- 敏感操作用环境变量；并行与重试策略。

## Keywords

detox, React Native, E2E, 端到端测试
