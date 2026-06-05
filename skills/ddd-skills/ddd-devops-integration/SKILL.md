---
name: ddd-devops-integration
description: DDD DevOps integration — CI/CD pipeline with ArchUnit automated architecture validation, multi-module build optimization for DDD projects, containerized deployment with Docker/K8s for layered/hexagonal/clean architectures, database migration strategies for domain events, and monitoring domain health. Use when user asks about DevOps, CI/CD, DDD deployment, ArchUnit CI, or needs to automate DDD project builds.
license: Apache-2.0
---

# DDD DevOps Integration

DevOps for DDD projects — ArchUnit quality gates (P0 block / P1 warn / P2 report) in CI/CD, multi-module incremental builds, architecture-type-aware Dockerfiles, event-driven DB migration, domain event health monitoring.

---

## Workflow

### Step 1: Code & Build — Compile all modules. Domain must compile last (zero framework contamination).
### Step 2: Unit Test — Per-module unit tests run independently.
### Step 3: ArchUnit Validate — P0 (zero deps, layer compliance) blocks CI; P1 (cycle-free) warns; P2 (naming) reports.
### Step 4: Integration Test — Cross-module interaction tests with event store and outbox.
### Step 5: Containerize — Build Docker images (monolith fat JAR or split CQRS with tuned JVM args).
### Step 6: Deploy — K8s deploy with per-BC namespace, DB migration init containers, health probes.
### Step 7: Monitor — Domain metrics (event rate, outbox depth, aggregate load) → Prometheus alerts.

Quality gates run at build time, never against production. Violations block merge, not deployment.

---

## Boundary

### ✅ 擅长处理
- 为 DDD 项目配置 ArchUnit 质量门禁（P0/P1/P2），集成到 CI/CD Pipeline
- 多模块 DDD 项目增量编译优化（Maven/Gradle）、并行构建加速
- 架构类型感知的 Dockerfile 生成（单体/CQRS/六边形架构）
- K8s 部署模板：Per-BC Namespace、DB 迁移 initContainers、领域健康探针
- 事件驱动数据库迁移：Event Store、Outbox 表创建与索引策略
- 领域事件健康监控：Prometheus 指标暴露与告警规则配置

### ⚠️ 需要素材
- **项目结构**：Maven/Gradle 模块列表、依赖关系图 → 自动生成 ArchUnit 规则
- **部署环境**：K8s 集群版本、Ingress 策略 → 生成适配的 YAML 模板
- **数据库方案**：采用 Layered/CQRS/Event Sourcing 何种模式 → 定制迁移策略

### ❌ 超出范围（不适用）
- 通用 CI/CD 配置（非 DDD 项目不适用）→ 使用通用 DevOps 工具
- 容器编排基础（K8s 入门教程）→ 参考官方文档
- K8s 集群运维（节点管理、RBAC 配置）→ 使用专业运维工具
- 通用数据库管理（备份、恢复、性能调优）→ 使用 DBA 工具
- 基础设施监控（CPU、内存、网络）→ 使用 Prometheus + Grafana

---

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## Rules

1. ArchUnit P0 checks (domain purity, layer compliance) must block CI pipeline on failure.
2. Dockerfiles must be architecture-type-aware (Monolith/CQRS/Hexagonal each get different builds).
3. Domain event monitoring must be configured before production deployment.
4. Database migrations for event-driven systems must include event store and outbox tables.

---

## CI/CD Pipeline

```yaml
stages:
  - build
  - unit-test
  - architecture-check    # DDD gate
  - integration-test
  - containerize
  - deploy
```
ArchUnit validation in `architecture-check` stage: P0 tests (`DomainPurityTest`, `LayeringComplianceTest`) block on failure; P1 (`ModuleDependencyTest`) warns with approval; P2 (`NamingConventionTest`) reports only. Key ArchUnit rules — domain must not depend on Spring/JPA/MyBatis; layer access restrictions (Domain only by Application, Infrastructure, Interface); no cyclic package dependencies. Full guide: [references/ci-cd-archunit-setup.md](references/ci-cd-archunit-setup.md)

---

## 多模块构建策略

```
ddd-project/
├── domain/ (zero framework deps) → application/ (depends on domain only) → infrastructure/ (implements domain interfaces)
├── adapter/ (REST/event adapters) → start/ (boot entry)
```
Build optimization: `mvn compile -pl domain -am` (~60% faster changed-only), `mvn -T 4` (~40% parallel), `mvn verify -pl '!domain'` (skip domain), `actions/cache` for `target/` (~80%). Domain purity enforced via Maven Enforcer (bans Spring deps in domain module). Full config: [references/multi-module-build-config.md](references/multi-module-build-config.md)

---

## 容器化部署

**Monolith** — Multi-stage fat JAR:
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS builder
COPY . . && RUN mvn clean package -DskipTests
FROM eclipse-temurin:17-jre-alpine
COPY --from=builder start/target/*.jar app.jar
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8080/actuator/health
```
**CQRS** — Separate images: Command (`-Xms512m -Xmx2g -XX:+UseZGC`, CPU-optimized); Query (`-Xms1g -Xmx4g`, memory-optimized). **K8s Patterns**: Per-BC `Namespace`, DB migration `initContainers` + Flyway, CQRS split `HorizontalPodAutoscaler`, `NetworkPolicy` isolation. Templates: [dockerfile-patterns.md](references/dockerfile-patterns.md) | [k8s-ddd-reference.md](references/k8s-ddd-reference.md)

---

## 数据库迁移（事件驱动）

```sql
CREATE TABLE domain_event_store (id UUID PRIMARY KEY, aggregate_id VARCHAR(36) NOT NULL,
    event_type VARCHAR(200) NOT NULL, event_data JSONB NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL, published BOOLEAN DEFAULT FALSE);
CREATE INDEX idx_events_pending ON domain_event_store(published) WHERE published = FALSE;
CREATE TABLE outbox_message (id UUID PRIMARY KEY, event_id UUID UNIQUE NOT NULL,
    payload JSONB NOT NULL, status VARCHAR(20) DEFAULT 'PENDING',
    retry_count INT DEFAULT 0, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE INDEX idx_outbox_pending ON outbox_message(status) WHERE status = 'PENDING';
```
Strategy: Layered single DB → Flyway/Liquibase sequential; CQRS L2 → Dual tracks + lag; Event Sourcing → Axon/EventStoreDB append-only; Per microservice → Per-BC Flyway. Full scripts: [flyway-migration.md](references/flyway-domain-event-migration.md) | [db-strategies.md](references/database-migration-strategies.md)

---

## 监控与告警

Bus metrics: `domain.events.published` (Counter), `domain.events.processing.duration` (Histogram p50/p95/p99), `domain.aggregate.load.duration` (Histogram), `domain.outbox.depth` (Gauge).

Alert rules: DomainEventBacklog (rate > 100 for 2m, critical), OutboxQueueGrowing (depth > 1000 for 1m, critical), EventProcessingErrorRate (> 5% for 2m, warning). Full config: [ddd-observability-config.md](references/ddd-observability-config.md)

---

## Gotchas

1. **ArchUnit 过严导致开发受阻**: 先用 warning 模式运行 2-3 个 sprint，P1/P2 不阻断 CI，团队适应后升级为 error。
2. **CQRS 读写容器未分离**: 命令服务 CPU 密集，查询服务内存密集，应独立构建部署。
3. **领域事件监控遗漏**: Event 投递延迟、Outbox 堆积、Consumer Lag 是事件驱动架构中最易忽略的可靠性指标。
4. **单体打成微服务镜像**: 先评估 BC 是否需要独立部署，过度拆分失去聚合内强一致性优势。
5. **数据库迁移未考虑事件存储**: 添加 Event Store 表时需同步考虑回填、索引、清理策略。
6. **ArchUnit 不检查充血模型**: 需结合 ddd-code-reviewer 做领域模型质量审查。

---

## FAQ

**Q: ArchUnit CI 失败但代码正确？** A: 检查 Domain 层是否有框架注解污染（如 `@Service`），移到基础设施层。
**Q: Monolith vs 微服务 DDD 部署策略？** A: 从单体开始。仅当 BC 需独立扩缩容、单 BC 团队 > 8 人、BC 间部署节奏差异大时再拆分。
**Q: 如何监控领域事件而不增加延迟？** A: 异步指标（Micrometer Timer 百分比采样）+ 采样追踪（1/100 OpenTelemetry）。绝不阻塞事件发布。
**Q: CQRS 读写应共享同一 pipeline？** A: 只共享 Domain 模块测试。Command pipeline 跑完整 ArchUnit 门禁；Query pipeline 聚焦读模型 schema 兼容性。
**Q: Event Sourcing schema 如何管理？** A: Event Store append-only，不需 schema 迁移。版本兼容性通过事件版本号（event_type + version）管理。
**Q: Bounded Context 金丝雀发布如何实现？** A: Service Mesh（Istio）流量权重分配。新版本先接 5% 流量，监控 domain event 健康指标后全量。

---

## Security & Safety

This skill is pure documentation. It does not collect user data, does not access external services or networks, and contains no executable scripts.

## Keywords

ddd devops, ddd ci/cd, archunit ci, domain event monitoring, ddd docker, ddd kubernetes, ddd outbox, ddd database migration, ddd build optimization, ddd quality gate, ddd deployment, ddd alerting, ddd observability, cqrs deployment, event sourcing infrastructure

## References

- [CI/CD ArchUnit Setup](references/ci-cd-archunit-setup.md) — ArchUnit CI/CD integration guide
- [Dockerfile Patterns](references/dockerfile-patterns.md) — Dockerfiles by DDD architecture type
- [K8s DDD Reference](references/k8s-ddd-reference.md) — K8s deployment for bounded contexts
- [Flyway Domain Event Migration](references/flyway-domain-event-migration.md) — Event store and outbox scripts
- [Monitoring & Alerting](references/monitoring-alerting-reference.md) — Prometheus metrics and alerting rules
- [Multi-Module Build Config](references/multi-module-build-config.md) — Maven/Gradle build optimization
- [DDD Observability Config](references/ddd-observability-config.md) — Micrometer/OTel/Logback configuration
- [GitLab CI Pipeline Reference](references/gitlab-ci-ddd-pipeline-reference.md) — GitLab CI complete pipeline
- [Database Migration Strategies](references/database-migration-strategies.md) — Event-driven migration strategies

## Examples

- [GitHub Actions Pipeline](examples/github-actions-pipeline.md) — Complete GitHub Actions workflow with ArchUnit
- [GitLab CI ArchUnit Pipeline](examples/gitlab-ci-archunit-pipeline.md) — GitLab CI with architecture validation
- [K8s DDD Deployment](examples/k8s-ddd-deployment.yaml) — K8s manifests for bounded context deployment
- [Flyway Domain Event Migration](examples/flyway-domain-event-migration.sql) — Complete migration SQL scripts
- [Grafana Domain Health Dashboard](examples/grafana-domain-health-dashboard.md) — Domain event monitoring dashboard
