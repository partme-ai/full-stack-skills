---
name: docker-build
description: Expert guidance for the `docker build` command — building container images, tagging strategies, build arguments, image management and inspection. Covers `docker build` complete syntax, `--build-arg` usage, image tagging (`docker tag`), image inspection (`docker inspect`, `docker history`, `docker image ls`), pushing to registries (`docker push`), image pruning (`docker image prune`, `docker system prune`), and Docker BuildKit basics. Distinct from docker-dockerfile (focuses on Dockerfile authoring) and docker-buildx (focuses on multi-platform builds and advanced BuildKit). Use when the user asks about docker build, docker tag, docker push, docker images, docker image management, or how to build and manage Docker images. 使用场景：docker build 构建镜像、docker tag 打标签、docker push 推送镜像、docker images 镜像管理、docker image 命令、构建参数 --build-arg、镜像标签、docker build 命令.
license: Apache-2.0
---

# Docker Build — 镜像构建与管理

Complete reference for `docker build` and image lifecycle management. Build, tag, inspect, push, prune.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker build", "怎么构建镜像", "docker build 命令"
- "docker tag", "docker push", "推送镜像"
- "docker images", "镜像管理", "docker image"
- "--build-arg", "构建参数"
- "docker history", "docker inspect", "镜像查看"
- "docker image prune", "docker system prune", "清理镜像"

| ✅ Use When | ❌ Use Instead |
|------------|---------------|
| Running docker build, tagging, pushing | |
| Managing local images | |
| Needing `docker build` CLI reference | |
| Writing the Dockerfile itself | `docker-dockerfile` |
| Multi-platform builds | `docker-buildx` |
| BuildKit advanced features | `docker-buildx` |

## docker build — Complete Syntax

```bash
docker build [OPTIONS] PATH | URL | -
```

### Essential Options

```bash
# Basic build
docker build -t myapp:v1 .

# Tag multiple tags at once
docker build -t myapp:v1.2.3 -t myapp:latest -t ghcr.io/org/myapp:v1.2.3 .

# Build from specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build from Git repository
docker build -t myapp https://github.com/user/repo.git#main

# Build from stdin
cat Dockerfile | docker build -t myapp -
docker build -t myapp - <<EOF
FROM alpine:3.20
CMD ["echo", "hello"]
EOF
```

### Build Arguments (--build-arg)

```bash
# Pass build arguments
docker build --build-arg NODE_VERSION=22 --build-arg ENV=production -t myapp .

# From file
docker build --build-arg $(cat .env.build | xargs) -t myapp .
```

```dockerfile
ARG NODE_VERSION=20
FROM node:${NODE_VERSION}-alpine
ARG ENV=development
ENV NODE_ENV=${ENV}
RUN echo "Building for ${NODE_ENV}"
```

| Option | Purpose |
|--------|---------|
| `--build-arg KEY=VALUE` | Pass single argument |
| `--build-arg-file FILE` | Read args from file |
| `ARG KEY=default` | Define in Dockerfile with default |

### Build Control

```bash
# No cache (force full rebuild)
docker build --no-cache -t myapp .

# Pull base image even if cached locally
docker build --pull -t myapp .

# Quiet mode (only image ID)
docker build -q -t myapp .

# Set build target (multi-stage)
docker build --target builder -t myapp:builder .

# BuildKit output (export to local directory)
docker build --output type=local,dest=./out .

# Platform (with BuildKit)
docker build --platform linux/amd64 -t myapp .

# Add metadata
docker build --label "org.opencontainers.image.version=v1.2.3" -t myapp .
```

### Build Context

```bash
# Current directory
docker build -t myapp .

# Specific directory
docker build -t myapp ./app

# Remote Git repo
docker build -t myapp https://github.com/user/repo.git#v1.0.0:subdir

# Pipe context via stdin (no context)
docker build -t myapp - < Dockerfile
```

## Image Tagging — docker tag

```bash
# Tag an existing image
docker tag myapp:v1 myapp:latest
docker tag myapp:v1 ghcr.io/org/myapp:v1

# Tag with registry
docker tag myapp:v1 registry.example.com:5000/myapp:v1

# Force overwrite existing tag
docker tag myapp:v1 myapp:latest   # replaces where :latest points
```

### Tag Naming Convention

```
[registry[:port]/][namespace/]name[:tag|@digest]

ghcr.io/myorg/myapp:v1.2.3
│       │     │      │
│       │     │      └── tag (semver)
│       │     └── image name
│       └── namespace
└── registry
```

## Image Inspection

```bash
# List images
docker images
docker image ls
docker image ls --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# Inspect image details
docker inspect myapp:v1
docker inspect --format='{{.Config.Env}}' myapp:v1
docker inspect --format='{{.Created}}' myapp:v1

# View layer history
docker history myapp:v1
docker history --no-trunc --human myapp:v1

# Show digest
docker image ls --digests myapp
docker inspect --format='{{index .RepoDigests 0}}' myapp:v1
```

## Pushing to Registry

```bash
# Login
docker login
docker login ghcr.io -u USERNAME -p $TOKEN

# Push
docker push myapp:v1
docker push myapp --all-tags

# Push with digest
docker push myapp@sha256:abc123...
```

## Image Cleanup

```bash
# Remove specific image
docker rmi myapp:v1
docker image rm myapp:v1

# Remove dangling images (<none>:<none>)
docker image prune

# Remove all unused images
docker image prune -a

# Full system cleanup
docker system prune -a --volumes

# Check disk usage
docker system df
docker system df -v
```

## Workflow — 推荐构建流程

Step 1: **准备 Dockerfile**: 已完成编写（或使用 `docker-dockerfile` 生成）
Step 2: **配置构建参数**: 确认 --build-arg、--label、--target
Step 3: **执行构建**: `docker build -t myapp:v1 -t myapp:latest .`
Step 4: **验证镜像**: `docker images` / `docker history` / `docker inspect`
Step 5: **推送仓库**: `docker push` 前 `docker login`，生产环境用 digest 固定

## Gotchas — Common Pitfalls

- **`docker build -t myapp .` sends entire context**: Without `.dockerignore`, sends node_modules/.git and everything. Use `.dockerignore` to minimize context.
- **`docker build --no-cache` is slow**: Only use when truly needed. Normal builds reuse cached layers.
- **`docker tag` is mutable**: Tags can be moved. For production, use digest (`@sha256:...`) instead of tag.
- **`docker push` without login fails silently**: Always `docker login` first, or use CI credential helpers.
- **`docker system prune -a` is destructive**: Removes ALL unused images, containers, networks. Don't run in production without confirmation.
- **`docker build --pull` changes base image**: Your build may produce different output if base image was updated.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | docker build 构建镜像 | 完整命令语法、上下文管理、多 tag |
| ✅ 能做 | docker tag 打标签 | 命名规范、多 registry 标签 |
| ✅ 能做 | docker push 推送镜像 | 仓库登录、digest 固定 |
| ✅ 能做 | 镜像管理（inspect/history/prune） | 本地镜像生命周期 |
| ⚠️ 需条件 | BuildKit 高级特性（secret/cache/ssh） | 使用 `docker-buildx` |
| ⚠️ 需条件 | 网络不稳定时推送大镜像 | 配置 max-concurrent-uploads |
| ❌ 超范围 | Dockerfile 编写 | 使用 `docker-dockerfile` |
| ❌ 超范围 | 多平台构建（arm64/amd64） | 使用 `docker-buildx` |
| ❌ 超范围 | CI/CD 流水线集成 | 使用 `docker-cicd` |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Writing the Dockerfile itself | `docker-dockerfile` |
| Multi-platform/arm64 builds | `docker-buildx` |
| BuildKit secrets/cache/SSH | `docker-buildx` |
| Running containers | `docker-run` |
| Docker basics | `docker-basics` |

## Security & Stability

- Always scan built images with `docker scout` before pushing to production registry.
- Use `docker build --pull` to ensure base images are up-to-date with security patches.
- Never embed secrets in build args (`--build-arg` is visible in image history). Use BuildKit `--secret` instead.
- Tag images with `--label` for metadata (version, git SHA, build timestamp) for audit trails.
- Remove unused images regularly with `docker image prune` to free disk space and reduce attack surface.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Build | https://docs.docker.com/build/ |
| docker build 命令 | https://docs.docker.com/reference/cli/docker/build/ |
| docker tag | https://docs.docker.com/reference/cli/docker/image/tag/ |
| docker push | https://docs.docker.com/reference/cli/docker/image/push/ |
| docker image | https://docs.docker.com/reference/cli/docker/image/ |
| Dockerfile 参考 | https://docs.docker.com/reference/dockerfile/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-build` — 镜像构建与管理**

```
basics → dockerfile → build → buildx → run → compose → ...
```

**→ Next**: `docker-buildx` — Multi-platform builds and BuildKit advanced features
