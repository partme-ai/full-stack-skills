---
name: selenium
description: Provides comprehensive guidance for Selenium WebDriver including browser automation, element location, waits, and test frameworks. Use when the user asks about Selenium, needs to automate web browsers, write Selenium tests, or work with Selenium WebDriver.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Selenium WebDriver 编写或维护浏览器自动化测试
- 定位元素、等待、多浏览器与 CI 集成（如 Grid）

## How to use this skill

1. **环境**：安装浏览器驱动（ChromeDriver/GeckoDriver）或 Selenium 4 管理；对应语言绑定（Python/Java/JS 等）。
2. **脚本**：driver.get、find_element、click、send_keys；显式/隐式等待；截图与 cookie。
3. **CI**：无头模式或 Grid；并行与报告（如 Allure）。

## Best Practices

- 显式等待替代 sleep；优先 id、css、相对定位。
- 用例独立、可重复；失败时截图与日志。
- 敏感信息与 URL 用配置；Grid 与版本匹配。

## Keywords

selenium, WebDriver, 浏览器自动化, E2E
