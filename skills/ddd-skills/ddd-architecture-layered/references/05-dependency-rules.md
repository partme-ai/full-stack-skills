# Dependency Rules — 依赖方向规则

> DDD 分层架构的核心约束：**所有依赖指向 Domain 层**。

## 依赖方向全景

```
┌─────────────────────────────────────────────────────────────┐
│                     Interface Layer                          │
│  controller / dto / converter / advice / filter             │
│  Dependencies: → Application                                 │
│  Forbidden:   → Domain (直接), → Infrastructure              │
└───────────────────────┬─────────────────────────────────────┘
                        │ 调用 AppService
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│  service / command / query / assembler / event              │
│  Dependencies: → Domain                                      │
│  Forbidden:   → Interface, → Infrastructure (直接)           │
└───────────────────────┬─────────────────────────────────────┘
                        │ 调用 Domain Service + Repository 接口
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      Domain Layer ★                          │
│  entity / valueobject / event / service / repository        │
│  Dependencies: → JDK only                                    │
│  Forbidden:   → Any other layer, → Spring/JPA/MyBatis       │
└───────────────────────┬─────────────────────────────────────┘
                        │ Domain 定义接口，Infra 实现
                        ▲
┌─────────────────────────────────────────────────────────────┐
│                  Infrastructure Layer                        │
│  repository / persistence / messaging / external / config   │
│  Dependencies: → Domain                                      │
│  Forbidden:   → Interface, → Application (直接)              │
└─────────────────────────────────────────────────────────────┘
```

## 依赖规则细则

| 规则编号 | 规则 | 严重级别 | 检测方法 |
|---------|------|:-------:|---------|
| R1 | Domain 层不能依赖任何其他层 | P0 | ArchUnit |
| R2 | Domain 层不能 import Spring/JPA/MyBatis | P0 | 代码审查 |
| R3 | Application 层可以依赖 Domain 层 | P0 | ArchUnit |
| R4 | Application 层不能直接依赖 Infrastructure 层 | P1 | ArchUnit |
| R5 | Interface 层可以依赖 Application 层 | P0 | ArchUnit |
| R6 | Interface 层不能直接依赖 Domain 层 | P1 | 代码审查 |
| R7 | Infrastructure 层可以依赖 Domain 层 | P0 | ArchUnit |
| R8 | Infrastructure 层不能依赖 Interface 层 | P1 | ArchUnit |
| R9 | 模块间不能循环依赖 | P0 | JDepend/ArchUnit |
| R10 | 聚合间通过 ID 引用，不能直接引用对象 | P1 | 代码审查 |

## 严格分层 vs 松散分层

```
严格分层（推荐）：
  Interface → Application → Domain ← Infrastructure
  └── 每层只依赖直接下层（或 Domain）
  └── 更安全，依赖关系清晰
  └── 更适合中大型团队

松散分层：
  Interface → Application → Domain ← Infrastructure
  └── 允许跳过 Application 层直接调用 Domain
  └── 开发更快，但容易产生违规
  └── 仅适合 < 5 人的小团队
```

## 常见违规场景

| 违规 | 示例 | 修复 |
|------|------|------|
| Domain import JPA | `import javax.persistence.Entity` | 将 JPA 注解移到 PO 中 |
| Domain import Spring | `import org.springframework.stereotype.Service` | 去掉注解，Domain 用纯 POJO |
| Controller 调用 Repository | `orderController → orderRepository.findById()` | 改为 Controller → AppService → Repository |
| AppService 写 SQL | `appService → jdbcTemplate.query()` | SQL 移到 Repository 实现 |
| Infra 调用 Interface | `infra → someController.method()` | 通过 Domain Event 解耦 |
| 跨聚合直接引用 | `Order.customer = Customer`（对象引用） | 改为 `Order.customerId = CustomerId`（ID 引用） |

## ArchUnit 验证

推荐在 CI 中集成以下 ArchUnit 规则（详见 `07-archunit-config.md`）：

```java
@ArchTest
public static final ArchRule domain_layer_should_not_depend_on_infra =
    noClasses().that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAPackage("..infrastructure..");

@ArchTest
public static final ArchRule domain_layer_should_not_depend_on_spring =
    noClasses().that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAnyPackage("org.springframework..", "javax.persistence..");
```

## 参考

- Robert C. Martin Clean Architecture — 依赖规则
- Eric Evans DDD Blue Book — 分层架构
- Vaughn Vernon IDD Red Book — 分层实现
