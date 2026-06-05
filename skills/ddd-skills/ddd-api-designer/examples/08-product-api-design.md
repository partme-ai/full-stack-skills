# 商品服务 API 设计案例

> 商品限界上下文（Product BC）的 REST API 设计，展示商品管理、分类查询等场景。

## 领域模型

```
Product (Aggregate Root)
├── ProductId
├── Sku
├── Title / Description
├── Price / CostPrice
├── CategoryId
└── ProductStatus: DRAFT / ONLINE / OFFLINE / DELETED
```

## 端点设计

| 端点 | 类型 | 说明 |
|------|------|------|
| `POST /api/v1/products` | Command | 创建商品 |
| `PUT /api/v1/products/{id}` | Command | 更新商品 |
| `PUT /api/v1/products/{id}/online` | Command | 上架 |
| `PUT /api/v1/products/{id}/offline` | Command | 下架 |
| `GET /api/v1/products/{id}` | Query | 商品详情 DTO |
| `GET /api/v1/products?category=&page=&size=` | Query | 商品列表（分页） |

## DTO 设计

- `ProductDetailDTO`：详情页（含描述、规格）
- `ProductSummaryDTO`：列表页（标题、价格、封面图）
- `ProductCreateCommand`：创建请求
