# Docker Buildx 架构

```
docker CLI (docker buildx build)
    ↓ gRPC
Buildx Client
    ↓
Builder Instance
    ├── Node 1 (amd64)
    ├── Node 2 (arm64)
    └── Node N (...)
    Driver: docker / docker-container / kubernetes / remote
```

| 概念 | 说明 |
|------|------|
| Builder | 构建环境实例（可跨节点） |
| Node | 实际执行构建的节点 |
| Driver | 后端驱动，决定隔离级别和功能 |

```bash
docker buildx create --name mybuilder --driver docker-container
docker buildx ls
docker buildx use mybuilder
docker buildx inspect --bootstrap
docker buildx rm mybuilder
```
```

