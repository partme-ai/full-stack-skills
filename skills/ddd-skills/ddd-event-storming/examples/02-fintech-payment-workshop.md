# 案例：金融支付领域事件风暴工作坊

## 基本信息

- **领域**: 金融科技 — 支付清算
- **日期**: 2024-08-20
- **时长**: 4 小时
- **参与角色**: 业务专家(3)、产品经理(1)、架构师(2)、开发(4)、合规(1)

## Step 1：混沌探索 — 领域事件清单

### 主线事件
```
🟠 支付指令已接收    🟠 风控检查已完成
🟠 账户余额已锁定    🟠 支付已处理
🟠 清算已发起        🟠 结算已完成
🟠 商户已收到款      🟠 交易对账已通过
🟠 支付通知已发送    🟠 凭证已生成
```

### 异常事件
```
🟠 风控规则已触发    🟠 支付已拒绝
🟠 余额已不足        🟠 余额已解锁
🟠 清算已失败        🟠 交易已冲正
🟠 对账已失败        🟠 差错已上报
🟠 退款已发起        🟠 退款已完成
```

## Step 2：时间线排序

```
Happy Path:
  🟠 支付指令已接收 → 🟠 风控检查已完成 → 🟠 账户余额已锁定 → 🟠 支付已处理
  → 🟠 清算已发起 → 🟠 结算已完成 → 🟠 商户已收到款 → 🟠 交易对账已通过

异常路径:
  🟠 支付指令已接收 → 🟠 风控规则已触发 → 🟠 支付已拒绝
  🟠 账户余额已锁定 → 🟠 余额已不足 → 🟠 余额已解锁 → 🟠 交易已冲正
```

## Step 3：关键事件

| 关键事件 | 重要性 |
|---------|--------|
| ★ 风控检查已完成 | 决定交易是否继续的转折点 |
| ★ 支付已处理 | 资金实际发生转移的节点 |
| ★ 交易对账已通过 | 日终结算确认，影响资金安全 |

## Step 4：命令与角色

```
👤 用户       → 🔵 Submit Payment        → 🟠 PaymentInstructionReceived
🤖 风控系统   → 🔵 Approve / Reject      → 🟠 RiskCheckCompleted / RiskTriggered
👤 系统       → 🔵 Lock Balance           → 🟠 BalanceLocked
👤 系统       → 🔵 Process Payment        → 🟠 PaymentProcessed
🔴 银联       → →                         → 🟠 ClearingCompleted
👤 系统       → 🔵 Settle                 → 🟠 SettlementCompleted
🤖 定时任务   → 🔵 Daily Reconciliation   → 🟠 ReconciliationPassed / Failed
```

## Step 5：聚合发现

```
┌─ Payment Aggregate ───────────────────────┐
│ 🟠 PaymentInstructionReceived              │
│ 🟠 PaymentProcessed / Rejected            │
│ 🟠 PaymentReversed                        │
│ 🔵 SubmitPayment / Approve / Reverse      │
│ 👤 User / RiskSystem                      │
│ 聚合根: Payment                           │
│ 不变式: 已拒绝的支付不可再次提交          │
└────────────────────────────────────────────┘

┌─ Settlement Aggregate ─────────────────────┐
│ 🟠 ClearingCompleted / SettlementCompleted │
│ 🟠 ReconciliationPassed / Failed           │
│ 🟠 SettlementReversed                     │
│ 🔵 Settle / Reconcile                     │
│ 聚合根: Settlement                        │
└────────────────────────────────────────────┘
```

## Step 6：限界上下文划分

```
┌─ Payment Context ──┐ → ┌─ Settlement Context ──┐ → ┌─ Notification Context ──┐
│ Payment Aggregate  │   │ Settlement Aggregate  │   │ Notification Aggregate  │
│ (Core Domain)      │   │ (Core Domain)         │   │ (Supporting Domain)    │
└────────────────────┘   └───────────────────────┘   └────────────────────────┘
```

## Workshop 产出建议

1. **支付聚合** 包含指令、处理、冲正 — 事务一致性边界
2. **结算聚合** 包含清算、结算、对账 — 日终批量处理
3. **风控** 作为外部系统（粉色便签）与 Payment Context 通过 ACL 集成
4. **Hot Spots**: 日切时间点、跨行清算超时、退款场景的资金归属
