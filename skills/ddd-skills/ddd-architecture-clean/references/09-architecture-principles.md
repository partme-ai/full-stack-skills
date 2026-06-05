# 整洁架构核心原理详解

> 本文包含 SKILL.md 主文档中移入的详细架构原理内容，供深度阅读。

## 四层结构

| 层（外→内） | 职责 | 依赖方向 |
|:---|------|------|
| Frameworks & Drivers | Web 框架、DB、UI、DI 配置 | → Adapter |
| Interface Adapters | Controller、Gateway、Presenter、Repository Impl | → UseCase |
| Application Business Rules | UseCase Interactor（编排实体+端口调用） | → Enterprise |
| Enterprise Business Rules | Entity、ValueObject、DomainEvent、业务规则 ★ | 无依赖 |

## 依赖规则（Gold Rule）

> 源码依赖只能指向内层。Enterprise 是中心，Framework 是最外圈。

```
Enterprise ← UseCase ← Adapter ← Framework
   (纯POJO)  (Port+Interactor) (转换+实现) (DI配置+启动)
```

## 架构对比

| 维度 | 整洁架构 | 六边形 | 洋葱 | COLA v5 |
|------|:---:|:---:|:---:|:---:|
| 核心概念 | UseCase + Entity | Port + Adapter | Domain 同心圆 | 菱形架构 |
| 层数 | 4 层 | 3 层（核心+端口+适配器） | 3+ 层 | 4 层 |
| 抽象层级 | 最高 | 高 | 高 | 中 |
| 学习成本 | ★★★ | ★★★ | ★★★ | ★★☆ |
| 适用场景 | 大型企业级 UseCase 驱动 | 多入口微服务 | 基础设施频繁变更 | 国内 Spring Boot 生态 |
| 模块隔离 | 极严格 | 严格 | 严格 | 严格 |
| 代表作 | Robert C. Martin | Alistair Cockburn | Jeffrey Palermo | 阿里 COLA |

## 四层间数据流转

```
HTTP Request
  → Controller (Adapter) 接收, 转为 Input DTO
    → UseCase Port (interface) 定义 Input
      → Interactor (UseCase Impl) 编排:
          1. 调 Entity 执行业务规则
          2. 调 Output Port 持久化/发消息
          3. 发布领域事件
    → UseCase Port 返回 Output DTO
  → Presenter/Response (Adapter) 转为 HTTP Response
```

## 完整目录结构

```
{project}/
├── {project}-core/                      # Enterprise Business Rules
│   ├── entity/                          # ★ 核心实体
│   │   ├── Order.java                   # 充血模型, 零框架依赖
│   │   └── OrderItem.java
│   ├── valueobject/                     # ★ 不可变值对象
│   │   ├── OrderId.java, Money.java, OrderStatus.java
│   ├── event/                           # ★ 领域事件
│   │   ├── DomainEvent.java (abstract)
│   │   ├── OrderCreatedEvent.java
│   │   └── OrderPaidEvent.java
│   ├── exception/                       # ★ 领域异常
│   │   ├── DomainException.java
│   │   └── OrderDomainException.java
│   └── service/                         # ★ 领域服务（无状态）
├── {project}-usecase/                   # Application Business Rules
│   ├── port/
│   │   ├── input/                       # ★ 输入端口（UseCase 接口）
│   │   │   ├── CreateOrderUseCase.java
│   │   │   └── PayOrderUseCase.java
│   │   └── output/                      # ★ 输出端口（Repository/Gateway 接口）
│   │       ├── OrderRepository.java
│   │       └── PaymentGateway.java
│   ├── interactor/                      # ★ UseCase 实现
│   │   ├── CreateOrderInteractor.java
│   │   └── PayOrderInteractor.java
│   └── dto/                             # UseCase 专用 DTO
├── {project}-adapter/                   # Interface Adapters
│   ├── controller/                      # REST Controller
│   ├── presenter/                       # 响应格式转换
│   ├── repository/                      # DB 实现（实现 Output Port）
│   ├── gateway/                         # 外部 API 实现
│   └── converter/                       # DTO ↔ Entity 转换
└── {project}-framework/                 # Frameworks & Drivers
    ├── config/                          # Spring DI 配置
    ├── persistence/                     # JPA Entity, Mapper
    └── web/                             # Web 配置 (CORS, Security)
```
