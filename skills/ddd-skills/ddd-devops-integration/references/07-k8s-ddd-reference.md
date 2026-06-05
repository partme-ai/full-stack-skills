# Kubernetes Deployment Reference for DDD

## Deployment Template (Bounded Context Service)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  labels:
    app: order-service
    domain-bounded-context: orders
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
      maxSurge: 1
  selector:
    matchLabels:
      app: order-service
  template:
    metadata:
      labels:
        app: order-service
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/actuator/prometheus"
    spec:
      containers:
        - name: order-service
          image: registry.example.com/order-service:1.0.0
          ports:
            - containerPort: 8080
              name: http
            - containerPort: 8081
              name: management
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: "k8s"
            - name: SPRING_DATASOURCE_URL
              valueFrom:
                secretKeyRef:
                  name: order-db-secret
                  key: jdbc-url
          resources:
            requests:
              memory: "512Mi"
              cpu: "500m"
            limits:
              memory: "2Gi"
              cpu: "1"
          livenessProbe:
            httpGet:
              path: /actuator/health/liveness
              port: management
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /actuator/health/readiness
              port: management
            initialDelaySeconds: 20
            periodSeconds: 5
          startupProbe:
            httpGet:
              path: /actuator/health
              port: management
            initialDelaySeconds: 10
            periodSeconds: 5
            failureThreshold: 30
      terminationGracePeriodSeconds: 60
```

## Service Template

```yaml
apiVersion: v1
kind: Service
metadata:
  name: order-service
  labels:
    app: order-service
    domain-bounded-context: orders
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: http
      name: http
    - port: 8081
      targetPort: management
      name: management
  selector:
    app: order-service
```

## Per-Bounded Context Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: bc-orders
  labels:
    domain-bounded-context: orders
    domain-type: core
---
apiVersion: v1
kind: Namespace
metadata:
  name: bc-payments
  labels:
    domain-bounded-context: payments
    domain-type: core
---
apiVersion: v1
kind: Namespace
metadata:
  name: bc-notifications
  labels:
    domain-bounded-context: notifications
    domain-type: supporting
```

## Init Container for DB Migration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  template:
    spec:
      initContainers:
        - name: db-migration
          image: registry.example.com/order-flyway:1.0.0
          command: ["flyway", "migrate"]
          envFrom:
            - secretRef:
                name: order-db-secret
      containers:
        - name: order-service
          # ... main container config
```

## Horizontal Pod Autoscaler for CQRS

```yaml
# Command service HPA — scale on CPU (write-bound)
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-command-hpa
  namespace: bc-orders
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-command
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
---
# Query service HPA — scale on memory (read/cache-bound)
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-query-hpa
  namespace: bc-orders
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-query
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
```

## Network Policy (Inter-BC Isolation)

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: bc-orders-isolation
  namespace: bc-orders
spec:
  podSelector:
    matchLabels:
      app: order-service
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: api-gateway
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              domain-bounded-context: payments
      ports:
        - port: 8080
```
