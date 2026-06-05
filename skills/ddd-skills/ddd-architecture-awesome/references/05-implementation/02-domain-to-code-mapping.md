# Domain-to-Code Mapping — 领域对象到代码对象的映射

## 映射流程

```
事件风暴 → 领域模型 → 用户故事分析 → 微服务设计 → 代码映射
```

## 领域对象整理表

| 维度 | 内容 |
|------|------|
| 领域模型 | 属于哪个限界上下文 |
| 聚合 | 属于哪个聚合 |
| 领域对象 | 具体的对象名称 |
| 领域类型 | 聚合根 / 实体 / 值对象 / 命令 / 领域事件 / 领域服务 / 仓储 |

## 从领域模型到微服务的设计清单

对每个聚合，逐一回答：

| 问题 | 产出 |
|------|------|
| 微服务内有哪些服务？ | 应用服务、领域服务、实体方法列表 |
| 服务在分层架构的哪一层？ | interfaces / application / domain / infrastructure |
| 应用服务由哪些服务组合编排？ | 编排依赖关系图 |
| 领域服务包含哪些实体的业务逻辑？ | 领域服务方法签名 |
| 充血模型实体有哪些属性和方法？ | 实体类定义 |
| 哪些属性应设计为值对象？ | VO 定义 |
| 哪个实体是聚合根？ | 聚合根确定 |

## 完整映射表模板

| 层 | 领域对象 | 领域类型 | 依赖的领域对象 | 包名 | 类名 | 方法名 |
|----|----------|----------|---------------|------|------|--------|
| interfaces | 订单请求 | DTO | - | interfaces.dto | OrderDTO | - |
| interfaces | Facade | Facade | OrderAppService | interfaces.facade | OrderFacade | createOrder |
| application | 下单命令 | Command | - | application.service | PlaceOrderCommand | - |
| application | 订单应用服务 | AppService | OrderDomainService, ProductAppService | application.service | OrderAppService | placeOrder |
| domain | 订单 | 聚合根 | OrderItem, OrderStatus | domain.order.entity | Order | place |
| domain | 订单项 | 实体 | ProductId, Money | domain.order.entity | OrderItem | - |
| domain | 金额 | 值对象 | - | domain.order.entity | Money | add |
| domain | 订单状态 | 值对象 | - | domain.order.entity | OrderStatus | canPay |
| domain | 订单领域服务 | DomainService | Order, OrderItem | domain.order.service | OrderDomainService | calculateTotal |
| domain | 订单仓储接口 | Repository | Order | domain.order.repository | OrderRepository | save |
| domain | 订单已创建 | 领域事件 | Order | domain.order.event | OrderCreatedEvent | - |
| infrastructure | 订单仓储实现 | RepoImpl | OrderMapper | infrastructure.persistence | OrderRepositoryImpl | save |

## 实体设计要点

| 要点 | 说明 |
|------|------|
| 充血模型 | 实体类的方法实现自身相关的所有业务逻辑 |
| 聚合根特殊职责 | 管理聚合内对象生命周期；对外接口（ID引用） |
| 值对象识别 | 有些属性集在微服务设计时才被发现需要设计为值对象 |
| 隐式实体发现 | 地址、电话、银行账号等可能在事件风暴中被忽略，微服务设计时补全 |

## 领域事件设计要点

1. 确定事件发生在微服务内还是微服务之间
2. 设计事件实体对象（继承 DomainEvent）
3. 设计事件发布和订阅机制
4. 判断是否需要事件总线或消息中间件
5. 事件实体放领域层 Event 目录，发布/订阅类放应用层 Event 目录

## 领域服务设计要点

| 场景 | 做法 |
|------|------|
| 业务逻辑跨多个实体 | 设计领域服务组合实体方法 |
| 实体方法需暴露给应用层（严格分层） | 先封装为领域服务，再封装为应用服务 |
| 多个应用服务重复编排同样的领域服务组合 | 下沉合并为新的领域服务 |

## 仓储设计要点

| 原则 | 说明 |
|------|------|
| 一聚合一仓储 | 每个聚合对应一个仓储接口和实现 |
| 接口在领域层 | 定义在 aggregate 目录下的 repository/ |
| 实现在基础层 | 放在 infrastructure/persistence/ |
| 依赖倒置 | 应用层依赖接口，不依赖实现 |
