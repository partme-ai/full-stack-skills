# Kubernetes Deployment Example — DDD Microservices with CQRS

## Namespace Setup

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ddd-orders
  labels:
    domain-bounded-context: orders
    domain-type: core
---
apiVersion: v1
kind: Namespace
metadata:
  name: ddd-payments
  labels:
    domain-bounded-context: payments
    domain-type: core
```

## Command Service (Write Model)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-command
  namespace: ddd-orders
spec:
  replicas: 2
  selector:
    matchLabels:
      app: order-command
  template:
    metadata:
      labels:
        app: order-command
        domain-layer: application
    spec:
      initContainers:
        - name: db-migration
          image: flyway/flyway:10-alpine
          command: ["flyway", "migrate"]
          env:
            - name: FLYWAY_URL
              value: "jdbc:postgresql://order-db:5432/orders"
            - name: FLYWAY_USER
              value: "postgres"
            - name: FLYWAY_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: order-db-credentials
                  key: password
          volumeMounts:
            - name: migrations
              mountPath: /flyway/sql
      containers:
        - name: command
          image: registry.example.com/order-command:1.0.0
          ports:
            - containerPort: 8080
              name: http
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: "k8s,command"
            - name: SPRING_DATASOURCE_URL
              value: "jdbc:postgresql://order-db:5432/orders"
            - name: EVENT_BROKER
              value: "kafka://kafka-cluster:9092"
          resources:
            requests:
              cpu: "500m"
              memory: "512Mi"
            limits:
              cpu: "2"
              memory: "2Gi"
          livenessProbe:
            httpGet:
              path: /actuator/health/liveness
              port: 8081
            initialDelaySeconds: 30
          readinessProbe:
            httpGet:
              path: /actuator/health/readiness
              port: 8081
            initialDelaySeconds: 20
      volumes:
        - name: migrations
          configMap:
            name: flyway-migrations
---
apiVersion: v1
kind: Service
metadata:
  name: order-command
  namespace: ddd-orders
spec:
  selector:
    app: order-command
  ports:
    - port: 8080
      targetPort: http
```

## Query Service (Read Model)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-query
  namespace: ddd-orders
spec:
  replicas: 3
  selector:
    matchLabels:
      app: order-query
  template:
    metadata:
      labels:
        app: order-query
        domain-layer: infrastructure
    spec:
      containers:
        - name: query
          image: registry.example.com/order-query:1.0.0
          ports:
            - containerPort: 8080
              name: http
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: "k8s,query"
            - name: READ_DB_HOST
              value: "order-read-db"
            - name: CACHE_TYPE
              value: "redis"
            - name: REDIS_HOST
              value: "redis-cluster"
          resources:
            requests:
              cpu: "300m"
              memory: "1Gi"
            limits:
              cpu: "1"
              memory: "4Gi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8081
---
apiVersion: v1
kind: Service
metadata:
  name: order-query
  namespace: ddd-orders
spec:
  selector:
    app: order-query
  ports:
    - port: 8080
      targetPort: http
```

## Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-command-hpa
  namespace: ddd-orders
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
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-query-hpa
  namespace: ddd-orders
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

## Network Policy — Bounded Context Isolation

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: bc-isolation
  namespace: ddd-orders
spec:
  podSelector:
    matchExpressions:
      - key: domain-layer
        operator: In
        values: [application, infrastructure]
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

## ConfigMap — Flyway Migration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flyway-migrations
  namespace: ddd-orders
data:
  V1__create_event_store.sql: |
    CREATE TABLE IF NOT EXISTS domain_event_store (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      aggregate_id VARCHAR(36) NOT NULL,
      event_type VARCHAR(200) NOT NULL,
      event_data JSONB NOT NULL,
      occurred_at TIMESTAMPTZ NOT NULL
    );
  V2__create_outbox.sql: |
    CREATE TABLE IF NOT EXISTS outbox (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      event_id VARCHAR(36) NOT NULL UNIQUE,
      payload JSONB NOT NULL,
      status VARCHAR(20) DEFAULT 'PENDING',
      created_at TIMESTAMPTZ DEFAULT NOW()
    );
```

## Deployment — Per-Bounded Context Database

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: order-db
  namespace: ddd-orders
spec:
  serviceName: order-db
  replicas: 1
  selector:
    matchLabels:
      app: order-db
  template:
    metadata:
      labels:
        app: order-db
    spec:
      containers:
        - name: postgres
          image: postgres:16-alpine
          env:
            - name: POSTGRES_DB
              value: orders
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: order-db-credentials
                  key: password
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql/data
          livenessProbe:
            exec:
              command: [pg_isready, -U, postgres]
            initialDelaySeconds: 30
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 10Gi
---
apiVersion: v1
kind: Service
metadata:
  name: order-db
  namespace: ddd-orders
spec:
  selector:
    app: order-db
  ports:
    - port: 5432
```
