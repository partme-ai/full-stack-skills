---
name: docker-hub
description: Guidance for Docker image registries — publishing images to Docker Hub, pulling images, tag management strategies, private registry setup (Docker Registry container and Harbor), registry mirrors for acceleration, image signing and content trust, and registry API usage. Use when the user asks about docker hub, image registry, docker push/pull, private registry, docker login, tag management, Harbor, or needs to manage container images in registries. 使用场景：docker hub、镜像仓库、docker push、docker pull、私有仓库、registry、Harbor、镜像标签管理.
license: Apache-2.0
---

# Docker Hub — 镜像仓库管理

Guidance for publishing, pulling, and managing Docker images.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker hub", "docker registry", "镜像仓库"
- "docker push", "docker pull", "docker tag"
- "私有仓库", "private registry", "Harbor"
- "镜像加速", "registry mirror"
- "docker login", "authentication"

## Core Workflow

```bash
# Login
docker login
docker login registry.example.com   # Private registry

# Tag
docker tag myapp:latest myuser/myapp:v1.0.0
docker tag myapp:latest myuser/myapp:latest

# Push
docker push myuser/myapp:v1.0.0
docker push myuser/myapp:latest

# Pull
docker pull myuser/myapp:v1.0.0
docker pull myuser/myapp:latest
```

## Tag Strategy

| Tag | Purpose | Retention |
|-----|---------|-----------|
| `v1.2.3` | Exact release (semver) | Forever |
| `v1.2` | Minor version latest | Until next minor |
| `v1` | Major version latest | Until next major |
| `latest` | Latest build (dev only!) | Rolling |
| `sha256-abc123` | Digest pin | As needed |

```
Production: NEVER use :latest. Always pin exact version or digest.
Development: :latest is OK for convenience.
```

## Private Registry

### Docker Registry (Official)

```bash
docker run -d -p 5000:5000 --name registry \
  -v registry:/var/lib/registry \
  registry:2
docker tag myapp localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1
```

### Harbor (Enterprise)

```bash
# Download and run
wget https://github.com/goharbor/harbor/releases/download/v2.10.0/harbor-offline-installer-v2.10.0.tgz
tar xzf harbor-offline-installer-v2.10.0.tgz
cd harbor
cp harbor.yml.tmpl harbor.yml
# Edit harbor.yml (hostname, passwords)
./install.sh
```

## Image Digest (Immutable Reference)

```bash
# Get digest
docker inspect --format='{{.RepoDigests}}' myimage:tag

# Pull by digest (immutable)
docker pull alpine@sha256:abc123...
```

## Workflow — 推荐操作流程

Step 1: **登录仓库**: `docker login` 或 `docker login ghcr.io`
Step 2: **打标签**: `docker tag myapp:v1 ghcr.io/org/myapp:v1`
Step 3: **推送镜像**: `docker push ghcr.io/org/myapp:v1`
Step 4: **验证**: `docker pull ghcr.io/org/myapp:v1` 拉取确认
Step 5: **固定版本**: 生产使用 `docker pull myapp@sha256:abc...`

## Gotchas — Common Pitfalls

- **`:latest` in production**: Tags are mutable — `latest` can point to different images over time. → **Recovery**: Always pin version or digest: `docker pull myapp:v1.2.3@sha256:abc...`.
- **Mixed public/private registries**: `docker login` is per-registry. → **Recovery**: `docker login registry.example.com` separately; use credential helpers: `docker-credential-ecr-login` for AWS ECR.
- **Large image push timeout**: Set `max-concurrent-uploads` in daemon config for large images. → **Recovery**: Edit `/etc/docker/daemon.json`: `{"max-concurrent-uploads": 1}` for slow connections.
- **Registry auth in CI**: Use `docker/login-action` (GitHub Actions) or secrets manager. → **Recovery**: Never commit credentials; use OIDC for cloud registries instead of long-lived tokens.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 公共仓库使用（Docker Hub/GHCR） | 登录、push/pull、标签管理 |
| ✅ 能做 | 私有仓库搭建 | Docker Registry + Harbor 企业方案 |
| ✅ 能做 | 标签策略制定 | semver/sha256/digest 对比选型 |
| ⚠️ 需条件 | 镜像加速（registry-mirrors） | 需配置 daemon.json + 可用 mirror 服务 |
| ⚠️ 需条件 | Harbor 高可用部署 | 需额外配置 Redis Cluster + PG 主从 |
| ❌ 超范围 | 镜像构建 | 使用 `docker-build` |
| ❌ 超范围 | CVE 扫描 | 使用 `docker-scout` |
| ❌ 超范围 | CI/CD 镜像管理 | 使用 `docker-cicd` |

## When NOT to Use

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Building images | `docker-build` |
| Vulnerability scanning | `docker-scout` |
| CI/CD pipeline | `docker-cicd` |
| Docker basics | `docker-basics` |

## Security & Stability

- Never commit registry credentials. Use CI secrets manager.
- Use content trust: `export DOCKER_CONTENT_TRUST=1` for signed images.
- Harbor provides vulnerability scanning, replication, and RBAC.
- No executable scripts bundled. Guidance only.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Hub | https://docs.docker.com/docker-hub/ |
| Docker Hub API | https://docs.docker.com/reference/api/hub/latest/ |
| Docker Registry | https://docs.docker.com/registry/ |
| Harbor 项目 | https://goharbor.io/ |
| 镜像管理 CLI | https://docs.docker.com/reference/cli/docker/image/ |
| 内容信任 | https://docs.docker.com/engine/security/trust/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-hub` — 镜像仓库管理**

**← Prev**: `docker-scout` — Vulnerability scanning
**→ Next**: `docker-cicd` — CI/CD integration
