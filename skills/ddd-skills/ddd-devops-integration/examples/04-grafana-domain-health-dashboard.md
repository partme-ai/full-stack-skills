# Grafana Domain Health Dashboard

用于领域事件监控的 Grafana 仪表板配置。

## Panels

| Panel | Metric | Type | Description |
|-------|--------|------|-------------|
| Event Publishing Rate | `rate(domain_events_published_total[5m])` | Time series | 每秒事件发布速率 |
| Processing Duration | `histogram_quantile(0.99, domain_events_processing_duration_seconds_bucket)` | Heatmap | P99 处理延迟 |
| Outbox Depth | `domain_outbox_depth` | Stat | 当前 Outbox 积压数量 |
| Error Rate | `rate(domain_events_error_total[5m])` | Time series | 错误率百分比 |

## Alert Rules

```yaml
- alert: DomainEventBacklog
  expr: rate(domain_events_published_total[2m]) > 100
  for: 2m
  severity: critical

- alert: OutboxQueueGrowing
  expr: domain_outbox_depth > 1000
  for: 1m
  severity: critical

- alert: EventProcessingErrorRate
  expr: rate(domain_events_error_total[5m]) / rate(domain_events_published_total[5m]) > 0.05
  for: 2m
  severity: warning
```

> 完整 Prometheus 配置见 [ddd-observability-config.md](../references/ddd-observability-config.md)。
