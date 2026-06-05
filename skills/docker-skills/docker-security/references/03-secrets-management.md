# Secrets 管理方案对比

## Docker Secrets（Swarm 模式）

```bash
# 创建 secret
echo "mysecretpassword" | docker secret create db_password -

# 服务中使用
docker service create \
  --secret db_password \
  --name db \
  mysql:8.4

# 容器内路径：/run/secrets/db_password
```

## BuildKit --secret（构建时）

```dockerfile
# syntax=docker/dockerfile:1

RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm install
```

```bash
docker buildx build --secret id=npmrc,src=$HOME/.npmrc -t myapp .
```

## 外部密钥管理器

| 方案 | 特点 | 复杂度 |
|------|------|:--:|
| **Vault** (HashiCorp) | 动态密钥、自动轮换、审计 | ⭐⭐⭐ |
| **AWS Secrets Manager** | 托管服务、自动轮换 | ⭐⭐ |
| **Azure Key Vault** | 托管、HSM | ⭐⭐ |
| **GCP Secret Manager** | 托管、IAM 集成 | ⭐⭐ |

### Vault + Docker

```bash
# 从 Vault 获取密钥后注入
export DB_PASSWORD=$(vault kv get -field=password secret/db)
docker run -e DB_PASSWORD myapp
```

## 方案对比

| 维度 | .env 文件 | Docker Secrets | BuildKit --secret | Vault |
|------|:--:|:--:|:--:|:--:|
| 加密存储 | ❌ | ✅（Raft 日志） | ❌（仅构建时） | ✅ |
| 自动轮换 | ❌ | ❌ | - | ✅ |
| 审计日志 | ❌ | ❌ | - | ✅ |
| 复杂度 | ⭐ | ⭐ | ⭐ | ⭐⭐⭐ |
| 适用场景 | 本地开发 | Swarm 生产 | CI/CD 构建 | 企业级 |
```

