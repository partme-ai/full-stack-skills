# Compose 文件完整语法速查

## 顶级元素

| 元素 | 说明 | 必需 |
|------|------|:--:|
| `name` | 项目名称（v2.24+） | - |
| `services` | 服务定义 | ✅ |
| `networks` | 网络拓扑 | - |
| `volumes` | 持久化卷 | - |
| `secrets` | 敏感数据（仅 Swarm） | - |
| `configs` | 非敏感配置（仅 Swarm） | - |
| `include` | 引入其他 Compose 文件 | - |

## Service 配置项速查

### 镜像与构建

```yaml
services:
  app:
    image: nginx:1.27-alpine             # 直接拉取
    build:                                # 从 Dockerfile 构建
      context: ./app
      dockerfile: Dockerfile.prod
      args:
        NODE_ENV: production
      target: production                  # 多阶段目标
      platforms:                          # 多平台（BuildKit）
        - linux/amd64
        - linux/arm64
    pull_policy: always                   # always/missing/never
```

### 端口

```yaml
ports:
  - "8080:80"                           # host:container
  - "127.0.0.1:3306:3306"               # 仅本地
  - "9090"                               # 随机 host 端口
  - target: 80
    published: 8080
    protocol: tcp
    mode: host                           # host/ingress (Swarm)
```

### 环境变量

```yaml
environment:
  NODE_ENV: production
  DB_URL: postgres://${DB_USER}:${DB_PASS}@db:5432/mydb

env_file:
  - .env
  - .env.production

# .env 文件（同目录下自动加载，用于变量替换 ${VAR}）
# DB_USER=myuser
# DB_PASS=secret
```

### 卷挂载

```yaml
volumes:
  - data_volume:/var/lib/mysql           # 命名卷
  - ./config:/etc/app/config:ro          # bind mount（绝对/相对路径）
  - /var/run/docker.sock:/var/run/docker.sock  # Docker socket
  - type: bind
    source: ./logs
    target: /var/log/app
  - type: tmpfs
    target: /tmp
    tmpfs:
      size: 128M
```

### 依赖与启动顺序

```yaml
depends_on:
  db:
    condition: service_healthy           # service_started/service_healthy/service_completed_successfully
    restart: true                        # 依赖重启时本服务也重启

  redis:
    condition: service_started

healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 10s
  start_interval: 2s
```

### 资源限制（Compose v2.x / docker compose）

```yaml
deploy:
  resources:
    limits:
      cpus: "0.5"
      memory: 256M
      pids: 100
    reservations:
      cpus: "0.25"
      memory: 128M
```

### 重启策略

```yaml
restart: unless-stopped                  # no/always/on-failure[:max-retries]/unless-stopped

deploy:
  restart_policy:
    condition: on-failure                # none/on-failure/any
    delay: 5s
    max_attempts: 3
    window: 120s
```

### 其他常用

```yaml
command: ["npm", "start"]               # 覆盖 CMD
entrypoint: ["/custom-entrypoint.sh"]    # 覆盖 ENTRYPOINT
user: "1000:1000"                        # 运行用户
working_dir: /app                        # 工作目录
stdin_open: true                         # -i
tty: true                                # -t
profiles:                                # 按 profile 启动
  - debug
  - tools
extra_hosts:                             # 额外 hosts
  - "host.docker.internal:host-gateway"
dns:
  - 8.8.8.8
  - 1.1.1.1
```

## Networks

```yaml
networks:
  frontend:
    driver: bridge
    driver_opts:
      com.docker.network.bridge.name: br-frontend
    ipam:
      config:
        - subnet: 172.28.0.0/16
    internal: false                       # 是否禁止外部访问

  backend:
    driver: bridge
    internal: true                        # 仅内部互通
    attachable: true                      # 允许外部容器连接
```

## Volumes

```yaml
volumes:
  db_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /mnt/data/db
    labels:
      backup: daily

  nfs_data:
    driver: local
    driver_opts:
      type: nfs
      o: addr=192.168.1.100,nolock,rw
      device: ":/exports/data"
```

## Profiles（可选服务）

```yaml
services:
  app:
    image: myapp

  debug-tools:
    image: nicolaka/netshoot
    command: sleep infinity
    profiles:
      - debug                              # 仅 --profile debug 时启动
```

```bash
docker compose --profile debug up -d
```

## 片段复用（x-扩展）

```yaml
x-logging: &default-logging
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 3s
  retries: 3

services:
  app1:
    logging: *default-logging
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]

  app2:
    logging: *default-logging
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:8081/health"]
```

## include（模块化）

```yaml
# compose.yml
include:
  - path: ./infra/compose.db.yml
  - path: ./infra/compose.mq.yml
  - path: ./services/compose.api.yml

name: full-stack
```
```

