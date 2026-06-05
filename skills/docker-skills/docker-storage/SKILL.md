---
name: docker-storage
description: Guidance for Docker storage and data persistence. Covers storage types (Volume/Bind Mount/Tmpfs) with comparison and use-case selection, volume lifecycle management (create/ls/inspect/prune), bind mount patterns, tmpfs for ephemeral data, backup and restore strategies, storage driver selection (overlay2), database persistence best practices (PostgreSQL/MySQL/Redis), and NFS/cloud storage integration. Use when the user asks about docker volume, data persistence, bind mount, tmpfs, storage driver, backup, data volume, or needs persistent storage for containers. 使用场景：docker volume、数据持久化、bind mount、tmpfs、存储驱动、数据卷、备份恢复、数据库持久化.
license: Apache-2.0
---

# Docker Storage — 存储与数据持久化

Comprehensive guidance for managing persistent data in Docker.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker volume", "数据卷", "数据持久化"
- "bind mount", "tmpfs"
- "容器数据怎么保存", "数据不丢失"
- "数据库容器怎么持久化"
- "备份恢复", "存储驱动"

## Storage Type Comparison

| Type | Persistence | Performance | Use Case |
|------|:--:|:--:|------|
| **Volume** | ✅ (managed by Docker) | High (native) | Production databases, shared data |
| **Bind Mount** | ✅ (host filesystem) | High | Development (live code sync), config files |
| **Tmpfs** | ❌ (memory only) | Highest | Secrets, temp files, sensitive data |

### Visual Comparison

```
Volume:                       Bind Mount:               Tmpfs:
  Container                     Container                 Container
     │                              │                        │
  Docker-managed               /host/path                 Memory only
  /var/lib/docker/volumes/        ↕                     (no disk)
     ↕                         Container sees:              ↕
  Container sees:              /container/path           Container sees:
  /data                         = host files              /tmp (in RAM)
```

## Volume Management

```bash
# Create & inspect
docker volume create mydata
docker volume ls
docker volume inspect mydata

# Use in container
docker run -v mydata:/var/lib/mysql mysql:8
docker run --mount source=mydata,target=/var/lib/mysql mysql:8  # explicit syntax (recommended)

# Cleanup
docker volume prune      # Remove unused volumes
docker volume rm mydata  # Remove specific volume
```

### Named vs Anonymous Volumes

```
-v mydata:/data      → Named volume  (mydata) — survives container removal ✅
-v /data             → Anonymous volume — hard to identify later ❌
```

## Bind Mount

```bash
# Read-write bind mount
docker run -v $(pwd)/app:/app nginx

# Read-only (protect host files)
docker run -v $(pwd)/config:/etc/nginx:ro nginx

# Explicit syntax
docker run --mount type=bind,source=$(pwd)/app,target=/app nginx
```

## Tmpfs (Memory)

```bash
# Ephemeral data, never touches disk
docker run --tmpfs /tmp:rw,noexec,nosuid,size=64m nginx
docker run --mount type=tmpfs,destination=/tmp,tmpfs-size=64m nginx
```

## Database Persistence Patterns

### PostgreSQL

```bash
docker volume create pgdata
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:16-alpine
```

### MySQL

```bash
docker volume create mysqldata
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  -v mysqldata:/var/lib/mysql \
  -v $(pwd)/my.cnf:/etc/mysql/conf.d/my.cnf:ro \
  -p 3306:3306 \
  mysql:8.4
```

### Redis (Persistence)

```bash
docker volume create redisdata
docker run -d \
  --name redis \
  -v redisdata:/data \
  -p 6379:6379 \
  redis:7-alpine redis-server --appendonly yes
```

## Backup & Restore

```bash
# Backup (using a temporary container)
docker run --rm \
  -v mysqldata:/source \
  -v $(pwd):/backup \
  alpine tar czf /backup/mysqldata-backup.tar.gz -C /source .

# Restore
docker run --rm \
  -v mysqldata:/target \
  -v $(pwd):/backup \
  alpine tar xzf /backup/mysqldata-backup.tar.gz -C /target
```

## Storage Drivers

| Driver | Status | Notes |
|--------|:--:|------|
| **overlay2** | ✅ Default | Best for most use cases; copy-on-write |
| devicemapper | Deprecated | - |
| aufs | Deprecated | - |
| btrfs/zfs | Niche | Use if filesystem matches |

```bash
docker info | grep "Storage Driver"  # Check current
```

## Workflow — 推荐配置流程

Step 1: **确定存储类型**: 持久化数据 → Volume；开发热加载 → Bind Mount；临时缓存 → tmpfs
Step 2: **创建 Volume**: `docker volume create db_data`
Step 3: **挂载到容器**: `docker run -v db_data:/var/lib/mysql mysql`
Step 4: **验证**: `docker volume inspect db_data` + `docker exec mysql ls /var/lib/mysql`
Step 5: **备份**: `docker run --rm -v db_data:/source -v $(pwd):/backup alpine tar czf /backup/db.tar.gz -C /source .`

## Gotchas — Common Pitfalls

- **Anonymous volumes accumulate**: Every `-v /data` (no name) creates a new anonymous volume. → **Recovery**: `docker volume prune` cleans all unused; use named volumes: `-v mydata:/data`.
- **Bind mount paths**: Must be absolute. → **Recovery**: `-v $(pwd)/app:/app` for docker run; `-v ./app:/app` works in Compose only.
- **Permission issues with bind mounts**: Container UID != host UID → permission denied. → **Recovery**: `--user $(id -u):$(id -g)` or `RUN chown 1000:1000 /data` in Dockerfile entrypoint.
- **Data loss on container removal**: Without `-v`, data is lost when container is removed. `--rm` flag even worse. → **Recovery**: Always use named volumes: `docker run -v db_data:/var/lib/mysql`.
- **macOS bind mount performance**: Bind mounts on Docker Desktop Mac are slow. → **Recovery**: Use `:cached` or `:delegated` mount options, or named volumes for better I/O.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 数据持久化配置（Volume/Bind Mount/tmpfs） | 三类存储的创建、挂载、管理 |
| ✅ 能做 | 备份与恢复 | `tar` + `--volumes-from` 备份恢复 |
| ✅ 能做 | 存储驱动选型 | overlay2/btrfs/zfs 对比 |
| ⚠️ 需条件 | NFS/云存储 Volume 驱动 | 需安装对应驱动插件 |
| ⚠️ 需条件 | macOS 下 Bind Mount 性能 | 使用 `:cached`/`:delegated` 或命名 Volume |
| ❌ 超范围 | K8s PersistentVolume/PVC | 使用 `docker-production` + K8s 文档 |
| ❌ 超范围 | 分布式文件系统（Ceph/GlusterFS） | 系统管理员范畴 |
| ❌ 超范围 | 数据库性能优化 | DBA 专业领域 |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Running containers (no data concerns) | `docker-run` |
| Multi-container orchestration | `docker-compose` |
| Kubernetes Storage (PV/PVC) | K8s documentation |
| Docker basics | `docker-basics` |

## Security & Stability

- Use `:ro` for config files that containers should not modify.
- Never bind mount Docker socket (`/var/run/docker.sock`) without understanding the security implications.
- Backup volumes regularly, especially database volumes.
- No executable scripts bundled. Guidance only.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker 存储 | https://docs.docker.com/storage/ |
| Volumes | https://docs.docker.com/storage/volumes/ |
| Bind Mounts | https://docs.docker.com/storage/bind-mounts/ |
| tmpfs | https://docs.docker.com/storage/tmpfs/ |
| 存储驱动 | https://docs.docker.com/storage/storagedriver/ |
| docker volume 命令 | https://docs.docker.com/reference/cli/docker/volume/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-storage` — 数据持久化**

**← Previous**: `docker-run` / `docker-networking`
**→ Next**: `docker-compose` / `docker-security`
