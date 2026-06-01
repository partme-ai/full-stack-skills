# 监控栈 — Prometheus + Grafana + cAdvisor + Loki

## compose.yml

```yaml
name: monitoring

services:
  prometheus:
    image: prom/prometheus:v3.1.0
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'
      - '--web.enable-lifecycle'
    networks:
      - monitoring
    restart: unless-stopped

  grafana:
    image: grafana/grafana:11.4.0
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/datasources:/etc/grafana/provisioning/datasources:ro
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards:ro
    environment:
      GF_SECURITY_ADMIN_USER: ${GRAFANA_USER:-admin}
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_PASSWORD:-admin}
      GF_USERS_ALLOW_SIGN_UP: "false"
    networks:
      - monitoring
    depends_on:
      - prometheus
      - loki
    restart: unless-stopped

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.50.0
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
      - /dev/disk/:/dev/disk:ro
    privileged: true
    devices:
      - /dev/kmsg
    networks:
      - monitoring
    restart: unless-stopped

  node-exporter:
    image: prom/node-exporter:v1.8.2
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/rootfs'
    networks:
      - monitoring
    restart: unless-stopped

  loki:
    image: grafana/loki:3.2.0
    ports:
      - "3100:3100"
    volumes:
      - ./loki/loki-config.yaml:/etc/loki/local-config.yaml:ro
      - loki_data:/loki
    command: -config.file=/etc/loki/local-config.yaml
    networks:
      - monitoring
    restart: unless-stopped

  promtail:
    image: grafana/promtail:3.2.0
    volumes:
      - /var/log:/var/log:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - ./promtail/promtail-config.yaml:/etc/promtail/config.yml:ro
    command: -config.file=/etc/promtail/config.yml
    networks:
      - monitoring
    depends_on:
      - loki
    restart: unless-stopped

  alertmanager:
    image: prom/alertmanager:v0.28.0
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager/alertmanager.yml:/etc/alertmanager/alertmanager.yml:ro
      - alertmanager_data:/alertmanager
    networks:
      - monitoring
    restart: unless-stopped

networks:
  monitoring:
    driver: bridge

volumes:
  prometheus_data:
  grafana_data:
  loki_data:
  alertmanager_data:
```

## prometheus/prometheus.yml

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - '/etc/prometheus/alert.rules.yml'

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']

  - job_name: cadvisor
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: node-exporter
    static_configs:
      - targets: ['node-exporter:9100']
```

## 启动

```bash
docker compose up -d

# 访问
# Prometheus: http://localhost:9090
# Grafana:    http://localhost:3000
# cAdvisor:   http://localhost:8080
```
```

