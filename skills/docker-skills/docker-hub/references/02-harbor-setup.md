# Harbor 企业级镜像仓库搭建

## 架构

```
┌───────────────────────────────────────────────┐
│                    Harbor                      │
│                                                │
│  ┌──────────┐  ┌───────────┐  ┌────────────┐ │
│  │  Portal  │  │  Core     │  │ Job Service│ │
│  │  (UI)    │  │  (API)   │  │            │ │
│  └──────────┘  └───────────┘  └────────────┘ │
│                                                │
│  ┌───────────┐  ┌───────────┐                 │
│  │ Registry  │  │ Trivy     │                 │
│  │ (OCI)     │  │ (扫描)    │                 │
│  └───────────┘  └───────────┘                 │
│                                                │
│  ┌──────────┐  ┌───────────────┐              │
│  │ Redis    │  │ PostgreSQL    │              │
│  │ (缓存)   │  │ (元数据)      │              │
│  └──────────┘  └───────────────┘              │
└───────────────────────────────────────────────┘
```

## 最小配置

```yaml
# harbor.yml
hostname: registry.example.com

http:
  port: 80

# 使用 HTTP（测试环境）或 HTTPS
# https:
#   port: 443
#   certificate: /data/certs/registry.crt
#   private_key: /data/certs/registry.key

harbor_admin_password: Harbor12345

database:
  password: root123
  max_idle_conns: 100
  max_open_conns: 900

data_volume: /data

trivy:
  ignore_unfixed: false
  skip_update: false
  offline_scan: false
  insecure: false
```

## 安装

```bash
# 在线安装（含 Trivy 扫描器）
./install.sh --with-trivy

# 仅核心功能
./install.sh
```

## 项目配置

1. 创建项目：Projects → New Project
2. 设为私有（Private）或公开（Public）
3. 配置成员权限：项目管理员/开发者/访客
4. 配置镜像代理缓存：Proxy Cache → 代理 Docker Hub

## 镜像复制（跨数据中心）

```
杭州 Harbor → 北京 Harbor
  ┌─────────────────┐      ┌─────────────────┐
  │ myapp:v1.2.3    │ ───→ │ myapp:v1.2.3    │
  └─────────────────┘      └─────────────────┘
```

配置：Administration → Replications → New Replication Rule

## 垃圾回收

```bash
# 手动触发
docker exec -it harbor-core /bin/bash
# Web UI: Administration → Garbage Collection
```

## 与 Docker Desktop 集成

Docker Desktop → Settings → Docker Engine：

```json
{
  "insecure-registries": ["registry.example.com"]
}
```
```

