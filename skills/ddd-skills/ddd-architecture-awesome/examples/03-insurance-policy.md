# 保险投保系统 — DDD 聚合设计深度案例

基于 DDD 的保险投保系统，重点展示复杂聚合的设计方法。

## 业务背景

保险投保核心流程：
- 用户创建投保单 → 选择险种 → 填写标的信息 → 填入被保人 → 核保 → 缴费 → 出单
- 涉及多个参与方：投保人、被保人、受益人
- 复杂的业务规则：年龄校验、健康告知、保额计算、费率表

## 领域划分

| 域 | 类型 | 说明 |
|----|------|------|
| 投保域 | Core Domain | 投保流程、核保规则，核心竞争优势 |
| 产品域 | Supporting | 险种定义、费率表，相对稳定 |
| 核保域 | Core Domain | 风险评估、健康告知，核心决策能力 |
| 支付域 | Generic | 通用支付能力 |

## 限界上下文

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Proposal BC  │────→│ Underwrite BC│────→│  Reinsure BC │
│  (投保上下文)  │     │  (核保上下文)  │     │  (再保上下文)  │
└──────┬───────┘     └──────┬───────┘     └──────────────┘
       │                    │
       ↓                    ↓
┌──────────────┐     ┌──────────────┐
│ Product BC   │     │ Payment BC   │
│  (产品上下文)  │     │  (支付上下文)  │
└──────────────┘     └──────────────┘
```

## 聚合设计 — 重点

### 投保单聚合（Proposal Aggregate）

这是一个典型的**复杂聚合**，包含多个实体和值对象：

```
Proposal (聚合根)
├── ProposalId (VO)
├── ProposalStatus (VO: DRAFT → SUBMITTED → UNDERWRITING → APPROVED → PAID → ISSUED)
├── Applicant (VO: 投保人信息)
│   ├── Name, IDNumber, Phone, Address
├── List<Insured> (Entity: 被保人)
│   ├── InsuredId
│   ├── Name, IDNumber, Age, Gender
│   ├── HealthDeclaration (VO: 健康告知)
│   └── Occupation (VO)
├── List<Coverage> (Entity: 险种)
│   ├── ProductId (VO — 外部引用)
│   ├── Money sumInsured (VO: 保额)
│   └── Money premium (VO: 保费)
├── List<Beneficiary> (VO: 受益人 — 不可变，无独立生命周期)
├── ── 行为 ──
├── void addInsured(Insured)
├── void addCoverage(ProductId, Money sumInsured)
├── void calculatePremium(RateTable)   // 保费计算
├── void submit()                       // 提交核保
├── void approve()                      // 核保通过
├── void reject(String reason)          // 核保拒绝
└── ── 事件 ──
    ├── ProposalSubmittedEvent
    ├── UnderwritingApprovedEvent
    └── PolicyIssuedEvent
```

### 聚合设计决策分析

| 问题 | 决策 | 理由 |
|------|------|------|
| Insured 是实体还是值对象？ | Entity | 有独立 ID，会被多次引用 |
| Beneficiary 是实体还是值对象？ | VO | 无独立生命周期，随投保单变化 |
| Coverage 放在哪个聚合？ | Proposal 内 | 保额、保费与投保单强一致 |
| Product 怎么引用？ | 仅通过 ProductId | 产品自身变更不应影响已有投保单 |
| 核保结果怎么通知？ | 领域事件 | 核保是独立 BC，异步通知结果 |

### 聚合大小分析

| 指标 | 值 | 评估 |
|------|-----|------|
| 每聚合实体数 | 3 (Insured, Coverage — 实体; Beneficiary — VO) | ✅ 健康 |
| 聚合根代码行数 | ~200 | ✅ 健康 |
| 事务锁时间 | <50ms | ✅ 健康 |

### 为什么 Coverage 放在 Proposal 而非独立聚合？

1. **一致性要求**：保额和保费的修改必须和投保单状态保持强一致
2. **不变量**：投保单提交时，所有 Coverage 的 premium 总和必须等于 totalPremium
3. **生命周期**：Coverage 随投保单创建和销毁，无独立生命周期

## 领域服务

```java
// PremiumCalculator — 保费计算（跨实体逻辑，不适合放在聚合根或实体中）
public class PremiumCalculator {
    public Money calculate(Insured insured, ProductId product, Money sumInsured, RateTable rateTable) {
        // 1. 根据被保人年龄查费率
        BigDecimal rate = rateTable.findRate(insured.getAge(), product);
        // 2. 根据职业类别调整系数
        BigDecimal occupationFactor = insured.getOccupation().getFactor();
        // 3. 计算保费 = 保额 × 费率 × 职业系数
        return sumInsured.multiply(rate).multiply(occupationFactor);
    }
}
```

## 分层架构代码示例

```java
// Domain Layer — 聚合根
public class Proposal extends AggregateRoot<ProposalId> {
    private Applicant applicant;
    private List<Insured> insureds = new ArrayList<>();
    private List<Coverage> coverages = new ArrayList<>();
    private List<Beneficiary> beneficiaries = new ArrayList<>();
    private ProposalStatus status = ProposalStatus.DRAFT;

    public void addCoverage(ProductId productId, Money sumInsured, RateTable rateTable) {
        if (status != ProposalStatus.DRAFT) {
            throw new ProposalException("Only draft proposals can modify coverage");
        }
        Coverage coverage = new Coverage(productId, sumInsured);
        for (Insured insured : insureds) {
            Money premium = new PremiumCalculator()
                .calculate(insured, productId, sumInsured, rateTable);
            coverage.addPremium(insured.getId(), premium);
        }
        this.coverages.add(coverage);
    }

    public void submit() {
        if (insureds.isEmpty()) throw new ProposalException("At least one insured required");
        if (coverages.isEmpty()) throw new ProposalException("At least one coverage required");
        this.status = ProposalStatus.SUBMITTED;
        addDomainEvent(new ProposalSubmittedEvent(this.id));
    }
}
```

## 从本案例学到的 DDD 关键点

1. **聚合边界决策**：不是越细越好，要根据一致性要求和不变量来判断
2. **实体 vs 值对象**：关键在于是否有独立标识和生命周期
3. **领域服务**：跨实体的计算逻辑（如保费计算）放入领域服务，保持实体纯粹
4. **聚合大小权衡**：3 个实体是健康范围，超出 5 个实体需要警惕
5. **ID 引用外部聚合**：Product 只用 ProductId 引用，避免跨聚合直接依赖
