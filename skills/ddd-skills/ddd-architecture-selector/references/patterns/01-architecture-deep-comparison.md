# 三种架构对比深度解析


## 执行摘要

| 架构 | 核心思想 | 适用场景 |
|------|---------|---------|
| **六边形** | 端口与适配器，核心不依赖外部 | 多入口系统、高可测性 |
| **整洁** | 依赖只指向内圈（实体→用例→适配器→框架） | 大型企业、严格隔离 |
| **COLA** | 菱形四层 + Command/DTO/Assembler/SPI | 国内工程化落地 |

## 选型 CheckList

| 场景 | 推荐 |
|------|------|
| 纯 CRUD/报表/管理后台 | 传统分层或轻量 DDD |
| 核心域/复杂规则/多集成 | 六边形或整洁优先 |
| 阿里系/工程化落地 | COLA（菱形） |
| 强变化的外设（DB/UI/队列/三方） | 六边形最"抗变化" |

## 六边形架构关键点

**结构**：入站适配器(HTTP/CLI/GRPC) → 入站端口 → 应用服务 → 领域模型 → 出站端口 → 出站适配器(DB/MQ/三方)

**优点**：高可测试、抗框架变化、天然契合 DDD

**代价**：端口过多导致过度抽象、DTO/Assembler 映射成本

## 整洁架构关键点

**圈层对照 DDD**：
- Entities ≈ DDD 聚合/实体/值对象
- Use Cases ≈ 应用服务
- Interface Adapters ≈ Controller/Presenter/Gateway
- Frameworks ≈ Web 框架/DB/消息

**常见陷阱**：用例贫血化（只当"转发器"）、圈层滥用

## COLA 关键点

**工程约定**：adapter.web / app / domain / infra 四层

**Command/Query**：明确用例输入，可观测、可审计

**Assembler**：DTO ⇆ DO/Entity 映射集中管理

**SPI 扩展点**：方便替换/灰度

## 迁移路径（从 MVC/贫血到 DDD/充血）

1. 识别限界上下文与聚合
2. 提取值对象（Money → Email → PhoneNumber）
3. 把业务规则从 Service 搬到 Entity（充血）
4. 引入 Repository 接口（Domain 定义，Infra 实现）
5. 用领域事件替代直接 Service 调用（跨聚合）
6. 把 Controller 变成薄适配器

## DTO/VO/DO 的边界

| 对象 | 全称 | 位置 | 职责 |
|------|------|------|------|
| DO | Domain Object | Domain 层 | 充血模型，含业务行为 |
| DTO | Data Transfer Object | Application/Adapter | 跨层/跨服务传输 |
| VO | View Object | Adapter 层 | 面向页面展示 |
| PO | Persistent Object | Infrastructure | 数据库映射 |

## 源代码

