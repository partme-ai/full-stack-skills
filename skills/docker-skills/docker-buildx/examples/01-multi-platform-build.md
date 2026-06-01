# 多平台构建：linux/amd64 + linux/arm64

```bash
# 创建 builder
docker buildx create --name multiarch --driver docker-container --use
docker buildx inspect --bootstrap

# 单命令多平台
docker buildx build --platform linux/amd64,linux/arm64 --tag myapp:latest --push .
```

```dockerfile
FROM --platform=$BUILDPLATFORM golang:1.23-alpine AS builder
ARG TARGETOS TARGETARCH
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build -ldflags="-s -w" -o /app .
FROM alpine:3.20
COPY --from=builder /app /usr/local/bin/app
ENTRYPOINT ["app"]
```

```bash
# 验证 manifest
docker buildx imagetools inspect myapp:latest
# Name: docker.io/library/myapp:latest
# Manifests:
#   sha256:abc... (amd64)
#   sha256:def... (arm64)

# 仅构建到本地
docker buildx build --platform linux/amd64 --load -t myapp:local .
```
```

