# 镜像标签策略与生命周期

## 标签策略决策树

```
需要精确追溯？→ 是 → digest (@sha256:abc...) + git SHA tag
需要语义版本？→ 是 → semver (v1.2.3) + minor (v1.2) + major (v1)
需要自动部署？→ 是 → git SHA + latest（仅 stable 分支）
团队协作？    → docker/metadata-action 自动生成标签矩阵
```

## 推荐标签方案

```bash
# 每个 commit 打多标签
docker build \
  -t myapp:sha-$(git rev-parse --short HEAD) \
  -t myapp:v1.2.3 \
  -t myapp:v1.2 \
  -t myapp:v1 \
  -t myapp:latest \
  .

# 生产部署使用 digest
docker pull myapp@sha256:abc123def456...
```

## 不可变标签最佳实践

| 标签类型 | 可变 | 推荐场景 |
|----------|:--:|------|
| `:latest` | ✅ 可变 | 开发环境、Demo |
| `:v1.2.3` | ⚠️ 应不可变 | 发布版本 |
| `:sha-abc1234` | ✅ 不可变 | CI 构建 |
| `@sha256:abc...` | ✅ 不可变 | 生产部署 |
| `:dev` / `:prod` | ✅ 可变 | ⚠️ 不推荐 |

## docker/metadata-action 标签矩阵

```yaml
tags: |
  type=semver,pattern={{version}}
  type=semver,pattern={{major}}.{{minor}}
  type=sha,format=short
  type=ref,event=branch
  type=raw,value=latest,enable=${{ github.ref == 'refs/heads/main' }}
```

## 清理策略

```bash
# 保留最近 10 个 tag，删除其余
docker images myapp --format '{{.Tag}}' | sort -V | head -n -10 | xargs -I {} docker rmi myapp:{}

# 删除 30 天前的未使用镜像
docker image prune -a --filter "until=720h"

# 仅删除 dangling 镜像
docker image prune
```
```

