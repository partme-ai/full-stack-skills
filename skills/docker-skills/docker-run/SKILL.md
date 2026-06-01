---
name: docker-run
description: Guidance for running and managing Docker containers. Covers the complete container lifecycle (create/start/stop/rm/restart), resource constraints (--memory/--cpus), health checks (HEALTHCHECK), restart policies, logging drivers, container inspection (inspect/stats/top), exec debugging, and signal handling. Use when the user asks about docker run, container management, resource limits, health checks, docker logs, docker exec, restart policies, or needs to manage running containers. 使用场景：docker run、容器管理、资源限制、健康检查、重启策略、docker logs、docker exec、docker ps.
license: Apache-2.0
---

# Docker Run — Container Lifecycle Management

Complete guidance for running, monitoring, and managing Docker containers.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker run", "运行容器", "启动容器"
- "docker ps", "docker stop", "docker restart"
- "容器资源限制", "memory limit", "CPU limit"
- "健康检查", "healthcheck"
- "docker logs", "查看日志"
- "docker exec", "进入容器"
- "restart policy", "容器重启策略"

## Container Lifecycle

```
docker pull → docker create → docker start → docker run (create+start)
                                                │
                          ┌─────────────────────┼─────────────────────┐
                          ▼                     ▼                     ▼
                      Running              Paused/Stopped         Killed
                          │                     │
                          ▼                     ▼
                      docker stop          docker start
                      docker kill          docker restart
                      docker rm            docker rm -f
```

## `docker run` — Complete Reference

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

# Most common form
docker run -d --name myapp \
  -p 8080:8080 \
  -v /host/path:/container/path \
  -e ENV_VAR=value \
  --restart unless-stopped \
  myimage:tag
```

| Flag | Purpose | Example |
|------|---------|---------|
| `-d` | Detached (background) | `-d` |
| `--name` | Container name | `--name my-nginx` |
| `-p` | Port mapping (host:container) | `-p 8080:80` |
| `-v` | Volume/bind mount | `-v data:/var/lib/mysql` |
| `-e` | Environment variable | `-e DB_HOST=localhost` |
| `--env-file` | Load env from file | `--env-file .env` |
| `--restart` | Restart policy | `--restart unless-stopped` |
| `--rm` | Auto-remove on stop | `--rm` (for temp containers) |

## Resource Constraints

```bash
# Memory: limit + reservation
docker run --memory=512m --memory-reservation=256m myapp

# CPU: shares (relative) + cpus (absolute)
docker run --cpus=2 --cpu-shares=1024 myapp

# Combined: production-grade limits
docker run -d \
  --memory=1g --memory-swap=1g \
  --cpus=2 \
  --pids-limit=100 \
  myapp
```

| Resource | Flag | Best Practice |
|----------|------|--------------|
| Memory | `--memory=512m` | Always set; container can exhaust host memory otherwise |
| Memory+Swap | `--memory-swap=1g` | Set equal to memory to disable swap |
| CPU | `--cpus=2` | Hard limit; `--cpu-shares` for relative priority |
| PIDs | `--pids-limit=100` | Prevent fork bombs |
| Ulimits | `--ulimit nofile=65536` | File descriptor limits |

## Health Checks

### Dockerfile HEALTHCHECK

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1
```

### Health Check States

```
starting → healthy (passes)
         → unhealthy (fails 3 consecutive checks)
```

```bash
# Check health status
docker inspect --format='{{.State.Health.Status}}' myapp

# Health check in compose
# services.app.healthcheck.test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
```

## Restart Policies

| Policy | Behavior | Use Case |
|--------|----------|----------|
| `no` | Never restart (default) | One-off tasks |
| `on-failure[:N]` | Restart on non-zero exit, max N times | Batch jobs |
| `always` | Always restart | Critical services (be careful — infinite loop risk) |
| `unless-stopped` | Restart unless explicitly stopped | **Recommended for most services** |

```bash
docker run --restart unless-stopped myapp
docker update --restart always myapp  # Change policy on running container
```

## Logging & Debugging

```bash
# View logs
docker logs myapp                # All logs
docker logs -f myapp             # Follow (tail -f)
docker logs --tail 50 myapp      # Last 50 lines
docker logs --since 10m myapp    # Last 10 minutes

# Execute commands in container
docker exec -it myapp sh         # Interactive shell
docker exec myapp cat /etc/hosts # Run single command

# Inspect state
docker inspect myapp             # Full JSON metadata
docker stats myapp               # Live resource usage
docker top myapp                 # Running processes
docker port myapp                # Port mappings
```

## Signal Handling

```bash
docker stop myapp    → SIGTERM → wait 10s → SIGKILL
docker kill myapp    → SIGKILL immediately
docker kill -s HUP myapp → Send custom signal
```

| Signal | docker command | Container effect |
|--------|---------------|------------------|
| SIGTERM | `docker stop` | Graceful shutdown (default) |
| SIGKILL | `docker kill` | Force kill (no cleanup) |
| SIGHUP | `docker kill -s HUP` | Reload config (app-specific) |

## Workflow — 推荐操作流程

Step 1: **拉取或构建镜像**: `docker pull` 或 `docker build` 准备好镜像
Step 2: **运行容器**: `docker run -d --name myapp -p 8080:8080 -v data:/data --memory 512m myapp`
Step 3: **验证启动**: `docker ps` + `docker logs myapp` 确认运行正常
Step 4: **配置健康检查**: 确保 HEALTHCHECK 在 Dockerfile 中定义或运行时指定
Step 5: **监控运行**: `docker stats` + `docker logs -f` 持续观察

## Gotchas — Common Pitfalls

- **Default `--memory=0` (unlimited)**: Container can consume all host memory. → **Recovery**: `docker run --memory=512m --cpus=1 app`; check usage with `docker stats`.
- **`docker stop` timeout**: Default 10s grace period. → **Recovery**: `docker stop -t 30 myapp`; ensure app handles SIGTERM properly.
- **`docker run` creates new container**: Running `docker run nginx` twice creates two containers. → **Recovery**: `docker start <existing-name>` to restart; `docker ps -a` to find stopped containers.
- **Logs filling disk**: JSON-file driver has no rotation by default. → **Recovery**: `docker run --log-opt max-size=10m --log-opt max-file=3 app`; existing containers: edit `/etc/docker/daemon.json` + restart dockerd.
- **`docker exec` exit codes**: Returns the command's exit code. → **Recovery**: Use for scripting: `docker exec myapp healthcheck.sh || exit 1`.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | docker run 运行容器 | 所有参数、资源限制、重启策略 |
| ✅ 能做 | 健康检查配置 | HEALTHCHECK 指令 + 运行时覆盖 |
| ✅ 能做 | 日志管理 | 日志驱动选择 + 轮转配置 |
| ✅ 能做 | 进入容器调试 | docker exec / docker attach |
| ⚠️ 需条件 | --privileged 特权模式 | 仅调试用，生产禁止 |
| ⚠️ 需条件 | 修改运行中容器限制 | 需 `docker update`，部分参数不可动态改 |
| ❌ 超范围 | 编写 Dockerfile | 使用 `docker-dockerfile` |
| ❌ 超范围 | 多容器编排 | 使用 `docker-compose` |
| ❌ 超范围 | 镜像构建 | 使用 `docker-build` |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Docker basics / first-time setup | `docker-basics` |
| Writing Dockerfile | `docker-build` |
| Multi-container apps | `docker-compose` |
| Network configuration | `docker-networking` |
| Storage/Volume management | `docker-storage` |

## Security & Stability

- Always set `--memory` and `--cpus` limits in production to prevent noisy-neighbor issues.
- Avoid `--privileged` flag. Use specific `--cap-add` instead.
- Never run containers as root. Use `--user` flag or `USER` in Dockerfile.
- Use `--read-only` for stateless containers where possible.
- No executable scripts bundled. Guidance only.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker 引擎 | https://docs.docker.com/engine/ |
| docker run 参考 | https://docs.docker.com/reference/cli/docker/container/run/ |
| 容器管理 CLI | https://docs.docker.com/reference/cli/docker/container/ |
| 运行时选项 | https://docs.docker.com/engine/reference/run/ |
| 资源限制 | https://docs.docker.com/config/containers/resource_constraints/ |
| 日志驱动 | https://docs.docker.com/config/containers/logging/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-run` — Step 3: 容器管理与运维**

**← Previous**: `docker-build` — Dockerfile & 镜像构建
**→ Next**: `docker-networking` / `docker-storage` / `docker-compose`
