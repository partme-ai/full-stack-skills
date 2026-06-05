---
name: docker-troubleshooting
description: Guidance for debugging and troubleshooting Docker issues. Covers container startup failures (exit codes, docker logs, inspect), disk space exhaustion (system df/prune, log rotation), OOM and resource pressure (memory limits, stats), network connectivity problems (network inspect, iptables, DNS resolution), storage issues (permission denied, volume inspection), daemon problems (dockerd startup, socket permissions), and common error diagnosis. Use when the user asks about docker troubleshooting, docker debug, OOM, disk full, network issues, docker not starting, container crash, or needs to investigate Docker problems. 使用场景：docker 排查、docker debug、容器问题、OOM、磁盘满、网络不通、启动失败、配置问题.
license: Apache-2.0
---

# Docker Troubleshooting — 问题排查与调试

Systematic approach to diagnosing and resolving common Docker issues.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker 排查", "docker debug", "容器问题"
- "容器启动失败", "exit code", "crash"
- "OOM", "磁盘满", "disk full"
- "网络不通", "network issues"
- "docker daemon", "daemon not running"

## Diagnostic Framework

```
1. Check container state    → docker ps -a, docker inspect
2. Check logs               → docker logs --tail 100
3. Check resources          → docker stats, docker system df
4. Check exit code          → docker inspect --format='{{.State.ExitCode}}'
5. Interactive debug        → docker run --rm -it image sh
```

## Container Startup Failure

### Exit Code Reference

| Code | Meaning | Action |
|------|---------|--------|
| **0** | Success | — |
| **1** | Application error | Check `docker logs` |
| **125** | Docker daemon error | Check daemon status |
| **126** | Command cannot execute | Check permissions |
| **127** | Command not found | Check CMD/ENTRYPOINT path |
| **137** | SIGKILL (OOM or docker kill) | Check memory limits |
| **139** | SIGSEGV (segfault) | Application bug |
| **143** | SIGTERM (graceful stop) | Health check timeout? |

```bash
# Quick diagnosis
docker ps -a | grep Exited
docker inspect --format='{{.State.ExitCode}} {{.State.Error}}' container
docker logs container
```

## Disk Space Exhaustion

```bash
# Check disk usage
docker system df

# What's using space?
docker system df -v   # Verbose breakdown

# Clean up
docker system prune -a     # Remove all unused: images, containers, volumes, networks
docker image prune -a      # Unused images only
docker volume prune        # Unused volumes only

# Log rotation (prevent future issues)
docker run --log-opt max-size=10m --log-opt max-file=3 myapp
```

## OOM (Out of Memory)

```bash
# Check if container was OOM-killed
docker inspect --format='{{.State.OOMKilled}}' container

# Check memory usage
docker stats --no-stream

# Solution: increase memory limit
docker update --memory=1g --memory-swap=1g container
```

## Network Connectivity

```bash
# Check network configuration
docker network inspect bridge
docker exec container ip addr show
docker exec container ping other-container

# DNS check
docker exec container nslookup other-container
docker exec container cat /etc/resolv.conf

# Host networking check
iptables -t nat -L DOCKER -n   # Port forwarding rules
```

## Permission Issues

```bash
# Bind mount permission denied
# Solution 1: Match UID
docker run -u $(id -u):$(id -g) -v $PWD:/app myapp

# Solution 2: Fix permissions in entrypoint
# In entrypoint script: chown -R appuser:appgroup /data

# Docker socket permission
sudo usermod -aG docker $USER   # Add user to docker group
newgrp docker                    # Refresh group (or re-login)
```

## Workflow — 排查流程

Step 1: **查看状态**: `docker ps -a` → 确认退出码和 OOMKilled
Step 2: **查看日志**: `docker logs --tail 100 <container>` 获取错误信息
Step 3: **深入检查**: `docker inspect` → 检查网络/挂载/资源限制
Step 4: **交互调试**: `docker run -it --rm --entrypoint sh <image>` 进入排查
Step 5: **资源排查**: `docker stats` + `docker system df` 检查 CPU/内存/磁盘

## Gotchas — Common Pitfalls

- **`docker system prune` is destructive**: Removes ALL unused objects. Don't run blindly in production. → **Recovery**: Use `docker system df` first to preview; add `--filter "until=24h"` for safe cleanup; never run `prune -a` without confirmation.
- **Logs fill disk silently**: JSON-file driver has NO rotation by default. A noisy app can fill the disk in hours. → **Recovery**: `docker run --log-opt max-size=10m --log-opt max-file=3 app`; existing: `truncate -s 0 $(docker inspect -f '{{.LogPath}}' myapp)`.
- **OOMKilled=TRUE but no error in logs**: SIGKILL can't be logged. → **Recovery**: Check `docker inspect -f '{{.State.OOMKilled}}' myapp`; increase memory: `docker update --memory 512m myapp`.
- **Exited (0) but service not working**: Application started but crashed after health check passed. → **Recovery**: `docker logs --tail 100 myapp`; check if app listens on 0.0.0.0 (not 127.0.0.1); verify with `docker exec myapp netstat -tlnp`.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 容器启动失败排查 | 退出码分析 + docker logs + inspect |
| ✅ 能做 | 磁盘/日志/资源问题 | docker system df + prune + log rotation |
| ✅ 能做 | OOM/CPU 排查 | docker stats + --memory 限制 + OOMKilled |
| ⚠️ 需条件 | 网络包级分析 | 需 tcpdump/Wireshark + 网络知识 |
| ⚠️ 需条件 | 内核级问题 | 需 Linux 内核调试技能 |
| ❌ 超范围 | 应用代码 bug 修复 | 开发者修复代码 |
| ❌ 超范围 | 生产环境部署 | 使用 `docker-production` |
| ❌ 超范围 | 安全漏洞修复 | 使用 `docker-security` + `docker-scout` |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Setting up production | `docker-production` |
| Security issues | `docker-security` |
| Performance tuning | `docker-run` (resource limits) |
| Docker basics | `docker-basics` |

## Security & Stability

- `docker exec` into production containers can expose sensitive data. Prefer log-based debugging.
- `docker system prune -a` removes ALL unused images and volumes — use with caution in production.
- Inspecting containers with `--privileged` debug tools can bypass security controls.
- Never expose Docker socket (`/var/run/docker.sock`) to containers for debugging — it grants root access.
- Rotate debug logs — they may contain sensitive information. Use log drivers with TTL.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker 引擎故障排查 | https://docs.docker.com/engine/troubleshoot/ |
| docker logs 命令 | https://docs.docker.com/reference/cli/docker/container/logs/ |
| docker inspect | https://docs.docker.com/reference/cli/docker/inspect/ |
| Docker CLI 参考 | https://docs.docker.com/reference/cli/docker/ |
| 守护进程配置 | https://docs.docker.com/reference/cli/dockerd/ |
| 常见问题 FAQ | https://docs.docker.com/faq/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-troubleshooting` — 问题排查**

**← Previous**: `docker-production`
