# 通知 CQRS — CQRS 化推送

> 事件 → 通知投影，L2 级别，Redis 缓冲

```java
// 事件 → 通知创建
@Component
public class OrderNotificationProjector {
    @EventListener
    public void on(OrderShippedEvent event) {
        Notification notif = new Notification(
            event.getCustomerId(),
            "订单已发货",
            "您的订单 " + event.getOrderId() + " 已发出"
        );
        notificationRepo.save(notif);
    }
}

// 通知查询
@Service
public class NotificationQueryService {
    public List<NotificationDTO> getUnread(String customerId) {
        return notificationRepo.findUnreadByCustomer(customerId);
    }
}
```
