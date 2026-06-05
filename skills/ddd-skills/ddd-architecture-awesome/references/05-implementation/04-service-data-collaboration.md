# Service & Data Collaboration — 服务与数据在各层的协作

## 四种服务类型

| 服务类型 | 所在层 | 职责 | 调用方 |
|----------|--------|------|--------|
| **Facade 服务** | interfaces | 请求解析、DTO转换 | 前端/API网关 |
| **应用服务** | application | 编排、事务、权限、事件 | Facade |
| **领域服务** | domain | 跨实体的核心业务逻辑 | 应用服务 |
| **基础服务** | infrastructure | 数据持久化、消息、缓存 | 领域服务/应用服务 |

## 服务调用路径

```
前端应用
  ↓ HTTP
API网关
  ↓
Facade (interfaces) — 请求解析 → 调用应用服务
  ↓
应用服务 (application) — 编排调用
  ├──→ 领域服务 (domain) — 核心业务逻辑
  │      ├──→ 实体方法 (domain) — 原子业务逻辑
  │      └──→ 仓储接口 (domain) — 数据访问抽象
  │             └──→ 仓储实现 (infrastructure) — 实际DB操作
  └──→ 外部微服务应用服务 — 跨服务调用
```

## 跨聚合服务编排

```
✅ 正确: 应用层编排

class OrderAppService {
    void placeOrder(PlaceOrderCommand cmd) {
        // 编排多个聚合的领域服务
        Order order = orderDomainService.create(cmd);
        Inventory inventory = inventoryDomainService.reserve(cmd.items);
        paymentDomainService.initiate(order.id(), order.totalAmount());
    }
}

❌ 错误: 聚合间直接调用

class Order {
    void place() {
        inventoryService.reserve(items); // 跨聚合直接调用！
    }
}
```

## 严格分层下的服务封装

```
底层 → 上层 必须逐级封装：

实体方法 (最底层)
  ↓ 封装为
领域服务
  ↓ 封装为
应用服务
  ↓ 暴露给
Facade (用户接口层)

不允许跨层暴露：实体方法不能直接暴露给应用服务
```

## 数据对象转换链

```
PO (Persistent Object)     ←→ 数据库表，基础层
  ↓↑ Repository转换
DO (Domain Object)          ←→ 领域层，运行时实体
  ↓↑ Assembler转换
DTO (Data Transfer Object)  ←→ 应用层/接口层，传输载体
  ↓↑ 前端转换
VO (View Object)            ←→ 前端展示
```

| 对象 | 所在层 | 职责 | 特点 |
|------|--------|------|------|
| **PO** | infrastructure | 与数据库表一一映射 | 只做数据载体，无业务逻辑 |
| **DO** | domain | 运行时实体和值对象 | 充血模型，承载业务行为 |
| **DTO** | interfaces/application | 层间和微服务间传输 | 隔离内部领域对象 |
| **VO** | 前端 | 展示层数据封装 | 按页面/组件定制 |

## 转换关系

```
大多数情况：PO 与 DO 一对一
特殊场景：
├── DO → 多个 PO（实体属性分散在多表）
├── 多个 PO → DO（数据聚合初始化）
└── DTO → 多个 DO（Facade 组装多个聚合数据）
```

## 层间调用规则总结

```
interfaces → 只能调 application
application → 调 domain service + infrastructure(基础设施)
domain → 只能调 domain（自身实体+领域服务+仓储接口）
infrastructure → 实现 domain 定义的接口，可调外部资源

调用的数据格式：
interfaces 传 DTO → application 转 DO → domain 处理 DO
domain 返 DO → application 转 DTO → interfaces 传 DTO
```
