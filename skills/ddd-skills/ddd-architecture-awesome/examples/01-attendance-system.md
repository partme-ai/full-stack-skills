# 考勤请假系统 — DDD 端到端全流程案例

> 来源：极客时间 DDD实战课 第18讲 | 展示从战略设计到战术设计的完整过程

## 项目背景

在线请假考勤系统：请假人提交审批 → 逐级核批 → 考勤统计。同时支持内外网，内外部人员无差异管理。

## 一、战略设计（事件风暴）

### 1.1 场景分析

| 场景 | 角色 | 关键操作 |
|------|------|----------|
| 请假 | 请假人 | 创建请假单 → 提交审批 |
| 审批 | 审批人 | 获取待审批列表 → 逐级审批 |
| 考勤 | 系统 | 核销请假数据 → 输出考勤统计 |

### 1.2 领域对象提取

| 实体/值对象 | 类型 | 来源 |
|------------|------|------|
| 请假单 | 聚合根 | 请假场景 |
| 审批意见 | 实体 | 审批场景 |
| 审批规则 | 值对象 | 审批场景 |
| 人员 | 聚合根 | 人员组织场景 |
| 组织关系 | 实体 | 人员组织场景 |
| 刷卡明细 | 实体 | 考勤场景 |
| 考勤明细 | 实体 | 考勤场景 |
| 考勤统计 | 实体 | 考勤场景 |

### 1.3 聚合设计

```
请假聚合：
├── 请假单 (聚合根)
│   ├── 属性：请假类型、起止时间、天数
│   ├── 方法：create(), submit(), approve(), reject()
│   └── 值对象：请假人、审批人、请假类型、审批状态、审批规则
├── 审批意见 (实体) — 多级审批产生多条
│   ├── 属性：审批人、审批状态、审批意见
│   └── 方法：agree(), reject()
└── 审批规则 (值对象)
    └── 根据请假类型和天数确定审批层级

人员组织关系聚合：
├── 人员 (聚合根)
│   ├── 属性：姓名、工号、岗位、部门
│   └── 方法：getSupervisor(orgType)
└── 组织关系 (实体)
    └── 属性：组织关系类型、上级领导

考勤聚合：(非典型聚合，无聚合根)
├── 刷卡明细 (实体)
├── 考勤明细 (实体) — 核销请假后生成
└── 考勤统计 (实体) — 汇总计算
```

### 1.4 限界上下文 & 微服务拆分

| 限界上下文 | 包含聚合 | 微服务 | 拆分理由 |
|-----------|----------|:---:|------|
| 请假上下文 | 请假 + 人员组织关系 | ✓ 请假微服务 | 共同完成请假功能 |
| 考勤上下文 | 考勤 | ✓ 考勤微服务 | 职责单一 |

## 二、战术设计（请假微服务为例）

### 2.1 服务识别

```
提交审批流程：
├── 应用服务：LeaveApplicationService.submitForApproval(leaveId)
├── 领域服务：
│   ├── ApprovalRuleService.getApprovalRule(leaveType, duration) → 审批规则
│   │   └── ApprovalRule.queryRule(leaveType, duration)
│   └── PersonService.getApprover(roleType) → 审批人
│       └── Person.getSupervisor(orgType)
└── 实体方法：
    └── Leave.assignApprover(approver, rule) → 分配审批人并保存规则
```

### 2.2 领域事件

| 事件 | 触发时机 | 后续操作 |
|------|----------|----------|
| LeaveSubmitted | 请假单提交 | 通知审批人 |
| LeaveApproved | 审批通过 | 发送请假数据到考勤微服务 |
| LeaveRejected | 审批驳回 | 通知请假人 |

### 2.3 代码结构

```
leave-microservice/
├── interfaces/
│   ├── controller/LeaveController.java
│   ├── dto/LeaveDTO.java, ApprovalDTO.java
│   └── assembler/LeaveAssembler.java
├── application/
│   ├── service/LeaveAppService.java          # 编排
│   └── event/publish/LeaveEventPublisher.java
├── domain/
│   ├── leave/                                # 请假聚合
│   │   ├── entity/Leave.java (聚合根), Approval.java (实体)
│   │   ├── vo/LeaveType.java, ApprovalStatus.java, Approver.java
│   │   ├── service/ApprovalRuleService.java
│   │   ├── event/LeaveSubmittedEvent.java, LeaveApprovedEvent.java
│   │   └── repository/LeaveRepository.java (接口)
│   └── person/                               # 人员组织关系聚合
│       ├── entity/Person.java (聚合根), OrgRelation.java (实体)
│       ├── vo/OrgType.java
│       ├── service/PersonService.java
│       └── repository/PersonRepository.java (接口)
└── infrastructure/
    ├── persistence/
    │   ├── LeaveRepositoryImpl.java
    │   └── PersonRepositoryImpl.java
    └── config/
```

### 2.4 关键代码

```java
// 聚合根 — 请假单
public class Leave extends AggregateRoot<LeaveId> {
    private LeaveId id;
    private Applicant applicant;
    private LeaveType type;
    private LocalDate startDate, endDate;
    private LeaveStatus status;
    private List<Approval> approvals = new ArrayList<>();
    private ApprovalRule rule;

    public void submit() {
        if (status != LeaveStatus.DRAFT) throw new LeaveException("Only DRAFT can submit");
        this.status = LeaveStatus.SUBMITTED;
        addDomainEvent(new LeaveSubmittedEvent(this.id, this.applicant, this.type));
    }

    public void assignApprover(Approver approver, ApprovalRule rule) {
        this.rule = rule;
        this.approvals.add(new Approval(approver, ApprovalStatus.PENDING));
    }

    public void approve(Approver approver, String comment) {
        Approval current = findPendingApproval(approver);
        current.approve(comment);
        Approval next = rule.getNextLevel(this.approvals.size());
        if (next == null) {
            this.status = LeaveStatus.APPROVED;
            addDomainEvent(new LeaveApprovedEvent(this.id));
        } else {
            this.approvals.add(next);
        }
    }
}
```

## 三、从本案例学到的关键点

1. **非典型聚合处理**：考勤聚合无聚合根，仍用聚合封装，照常设计实体和仓储
2. **聚合间通过应用层编排**：请假提交审批需要请假聚合 + 人员聚合协作，通过应用服务编排
3. **领域事件驱动跨微服务**：审批通过后通过事件将请假数据发到考勤微服务
4. **聚合是微服务演进的最小单位**：人员组织关系聚合可随时从请假微服务中独立出来
