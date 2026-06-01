---
name: docker-production
description: Guidance for deploying Docker in production environments. Covers Docker Swarm (init, join, stack deploy, service scaling, rolling updates), Kubernetes migration (kompose conversion, Helm charts, differences), resource quotas and limits, zero-downtime deployment patterns, monitoring with cAdvisor + Prometheus + Grafana, Docker with systemd, and production hardening. Use when the user asks about production Docker, swarm, stack deploy, K8s migration, zero-downtime, container monitoring, or needs to deploy Docker in production. 使用场景：生产部署、docker swarm、docker stack、K8s迁移、零停机部署、容器监控、生产环境.
license: Apache-2.0
---

# Docker Production — 生产环境部署

Guidance for deploying and managing Docker in production.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "生产部署", "production Docker"
- "docker swarm", "docker stack", "swarm cluster"
- "Kubernetes migration", "kompose", "K8s"
- "零停机部署", "rolling update"
- "容器监控", "监控", "Prometheus"

## Docker Swarm Quick Start

```bash
# Initialize cluster
docker swarm init --advertise-addr <MANAGER-IP>

# Join workers (run on worker nodes)
docker swarm join --token <TOKEN> <MANAGER-IP>:2377

# Deploy a stack
docker stack deploy -c docker-compose.yml myapp

# Manage services
docker service ls
docker service scale myapp_web=5
docker service update --image myapp:v2 myapp_web
docker service logs -f myapp_web
```

### Swarm Compose Example

```yaml
version: '3.8'
services:
  web:
    image: myapp:${TAG:-latest}
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
      rollback_config:
        parallelism: 1
        delay: 10s
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    ports:
      - "80:8080"
```

## Zero-Downtime Deployment

```
Rolling Update Flow:

┌──────┐  ┌──────┐  ┌──────┐     Old replicas (v1)
│ v1  │  │ v1  │  │ v1  │
└──────┘  └──────┘  └──────┘

docker service update --image myapp:v2 web

Step 1: Start v2
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
│ v1  │  │ v1  │  │ v1  │  │ v2  │    ← 1 new
└──────┘  └──────┘  └──────┘  └──────┘

Step 2: Replace one v1 with v2
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
│ v1  │  │ v1  │  │ v2  │  │ v2  │    ← 2 new
└──────┘  └──────┘  └──────┘  └──────┘

... until all v2
```

## Kubernetes Migration

```bash
# Convert compose to K8s
kompose convert -f docker-compose.yml

# Output:
# web-deployment.yaml
# web-service.yaml
# ...

# Apply
kubectl apply -f .
```

| Compose | K8s |
|---------|-----|
| services | Deployments + Services |
| networks | Network Policies |
| volumes | PersistentVolumeClaims |
| deploy.replicas | Deployment.spec.replicas |
| secrets | Secrets |

## Monitoring Stack

### cAdvisor + Prometheus + Grafana

```yaml
# docker-compose.monitoring.yml
services:
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports: ["8080:8080"]
    volumes:
      - /:/rootfs:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /sys:/sys:ro

  prometheus:
    image: prom/prometheus:latest
    ports: ["9090:9090"]
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports: ["3000:3000"]
```

## Workflow — 推荐部署流程

Step 1: **单机部署**: compose.yml + `restart: unless-stopped` + systemd 守护
Step 2: **Swarm 集群**: `docker swarm init` → `docker stack deploy -c compose.yml myapp`
Step 3: **滚动更新**: `docker service update --image myapp:v2` + health check + rollback
Step 4: **监控接入**: Prometheus + cAdvisor + Grafana 绑定额仪表盘
Step 5: **K8s 迁移**: `kompose convert` → 手动添加资源限制+健康检查 → Helm Chart

## Gotchas — Common Pitfalls

- **Single Swarm manager**: If the only manager goes down, the cluster is unresponsive. → **Recovery**: Use 3 or 5 managers; `docker node promote <worker>` to add manager; back up `/var/lib/docker/swarm/` regularly.
- **Rolling update health check**: Without health checks, updates may deploy broken containers. → **Recovery**: Define HEALTHCHECK in Dockerfile + service health check; use `--update-failure-action rollback`.
- **Data without volumes**: Production databases MUST use volumes. Container restart = new filesystem without volumes. → **Recovery**: `docker service create --mount type=volume,src=db_data,target=/var/lib/mysql`.
- **Direct K8s migration**: `kompose` is a starting point, not production-ready K8s configs. → **Recovery**: After `kompose convert`, manually add resource limits, health checks, init containers, and ConfigMap/Secret references.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 单机 Compose 生产部署 | compose.yml + systemd 守护 |
| ✅ 能做 | Swarm 集群管理 | init/join/stack deploy/rolling update |
| ✅ 能做 | K8s 迁移方案 | kompose + 手动调整 + Helm Chart |
| ✅ 能做 | 生产监控搭建 | Prometheus + cAdvisor + Grafana + Loki |
| ⚠️ 需条件 | 多数据中心 Swarm | 需 overlay 网络 + 低延迟连接 |
| ⚠️ 需条件 | 零停机迁移 K8s | 需蓝绿/金丝雀发布策略 |
| ❌ 超范围 | 应用代码部署 | 各语言 CI/CD 管道 |
| ❌ 超范围 | K8s 集群搭建 | 使用 K8s 官方文档 |
| ❌ 超范围 | 数据库高可用 | DBA 专业领域 + 数据库原生方案 |

## When NOT to Use

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Development/debugging | `docker-run` |
| Single-container apps | `docker-run` + systemd |
| K8s-native from start | Skip Swarm, use K8s directly |
| Docker basics | `docker-basics` |

## Security & Stability

- Rotate Swarm join tokens regularly. Leaked worker tokens allow unauthorized node joining.
- Use Docker Secrets for all sensitive configuration in production stacks.
- Enable TLS for Docker daemon in production (`tlsverify` mode).
- Implement resource limits on all production services to prevent noisy-neighbor issues.
- Back up Swarm raft data regularly: `/var/lib/docker/swarm/`.
- Monitor node health and set up alerts for node failures.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Swarm | https://docs.docker.com/engine/swarm/ |
| Docker Stack | https://docs.docker.com/engine/swarm/stack-deploy/ |
| 管理指南 | https://docs.docker.com/admin/ |
| 生产环境 Compose | https://docs.docker.com/compose/production/ |
| 安全部署 | https://docs.docker.com/engine/security/ |
| Docker 引擎 | https://docs.docker.com/engine/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-production` — 生产部署**

**← Previous**: `docker-cicd` | **→ Next**: `docker-troubleshooting`
