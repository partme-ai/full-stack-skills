---
name: terraform
description: Provides comprehensive guidance for Terraform including infrastructure as code, providers, modules, and state management. Use when the user asks about Terraform, needs to create infrastructure as code, manage cloud resources with Terraform, or implement IaC best practices.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写或调试 Terraform 配置文件（`.tf`）
- 管理云基础设施（AWS、Azure、GCP、阿里云等）
- 配置 Terraform providers、resources、data sources
- 管理 Terraform state、modules、workspaces

## How to use this skill

1. **配置文件**：HCL 语法定义 provider、resource、variable、output、module。
2. **工作流**：`terraform init` → `terraform plan` → `terraform apply` → `terraform destroy`。
3. **State 管理**：本地或远程（ S3 + DynamoDB、Azure Blob、阿里云 OSS 等）。
4. **Modules**：复用基础设施模板，版本化管理。

## Best Practices

- 使用 remote state 替代本地 state，避免状态文件冲突。
-敏感信息用 variable 或 environment variable，不在 .tf 文件中硬编码。
- 使用 `terraform fmt` 格式化代码，`terraform validate` 检查语法。
- 生产环境使用 workspace 或 environment 隔离。

## Keywords

terraform, iac, infrastructure as code, hcl, aws, azure, gcp, aliyun, 基础设施即代码, 云资源管理