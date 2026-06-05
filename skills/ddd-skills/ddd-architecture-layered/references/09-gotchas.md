# 15 Gotchas — 常见陷阱

1. **贫血模型回退** — Entity 只有 getter/setter，业务逻辑在 Service 中。→ 将业务方法迁入 Entity
2. **Application 膨胀** — AppService 超过 50 行，内含 if/else。→ 业务下沉到 Domain
3. **Domain 框架污染** — 出现 `@Entity`、`@Service` 注解。→ 用 PO 分离持久化
4. **跨聚合直接引用** — Order 中引用 Customer 对象。→ 改为 CustomerId
5. **Controller 含业务** — Controller 中有 if/else。→ 移到 Application
6. **大聚合** — 一个聚合 > 5 实体。→ 拆分为小聚合
7. **跨聚合事务** — 一个 `@Transactional` 涉及多个聚合。→ 领域事件最终一致
8. **Repo 返回 DTO** — Repository 返回非聚合根。→ Repository 只操作聚合根
9. **跳过 Application** — Controller 直接调用 Repository。→ 必须经过 AppService
10. **测试只测 API** — 忽视 Domain 测试。→ Domain 测试覆盖率 ≥ 80%
11. **值对象可变** — ValueObject 有 setter。→ 用 final + 构造器初始化
12. **Infra 反向依赖** — Infra 直接引用 Interface。→ Infra 只依赖 Domain
13. **忽略领域事件** — 关键操作不发布事件。→ 为状态变更添加事件
14. **上帝 Service** — 一个 Service 超过 200 行。→ 拆分为多个领域服务
15. **过度设计** — 简单 CRUD 也用 DDD。→ 评估业务复杂度，不滥用
