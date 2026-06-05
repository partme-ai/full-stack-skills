# Monitoring & Alerting Reference for DDD

## Prometheus Metrics Configuration

```yaml
# prometheus.yml — scrape config for DDD services
scrape_configs:
  - job_name: 'ddd-services'
    metrics_path: '/actuator/prometheus'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        regex: '(order|payment|notification).*'
        action: keep
      - source_labels: [__meta_kubernetes_pod_label_domain_bounded_context]
        target_label: bounded_context
      - source_labels: [__meta_kubernetes_pod_label_app]
        target_label: service
```

## Key DDD Metrics

```yaml
# Domain Event Metrics
domain_events_published_total:
  type: counter
  labels: [event_type, aggregate_type]
  description: Total domain events published

domain_events_processing_duration_seconds:
  type: histogram
  labels: [event_type]
  buckets: [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5]
  description: Domain event processing latency

aggregate_loading_duration_seconds:
  type: histogram
  labels: [aggregate_type]
  buckets: [0.01, 0.05, 0.1, 0.5, 1]
  description: Aggregate root loading time

repository_query_duration_seconds:
  type: histogram
  labels: [repository, operation]
  description: Repository query latency

outbox_queue_depth:
  type: gauge
  labels: [destination]
  description: Number of pending outbox messages
```

## PrometheusAlerting Rules

```yaml
# alerts/ddd-alerts.yml
groups:
  - name: ddd-domain-alerts
    interval: 30s
    rules:
      - alert: DomainEventBacklog
        expr: |
          sum by (event_type) (
            rate(domain_events_published_total[5m])
          ) -
          sum by (event_type) (
            rate(domain_events_processed_total[5m])
          ) > 100
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "Domain event backlog for {{ $labels.event_type }}"

      - alert: AggregateLoadingSlow
        expr: |
          histogram_quantile(0.95,
            rate(aggregate_loading_duration_seconds_bucket[5m])
          ) > 0.5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "P95 aggregate loading > 500ms for {{ $labels.aggregate_type }}"

      - alert: OutboxQueueGrowing
        expr: outbox_queue_depth > 1000
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Outbox queue depth > 1000 for {{ $labels.destination }}"

      - alert: HighEventProcessingErrorRate
        expr: |
          rate(domain_events_failed_total[5m]) /
          rate(domain_events_processed_total[5m]) > 0.05
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Event processing error rate > 5% for {{ $labels.event_type }}"

      - alert: NPlusOneDetection
        expr: |
          rate(repository_query_count_total[1m]) /
          rate(repository_aggregate_load_count_total[1m]) > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Possible N+1 queries for {{ $labels.repository }}"
```

## Grafana Dashboard (JSON Model)

```json
{
  "title": "DDD Domain Health",
  "panels": [
    {
      "title": "Domain Event Publication Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(domain_events_published_total[5m])",
          "legendFormat": "{{event_type}}"
        }
      ]
    },
    {
      "title": "Event Processing Latency (P95)",
      "type": "heatmap",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, rate(domain_events_processing_duration_seconds_bucket[5m]))",
          "legendFormat": "{{event_type}}"
        }
      ]
    },
    {
      "title": "Aggregate Load Times",
      "type": "stat",
      "targets": [
        {
          "expr": "histogram_quantile(0.99, rate(aggregate_loading_duration_seconds_bucket[5m]))"
        }
      ]
    },
    {
      "title": "Outbox Queue Depth",
      "type": "gauge",
      "targets": [
        {
          "expr": "outbox_queue_depth"
        }
      ]
    }
  ]
}
```

## Log Aggregation Patterns

```xml
<!-- logback-spring.xml — DDD-specific appenders -->
<configuration>
    <!-- Domain event audit log -->
    <appender name="DOMAIN_EVENT" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/domain-events.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>logs/domain-events-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>100MB</maxFileSize>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{ISO8601} | %X{traceId} | %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Aggregate performance log -->
    <appender name="AGGREGATE_PERF" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/aggregate-perf.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>logs/aggregate-perf-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>100MB</maxFileSize>
            <maxHistory>7</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{ISO8601} | %-5level | %msg%n</pattern>
        </encoder>
    </appender>

    <logger name="com.example.domain.event" level="INFO" additivity="false">
        <appender-ref ref="DOMAIN_EVENT"/>
    </logger>

    <logger name="com.example.domain.aggregate.performance" level="WARN" additivity="false">
        <appender-ref ref="AGGREGATE_PERF"/>
    </logger>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>
</configuration>
```

## Custom DDD Health Indicator

```java
@Component
public class DddHealthIndicator implements HealthIndicator {
    private final EventBus eventBus;
    private final DataSource dataSource;
    private final MeterRegistry meterRegistry;

    @Override
    public Health health() {
        Health.Builder builder = new Health.Builder();

        // Domain event bus health
        try {
            boolean busHealthy = eventBus.ping();
            builder.withDetail("eventBus", busHealthy ? "UP" : "DOWN");
            if (!busHealthy) builder.down();
        } catch (Exception e) {
            builder.down().withDetail("eventBus", e.getMessage());
        }

        // Aggregate load health
        double p99LoadTime = meterRegistry
            .get("aggregate.load.time")
            .histogram()
            .takeSnapshot()
            .getPercentileValues()
            .stream()
            .filter(p -> p.percentile() == 0.99)
            .findFirst()
            .map(p -> p.value())
            .orElse(0.0);

        builder.withDetail("aggregateP99LoadMs", String.format("%.0f", p99LoadTime));
        if (p99LoadTime > 1000) {
            builder.down();
        }

        return builder.build();
    }
}
```
