# Buildx Driver 选型

| 特性 | docker | docker-container | kubernetes | remote |
|------|:--:|:--:|:--:|:--:|
| 隔离级别 | 共享 dockerd | 独立容器 | K8s Pod | 远程 |
| 多平台 | ❌ | ✅ | ✅ | ✅ |
| 缓存挂载 | ❌ | ✅ | ✅ | ✅ |
| SSH 转发 | ❌ | ✅ | ✅ | ✅ |
| 并发构建 | ❌ | ✅ | ✅ | ✅ |
| 复杂度 | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

## 决策树
```
需要多平台？→ 否 → docker（零配置）
需要多平台？→ 是 → 在 K8s 中？→ 是 → kubernetes
                              → 否 → docker-container + QEMU
```

```bash
docker buildx create --name multiarch --driver docker-container --use
docker buildx create --name k8s-builder --driver kubernetes --driver-opt replicas=3
docker buildx create --name remote --driver remote tcp://buildkitd:1234
```
```

