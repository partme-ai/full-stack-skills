# 支付 CQRS — 事件驱动对账

> 支付命令 + 支付事件 → 对账视图，L2 级别

```java
// 支付命令
public class ProcessPaymentCommand {
    private final String orderId;
    private final BigDecimal amount;
}

// 支付事件 → 对账投影
@Component
public class PaymentEventHandler {
    @EventListener
    public void on(PaymentCompletedEvent event) {
        // 更新对账视图
        reconciliationRepo.recordPayment(
            event.getOrderId(), event.getAmount(), event.getPaidAt());
    }
}

// 对账查询
@Service
public class ReconciliationQueryService {
    public List<ReconciliationDTO> getDailyReport(LocalDate date) {
        return reconciliationRepo.findByDate(date);
    }
}
```
