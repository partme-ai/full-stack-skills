# FAQ

**Q1: 团队5人和50人的架构选择逻辑有什么本质区别？**
A: 5人团队核心痛点是"快速交付"，推荐 Layered 或 COLA 简化版。50人团队核心痛点是"协调成本"，推荐 Clean 或多模块 COLA 实现物理隔离。

**Q2: CQRS 一定要和 Hexagonal/Clean 搭配吗？**
A: 理论上可以独立使用，但实践中 CQRS L2+（DB 分离）涉及同步机制（领域事件 → MQ → Query DB），只有 Hexagonal 或 Clean 的端口隔离能干净处理这种复杂度。Layered 搭配 CQRS 容易导致架构混乱。

**Q3: 同一个项目里多个模块可以用不同架构吗？**
A: 可以。微服务架构下每个服务独立选型完全合理。COLA 官方也支持"Domain + App + Adapter + Infra"四层的模块级差异化。关键是定义好模块间的通信契约。

**Q4: 有没有推荐的从 Layered 到 Hexagonal 的渐进迁移路径？**
A: 推荐三步：Phase 1 在现有 Layered 中识别聚合边界，Phase 2 引入 Repository 接口（依赖倒置），Phase 3 逐步将 Service 层重构为 UseCase + Port。整个迁移使用 Strangler Fig 模式，不需要重写。

**Q5: COLA 和 Clean Architecture 的核心区别是什么？**
A: COLA 更工程化（有脚手架、代码生成、ArchUnit 自动化检查），Clean 更学术化（强调 Entity → UseCase 的层次纯度）。COLA 适合国内 Spring Boot 团队，Clean 适合国际化大型团队。

**Q6: 微服务拆分粒度太细或太粗怎么办？**
A: 太细 → 合并事务边界（2个服务需要强一致性 → 合并）。太粗 → 按部署节奏和团队归属拆分。基本原则：一个 BC 一个服务，BC 大小由领域事件流自然界定。

**Q7: 我该先选架构还是先做领域建模？**
A: 先选架构再建模。架构类别（Layered/Hexagonal）决定了代码组织方式，领域建模结果（聚合/限界上下文）填入架构框架中。推荐路径：selector → domain-designer → 对应架构 Skill。

**Q8: Onion 和 Hexagonal 到底有什么区别？实际选哪个？**
A: 两者本质上是同一思想的不同表述。Onion 更强调"层次嵌套"（可视化直观），Hexagonal 更强调"端口/适配器"（接口契约清晰）。建议：如果是教学/团队展示 → Onion；如果是代码落地 → Hexagonal。

**Q9: 我的团队全是新手，能用 Hexagonal 吗？**
A: 不建议。Hexagonal 需要团队理解 Port/Adapter、UseCase 接口、依赖倒置等概念。新手团队从 Layered 或 COLA 简化版开始，待团队 DDD 成熟后再升级。至少需要有 1-2 名有 DDD 经验的成员才能成功落地 Hexagonal。

**Q10: 选型时团队规模和业务复杂度冲突怎么办？（比如小团队做复杂业务）**
A: 优先处理业务复杂度。小团队做复杂业务时推荐 COLA（有脚手架减少样板代码）或 Hexagonal（领域层纯净度保证复杂逻辑不被基础设施污染）。不推荐 Layered（容易退化为"大泥球"）和 Clean（模块太多）。

**Q11: 非 Java 技术栈怎么选？**
A: COLA 是 Java 专有，其他 4 种架构语言无关。推荐：Python/Django → Layered 或 Hexagonal；Go → Hexagonal（接口友好）；.NET → Onion（.NET 社区 Onion 生态好）；Node.js → Hexagonal 或 Clean。

**Q12: 我在做微服务架构，每个服务内部的架构需要统一吗？**
A: 不需要统一，但建议标准化 2-3 种模式。典型策略：Core 域服务用 Hexagonal 或 Clean，Generic 域服务用 Layered，制定"架构选择手册"确保团队遵循。

**Q13: 有没有"绝对不要选"的架构？**
A: 对于新项目，没有绝对错误的架构，只有不匹配的架构。但在以下情况要特别谨慎：团队 < 3 人选 Clean（过度设计）；非 Java 人选 COLA（框架依赖）；简单 CRUD 选 Hexagonal（性价比低）；团队无 DDD 经验选 Onion（抽象门槛高）。

**Q14: ArchUnit 必须用吗？有没有轻量替代？**
A: 大型项目 (> 10人) → 必须用 ArchUnit 或类似工具（.NET 用 NetArchTest，Go 用 go-arch-lint）。小型项目 → 可以用目录命名约定 + PR Review Checklist 替代。但建议从 Day 1 开启，后期补充的修复成本更高。

**Q15: 选型完成后，多久应该重新评估一次？**
A: 建议两种触发条件：(1) 时间触发 — 每 6 个月做一次架构适配度评估；(2) 事件触发 — 团队规模翻倍、业务复杂度跃升、基础设施大换血时立即重新评估。使用 `ddd-architecture-evaluator` 进行评估。
