# DDD Layered Architecture — 四层架构详解

## 层级与职责

```
用户接口层 (Interfaces) — DTO, Assembler, Facade
        │
  应用层 (Application) — 编排、事务、权限、事件发布
        │
  领域层 (Domain) — 核心业务逻辑、充血模型
        │  ↑ 接口定义（依赖倒置）
  基础层 (Infrastructure) — Repository实现, Mapper, 消息中间件, 缓存
```

| 层 | 职责 | 关键组件 |
|----|------|----------|
| **用户接口层** | 请求解析、数据展示、DTO转换 | Controller, Facade, Assembler, DTO |
| **应用层** | 服务编排、事务控制、权限校验、事件发布 | ApplicationService, EventPublisher, EventSubscriber |
| **领域层** | 核心业务逻辑、不变量校验、充血模型 | Entity, ValueObject, AggregateRoot, DomainService, Repository接口 |
| **基础层** | 技术支撑、资源访问 | Repository实现, DAO/Mapper, 消息中间件, 缓存 |

## 严格分层 vs 松散分层

| 模式 | 规则 | 优点 | 缺点 |
|------|------|------|------|
| **严格分层** | 每层只能依赖紧邻下层 | 服务可管理，变更影响可控 | 封装层次多 |
| **松散分层** | 任意下层可被上层调用 | 调用直接，响应快 | 变更影响难追踪 |

> **推荐严格分层**。领域服务变更时只需逐层通知上层，不会遗漏调用方。

## 三层架构 → DDD 四层演进

```
传统三层                    DDD 四层
────────                    ───────
表现层 (Controller)  ───→  用户接口层（引入 DTO+Facade）
                              ↓
业务逻辑层 (Service)  ───→  应用层（编排+事务+权限）
                           + 领域层（充血模型+不变量）
                              ↓
数据访问层 (DAO)      ───→  基础层（仓储+依赖倒置）
```

### 演进关键变化

| 变化点 | 传统做法 | DDD 做法 |
|--------|----------|----------|
| 业务逻辑 | Service 中写所有逻辑 | 实体充血 + 领域服务 + 应用编排 |
| 数据访问 | Service 直接调 DAO | Repository 接口在领域层，实现在基础层 |
| 依赖方向 | 上层依赖下层 | 领域层不依赖基础层（依赖倒置） |
| DTO 位置 | Controller 层拼数据 | 用户接口层 Assembler 转换 |

## 依赖倒置 (DIP)

```java
// 领域层 — 定义接口（不依赖任何框架）
package domain.order;
public interface OrderRepository {
    Order findById(OrderId id);
    void save(Order order);
}

// 基础层 — 实现接口
package infrastructure.persistence;
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    private final OrderMapper mapper;
    // 实现...
}
```

## 服务编排模式

```
应用服务 (粗粒度)
  ├── 领域服务A (细粒度)
  │     ├── 实体方法1
  │     └── 实体方法2
  ├── 领域服务B
  │     └── 实体方法3
  └── 仓储接口 (数据持久化)
```

## 服务演进

```
初始：领域服务 a, b, c 各自独立
  ↓ 多次编排后发现 b+c 总是同一组合
优化：合并为新领域服务 (b+c)
  ↓ 应用层编排简化
结果：领域模型越来越精炼
```

## 以聚合为单位的架构演进

```
微服务 1:
├── 聚合 A (热点，拖累整体性能)
├── 聚合 B
└── 聚合 C

演进 ↓

微服务 1:              微服务 2 (独立):
├── 聚合 B              └── 聚合 A (独立部署，独立扩容)
└── 聚合 C
```

## 常见错误

| 错误 | 纠正 |
|------|------|
| 应用层写业务逻辑 | 应用层只编排，if/else 业务判断在领域层 |
| 领域层 import Spring/JPA | 领域层零框架依赖 |
| Controller 直接调 Repository | 必须经过完整调用链 |
| 仓储接口放基础层 | 接口在领域层，实现才放基础层 |
