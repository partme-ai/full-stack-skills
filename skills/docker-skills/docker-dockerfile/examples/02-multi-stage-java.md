# 通用 Java 多阶段构建 — Maven/Gradle → JRE slim

## Maven 版本

```dockerfile
# syntax=docker/dockerfile:1
FROM maven:3.9-eclipse-temurin-21-alpine AS builder
WORKDIR /build
COPY pom.xml ./
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn package -DskipTests -B

FROM eclipse-temurin:21-jre-alpine
RUN apk add --no-cache tzdata curl
RUN addgroup -S java && adduser -S java -G java
USER java
COPY --from=builder /build/target/*.jar /app/app.jar
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-XX:+UseZGC", "-XX:MaxRAMPercentage=75", "-jar", "/app/app.jar"]
```

## Gradle 版本

```dockerfile
FROM gradle:8.10-jdk21-alpine AS builder
WORKDIR /build
COPY build.gradle settings.gradle ./
COPY gradle ./gradle
COPY gradlew ./
RUN ./gradlew dependencies --no-daemon
COPY src ./src
RUN ./gradlew bootJar --no-daemon

FROM eclipse-temurin:21-jre-alpine
COPY --from=builder /build/build/libs/*.jar /app/app.jar
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
```

## jlink 定制 JRE（进一步瘦身）

```dockerfile
FROM eclipse-temurin:21-jdk-alpine AS jre-builder
RUN jlink --add-modules java.base,java.logging,java.sql,java.naming,java.management,java.net.http,jdk.unsupported --strip-debug --no-man-pages --no-header-files --compress=zip-6 --output /javaruntime

FROM alpine:3.20
COPY --from=jre-builder /javaruntime /opt/java
COPY --from=builder /build/target/*.jar /app/app.jar
ENV PATH=/opt/java/bin:$PATH
```

| 方案 | 镜像大小 |
|------|---------|
| openjdk:21 直接跑 jar | ~470 MB |
| jre-alpine 多阶段 | ~210 MB |
| jlink 定制 + alpine | ~90 MB |
```
