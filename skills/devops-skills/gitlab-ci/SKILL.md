---
name: gitlab-ci
description: Provides comprehensive guidance for GitLab CI/CD including pipeline configuration, runners, artifacts, and automation. Use when the user asks about GitLab CI, needs to create GitLab pipelines, configure CI/CD workflows, or automate deployments with GitLab.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写或调试 GitLab CI 流水线 (`.gitlab-ci.yml`)
- 配置 GitLab Runner、stages、jobs、artifacts
- 设置 GitLab CI/CD 变量、secrets、environments
- 集成测试、构建、部署自动化

## How to use this skill

1. **流水线结构**：YAML 中定义 `stages`、`jobs`；每个 job 属于某个 stage。
2. **Runner 配置**：shared runner、specific runner、tags 选择。
3. **Artifacts 与缓存**：在 jobs 间传递构建产物，使用 cache 加速。
4. **环境与部署**：使用 `environment` 定义部署目标，配置 `only/except` 规则。

## Best Practices

- 用 `stages` 明确构建顺序，job 并行执行。
- 敏感信息用 CI/CD 变量（Settings → CI/CD → Variables），不在 yaml 中硬编码。
- 用 `needs` 实现复杂依赖图，避免不必要的等待。
- 失败 job 加 `artifacts` 保留日志和产物。

## Keywords

gitlab ci, gitlab-ci, pipeline, runner, ci/cd, 流水线, 自动化部署, gitlab runner