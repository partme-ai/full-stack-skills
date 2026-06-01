# DTO/VO/DO/PO 四层转换边界


## 对象定义与位置

| 对象 | 全称 | 层级 | 职责 |
|------|------|------|------|
| **DO** | Domain Object | Domain 层 | 充血模型，含业务行为 |
| **DTO** | Data Transfer Object | Application/Adapter | 跨层/跨服务传输 |
| **VO** | View Object | Adapter 层 | 面向页面展示 |
| **PO** | Persistent Object | Infrastructure | 数据库映射 |

## 转换链

```
Frontend VO ↔ Adapter DTO ↔ Application DO ↔ Infrastructure PO
```

## 转换规则

### DO → DTO
```java
public class OrderAssembler {
    public static OrderDTO toDTO(Order order) {
        return OrderDTO.builder()
            .orderId(order.getId().getValue())
            .status(order.getStatus().name())
            .total(order.getTotalAmount().toString())
            .items(order.getItems().stream().map(OrderAssembler::toItemDTO).toList())
            .build();
    }
}
```

### PO → DO（仓储完成）
```java
// Infrastructure 层
public class JpaOrderRepository implements OrderRepository {
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue())
            .map(OrderMapper::toDomain);  // PO → DO
    }
}
```

### DO → PO（仓储完成）
```java
public void save(Order order) {
    OrderPO po = OrderMapper.toPO(order);  // DO → PO
    jpaRepo.save(po);
}
```

## 转换位置约定

| 转换 | 位置 | 工具 |
|------|------|------|
| PO ↔ DO | Infrastructure Repository | Mapper/Converter |
| DO → DTO | Application Assembler | Assembler |
| DTO ↔ VO | Adapter Controller | WebConverter |

## 一个 DO → 多个 DTO

同一个 Order 聚合根可以产出：
- `OrderDetailDTO` — 详情页（完整字段）
- `OrderSummaryDTO` — 列表页（精简字段）
- `OrderExportDTO` — 导出（特定字段）

每个 DTO 面向特定场景，避免"万能 DTO"。

