# DDD Observability Configuration

## Micrometer Custom Metrics

```java
@Component
public class DomainMetricsCollector {
    private final MeterRegistry registry;

    public DomainMetricsCollector(MeterRegistry registry) {
        this.registry = registry;
    }

    // Domain event publication metrics
    public void recordEventPublished(String eventType, String aggregateType) {
        Counter.builder("domain.events.published")
            .tag("event_type", eventType)
            .tag("aggregate_type", aggregateType)
            .register(registry)
            .increment();
    }

    public void recordEventProcessed(String eventType, Duration duration) {
        Timer.builder("domain.events.processing.duration")
            .tag("event_type", eventType)
            .publishPercentiles(0.5, 0.95, 0.99)
            .register(registry)
            .record(duration);
    }

    // Aggregate loading metrics
    public Timer.Sample startAggregateLoad() {
        return Timer.start(registry);
    }

    public void stopAggregateLoad(Timer.Sample sample, String aggregateType) {
        sample.stop(Timer.builder("domain.aggregate.load.duration")
            .tag("aggregate_type", aggregateType)
            .publishPercentiles(0.5, 0.95, 0.99)
            .register(registry));
    }

    // Repository metrics
    public <T> T measureRepositoryCall(String repoName, String operation,
                                        Supplier<T> call) {
        return Timer.builder("domain.repository.call.duration")
            .tag("repository", repoName)
            .tag("operation", operation)
            .register(registry)
            .record(call);
    }

    // Outbox monitoring
    public void updateOutboxDepth(String destination, int depth) {
        Gauge.builder("domain.outbox.depth", () -> depth)
            .tag("destination", destination)
            .register(registry);
    }
}
```

## OpenTelemetry Tracing Integration

```java
@Component
public class DomainTracingConfig {

    @Autowired
    private Tracer tracer;

    // Trace domain event publication
    public Span startEventSpan(String eventType, String aggregateId) {
        Span span = tracer.spanBuilder("domain.event.publish")
            .setSpanKind(SpanKind.INTERNAL)
            .startSpan();
        span.setAttribute("event.type", eventType);
        span.setAttribute("aggregate.id", aggregateId);
        return span;
    }

    // Trace aggregate operations
    public Span startAggregateSpan(String operation, String aggregateType,
                                    String aggregateId) {
        Span span = tracer.spanBuilder("domain.aggregate." + operation)
            .setSpanKind(SpanKind.INTERNAL)
            .startSpan();
        span.setAttribute("aggregate.type", aggregateType);
        span.setAttribute("aggregate.id", aggregateId);
        return span;
    }

    // Propagate context across event boundaries
    public Context injectContext(Context context) {
        return context;
    }
}
```

## Logging Correlation

```xml
<!-- Logback pattern with trace context -->
<property name="DDD_LOG_PATTERN"
          value="%d{ISO8601} [%X{traceId},%X{spanId}] %-5level %logger{36} - %msg%n"/>

<appender name="JSON" class="ch.qos.logback.core.ConsoleAppender">
    <encoder class="net.logstash.logback.encoder.LogstashEncoder">
        <includeMdc>true</includeMdc>
        <fieldNames>
            <timestamp>@timestamp</timestamp>
            <version>[ignore]</version>
            <logger>logger.name</logger>
        </fieldNames>
    </encoder>
</appender>

<!-- Structured logging for domain events -->
<appender name="EVENT_JSON" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>logs/domain-events.json</file>
    <encoder class="net.logstash.logback.encoder.LogstashEncoder"/>
</appender>
```

## Spring Boot Actuator Configuration

```yaml
# application.yml — Actuator for DDD
management:
  endpoints:
    web:
      exposure:
        include: health,metrics,prometheus,info
  metrics:
    tags:
      application: ${spring.application.name}
      bounded-context: ${ddd.bounded-context:unknown}
    export:
      prometheus:
        enabled: true
    distribution:
      percentiles-histogram:
        "[domain.*]": true
      slo:
        "[domain.repository.call.duration]": "10ms,50ms,100ms,500ms"
  health:
    probes:
      enabled: true
```

## Custom Health Checks for Domain

```java
@Component
public class DomainHealthAggregator implements ReactiveHealthIndicator {

    @Autowired
    private List<HealthIndicator> domainHealthIndicators;

    @Override
    public Mono<Health> health() {
        return Flux.fromIterable(domainHealthIndicators)
            .flatMap(indicator -> Mono.fromCallable(indicator::health))
            .reduce(Health.up(), (combined, next) -> {
                // Aggregate health: all must be UP
                if (!"UP".equals(next.getStatus().getCode())) {
                    return Health.down(combined)
                        .withDetails(next.getDetails())
                        .build();
                }
                return combined;
            });
    }
}
```

## AlertManager Configuration

```yaml
# alertmanager.yml
route:
  receiver: "domain-team"
  routes:
    - match:
        severity: critical
      receiver: "domain-oncall"
      repeat_interval: 5m
    - match:
        severity: warning
      receiver: "domain-team"
      repeat_interval: 30m

receivers:
  - name: "domain-oncall"
    webhook_configs:
      - url: "https://hooks.example.com/domain/critical"
        send_resolved: true
  - name: "domain-team"
    slack_configs:
      - channel: "#ddd-alerts"
        api_url: "https://hooks.slack.com/services/xxx"
```
