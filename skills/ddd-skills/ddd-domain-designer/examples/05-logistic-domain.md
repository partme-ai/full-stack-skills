# 物流领域设计示例

## 业务概述

物流系统核心业务：订单履约 → 仓储拣货 → 运输配送 → 签收完成。涉及仓库管理、运输调度、配送路线规划等。

## 限界上下文划分

| 上下文 | 职责 | 聚合 |
|--------|------|------|
| **Fulfillment** | 订单履约执行 | FulfillmentOrder, Dispatch |
| **Warehouse** | 仓储管理 | Inventory, StockMovement |
| **Transportation** | 运输管理 | Shipment, RoutePlan |
| **Delivery** | 末端配送 | DeliveryOrder, DeliveryTask |
| **Tracking** | 物流追踪 | TrackingRecord |

## 聚合设计

### 1. FulfillmentOrder 聚合

| 角色 | 名称 | 类型 | 描述 |
|------|------|------|------|
| **聚合根** | FulfillmentOrder | Entity | 履约单，关联原始订单和物流 |
| 实体 | FulfillmentItem | Entity | 履约商品明细 |
| 值对象 | Address | VO | 收货地址 |
| 领域事件 | FulfillmentCreated | Event | 履约单已创建 |
| 领域事件 | FulfillmentCompleted | Event | 履约已完成 |

**不变式**：
- FulfillmentItem.quantity ≤ Inventory.availableQuantity
- 一个 FulfillmentOrder 必须关联至少一个 FulfillmentItem
- 状态流转：CREATED → PICKING → PACKED → SHIPPED → DELIVERED

### 2. Shipment 聚合

| 角色 | 名称 | 类型 | 描述 |
|------|------|------|------|
| **聚合根** | Shipment | Entity | 运单，描述一次运输任务 |
| 实体 | ShipmentStop | Entity | 运输节点（装货/卸货点） |
| 值对象 | GeoLocation | VO | 地理位置（经纬度） |
| 值对象 | TimeWindow | VO | 时间窗口 |
| 领域事件 | ShipmentDispatched | Event | 运单已发车 |
| 领域事件 | ShipmentArrived | Event | 运单已到达 |

**不变式**：
- Shipment 必须有 ≥ 1 个装货点和 ≥ 1 个卸货点
- 运输路线顺序不能矛盾（按时间窗口排序）
- ShipmentStop 的时间窗口不可重叠

## 上下文映射

```
Fulfillment ←[Partnership]→ Warehouse（紧密配合，一起规划拣货）
Fulfillment ←[Customer-Supplier]→ Transportation（Fulfillment 定义运输需求，Transportation 执行）
Transportation ←[Customer-Supplier]→ Delivery（Transportation 将货物送达配送站）
Fulfillment →[OHS]→ Tracking（开放物流数据给 Tracking 上下文做追踪）
```

## 领域事件流程

```
订单创建 → FulfillmentCreated
  → Warehouse 接收 → InventoryReserved
    → Picking → StockConfirmed
      → ShipmentCreated → ShipmentDispatched
        → DeliveryOrderCreated → Delivered
          → FulfillmentCompleted
```

## 代码包结构

```
logistic-domain/
├── fulfillment/          # 履约聚合
│   ├── entity/           # FulfillmentOrder, FulfillmentItem
│   ├── valueobject/      # Address
│   ├── event/            # FulfillmentCreated, FulfillmentCompleted
│   ├── service/          # FulfillmentSplitService
│   └── repository/       # FulfillmentOrderRepository
├── warehouse/            # 仓储聚合
│   ├── entity/           # Inventory, StockMovement
│   ├── valueobject/      # SkuCode, LocationCode
│   ├── event/            # InventoryReserved, StockConfirmed
│   └── repository/       # InventoryRepository
├── transportation/       # 运输聚合
│   ├── entity/           # Shipment, ShipmentStop
│   ├── valueobject/      # GeoLocation, TimeWindow
│   ├── event/            # ShipmentDispatched, ShipmentArrived
│   └── repository/       # ShipmentRepository
├── delivery/             # 配送聚合
├── tracking/             # 追踪聚合
└── shared/               # 共享值对象
    └── valueobject/      # Address, GeoLocation, TimeWindow
```
