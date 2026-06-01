# 每种架构的详细决策指南

## Layered Architecture — 详细选型

### 核心问题
> "我已有三层架构的项目，想引入 DDD，但不想大改。怎么选？"

### 决策路径
```
你的项目是否已有三层架构？
├── 是 → 直接用 Layered，把 Service 层拆成 Application + Domain
│        Interface 层保持不变，Infrastructure 层单独抽出来
│
└── 否 → 你的团队对 DDD 的理解程度？
    ├── 刚接触 → Layered（学习曲线最低，和三层最像）
    ├── 有经验 → 考虑 Onion 或 COLA
    └── 专家 → 跳到 Hexagonal 或 Clean
```

### 升级路径
```
Layered → 业务更复杂 → Onion（加内外层隔离）
Layered → 多入口 → Hexagonal（引入端口/适配器）
Layered → 国内团队扩编 → COLA（引入工程规范+ArchUnit）
```

### 关键约束
- Domain 层零依赖（无 Spring/JPA/MyBatis）
- App 层只编排，不写业务逻辑
- 事务边界在 App 层

---

## Onion Architecture — 详细选型

### 核心问题
> "我想让领域模型彻底独立，基础设施可以随时换。选哪个？"

### 决策路径
```
你是否需要频繁切换基础设施（DB、MQ、缓存）？
├── 是 → 你的团队能否设计好接口？
│   ├── 能 → Onion（内层定义接口，外层实现）
│   └── 不能 → 先学接口设计，用 Layered 过渡
│
└── 否 → 基础设施稳定吗？
    ├── 稳定 → 不需要 Onion 的复杂度，用 Layered 或 COLA
    └── 不确定 → Onion 或 Hexagonal 都行（Hexagonal 更规范）
```

### 与六边形/整洁的区别
- Onion 更强调"层次嵌套"：Domain ⊂ Application ⊂ Infrastructure
- Hexagonal 更强调"端口/适配器"的接口抽象
- Clean 更强调"用例 + 实体"的业务规则分离
- 三者本质同源——选你团队最习惯的术语体系

### 关键约束
- 内层定义接口，外层实现接口
- 所有依赖指向圆心（Domain）
- Composition 层负责 DI 组装所有层

---

## Hexagonal Architecture — 详细选型

### 核心问题
> "我的系统有 REST API、CLI 工具、MQ 消费者、定时任务……多个入口。怎么统一？"

### 决策路径
```
你的系统有几个"入口"（外部如何调用你的系统）？
├── 1 个（只有 REST API）
│   └── 未来会增加吗？
│       ├── 不会 → 不需要 Hexagonal，用 Layered 或 COLA
│       └── 会 → Hexagonal 提前布局端口/适配器
│
├── 2+ 个（REST + CLI + MQ + gRPC 等）
│   └── Hexagonal 是最佳选择
│       每个入口一个 Adapter，核心逻辑完全复用
│
└── 需要极高的测试覆盖率？
    └── Hexagonal 端口 Mock 测试天然支持
```

### 端口粒度原则
- 入站端口：一个 UseCase 一个接口（`CreateOrderUseCase`, `PayOrderUseCase`）
- 出站端口：一个外部依赖一个接口（`OrderRepository`, `PaymentGateway`, `NotificationPort`）
- 不要为"未来可能"创建端口——等实际需要时再抽

### 设计验证
> "如果不用数据库和 HTTP 就能跑通领域逻辑的单元测试，你的六边形边界就对了。" — Alistair Cockburn

---

## Clean Architecture — 详细选型

### 核心问题
> "大型企业项目，需要严格模块物理隔离。团队 15-50 人。选什么？"

### 决策路径
```
你的项目是否需要"物理模块隔离"（不是逻辑上的分层，而是 Maven/Gradle 模块级隔离）？
├── 是 → Clean Architecture
│        Enterprise / UseCase / Adapter / Framework 四个独立模块
│        编译时强制依赖方向
│
└── 否 → 考虑 COLA 或 Layered
    （逻辑分层就够了，不需要物理模块隔离的代价）
```

### 四层映射到 Maven 模块
```
{project}-core/          → Enterprise Business Rules（零依赖）
{project}-usecase/       → Application Business Rules（只依赖 core）
{project}-adapter/       → Interface Adapters（依赖 usecase + core）
{project}-framework/     → Frameworks & Drivers（依赖以上全部）
```

### 常见陷阱
- **用例贫血化**：UseCase 只当"转发器"，实际逻辑散落在外层
- **圈层滥用**：所有类都"按圈放"，但业务边界不清晰
- **过度隔离**：简单 CRUD 也拆四个模块，开发和构建变慢

---

## COLA v5 — 详细选型

### 核心问题
> "国内团队，Spring Boot + MyBatis 技术栈，想要标准化工程规范。选什么？"

### 决策路径
```
你的技术栈是 Spring Boot + MyBatis 吗？
├── 是 → 团队熟悉 DDD 吗？
│   ├── 不熟悉 → COLA（脚手架帮你建好项目，跟着规范走）
│   ├── 部分熟悉 → COLA（ArchUnit 自动化检查，不会走偏）
│   └── 非常熟悉 → COLA 或 Hexagonal（看是否需要多入口）
│
└── 否（Go/Rust/Python/Node.js）
    └── 不要选 COLA（它是 Java 专属的）
        → 选 Hexagonal 或 Clean（语言无关）
```

### COLA 独有优势
1. **脚手架生成**：一键创建完整项目骨架
2. **ArchUnit 自动检查**：CI/CD 集成，P0 违规阻止合并
3. **CQRS 原生支持**：CommandExe + QueryExe 独立目录
4. **扩展点机制**：SPI 模式，方便灰度和替换

### COLA 不如其他架构的地方
1. 非 Java 项目无法使用
2. 学习成本比 Layered 高（4 模块 + Command/Query 分离）
3. 不适合只有 1-2 人的小团队
