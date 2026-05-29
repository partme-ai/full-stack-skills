# 架构反模式与气味 — 诊断+修复

## 贫血领域模型

| 症状 | 诊断 | 修复 |
|------|------|------|
| Entity 只有 getter/setter | 检查实体类：是否有 `void` 返回类型的业务方法？ | 把 Service 中的业务逻辑搬进 Entity |
| 所有逻辑在 Service | 检查 Service 行数：是否 > 500 行？ | 拆分为聚合内方法和领域服务 |

## Repository per Table

| 症状 | 诊断 | 修复 |
|------|------|------|
| 每个 DB 表一个 Repository 接口 | grep -r "interface.*Repository" \| wc -l → 是否远超聚合数？ | 合并为按聚合的 Repository |
| `OrderItemRepository` 独立存在 | OrderItem 是实体还是独立聚合？ | 如果是 Order 聚合内的实体，删除独立 Repository |

## 泄露基础设施

| 症状 | 诊断 | 修复 |
|------|------|------|
| Domain 层 import `@Entity` | grep "import javax.persistence" domain/ | 在 Infrastructure 层创建 PO，Domain 只用纯 Java |
| Domain 层 import `@Service` | grep "import org.springframework" domain/ | 移除框架注解 |
| Domain 层 import JDBC | grep "import java.sql" domain/ | 移到 Infrastructure Repository |

## God Aggregate（上帝聚合）

| 症状 | 诊断 | 修复 |
|------|------|------|
| 单个聚合 > 10 个实体 | wc -l domain/{aggregate}/*.java | 按业务子流程拆分 |
| 聚合加载慢 | 检查 N+1 查询 | 拆分聚合 + lazy loading |
| 并发修改冲突 | 检查事务冲突日志 | 拆分聚合减少锁范围 |

## 跳过 UseCase

| 症状 | 诊断 | 修复 |
|------|------|------|
| Controller 直接调 Repository | grep "repository\." adapter/controller/ | Controller → AppService → Repository |

## CRUD Thinking

| 症状 | 诊断 | 修复 |
|------|------|------|
| 方法名是 `save`/`update`/`delete` | grep "public.*save\|update\|delete" domain/ | 改为 `place`/`confirm`/`cancel`/`ship` |
| 实体没有业务含义的方法 | 检查方法是否反映业务操作 | 用领域语言重命名 |

## 不成熟的 CQRS

| 症状 | 诊断 | 修复 |
|------|------|------|
| 读写负载相似却引入了 CQRS | 检查读 QPS vs 写 QPS 差异 | 先共用模型，差异显著时再分离 |
| 引入了 Event Sourcing 但不需要审计 | 检查业务是否真的需要事件溯源 | 降级到 L1 或 L2 |

## 跨聚合事务

| 症状 | 诊断 | 修复 |
|------|------|------|
| 一个 `@Transactional` 操作多个聚合 | grep "@Transactional" \| grep -c "save\|update" | 用领域事件实现最终一致性 |

## 值对象滥用（设计气味）

| 症状 | 诊断 | 修复 |
|------|------|------|
| 每个 String 都包装成值对象 | 检查 VO 类数量 / 实体数量 比值 | 只在有业务含义时用 VO（Money ✓, Email ✓, NameString ✗） |

## 修复优先级

```
P0（阻止合并）：
  1. 领域层去框架化
  2. 切断循环依赖
  3. 修复跨聚合引用

P1（下个版本前）：
  4. Repository 返回聚合根
  5. Controller 去业务化
  6. App 层去 SQL

P2（持续改进）：
  7. 聚合瘦身（>5 实体 → 拆分）
  8. 补充领域事件
  9. String → Value Object 替换
```
