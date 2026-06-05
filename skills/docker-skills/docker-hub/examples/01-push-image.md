# 镜像发布与标签策略

## 登录

```bash
docker login
docker login ghcr.io -u USERNAME -p $GITHUB_TOKEN
docker login registry.gitlab.com
```

## 标签策略

```bash
# 构建时打好所有标签
docker build -t myapp:v1.2.3 \
             -t myapp:v1.2 \
             -t myapp:v1 \
             -t myapp:latest \
             -t ghcr.io/myorg/myapp:v1.2.3 .

# 推送
docker push myapp:v1.2.3
docker push myapp:v1.2
docker push myapp:v1
docker push myapp:latest
docker push ghcr.io/myorg/myapp:v1.2.3
```

## 多标签推送

```bash
# 使用 --all-tags
docker push myapp --all-tags

# 或使用 docker buildx（含多平台）
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag myapp:v1.2.3 \
  --tag myapp:latest \
  --push .
```

## SHA256 Digest 固定

```bash
# 获取 digest
docker inspect --format='{{index .RepoDigests 0}}' myapp:latest
# myapp@sha256:abc123def456...

# 拉取固定版本（不随 tag 变化）
docker pull myapp@sha256:abc123def456...
```

## CI/CD 自动标签

```yaml
# GitHub Actions
- name: Docker metadata
  id: meta
  uses: docker/metadata-action@v5
  with:
    images: ghcr.io/${{ github.repository }}
    tags: |
      type=semver,pattern={{version}}
      type=semver,pattern={{major}}.{{minor}}
      type=sha,format=short
      type=raw,value=latest,enable=${{ github.ref == 'refs/heads/main' }}
```

输出示例：`v1.2.3`, `v1.2`, `abc1234`, `latest`（仅 main 分支）
```

