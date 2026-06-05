# DDD Code Review Gotchas — 常见审查陷阱与检测方法

## 1. 漏检跨聚合引用陷阱

**问题**：只检查了直接字段引用（`Order.customer`），忽略了方法返回类型中的跨聚合情况。

**检测命令**：

```bash
# 检查方法返回类型中是否直接返回了其他聚合的对象
grep -rn "Customer " --include="*.java" domain/   # 检查是否有 Customer 类型出现在 domain 层
grep -rn "import.*domain\..*\.model\." --include="*.java" domain/  # 检查 domain 内跨包引用

# 检查 Repository 是否返回非自有聚合
grep -rn "interface.*Repository" --include="*.java" domain/ | while read line; do
  return_type=$(echo "$line" | grep -oP '(?<=findBy\w+\()\w+')
  echo "Check: $line -> returns $return_type"
done
```

**区分标记**：

| 检查项 | 合法 | 非法 |
|--------|:---:|:---:|
| `order.customerId: CustomerId` | ✓ | |
| `order.customer: Customer` | | ✗ |
| `orderRepository.findById(id)` 返回 `Optional<Order>` | ✓ | |
| `userService.getUser(id)` 返回 `User` 被 Order 聚合持有 | | ✗ |
| `Order.create(customerId)` — 只传 ID | ✓ | |
| `OrderItem.productId` | ✓ | |

---

## 2. PO/DTO 混用

**问题**：Repository 返回 JPA Entity 或 DTO，Domain 层收到贫血对象。

**检测命令**：

```bash
# 检查 Repository 返回类型是否为 Domain 对象（非 JPA Entity）
grep -rn "import javax.persistence\|import jakarta.persistence" --include="*.java" domain/ | head -20

# 检查 Application Service 中是否有 JPA 查询
grep -rn "JdbcTemplate\|EntityManager\|@Query" --include="*.java" application/

# 检查 Infrastructure Repository 实现是否返回 Domain 对象
grep -rn "return.*Entity\|return.*DTO\|return.*PO" --include="*RepositoryImpl*.java" infrastructure/
```

---

## 3. 测试反模式被忽略

**问题**：Mock 了不该 Mock 的，没 Mock 该 Mock 的。

**检测方法**：

```bash
# 检查测试中是否 Mock 了 Domain Service（应该 Mock Repository，不是其他 Domain Service）
grep -rn "@Mock.*Service\|mock(.*Service\.class)" --include="*Test*.java" domain/

# 检查测试类是否有真实的数据库测试
grep -rn "@DataJpaTest\|@SpringBootTest\|@MybatisTest" --include="*Test*.java" infrastructure/

# 检查 Domain 层测试是否引用了 Spring
grep -rn "@SpringBootTest\|@Autowired\|@MockBean" --include="*Test*.java" domain/ | head -10
```

**测试 Mock 决策表**：

| 层 | 应该真实调用 | Mock |
|----|:--------:|:--:|
| Domain 单元测试 | 聚合根、Domain Service | Repository 接口 |
| Application Service 测试 | 编排逻辑 | Repository, Domain Service |
| Infrastructure 集成测试 | Repository 实现 + 真实 DB | 无（不 Mock DB） |
| Adapter 测试 | Controller + HTTP | Application Service |

---

## 4. 把编排厚度当成 God Service

**问题**：`Service > 500 行` 不一定都有问题。需区分"编排多" vs "业务逻辑泄露"。

**检测命令**：

```bash
# 量化：统计 Service 中 if/else 分支数（业务逻辑指标）
grep -c "if\|else if\|switch" application/service/*Service.java

# 区分编排 vs 业务逻辑：
# 编排特征：serviceA.doX() → serviceB.doY() → save()
# 业务逻辑：if (order.status == PAID && amount > 100) { applyDiscount() }
# → if/switch 中直接判断领域状态的，是业务逻辑泄露
```

**判断表**：

| Service 类型 | 行数 | 内容 | 是否反模式 |
|-------------|:---:|------|:--------:|
| 编排 Service | 600 | 全是 `serviceA.doSth()` + `repo.save()` | 否（厚度） |
| 编排 Service | 600 | 50% `if (order.getXxx())` 判断 | 是（毒性） |
| God Service | 800 | 全部业务逻辑在一个类 | 是 |

---

## 5. 分层检查只查 import

**问题**：只检查了 import，忽略了方法参数和调用链。

**检测命令**：

```bash
# 检查 Domain 方法参数是否包含框架类型
grep -rn "HttpServletRequest\|HttpServletResponse\|@RequestParam\|@PathVariable" --include="*.java" domain/

# 检查 Application Service 是否接收了 Web 层对象
grep -rn "HttpRequest\|HttpResponse\|@RequestBody" --include="*.java" application/

# 检查 Adapter 层是否有业务逻辑（非纯转换）
grep -rn "if\|else\|switch\|throw new.*Exception" adapter/inbound/controller/

# 检查 ORM 注解是否出现在 Domain 层
grep -rn "@Entity\|@Table\|@Column\|@Id\|@ManyToOne\|@OneToMany" --include="*.java" domain/ 2>/dev/null
```

**分层依赖检查矩阵**：

| 层 | 允许依赖 | 禁止依赖 |
|----|---------|---------|
| Domain | 无框架依赖 | `spring`, `javax.persistence`, `java.sql`, `HttpServletRequest` |
| Application | Domain, DTO, Command | Adapter, Controller, `HttpServletRequest` |
| Infrastructure | Domain, 框架 | 无（最外层） |
| Adapter | Application, DTO | Domain 聚合根 |

---

## 6. 忽略贫血模型中的隐式行为

**问题**：Entity 有 getter/setter 但没有行为方法，所有逻辑在 Service 中。

**检测命令**：

```bash
# 统计 Entity 中 public setter 数量 vs public 行为方法数量
for f in domain/model/*.java; do
  setters=$(grep -c "public void set" "$f")
  behaviors=$(grep -cP "public (void|bool|Money|\w+) (?!get|set|is)" "$f" || echo 0)
  if [ "$setters" -gt "$behaviors" ]; then
    echo "ANEMIC: $f (setters=$setters, behaviors=$behaviors)"
  fi
done
```

**反模式 → 修复**：

```java
// 反模式：贫血模型
order.setStatus("PAID");           // Service 中直接 set
order.setPaidAt(LocalDateTime.now());

// 修复：充血模型
order.pay();                       // 聚合根方法，内部 set + 发事件 + 校验
```

---

## 7. 聚合事务边界超出预期

**问题**：单个 Application Service 方法操作了 2+ 聚合但没有发领域事件。

**检测命令**：

```bash
# 检查 AppService 中是否操作了多个 Repository（跨聚合事务风险）
grep -rn "Repository" application/service/ | awk -F: '{print $1}' | sort | uniq -c | awk '$1 > 1'
```

**修复方案**：

```
如果一个 AppService 操作了 OrderRepository + InventoryRepository：
→ 改为：OrderRepository.save() → 发 OrderPlacedEvent → 异步 handler 调用 InventoryRepository
```

---

## 8. 值对象被用作可变引用

**问题**：VO 有 setter 或可变集合（List<OrderItem> items 可被外部修改）。

**检测命令**：

```bash
# 检查 VO 类中的 setter
grep -rn "public void set" --include="*.java" domain/model/*/   # 检查极子包
grep -rn "List<.*> get.*()" --include="*.java" domain/  # 返回可变集合
```

**修复**：返回值使用 `Collections.unmodifiableList()` 或返回不可变副本。
