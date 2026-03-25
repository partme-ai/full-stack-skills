---
name: cloudformation
description: "Provides comprehensive guidance for AWS CloudFormation including templates, stacks, parameters, and infrastructure automation. Use when the user asks about CloudFormation, needs to create AWS infrastructure as code, manage stacks, or implement AWS IaC best practices."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write or debug CloudFormation templates (YAML/JSON)
- Create and manage AWS resources (EC2, S3, RDS, Lambda, etc.)
- Configure CloudFormation stacks, nested stacks, or stack sets
- Implement infrastructure automation with CloudFormation best practices
- Use cross-stack references with Export/ImportValue

## How to use this skill

### Workflow

1. **Define template** — write YAML with Parameters, Resources, and Outputs
2. **Create change set** — preview changes before applying
3. **Deploy stack** — create or update the stack
4. **Validate** — check stack events and outputs

### Quick Start Example

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple S3 bucket with versioning

Parameters:
  Environment:
    Type: String
    AllowedValues: [dev, staging, prod]
    Default: dev

Resources:
  AppBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub 'myapp-${Environment}-assets'
      VersioningConfiguration:
        Status: Enabled

Outputs:
  BucketArn:
    Value: !GetAtt AppBucket.Arn
    Export:
      Name: !Sub '${Environment}-AppBucketArn'
```

```bash
# Validate template
aws cloudformation validate-template --template-body file://template.yaml

# Create stack with change set preview
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name myapp-dev \
  --parameter-overrides Environment=dev
```

### Cross-Stack Reference Example

```yaml
# In consuming stack — import the exported bucket ARN
Resources:
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Environment:
        Variables:
          BUCKET_ARN: !ImportValue dev-AppBucketArn
```

## Best Practices

- Use YAML over JSON for readability and version control
- Store sensitive values with `Parameter` + `NoEcho` or AWS Secrets Manager — never hardcode
- Use Mappings and Conditions for environment-specific configuration
- Prefix stack names with environment (e.g., `dev-`, `prod-`) to avoid conflicts
- Encapsulate reusable resources as nested stacks for composability

## Troubleshooting

- **Rollback on create**: Check stack events in CloudFormation console for the specific resource failure
- **Circular dependency**: Refactor with `DependsOn` or split resources across stacks
- **Drift detection**: Run `aws cloudformation detect-stack-drift` to find out-of-band changes

## Keywords

cloudformation, aws, infrastructure as code, cloudformation template, aws iac, nested stacks, cross-stack references
