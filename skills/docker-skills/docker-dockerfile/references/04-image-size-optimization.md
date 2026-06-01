# 镜像瘦身路线图：1GB → 50MB

## 五步法
```
1GB → 步骤1:多阶段构建 → ~300MB (-70%) → 步骤2:Alpine → ~120MB → 步骤3:distroless → ~50MB → 步骤4:清理 → ~40MB → 步骤5:dive分析 → ~35MB
```

## 步骤 1：多阶段构建
```dockerfile
FROM golang:1.23 AS builder
RUN go build -o /app
FROM alpine:3.20
COPY --from=builder /app /app
```

## 步骤 2：基础镜像选择
| 镜像 | 大小 | 场景 |
|------|------|------|
| ubuntu:24.04 | ~78 MB | 需要完整系统 |
| debian:bookworm-slim | ~28 MB | 需 apt |
| alpine:3.20 | ~3 MB | 通用首选 |
| distroless/static | ~2 MB | 纯 Go/C 静态 |
| scratch | 0 MB | 无 Shell |

决策树：需要包管理器？→ alpine | Go/C 静态？→ distroless/scratch | 其他 → alpine

## 步骤 3：distroless vs scratch
```dockerfile
# scratch（需手动复制 CA/时区/passwd）
FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /app /app
USER 65534
ENTRYPOINT ["/app"]
```

## 步骤 4：清理
- APT: `rm -rf /var/lib/apt/lists/*`
- APK: `--no-cache`
- pip: `--no-cache-dir`
- npm: `--production && npm cache clean --force`

## 步骤 5：dive 分析
```bash
brew install dive
dive my-image:tag
CI=true dive my-image:tag
```

| 语言 | 单阶段 | 多阶段+Alpine | distroless |
|------|--------|-------------|-----------|
| Go | ~850 MB | ~12 MB | ~8 MB |
| Java | ~470 MB | ~210 MB | ~150 MB |
| Node.js | ~350 MB | ~120 MB | ~80 MB |
| Python | ~200 MB | ~80 MB | N/A |
| Rust | ~1.5 GB | ~15 MB | ~6 MB |
```

