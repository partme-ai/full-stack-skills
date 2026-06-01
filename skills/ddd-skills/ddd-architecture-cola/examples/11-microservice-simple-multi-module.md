# COLA 项目规模示例：微服务简单的多模块项目

> 适用场景：微服务架构，每个业务服务内部采用 Maven 多模块 COLA 结构，业务简单但对架构约束有高要求，基于 ddd4j-rednote 真实结构。

## 参考项目

本示例基于真实项目 `ddd4j-rednote`（`io.ddd4j.rednote:ddd4j-rednote`）的结构提取。

## 项目目录树

```
ddd4j-rednote/                                      # 父 POM, packaging=pom
├── pom.xml                                         # 继承 ddd4j-boot-parent, modules=4
│   <modules>
│     <module>ddd4j-rednote-bom</module>
│     <module>ddd4j-rednote-dependencies</module>
│     <module>ddd4j-rednote-api</module>
│     <module>ddd4j-rednote-common</module>
│   </modules>
│
├── ddd4j-rednote-bom/                              # BOM (Bill of Materials)
│   └── pom.xml                                     # 统一版本管理, packaging=pom
│
├── ddd4j-rednote-dependencies/                     # 依赖管理
│   └── pom.xml                                     # 集中管理外部依赖版本, packaging=pom
│
├── ddd4j-rednote-api/                              # 业务接口模块 (聚合子模块)
│   ├── pom.xml                                     # packaging=pom, modules=5
│   │   <modules>
│   │     <module>ddd4j-rednote-api-adapter</module>
│   │     <module>ddd4j-rednote-api-client</module>
│   │     <module>ddd4j-rednote-api-app</module>
│   │     <module>ddd4j-rednote-api-domain</module>
│   │     <module>ddd4j-rednote-api-infrastructure</module>
│   │   </modules>
│   │
│   ├── ddd4j-rednote-api-adapter/                  # 适配层
│   │   ├── pom.xml                                 # 依赖 api-app, api-domain
│   │   └── src/main/java/io/ddd4j/rednote/api/
│   │       └── adapter/
│   │           └── ...                             # Controller / RPC / DTO
│   │
│   ├── ddd4j-rednote-api-client/                   # 客户端 SDK
│   │   ├── pom.xml                                 # 依赖 api-domain (仅接口)
│   │   └── src/main/java/io/ddd4j/rednote/api/
│   │       └── client/
│   │           └── ...                             # Feign Client / Dubbo 接口
│   │
│   ├── ddd4j-rednote-api-app/                      # 应用层
│   │   ├── pom.xml                                 # 依赖 api-domain, api-infrastructure
│   │   └── src/main/java/io/ddd4j/rednote/api/
│   │       └── app/
│   │           └── ...                             # Executor / Service / Assembler
│   │
│   ├── ddd4j-rednote-api-domain/                   # 领域层 ★
│   │   ├── pom.xml                                 # 零外部依赖
│   │   └── src/main/java/io/ddd4j/rednote/api/
│   │       └── domain/
│   │           └── ...                             # Entity / VO / Repository 接口
│   │
│   └── ddd4j-rednote-api-infrastructure/           # 基础设施层
│       ├── pom.xml                                 # 依赖 api-domain, common-infrastructure
│       └── src/main/java/io/ddd4j/rednote/api/
│           └── infrastructure/
│               └── ...                             # RepositoryImpl / Mapper / PO
│
└── ddd4j-rednote-common/                           # 公共模块 (聚合子模块)
    ├── pom.xml                                     # packaging=pom, modules=2
    │   <modules>
    │     <module>ddd4j-rednote-common-domain</module>
    │     <module>ddd4j-rednote-common-infrastructure</module>
    │   </modules>
    │
    ├── ddd4j-rednote-common-domain/                # 公共领域对象
    │   ├── pom.xml                                 # 零外部依赖
    │   └── src/main/java/io/ddd4j/rednote/common/
    │       └── domain/
    │           └── ...                             # 共享值对象、公共枚举
    │
    └── ddd4j-rednote-common-infrastructure/        # 公共基础设施
        ├── pom.xml                                 # 依赖 common-domain
        └── src/main/java/io/ddd4j/rednote/common/
            └── infrastructure/
                └── ...                             # 公共配置、工具类、组件
```

## 模块结构总结

ddd4j-rednote 采用**三级模块层级**：

```
Level 1: ddd4j-rednote (父 POM)
├── Level 2: ddd4j-rednote-bom           (版本管理)
├── Level 2: ddd4j-rednote-dependencies  (依赖管理)
├── Level 2: ddd4j-rednote-api           (业务接口聚合)
│   ├── Level 3: ddd4j-rednote-api-adapter
│   ├── Level 3: ddd4j-rednote-api-client        ← 特有模块：给其他服务用的 SDK
│   ├── Level 3: ddd4j-rednote-api-app
│   ├── Level 3: ddd4j-rednote-api-domain
│   └── Level 3: ddd4j-rednote-api-infrastructure
└── Level 2: ddd4j-rednote-common        (公共模块聚合)
    ├── Level 3: ddd4j-rednote-common-domain
    └── Level 3: ddd4j-rednote-common-infrastructure
```

总计 10 个 Maven 模块（含 pom 类型）。

## 各模块的包结构说明

| Level 2 模块 | Level 3 模块 | 包路径 | 职责 |
|-------------|-------------|--------|------|
| `rednote-bom` | — | — | 统一管理所有模块版本号 |
| `rednote-dependencies` | — | — | 集中管理外部依赖版本 (scope=import) |
| `rednote-api` | `rednote-api-adapter` | `io.ddd4j.rednote.api.adapter` | REST/RPC 适配 |
| `rednote-api` | `rednote-api-client` | `io.ddd4j.rednote.api.client` | 其他微服务调用本服务的 Feign/Dubbo 接口 |
| `rednote-api` | `rednote-api-app` | `io.ddd4j.rednote.api.app` | 用例编排 + CQRS |
| `rednote-api` | `rednote-api-domain` | `io.ddd4j.rednote.api.domain` | 核心领域对象 + Repository 接口 |
| `rednote-api` | `rednote-api-infrastructure` | `io.ddd4j.rednote.api.infrastructure` | 持久化 + 外部调用实现 |
| `rednote-common` | `rednote-common-domain` | `io.ddd4j.rednote.common.domain` | 跨微服务共享的值对象、枚举 |
| `rednote-common` | `rednote-common-infrastructure` | `io.ddd4j.rednote.common.infrastructure` | 共享配置、工具类 |

**核心理念**：`rednote-api-client` 模块是本项目的关键设计——它为其他微服务提供**零依赖领域接口**的 SDK，调用方只需依赖 client 模块即可调用本服务。

## COLA 四层职责分工

| 层 | 对应模块 | 职责 | 微服务环境特点 |
|----|---------|------|--------------|
| **Adapter** | `api-adapter` | HTTP/RPC 适配入口 | 同时提供 REST 和 Dubbo 协议 |
| **Application** | `api-app` | 用例编排 | 可依赖 common-infrastructure 使用共享组件 |
| **Domain** ★ | `api-domain` + `common-domain` | 核心领域 + 共享值对象 | `api-domain` 依赖 `common-domain`（唯一允许的领域间依赖） |
| **Infrastructure** | `api-infrastructure` + `common-infrastructure` | 持久化 + 共享工具 | 共享基础设施减少重复代码 |

## 模块间依赖关系图

```
ddd4j-rednote-bom ──────────────────────────────────────────────┐
ddd4j-rednote-dependencies ─────────────────────────────────────┤
                                                                 │
┌────────────────────────────────────────────────────────────────┤
│                        rednote-api                             │
│                                                                 │
│  ┌──────────────────────┐                                      │
│  │   api-adapter         │                                     │
│  │   (REST/RPC 入口)     │                                     │
│  └───────┬──────────────┘                                     │
│          │ depends                                              │
│          ▼                                                     │
│  ┌──────────────────────┐                                      │
│  │   api-app             │───── depends ────┐                  │
│  │   (用例编排)           │                  │                   │
│  └───────┬──────────────┘                  │                   │
│          │ depends                          │                   │
│          ▼                                 │                   │
│  ┌──────────────────────┐                  ▼                   │
│  │   api-domain  ★       │   ┌──────────────────────┐         │
│  │   (核心领域)           │   │  api-infrastructure  │         │
│  └───────┬──────────────┘   │  (持久化实现)         │         │
│          │ depends           └──────────────────────┘         │
│          ▼                                                      │
│  ┌──────────────────────┐                                      │
│  │   api-client          │← 其他微服务依赖此模块                       │
│  │   (对外 SDK)           │                                      │
│  └──────────────────────┘                                      │
│                                                                 │
├────────────────────────────────────────────────────────────────┤
│                       rednote-common                           │
│                                                                 │
│  ┌──────────────────────┐     ┌──────────────────────────────┐ │
│  │ common-domain         │     │ common-infrastructure        │ │
│  │ (共享值对象)           │──→  │ (共享配置/工具)               │ │
│  └──────────────────────┘     └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**关键依赖规则**：
- `api-domain` → `common-domain`（领域层共享值对象）
- `api-infrastructure` → `common-infrastructure`（共享技术组件）
- `api-client` → `api-domain`（对外 SDK 仅暴露领域对象，不暴露基础设施）
- `common-infrastructure` → `common-domain`（基础设施依赖领域）

## 适用场景

- 微服务数量较多 (5+)，需要一个服务提供 SDK 给其他服务调用
- 需要 Maven 编译时强制依赖约束
- 团队 5-15 人，对代码质量要求高
- 有跨微服务共享的公共值对象和工具
- BOM + Dependencies 统一管理全项目依赖版本

## ddd4j-rednote 的设计精髓

1. **BOM + Dependencies 双重版本管理**：BOM 管理模块版本，Dependencies 管理外部依赖版本
2. **Client 模块**：为其他微服务提供类型安全的调用 SDK，避免硬编码 URL
3. **Common 分层**：Common 也按 Domain/Infrastructure 拆分，保持架构一致性
4. **三级模块层级**：Parent → API/Common → COLA 四层，结构清晰

## 优点

- 编译时依赖约束（Maven 模块级隔离，比 ArchUnit 更早发现问题）
- Client 模块让其他服务调用方无需了解内部实现
- BOM + Dependencies 统一版本管理，避免依赖冲突
- Common 模块按分层拆分，避免 common 变"垃圾桶"
- 每个微服务可独立发布 Client 模块给依赖方

## 缺点

- 10 个 Maven 模块增加构建复杂度
- 新手需要理解模块间的依赖关系
- 模块间接口变化影响范围大
- BOM/Dependencies 维护需要专人负责
