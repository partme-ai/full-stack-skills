# 多阶段构建目标选择

## Dockerfile

```dockerfile
FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY . .
RUN go build -o /app .

FROM golang:1.23-alpine AS tester
WORKDIR /src
COPY . .
RUN go test ./...

FROM alpine:3.20 AS runtime
COPY --from=builder /app /usr/local/bin/app
CMD ["app"]
```

## 按目标构建

```bash
# 仅构建测试阶段（不产生最终镜像）
docker build --target tester -t myapp:test .

# 构建运行阶段
docker build --target runtime -t myapp:latest .

# 构建全部阶段（默认）
docker build -t myapp:latest .
```

## 场景

| 场景 | 命令 |
|------|------|
| CI 仅跑测试 | `docker build --target tester .` |
| 构建生产镜像 | `docker build --target runtime -t myapp:prod .` |
| 调试编译阶段 | `docker build --target builder -t myapp:debug .` && `docker run -it myapp:debug sh` |
```

