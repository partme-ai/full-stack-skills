# COLA v5 菱形架构核心原理

## 菱形架构全景

COLA v5（Clean Object-oriented Layered Architecture）采用"菱形架构"——以 Domain 为中心，Adapter 和 Infrastructure 分居两侧：

```
          ┌──────────────┐
          │   Adapter    │  ← 适配层：HTTP、MQ、RPC 协议适配
          └──────┬───────┘
                 │
          ┌──────▼───────┐
          │   Application│  ← 应用层：编排、事务、CQRS 分流
  ┌───────┴───────┬───────┴───────┐
  ▼               ▼               ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│  Domain  │ │  Domain  │ │  Domain  │  ← 领域层：核心业务逻辑 ★
│   ★      │ │   ★      │ │   ★      │
└──────────┘ └──────────┘ └──────────┘
  ▲               ▲               ▲
  └───────────────┴───────────────┘
                 │
          ┌──────▼───────┐
          │Infrastructure│  ← 基础设施层：DB、MQ、缓存、外部 API
          └──────────────┘
```

## 四层职责

| 层 | 模块名 | 核心职责 | 依赖方向 |
|---|--------|---------|---------|
| **Adapter** | `{project}-adapter` | HTTP/RPC/MQ 协议适配，DTO 转换 | → app, domain |
| **Application** | `{project}-app` | 用例编排，事务管理，CQRS 执行器 | → domain, infrastructure |
| **Domain** | `{project}-domain` | 领域模型、业务规则、Repository/Gateway 接口 | 无（零依赖） |
| **Infrastructure** | `{project}-infrastructure` | 技术实现（DB/MQ/缓存）、Repository/Gateway 实现 | → domain |

## 四大核心约束（P0）

1. **Domain 零依赖** — Domain 层不允许 import Spring/JPA/MyBatis 等框架注解
2. **App 层无业务逻辑** — App 层仅编排，不放 if/else 业务判断
3. **Adapter 层无 SQL/业务** — Adapter 只做协议转换和数据映射
4. **模块间无循环依赖** — 四层之间只允许单向依赖

## 依赖方向规则

```
adapter → app → domain ← infrastructure
                        ↑
                    domain 不依赖任何人
```

## v5 新增概念

- **Extension Point（扩展点）**：通过 `@ExtensionPoint` + `@Extension(bizId = "...")` 实现业务维度的扩展
- **Ability（领域能力）**：`domain/ability/` 为领域层提供能力抽象
- **组件化基础设施**：分布式锁、限流器、熔断器作为基础设施组件
- **CQRS 强化**：`app/executor/command/` 和 `app/executor/query/` 严格分离
