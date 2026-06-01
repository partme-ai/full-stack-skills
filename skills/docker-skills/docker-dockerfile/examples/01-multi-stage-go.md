# Go 微服务多阶段构建 — 12MB 级最终镜像

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.23-alpine AS builder
RUN apk add --no-cache git ca-certificates
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o /app ./cmd/api

FROM alpine:3.20
RUN apk add --no-cache ca-certificates tzdata
COPY --from=builder /app /usr/local/bin/server
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD wget -qO- http://localhost:8080/health || exit 1
ENTRYPOINT ["server"]
```

**.dockerignore**
```
.git/ .github/ *.md .env* Dockerfile* docker-compose* vendor/ tmp/
```

| 方案 | 镜像大小 |
|------|---------|
| 单阶段 golang:1.23 | ~850 MB |
| 多阶段 alpine | ~12 MB |
| 多阶段 scratch | ~8 MB |
```
