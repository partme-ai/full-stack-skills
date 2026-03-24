---
name: cloudformation
description: Provides comprehensive guidance for AWS CloudFormation including templates, stacks, parameters, and infrastructure automation. Use when the user asks about CloudFormation, needs to create AWS infrastructure as code, manage CloudFormation stacks, or implement AWS IaC best practices.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写或调试 CloudFormation 模板（YAML/JSON）
- 创建和管理 AWS 资源（EC2、S3、RDS、Lambda 等）
- 配置 CloudFormation stacks、nested stacks、stack sets
- 使用 CloudFormation 最佳实践实现基础设施自动化

## How to use this skill

1. **模板结构**：AWSTemplateFormatVersion、Description、Parameters、Resources、Outputs。
2. **工作流**：创建堆栈 → 更新堆栈 → 删除堆栈；使用变更集预览变更。
3. **嵌套堆栈**：将重复使用的资源封装为 nested stack，提高复用性。
4. **Cross-stack references**：通过 Export/Import-Value 在堆栈间共享资源。

## Best Practices

- 使用 YAML 格式替代 JSON，便于版本控制和 Code Review。
- 敏感信息用 Parameter + NoEcho 或 Secrets Manager，不在模板中硬编码。
- 使用 Mappings 和 Conditions 实现环境差异化配置。
- 堆栈名称加环境前缀（dev-、prod-），避免冲突。

## Keywords

cloudformation, aws, infrastructure as code, cloudformation template, 亚马逊云科技, aws iac, 基础设施自动化