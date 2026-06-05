---
name: ddd-testing-strategist
description: DDD testing strategy — domain model unit testing, aggregate root testing, repository testing with mocks, application service integration testing, adapter E2E testing, test pyramid for DDD layered/hexagonal/clean architectures, and Test-Driven Domain Design (TDDD). Use when user asks about testing strategy, 测试策略, DDD testing, aggregate test, repository test, test-driven domain design, or needs to test DDD applications.
license: Apache-2.0
---

# DDD Testing Strategist
DDD testing strategy — from value object unit tests to end-to-end validation across all DDD architectures. Covers the DDD test pyramid, layer-specific test patterns, mock strategies by architecture, Test-Driven Domain Design (TDDD), CI/CD pipeline integration, and N+1 query detection.

## Workflow
```
用户输入 → 场景分类 → 输出测试策略 + 代码模板

Step 1: 按用户问题场景分类（金字塔/AR/Repository/Mock/CQRS/TDDD/CI-CD/覆盖率）
Step 2: 从 references 获取对应测试模板
Step 3: 按架构类型调整 Mock 策略
Step 4: 输出代码模板 + CI/CD 配置 + 覆盖率目标
```
什么时候用：用户询问 DDD 测试策略、聚合根测试、Repository 测试、Mock 策略、CQRS 测试、TDDD、CI/CD 测试集成时触发。
## Boundary
### ✅ 擅长处理
1. DDD 测试金字塔（60% Domain + 20% Integration + 10% E2E + 10% Architecture）
2. 各层测试策略：Value Object / Aggregate Root / Domain Service / Repository / Application / Adapter
3. 按架构类型差异化测试（Layered / Hexagonal / Clean / COLA / CQRS / Event Sourcing）
4. 测试驱动领域设计（TDDD）方法论
5. Mock 策略选择（Mock Ports / Capture Events / Real DB）
6. CI/CD 三阶段流水线 + N+1 查询检测 + ArchUnit 架构测试
7. 测试覆盖率目标设定 + 分支覆盖率检查
### ⚠️ 需要条件
1. 已有 DDD 项目代码或正在设计领域模型
2. 已有测试框架（JUnit / Mockito / Spring Test / Testcontainers）
3. 理解 DDD 战术模式（Entity / VO / Aggregate / Repository / Domain Event）
### ❌ 超出范围（不适用场景）
1. 非 DDD 项目测试 — 标准测试框架（JUnit / pytest / Jest）
2. 纯前端测试 — Cypress / Playwright / Vitest
3. 性能 / 负载 / 安全测试 — JMeter / k6 / OWASP ZAP
4. 语言特定测试教程 — 概念和模式语言无关
5. 非 DDD 项目的 CI/CD 配置

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## Rules

1. DDD test pyramid must prioritize Domain layer testing (60% of total tests).
2. Domain layer tests must never mock Domain Services or Aggregate Roots — only mock external ports.
3. Repository integration tests must use Testcontainers with real databases, never mocks.
4. Event Sourcing projects must include event replay and projection tests.
5. Architecture compliance tests (ArchUnit) must run in CI pipeline.

## DDD 测试金字塔
DDD 金字塔与经典金字塔的关键区别：Domain 层（VO + AR + DS）占 **60%**，是测试核心。
```
         ╱           E2E Tests           ╲       ← 10%
        ╱──────── API Integration ────────╲       ← 10%
       ╱────── Repository Integration ──────╲     ← 10%
      ╱─────── Application Service ─────────╲    ← 10%
     ╱──────── Domain Service Tests ──────────╲   ← 15%
    ╱────────── Aggregate Root Tests ───────────╲  ← 25%
   ╱──────────── Value Object Tests ──────────────╲ ← 15%
```
## 各层测试策略
### ① Value Object 测试（纯函数）
```java
@Test void money_should_prevent_negative_amount() {
    assertThrows(IllegalArgumentException.class, () -> new Money(-1.0, "CNY")); }
@Test void money_add_should_sum_same_currency() {
    assertEquals(new Money(30.0, "CNY"), new Money(10.0, "CNY").add(new Money(20.0, "CNY"))); }
```
覆盖：构造验证、运算逻辑、等值比较、不变式。
### ② Aggregate Root 测试（核心业务逻辑）
```java
class OrderPayTest {
    @Test void pay_changes_status_to_paid_when_draft() { ... }
    @Test void pay_emits_orderPaidEvent() { ... }
    @Test void pay_fails_when_already_paid() { ... }
    @Test void pay_fails_when_cancelled() { ... } }
```
覆盖：每个状态转移独立测试类 → happy path + 边界条件 + 不变量 + 事件。
### ③ Domain Service 测试（Mock Repository，Capture Event）
```java
@Test void pricing_service_applies_vip_discount() {
    when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));
    pricingService.calculatePrice(order.getId());
    assertEquals(new Money(90.0, "CNY"), order.getTotalAmount()); }
```
Mock 原则：只 Mock Repository / Gateway（Interface），不 Mock Domain Service 或 Aggregate Root。
### ④ Application Service + ⑤ Repository + ⑥ Adapter 测试
```java
@Test void place_order_creates_and_saves() {
    var orderId = handler.handle(new PlaceOrderCommand("cust-123", ...));
    assertNotNull(orderId); }
@SpringBootTest @Testcontainers
class OrderRepositoryImplTest {
    @Test void persists_and_retrieves_complete_aggregate() { ... } }
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class OrderControllerTest {
    @Test void post_orders_returns_201() { ... }
    @Test void post_invalid_product_returns_400() { ... } }
```
App Service：Mock 所有外部端口。Repository：Testcontainers + 真实 DB。Adapter：MockMvc + 真实 DB。
## Mock 策略矩阵
| 测试目标 | Repository | Gateway | EventBus | External |
|---------|:--------:|:-------:|:-------:|:--------:|
| Value Object | N/A | N/A | N/A | N/A |
| Aggregate Root | N/A | N/A | Capture | N/A |
| Domain Service | Mock | Mock | Capture | Mock |
| Application Service | Mock | Mock | Mock | Mock |
| Repository Integration | Real DB | N/A | N/A | N/A |
| API Integration | Real DB | Mock | Mock | Mock |
| E2E | Real DB | Real | Real | Real |
原则：Domain 层不需要 Mock；只 Mock 接口（Port）不 Mock 实现类；领域事件用 Capture 模式。
## 各架构测试差异
| 架构 | 测试重心 | 差异说明 |
|------|---------|---------|
| **Layered** | Aggregate Root + Repository | Domain 层全量测试（60%+） |
| **Hexagonal** | Port Mock + Adapter Integration | Mock 接口即 Mock 整个外部 |
| **Clean** | Entity + UseCase Interactor | UseCase 层 Mock 输出端口 |
| **COLA** | Domain + App Service | Domain 零依赖；额外测 CQRS 分流 |
| **CQRS** | Command + Query Read Model | 写模型用聚合测试；读模型直接查视图 |
| **Event Sourcing** | Event Replay + Projection | 聚合重放测试（必测）；投影读模型测试 |
## Test-Driven Domain Design（TDDD）
四步工作流：RED → GREEN → REFACT → REPEAT
```java
@Test void tddd_order_should_not_allow_paying_twice() {
    Order order = Order.create(customerId, items);
    order.pay(mockGateway);
    assertThrows(OrderException.class, () -> order.pay(mockGateway)); }
public void pay(PaymentGateway gateway) {
    if (this.status == OrderStatus.PAID) throw new OrderException("Already paid");
    this.status = OrderStatus.PAID;
    addDomainEvent(new OrderPaidEvent(this.getId())); }
```
## 测试覆盖率目标
| 层 | 目标 | 关键覆盖点 |
|----|:---:|-----------|
| Value Object | ≥ 95% | 构造验证、运算逻辑、等值比较 |
| Aggregate Root | ≥ 95% | 状态转移（每个路径）、领域事件 |
| Domain Service | ≥ 90% | 跨实体编排、外部数据计算 |
| Application | ≥ 80% | Use Case 完整路径 + 异常路径 |
| Repository | ≥ 80% | 聚合完整性、N+1 查询 |
| Adapter (API) | ≥ 70% | 协议转换、错误映射 |
建议优先追踪**分支覆盖率**，Domain 层 ≥ 90%。
## Gotchas — 常见陷阱
1. **只测 App Service 不测 Domain** — DDD 核心是 Domain 层。
2. **Mock 了 Domain Service** — Domain Service 不应被 Mock。
3. **聚合根只测 Happy Path** — 必须覆盖不变式违反和边界条件。
4. **把 Repository 测试当作 E2E** — Repository 只验证持久化。
5. **忘记 Event Replay 测试** — 最隐蔽的 bug 来源。
6. **测试与实现耦合** — 测试行为而非内部细节。
7. **领域事件不测试** — 每个业务方法应验证事件发布。
8. **Mock DB 而不用 Testcontainers** — 始终用真实数据库。
9. **CQRS 不测 Query 端** — Command 和 Query 端策略完全不同。
10. **N+1 查询不检测** — CI 中集成 SQL 计数检测。
11. **E2E 测试太多** — 只保留 3-5 个关键旅程。
12. **忘记 ArchUnit** — 依赖方向合规应自动化检查。
## FAQ
| 问题 | 回答 |
|------|------|
| 聚合根测试需要 Spring 吗？ | 不需要。纯 POJO，直接用 JUnit + AssertJ。 |
| Repository 应 Mock 还是真实 DB？ | Domain Service 用 Mock；Repository 用真实 DB。 |
| CQRS 怎么测 Query 端？ | 直接访问读模型，不需要 Mock。 |
| Event Sourcing 的必要测试？ | Event Replay：给定事件序列 → 重放 → 验证状态。 |
| 怎么避免 N+1 查询？ | 集成 SQLStatementCountValidator。 |
| TDDD 和传统 TDD 的区别？ | TDDD 以"领域行为/状态转移"为单元。 |
## Keywords
DDD testing, test pyramid, aggregate root test, value object test, domain service test, repository test, application service test, adapter test, CQRS testing, Event Sourcing test, TDDD, mock strategy, Testcontainers, ArchUnit, N+1 test, domain event test, branch coverage, CI/CD testing, integration test, E2E test, event replay test
## References
| 文件 | 用途 |
|------|------|
| [references/testing.md](references/testing.md) | 测试金字塔 + 各层 TypeScript 示例 |
| [references/mock-integration-patterns.md](references/mock-integration-patterns.md) | Mock 实现 + Java 集成测试 |
| [references/clean-ddd-hexagonal-testing.md](references/clean-ddd-hexagonal-testing.md) | Clean/Hexagonal/DDD 多层测试 |
| [references/unit-testing-strategies.md](references/unit-testing-strategies.md) | VO/AR/DS 单元测试 + 状态转移 |
| [references/integration-test-strategies.md](references/integration-test-strategies.md) | Repository/API 集成测试 + N+1 |
| [references/cqrs-event-sourcing-testing.md](references/cqrs-event-sourcing-testing.md) | CQRS + ES 重放/投影/快照测试 |
| [references/test-coverage-targets.md](references/test-coverage-targets.md) | 覆盖率目标 + 分支覆盖率 + JaCoCo |
| [references/ci-cd-test-stages.md](references/ci-cd-test-stages.md) | CI/CD 三阶段 + GitHub Actions |
| [references/architecture-testing-comparison.md](references/architecture-testing-comparison.md) | 各架构测试差异 + 项目阶段策略 |
| [references/test-driven-domain-design.md](references/test-driven-domain-design.md) | TDDD 四步工作流 + 完整案例 |
## Examples
| 文件 | 用途 |
|------|------|
| [examples/domain-test-examples.md](examples/domain-test-examples.md) | VO + AR + DS 完整测试示例 |
| [examples/app-adapter-test-examples.md](examples/app-adapter-test-examples.md) | App Service + Adapter + E2E |
| [examples/cqrs-es-test-examples.md](examples/cqrs-es-test-examples.md) | CQRS + ES 重放/投影/快照测试 |
| [examples/builder-mock-patterns.md](examples/builder-mock-patterns.md) | Builder + Mock Repository/EventPublisher |
| [examples/architecture-test-examples.md](examples/architecture-test-examples.md) | ArchUnit 架构测试（分层/聚合隔离） |
## Security & Safety

This skill is pure documentation. It contains no executable scripts, collects no user data, accesses no external services or networks.

## DDD Skills Journey
> 📍 **You are here: `ddd-testing-strategist` — Step 6**
**← Previous**: [domain-designer](../ddd-domain-designer/)
**→ Next**: [devops-integration](../ddd-devops-integration/)
**🔗 Related**: [code-reviewer](../ddd-code-reviewer/) | [cqrs-architecture](../ddd-cqrs-architecture/)
**🏠 Home**: [awesome](../ddd-architecture-awesome/)
