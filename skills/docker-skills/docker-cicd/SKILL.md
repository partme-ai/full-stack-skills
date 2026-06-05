---
name: docker-cicd
description: Guidance for integrating Docker into CI/CD pipelines. Covers GitHub Actions (docker/build-push-action, multi-platform builds with buildx, cache-from/to), Jenkins Pipeline (Docker agent, build/push stages), Docker Build Cloud for accelerated builds, layer caching strategies in CI, image tagging strategies for CI/CD, deployment patterns (rolling update, blue-green). Use when the user asks about Docker CI/CD, GitHub Actions Docker, Jenkins Docker pipeline, buildx multi-platform, Docker Build Cloud, or needs to automate Docker builds. 使用场景：docker CI/CD、GitHub Actions docker、Jenkins docker、buildx、多平台构建、Docker Build Cloud、流水线.
license: Apache-2.0
---

# Docker CI/CD — 持续集成与持续部署

Guidance for integrating Docker into automated build, test, and deployment pipelines.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker CI", "docker CD", "CI/CD pipeline"
- "GitHub Actions docker", "Jenkins docker"
- "buildx", "multi-platform build", "多平台构建"
- "Docker Build Cloud"
- "镜像构建流水线"

## GitHub Actions

### Build & Push Pipeline

```yaml
name: Build and Push
on:
  push:
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          push: true
          tags: user/app:${{ github.ref_name }},user/app:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### Multi-Platform Build

```yaml
- name: Build and push multi-platform
  uses: docker/build-push-action@v6
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: user/app:latest
```

## Jenkins Pipeline

```groovy
pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'myapp'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Build') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }
        stage('Test') {
            steps {
                sh "docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} npm test"
            }
        }
        stage('Push') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub']) {
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }
}
```

## Layer Caching in CI

```bash
# Pull previous image for layer cache
docker pull $IMAGE:latest || true
docker build \
  --cache-from $IMAGE:latest \
  --build-arg BUILDKIT_INLINE_CACHE=1 \
  -t $IMAGE:$TAG .
```

## Workflow — 推荐 CI/CD 流程

Step 1: **配置 CI 环境**: docker/login-action + docker/setup-buildx-action
Step 2: **构建镜像**: docker/build-push-action + registry 缓存加速
Step 3: **安全扫描**: docker/scout-action 扫描 CVE + 策略门禁
Step 4: **推送仓库**: 多标签（semver + sha + latest）推送到 ghcr.io/Docker Hub
Step 5: **部署**: ArgoCD/Flux 监听仓库变更自动部署

## Gotchas — Common Pitfalls

- **CI cache miss**: Without `--cache-from`, every CI build starts from scratch. → **Recovery**: `docker pull myapp:latest || true` before build; use `--cache-from type=gha` in GitHub Actions.
- **Build secrets in CI logs**: Never `echo` or print secrets. Use buildx `--secret` or CI secrets masking. → **Recovery**: `docker buildx build --secret id=npmrc,src=$HOME/.npmrc`; check CI secrets are masked in logs.
- **Disk space in CI**: Multi-stage builds can consume CI disk. → **Recovery**: `docker system prune -af` between builds; monitor with `docker system df`.
- **Multi-platform emulation slow**: QEMU emulation for ARM on AMD is slow (~10x). → **Recovery**: Use native ARM runners (e.g., GitHub Actions ARM64 runners) or Docker Build Cloud for multi-platform.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | GitHub Actions Docker 集成 | docker/build-push-action + QEMU + multi-arch |
| ✅ 能做 | Jenkins Pipeline Docker | Docker agent + build/push/scan |
| ✅ 能做 | 多平台 CI 构建 | buildx + QEMU + 多架构 manifest |
| ⚠️ 需条件 | Docker Build Cloud 加速 | 需付费订阅 |
| ⚠️ 需条件 | 非 GitHub/Jenkins CI | 参考通用模式适配 |
| ❌ 超范围 | Dockerfile 编写 | 使用 `docker-dockerfile` |
| ❌ 超范围 | K8s CD（ArgoCD/Flux） | K8s 部署技能 |
| ❌ 超范围 | CI 平台搭建（Jenkins 安装） | DevOps 基础设施 |

## When NOT to Use

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Writing Dockerfile | `docker-build` |
| Security scanning | `docker-security` / `docker-scout` |
| Production deployment | `docker-production` |
| Registry management | `docker-hub` |

## Security & Stability

- Never hardcode registry credentials in CI configs. Use CI secrets manager (GitHub Secrets, Jenkins Credentials).
- Use OIDC (OpenID Connect) for cloud registry auth instead of long-lived credentials.
- Scan images with Docker Scout before pushing to production registry.
- Tag images with SHA digest for audit trails: `image:sha-${GITHUB_SHA::7}`.
- Rotate registry tokens regularly. Never use personal access tokens for CI.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Build CI | https://docs.docker.com/build/ci/ |
| Docker Build Cloud | https://docs.docker.com/build-cloud/ |
| GitHub Actions Docker | https://docs.docker.com/build/ci/github-actions/ |
| Docker Scout CI | https://docs.docker.com/scout/policy/ci/ |
| Buildx CI 集成 | https://docs.docker.com/build/ci/github-actions/build-push-action/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-cicd` — CI/CD 自动化**

**← Previous**: `docker-build` | **→ Next**: `docker-production`
