---
name: docker-compose
description: Expert guidance for Docker Compose — writing production-grade compose.yml files for multi-container applications. Covers complete Compose file syntax (services, networks, volumes, secrets, configs, profiles, extends, include), service configuration (image/build, ports, environment, env_file, depends_on with health checks, deploy resources, restart policies), networking in Compose (default networks, custom networks, internal networks), volume management, environment variable strategies (.env vs environment vs env_file), override files for multi-environment, profiles for optional services, and migration to Kubernetes with kompose. Use when the user asks about docker compose, docker-compose.yml, compose file, multi-container, service orchestration, compose configuration, or needs to write/modify a compose file. 使用场景：docker compose、docker-compose.yml、compose 文件、多容器、服务编排、compose 配置、depends_on、profiles.
license: Apache-2.0
---

# Docker Compose — 多容器编排与 Compose 文件

Expert guidance for writing production-grade Docker Compose configurations.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker compose", "docker-compose.yml", "compose 文件"
- "compose 怎么写", "compose 配置"
- "多容器", "multi-container", "服务编排"
- "depends_on", "profiles", "override"
- "compose network", "compose volume"

## Complete File Structure

```yaml
# compose.yml
name: myapp

services:       # Container definitions
networks:       # Network topology
volumes:        # Persistent storage
secrets:        # Sensitive data (Swarm)
configs:        # Non-sensitive configs (Swarm)
```

## Services — Core Configuration

```yaml
services:
  web:
    image: myapp:${TAG:-latest}     # Pull from registry
    # build: .                      # Or build from Dockerfile
    # build:                        # Build with options
    #   context: .
    #   dockerfile: Dockerfile.prod

    container_name: myapp-web       # Explicit name (optional)
    hostname: web

    ports:
      - "8080:8080"                 # host:container
      - "127.0.0.1:8443:443"       # bind to localhost
      - "8080:8080/udp"            # UDP

    environment:
      - NODE_ENV=production
      - DB_HOST=db                  # Service name = hostname!
    # env_file: .env.production    # Load from file

    volumes:
      - app-logs:/var/log/app       # Named volume
      - ./config:/etc/app:ro        # Bind mount (read-only)
      - /tmp/app:/tmp               # Bind mount (read-write)

    depends_on:
      db:
        condition: service_healthy  # Wait for health check
      redis:
        condition: service_started

    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 10s

    restart: unless-stopped

    deploy:                         # Swarm-only
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

    profiles:                       # Optional service
      - debug
```

## Networking

### Default Network (Auto-Created)

```yaml
# Compose auto-creates a default bridge network.
# All services can reach each other by service name.
services:
  web:
    ports: ["8080:8080"]
  db:
    # No ports exposed externally — only accessible by 'web'
```

### Custom Networks

```yaml
networks:
  frontend:                        # Public-facing
  backend:
    internal: true                 # No external access

services:
  web:
    networks: [frontend, backend]  # In both networks
  db:
    networks: [backend]            # Backend only (isolated)
  cache:
    networks: [backend]
```

## Environment Variables

### Approaches

| Method | Where | Best For |
|--------|-------|----------|
| `environment:` | In compose.yml | Simple, few vars |
| `env_file:` | External `.env.prod` | Many vars, env-specific |
| `.env` file | Project root (auto-loaded) | Default values, `$VARIABLE` substitution |

### .env File (Auto-Loaded)

```bash
# .env — auto-loaded by docker compose
TAG=v1.2.3
DB_PASSWORD=secret123
```

```yaml
# compose.yml — uses ${TAG} and ${DB_PASSWORD}
services:
  web:
    image: myapp:${TAG:-latest}
  db:
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
```

### env_file

```bash
# .env.production
DB_HOST=prod-db.example.com
DB_PORT=5432
```

```yaml
services:
  web:
    env_file: .env.production
```

## Depends On — Service Order

```yaml
services:
  db:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      retries: 5

  web:
    depends_on:
      db:
        condition: service_healthy   # Wait for DB to be ready
      redis:
        condition: service_started   # Wait for Redis to start
```

## Profiles — Optional Services

```yaml
services:
  app:
    image: myapp

  debug-tools:
    image: nicolaka/netshoot
    command: sleep infinity
    profiles: [debug]                # Only starts with --profile

  elasticsearch:
    image: elasticsearch:8.15.0
    profiles: [analytics]            # Only starts with --profile
```

```bash
docker compose --profile debug up    # Starts app + debug-tools
docker compose --profile analytics up # Starts app + elasticsearch
```

## Multi-Environment with Override

```
compose.yml                # Base configuration
compose.override.yml       # Local dev overrides (auto-applied)
compose.prod.yml           # Production overrides
```

```bash
# Local: compose.yml + compose.override.yml (auto)
docker compose up -d

# Production: explicit files
docker compose -f compose.yml -f compose.prod.yml up -d
```

## Migration to Kubernetes

```bash
kompose convert -f compose.yml   # Generates K8s YAML files
kubectl apply -f .
```

## Workflow — 推荐编排流程

Step 1: **规划服务**: 列出所有服务、端口、数据卷、环境变量
Step 2: **编写 compose.yml**: 定义 services/networks/volumes
Step 3: **配置依赖**: depends_on + condition: service_healthy
Step 4: **本地验证**: `docker compose up -d` → `docker compose ps` → `docker compose logs`
Step 5: **生产部署**: 添加 resource limits、restart policy、日志轮转 → `docker compose -f compose.yml -f compose.prod.yml up -d`

## Gotchas — Common Pitfalls

- **depends_on without healthcheck**: `depends_on` only waits for container START, not READY. → **Recovery**: Always add `condition: service_healthy` + `healthcheck:` block; use `docker compose ps` to verify health status.
- **Port conflict**: Multiple services can't bind the same host port. → **Recovery**: Use different host ports or remove `ports:` for internal-only services (they communicate via service name).
- **Bind mount paths**: Relative paths are resolved from the compose file location. → **Recovery**: Use `./config` not `config/`; verify with `docker compose config` to see resolved paths.
- **`.env` file security**: `.env` files often contain secrets. → **Recovery**: Add `.env` to `.gitignore`; use Docker secrets for Swarm; use `.env.example` with placeholder values.
- **`docker compose` vs `docker-compose`**: Modern syntax is `docker compose` (plugin). → **Recovery**: `docker-compose` (standalone binary) is deprecated; always use `docker compose` (with space).

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 多容器应用编排 | services/networks/volumes/secrets/configs 完整定义 |
| ✅ 能做 | 环境管理 | .env / env_file / override 文件策略 |
| ✅ 能做 | 依赖控制 | depends_on + healthcheck + profiles |
| ⚠️ 需条件 | 多主机部署 | 迁移到 Swarm（`docker stack deploy`）或 K8s |
| ⚠️ 需条件 | 滚动更新/自动扩缩 | Compose 不支持，需 Swarm 或 K8s |
| ❌ 超范围 | 编写 Dockerfile | 使用 `docker-dockerfile` |
| ❌ 超范围 | K8s 部署 | 使用 `kompose convert` + K8s 技能 |
| ❌ 超范围 | 云服务编排（Terraform） | IaaC 工具 |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Single-container apps | `docker-run` |
| Writing Dockerfile | `docker-dockerfile` |
| Kubernetes deployment | K8s manifests / Helm charts |
| Docker basics | `docker-basics` |

## Security & Stability

- Use `internal: true` for backend networks to prevent external access.
- Never commit `.env` files with secrets. Use CI secrets or Docker Swarm secrets.
- Production Compose on single host: combine with systemd for auto-start on boot.
- Multi-host production: migrate to Swarm (`docker stack deploy`) or Kubernetes.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Compose 概述 | https://docs.docker.com/compose/ |
| Compose 文件参考 | https://docs.docker.com/reference/compose-file/ |
| Compose CLI | https://docs.docker.com/reference/cli/docker/compose/ |
| 环境变量 | https://docs.docker.com/compose/environment-variables/ |
| Compose 网络 | https://docs.docker.com/compose/networking/ |
| 生产环境 Compose | https://docs.docker.com/compose/production/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-compose` — 多容器编排**

**← Previous**: `docker-buildx` / `docker-networking`
**→ Next**: `docker-production` / `docker-cicd`
