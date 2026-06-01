# DDD 经典分层架构 — 完整目录结构参考


## 模块划分

```
project-root/
├── project-interface/              # 用户接口层
├── project-application/            # 应用层
├── project-domain/                 # 领域层（核心，零依赖）
├── project-infrastructure/         # 基础设施层
└── start/                          # 启动模块
```

## 领域层详细结构

```
domain/
├── model/
│   ├── aggregate/                  # 按聚合分包
│   │   ├── order/                  # 订单聚合
│   │   │   ├── Order.java         # 聚合根（充血模型）
│   │   │   ├── OrderItem.java     # 实体
│   │   │   ├── OrderStatus.java   # 值对象/枚举
│   │   │   └── repository/        # 仓储接口（只定义）
│   │   ├── customer/              # 客户聚合
│   │   └── product/               # 产品聚合
│   ├── entity/                    # 独立实体
│   ├── valueobject/               # 值对象
│   │   ├── Money.java
│   │   ├── Email.java
│   │   ├── Address.java
│   │   └── Quantity.java
│   ├── service/                   # 领域服务
│   ├── event/                     # 领域事件
│   ├── specification/             # 规约模式
│   ├── factory/                   # 工厂
│   ├── policy/                    # 业务策略
│   └── exception/                 # 领域异常
├── boundedcontext/                # 限界上下文（大型系统）
└── sharedkernel/                  # 共享内核
```

## 关键设计原则

1. **依赖方向**: Interface → Application → Domain ← Infrastructure
2. **Domain 纯净度**: 零 Spring/JPA/MyBatis 依赖
3. **充血模型**: 业务逻辑在实体方法中，不在 Service 中
4. **聚合设计**: 一次事务只修改一个聚合，聚合间通过 ID 引用
5. **仓储接口**: 在 Domain 层定义接口，在 Infrastructure 层实现

## 源代码

