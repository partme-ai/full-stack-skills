# 生产级 Compose 部署

## 资源限制

```yaml
services:
  api:
    image: myapp:latest
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M
          pids: 100
        reservations:
          cpus: "0.5"
          memory: 256M
```

## 滚动更新（零停机）

```yaml
services:
  api:
    image: myapp:latest
    deploy:
      replicas: 3
      update_config:
        parallelism: 1             # 每次更新几个
        delay: 10s                 # 间隔
        failure_action: rollback   # 失败回滚
        monitor: 30s               # 监控新容器是否正常
        max_failure_ratio: 0.3     # 容忍 30% 失败
        order: start-first         # 先启新再停旧
      rollback_config:
        parallelism: 1
        delay: 0s
```

## Secrets 管理

```yaml
secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    external: true                  # Swarm 中已存在

services:
  db:
    secrets:
      - db_password
    environment:
      MYSQL_PASSWORD_FILE: /run/secrets/db_password
```

## Configs（非敏感配置）

```yaml
configs:
  nginx_conf:
    file: ./nginx/nginx.conf

services:
  web:
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf
```

## 日志配置

```yaml
services:
  api:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
        labels: "com.docker.compose.project,com.docker.compose.service"
```

```yaml
# 使用 loki 驱动
logging:
  driver: loki
  options:
    loki-url: "http://loki:3100/loki/api/v1/push"
    loki-retries: "5"
    loki-batch-size: "400"
```

## systemd 守护

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=MyApp Docker Compose
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
ExecReload=/usr/bin/docker compose restart
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
```

## Kompose：迁移到 Kubernetes

```bash
# 转换
kompose convert -f compose.yml -o k8s/

# 输出
# k8s/api-deployment.yaml
# k8s/api-service.yaml
# k8s/db-deployment.yaml
# k8s/db-service.yaml
# k8s/frontend-networkpolicy.yaml
# k8s/backend-networkpolicy.yaml

# 直接部署到 K8s
kompose up -f compose.yml
```

## Compose vs Swarm vs K8s

| 特性 | Compose | Swarm | K8s |
|------|:--:|:--:|:--:|
| 单机 | ✅ | ✅ | ✅ |
| 多节点 | - | ✅ | ✅ |
| 自动扩缩 | - | ✅ | ✅ |
| 滚动更新 | - | ✅ | ✅ |
| 服务发现 | ✅（DNS） | ✅（内置） | ✅（kube-dns） |
| Secrets | ✅（文件） | ✅（加密） | ✅（etcd） |
| 学习曲线 | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
```

