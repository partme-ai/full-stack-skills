# Docker Build Cloud CI 集成

## 概述

将构建卸载到云端 BuildKit 集群，CI Runner 仅发送构建上下文。

## 前置步骤

```bash
# 登录 Docker（需付费订阅）
docker login

# 创建 Cloud Builder
docker buildx create \
  --name cloud-builder \
  --driver cloud \
  --use

# 验证
docker buildx ls
```

## GitHub Actions 集成

```yaml
- name: Set up Docker Buildx with Cloud
  uses: docker/setup-buildx-action@v3
  with:
    driver: cloud
    endpoint: myorg/cloud-builder     # Build Cloud endpoint

- name: Build and push
  uses: docker/build-push-action@v6
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: myorg/myapp:latest
    cache-from: type=registry,ref=myorg/myapp:buildcache
    cache-to: type=registry,ref=myorg/myapp:buildcache,mode=max
```

## Jenkins Pipeline

```groovy
pipeline {
    agent any
    environment {
        DOCKER_BUILDKIT = '1'
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                    docker buildx build \
                        --builder cloud-builder \
                        --platform linux/amd64,linux/arm64 \
                        --tag myorg/myapp:${BUILD_NUMBER} \
                        --push .
                '''
            }
        }
    }
}
```

## 共享缓存

团队内所有成员共享 Build Cloud 缓存，无需额外配置：

```
开发者 A 构建 → 缓存写入 Cloud
开发者 B 构建 → 命中 A 的缓存（层 hash 匹配）
CI 构建 → 命中团队缓存
```

## 与本地构建对比

| 指标 | 本地 | Build Cloud |
|------|:--:|:--:|
| 首次构建 (多平台) | ~12 min | ~6 min |
| 二次构建（缓存命中） | ~2 min | ~1 min |
| CI Runner 规格 | 高性能（4c8g+） | 低配（2c4g 即可） |
| 团队缓存共享 | ❌ | ✅ |
```

