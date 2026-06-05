# Spring Boot 层优化 — 最大化构建缓存命中率

Spring Boot 2.3+ 的 `layers.idx` 将 jar 拆为 4 层：dependencies → spring-boot-loader → snapshot-dependencies → application（变化最频繁）。

```dockerfile
# syntax=docker/dockerfile:1
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app
COPY build.gradle* settings.gradle* ./
COPY gradle ./gradle
COPY gradlew ./
RUN ./gradlew dependencies --no-daemon
COPY src ./src
RUN ./gradlew bootJar --no-daemon
RUN java -Djarmode=layertools -jar build/libs/*.jar extract

FROM eclipse-temurin:21-jre-alpine
RUN addgroup -S spring && adduser -S spring -G spring
USER spring
WORKDIR /app
COPY --from=builder /app/dependencies/ ./
COPY --from=builder /app/spring-boot-loader/ ./
COPY --from=builder /app/snapshot-dependencies/ ./
COPY --from=builder /app/application/ ./
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "org.springframework.boot.loader.launch.JarLauncher"]
```

## Maven pom.xml 配置

```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration><layers><enabled>true</enabled></layers></configuration>
</plugin>
```

| 场景 | 单层 COPY | 四层 COPY |
|------|----------|----------|
| 只改一行代码重构建 | 全部重建 (~60s) | 只重建 application 层 (~2s) |
| 新增依赖 | 全部重建 | 重建 dependencies + application |
```
