---
name: appium
description: Provides comprehensive guidance for Appium mobile testing including mobile app automation, element location, gestures, and cross-platform testing. Use when the user asks about Appium, needs to test mobile applications, automate mobile apps, or write Appium test scripts.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写或维护 Appium 自动化测试（Android/iOS 原生或混合应用）
- 定位元素、手势、多端能力与 CI 集成

## How to use this skill

1. **环境**：安装 Appium Server、驱动（UiAutomator2/XCUITest）、JDK/Node；真机或模拟器。
2. **脚本**：Capabilities（deviceName、app、platformName）；定位器（id、xpath、accessibility id）；手势与等待。
3. **CI**：在 Jenkins/GitHub Actions 中运行；并行与报告。

## Best Practices

- 优先用 accessibility id 或 id；避免脆弱 xpath。
- 显式等待与重试；截图与日志便于排查。
- 多设备/多版本用矩阵；敏感信息用环境变量。

## Keywords

appium, 移动端自动化, Android, iOS, UI 测试
