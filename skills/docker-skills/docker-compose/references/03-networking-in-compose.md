# Compose 网络深度指南

## 默认网络行为

```yaml
# compose.yml（不定义 networks）
services:
  web:
    image: nginx
  api:
    image: myapp
```

启动后自动创建 `<project>_default` bridge 网络，所有服务加入，可通过 **服务名** DNS 互访：

```bash
# web 容器中可 ping api 服务名
docker compose exec web ping api
```

## 自定义网络

```yaml
services:
  web:
    networks:
      - frontend
  api:
    networks:
      - frontend
      - backend        # 多网络
  db:
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true      # 不暴露到宿主机
```

## 网络模式选择

| 模式 | 说明 | 场景 |
|------|------|------|
| `bridge`（默认） | 隔离网络 + NAT | 90% 场景 |
| `host` | 共享宿主机网络栈 | 高性能/固定端口 |
| `none` | 无网络 | 安全隔离 |
| `container:name` | 共享另一容器网络 | sidecar 模式 |

```yaml
services:
  app:
    network_mode: host

  sidecar:
    network_mode: service:app   # 共享 app 的网络
```

## 外部网络

连接已存在的 Docker 网络（如独立创建的共享网络）：

```bash
docker network create shared-network
```

```yaml
services:
  app:
    networks:
      - shared-network

networks:
  shared-network:
    external: true       # 使用已存在的网络
```

## IP 地址分配

```yaml
networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1

services:
  app:
    networks:
      frontend:
        ipv4_address: 172.28.0.10
```

## DNS 解析

Compose 内置 DNS，服务名即域名：

```
服务名 → 该服务的所有容器 IP
<service>.<network> → 指定网络中的容器 IP
```

```yaml
services:
  api:
    networks:
      - frontend
      - backend

  web:
    networks:
      - frontend
    # 可以访问: api, api.frontend, api.backend
```

## 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 服务名无法解析 | 不同网络 | 加入同一自定义网络 |
| `localhost` 不通 | Compose 中 localhost=本容器 | 用服务名 |
| 端口冲突 | host 网络直接占用 | 用 bridge + 端口映射 |
| `internal: true` 仍可被宿主机访问 | 误解 | `internal` 仅禁止出站，非禁止入站映射 |
```

