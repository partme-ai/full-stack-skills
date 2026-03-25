---
name: oracle
description: "Guides Oracle database development including SQL, PL/SQL stored procedures, triggers, EXPLAIN PLAN optimization, AWR analysis, RMAN backup, RAC clustering, and Data Guard. Use when the user needs to write Oracle SQL, create PL/SQL procedures, tune query performance, or manage Oracle database administration."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write Oracle SQL or PL/SQL (stored procedures, functions, triggers, packages)
- Design tables, indexes, partitions, or constraints in Oracle
- Tune query performance with EXPLAIN PLAN, AWR, or ASH reports
- Manage Oracle administration (users, roles, tablespaces, RMAN backup)
- Configure RAC, Data Guard, or Oracle replication

## How to use this skill

### Workflow

1. **Identify the task** - SQL writing, PL/SQL development, performance tuning, or DBA operations
2. **Write the code** - Use the patterns below matching Oracle syntax
3. **Analyze performance** - Run EXPLAIN PLAN or review AWR snapshots
4. **Apply Oracle-specific best practices** - Bind variables, partitioning, RMAN

### Quick-Start Example: PL/SQL Procedure with Error Handling

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    p_from_acct  IN NUMBER,
    p_to_acct    IN NUMBER,
    p_amount     IN NUMBER
) AS
    v_balance NUMBER;
BEGIN
    -- Check source balance
    SELECT balance INTO v_balance
    FROM accounts WHERE account_id = p_from_acct
    FOR UPDATE;

    IF v_balance < p_amount THEN
        RAISE_APPLICATION_ERROR(-20001, 'Insufficient funds');
    END IF;

    UPDATE accounts SET balance = balance - p_amount WHERE account_id = p_from_acct;
    UPDATE accounts SET balance = balance + p_amount WHERE account_id = p_to_acct;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END transfer_funds;
/
```

### Performance Analysis

```sql
EXPLAIN PLAN FOR
SELECT /*+ INDEX(o idx_orders_date) */ * FROM orders o WHERE order_date > SYSDATE - 30;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

## Best Practices

1. **Use bind variables** - Prevent SQL injection and hard parsing; never concatenate user input into SQL
2. **Partition large tables** - Range partition on date columns; hash partition for even distribution
3. **RMAN backup strategy** - Full weekly + incremental daily; test restore procedures quarterly
4. **Monitor wait events** - Use AWR/ASH to identify I/O, latch, or lock contention
5. **Audit and secure** - Use Oracle Audit Vault; grant least-privilege roles; encrypt sensitive columns

## Keywords

oracle, PL/SQL, SQL*Plus, SQL Developer, RMAN, RAC, Data Guard, AWR, 关系型数据库, stored procedure, EXPLAIN PLAN, tablespace, 索引, 分区
