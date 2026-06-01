# 单体复杂项目 — 多聚合根 DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 5-15 人，有一定 DDD 经验 |
| 业务复杂度 | 3-5 个聚合根，多领域服务协作 |
| 部署方式 | 单体 Spring Boot JAR，单数据库或多 Schema |
| 技术栈 | Spring Boot + MyBatis/JPA + Maven |
| 典型业务 | 电商核心域（订单/商品/支付）、CRM 系统、进销存 |

**关键特征**：单应用承载多子域，Application 层做跨聚合编排，Domain 层按聚合内聚。

## 目录树

```
ecommerce/
├── pom.xml
└── src/
    └── main/
        └── java/
            └── com/example/ecommerce/
                ├── EcommerceApplication.java
                │
                ├── interface/                          # 接口层（按聚合分子包）
                │   ├── controller/
                │   │   ├── order/
                │   │   │   └── OrderController.java
                │   │   ├── product/
                │   │   │   └── ProductController.java
                │   │   └── payment/
                │   │       └── PaymentController.java
                │   ├── dto/
                │   │   ├── request/
                │   │   └── response/
                │   └── converter/
                │       ├── OrderDtoConverter.java
                │       ├── ProductDtoConverter.java
                │       └── PaymentDtoConverter.java
                │
                ├── application/                        # 应用层（跨聚合编排）
                │   ├── service/
                │   │   ├── order/
                │   │   │   └── OrderApplicationService.java
                │   │   ├── product/
                │   │   │   └── ProductApplicationService.java
                │   │   ├── payment/
                │   │   │   └── PaymentApplicationService.java
                │   │   └── orchestration/              # 跨聚合编排服务
                │   │       └── CheckoutOrchestrationService.java
                │   ├── command/
                │   │   ├── CreateOrderCommand.java
                │   │   ├── DeductStockCommand.java
                │   │   └── CreatePaymentCommand.java
                │   ├── query/
                │   │   ├── OrderDetailQuery.java
                │   │   └── ProductListQuery.java
                │   ├── assembler/
                │   │   └── OrderAssembler.java         # 跨聚合数据组装
                │   └── event/
                │       └── handler/
                │           ├── OrderPaidHandler.java    # 支付后扣库存
                │           └── StockShortageHandler.java # 库存不足补偿
                │
                ├── domain/                             # 领域层 ★（按聚合分包）
                │   ├── order/
                │   │   ├── entity/
                │   │   │   ├── Order.java              # 订单聚合根
                │   │   │   └── OrderItem.java
                │   │   ├── valueobject/
                │   │   │   ├── Money.java
                │   │   │   ├── OrderStatus.java
                │   │   │   ├── Address.java
                │   │   │   └── OrderId.java
                │   │   ├── service/
                │   │   │   ├── OrderDomainService.java
                │   │   │   └── OrderPricingService.java # 定价领域服务
                │   │   ├── repository/
                │   │   │   └── OrderRepository.java
                │   │   └── event/
                │   │       ├── OrderPlacedEvent.java
                │   │       └── OrderCancelledEvent.java
                │   │
                │   ├── product/
                │   │   ├── entity/
                │   │   │   ├── Product.java            # 商品聚合根
                │   │   │   └── Category.java
                │   │   ├── valueobject/
                │   │   │   ├── Price.java
                │   │   │   ├── Sku.java
                │   │   │   └── ProductId.java
                │   │   ├── service/
                │   │   │   └── InventoryDomainService.java
                │   │   ├── repository/
                │   │   │   └── ProductRepository.java
                │   │   └── event/
                │   │       ├── StockDeductedEvent.java
                │   │       └── StockReplenishedEvent.java
                │   │
                │   ├── payment/
                │   │   ├── entity/
                │   │   │   └── Payment.java            # 支付聚合根
                │   │   ├── valueobject/
                │   │   │   ├── PaymentMethod.java
                │   │   │   └── PaymentStatus.java
                │   │   ├── service/
                │   │   │   └── PaymentDomainService.java
                │   │   ├── repository/
                │   │   │   └── PaymentRepository.java
                │   │   └── event/
                │   │       ├── PaymentCompletedEvent.java
                │   │       └── PaymentRefundedEvent.java
                │   │
                │   ├── factory/
                │   │   └── OrderFactory.java           # 复杂聚合创建
                │   └── shared/
                │       ├── BaseEntity.java
                │       ├── BaseValueObject.java
                │       ├── AggregateRoot.java
                │       └── DomainEvent.java
                │
                └── infrastructure/                     # 基础设施层
                    ├── repository/
                    │   ├── order/
                    │   │   └── MyBatisOrderRepository.java
                    │   ├── product/
                    │   │   └── MyBatisProductRepository.java
                    │   └── payment/
                    │       └── MyBatisPaymentRepository.java
                    ├── persistence/
                    │   ├── OrderPO.java
                    │   ├── OrderItemPO.java
                    │   ├── ProductPO.java
                    │   ├── ProductSkuPO.java
                    │   └── PaymentPO.java
                    ├── messaging/                       # 领域事件发布
                    │   ├── DomainEventPublisher.java
                    │   └── SpringEventPublisher.java
                    ├── external/                        # 外部服务适配
                    │   ├── AlipayClient.java
                    │   └── SmsClient.java
                    └── config/
                        ├── RepositoryConfig.java
                        └── EventConfig.java
```

## 包结构

```
com.example.ecommerce
├── interface
│   └── 按聚合分子包（order/product/payment controller）
├── application
│   ├── 按聚合分 service (order/product/payment)
│   └── orchestration 层负责跨聚合编排
├── domain
│   ├── order/     — 订单聚合
│   ├── product/   — 商品聚合
│   ├── payment/   — 支付聚合
│   └── shared/    — 共享基类
└── infrastructure
    ├── repository/ — 按聚合分实现
    ├── messaging/  — 事件总线
    └── external/   — 外部服务适配器
```

## 模块依赖

```xml
<!-- 单模块 pom.xml -->
<dependencies>
    <!-- Spring Boot -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- 持久化 -->
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
    </dependency>
    <!-- 事件发布（Application 层用） -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <!-- 架构验证 -->
    <dependency>
        <groupId>com.tngtech.archunit</groupId>
        <artifactId>archunit-junit5</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

**跨聚合编排示例**：

```java
// Application 层：CheckoutOrchestrationService（跨聚合编排）
@Service
public class CheckoutOrchestrationService {
    private final OrderDomainService orderDomainService;
    private final InventoryDomainService inventoryDomainService;
    private final PaymentDomainService paymentDomainService;

    @Transactional
    public CheckoutResult checkout(CheckoutCommand command) {
        // 1. 锁定库存（Product 聚合）
        inventoryDomainService.deduct(command.getProductId(), command.getQuantity());
        // 2. 创建订单（Order 聚合）
        Order order = orderDomainService.createOrder(command);
        // 3. 发起支付（Payment 聚合）
        Payment payment = paymentDomainService.initiate(order);
        return new CheckoutResult(order, payment);
    }
}
```

## 关键设计要点

| 要点 | 说明 |
|------|------|
| 聚合间引用 | 通过 ID 引用，不直接持有对象引用 |
| 跨聚合编排 | Application 层 orchestration 包集中管理 |
| 领域服务 | Domain 层中的 service 处理跨实体逻辑 |
| 领域事件 | 聚合内事件，同进程发布 |
| 事务边界 | Application 层 `@Transactional` 控制 |

## 优点与局限

| 优点 | 局限 |
|------|------|
| 单应用部署，运维简单 | 业务耦合度高，修改需全量回归 |
| 多聚合协作方便 | 事务边界大，性能瓶颈明显 |
| 共享基础设施（DB/缓存） | DB 耦合，无法独立伸缩 |
| 适合中等规模业务 | 团队扩大后易产生合并冲突 |

## 演进路径

```
单体复杂 → 多模块拆分（08）→ 按子域拆分微服务（09/10）
```
