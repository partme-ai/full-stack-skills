# COLA 项目规模示例：微服务复杂的多模块项目

> 适用场景：大型微服务系统，多个业务域（如支付-API 和支付-Admin），每个业务域内部 Maven 多模块 COLA 结构，15-50 人团队，基于 ddd4j-pay 真实结构。

## 参考项目

本示例基于真实项目 `ddd4j-pay`（`io.ddd4j.pay:ddd4j-pay`）的结构提取。

## 项目目录树

```
ddd4j-pay/                                            # 父 POM, packaging=pom
├── pom.xml                                           # 继承 ddd4j-boot-parent, modules=5
│   <modules>
│     <module>ddd4j-pay-bom</module>
│     <module>ddd4j-pay-dependencies</module>
│     <module>ddd4j-pay-api</module>
│     <module>ddd4j-pay-admin</module>
│     <module>ddd4j-pay-common</module>
│   </modules>
│
├── ddd4j-pay-bom/                                    # BOM
│   └── pom.xml                                       # 统一版本管理
│
├── ddd4j-pay-dependencies/                           # 依赖管理
│   └── pom.xml                                       # 集中管理外部依赖版本
│
├── ddd4j-pay-api/                                    # 支付对外接口域 (Level 2)
│   ├── pom.xml                                       # packaging=pom, modules=5
│   │   <modules>
│   │     <module>ddd4j-pay-api-adapter</module>
│   │     <module>ddd4j-pay-api-client</module>
│   │     <module>ddd4j-pay-api-app</module>
│   │     <module>ddd4j-pay-api-domain</module>
│   │     <module>ddd4j-pay-api-infrastructure</module>
│   │   </modules>
│   │
│   ├── ddd4j-pay-api-adapter/                        # 支付 API 适配层
│   │   └── src/main/java/io/ddd4j/pay/api/
│   │       └── adapter/
│   │           └── ...                               # 支付接口 Controller / RPC
│   │
│   ├── ddd4j-pay-api-client/                         # 支付 API 客户端 SDK
│   │   └── src/main/java/io/ddd4j/pay/api/
│   │       └── client/
│   │           └── ...                               # Feign Client / 调用接口
│   │
│   ├── ddd4j-pay-api-app/                            # 支付 API 应用层
│   │   └── src/main/java/io/ddd4j/pay/api/
│   │       └── app/
│   │           └── ...                               # 支付流程编排 / 对账 / 退款
│   │
│   ├── ddd4j-pay-api-domain/                         # 支付 API 领域层 ★
│   │   └── src/main/java/io/ddd4j/pay/api/
│   │       └── domain/
│   │           └── ...                               # Payment / Refund / Transaction
│   │
│   └── ddd4j-pay-api-infrastructure/                 # 支付 API 基础设施层
│       └── src/main/java/io/ddd4j/pay/api/
│           └── infrastructure/
│               └── ...                               # 支付网关接入 / 银行接口 / 证书管理
│
├── ddd4j-pay-admin/                                  # 支付管理后台域 (Level 2)
│   ├── pom.xml                                       # packaging=pom, modules=5
│   │   <modules>
│   │     <module>ddd4j-pay-admin-adapter</module>
│   │     <module>ddd4j-pay-admin-client</module>
│   │     <module>ddd4j-pay-admin-app</module>
│   │     <module>ddd4j-pay-admin-domain</module>
│   │     <module>ddd4j-pay-admin-infrastructure</module>
│   │   </modules>
│   │
│   ├── ddd4j-pay-admin-adapter/                      # Admin 适配层
│   │   └── src/main/java/io/ddd4j/pay/admin/
│   │       └── adapter/
│   │           └── ...                               # 管理后台 Controller
│   │
│   ├── ddd4j-pay-admin-client/                       # Admin 客户端 SDK
│   │   └── src/main/java/io/ddd4j/pay/admin/
│   │       └── client/
│   │           └── ...                               # Admin 调用接口
│   │
│   ├── ddd4j-pay-admin-app/                          # Admin 应用层
│   │   └── src/main/java/io/ddd4j/pay/admin/
│   │       └── app/
│   │           └── ...                               # 商户管理 / 费率配置 / 风控
│   │
│   ├── ddd4j-pay-admin-domain/                       # Admin 领域层 ★
│   │   └── src/main/java/io/ddd4j/pay/admin/
│   │       └── domain/
│   │           └── ...                               # Merchant / FeeRule / RiskRule
│   │
│   └── ddd4j-pay-admin-infrastructure/               # Admin 基础设施层
│       └── src/main/java/io/ddd4j/pay/admin/
│           └── infrastructure/
│               └── ...                               # 商户数据持久化 / 风控引擎
│
├── ddd4j-pay-common/                                 # 公共模块 (Level 2)
│   ├── pom.xml                                       # packaging=pom, modules=2
│   │   <modules>
│   │     <module>ddd4j-pay-common-domain</module>
│   │     <module>ddd4j-pay-common-infrastructure</module>
│   │   </modules>
│   │
│   ├── ddd4j-pay-common-domain/                      # 公共领域对象
│   │   └── src/main/java/io/ddd4j/pay/common/
│   │       └── domain/
│   │           └── ...                               # Money / Currency / PayChannel 枚举
│   │
│   └── ddd4j-pay-common-infrastructure/              # 公共基础设施
│       └── src/main/java/io/ddd4j/pay/common/
│           └── infrastructure/
│               └── ...                               # 分布式锁 / 幂等组件 / 日志
│
├── libs/                                             # 本地 jar 依赖 (如银行 SDK)
├── docs/                                             # 文档
│   └── icons/
└── ...
```

## 模块完整层级结构

```
ddd4j-pay (父 POM)
├── Level 2: ddd4j-pay-bom               — BOM 版本管理
├── Level 2: ddd4j-pay-dependencies      — 外部依赖版本管理
├── Level 2: ddd4j-pay-api               — 支付接口域 (5 个 Level 3 子模块)
├── Level 2: ddd4j-pay-admin             — 管理后台域 (5 个 Level 3 子模块)
└── Level 2: ddd4j-pay-common            — 公共模块 (2 个 Level 3 子模块)
                                               │
            ┌──────────────────────────────────┘
            ▼
    总计 14 个 Maven 模块 (含 pom 类型)
```

**两层业务域**：
- `ddd4j-pay-api`：面向 C 端用户/商户的支付接口（下单、支付、退款、查询）
- `ddd4j-pay-admin`：面向运营/管理员的后台管理（商户管理、费率配置、风控规则）

## 各模块的包结构说明

| Level 2 模块 | Level 3 模块 | 包路径 | 职责 |
|-------------|-------------|--------|------|
| `pay-bom` | — | — | 统一管理 14 个模块版本号 |
| `pay-dependencies` | — | — | 集中管理外部依赖版本 |
| `pay-api` | `pay-api-adapter` | `io.ddd4j.pay.api.adapter` | 支付 REST/RPC 接口 |
| `pay-api` | `pay-api-client` | `io.ddd4j.pay.api.client` | 支付服务 SDK（给其他系统调用） |
| `pay-api` | `pay-api-app` | `io.ddd4j.pay.api.app` | 支付流程编排（下单/退款/对账） |
| `pay-api` | `pay-api-domain` | `io.ddd4j.pay.api.domain` | 支付核心领域（Payment/Refund/Transaction） |
| `pay-api` | `pay-api-infrastructure` | `io.ddd4j.pay.api.infrastructure` | 支付网关接入/银行接口/证书管理 |
| `pay-admin` | `pay-admin-adapter` | `io.ddd4j.pay.admin.adapter` | 管理后台 Controller |
| `pay-admin` | `pay-admin-client` | `io.ddd4j.pay.admin.client` | Admin SDK |
| `pay-admin` | `pay-admin-app` | `io.ddd4j.pay.admin.app` | 商户管理/费率/风控编排 |
| `pay-admin` | `pay-admin-domain` | `io.ddd4j.pay.admin.domain` | 商户/费率/风控领域 |
| `pay-admin` | `pay-admin-infrastructure` | `io.ddd4j.pay.admin.infrastructure` | 商户数据/风控引擎实现 |
| `pay-common` | `pay-common-domain` | `io.ddd4j.pay.common.domain` | 共享值对象（Money/Currency） |
| `pay-common` | `pay-common-infrastructure` | `io.ddd4j.pay.common.infrastructure` | 分布式锁/幂等/日志组件 |

## COLA 四层职责分工

| 层 | pay-api 职责 | pay-admin 职责 |
|----|-------------|---------------|
| **Adapter** | 支付下单/退款/查询 REST API | 商户管理/费率配置/风控规则 REST API |
| **Application** | 支付流程编排（下单→风控→扣款→通知） | 商户入驻/费率变更/风控策略编排 |
| **Domain** ★ | Payment / Refund / Transaction 核心模型 | Merchant / FeeRule / RiskRule 核心模型 |
| **Infrastructure** | 银行网关实现 / 支付回调处理 / 证书管理 | 商户数据持久化 / 风控规则引擎 / 审计日志 |

## 模块间依赖关系图

```
┌──────────────────────────────────────────────────────────────────┐
│                         ddd4j-pay-bom                             │
│                         ddd4j-pay-dependencies                    │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────┐  ┌──────────────────────────────┐│
│  │       ddd4j-pay-api         │  │      ddd4j-pay-admin         ││
│  │                             │  │                              ││
│  │  api-adapter                │  │  admin-adapter               ││
│  │     ↓                       │  │     ↓                        ││
│  │  api-app ──→ api-domain ★   │  │  admin-app ──→ admin-domain ★││
│  │     ↓                  ↑    │  │     ↓                   ↑    ││
│  │  api-infrastructure ────┘   │  │  admin-infrastructure ───┘   ││
│  │     ↓                       │  │     ↓                        ││
│  │  api-client                 │  │  admin-client                ││
│  └─────────┬───────────────────┘  └─────────┬────────────────────┘│
│            │                                 │                     │
│            │          ┌──────────┐           │                     │
│            └──────────→ common   ←──────────┘                    │
│                       │          │                                │
│                       │ common-  │                                │
│                       │ domain   │                                │
│                       │    ↓     │                                │
│                       │ common-  │                                │
│                       │ infra    │                                │
│                       └──────────┘                                │
│                                                                   │
│  关键依赖:                                                        │
│  • api-domain ──→ common-domain  (共享值对象)                     │
│  • admin-domain ──→ common-domain (共享值对象)                    │
│  • api-infrastructure ──→ common-infrastructure (共享组件)        │
│  • admin-infrastructure ──→ common-infrastructure (共享组件)      │
│  • api-app ──→ admin-client (调用管理后台服务)                    │
└──────────────────────────────────────────────────────────────────┘
```

**跨域依赖规则**：
- `pay-api` 和 `pay-admin` 是两个独立的 Bounded Context
- 它们通过 `common-*` 共享值对象和基础设施
- 两个域的应用层可以通过各自的 `client` 模块相互调用
- **严禁** `pay-api-domain` 直接依赖 `pay-admin-domain`（跨域聚合隔离）
- **严禁** 通过数据库层面实现跨域数据访问（各自独立表空间）

## 适用场景

- 大型支付/金融系统，需要严格的域隔离
- 多业务域共存（如支付接口 + 管理后台 + 对账 + 风控）
- 团队 15-50 人，按业务域分小组
- 需要 Bounded Context 级别的模块隔离
- 需要独立发布 Client SDK 给多个下游系统
- 对代码质量和架构一致性有极高要求

## 与 ddd4j-rednote 的结构对比

| 维度 | ddd4j-rednote (简单) | ddd4j-pay (复杂) |
|------|:---------------------:|:-----------------:|
| Level 2 业务域数 | 1 (api) | 2 (api + admin) |
| Level 3 子模块数 | 7 | 12 |
| 总模块数 | 10 | 14 |
| 跨域依赖 | 无 | 通过 client 相互调用 |
| Common 共享范围 | 单域内共享 | 跨域共享 |
| BOM 管理复杂度 | 低 | 中 |
| 适用团队规模 | 5-15 人 | 15-50 人 |

## 优点

- 编译时强约束：`pay-api-domain` 和 `pay-admin-domain` 完全隔离
- 每个业务域可独立发布 Client SDK
- Common 模块按 Domain/Infrastructure 分层，避免成为"大垃圾桶"
- BOM + Dependencies 统一 14 个模块的版本，避免依赖地狱
- 高粒度模块可独立测试、独立编译
- 为大团队并行开发提供清晰的模块边界

## 缺点

- 14 个 Maven 模块维护成本高
- 新人学习曲线陡峭（需要理解 API/Admin 两个域的边界）
- Client 模块的接口变化需要协调多个服务同时升级
- BOM 版本发布需要严格的版本管理流程
- 构建时间较长（14 个模块需要全部编译）
- 模块间过度拆分可能导致过早抽象
