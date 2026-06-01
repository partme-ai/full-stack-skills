# 领域对象 → 代码对象映射指南

## 映射流程

```
事件风暴领域对象
  → 整理领域对象清单（聚合、实体、事件、命令）
    → 用户故事/领域故事分析
      → 设计代码对象（充血模型实体、值对象、仓储接口）
        → 确定分层归属
          → 建立领域对象 → 代码对象映射表
```

## 领域对象整理表模板

| 领域模型 | 聚合 | 领域对象 | 领域类型 |
|---------|------|---------|---------|
| 投保模型 | 投保聚合 | 投保单 | 聚合根 |
| 投保模型 | 投保聚合 | 被保人 | 实体 |
| 投保模型 | 投保聚合 | 证件类型 | 值对象 |
| 投保模型 | 投保聚合 | 投保单已创建 | 领域事件 |
| 投保模型 | 投保聚合 | 提交投保 | 命令 |

## 领域对象 → 代码对象映射表

| 层 | 领域对象 | 领域类型 | 依赖对象 | 包名 | 类名 | 方法名 |
|----|---------|---------|---------|------|------|--------|
| Domain | 个人客户 | 聚合根 | 地址, 电话 | domain.customer.entity | Customer | create, update |
| Domain | 地址 | 实体 | 无 | domain.customer.entity | Address | change |
| Domain | 客户类型 | 值对象 | 无 | domain.customer.entity | CustomerType | — |
| Domain | 客户已创建 | 领域事件 | 个人客户 | domain.customer.event | CustomerCreated | — |
| Domain | 创建客户 | 领域服务 | 个人客户, 地址 | domain.customer.service | CustomerDomainService | createCustomer |
| Domain | 客户仓储 | 仓储接口 | 个人客户 | domain.customer.repository | CustomerRepository | save, findById |
| App | 创建客户 | 应用服务 | 领域服务 | application.service | CustomerAppService | createCustomer |
| App | 客户已创建 | 事件发布 | 领域事件 | application.event.publish | CustomerEventPublisher | publish |
| Interface | 创建客户 DTO | DTO | — | interfaces.dto | CreateCustomerRequest | — |
| Interface | 客户 Controller | Controller | — | interfaces.controller | CustomerController | create |
| Infra | 客户仓储实现 | 仓储实现 | — | infrastructure.repository | CustomerRepositoryImpl | save |

## 服务分层与调用规则

```
严格分层模式（推荐）：

Interface → Application → Domain Service → Entity Method
                ↓                ↓
          Infrastructure     Repository (接口在 Domain)

禁止：
  Interface → Domain（跨层）
  Interface → Infrastructure（跨层）
  Application → Entity Method（跨层，需经 Domain Service）
```

## 实体设计准则

| 准则 | 做法 |
|------|------|
| 充血模型 | 实体内实现业务方法，不只是 getter/setter |
| 值对象 vs 实体 | 有独立生命周期 + 需要查询统计 → 实体；只读不修改 → 值对象 |
| 实体方法暴露 | 实体方法 → 领域服务封装 → 应用服务封装（逐层暴露） |
| 服务去重 | 应用服务反复编排相同领域服务 → 合并为一个领域服务 |

## 非典型模型处理（无聚合根场景）

```
场景：客户归并（扫描所有客户，按身份证/电话去重）
→ 无聚合根

处理：
  - 仍用聚合概念组织代码（domain.customer.merge/）
  - 实体仍设计属性和行为方法
  - 设计仓储接口和领域服务
  - 只是没有聚合根来管理生命周期

原则：找不到聚合根不影响使用 DDD 其他方法（实体、值对象、仓储、领域服务）
```

## 常见错误

| 错误 | 修复 |
|------|------|
| 领域对象和数据库表一一对应 | 领域模型驱动，不是数据模型驱动 |
| 所有方法都在实体上 | 跨实体逻辑放入领域服务 |
| Interface 直接调 Repository | 必须经过 Application Service |
| 把领域事件发布放在 Domain 层 | 发布订阅在 App 层，事件定义在 Domain 层 |
