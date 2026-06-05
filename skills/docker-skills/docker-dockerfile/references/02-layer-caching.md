# Docker 层缓存策略

## 核心原则：从变化最少到最频繁

```
FROM node:22-alpine          ← 层 0（缓存：除非改 tag）
COPY package.json ./          ← 层 1（缓存：文件 hash 不变）
RUN npm install               ← 层 2（缓存：层 1 hash 不变）
COPY src/ ./                  ← 层 3（代码变了 → 本层及以后重建）
RUN npm run build             ← 层 4（层 3 变了 → 重建）
```

## 按语言/生态的缓存顺序

**Node.js**: `COPY package.json pnpm-lock.yaml` → `RUN pnpm install` → `COPY .` → `RUN build`  
**Java/Maven**: `COPY pom.xml` → `RUN mvn dependency:go-offline` → `COPY src` → `RUN mvn package`  
**Go**: `COPY go.mod go.sum` → `RUN go mod download` → `COPY .` → `RUN go build`  
**Python**: `COPY requirements.txt` → `RUN pip install` → `COPY .`  
**Rust**: 使用 cargo-chef 预计算依赖 → 再编译

## BuildKit 缓存挂载

```dockerfile
RUN --mount=type=cache,target=/go/pkg/mod go mod download          # Go
RUN --mount=type=cache,target=/root/.m2 mvn dependency:go-offline  # Maven
RUN --mount=type=cache,target=/root/.cache/pip pip install -r ...  # pip
RUN --mount=type=cache,target=/root/.npm npm ci                    # npm
RUN --mount=type=cache,target=/usr/local/cargo/registry cargo build # Rust
```

## RUN 合并
```dockerfile
# ❌ 3 层
RUN apt-get update
RUN apt-get install -y pkg
RUN rm -rf /var/lib/apt/lists/*
# ✅ 1 层
RUN apt-get update && apt-get install -y pkg && rm -rf /var/lib/apt/lists/*
```
```

