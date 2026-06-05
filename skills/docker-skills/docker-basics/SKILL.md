---
name: docker-basics
description: Docker entry point — provides comprehensive guidance for Docker concepts, architecture, and basic operations. Covers what Docker is, container vs VM comparison, Docker architecture (Client-Server, daemon, registry), installation guidance for Linux/Mac/Windows, and first-container walkthrough. Includes Docker object model (Image/Container/Registry/Engine), CLI basics, and the Docker ecosystem overview. Use when the user asks about Docker basics, needs to understand Docker concepts, is new to Docker, or wants containerization fundamentals. 使用场景：Docker 入门、什么是 Docker、容器概念、Docker vs VM、Docker 安装、docker 基础命令、container basics、Docker 架构.
license: Apache-2.0
---

# Docker Basics — 概念与基础

Docker 生态的第一入口。从零理解 Docker 概念、架构和基础操作。

## When to Use

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| New to Docker, learning from scratch | Already proficient with Docker |
| Need to understand container vs VM | Need specific Dockerfile/CLI commands → `docker-build` / `docker-run` |
| Setting up Docker for the first time | Need multi-container orchestration → `docker-compose` |
| Evaluating whether to adopt Docker | Need security scanning → `docker-security` |

## Core Concepts

| Concept | Definition | Analogy |
|---------|-----------|---------|
| **Image** | Read-only template with app + dependencies | Class definition |
| **Container** | Runnable instance of an image | Object instance |
| **Registry** | Repository for storing/sharing images | App Store |
| **Docker Engine** | Runtime that builds and runs containers | JVM / Python interpreter |

## Container vs VM

| Aspect | Container | VM |
|--------|----------|-----|
| **Isolation** | Process-level (share host kernel) | Hardware-level (full OS) |
| **Startup** | Seconds | Minutes |
| **Size** | MB | GB |
| **Density** | Dozens per host | Few per host |
| **Use Case** | Microservices, CI/CD, dev environments | Legacy apps, multi-OS, strong isolation |

## Docker Architecture

```
┌─────────────────────────────┐
│         Docker CLI           │  ← docker build/run/push...
├─────────────────────────────┤
│       Docker Daemon          │  ← dockerd: manages images, containers, networks, volumes
├─────────────────────────────┤
│       containerd             │  ← container runtime supervisor
├─────────────────────────────┤
│        runc                  │  ← OCI runtime (actually runs containers)
└─────────────────────────────┘
         │
    ┌────┴────┐
    ▼         ▼
 Registry   Host OS
 (Docker    (Linux kernel:
  Hub)       namespaces, cgroups)
```

## Quick Start

```bash
# Verify installation
docker --version
docker run hello-world

# Pull and run your first container
docker pull nginx:alpine
docker run -d -p 8080:80 --name my-nginx nginx:alpine

# Check it's running
curl localhost:8080
docker ps
docker stop my-nginx
```

## Docker Object Model

```
docker run → Container (running instance of an image)
docker build → Image (built from Dockerfile)
docker pull → Image (downloaded from Registry)
docker push → Image (uploaded to Registry)
docker volume → Volume (persistent data)
docker network → Network (container communication)
```

## Installation Path

| OS | Method | Notes |
|----|--------|-------|
| **macOS** | Docker Desktop | Includes GUI, CLI, Compose, K8s |
| **Windows** | Docker Desktop + WSL2 | WSL2 backend recommended |
| **Linux** | `apt/yum install docker-ce` | No GUI; add user to docker group |
| **CI/Server** | Docker Engine only | Minimal footprint |

## Key CLI Groups

```
docker container   → create, run, start, stop, rm, ls, inspect, logs, exec
docker image       → build, pull, push, tag, ls, rm, prune, inspect
docker volume      → create, ls, rm, prune, inspect
docker network     → create, ls, rm, inspect, connect, disconnect
docker system      → df, prune, info, events
```

## Workflow — 推荐学习路径

Step 1: **理解概念**: 阅读 Core Concepts（Image/Container/Registry/Engine）
Step 2: **安装验证**: `docker run hello-world` 确认安装成功
Step 3: **第一个容器**: `docker run -d -p 8080:80 nginx:alpine` 体验
Step 4: **进阶学习**: 掌握 docker build（写 Dockerfile）→ docker run（管理容器）
Step 5: **进入生态**: 按需探索 `docker-dockerfile`/`docker-build`/`docker-compose`

## Gotchas — Common Pitfalls

- **Image vs Container confusion**: `docker run` creates a NEW container each time. → **Recovery**: Use `docker start <name>` to restart an existing container; `docker ps -a` to see stopped containers.
- **Root permission**: Linux requires `sudo` unless user is added to `docker` group (security risk: docker group = root access). → **Recovery**: `sudo usermod -aG docker $USER && newgrp docker` or use rootless Docker.
- **Disk bloat**: Old images/volumes/cache accumulate fast. → **Recovery**: `docker system prune -a` monthly; check with `docker system df` first.
- **Port conflict**: `-p 8080:80` means host:8080 → container:80. If host port is taken, change host side. → **Recovery**: `lsof -i :8080` to find process occupying the port, then use a different port.
- **Data loss**: Without volumes, container data is ephemeral. → **Recovery**: Always use `-v volume_name:/data` for stateful data; never rely on container filesystem.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | Docker 概念教学（Image/Container/Registry/Engine） | 从零解释核心概念 |
| ✅ 能做 | 安装指导（macOS/Linux/Windows） | 提供各平台安装步骤 |
| ✅ 能做 | 第一个容器实操 | `docker run hello-world` + nginx 示例 |
| ⚠️ 需条件 | 深入理解容器原理 | 建议结合 Linux namespace/cgroups 文档 |
| ⚠️ 需条件 | Docker Compose 多容器 | 基础概念后进入 `docker-compose` 技能 |
| ❌ 超范围 | 编写 Dockerfile | 使用 `docker-dockerfile` |
| ❌ 超范围 | 构建/推送镜像 | 使用 `docker-build` |
| ❌ 超范围 | 生产部署/Swarm/K8s | 使用 `docker-production` |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Need to write Dockerfile | `docker-build` |
| Need container management | `docker-run` |
| Need multi-container apps | `docker-compose` |
| Already know Docker basics | Jump to specific skill |

## Security & Stability

- All examples are educational. Use official images and verified publishers in production.
- Docker group membership on Linux is equivalent to root access.
- No executable scripts bundled. This skill teaches concepts and basic operations.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker 概述 | https://docs.docker.com/get-started/docker-overview/ |
| Docker 概念 | https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/ |
| 安装 Docker | https://docs.docker.com/get-started/get-docker/ |
| Docker 引擎 | https://docs.docker.com/engine/ |
| Docker 入门 workshop | https://docs.docker.com/get-started/workshop/ |
| Docker CLI 参考 | https://docs.docker.com/reference/cli/docker/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-basics` — Step 1: Docker 概念与基础**

```
basics → build → run → networking/storage → compose → security/cicd → production/troubleshooting → ai-ml
```

**→ Next**: `docker-build` — Write Dockerfiles and build optimized images
