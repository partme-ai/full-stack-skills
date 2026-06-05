# 多平台构建策略

| 策略 | 原理 | 速度 | 镜像 |
|------|------|:--:|:--:|
| QEMU 模拟 | CPU 指令翻译 | 慢 (10-50x) | 原生 |
| 原生节点 | 不同架构物理机 | 快 | 原生 |
| 交叉编译 | 编译器直接输出目标平台 | 最快 | 原生 |

## QEMU（最简单）
```bash
docker run --privileged --rm tonistiigi/binfmt --install all
docker buildx build --platform linux/amd64,linux/arm64 -t app .
```

## 原生节点（推荐生产）
```bash
docker buildx create --name multiarch --driver docker-container
docker buildx create --name multiarch --append --node arm64-node ssh://arm-server
```

## 交叉编译（最快，有语言限制）
```dockerfile
FROM --platform=$BUILDPLATFORM golang:1.23 AS builder
ARG TARGETOS TARGETARCH
RUN CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build
```

| 语言 | 推荐策略 |
|------|------|
| Go（纯 Go） | 交叉编译 |
| Go（CGO） | QEMU 或原生节点 |
| Rust | 交叉编译 |
| Java | QEMU（字节码跨平台） |
| Node.js/Python | QEMU |
| C/C++ | 交叉编译或 QEMU |
```

