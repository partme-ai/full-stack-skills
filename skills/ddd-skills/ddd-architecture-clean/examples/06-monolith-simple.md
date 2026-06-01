# 06 — 单体 Clean 架构（简单版）

> 单一 Maven 模块内按包名划分四层：entities + usecases + interface-adapters + frameworks。

## 目录树

```
order-service/
├── src/main/java/com/example/order/
│   ├── enterprise/                  # Enterprise Business Rules
│   │   ├── entity/
│   │   │   ├── Order.java           # 聚合根
│   │   │   └── OrderItem.java       # 值对象
│   │   ├── vo/
│   │   │   ├── OrderId.java
│   │   │   ├── Money.java
│   │   │   └── OrderStatus.java
│   │   └── event/
│   │       ├── DomainEvent.java
│   │       └── OrderCreatedEvent.java
│   │
│   ├── usecase/                     # Application Business Rules
│   │   ├── port/
│   │   │   ├── input/
│   │   │   │   └── CreateOrderUseCase.java
│   │   │   └── output/
│   │   │       ├── OrderRepository.java
│   │   │       ├── PaymentGateway.java
│   │   │       └── EventPublisher.java
│   │   ├── dto/
│   │   │   ├── CreateOrderRequest.java
│   │   │   └── CreateOrderResponse.java
│   │   └── interactor/
│   │       └── CreateOrderInteractor.java
│   │
│   ├── adapter/                     # Interface Adapters
│   │   ├── controller/
│   │   │   └── OrderController.java
│   │   ├── repository/
│   │   │   ├── OrderJpaRepository.java
│   │   │   └── OrderRepositoryImpl.java
│   │   ├── gateway/
│   │   │   └── PaymentGatewayImpl.java
│   │   └── presenter/
│   │       └── CreateOrderPresenter.java
│   │
│   └── framework/                   # Frameworks & Drivers
│       └── config/
│           ├── PersistenceConfig.java
│           ├── UseCaseConfig.java
│           └── WebConfig.java
│
├── src/test/java/com/example/order/
│   ├── enterprise/entity/OrderTest.java
│   ├── usecase/interactor/CreateOrderInteractorTest.java
│   ├── adapter/repository/OrderRepositoryImplTest.java
│   └── architecture/
│       └── ArchitectureTest.java
│
└── pom.xml
```

## 包结构关系

```
┌─────────────────────────────────────────────────┐
│  framework                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Config   │  │ Spring DI│  │ DevTools │      │
│  └────┬─────┘  └──────────┘  └──────────┘      │
│       │ 依赖                                     │
├───────▼─────────────────────────────────────────┤
│  adapter                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │Controller│  │Repository│  │ Gateway  │      │
│  │          │  │ Impl     │  │ Impl     │      │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
│       │              │              │            │
├───────▼──────────────▼──────────────▼───────────┤
│  usecase                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │Interactor│  │Port(input│  │Port(out) │      │
│  │          │  │ /output) │  │          │      │
│  └────┬─────┘  └──────────┘  └──────────┘      │
│       │                                          │
├───────▼─────────────────────────────────────────┤
│  enterprise                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Entity   │  │ ValueObj │  │ Event    │      │
│  └──────────┘  └──────────┘  └──────────┘      │
└─────────────────────────────────────────────────┘
```

## 依赖方向

```
framework ──► adapter ──► usecase ──► enterprise
   │              │            │
   └── 只依赖外层 ─┴── 不依赖内层 ─┘
```

- **enterprise**: 零依赖（不依赖任何外部包，只依赖 Java 标准库）
- **usecase**: 只依赖 `enterprise` 包
- **adapter**: 依赖 `usecase` 端口 + `enterprise` 实体
- **framework**: 依赖 `adapter` + Spring Boot

## ArchUnit 验证规则

```java
@AnalyzeClasses(packages = "com.example.order")
public class ArchitectureTest {

    @ArchTest
    static final ArchRule enterprise_no_deps = classes()
        .that().resideInAPackage("..enterprise..")
        .should().onlyDependOnClassesThat()
        .resideInAnyPackage("java..", "..enterprise..");

    @ArchTest
    static final ArchRule usecase_no_framework = classes()
        .that().resideInAPackage("..usecase..")
        .should().onlyDependOnClassesThat()
        .resideInAnyPackage("..enterprise..", "..usecase..", "java..");

    @ArchTest
    static final ArchRule adapter_no_web = classes()
        .that().resideInAPackage("..adapter.repository..")
        .should().onlyHaveDependentClassesThat()
        .resideInAPackage("..adapter..");
}
```

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 3-8 人，单团队维护 |
| 项目复杂度 | 1-3 个聚合根，< 20 个 UseCase |
| 模块数 | 单一 Maven 模块（单仓库） |
| 部署方式 | 单体部署，一个 Spring Boot JAR |
| 演进路径 | 简单版 → 复杂版（07）→ 多模块（08）→ 微服务拆分 |
| 典型业务 | 中小型电商后台、CMS、内部工具系统 |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| 包级隔离，结构清晰 | 编译期无法强制分层约束（需 ArchUnit 补救） |
| 学习成本低，团队快速上手 | 包依赖靠约定，新人可能放错位置 |
| 一套 CI 管道，部署简单 | 单一模块耦合，难以模块级独立发布 |
| 适合从三层架构渐进迁移 | 大型项目包膨胀，定位文件困难 |
