## DDD、六边形架构、整洁架构、菱形（cola）架构的深度解析

原文：https://blog.csdn.net/dividividiv/article/details/151934659

### 文章目录

执行摘要（Executive Summary）
1. DDD 基础（战略 + 战术）
   1.1 战略设计（做正确的事）
   1.2 战术设计（把事做正确）
2. 六边形架构（Ports & Adapters）
   2.1 结构与角色
   2.2 优点
   2.3 代价与误用
   2.4 与 DDD 对齐的最小落地模板（Java）
3. 整洁架构（Clean Architecture）
   3.1 圈层对照 DDD
   3.2 优点
   3.3 常见陷阱
   3.4 最小实践清单
4. 菱形架构（COLA）
   4.1 结构
   4.2 工程约定（常见包结构）
   4.3 优点
   4.4 注意点
5. 三种架构对比
6. 关键设计议题（与 DDD 的融合）
   6.1 事务与一致性
   6.2 幂等与重试
   6.3 模型完整性（不变式）
   6.4 DTO/VO/DO 的边界
7. 目录与包结构建议（Java 示例）
8. PlantUML 模板
   8.1 时序图（支付用例）
   8.2 组件图（六边形）
9. 迁移路径（从 MVC/贫血到 DDD/充血）
10. 反模式与气味
11. 选型建议（Checklist）
12. 附：示例代码片段（充血聚合）
    结语

### 执行摘要（Executive Summary）

- **DDD（领域驱动设计）强调用“领域模型”承载业务知识，通过限界上下文划分边界；战术上用实体、值对象、聚合、领域服务、仓储、工厂、领域事件组织代码。**
- **六边形架构（Ports & Adapters）把系统核心与外界交互隔离，所有 IO 通过端口（Port）与适配器（Adapter）**进出，核心可独立于框架、UI、DB 运行与测试。
- **整洁架构（Clean Architecture）强调依赖方向只指向内圈（实体→用例→接口适配器→框架与驱动）**，与“洋葱/六边形”同宗同源，关注可演进、可测试。
- **菱形架构（COLA）是国内工程化落地的 DDD 分层风格（形似菱形）**，用Adapter / Application / Domain / Infrastructure 四层 + Command/DTO/Assembler/SPI 扩展点等工程实践，兼顾协作与落地效率。

> ##### 如何选型：
- **纯 CRUD/报表/管理后台**：传统分层或轻量 DDD 即可。
- **核心域/复杂规则/多集成**：六边形或整洁优先；若团队熟悉阿里系/工程化落地，**COLA（菱形）**更好落地。
- **强变化的外设（UI/DB/队列/三方）**：六边形最“抗变化”。

### 1. DDD 基础（战略 + 战术）

#### 1.1 战略设计（做正确的事）

- **限界上下文（Bounded Context）**：业务语言与模型的边界，一个上下文内统一语言，跨上下文用**上下文映射（Context Map）**明确关系（ACL/Conformist/Anti-Corruption 等）。
- **子域**：核心域 / 支撑域 / 通用域，不同优先级、不同投入。
- **统一语言**：与业务共创词典，模型与词语一一对应。

#### 1.2 战术设计（把事做正确）

- **实体（Entity）**：有标识、可变更（例如 PayOrder）。
- **值对象（VO）**：无标识、不可变（例如 Money、Email）。
- **聚合（Aggregate）**：一致性边界；聚合根负责约束不变式（状态机、额度、时间窗等）。
- **领域服务（Domain Service）**：无法归属实体/值对象的领域行为（保持领域纯度，不要堆技术细节）。
- **仓储（Repository）**：持久化抽象，只暴露按聚合的取/存接口。
- **工厂（Factory）**：复杂构造的封装。
- **领域事件（Domain Event）**：领域内重要事实改变时发布（解耦后续反应）。

### 2. 六边形架构（Ports & Adapters）

> 别名：端口与适配器。核心思想：核心不依赖外部世界，一切 IO 通过端口；入站适配器把“外部请求→端口调用”，出站适配器把“端口调用→外部资源”。

#### 2.1 结构与角色

```
          [ 入站适配器 ]  HTTP/CLI/GRPC
                │
             (入站端口)
                │        ┌─────────────┐
            ┌───────┐    │ 领域模型/聚合│   ┌─────────────┐
            │应用服务│───>│ 领域服务/事件│<──│仓储接口(端口)│
            └───────┘    └─────────────┘   └─────────────┘
                │                                 │
             (出站端口)                        [ 出站适配器 ]  DB/MQ/第三方

```

- **入站端口**：应用用例接口（Use Case Interface），例如 `PayUseCase`。
- **入站适配器**：Controller/CLI/Job，把协议转成端口调用。
- **出站端口**：对外依赖抽象，例如 `PaymentGateway`、`OrderRepository`。
- **出站适配器**：技术实现（MyBatis/JPA、HTTP SDK、Kafka 等）。

#### 2.2 优点

- **高可测试**：核心可用内存替身（Fake Adapter）跑完整用例。
- **抗框架/抗外设变化**：换 DB/UI/MQ 仅替换适配器。
- **天然契合 DDD**：端口即策略边界，聚合不被技术污染。

#### 2.3 代价与误用

- 端口过多/粒度不当会过度抽象。
- DTO/Assembler 映射成本；新手容易把业务塞到适配器里。

### 2.4 与 DDD 对齐的最小落地模板（Java）

```java
// 入站端口（用例接口）
public interface PayUseCase { PayResult pay(PayCommand cmd); }

// 应用服务（实现入站端口，编排事务）
@Service
class PayApplicationService implements PayUseCase {
  private final OrderRepository orderRepo; // 出站端口
  private final PaymentGateway payment;    // 出站端口
  @Transactional
  public PayResult pay(PayCommand cmd) {
    PayOrder order = orderRepo.byId(cmd.orderId());
    order.ensurePayable();                 // 领域不变式
    PaymentRes res = payment.charge(cmd.orderId(), order.amount());
    order.applyPaid(res.tradeNo(), res.paidAt());   // 聚合修改 + 事件
    orderRepo.save(order);
    return PayResult.success(res.tradeNo());
  }
}

// 出站端口
public interface OrderRepository { PayOrder byId(String id); void save(PayOrder o); }
public interface PaymentGateway { PaymentRes charge(String orderId, Money amount); }

// 出站适配器（例如基于 MyBatis）
@Repository
class MyBatisOrderRepository implements OrderRepository { /* mapper 调用 */ }

```

### 3. 整洁架构（Clean Architecture）

> 圈层模型：实体（Entities）→ 用例（Use Cases）→ 接口适配器（Interface Adapters）→ 框架与驱动（Frameworks & Drivers）。依赖只能向内。

#### 3.1 圈层对照 DDD

- **Entities** ≈ DDD 的聚合/实体/值对象。
- **Use Cases** ≈ 应用服务（入站端口的实现）。
- **Interface Adapters** ≈ Controller / Presenter / Gateway 实现（DTO 映射）。
- **Frameworks & Drivers **≈ Web 框架、DB、消息、UI。

#### 3.2 优点

- 依赖方向明确，降低变更扩散。
- 与测试金字塔吻合：内核可单测、用例可服务级测试。

#### 3.3 常见陷阱

- 用例贫血化：只当“转发器”，导致业务散落到外层。
- 圈层滥用：所有类都“按圈放”，但实际边界仍不清（需要限界上下文先行）。

#### 3.4 最小实践清单

- 用例层只保留业务编排 + 事务边界，不写 IO 细节。
- Presenter/Assembler 在接口适配器层完成 DTO 转换。
- 网关接口定义在内层，具体实现放外层并通过依赖反转注入。

### 4. 菱形架构（COLA）

> COLA（Clean Object-Oriented and Layered Architecture） 是国内常用的 DDD 工程化落地模型，图形呈“菱形”，强调四层 + 契约：Adapter / Application / Domain / Infrastructure，并推广 Command/Result/DTO/Assembler/SPI 扩展点 等实践。

#### 4.1 结构

```
       Adapter（入口/出入口适配器：Web/Job/Schedule）
           │      ↑DTO/Assembler        ↓RPC/HTTP 调用
     Application（用例编排：Command/Query、事务、权限、日志）
           │      ↑Domain Event         ↓Repository/SPI
        Domain（聚合/实体/值对象/领域服务/领域事件）
           │      ↑仓储接口             ↓技术实现
   Infrastructure（DB/MQ/Cache/三方 SDK 实现、配置、SPI 扩展）
```

#### 4.2 工程约定（常见包结构）

```java
com.xxx.pay
  ├─ adapter.web   // Controller, VO
  ├─ app           // Command, Query, Service, Assembler
  ├─ domain        // model(aggregate), service, event, repository
  └─ infra         // repo impl, mapper, gateway impl, config
```

- **Command/Query**：明确用例输入（比“方法参数”更可观测、可审计）。
- **Assembler**：DTO ⇆ DO/Entity 映射集中管理。
- **SPI 扩展点**：在 infra 定义接口实现 + 装配；在 app 通过接口使用，方便替换/灰度。

#### 4.3 优点

- **工程实践成熟**：脚手架、规范、目录清晰，适合大团队协作。
- **可观测性好**：Command/Result 自带审计痕迹。
- **与 DDD 兼容**：领域仍是中心，技术实现沉到底层。

#### 4.4 注意点

- 需要纪律：防止业务滑入** infra/adapter**。
- Command/Assembler 要避免泛滥；界限不清会回到“贫血分层”。

### 5. 三种架构对比

| 维度 | 六边形（Ports & Adapters） | 整洁架构（Clean） | 菱形（COLA） |
|------|--------------------------|------------------|-------------|
| 关注点 | IO 隔离，适配器可插拔 | 依赖向内，圈层清晰 | 工程化与团队协作、规约化 |
| 对 DDD 适配 | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| 学习/落地成本 | 中 | 中 | 低-中（有模板） |
| 抗变能力 | UI/DB/MQ 强 | 框架/基础设施强 | 强（取决于执行） |
| 测试友好 | 非常强 | 强 | 强 |
| 易犯错误 | 端口粒度失控 | 用例贫血 | 规约过度、装配泛滥 |

### 6. 关键设计议题（与 DDD 的融合）

#### 6.1 事务与一致性

- **应用服务**作为事务边界；聚合内部保持强一致。
- 跨聚合/跨上下文：**领域事件 + Outbox**，或 **Saga/补偿**。

示例：

```sql
-- 幂等更新：仅当待支付时推进
UPDATE pay_order
SET status='SUCCESS', paid_at=NOW(), update_time=NOW()
WHERE id=:id AND status='PAY_WAIT';
```

#### 6.2 幂等与重试

- 入站：Idempotency-Key（去重表/唯一索引），重复请求返回首个结果。
- 出站：网关调用包裹 重试 + 幂等语义（例如第三方扣款接口）。

#### 6.3 模型完整性（不变式）

- 状态机、时间窗、额度校验在聚合内实现；减少“散落校验”。

#### 6.4 DTO/VO/DO 的边界

- **DTO**：跨层/跨上下文传输。
- **VO**：领域语义不可变值。
- **DO/PO**：数据持久化形态，尽量在 infra 层。

### 7. 目录与包结构建议（Java 示例）

```
com.example.mall
  ├─ pay
  │   ├─ adapter.web (controller, request/response VO)
  │   ├─ app (service, command/query, usecase, assembler)
  │   ├─ domain (model, aggregate, repository, domainservice, event)
  │  └─ infra (repoimpl, mapper, gatewayimpl, config)
  └─ common (exception, id, money, eventbus, outbox)
```

### 8. PlantUML 模板

#### 8.1 时序图（支付用例）

```
@startuml
actor User
participant API
participant App as ApplicationService
participant Domain
database DB
participant PayGW

User -> API : POST /pay
API -> ApplicationService : PayCommand
ApplicationService -> DB : repo.byId()
ApplicationService -> Domain : order.pay()
ApplicationService -> PayGW : charge()
PayGW --> ApplicationService : ok(tradeNo)
ApplicationService -> DB : repo.save(order)
ApplicationService --> API : PayResult
@enduml
```

#### 8.2 组件图（六边形）

```
@startuml
package Core {
  [Domain Model] -> [Domain Service]
}
[Inbound Port] --> [Application Service]
[Application Service] --> [Domain Model]
[Application Service] ..> [Repository Port]
[Application Service] ..> [Payment Port]
[HTTP Adapter] --> [Inbound Port]
[Repo Adapter(JPA)] ..> [Repository Port]
[Payment Adapter(HTTP)] ..> [Payment Port]
@enduml
```

### 9. 迁移路径（从 MVC/贫血到 DDD/充血）

- **按业务能力切上下文**（先战略后战术）。
- 识别聚合与不变式，把校验与状态变更**收口到实体**方法。
- 引入**应用服务**作为用例编排 + 事务边界。
- 抽象**出站端口**，替换直连三方/DAO；适配器承接技术实现。
- 引入**领域事件 + Outbox** 解耦跨上下文反应。
- 渐退 Controller/Service 巨物，分解到 UseCase + Domain。

### 10. 反模式与气味

- **贫血领域模型**：实体全是 getter/setter；规则散落 service/controller。
- **三方 SDK 直通领域**：领域被技术细节污染。
- **用例层写复杂业务**：违反“业务落域，编排在用例”。
- **跨聚合强一致事务**：耦合高、伸缩差；应使用事件/补偿。
- **DTO/DO/VO 混用**：边界不清导致层穿透。

### 11. 选型建议（Checklist）

- 你的系统是否**三方集成多/变化频繁**？→ 六边形优先。
- 是否需要**明确依赖方向与同心演进**？→ 整洁优先。
- 团队规模大、需要**统一规约与脚手架**？→ COLA 优先。
- 是否只是**后台 CRUD**？→ 轻量分层 + 少量 DDD 元素即可。

### 12. 附：示例代码片段（充血聚合）

```java
public class PayOrder {
  public enum Status { PAY_WAIT, SUCCESS, CLOSE }
  private final OrderId id; private Money amount; private Status status; private Instant expireAt;
  private String tradeNo; private Instant paidAt;

  public void ensurePayable() {
    if (status != Status.PAY_WAIT) throw new DomainException("非法状态");
    if (Instant.now().isAfter(expireAt)) throw new DomainException("已超时");
  }

  public void applyPaid(String tradeNo, Instant paidAt) {
    if (status == Status.SUCCESS) return; // 幂等
    ensurePayable();
    this.status = Status.SUCCESS; this.tradeNo = tradeNo; this.paidAt = paidAt;
    DomainEvents.raise(new OrderPaid(id, tradeNo, paidAt));
  }

  public void closeIfTimeout(Instant now) {
    if (status == Status.PAY_WAIT && now.isAfter(expireAt)) status = Status.CLOSE;
  }
}
```

### 结语

- DDD 是“分清边界 + 把业务装进模型”；
- 六边形/整洁/菱形是“把模型与外界解耦”的三种工程表达；
- 选型没有银弹，按变化点与团队能力做最小充分设计，才是长期演进的关键。