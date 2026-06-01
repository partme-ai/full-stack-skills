# Docker Build Cloud

```
本地/CI → Build Cloud（云端 BuildKit 集群） → 推送到 Registry
              ↑
         共享缓存（团队复用）
```

## 接入
```bash
docker login
docker buildx create --name cloud-builder --driver cloud --use
docker buildx build --builder cloud-builder --platform linux/amd64,linux/arm64 --tag myorg/myapp:latest --push .
```

## GitHub Actions
```yaml
- uses: docker/setup-buildx-action@v3
  with:
    driver: cloud
    endpoint: myorg/cloud-builder
- uses: docker/build-push-action@v6
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: myorg/myapp:latest
```

| 指标 | 本地 | Build Cloud |
|------|:--:|:--:|
| 团队缓存共享 | ❌ | ✅ |
| 多平台速度 | 慢 (QEMU) | 快 (原生) |
| CI 资源消耗 | 高 | 低 |
```

