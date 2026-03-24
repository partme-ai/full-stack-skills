---
name: playwright
description: Provides comprehensive guidance for Playwright testing including browser automation, test writing, page objects, and cross-browser testing. Use when the user asks about Playwright, needs to write E2E tests, automate browsers, or test web applications across browsers.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Playwright 编写或调试浏览器 E2E 测试（多浏览器、多标签、自动等待）
- 配置项目、定位器、Fixture 与 CI 运行

## How to use this skill

1. **安装**：npm init playwright；选浏览器与语言；生成示例与配置。
2. **编写**：page.goto、getByRole、click、fill、expect；自动等待与断言；多页与 API 请求。
3. **运行**：npx playwright test；headed/UI 模式；报告与 trace。

## Best Practices

- 优先用 getByRole/getByLabel；避免脆弱 xpath。
- 用例独立、可重复；用 fixture 或 beforeEach 准备状态。
- CI 中安装依赖与浏览器；失败时保留 trace 与截图。

## Keywords

playwright, E2E, 端到端测试, 多浏览器
