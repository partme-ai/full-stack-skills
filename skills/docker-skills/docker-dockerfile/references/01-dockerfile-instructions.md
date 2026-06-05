# Dockerfile 指令完整速查

| 指令 | 用途 | 影响构建 | 影响运行时 |
|------|------|:--:|:--:|
| `FROM` | 基础镜像 | ✅ | ✅ |
| `RUN` | 执行命令 | ✅ | - |
| `COPY` | 复制文件 | ✅ | ✅ |
| `ADD` | 复制+解压+URL | ✅ | ✅ |
| `WORKDIR` | 工作目录 | ✅ | ✅ |
| `ENV` | 环境变量 | ✅ | ✅ |
| `ARG` | 构建参数 | ✅ | - |
| `EXPOSE` | 声明端口 | - | - |
| `CMD` | 默认命令 | - | ✅ |
| `ENTRYPOINT` | 入口点 | - | ✅ |
| `VOLUME` | 挂载点 | - | ✅ |
| `USER` | 切换用户 | - | ✅ |
| `HEALTHCHECK` | 健康检查 | - | ✅ |
| `SHELL` | 切换 Shell | ✅ | ✅ |

## FROM
```dockerfile
FROM image:tag
FROM image:tag AS stage-name
FROM image@sha256:abc123...
```
✅ 使用具体 tag 或 sha256 digest | ❌ `FROM node:latest`

## RUN
```dockerfile
RUN apt-get update && apt-get install -y pkg && rm -rf /var/lib/apt/lists/*
RUN --mount=type=cache,target=/root/.cache go build ...
```
✅ 用 `&&` 合并命令、安装后清理 | ❌ 每条 RUN 单独写

## COPY vs ADD
```dockerfile
COPY src dst              # 优先使用
COPY --chown=1000:1000 src dst
ADD archive.tar.gz /app/   # 仅解压时用 ADD
```
✅ 默认用 COPY | ❌ `ADD https://...`（应用 curl/wget）

## ENV vs ARG
```dockerfile
ARG NODE_VERSION=22       # 仅构建时
ENV NODE_ENV=production   # 构建+运行时
```
秘密/密钥 ❌ 都不要（用 `--secret`）

## CMD vs ENTRYPOINT
| 指令 | 可覆盖 | 用途 |
|------|:--:|------|
| CMD | ✅ | 默认参数 |
| ENTRYPOINT | ❌ | 固定入口 |

## USER
```dockerfile
RUN addgroup -S app && adduser -S app -G app
USER app:app
```

## HEALTHCHECK
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1
```
模式：HTTP `curl` | TCP `nc -z` | 进程 `pgrep` | 自定义脚本
```

