# 上下文映射 — 限界上下文之间的关系

## 上下文映射类型

| 关系类型 | 含义 | 何时使用 | 实现方式 |
|---------|------|---------|---------|
| **Partnership（合作）** | 两个团队共同演进接口 | 紧密协作的团队 | 同步沟通，共同制定接口 |
| **Shared Kernel（共享内核）** | 两个上下文共享一部分模型 | 核心概念需要一致 | 共享代码库，严格变更控制 |
| **Customer-Supplier（客户-供应商）** | 上游定义，下游消费 | 上下游关系明确 | SLA，上游承诺接口稳定性 |
| **Conformist（遵奉者）** | 下游完全遵从上游模型 | 下游无力影响上游 | 直接使用上游模型，不做翻译 |
| **Anti-Corruption Layer（防腐层）** | 下游构建翻译层保护自身模型 | 需要隔离外部模型 | 适配器模式，DTO 转换 |
| **Open Host Service（开放主机）** | 上游提供标准化 API | 多个下游消费者 | REST/gRPC API，版本管理 |
| **Published Language（发布语言）** | 标准化数据格式 | 跨系统集成 | XML Schema，JSON Schema，Protobuf |

## 上下文映射落地

```java
// 防腐层（ACL）示例
// domain/gateway/PaymentGateway.java — Domain 层定义接口
public interface PaymentGateway {
    PaymentResult process(PaymentRequest request);
}

// infrastructure/gateway/PaymentGatewayImpl.java — Infrastructure 实现防腐
public class PaymentGatewayImpl implements PaymentGateway {
    private final ExternalPaymentClient client;  // 外部支付系统 SDK

    public PaymentResult process(PaymentRequest request) {
        ExternalRequest extReq = PaymentMapper.toExternal(request);  // DO → 外部模型
        ExternalResponse extRes = client.charge(extReq);
        return PaymentMapper.toDomain(extRes);  // 外部模型 → DO
    }
}
```

## 限界上下文识别方法

### Event Storming 工作流
1. **Chaotic exploration** — 所有人贴出已知事件
2. **Timeline ordering** — 按时间排列事件
3. **Identify aggregates** — 将相关事件分组
4. **Find boundaries** — 语言变化处 = 限界上下文边界
5. **Surface problems** — 标注模糊区域后续跟进

### Context Mapping Workshop（已有系统）
1. 列出所有系统/服务
2. 识别每个系统的所属团队
3. 画出关系（上游/下游）
4. 标注关系类型（ACL, Conformist 等）
5. 找出当前集成中的痛点

## 示例：电商系统上下文划分

```
E-Commerce System
├── Sales Context（销售）
│   ├── Customer: id, email, preferences
│   └── Order: items, total, status
├── Shipping Context（物流）
│   ├── Recipient: name, address, phone
│   └── Shipment: packages, carrier, trackingNo
├── Billing Context（财务）
│   ├── Payer: name, billingAddress, paymentMethod
│   └── Invoice: lineItems, total, dueDate
└── Catalog Context（商品）
    └── Product: name, description, price
```

**"Customer" 在不同上下文含义不同：**
- Sales：Email, preferences, order history
- Shipping：Delivery address, phone number
- Billing：Payment methods, billing address

## Bounded Context = Microservice Boundary

每个限界上下文通常对应一个微服务，通过事件总线通信：

```
Sales Service → events → Shipping Service
Shipping Service → events → Billing Service
Sales Service → Integration Events → Event Bus
Shipping Service → Integration Events → Event Bus
Billing Service → Integration Events → Event Bus
```

## Ubiquitous Language（统一语言）

**原则：**
1. 每个限界上下文一个统一语言
2. 代码反映语言 — `Order.confirm()` 而不是 `Order.setStatus("confirmed")`
3. 语言演变时，代码同步演变

```java
// ❌ 技术语言
class Order { void setStatus(int s) { this.status = s; } }

// ✅ 统一语言
class Order { void confirm() { this.status = OrderStatus.CONFIRMED; } }
```

## 子域类型

| 类型 | 说明 | 投入 | 示例 |
|------|------|:--:|------|
| **Core（核心域）** | 竞争优势所在 | 高 | 商品推荐引擎 |
| **Supporting（支撑域）** | 必要但不独特 | 中 | 订单管理 |
| **Generic（通用域）** | 可采购/外包 | 低 | 邮件发送、支付 |

### 识别问题
1. 什么让我们与众不同？ → Core
2. 我们需要但不专长的是什么？ → Supporting
3. 所有人都一样需要的是什么？ → Generic
