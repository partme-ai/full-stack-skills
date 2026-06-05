# 08 — Comparison: Onion vs Hexagonal vs Clean Architecture

> 洋葱、六边形、整洁架构都是领域中心架构模式，本文件对比三者差异以辅助选型。

## 核心思想对比

| 维度 | 洋葱架构 | 六边形架构 | 整洁架构 |
|------|---------|-----------|---------|
| **提出者** | Jeffrey Palermo (2008) | Alistair Cockburn (2005) | Robert C. Martin (2012) |
| **心智模型** | 同心圆（如洋葱切片） | 六边形 + 端口/适配器 | 四圈层 + 依赖规则 |
| **核心隐喻** | 层嵌套层，依赖指向圆心 | 端口提供抽象，适配器对接外部 | 越靠近中心越抽象，越稳定 |
| **层数** | 3-4 层 | 2 层（内六边形 + 外六边形） | 4 层 |
| **接口组织** | 按层（Domain 定义 Repository） | 按端口（inbound/outbound） | 按用例（I/O UseCase Port） |

## 层结构对比

### 洋葱架构

```
Infrastructure (最外层)
  └── API / Adapters
       └── Application
            └── Domain (核心，零依赖) ★
```

**关键特征**：
- Application 服务和接口在 Core 层定义
- API 和 Infrastructure 是独立的外层模块
- Composition Root 是第 4 个独立模块

### 六边形架构

```
         [Driving Adapters]         [Driven Adapters]
         HTTP / CLI / gRPC          DB / MQ / External
              │                          │
              ▼                          ▼
         ┌──────────────────────────────────────┐
         │       Application + Domain Core       │
         │    (内六边形：纯业务逻辑 + 端口)         │
         └──────────────────────────────────────┘
```

**关键特征**：
- 入站端口（UseCase 接口）+ 出站端口（Repository 接口）
- 适配器在外层实现端口
- 端口明确分为 driving 和 driven

### 整洁架构

```
Frameworks & Drivers (最外层)
  └── Interface Adapters
       └── Application Business Rules (Use Cases)
            └── Enterprise Business Rules (Entities) ★
```

**关键特征**：
- 四层命名不同：Entities / Use Cases / Adapters / Frameworks
- Use Cases 是核心组织单元
- Interface Adapters 负责 Controller + Presenter + Gateway

## 目录结构对比

### 洋葱架构目录

```
order-core/
  domain/model/       # 实体、值对象
  domain/repository/  # 仓储接口
  domain/service/     # 领域服务
  domain/event/       # 领域事件
  application/service/# 应用服务接口
order-infrastructure/
  data/repository/    # 仓储实现
  messaging/          # MQ 实现
  external/           # 外部 API
order-api/
  controller/         # REST 控制器
  dto/                # 请求/响应
  assembler/          # 转换器
order-composition/
  config/             # DI 配置
```

### 六边形架构目录

```
domain/
  model/              # 实体、值对象
  port/inbound/       # 入站端口 (UseCase 接口)
  port/outbound/      # 出站端口 (Repository 接口)
  service/            # 领域服务
application/
  service/            # UseCase 实现
adapter/inbound/
  web/                # REST Controller
  cli/                # 命令行
  event/              # 事件监听
adapter/outbound/
  persistence/        # DB 实现
  messaging/          # MQ 实现
  external/           # 外部 API
configuration/
  config/             # DI 配置
```

### 整洁架构目录

```
entity/               # 企业业务规则（核心实体）
usecase/
  port/input/         # 入站端口
  port/output/        # 出站端口
  interactor/         # Use Case 实现
  dto/                # Use Case 专用 DTO
adapter/
  controller/         # 控制器
  presenter/          # 响应格式化
  repository/         # Repository 实现
  gateway/            # 外部服务实现
framework/
  config/             # DI + 框架配置
  persistence/        # JPA Entity
  web/                # CORS, Security
```

## 选型决策树

```
你的场景是？
├── 团队喜欢"层嵌套"的直观可视化
│   └── → 洋葱架构（适合领域复杂、多入口系统）
│
├── 团队习惯"端口+适配器"的接口抽象
│   └── → 六边形架构（适合 API 集成多的微服务）
│
├── 需要严格按用例组织代码
│   └── → 整洁架构（适合企业级大型系统）
│
├── 国内企业 Spring Boot + MyBatis 技术栈
│   └── → COLA（阿里系，社区成熟）
│
└── 简单 CRUD，小团队快速迭代
    └── → 传统分层架构（避免过度设计）
```

## 优缺点矩阵

| 特性 | 洋葱 | 六边形 | 整洁 |
|------|:---:|:-----:|:---:|
| 学习曲线 | ★★☆ | ★★★ | ★★★ |
| 可视化清晰度 | ★★★ | ★★☆ | ★★☆ |
| 接口抽象度 | ★★☆ | ★★★ | ★★★ |
| 多入口适应性 | ★★★ | ★★★ | ★★☆ |
| 测试友好度 | ★★★ | ★★★ | ★★★ |
| 基础设施替换性 | ★★★ | ★★★ | ★★☆ |
| 社区案例 | ★★☆ | ★★★ | ★★★ |
| 国内流行度 | ★☆☆ | ★★☆ | ★★☆ |
| 过度设计风险 | ★★☆ | ★★★ | ★★★ |

## 选型建议

| 项目类型 | 推荐架构 | 理由 |
|---------|---------|------|
| 电商核心交易 | 洋葱 | 领域复杂，需要清晰的层隔离 |
| 微服务 API 网关 | 六边形 | 多入口适配，端口抽象天然匹配 |
| 企业 ERP 系统 | 整洁 | 用例驱动，适合大型团队分工 |
| 国内中台项目 | COLA | 社区成熟，脚手架完善 |
| 快速原型 | 分层 | 简单高效，避免过度设计 |

## 三种架构的共同点

1. **领域模型为中心** — 业务逻辑在核心层
2. **依赖倒置** — 外层依赖内层，内层不依赖外层
3. **基础设施可替换** — 通过接口隔离技术细节
4. **高可测试性** — 核心层可脱离框架独立测试
5. **关注点分离** — 各层职责清晰，互不干扰
