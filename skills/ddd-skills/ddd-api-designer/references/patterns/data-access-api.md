# Data Access Layer API 设计原则

DAO 层接口设计：

- **Repository 隔离**：领域 Repository 接口定义在 Domain 层，实现在 Infrastructure 层
- **CQS 分离**：查询 Repository 和命令 Repository 接口分离
- **分页抽象**：统一 Pageable/Page 泛型，避免泄露 ORM 分页模型
- **规约模式**：Specification 模式封装复杂查询条件，UserSpecification.withStatus(Status.PAID).and(between(from, to))
- **延迟加载**：设计 API 时避免 N+1 查询，使用 Fetch Join 或 EntityGraph
