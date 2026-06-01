---
name: ddd-api-designer
description: API design from domain model — CQRS command/query separation, REST API endpoint design, data object conversion chain (PO→DO→DTO→VO), unified response format, OpenAPI/Swagger generation, BFF pattern, API versioning, and security design. Use when user asks about API design, REST API, OpenAPI, BFF, DTO design, 接口设计, or data object conversion.
license: Apache-2.0
---

# DDD API Designer

从领域模型到 REST API 的完整设计指南：CQRS 读写分离、四层数据对象转换链（PO→DO→DTO→VO）、统一响应格式、BFF 多端适配、版本管理与安全设计。

## Workflow

1. **识别 Command vs Query** — 将领域行为分为命令（写）和查询（读），决定 Method 和端点
2. **设计数据对象转换链** — 建立 PO→DO→DTO→VO 四层转换，各层独立职责
3. **设计 REST 端点** — Command 动词后缀, Query 资源命名
4. **定义统一响应格式** — Result&lt;T&gt; 包装 + 业务错误码体系
5. **应用 BFF** — 每前端一个 BFF, 数据聚合 + 格式适配 + 协议转换
6. **选择版本策略** — 推荐 URL Path: /api/v1/orders, CDN 友好
7. **施加安全控制** — AuthN + AuthZ + 三层校验 + 差异化限流

## When to Use

| ✅ ALWAYS use when | ❌ Skip when |
|---|---|
| API 设计、REST API、接口设计 | 内部工具无外部消费者 |
| DTO/VO 设计、数据对象转换 | GraphQL/gRPC 项目 |
| BFF / Backend for Frontend | 无领域模型时 → domain-designer |
| OpenAPI / Swagger / API 文档 | 简单 CRUD 无 DDD |
| API 版本管理 / 安全设计 | 纯 gRPC 微服务（用 protobuf IDL） |
| 需要将 DDD 聚合暴露为 REST API | 快速原型不关心 API 规范 |

## Boundary

### ✅ 明确适用
- 需要将 DDD 领域模型暴露为 REST API — CQRS 读写分离、数据对象转换链完整落地
- CQRS 命令/查询分离设计 — 独立 Command DTO 和 Query DTO，各自演化
- 多端（Web/iOS/MiniApp）API 统一设计 — BFF 模式按平台适配
- 统一响应格式与错误码体系设计 — Result&lt;T&gt; + 业务错误码标准化
- OpenAPI/Swagger 规范输出 — 代码生成策略保持接口与实现同步

### ⚠ 需谨慎评估
- 团队对 DDD/CQRS 不熟悉 → 先学习基础概念
- 单体应用无扩展需求 → 评估 ROI，可能过度设计
- 现有 API 无消费者兼容需求 → 版本管理可简化

### ❌ 不适用
- GraphQL/gRPC 项目 → 使用对应 IDL 和工具链
- 简单 CRUD 无 DDD → 先用通用 REST 框架或 domain-designer
- 快速原型/演示阶段 → 先用简化 API，后续再引入规范
- 纯 gRPC 微服务 → 使用 protobuf IDL + gRPC 拦截器
- 内部工具无外部消费者 → 简化 API 设计

## CQRS API Design

Command（写）动词驱动，Query（读）资源驱动：

| 维度 | Command | Query |
|------|---------|-------|
| HTTP Method | POST/PUT/DELETE | GET |
| URL 动词 | 需要（confirm, cancel） | 不需要 |
| 请求体 | Command 对象 | 仅查询参数 |
| DTO 分离 | 独立 Command DTO | 独立 Query DTO |
| 幂等性 | 必须实现 | 天然幂等 |
| 缓存 | 从不缓存 | ETag, max-age |
| 响应 | 创建的资源摘要 | 数据 DTO / 列表 |

原则：Command DTO 和 Query DTO 始终分开定义。子资源嵌套最多 2 层。详见 [references/patterns/cqrs-api-design.md](references/patterns/cqrs-api-design.md)

## 数据对象转换链（PO → DO → DTO → VO）

| 对象 | 层 | 职责 | 可见性 |
|------|-----|------|--------|
| **PO** | Infrastructure | ORM 映射，数据库结构对应 | 内部 |
| **DO** | Domain | 充血模型，含业务行为 | 内部 |
| **DTO** | Interface/App | 跨层跨服务数据传输 | 半内部 |
| **VO** | Interface | 页面专用展示数据 | 外部 |

读方向：PO→DO→DTO→VO；写方向：VO→DTO→Command→DO→PO。
一个 DO 可按场景转换为多个 DTO（详情 DTO、摘要 DTO 等），Controller 不直接返回领域对象。详见 [references/examples-ref/data-object-transformation.md](references/examples-ref/data-object-transformation.md)

## API 设计规范

| 规则 | 示例 |
|------|------|
| 名词复数 | /orders ✓ |
| Kebab-case | /order-history ✓ |
| 最大 2 层嵌套 | /orders/{id}/items |
| 写动词后缀 | /orders/{id}/confirm |
| 查询参数 | ?status=PAID&page=1 |
| 无 URL 动词 | ❌ GET /getOrders → GET /orders |

HTTP Status：201 Created（创建）、200 OK（查询/更新）、204 No Content（删除）、400（校验/业务）、404（未找到）、409（并发冲突）、429（限流）、500（内部错误）。详见 [references/security/api-naming-conventions.md](references/security/api-naming-conventions.md)

## 统一响应格式

成功：`{ "code": 0, "message": "success", "data": T }` — 201/200/204
错误：`{ "code": 40001, "message": "...", "detail": "...", "requestId": "req-xxx" }` — 400/404/409/429/500

Response wrapper `Result<T>` 包含 code + message + data + requestId。错误响应绝不返回堆栈信息。详见 [references/examples-ref/unified-response-format.md](references/examples-ref/unified-response-format.md)

## BFF（Backend for Frontend）

每前端一个 BFF（Web/iOS/MiniApp），职责：
- **数据聚合**：组合多服务数据为页面 VO（1 次前端调用替代 N 次）
- **格式适配**：Web 全量字段 / 移动端精简字段
- **协议转换**：内部 gRPC → 外部 REST/JSON
- **响应塑形**：移除内部字段，添加 UI 元数据

与 API Gateway 区别：BFF 做视图聚合（页面级），Gateway 做路由+限流（服务级）。
BFF 不直接访问数据库，不包含业务逻辑。详见 [references/patterns/BFF-design-pattern.md](references/patterns/BFF-design-pattern.md)

## API 版本管理

| 策略 | 示例 | 推荐度 |
|------|------|:------:|
| **URL Path** ★ | `/api/v1/orders` → `/api/v2/orders` | ★★★★★ |
| Request Header | `Accept: vnd.company.v2+json` | ★★★☆☆ |
| Query Param | `/api/orders?version=2` | ★★☆☆☆ |

推荐 URL Path：直观、CDN 友好、Swagger 兼容。迁移流程：v1 → v1+v2 → v2 only → v1 sunset（410 Gone）。详见 [references/migration/api-versioning-strategies.md](references/migration/api-versioning-strategies.md)

## API 安全设计

四层安全模型：
1. **认证**：JWT Bearer Token / OAuth2 / API Key（服务间）
2. **授权**：按限界上下文 + 资源所有权 + 角色
3. **输入校验**：Controller 格式 → Application 业务 → Domain 不变式
4. **限流**：Command 50/s, Query 200/s, Auth 10/s。详见 [references/security/api-security-design.md](references/security/api-security-design.md)

## Gotchas — 常见陷阱

DTO 暴露枚举→string code | Command/Query DTO 混用→分开 | null 安全→处理 Optional | VO 透传 DB 字段→视图定制 |
幂等缺失→Idempotency-Key | 错误透传堆栈→requestId | 深层嵌套→≤2 层 | 领域对象序列化→经 DTO/VO

## Rules

- **Command/Query DTO 分离** — 写操作和读操作使用独立 DTO，禁止复用同一结构
- **Controller 协议转换** — Controller 层仅做 HTTP 协议适配，不包含业务逻辑或领域调用
- **统一错误码前缀** — 业务错误 5 位码：首位类别（4=客户端/5=服务端）+ 后两位 HTTP + 末三位具体错误
- **BFF 职责边界** — BFF 只做数据聚合与格式适配，不直接访问数据库或不包含业务规则
- **响应封装** — 所有 API 响应使用 Result&lt;T&gt; 包装，仅 204 No Content 和文件下载可例外

## FAQ

| Question | Answer |
|----------|--------|
| DO 和 DTO 字段一样能复用吗？ | 不能。DO 含行为，DTO 纯数据，演化方向不同。 |
| 所有 API 都要统一响应格式？ | 是，仅文件下载、204 可例外。 |
| 错误码怎么设计？ | 5 位数字：首位类别+后两位 HTTP+末三位具体错误。 |
| 何时需要 BFF？ | 多前端平台或前端需组合多服务数据。 |
| 子资源最多嵌套几层？ | 最多 2 层，超 2 层说明聚合边界有问题。 |
| Controller 中能放业务逻辑吗？ | 不能，只做协议转换。 |

## Keywords

`CQRS API` `REST endpoint design` `PO DO DTO VO` `data object transformation` `unified response format` `BFF` `Backend for Frontend` `OpenAPI` `Swagger` `API versioning` `API security` `command query separation` `Result<T>` `response wrapper` `input validation` `rate limiting` `idempotency` `pagination design`
## References
- [references/patterns/cqrs-api-design.md](references/patterns/cqrs-api-design.md) — CQRS API 设计
- [references/examples-ref/data-object-transformation.md](references/examples-ref/data-object-transformation.md) — PO↔DO↔DTO↔VO 转换
- [references/patterns/BFF-design-pattern.md](references/patterns/BFF-design-pattern.md) — BFF 设计模式
- [references/security/api-security-design.md](references/security/api-security-design.md) — API 安全
- [references/migration/api-versioning-strategies.md](references/migration/api-versioning-strategies.md) — 版本管理
- [references/security/api-naming-conventions.md](references/security/api-naming-conventions.md) — 命名规范
- [references/examples-ref/unified-response-format.md](references/examples-ref/unified-response-format.md) — 统一响应
- [references/security/openapi-specification.md](references/security/openapi-specification.md) — OpenAPI 3.0 规范
- [references/patterns/data-access-api.md](references/patterns/data-access-api.md) — 数据访问层 API 设计
- [references/patterns/idempotency-design.md](references/patterns/idempotency-design.md) — 幂等设计
- [references/patterns/pagination-filtering-design.md](references/patterns/pagination-filtering-design.md) — 分页过滤
- [references/architecture/partme-16-service-data-view.md](references/architecture/partme-16-service-data-view.md) — 协作关系
- [references/architecture/clean-ddd-hexagonal-hexagonal.md](references/architecture/clean-ddd-hexagonal-hexagonal.md) — 六边形架构
- [references/examples-ref/api-error-handling.md](references/examples-ref/api-error-handling.md) — 错误处理
- [references/security/api-rate-limiting.md](references/security/api-rate-limiting.md) — 限流设计
- [references/examples-ref/event-driven-api.md](references/examples-ref/event-driven-api.md) — 事件驱动 API

## Examples

- [examples/order-api-design.md](examples/order-api-design.md) — 订单服务案例
- [examples/user-api-design.md](examples/user-api-design.md) — 用户服务案例：注册/登录/资料 + 安全设计
- [examples/BFF-aggregation-example.md](examples/BFF-aggregation-example.md) — BFF 聚合案例：订单详情页多服务数据聚合
- [examples/api-version-migration.md](examples/api-version-migration.md) — API 版本迁移案例：v1 → v2 全流程
- [examples/payment-api-design.md](examples/payment-api-design.md) — 支付服务 API 案例：退款幂等、状态机、异步通知
- [examples/openapi-codegen-example.md](examples/openapi-codegen-example.md) — OpenAPI 代码生成案例：Spec-first 策略
- [examples/product-api-design.md](examples/product-api-design.md) — 商品服务 API 案例
- [examples/inventory-api-design.md](examples/inventory-api-design.md) — 库存服务 API 案例
- [examples/notification-api-design.md](examples/notification-api-design.md) — 通知服务 API 案例
- [examples/search-api-design.md](examples/search-api-design.md) — 搜索服务 API 案例

---

## 🧭 DDD Skills Journey

> 📍 **当前：`ddd-api-designer` — Step 4: API 设计与数据转换**

```
Step 1 (awesome) → Step 2 (selector) → Step 3 (架构落地) → Step 4 (领域+CQRS+API) → Step 5 (审查) → Step 6 (辅助) → Step 7 (文档)
                                                                    ↑
                                         ⭐ ddd-api-designer: 领域模型 → REST API
```

**← 上一站**: [ddd-domain-designer](../ddd-domain-designer/) — 先有领域模型再设计 API
**→ 下一站**: [ddd-code-reviewer](../ddd-code-reviewer/) — 审查 API 设计合规性
**🔗 相关**: [ddd-cqrs-architecture](../ddd-cqrs-architecture/) — CQRS 深入 | [ddd-architecture-doc](../ddd-architecture-doc/) — OpenAPI 文档输出

> 核心原则：Command 和 Query 分开设计。牢记 PO→DO→DTO→VO 四层转换链，DTO 与领域对象解耦，VO 与数据库结构解耦。
