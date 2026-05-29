# ELK Stack 集成

## Elastic Stack 架构

```
Kibana (可视化/仪表盘/Dev Tools)
    ↓
Elasticsearch (存储/搜索/聚合)
    ↓
Logstash (ETL)  ←  Filebeat (日志)  ←  Metricbeat (指标)  ←  其他 Beats
```

## Logstash 配置

```ruby
# logstash.conf — 接收文件日志, 解析后写入 ES
input {
  beats {
    port => 5044
  }
  file {
    path => "/var/log/app/*.log"
    start_position => "beginning"
  }
}

filter {
  # 解析 Nginx 日志
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  # 解析 JSON 格式
  json {
    source => "message"
    target => "parsed"
    skip_on_invalid_json => true
  }
  # 添加时间戳
  date {
    match => ["timestamp", "ISO8601"]
    target => "@timestamp"
  }
  # 地理 IP 解析
  geoip {
    source => "client_ip"
    target => "geo"
  }
  # 字段处理
  mutate {
    remove_field => ["message", "original"]
    convert => ["response", "integer"]
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "nginx-logs-%{+YYYY.MM.dd}"
    user => "elastic"
    password => "${ES_PASSWORD}"
    ssl => true
    cacert => "/etc/elasticsearch/certs/ca.crt"
  }
}
```

Logstash 是 ETL 工具，适合复杂数据转换（grok/geoip/useragent）。纯日志采集场景推荐 Filebeat（更轻量）。

## Filebeat 配置

```yaml
# filebeat.yml — 轻量级日志采集
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/nginx/access.log
      - /var/log/nginx/error.log
    fields:
      service: nginx
      env: production
    fields_under_root: true

  - type: log
    enabled: true
    paths:
      - /var/log/app/*.log
    multiline:
      pattern: '^\d{4}-\d{2}-\d{2}'
      negate: true
      match: after       # 合并多行异常堆栈

filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: true

output.elasticsearch:
  hosts: ["localhost:9200"]
  username: "elastic"
  password: "${ES_PASSWORD}"
  index: "filebeat-%{[agent.version]}-%{+yyyy.MM.dd}"

setup.kibana:
  host: "localhost:5601"
```

**Filebeat 特点**：轻量级、资源占用低、支持多行合并 (Java 异常堆栈)、模块化配置。

## Metricbeat 配置

```yaml
# metricbeat.yml — 系统和应用指标采集
metricbeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: true

metricbeat.modules:
  - module: system
    metricsets:
      - cpu
      - memory
      - network
      - diskio
      - filesystem
      - process
    period: 10s
    enabled: true
  - module: elasticsearch
    metricsets:
      - node
      - node_stats
      - cluster_stats
      - index
    period: 10s
    hosts: ["localhost:9200"]
```

## Kibana 核心功能

| 功能 | 说明 |
|------|------|
| **Discover** | 日志搜索浏览 (KQL / Lucene 查询) |
| **Dashboard** | 仪表盘组合多个可视化 |
| **Visualize** | 创建图表 (柱状图/折线图/饼图/地图) |
| **Maps** | 地理空间分析 |
| **Canvas** | 自定义报告设计 |
| **Machine Learning** | 异常检测/预测 |
| **APM** | 应用性能监控 |
| **Security** | SIEM 安全分析 |

## KQL 查询语法

```
service.name: "my-app" AND http.response.status_code >= 400
agent.hostname: "web-*" AND NOT response_time > 5s
```

## 实战: 构建 Nginx 日志分析管道

1. **Filebeat** 采集 `/var/log/nginx/access.log`
2. **Logstash** (可选) 解析日志 → grok 提取字段 + geoip 解析 IP
3. **Elasticsearch** 存储到 `nginx-logs-YYYY.MM.dd` 索引 (ILM 管理)
4. **Kibana** 创建 Dashboard: 请求量趋势、状态码分布、TOP URL、地理分布

**完整 pipeline 参考**：
```bash
# 使用 Filebeat Nginx 模块 (免手动配置)
filebeat modules enable nginx
filebeat setup
```
