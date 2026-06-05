---
name: docker-buildx
description: Expert guidance for Docker image building — docker build CLI, buildx for multi-platform builds, BuildKit features (secret mounts, cache mounts, SSH forwarding, inline cache), Docker Build Cloud for accelerated cloud builds, layer caching strategies (--cache-from, --cache-to, GHA cache, registry cache), and CI/CD build optimization. Use when the user asks about docker build, buildx, multi-platform, multi-arch, linux/arm64, BuildKit, Build Cloud, Docker build acceleration, or build optimization. 使用场景：docker build、buildx、多平台构建、multi-platform、linux/arm64、BuildKit、Docker Build Cloud、构建加速、build optimization.
license: Apache-2.0
---

# Docker Buildx — 构建引擎与多平台

Expert guidance for `docker build`, buildx, multi-platform builds, and build optimization.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker build", "buildx", "构建镜像"
- "multi-platform", "multi-arch", "多平台构建"
- "linux/arm64", "linux/amd64"
- "BuildKit", "Build Cloud"
- "构建加速", "build cache", "构建缓存"
- "Docker build 慢", "怎么加速 docker build"
- Need to build images for multiple CPU architectures

## Core Commands

```bash
# Basic build
docker build -t myapp:v1 .

# Build with BuildKit (default in modern Docker)
DOCKER_BUILDKIT=1 docker build -t myapp:v1 .

# Build from specific Dockerfile
docker build -f Dockerfile.prod -t myapp:v1 .

# No cache rebuild
docker build --no-cache -t myapp:v1 .
```

## Buildx — Multi-Platform Builder

### Setup

```bash
# Create a builder instance
docker buildx create --name multiarch --use

# Inspect available platforms
docker buildx inspect --bootstrap
```

### Build for Multiple Platforms

```bash
# Build and push directly (single command)
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myorg/myapp:v1.0.0 \
  --push .

# Build and load to local Docker (single platform only)
docker buildx build \
  --platform linux/arm64 \
  -t myapp:arm64 \
  --load .

# Build and export as tar
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:v1.0.0 \
  --output type=tar,dest=myapp.tar .
```

### Platform Aliases

| Alias | Architectures |
|-------|---------------|
| `linux/amd64` | Intel/AMD 64-bit |
| `linux/arm64` | ARM 64-bit (Apple Silicon, AWS Graviton) |
| `linux/arm/v7` | ARM 32-bit (Raspberry Pi 3) |
| `linux/arm/v6` | ARM 32-bit (Raspberry Pi Zero) |

## BuildKit Features

### Secret Mount

```dockerfile
# Dockerfile
RUN --mount=type=secret,id=npmrc \
  cp /run/secrets/npmrc .npmrc && \
  npm ci && \
  rm .npmrc
```

```bash
docker buildx build --secret id=npmrc,src=$HOME/.npmrc -t myapp .
```

### Cache Mount (Persist Across Builds)

```dockerfile
# Python: persist pip cache
RUN --mount=type=cache,target=/root/.cache/pip \
  pip install -r requirements.txt

# Node.js: persist npm cache
RUN --mount=type=cache,target=/root/.npm \
  npm ci

# Go: persist module cache
RUN --mount=type=cache,target=/root/.cache/go-build \
  go build -o server .
```

### SSH Forwarding

```dockerfile
# Clone private repo during build
RUN --mount=type=ssh \
  git clone git@github.com:org/private-repo.git
```

```bash
docker buildx build --ssh default -t myapp .
```

### Inline Cache (Export Cache into Image)

```bash
# Export cache metadata into the image itself
docker buildx build \
  --build-arg BUILDKIT_INLINE_CACHE=1 \
  -t myapp:latest \
  --push .

# Later builds can use this image as cache source
docker build --cache-from myapp:latest -t myapp:v2 .
```

## Layer Caching — Pull Before Build

```bash
# Pull previous image for layer cache
docker pull myapp:latest || true
docker build \
  --cache-from myapp:latest \
  -t myapp:${TAG} .
```

## GitHub Actions — Multi-Platform

```yaml
- uses: docker/setup-buildx-action@v3
- uses: docker/build-push-action@v6
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: user/app:latest
    cache-from: type=gha          # GitHub Actions cache
    cache-to: type=gha,mode=max
```

## Workflow — 推荐构建流程

Step 1: **创建 Builder**: `docker buildx create --name multiarch --driver docker-container --use`
Step 2: **选择方案**: 单平台（--load）还是多平台（--push）？交叉编译还是 QEMU？
Step 3: **配置 Dockerfile**: 使用 `--platform=$BUILDPLATFORM` + `ARG TARGETOS TARGETARCH`
Step 4: **执行构建**: `docker buildx build --platform linux/amd64,linux/arm64 -t app --push .`
Step 5: **验证**: `docker buildx imagetools inspect app` 确认多架构 manifest

## Gotchas — Common Pitfalls

- **`--load` with multi-platform**: `--load` only works for a SINGLE platform. → **Recovery**: Use `--push` or `--output type=oci,dest=image.tar` for multi-platform; or build single platform with `--load`.
- **QEMU emulation is slow**: Building ARM on AMD is 5-10x slower. → **Recovery**: Use native ARM runners in CI (`ubuntu-24.04-arm` on GitHub Actions); or Docker Build Cloud for native multi-arch builders.
- **BuildKit by default**: Modern Docker uses BuildKit by default. → **Recovery**: `DOCKER_BUILDKIT=1` is a no-op on Docker 23+; use `docker buildx build` for explicit BuildKit control.
- **`--cache-from` without pulling first**: Docker won't pull the cache image automatically. → **Recovery**: `docker pull myapp:latest || true` before `docker build --cache-from myapp:latest`.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 多平台构建（linux/amd64,arm64） | buildx + QEMU/交叉编译/原生节点 |
| ✅ 能做 | BuildKit 高级特性 | secret mount、cache mount、SSH 转发、内联缓存 |
| ✅ 能做 | Docker Build Cloud 接入 | 云端构建 + 团队共享缓存 |
| ⚠️ 需条件 | 多平台 + --load | 仅支持单平台，多平台需 --push |
| ⚠️ 需条件 | ARM 本地无 QEMU | 需 `docker run --privileged --rm tonistiigi/binfmt --install all` |
| ❌ 超范围 | Dockerfile 编写 | 使用 `docker-dockerfile` |
| ❌ 超范围 | 基础 docker build/tag/push | 使用 `docker-build` |
| ❌ 超范围 | 容器编排（Compose/Swarm） | 使用 `docker-compose`/`docker-production` |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Writing Dockerfile content | `docker-dockerfile` |
| Compose-based builds | `docker-compose` |
| Docker basics | `docker-basics` |
| Running containers | `docker-run` |

## Security & Stability

- Never expose secrets in build logs. Use `--secret` for BuildKit or CI secrets masking.
- Multi-platform images must be pushed to a registry — `--load` only works for single platform.
- Cache images in CI should be pulled with `|| true` — first build won't have a cache.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Build | https://docs.docker.com/build/ |
| Buildx 参考 | https://docs.docker.com/reference/cli/docker/buildx/ |
| BuildKit | https://docs.docker.com/build/buildkit/ |
| Docker Build Cloud | https://docs.docker.com/build-cloud/ |
| 多平台构建 | https://docs.docker.com/build/building/multi-platform/ |
| 构建缓存 | https://docs.docker.com/build/cache/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-buildx` — 构建引擎**

**← Previous**: `docker-dockerfile` — Write Dockerfiles
**→ Next**: `docker-run` — Run containers / `docker-cicd` — CI/CD
