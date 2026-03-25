---
name: terraform
description: "Provides comprehensive guidance for Terraform including infrastructure as code, providers, modules, state management, and multi-cloud resource provisioning. Use when the user asks about Terraform, needs to create IaC configurations, manage cloud resources, or implement Terraform best practices."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write or debug Terraform configuration files (`.tf`)
- Manage cloud infrastructure (AWS, Azure, GCP, etc.)
- Configure providers, resources, data sources, and outputs
- Manage Terraform state, modules, and workspaces

## How to use this skill

### Workflow

1. **Write configuration** — define providers, resources, variables, and outputs in HCL
2. **Initialize** — run `terraform init` to download providers and modules
3. **Plan** — run `terraform plan` to preview changes
4. **Apply** — run `terraform apply` to provision infrastructure
5. **Validate** — confirm resources with `terraform state list` and cloud console

### Quick Start Example

```hcl
# main.tf
terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "myapp-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

resource "aws_s3_bucket" "app_assets" {
  bucket = "myapp-${var.environment}-assets"
  tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

output "bucket_arn" {
  value = aws_s3_bucket.app_assets.arn
}
```

```bash
# Standard workflow
terraform init
terraform fmt          # Format code
terraform validate     # Check syntax
terraform plan         # Preview changes
terraform apply        # Apply changes

# State inspection
terraform state list
terraform state show aws_s3_bucket.app_assets
```

### Module Usage Example

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "myapp-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
}
```

## Best Practices

- Use remote state (S3 + DynamoDB, Azure Blob, etc.) to avoid state file conflicts
- Store sensitive values in variables or environment variables — never hardcode in `.tf` files
- Run `terraform fmt` and `terraform validate` before every commit
- Use workspaces or directory-based environments for isolation (dev/staging/prod)
- Version-pin providers and modules to avoid unexpected breaking changes

## Troubleshooting

- **State lock error**: Check for stale locks in DynamoDB/backend; use `terraform force-unlock` as last resort
- **Provider version conflict**: Pin versions in `required_providers` and run `terraform init -upgrade`
- **Drift detected**: Run `terraform plan` to see differences; import or taint resources as needed
- **Destroy hanging**: Check for resource dependencies; use `-target` for selective destruction

## Keywords

terraform, iac, infrastructure as code, hcl, aws, azure, gcp, modules, state management, cloud provisioning
