# 微服务简单 — DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 10-30 人，分为 3-5 个子团队 |
| 业务复杂度 | 中高，各子域独立性强 |
| 部署方式 | 独立 Spring Boot JAR，Docker/K8s 部署 |
| 技术栈 | Spring Boot + Spring Cloud / REST + MyBatis/JPA |
| 通信方式 | REST API（同步）+ 轻量 MQ（异步通知） |

**典型业务**：电商系统已拆分为订单服务、商品服务、支付服务；每个服务内部是独立的 DDD 分层单体。

## 目录树

```
ecommerce-platform/
├── pom.xml                                    # 根 POM
│
├── order-service/                             # 订单服务
│   ├── pom.xml
│   └── src/main/java/com/example/order/
│       ├── OrderServiceApplication.java       # 独立启动类
│       ├── interface/
│       │   ├── controller/
│       │   │   └── OrderController.java       # REST API
│       │   ├── dto/
│       │   │   ├── request/
│       │   │   └── response/
│       │   └── converter/
│       │       └── OrderDtoConverter.java
│       ├── application/
│       │   ├── service/
│       │   │   └── OrderApplicationService.java
│       │   ├── command/
│       │   │   ├── CreateOrderCommand.java
│       │   │   └── CancelOrderCommand.java
│       │   └── query/
│       │       └── OrderDetailQuery.java
│       ├── domain/
│       │   └── order/
│       │       ├── entity/
│       │       │   ├── Order.java
│       │       │   └── OrderItem.java
│       │       ├── valueobject/
│       │       │   ├── Money.java
│       │       │   ├── OrderStatus.java
│       │       │   └── Address.java
│       │       ├── service/
│       │       │   └── OrderDomainService.java
│       │       ├── repository/
│       │       │   └── OrderRepository.java
│       │       └── event/
│       │           └── OrderPlacedEvent.java
│       └── infrastructure/
│           ├── repository/
│           │   └── MyBatisOrderRepository.java
│           ├── persistence/
│           │   ├── OrderPO.java
│           │   └── OrderItemPO.java
│           ├── external/
│           │   ├── ProductServiceClient.java   # 调用商品服务 REST API
│           │   ├── PaymentServiceClient.java   # 调用支付服务 REST API
│           │   └── UserServiceClient.java      # 调用用户服务 REST API
│           └── config/
│               └── RepositoryConfig.java
│
├── product-service/                           # 商品服务
│   ├── pom.xml
│   └── src/main/java/com/example/product/
│       ├── ProductServiceApplication.java
│       ├── interface/
│       │   ├── controller/
│       │   │   └── ProductController.java
│       │   ├── dto/
│       │   └── converter/
│       ├── application/
│       │   ├── service/
│       │   │   └── ProductApplicationService.java
│       │   ├── command/
│       │   └── query/
│       ├── domain/
│       │   └── product/
│       │       ├── entity/
│       │       │   ├── Product.java
│       │       │   └── Category.java
│       │       ├── valueobject/
│       │       │   ├── Price.java
│       │       │   ├── Sku.java
│       │       │   └── Stock.java
│       │       ├── service/
│       │       │   └── InventoryDomainService.java
│       │       ├── repository/
│       │       │   └── ProductRepository.java
│       │       └── event/
│       │           └── StockDeductedEvent.java
│       └── infrastructure/
│           ├── repository/
│           │   └── MyBatisProductRepository.java
│           ├── persistence/
│           │   ├── ProductPO.java
│           │   └── CategoryPO.java
│           └── config/
│               └── RepositoryConfig.java
│
├── payment-service/                           # 支付服务
│   ├── pom.xml
│   └── src/main/java/com/example/payment/
│       ├── PaymentServiceApplication.java
│       ├── interface/
│       │   ├── controller/
│       │   │   └── PaymentController.java
│       │   ├── dto/
│       │   └── converter/
│       ├── application/
│       │   ├── service/
│       │   │   └── PaymentApplicationService.java
│       │   ├── command/
│       │   └── query/
│       ├── domain/
│       │   └── payment/
│       │       ├── entity/
│       │       │   └── Payment.java
│       │       ├── valueobject/
│       │       │   ├── PaymentMethod.java
│       │       │   ├── PaymentStatus.java
│       │       │   └── Amount.java
│       │       ├── service/
│       │       │   └── PaymentDomainService.java
│       │       ├── repository/
│       │       │   └── PaymentRepository.java
│       │       └── event/
│       │           └── PaymentCompletedEvent.java
│       └── infrastructure/
│           ├── repository/
│           │   └── MyBatisPaymentRepository.java
│           ├── persistence/
│           │   └── PaymentPO.java
│           ├── external/
│           │   └── AlipayClient.java
│           └── config/
│               └── RepositoryConfig.java
│
└── api-gateway/                               # API 网关（可选）
    ├── pom.xml
    └── src/main/java/com/example/gateway/
        └── GatewayApplication.java
```

## 包结构

```
com.example.order      — 订单微服务
com.example.product    — 商品微服务
com.example.payment    — 支付微服务
com.example.gateway    — API 网关
```

每个微服务内部是独立的 DDD 四层结构，与单体简单项目（06）完全一致。

## 模块依赖

### 根 POM

```xml
<groupId>com.example</groupId>
<artifactId>ecommerce-platform</artifactId>
<version>1.0.0</version>
<packaging>pom</packaging>

<modules>
    <module>order-service</module>
    <module>product-service</module>
    <module>payment-service</module>
    <module>api-gateway</module>
</modules>
```

### 服务间依赖

```
order-service  ──REST──▶  product-service
order-service  ──REST──▶  payment-service
payment-service ──REST──▶  order-service (查询订单)
```

服务间通过 Feign/OpenFeign 或 RestTemplate 通信，在 Infrastructure 层的 `external/` 包中实现客户端：

```java
// order-service/infrastructure/external/ProductServiceClient.java
@FeignClient(name = "product-service", url = "${product.service.url}")
public interface ProductServiceClient {
    @GetMapping("/api/products/{id}")
    ProductDTO getProduct(@PathVariable("id") Long id);

    @PostMapping("/api/products/{id}/deduct-stock")
    void deductStock(@PathVariable("id") Long id, @RequestBody DeductStockDTO request);
}
```

## 服务间集成策略

| 场景 | 方式 | 说明 |
|------|------|------|
| 创建订单 → 校验商品 | 同步 REST | 需要即时返回结果 |
| 创建订单 → 查询用户信息 | 同步 REST | 查询操作 |
| 支付完成 → 更新订单状态 | 异步 MQ | 最终一致性 |
| 库存扣减 → 通知订单 | 异步 MQ | 解耦通知 |
| 商品下架 → 取消关联订单 | 异步 MQ | 批量处理 |

## 关键设计要点

| 要点 | 说明 |
|------|------|
| 服务自治 | 每个服务有独立数据库，不共享表 |
| 独立部署 | 各服务独立构建、独立部署、独立扩缩容 |
| 合同优先 | 服务间 API 版本化，向前兼容 |
| 防腐层 | 外部服务调用封装在 infrastructure/external |
| 最终一致性 | 跨服务业务通过 MQ 异步对齐 |

## 优点与局限

| 优点 | 局限 |
|------|------|
| 独立部署和扩缩容 | 分布式系统复杂性（网络/超时/重试） |
| 团队自治，并行开发 | 服务间耦合仍存在 |
| 故障隔离，单服务挂不影响全局 | 调试和排错困难 |
| 技术栈可异构 | 数据一致性需要分布式事务支持 |

## 演进路径

```
微服务简单 → 微服务复杂（10，事件驱动）→ 微服务多模块（11）
```
