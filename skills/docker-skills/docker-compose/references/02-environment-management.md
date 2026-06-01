# Compose 环境变量管理策略

## 三种方式对比

| 方式 | 作用范围 | 优先级 | 典型场景 |
|------|:--:|:--:|------|
| `.env` 文件 | `$VAR` 变量替换 | 自动加载 | 敏感值、环境差异 |
| `env_file` | 容器内环境变量 | 低 | 大量共享变量 |
| `environment` | 容器内环境变量 | 高 | 少量、明确的值 |

## .env 文件（变量替换）

`.env` 放在 `compose.yml` 同目录，自动加载用于 `${VAR}` 替换，**不直接注入容器**。

```bash
# .env
POSTGRES_VERSION=16
DB_USER=myapp
DB_PASSWORD=secret123
```

```yaml
services:
  db:
    image: postgres:${POSTGRES_VERSION:-16}    # 替换为 16
    environment:
      POSTGRES_USER: ${DB_USER}                 # 替换为 myapp
      POSTGRES_PASSWORD: ${DB_PASSWORD}
```

| 语法 | 含义 |
|------|------|
| `${VAR}` | 必需，无值则报错 |
| `${VAR:-default}` | 有默认值 |
| `${VAR:?error}` | 必需，无值则显示错误 |
| `${VAR:+alt}` | 如果 VAR 有值则用 alt |

## env_file（注入容器）

```yaml
services:
  app:
    env_file:
      - .env.common
      - .env.api
```

```bash
# .env.common
TZ=Asia/Shanghai
LOG_LEVEL=info

# .env.api
API_PORT=8080
RATE_LIMIT=100
```

⚠️ `env_file` 不用于 `$VAR` 替换，如需替换请用 `.env` 或 cli `--env-file`。

## environment（直接声明）

```yaml
services:
  app:
    environment:
      NODE_ENV: production
      PORT: "8080"
      DATABASE_URL: postgres://user:pass@db:5432/mydb
```

## 多环境 override 策略

```yaml
# compose.yml（基础配置）
services:
  app:
    image: myapp:latest
    ports:
      - "8080:8080"
    environment:
      LOG_LEVEL: info

# compose.override.yml（本地开发，默认自动合并）
services:
  app:
    build: .
    ports:
      - "8080:8080"
      - "9229:9229"           # debug port
    environment:
      NODE_ENV: development
      LOG_LEVEL: debug

# compose.prod.yml（生产环境，-f 显式指定）
services:
  app:
    ports:
      - "80:8080"
    environment:
      NODE_ENV: production
    deploy:
      resources:
        limits:
          memory: 512M
    restart: always
```

```bash
# 开发（自动合并 compose.yml + compose.override.yml）
docker compose up -d

# 生产（合并 compose.yml + compose.prod.yml）
docker compose -f compose.yml -f compose.prod.yml up -d
```

## 优先级总结

```
命令行 -e VAR=val          ← 最高
    ↓
compose.yml environment   ← 中
    ↓
env_file 文件值            ← 低
    ↓
.env 文件默认值 ${VAR:-x}  ← 最低
```

## 最佳实践

| 场景 | 建议 |
|------|------|
| 密码/密钥 | `.env` 文件（不提交 Git） + Docker secrets（Swarm） |
| 环境差异 | override 文件：`compose.dev.yml` / `compose.prod.yml` |
| 共享配置 | `env_file: .env.common` |
| CI/CD | `echo "$SECRET" > .env && docker compose up` |
```

