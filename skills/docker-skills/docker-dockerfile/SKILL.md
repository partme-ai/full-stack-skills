---
name: docker-dockerfile
description: Expert guidance for Dockerfile authoring — the complete reference for writing production-grade Dockerfiles. Covers every instruction (FROM/RUN/COPY/ADD/ENV/ARG/WORKDIR/EXPOSE/CMD/ENTRYPOINT/USER/HEALTHCHECK/SHELL) with syntax, best practices, and common mistakes. Includes multi-stage build patterns (build+scratch, build+alpine, builder pattern), layer caching optimization strategies, .dockerignore rules, and language-specific production templates (Go/Rust/Java Spring Boot/Python FastAPI/Node.js Express/TypeScript). Use when the user asks about Dockerfile, how to write a Dockerfile, multi-stage build, layer optimization, or needs Dockerfile examples for a specific language. 使用场景：Dockerfile 编写、怎么写 Dockerfile、Dockerfile 指令、多阶段构建、multi-stage、层优化、layer cache、Dockerfile 模板.
license: Apache-2.0
---

# Dockerfile — 完整编写指南

Expert reference for writing production-grade Dockerfiles. Every instruction, every pattern, every optimization.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "Dockerfile", "怎么写 Dockerfile", "Dockerfile 指令"
- "多阶段构建", "multi-stage build"
- "Dockerfile 层优化", "layer caching"
- "Dockerfile 模板", language-specific: "Go Dockerfile", "Java Dockerfile", "Python Dockerfile"
- Need to create or optimize a Dockerfile
- "Dockerfile best practices"

## Instruction Reference

### FROM — Base Image

```dockerfile
FROM <image>[:<tag>] [AS <stage-name>]
FROM alpine:3.20                           # Tag
FROM alpine:3.20@sha256:abc123...def456     # Digest (production!)
FROM golang:1.22-alpine AS builder          # Named stage
FROM scratch                                 # Empty image (for static binaries)
```

| Best Practice | Why |
|---------------|-----|
| Pin digest for production | Tags are mutable; digest is immutable |
| Use Alpine/slim variants | Smaller attack surface, smaller image |
| `FROM scratch` for Go/Rust | Static binaries need nothing else |

### RUN — Execute Commands

```dockerfile
# ✅ Chain commands, clean in same layer
RUN apk add --no-cache curl && \
    curl -fsSL https://example.com/script.sh -o /usr/local/bin/script && \
    chmod +x /usr/local/bin/script

# ❌ Each RUN = new layer (bloat)
RUN apk add curl
RUN curl ... -o /usr/local/bin/script
RUN chmod +x /usr/local/bin/script

# Multi-line readability
RUN set -eux; \
    apk add --no-cache \
      curl \
      ca-certificates \
      tzdata; \
    curl -fsSL ... | tar xz -C /usr/local
```

### COPY — Copy Files

```dockerfile
COPY [--chown=<user>:<group>] <src>... <dest>
COPY . /app
COPY --chown=app:app ./binary /usr/local/bin/
COPY --from=builder /app/build /app       # From another stage (multi-stage)
```

```dockerfile
# ✅ Layer-friendly: copy deps first, then source
COPY go.mod go.sum ./
RUN go mod download
COPY . .

# ❌ Source change invalidates dependency cache
COPY . .
RUN go mod download
```

### ADD — Copy + Auto-extract

```dockerfile
# ADD auto-extracts tar archives
ADD archive.tar.gz /app/

# Prefer COPY unless you need tar extraction
COPY archive.tar.gz /app/
RUN tar xzf /app/archive.tar.gz -C /app
```

### WORKDIR — Set Working Directory

```dockerfile
WORKDIR /app
# All subsequent RUN/COPY/CMD use /app as base

# Prefer over:
RUN cd /app && npm install   # ❌ cd doesn't persist
```

### ENV & ARG

```dockerfile
# ARG: build-time only (not in final image)
ARG VERSION=1.0.0
FROM myapp:${VERSION}

# ENV: runtime (persists in image)
ENV NODE_ENV=production \
    PORT=8080

# Combine: pass ARG to ENV
ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}
```

### EXPOSE — Document Ports

```dockerfile
EXPOSE 8080
EXPOSE 8080/tcp     # Protocol-specific
EXPOSE 8080/udp

# Note: EXPOSE does NOT publish ports. Use -p at runtime:
# docker run -p 8080:8080 myapp
```

### CMD vs ENTRYPOINT

```dockerfile
# CMD: default command (overridable)
CMD ["nginx", "-g", "daemon off;"]
# docker run myimage echo hello → overrides CMD

# ENTRYPOINT: fixed entry (not overridable)
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
# docker run myimage → runs: docker-entrypoint.sh nginx -g 'daemon off;'
# docker run myimage echo hello → runs: docker-entrypoint.sh echo hello

# Common pattern: script + default args
ENTRYPOINT ["/entrypoint.sh"]
CMD ["start"]
```

### USER — Switch to Non-Root

```dockerfile
# Create user and group
RUN addgroup --system app && adduser --system --ingroup app app
USER app
```

### HEALTHCHECK

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:8080/health || exit 1

# Dockerfile without shell (scratch):
HEALTHCHECK --interval=30s CMD /app/healthcheck || exit 1
```

### SHELL — Change Default Shell

```dockerfile
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]
RUN echo "Now using bash with strict mode"
```

## Multi-Stage Build Patterns

### Pattern 1: Build Binary + Scratch (Go/Rust)

```dockerfile
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o server .

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/server /server
USER 1000:1000
CMD ["/server"]
```

### Pattern 2: Build + Minimal Runtime (Java)

```dockerfile
FROM maven:3.9-eclipse-temurin-21 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:21-jre-alpine
RUN addgroup --system app && adduser -S -G app app
COPY --from=builder /app/target/*.jar /app.jar
USER app
CMD ["java", "-jar", "/app.jar"]
```

### Pattern 3: Layer-Optimized (Spring Boot)

```dockerfile
FROM eclipse-temurin:21-jre-alpine AS builder
WORKDIR /app
COPY build/libs/*.jar app.jar
RUN java -Djarmode=layertools -jar app.jar extract

FROM eclipse-temurin:21-jre-alpine
RUN addgroup --system app && adduser -S -G app app
# Layers in dependency order (max cache)
COPY --from=builder /app/dependencies/ ./
COPY --from=builder /app/spring-boot-loader/ ./
COPY --from=builder /app/snapshot-dependencies/ ./
COPY --from=builder /app/application/ ./
USER app
ENTRYPOINT ["java", "org.springframework.boot.loader.launch.JarLauncher"]
```

### Pattern 4: Build + Alpline (Node.js)

```dockerfile
FROM node:22-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-alpine
RUN addgroup --system app && adduser -S -G app app
COPY --from=builder /app/dist /app
COPY --from=builder /app/node_modules /app/node_modules
USER app
CMD ["node", "/app/index.js"]
```

### Pattern 5: Python Dependencies + Slim Runtime

```dockerfile
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.12-slim
RUN groupadd --system app && useradd --system -g app app
COPY --from=builder /root/.local /home/app/.local
COPY . /app
ENV PATH=/home/app/.local/bin:$PATH
USER app
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
```

## Layer Caching Strategy

```
Docker builds layers from top to bottom.
A changed layer invalidates ALL layers below it.

✅ CORRECT order:
  FROM base                  ← rarely changes
  RUN install-system-deps    ← changes with system updates
  COPY go.mod go.sum ./      ← changes with dependency changes
  RUN go mod download        ← changes with dependency changes
  COPY . .                   ← changes every commit ← MUST BE LAST

❌ WRONG order (slow builds):
  COPY . .                   ← changes every commit
  RUN go mod download        ← reruns every time!
```

## .dockerignore

```dockerfile
# .dockerignore
.git
.gitignore
*.md
.env
.env.*
Dockerfile
docker-compose*.yml
node_modules
__pycache__
*.pyc
.git
.idea
.vscode
*.log
tmp/
```

## Workflow — 推荐编写流程

Step 1: **确定语言和运行时**: Go/Java/Node.js/Python → 选择基础镜像
Step 2: **选择构建模式**: 单阶段/多阶段/Spring Boot 分层 → 从 templates 选模板
Step 3: **编写 Dockerfile**: 先 COPY 依赖 → RUN install → COPY 源码 → CMD
Step 4: **验证**: `docker build -t app .` + `docker run` + dive 分析镜像大小
Step 5: **生产加固**: USER 非 root、HEALTHCHECK、固定 digest、Security 检查

## Gotchas — Common Pitfalls

- **`COPY . .` before `RUN install`**: Every code change invalidates the dependency layer — rebuilds from scratch. → **Recovery**: Always copy deps first: `COPY package.json . → RUN install → COPY src/ .`.
- **Root user by default**: Always `USER <non-root>` at the end of Dockerfile. Escaping the container as root = host root. → **Recovery**: Add `RUN addgroup -S app && adduser -S app -G app` + `USER app`; verify with `docker exec myapp whoami`.
- **`ENV SECRET=value` in Dockerfile**: Baked into image layers forever. → **Recovery**: Use BuildKit `--mount=type=secret` or runtime injection `docker run -e SECRET=$VAL`.
- **No `.dockerignore`**: Sends entire project to build context — slow and leaks sensitive files. → **Recovery**: Create `.dockerignore` with at minimum `.git node_modules .env`; verify with `docker build --no-cache . 2>&1 | head -1`.
- **`RUN apt update && apt install` without cleanup**: Leaves package lists in layer. → **Recovery**: Chain with `&& rm -rf /var/lib/apt/lists/*`; for apk: `--no-cache` flag.
- **Heavy base image**: `ubuntu:22.04` (77 MB) vs `alpine:3.20` (7 MB). → **Recovery**: Prefer alpine; if glibc needed, use `debian:bookworm-slim`; check size with `docker images`.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 编写生产级 Dockerfile | 14 条指令完整参考 + 最佳实践 |
| ✅ 能做 | 多阶段构建（Go/Java/Node/Python） | 5 种语言专属模板 |
| ✅ 能做 | 层缓存优化 | COPY 依赖优先 + RUN 合并 + BuildKit cache mount |
| ✅ 能做 | 镜像瘦身 | 5 步法路线图：多阶段→Alpine→distroless→清理→dive |
| ⚠️ 需条件 | 私有依赖安装 | 需配合 BuildKit --secret 或 SSH forwarding |
| ⚠️ 需条件 | CMD vs ENTRYPOINT 选择 | 见指令参考中的决策树（工具用 ENTRYPOINT，服务用 CMD） |
| ❌ 超范围 | docker build 命令执行 | 使用 `docker-build` |
| ❌ 超范围 | 多平台构建（arm64/amd64） | 使用 `docker-buildx` |
| ❌ 超范围 | 容器编排（多容器） | 使用 `docker-compose` |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Building images (`docker build ...`) | `docker-build` |
| Multi-platform builds | `docker-buildx` |
| Compose file authoring | `docker-compose` |
| Docker basics | `docker-basics` |
| Running containers | `docker-run` |

## Security & Stability

- All Dockerfile templates are educational. Review and harden before production use.
- Never embed secrets in Dockerfile. Use BuildKit `--mount=type=secret` or runtime injection.
- Always `USER <non-root>` for production. Use `COPY --chown` when copying files for that user.
- Pin base image digests for production reproducibility.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Dockerfile 参考 | https://docs.docker.com/reference/dockerfile/ |
| Docker Build 概述 | https://docs.docker.com/build/ |
| 构建最佳实践 | https://docs.docker.com/build/building/best-practices/ |
| 多阶段构建 | https://docs.docker.com/build/building/multi-stage/ |
| .dockerignore | https://docs.docker.com/build/building/context/#dockerignore-files |
| 镜像层与缓存 | https://docs.docker.com/build/cache/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-dockerfile` — Dockerfile 编写**

```
basics → dockerfile → build → buildx → run → compose → ...
```

**→ Next**: `docker-build` — Build images with `docker build`
