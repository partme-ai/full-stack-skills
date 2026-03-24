---
name: kubernetes
description: Provides comprehensive guidance for Kubernetes including pods, services, deployments, ingress, and cluster management. Use when the user asks about Kubernetes, needs to deploy applications to Kubernetes, configure Kubernetes resources, or manage Kubernetes clusters.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写或应用 Deployment、Service、ConfigMap、Secret、Ingress 等资源
- 使用 kubectl 部署、扩缩容、排查 Pod 与集群
- 设计资源限制、探针、滚动更新与运维流程

## How to use this skill

1. **资源**：YAML 定义 workload（Deployment/StatefulSet）、Service、ConfigMap/Secret；Ingress 做 HTTP 路由。
2. **kubectl**：`apply -f`、`get/describe/logs/exec`、`scale`、`rollout status`；context 与 namespace 切换。
3. **环境**：集群需 kubeconfig；本地可用 minikube/kind/k3d；生产注意 RBAC 与网络策略。

## Best Practices

- 设置 requests/limits；配置 liveness/readiness 探针。
- 敏感信息用 Secret；配置用 ConfigMap 或外部配置中心。
- 滚动更新与回滚策略明确；日志与监控集中收集。

## Keywords

kubernetes, k8s, kubectl, deployment, pod, service, 容器编排, 部署
