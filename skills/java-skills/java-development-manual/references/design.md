# 设计规约

## 目录
- [一、UML图使用规范](#一uml图使用规范)
- [二、存储与数据结构设计](#二存储与数据结构设计)
- [三、设计原则](#三设计原则)
- [四、敏捷开发误区](#四敏捷开发误区)
- [五、可扩展性设计](#五可扩展性设计)

---

## 一、UML图使用规范

### 【强制】规约

| 场景 | 使用UML图 |
|------|----------|
| User超过1类 + UserCase超过5个 | **用例图** |
| 业务对象状态超过3个 | **状态图** |
| 调用链路涉及对象超过3个 | **时序图** |
| 模型类超过5个且有复杂依赖 | **类图** |
| 超过2个对象协作+复杂流程 | **活动图** |

### 状态图示例（订单状态）

```
┌──────────┐     付款成功      ┌──────────┐     发货       ┌──────────┐
│  已下单   │ ───────────────> │  已付款   │ ────────────> │  已发货   │
└──────────┘                   └──────────┘                └──────────┘
     │                              │                           │
     │ 取消                         │ 取消                      │ 确认收货
     ↓                              ↓                           ↓
┌──────────┐                   ┌──────────┐                ┌──────────┐
│  已取消   │                   │  已取消   │                │  已完成   │
└──────────┘                   └──────────┘                └──────────┘
```

**注意**：已下单与已完成之间不可能直接转换

---

## 二、存储与数据结构设计

### 【强制】规约

**存储方案和底层数据结构设计需评审通过并沉淀为文档**

评审内容包括：
1. 存储介质选型
2. 表结构设计是否满足技术方案
3. 存取性能和存储空间是否满足业务发展
4. 表/字段之间的辩证关系
5. 字段名称、类型、索引

**数据结构变更同样需要评审**

---

## 三、设计原则

### 【推荐】规约

#### 1. 系统架构设计目标

| 目标 | 说明 |
|------|------|
| 确定系统边界 | 技术层面的做与不做 |
| 确定模块关系 | 依赖关系、宏观输入输出 |
| 确定演化原则 | 后续设计的框架和方向 |
| 确定非功能需求 | 安全性、可用性、可扩展性 |

#### 2. 单一职责原则（SRP）

类在设计时只负责一项职责

#### 3. 优先聚合/组合而非继承

```java
// 正例：聚合/组合
public class Car {
    private Engine engine;  // 组合
}

// 继承需符合里氏代换原则
```

#### 4. 依赖倒置原则（DIP）

```java
// 正例：依赖抽象
public class OrderService {
    private PaymentProcessor processor;  // 依赖接口
}

// 反例：依赖具体实现
public class OrderService {
    private AlipayProcessor processor;  // 依赖具体类
}
```

#### 5. 开闭原则（OCP）

对扩展开放，对修改闭合

```java
// 正例：通过扩展支持新功能
public interface PaymentProcessor {
    Result process(Order order);
}

public class AlipayProcessor implements PaymentProcessor { }
public class WechatProcessor implements PaymentProcessor { }
public class NewPaymentProcessor implements PaymentProcessor { }  // 扩展
```

#### 6. DRY原则（Don't Repeat Yourself）

```java
// 正例：抽取公共方法
public class UserService {
    public void createUser(UserDTO dto) {
        validateUser(dto);  // 复用
    }

    public void updateUser(UserDTO dto) {
        validateUser(dto);  // 复用
    }

    private void validateUser(UserDTO dto) {
        // 校验逻辑
    }
}
```

---

## 四、敏捷开发误区

### 【推荐】规约

**误区**：敏捷开发 = 讲故事 + 编码 + 发布

**正解**：
- 敏捷是快速交付迭代可用的系统
- 省略多余设计方案
- 摒弃传统审批流程
- **核心关键点的设计和文档沉淀仍然需要**

**反例**：以敏捷为借口催进度，系统代码像面条，一年后大规模重构

---

## 五、可扩展性设计

### 【参考】规约

**可扩展性本质**：找到系统变化点，隔离变化点

**极致扩展性标志**：需求新增不会在原有代码上做任何修改

```java
// 正例：策略模式隔离变化
public interface PricingStrategy {
    BigDecimal calculate(Order order);
}

public class NormalPricing implements PricingStrategy { }
public class VipPricing implements PricingStrategy { }
public class PromotionPricing implements PricingStrategy { }

// 新增定价策略只需新增类，无需修改现有代码
```

### 设计文档作用

1. **明确需求、理顺逻辑、后期维护**
2. **避免为了设计而设计**
3. **代码即文档是错误的观点**：
   - 清晰代码只是文档片断
   - 深度调用、依赖关系需要文档呈现
