---
name: nvm-docker-ci
description: Cover nvm installation and usage in Docker images and CI/CD pipelines, including non-interactive shell loading.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Installing nvm in Docker
- Using nvm in CI/CD pipelines
- Non-interactive shell configuration

**Trigger phrases include:**
- "Dockerfile", "容器", "CI/CD"
- "BASH_ENV", "ENTRYPOINT", "non-interactive"

## How to use this skill

**CRITICAL: This skill targets container and CI usage only.** Base install steps remain in nvm-install.

1. Choose Dockerfile or CI job installation approach.
2. Ensure non-interactive shells load nvm via BASH_ENV or ENTRYPOINT.
3. Validate nvm availability in container or pipeline.

### Example file map

- examples/install-docker.md
- examples/install-docker-cicd.md
- examples/docker-dev.md

## Keywords

docker, ci, bash_env, entrypoint, non-interactive shell, nvm in container, 容器
