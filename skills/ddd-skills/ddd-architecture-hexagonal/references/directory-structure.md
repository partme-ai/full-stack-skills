# 六边形架构 — 完整目录结构参考


## 核心目录

```
project-root/
├── src/
│   ├── application/                # 应用层（用例层）
│   │   ├── ports/                  # 端口（接口定义）
│   │   │   ├── inbound/           # 入站端口（驱动端）
│   │   │   │   ├── UserService.java
│   │   │   │   └── OrderService.java
│   │   │   └── outbound/          # 出站端口（被驱动端）
│   │   │       ├── UserRepository.java
│   │   │       └── OrderRepository.java
│   │   ├── services/              # 应用服务实现
│   │   ├── usecases/              # 具体用例
│   │   └── dto/                   # 数据传输对象
│   ├── domain/                     # 领域层
│   │   ├── models/                # 聚合根/实体
│   │   ├── valueobjects/          # Email, Money, Quantity
│   │   ├── events/                # 领域事件
│   │   ├── services/              # 领域服务
│   │   └── repositories/          # 仓储接口
│   ├── infrastructure/             # 基础设施层（所有适配器）
│   │   ├── adapters/
│   │   │   ├── inbound/           # 入站适配器
│   │   │   │   ├── web/controllers/
│   │   │   │   ├── cli/
│   │   │   │   └── messaging/
│   │   │   └── outbound/          # 出站适配器
│   │   │       ├── persistence/repositories/
│   │   │       ├── external/
│   │   │       └── messaging/
│   │   ├── config/                # DatabaseConfig, CacheConfig
│   │   └── database/migrations/
│   ├── shared/                     # BaseEntity, AggregateRoot, ValueObject
│   └── MainApplication.java
└── test/
    ├── unit/domain/
    ├── unit/application/
    └── integration/
```

## 端口命名约定

| 类型 | 模式 | 示例 |
|------|------|------|
| 入站端口 | `I{Action}UseCase` | `IPlaceOrderUseCase` |
| 出站端口 | `I{Resource}Repository` | `IOrderRepository` |
| 出站端口 | `I{Resource}Gateway` | `IPaymentGateway` |

## 关键规则

1. 端口在应用层/领域层定义，适配器在基础设施层实现
2. 所有依赖指向核心：Infrastructure → Application → Domain
3. 入站适配器（Controller）把 HTTP 请求转为端口调用
4. 出站适配器（RepositoryImpl）实现仓储接口

## 源代码

