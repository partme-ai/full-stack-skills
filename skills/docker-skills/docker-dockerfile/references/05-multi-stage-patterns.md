# 多阶段构建 5 种模式

## 模式 1：编译分离（最常用）
```dockerfile
FROM lang:ver AS builder
# ... 编译 ...
FROM alpine:3.20
COPY --from=builder /app /app
```
适用：Go/Rust/C 编译型语言

## 模式 2：资产构建（前后端一体）
```dockerfile
FROM node:22 AS frontend-builder
COPY web/ ./ && RUN npm run build

FROM golang:1.23 AS backend-builder
COPY . . && RUN go build -o /server

FROM alpine:3.20
COPY --from=backend-builder /server /server
COPY --from=frontend-builder /dist /static
CMD ["/server"]
```

## 模式 3：测试并行
```dockerfile
FROM node:22 AS lint
RUN npm run lint
FROM node:22 AS unit-test
RUN npm run test:unit
FROM node:22 AS build
RUN npm run build
FROM alpine:3.20
COPY --from=build /app/dist /app
```

## 模式 4：平台矩阵
```dockerfile
FROM --platform=$BUILDPLATFORM golang:1.23 AS builder
ARG TARGETOS TARGETARCH
RUN CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /app
FROM alpine:3.20
COPY --from=builder /app /app
```
```bash
docker buildx build --platform linux/amd64,linux/arm64 -t app:latest .
```

## 模式 5：Common Base
```dockerfile
FROM alpine:3.20 AS base
RUN apk add --no-cache ca-certificates tzdata
FROM base AS app1
COPY app1 /app1 && CMD ["/app1"]
FROM base AS app2
COPY app2 /app2 && CMD ["/app2"]
```

| 模式 | 减少体积 | 加速构建 | 适用度 |
|------|:--:|:--:|------|
| 编译分离 | ⭐⭐⭐ | ⭐⭐ | 必须掌握 |
| 资产构建 | ⭐⭐ | ⭐⭐ | 前后端一体 |
| 测试并行 | - | ⭐⭐⭐ | CI |
| 平台矩阵 | - | ⭐⭐⭐ | 多架构 |
| Common Base | ⭐ | ⭐⭐ | 多镜像项目 |
```

