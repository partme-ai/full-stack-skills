# 银行账户 Event Sourcing

> 存款/取款事件溯源，L3 级别，审计追踪

```java
// 事件
public class MoneyDepositedEvent extends DomainEvent {
    public final BigDecimal amount;
    public final BigDecimal newBalance;
}
public class MoneyWithdrawnEvent extends DomainEvent {
    public final BigDecimal amount;
    public final BigDecimal newBalance;
}

// 事件溯源聚合
public class BankAccount extends EventSourcedAggregate {
    private BigDecimal balance;

    public void deposit(BigDecimal amount) {
        apply(new MoneyDepositedEvent(this.id, amount, balance.add(amount)));
    }

    public void withdraw(BigDecimal amount) {
        if (balance.compareTo(amount) < 0) throw new InsufficientFundsException();
        apply(new MoneyWithdrawnEvent(this.id, amount, balance.subtract(amount)));
    }

    @Override
    protected void when(DomainEvent event) {
        if (event instanceof MoneyDepositedEvent e) this.balance = e.newBalance;
        else if (event instanceof MoneyWithdrawnEvent e) this.balance = e.newBalance;
    }
}

// 投影：账户余额视图
@Component
public class AccountBalanceProjector {
    @EventListener
    public void on(MoneyDepositedEvent e) {
        jdbc.update("UPDATE account_balance SET balance = ? WHERE id = ?",
            e.newBalance, e.getAggregateId());
    }
}
```
