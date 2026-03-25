---
name: github-actions
description: "Provides comprehensive guidance for GitHub Actions including workflow creation, CI/CD pipelines, secrets management, matrix strategies, and reusable workflows. Use when the user asks about GitHub Actions, needs to create workflows, automate processes, or configure CI/CD."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create or debug GitHub Actions workflows (`.github/workflows/*.yml`)
- Configure triggers, jobs, steps, secrets, matrix strategies, or reusable workflows
- Integrate checkout, build, test, deploy, and notification steps
- Optimize workflow performance with caching and concurrency controls

## How to use this skill

### Workflow

1. **Create workflow file** — add YAML to `.github/workflows/`
2. **Define triggers** — specify `on` events (push, pull_request, schedule, etc.)
3. **Configure jobs and steps** — use official and third-party actions
4. **Test and iterate** — push to trigger, check logs, fix failures

### Quick Start Example

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - run: npm ci
      - run: npm test

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - name: Deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
        run: ./scripts/deploy.sh
```

### Reusable Workflow Example

```yaml
# .github/workflows/reusable-build.yml
on:
  workflow_call:
    inputs:
      node-version:
        type: string
        default: '20'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
      - run: npm ci && npm run build
```

## Best Practices

- Store tokens and keys in `secrets` — never echo sensitive values in logs
- Add `id` and `outputs` to key steps for downstream consumption
- Cache dependencies with `actions/cache` or built-in setup action caching
- Use `concurrency` to cancel outdated workflow runs on the same branch
- Pin action versions to a SHA or major version tag for security

## Troubleshooting

- **Workflow not triggered**: Verify the `on` event matches your branch and event type
- **Permission denied**: Check `permissions` block and repository settings for GITHUB_TOKEN scope
- **Cache miss**: Ensure the cache key includes lockfile hash (e.g., `hashFiles('**/package-lock.json')`)
- **Matrix failures**: Use `continue-on-error` selectively; check logs per matrix combination

## Keywords

github actions, workflow, yaml, CI/CD, automation, matrix strategy, reusable workflows, secrets
