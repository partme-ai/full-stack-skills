---
name: github-actions
description: Provides comprehensive guidance for GitHub Actions including workflow creation, actions, secrets, and automation. Use when the user asks about GitHub Actions, needs to create GitHub workflows, automate GitHub processes, or configure CI/CD with GitHub Actions.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写或调试 GitHub Actions 工作流（`.github/workflows/*.yml`）
- 配置 trigger、jobs、steps、secrets、矩阵与复用
- 集成 checkout、build、test、deploy、通知

## How to use this skill

1. **工作流**：YAML 中定义 `on`、`jobs`、`steps`；用 `actions/checkout`、官方/第三方 action；secrets 在 Settings 中配置。
2. **复用**：composite actions、reusable workflows；矩阵策略跑多版本/多平台。
3. **环境**：runner 环境（Ubuntu/Windows/macOS）；容器 job 时注意网络与挂载。

## Best Practices

- 用 `secrets` 存令牌与密钥；不在 log 中 echo 敏感信息。
- 关键步骤加 `id` 与 `outputs` 便于后续步骤使用。
- 缓存依赖（actions/cache）；必要时用 concurrency 取消旧运行。

## Keywords

github actions, workflow, yaml, CI/CD, 工作流, 自动化
