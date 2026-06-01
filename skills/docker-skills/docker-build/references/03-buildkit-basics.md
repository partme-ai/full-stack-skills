# BuildKit 基础：本地构建加速

## 启用 BuildKit

```bash
# 方式1：环境变量
export DOCKER_BUILDKIT=1
docker build -t myapp .

# 方式2：Daemon 配置（永久）
# /etc/docker/daemon.json
{ "features": { "buildkit": true } }

# 方式3：docker buildx（推荐）
docker buildx build -t myapp --load .

# 检查是否启用
docker buildx version
```

## BuildKit 带来的提升

| 功能 | 传统构建 | BuildKit |
|------|:--:|:--:|
| 并行构建 | ❌ 串行 | ✅ 并行无依赖的层 |
| 构建缓存 | ❌ 仅本地 | ✅ `--cache-from` / `--cache-to` |
| 密钥挂载 | ❌ 嵌入层 | ✅ `--mount=type=secret` |
| 缓存挂载 | ❌ | ✅ `--mount=type=cache` |
| SSH 转发 | ❌ | ✅ `--mount=type=ssh` |
| 构建输出 | ❌ 仅镜像 | ✅ `--output` 导出文件 |

## 基础 BuildKit 用法

```bash
# 使用 registry 缓存
docker buildx build \
  --cache-from type=registry,ref=myapp:buildcache \
  --cache-to type=registry,ref=myapp:buildcache,mode=max \
  -t myapp:latest \
  --load .

# 行式输出（CI 友好）
docker buildx build --progress plain -t myapp --load .

# 仅构建不加载到本地
docker buildx build -t myapp .
# 镜像不在 docker images 中，需 --load 或 --push
```

## 迁移到 buildx

```bash
# 传统
docker build -t myapp .

# 等价 buildx
docker buildx build -t myapp --load .

# 多 tag
docker build -t myapp:v1 -t myapp:latest .
docker buildx build -t myapp:v1 -t myapp:latest --load .
```

## 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `buildx build` 后 `docker images` 看不到 | buildx 默认不加载到本地 | 加 `--load` |
| `--load` 不支持多平台 | buildx 限制 | 单平台用 `--load`，多平台用 `--push` |
| 构建变慢 | driver 是 docker（非 docker-container） | `docker buildx create --use` |
```

