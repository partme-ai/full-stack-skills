# docker build 参数速查

## 完整参数表

| 参数 | 说明 | 示例 |
|------|------|------|
| `-t, --tag` | 镜像名称:标签 | `-t myapp:v1` |
| `-f, --file` | 指定 Dockerfile | `-f Dockerfile.prod` |
| `--build-arg` | 构建参数 | `--build-arg NODE_ENV=prod` |
| `--build-arg-file` | 从文件读取构建参数 | `--build-arg-file .env.build` |
| `--no-cache` | 不使用构建缓存 | `--no-cache` |
| `--pull` | 强制拉取基础镜像 | `--pull` |
| `--target` | 多阶段构建目标 | `--target builder` |
| `--platform` | 目标平台（需 BuildKit） | `--platform linux/amd64` |
| `--output` | BuildKit 输出格式 | `--output type=local,dest=./out` |
| `--label` | 镜像元数据 | `--label version=v1.2.3` |
| `--add-host` | 添加 hosts 条目 | `--add-host api:192.168.1.100` |
| `--network` | 构建时网络模式 | `--network host` |
| `-q, --quiet` | 安静模式（仅输出 ID） | `-q` |
| `--secret` | BuildKit 密钥挂载 | `--secret id=npmrc,src=.npmrc` |
| `--ssh` | BuildKit SSH 转发 | `--ssh default` |
| `--cache-from` | 外部缓存源 | `--cache-from myapp:latest` |
| `--progress` | 输出样式 | `--progress plain` |
| `--ulimit` | ulimit 设置 | `--ulimit nofile=1024:1024` |

## 镜像管理命令速查

| 命令 | 说明 |
|------|------|
| `docker build -t name:tag .` | 构建镜像 |
| `docker tag src:tag dst:tag` | 打标签 |
| `docker images` / `docker image ls` | 列出镜像 |
| `docker rmi name:tag` | 删除镜像 |
| `docker image prune` | 清理 dangling 镜像 |
| `docker image prune -a` | 清理所有未使用镜像 |
| `docker inspect name:tag` | 查看镜像详情 |
| `docker history name:tag` | 查看层历史 |
| `docker save name:tag -o file.tar` | 导出镜像 |
| `docker load -i file.tar` | 导入镜像 |
| `docker push name:tag` | 推送到仓库 |
| `docker pull name:tag` | 从仓库拉取 |
| `docker login` | 登录仓库 |
| `docker logout` | 登出仓库 |
| `docker system df` | 磁盘占用 |
| `docker system prune -a` | 全量清理 |

## 构建上下文优化

```bash
# 查看上下文大小
docker build -t myapp . 2>&1 | head -1
# => [internal] load build context    transfer context: 2.56MB

# 使用 .dockerignore 减小上下文
echo "node_modules/" >> .dockerignore
echo ".git/" >> .dockerignore
echo ".env" >> .dockerignore
```

## 导出/导入镜像

```bash
# 导出（含所有层）
docker save myapp:v1 -o myapp-v1.tar
docker save myapp:v1 | gzip > myapp-v1.tar.gz

# 导入
docker load -i myapp-v1.tar
docker load < myapp-v1.tar.gz
```

## 常用构建模式

```bash
# CI 构建（拉取缓存 + 推送到仓库）
docker build \
  --pull \
  --cache-from ghcr.io/org/myapp:latest \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
  --build-arg VCS_REF=$(git rev-parse --short HEAD) \
  --label "org.opencontainers.image.created=$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
  --label "org.opencontainers.image.revision=$(git rev-parse --short HEAD)" \
  -t ghcr.io/org/myapp:$(git rev-parse --short HEAD) \
  -t ghcr.io/org/myapp:latest \
  .

# 无上下文构建（仅 Dockerfile）
docker build -t myapp - < Dockerfile
```
```

