---
name: docker
description: Provides comprehensive guidance for Docker including container creation, images, Dockerfile, docker-compose, and container management. Use when the user asks about Docker, needs to create Docker containers, build Docker images, or manage containerized applications.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写 Dockerfile、构建镜像、运行与管理容器
- 使用 docker run/build/exec/logs/network/volume 等命令
- 排查镜像层、权限、网络与资源问题

## How to use this skill

1. **Dockerfile**：多阶段构建减小镜像；COPY/ADD、ENV、EXPOSE、USER；避免以 root 长期运行。
2. **CLI**：`docker build -t tag .`、`docker run -d -p host:container -v ...`；`docker compose` 管理多容器。
3. **环境**：Linux 上需 Docker 引擎；Windows/macOS 用 Docker Desktop；生产注意存储驱动与资源限制。

## Best Practices

- 镜像打明确 tag；不用 latest 做生产依赖。
- 容器内进程用非 root；只挂载必要卷。
- 日志与数据外置；健康检查与重启策略配置好。

## Keywords

docker, Dockerfile, container, image, 容器, 镜像
