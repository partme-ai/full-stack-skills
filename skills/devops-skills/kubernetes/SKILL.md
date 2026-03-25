---
name: kubernetes
description: "Provides comprehensive guidance for Kubernetes including pods, services, deployments, ingress, ConfigMaps, and cluster management. Use when the user asks about Kubernetes, needs to deploy applications, configure resources, or troubleshoot cluster issues."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write Deployment, Service, ConfigMap, Secret, or Ingress manifests
- Deploy, scale, or troubleshoot pods and clusters with kubectl
- Design resource limits, health probes, rolling updates, and operational workflows
- Set up local development clusters with minikube, kind, or k3d

## How to use this skill

### Workflow

1. **Write manifests** — define workloads and services in YAML
2. **Apply to cluster** — use `kubectl apply -f` to deploy
3. **Verify status** — check rollout, pod health, and service endpoints
4. **Debug issues** — inspect logs, describe resources, exec into pods

### Quick Start Example

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: myapp:1.0.0
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 256Mi
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

```bash
# Apply manifests
kubectl apply -f deployment.yaml

# Check rollout status
kubectl rollout status deployment/myapp

# View pod logs
kubectl logs -l app=myapp --tail=50

# Exec into a pod for debugging
kubectl exec -it deployment/myapp -- /bin/sh
```

### Essential kubectl Commands

| Command | Purpose |
|---------|---------|
| `kubectl apply -f <file>` | Create or update resources |
| `kubectl get pods -w` | Watch pod status |
| `kubectl describe pod <name>` | Inspect pod details and events |
| `kubectl logs <pod> -f` | Stream container logs |
| `kubectl rollout undo deployment/<name>` | Roll back a deployment |
| `kubectl scale deployment/<name> --replicas=5` | Scale replicas |

## Best Practices

- Always set `requests` and `limits` for CPU and memory
- Configure `livenessProbe` and `readinessProbe` for every container
- Use Secrets for sensitive data and ConfigMaps for configuration
- Define rolling update strategy with `maxSurge` and `maxUnavailable`
- Collect logs and metrics centrally; use RBAC and NetworkPolicies in production

## Troubleshooting

- **CrashLoopBackOff**: Run `kubectl logs <pod> --previous` to see crash output; check resource limits and probe configuration
- **ImagePullBackOff**: Verify image name/tag exists and imagePullSecrets are configured
- **Pending pods**: Run `kubectl describe pod <name>` — look for insufficient resources or unschedulable nodes
- **Service not reachable**: Verify selector labels match pod labels; check endpoints with `kubectl get endpoints <svc>`

## Keywords

kubernetes, k8s, kubectl, deployment, pod, service, ingress, configmap, secret, container orchestration
