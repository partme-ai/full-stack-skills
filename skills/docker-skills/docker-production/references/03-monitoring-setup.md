# Docker 监控栈搭建

## 组件

| 组件 | 用途 | 端口 |
|------|------|:--:|
| **Prometheus** | 指标收集与存储 | 9090 |
| **Grafana** | 可视化仪表盘 | 3000 |
| **cAdvisor** | 容器资源监控 | 8080 |
| **Node Exporter** | 宿主机指标 | 9100 |
| **Loki** | 日志聚合 | 3100 |
| **Alertmanager** | 告警管理 | 9093 |

## 快速启动

```yaml
# compose.yml
services:
  prometheus:
    image: prom/prometheus:v3.1.0
    ports: ["9090:9090"]
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus

  grafana:
    image: grafana/grafana:11.4.0
    ports: ["3000:3000"]
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      GF_SECURITY_ADMIN_PASSWORD: admin

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.50.0
    ports: ["8080:8080"]
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    privileged: true

  node-exporter:
    image: prom/node-exporter:v1.8.2
    ports: ["9100:9100"]
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro

  loki:
    image: grafana/loki:3.2.0
    ports: ["3100:3100"]

  promtail:
    image: grafana/promtail:3.2.0
    volumes:
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - ./promtail-config.yml:/etc/promtail/config.yml:ro
    command: -config.file=/etc/promtail/config.yml

volumes:
  prometheus_data:
  grafana_data:
```

## prometheus.yml

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: cadvisor
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: node-exporter
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']
```

## Grafana 仪表盘 ID（导入）

| 仪表盘 | ID | 用途 |
|------|:--:|------|
| Docker Monitoring | 193 | 容器 CPU/内存/网络/IO |
| Node Exporter Full | 1860 | 宿主机指标 |
| cAdvisor | 14282 | 容器详情 |
| Loki | 13639 | 日志查询 |

## 常用 PromQL

```promql
# CPU 使用率
rate(container_cpu_usage_seconds_total{name="api"}[5m]) * 100

# 内存使用
container_memory_usage_bytes{name="api"} / 1024 / 1024

# 容器重启次数
changes(container_tasks_state{name="api"}[1h])

# 磁盘 IO
rate(container_fs_writes_bytes_total{name="api"}[5m])
```
```

