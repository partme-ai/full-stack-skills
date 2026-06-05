# COLA 示例：Extension Point 扩展点机制

> COLA v5 最核心的新特性。通过扩展点实现业务维度的差异化逻辑。

## 场景说明

订单价格计算规则，不同会员级别（普通/VIP/企业）有不同的折扣策略。

## 扩展点定义

```java
// 1. 定义扩展点接口（放在 app/extension/point/）
@ExtensionPoint
public interface OrderPriceCalculateExtPt {
    /**
     * 计算订单最终价格
     * @param order 订单领域对象
     * @param basePrice 基础价格
     * @return 最终价格
     */
    Money calculate(Order order, Money basePrice);
}
```

## 扩展点实现

```java
// 2. 普通会员 —— 无折扣
@Extension(bizId = "normalOrder")
public class NormalOrderPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculate(Order order, Money basePrice) {
        return basePrice;  // 原价
    }
}

// 3. VIP 会员 —— 9 折
@Extension(bizId = "vipOrder")
public class VipOrderPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculate(Order order, Money basePrice) {
        return basePrice.multiply(0.9)  // 九折
            .setScale(2, RoundingMode.HALF_UP);
    }
}

// 4. 企业会员 —— 8 折 + 满减
@Extension(bizId = "enterpriseOrder")
public class EnterpriseOrderPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculate(Order order, Money basePrice) {
        Money afterDiscount = basePrice.multiply(0.8);  // 八折
        if (afterDiscount.compareTo(new Money(10000, Currency.getInstance("CNY"))) >= 0) {
            afterDiscount = afterDiscount.subtract(new Money(500, Currency.getInstance("CNY")));
            // 满 10000 减 500
        }
        return afterDiscount.setScale(2, RoundingMode.HALF_UP);
    }
}
```

## 扩展点调用

```java
// 5. 在 App 层注入 ExtensionExecutor
@Component
public class OrderCreateCmdExe implements CommandExecutor<OrderCreateCmd, OrderDTO> {
    @Resource
    private ExtensionExecutor extensionExecutor;

    @Override
    @Transactional
    public OrderDTO execute(OrderCreateCmd cmd) {
        Order order = Order.create(/* ... */);
        Money basePrice = order.getTotalAmount();

        // 根据业务身份（bizId）自动路由到对应的扩展实现
        Money finalPrice = extensionExecutor.execute(
            OrderPriceCalculateExtPt.class,   // 扩展点接口
            cmd.getBizId(),                    // 业务身份（normal/vip/enterprise）
            ext -> ext.calculate(order, basePrice)
        );

        // 使用 finalPrice 进行后续处理
        return OrderAssembler.toDTO(order);
    }
}
```

## 业务身份注入

```java
// 6. 前端请求携带业务身份
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    @PostMapping
    public Response<OrderDTO> create(
            @RequestHeader(value = "X-Biz-Id", defaultValue = "normalOrder") String bizId,
            @Valid @RequestBody OrderCreateRequest request) {
        request.setBizId(bizId);
        return Response.success(orderCreateCmdExe.execute(request.toCommand()));
    }
}
```

## 扩展点最佳实践

| 实践 | 说明 |
|------|------|
| **接口粒度** | 一个扩展点只做一件事，如价格计算、库存校验 |
| **默认实现** | 必须提供默认实现（普通场景），新增扩展不影响已有逻辑 |
| **测试覆盖** | 每个扩展实现都应有独立单元测试 |
| **无状态** | 扩展实现应为无状态，通过参数传递上下文 |
| **日志记录** | 在扩展执行器层记录扩展路由日志，便于排查 |
