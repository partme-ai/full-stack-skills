# 库存服务 API 设计案例

> 库存限界上下文（Inventory BC）的 REST API 设计，展示库存扣减、锁定、释放等 CQRS 场景。

## 领域模型

```
Inventory (Aggregate Root)
├── SkuId
├── AvailableQty
├── LockedQty
└── WarehouseCode
```

## 端点设计

| 端点 | 类型 | 说明 |
|------|------|------|
| `POST /api/v1/inventory/lock` | Command | 锁定库存（下单） |
| `POST /api/v1/inventory/release` | Command | 释放库存（取消） |
| `POST /api/v1/inventory/deduct` | Command | 扣减库存（支付） |
| `GET /api/v1/inventory/{skuId}` | Query | 库存查询 |
| `GET /api/v1/inventory/warehouse/{code}` | Query | 仓库库存概览 |

## 幂等设计

锁定/扣减操作使用 `Idempotency-Key` 防止重复处理，服务端缓存 TTL 24h。
