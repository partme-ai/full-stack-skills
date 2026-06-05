# Compose → Kubernetes 迁移指南

## Kompose 一键转换

```bash
# 安装
brew install kompose

# 转换
kompose convert -f compose.yml -o k8s/

# 输出文件列表
ls k8s/
# api-deployment.yaml
# api-service.yaml
# db-deployment.yaml
# db-service.yaml
# db-persistentvolumeclaim.yaml
# frontend-networkpolicy.yaml
# backend-networkpolicy.yaml
```

## 转换差异处理

| Compose | Kubernetes |
|---------|-----------|
| `depends_on` | Kompose 忽略（需 init container） |
| `deploy.replicas` | Deployment `spec.replicas` |
| `deploy.resources.limits` | 直接映射 |
| `restart: always` | Deployment 默认行为 |
| `ports` | Service + Deployment `containerPort` |
| `volumes` | PersistentVolumeClaim |
| `networks` | NetworkPolicy（需 Calico 等 CNI） |
| `environment` | `env` 字段 |
| `secrets` | Secret 对象 |
| `configs` | ConfigMap 对象 |

## 转换后手动调整

```yaml
# 添加 init container 替代 depends_on
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  template:
    spec:
      initContainers:
        - name: wait-for-db
          image: busybox:1.36
          command: ['sh', '-c', 'until nc -z db 5432; do sleep 2; done']
      containers:
        - name: api
          image: myapp:latest
```

## Helm Chart 包装

```bash
helm create myapp-chart
cp k8s/*.yaml myapp-chart/templates/
helm install myapp ./myapp-chart
```

## 常见陷阱

| 陷阱 | 说明 | 解决 |
|------|------|------|
| `depends_on` 丢失 | Kompose 不转换启动顺序 | 添加 init container |
| `network_mode: host` | K8s 中无 host 网络 | 使用 `hostNetwork: true`（慎用） |
| Volume 权限 | K8s PVC 权限模型不同 | 使用 `securityContext.fsGroup` |
| 环境变量 `$VAR` | Compose .env vs K8s 不同 | 改用 ConfigMap/Secret |
| `docker.sock` 挂载 | K8s 中不应挂载 socket | 使用 K8s API |
```

## 最终建议

小型项目用 Compose 足够；多节点/弹性扩容/服务网格用 K8s。过渡期可 Compose + K8s 并行运行。
```

