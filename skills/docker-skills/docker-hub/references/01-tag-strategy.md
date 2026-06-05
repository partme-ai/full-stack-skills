# 镜像标签策略

## 常见标签策略对比

| 策略 | 示例 | 可变 | 可追溯 | 推荐度 |
|------|------|:--:|:--:|:--:|
| `latest` | `myapp:latest` | ✅ | ❌ | ⭐ |
| SemVer | `myapp:v1.2.3` | ❌ | ✅ | ⭐⭐⭐ |
| Git SHA | `myapp:abc1234` | ❌ | ✅ | ⭐⭐⭐ |
| Git SHA + SemVer | `myapp:v1.2.3-abc1234` | ❌ | ✅✅ | ⭐⭐⭐⭐⭐ |
| SHA256 Digest | `myapp@sha256:abc...` | ❌ | ✅✅ | ⭐⭐⭐⭐ |
| 日期 | `myapp:2024-06-15` | ❌ | ⭐ | ⭐⭐ |
| 环境 | `myapp:dev` / `myapp:prod` | ✅ | ❌ | ⭐ |

## 推荐标签方案

```bash
# 每个 build 打 3 类标签
docker build \
  -t myapp:v1.2.3 \                          # SemVer
  -t myapp:v1.2 \                             # Minor 浮动
  -t myapp:v1 \                               # Major 浮动
  -t myapp:sha-$(git rev-parse --short HEAD) \ # Git SHA
  -t ghcr.io/org/myapp:v1.2.3 .
```

## 不可变标签最佳实践

```bash
# ❌ 不要：latest 随意覆盖
docker build -t myapp:latest .
docker push myapp:latest    # 不知道具体是哪个版本

# ✅ 正确：latest 始终指向最新稳定版
docker build -t myapp:v1.2.3 -t myapp:latest .
docker push myapp:v1.2.3
# latest 仅在稳定版 release 时更新

# ✅ 生产环境使用 digest
docker pull myapp@sha256:abc123def456...
```

## Docker metadata-action 标签模板

```yaml
tags: |
  type=semver,pattern={{version}}
  type=semver,pattern={{major}}.{{minor}}
  type=sha,format=short
  type=ref,event=branch
  type=raw,value=latest,enable=${{ github.ref == 'refs/heads/main' }}
```

## 标签清理

```bash
# Docker Hub API 删除 tag
curl -X DELETE -u "$DOCKER_USER:$DOCKER_TOKEN" \
  "https://hub.docker.com/v2/repositories/$DOCKER_USER/myapp/tags/v0.1.0/"
```
```

