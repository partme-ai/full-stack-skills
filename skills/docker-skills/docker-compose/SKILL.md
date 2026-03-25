---
name: docker-compose
description: Provides comprehensive guidance for Docker Compose including multi-container applications, service definition, networking, and volumes. Use when the user asks about Docker Compose, needs to orchestrate multiple containers, define docker-compose services, or manage multi-container applications.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 docker-compose 定义多服务栈（services、networks、volumes）
- 本地或单机运行多容器（app、DB、缓存、队列）
- 管理环境变量、依赖顺序与健康检查

## How to use this skill

1. **配置**：`docker-compose.yml` 定义 services、image/build、ports、volumes、environment、depends_on；用 `profiles` 做可选服务。
2. **CLI**：`docker compose up -d`、`down`、`logs -f`、`ps`；override 用 `-f` 或 `docker-compose.override.yml`。
3. **环境**：`.env` 或 env_file 注入变量；secrets 用 Docker secrets 或外部方案。

### Example: docker-compose.yml with health check

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      db:
        condition: service_healthy
    environment:
      DATABASE_URL: postgres://user:pass@db:5432/mydb

  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 3

volumes:
  pgdata:
```

## Best Practices

- 服务间用内部网络；仅暴露必要端口。
- 数据卷命名或使用命名卷；避免依赖默认匿名卷路径。
- 生产多节点用 Kubernetes 或 Swarm；compose 适合开发与单机部署。

## Keywords

docker compose, docker-compose.yml, multi-container, 多容器, 编排
