# Dockerfile Patterns for DDD Architectures

## Pattern 1: Optimized Multi-Stage Build (Monolith DDD)

```dockerfile
# Stage 1: Build
FROM eclipse-temurin:17-jdk-alpine AS builder
WORKDIR /build
COPY pom.xml .
COPY start/ start/
COPY domain/ domain/
COPY application/ application/
COPY infrastructure/ infrastructure/
COPY adapter/ adapter/
RUN --mount=type=cache,target=/root/.m2 \
    mvn clean package -DskipTests -pl start -am

# Stage 2: Runtime
FROM eclipse-temurin:17-jre-alpine AS runtime
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /app
COPY --from=builder /build/start/target/*.jar app.jar

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD wget -qO- http://localhost:8080/actuator/health || exit 1

USER appuser
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## Pattern 2: CQRS — Command Service (Write-Optimized)

```dockerfile
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY command-service/target/*.jar app.jar

# Write-optimized JVM tuning
ENV JAVA_OPTS="-Xms512m -Xmx2g \
  -XX:+UseZGC \
  -XX:MaxGCPauseMillis=10 \
  -Dspring.datasource.hikari.maximum-pool-size=20"

HEALTHCHECK --interval=15s --timeout=5s \
    CMD wget -qO- http://localhost:8080/actuator/health/readiness || exit 1

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

## Pattern 3: CQRS — Query Service (Read-Optimized)

```dockerfile
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY query-service/target/*.jar app.jar

# Read-optimized JVM tuning — larger heap for caching
ENV JAVA_OPTS="-Xms1g -Xmx4g \
  -XX:+UseZGC \
  -XX:MaxGCPauseMillis=50 \
  -Dspring.datasource.hikari.maximum-pool-size=5 \
  -Dspring.cache.type=caffeine"

HEALTHCHECK --interval=30s --timeout=5s \
    CMD wget -qO- http://localhost:8080/actuator/health/liveness || exit 1

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

## Pattern 4: Sidecar Container (for Event Monitoring)

```dockerfile
# sidecar/Dockerfile — Event monitor sidecar
FROM alpine:3.19
RUN apk add --no-cache curl jq
COPY monitor.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/monitor.sh
ENTRYPOINT ["monitor.sh"]
```

## Pattern 5: Distroless Base Image (Security-First)

```dockerfile
FROM maven:3.9-eclipse-temurin-17-alpine AS build
WORKDIR /build
COPY . .
RUN mvn clean package -DskipTests

FROM gcr.io/distroless/java17-debian12
COPY --from=build /build/start/target/*.jar /app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

## Docker Compose for Multi-Service DDD

```yaml
version: "3.9"
services:
  order-command:
    build:
      context: .
      dockerfile: Dockerfile.command
    ports: ["8081:8080"]
    environment:
      - DB_URL=jdbc:postgresql://write-db:5432/orders
      - EVENT_BOOTSTRAP_SERVERS=kafka:9092
    depends_on:
      write-db: { condition: service_healthy }
      kafka: { condition: service_started }

  order-query:
    build:
      context: .
      dockerfile: Dockerfile.query
    ports: ["8082:8080"]
    environment:
      - ES_HOSTS=elasticsearch:9200
    depends_on:
      elasticsearch: { condition: service_healthy }

  write-db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: orders
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s

  elasticsearch:
    image: elasticsearch:8.12.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    volumes: ["esdata:/usr/share/elasticsearch/data"]

  kafka:
    image: confluentinc/cp-kafka:7.6.0
    environment:
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092

volumes:
  pgdata:
  esdata:
```

## Image Optimization Rules

| Practice | Benefit |
|----------|---------|
| Multi-stage builds | Reduce image size by 60-80% |
| Distroless base | 0 CVE, smaller attack surface |
| Specific tag (not `:latest`) | Reproducible builds |
| Add non-root user | Container security best practice |
| Layer ordering: infrequent → frequent | Better layer cache utilization |
