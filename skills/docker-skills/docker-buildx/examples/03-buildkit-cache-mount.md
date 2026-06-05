# BuildKit 缓存挂载：加速重复构建

```dockerfile
RUN --mount=type=cache,target=/cache/dir some-heavy-command
```

## 按生态

```dockerfile
# Go
RUN --mount=type=cache,target=/go/pkg/mod go mod download
# Maven
RUN --mount=type=cache,target=/root/.m2 mvn dependency:go-offline -B
# npm
RUN --mount=type=cache,target=/root/.npm npm ci
# pip
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
# Rust
RUN --mount=type=cache,target=/usr/local/cargo/registry \
    --mount=type=cache,target=/app/target \
    cargo build --release
```

```bash
# 清理缓存
docker buildx prune --filter=until=24h
docker buildx prune --all
```
```

