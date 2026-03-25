---
name: gitlab-ci
description: "Provides comprehensive guidance for GitLab CI/CD including pipeline configuration, runners, artifacts, environments, and deployment automation. Use when the user asks about GitLab CI, needs to create pipelines, configure runners, or automate builds and deployments."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write or debug GitLab CI pipelines (`.gitlab-ci.yml`)
- Configure GitLab Runner, stages, jobs, and artifacts
- Set up CI/CD variables, secrets, and environments
- Integrate testing, building, and deployment automation
- Use `needs` for complex dependency graphs between jobs

## How to use this skill

### Workflow

1. **Define stages** — declare the pipeline execution order
2. **Write jobs** — assign each job to a stage with scripts and rules
3. **Configure artifacts and cache** — pass build outputs between jobs
4. **Set up environments** — define deployment targets with rules

### Quick Start Example

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  NODE_VERSION: "20"

test:
  stage: test
  image: node:${NODE_VERSION}
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  script:
    - npm ci
    - npm test
  artifacts:
    when: on_failure
    paths:
      - test-reports/
    expire_in: 7 days

build:
  stage: build
  image: node:${NODE_VERSION}
  needs: [test]
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

deploy_production:
  stage: deploy
  needs: [build]
  environment:
    name: production
    url: https://myapp.example.com
  script:
    - ./scripts/deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

### Key Concepts

| Feature | Purpose |
|---------|---------|
| `stages` | Define execution order |
| `needs` | Create DAG dependencies (skip stage waiting) |
| `artifacts` | Pass files between jobs |
| `cache` | Speed up repeated installs |
| `rules` | Control when jobs run |
| `environment` | Track deployment targets |

## Best Practices

- Use `stages` to define clear build order; jobs within a stage run in parallel
- Store sensitive values in CI/CD Variables (Settings > CI/CD > Variables) — never hardcode in YAML
- Use `needs` to create complex dependency graphs and avoid unnecessary waiting
- Preserve logs and artifacts on failure with `artifacts: when: on_failure`
- Use `rules` instead of deprecated `only/except` for conditional job execution

## Troubleshooting

- **Job stuck pending**: Check runner tags match and runners are available
- **Artifact not found**: Verify the producing job completed and artifact paths are correct
- **Cache not restoring**: Ensure cache key is consistent; check runner cache configuration
- **Pipeline not triggered**: Verify `rules` conditions match the event (push, merge request, etc.)

## Keywords

gitlab ci, gitlab-ci, pipeline, runner, ci/cd, artifacts, cache, environments, deployment automation
