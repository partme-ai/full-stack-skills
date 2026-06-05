# 支付领域设计示例

## 业务概述

支付系统核心流程：用户发起支付 → 资金从用户账户转移到商户账户 → 记录交易流水。支持多种支付方式（余额、银行卡、第三方支付）。

## 限界上下文划分

| 上下文 | 职责 | 聚合 |
|--------|------|------|
| **Payment** | 支付交易核心 | PaymentOrder, PaymentMethod |
| **Settlement** | 资金结算与对账 | SettlementAccount, Transaction |
| **Refund** | 退款处理 | RefundOrder |
| **Account** | 账户资金管理 | Account, Ledger |

## 聚合设计

### 1. PaymentOrder 聚合

| 角色 | 名称 | 类型 | 描述 |
|------|------|------|------|
| **聚合根** | PaymentOrder | Entity | 支付单，包含支付金额、状态、支付方式 |
| 实体 | PaymentItem | Entity | 支付明细（拆单场景） |
| 值对象 | Money | VO | 金额（币种 + 数值） |
| 值对象 | PaymentResult | VO | 支付结果（流水号、支付时间） |
| 领域事件 | PaymentCompleted | Event | 支付完成通知 |
| 领域事件 | PaymentFailed | Event | 支付失败通知 |

**不变式**：
- PaymentOrder.amount > 0
- 一个 PaymentOrder 只有一个 PaymentResult
- 状态流转：PENDING → PROCESSING → SUCCESS/FAILED

### 2. Account 聚合

| 角色 | 名称 | 类型 | 描述 |
|------|------|------|------|
| **聚合根** | Account | Entity | 账户（用户/商户），记录余额 |
| 值对象 | Money | VO | 金额 |
| 领域事件 | AccountDebited | Event | 账户扣款 |
| 领域事件 | AccountCredited | Event | 账户入账 |

**不变式**：
- Account.balance ≥ 0（不允许透支）
- 扣款金额 ≤ 余额

## 上下文映射

```
Account ←[ACL]→ Payment（Account 通过防腐层向 Payment 提供查余额和扣款接口）
Payment ←[ACL]→ Settlement（Payment 通过防腐层向 Settlement 推送交易数据）
Settlement ←[ACL]→ Refund（Refund 通过防腐层调用 Settlement 的退款能力）
```

## 领域事件流程

```
用户发起支付 → PaymentOrderCreated
  → 调用 Account 扣款 → AccountDebited
    → PaymentOrder 状态变更为 SUCCESS → PaymentCompleted
      → Settlement 接收事件 → 生成 Transaction
        → 如果退款 → RefundRequested → AccountCredited
```

## 代码包结构

```
payment-domain/
├── payment/              # 支付聚合
│   ├── entity/           # PaymentOrder, PaymentItem
│   ├── valueobject/      # Money, PaymentResult
│   ├── event/            # PaymentCompleted, PaymentFailed
│   ├── service/          # PaymentValidationService
│   └── repository/       # PaymentOrderRepository
├── account/              # 账户聚合
│   ├── entity/           # Account
│   ├── valueobject/      # Money
│   ├── event/            # AccountDebited, AccountCredited
│   └── repository/       # AccountRepository
├── settlement/           # 结算聚合
│   └── ...
├── refund/               # 退款聚合
│   └── ...
└── shared/               # 共享值对象
    └── valueobject/      # Money, Currency
```
