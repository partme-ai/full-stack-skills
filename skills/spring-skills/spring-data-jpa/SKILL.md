---
name: spring-data-jpa
description: Provides comprehensive guidance for Spring Data JPA including repositories, entity management, query methods, and database operations. Use when the user asks about Spring Data JPA, needs to work with JPA repositories, implement data access layers, or configure JPA in Spring.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Spring Data JPA 定义实体、Repository、查询方法与事务
- 配置数据源、JPQL、规范与审计

## How to use this skill

1. **核心**：@Entity、JpaRepository、CrudRepository；方法名查询、@Query、Pageable。
2. **进阶**：@EntityGraph、Specification、审计 @CreatedDate；多数据源与事务传播。
3. **参考**：https://spring.io/projects/spring-data-jpa

## Best Practices

- N+1 与 fetch 策略；分页与批量操作。
- 实体与 DTO 分离；事务边界明确。

## Keywords

spring data jpa, JPA, Repository, 持久化
