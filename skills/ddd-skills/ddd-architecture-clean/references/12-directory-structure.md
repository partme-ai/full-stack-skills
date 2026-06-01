# 整洁架构 — 完整目录结构参考


## 四层圈层结构

```
project-root/
├── src/
│   ├── domain/                     # 最内层：业务实体
│   │   ├── entities/
│   │   │   ├── User.java          # 核心实体
│   │   │   ├── Order.java         # 核心实体
│   │   │   └── aggregates/        # 聚合根
│   │   ├── valueobjects/
│   │   │   ├── common/            # Money, Email, PhoneNumber
│   │   │   ├── user/              # UserId, UserName, Password
│   │   │   └── order/             # OrderId, OrderItem, OrderStatus
│   │   ├── services/              # UserRegistrationService, PricingService
│   │   ├── events/                # DomainEvent 接口 + 具体事件
│   │   ├── repositories/          # 仓储接口（不含实现）
│   │   ├── policies/              # DiscountPolicy, ShippingPolicy
│   │   └── exceptions/            # DomainException, BusinessRuleException
│   │
│   ├── application/               # 第二层：用例层
│   │   ├── usecases/
│   │   │   ├── user/              # CreateUserUseCase, GetUserUseCase
│   │   │   ├── order/             # CreateOrderUseCase, CancelOrderUseCase
│   │   │   └── commands/          # CreateUserCommand, CreateOrderCommand
│   │   ├── services/              # 应用服务（协调用例）
│   │   ├── ports/
│   │   │   ├── input/             # 输入端口（驱动端接口）
│   │   │   ├── output/            # 输出端口（仓储、网关接口）
│   │   │   └── gateways/          # IdGeneratorGateway, CryptoGateway
│   │   ├── dto/                   # request/, response/, internal/
│   │   ├── mappers/               # 对象映射器
│   │   └── exceptions/
│   │
│   ├── infrastructure/             # 最外层：技术实现
│   │   ├── persistence/
│   │   │   ├── repositories/      # 仓储实现（JPA/MyBatis）
│   │   │   ├── entities/          # 持久化实体（@Entity）
│   │   │   ├── mappers/           # 持久化映射器
│   │   │   └── migrations/
│   │   ├── messaging/             # Kafka, RabbitMQ
│   │   ├── external/              # 外部 API 客户端
│   │   └── configuration/         # Spring/DI 配置
│   │
│   └── shared/                    # 跨层共享
│       ├── kernel/                # BaseEntity, AggregateRoot, ValueObject
│       └── utils/                 # 工具类
```

## 依赖规则

```
Infrastructure → Application → Domain
  (适配器)       (用例)        (核心)

内层不依赖外层。Domain 层零框架依赖。
```

## 源代码

