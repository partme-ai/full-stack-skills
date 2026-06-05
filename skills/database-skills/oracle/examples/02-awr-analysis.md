# 示例：AWR 性能分析 — 定位 Top SQL 与等待事件

## 场景

某生产数据库近期响应变慢，需要通过 AWR/ASH 分析找到性能瓶颈。

## 步骤 1：创建 AWR 快照

```sql
-- 在性能问题期间创建快照
EXEC DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();

-- 等待一段时间（比如 30 分钟）后再次创建
EXEC DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();
```

## 步骤 2：生成 AWR 报告

```sql
-- 查找快照 ID
SELECT snap_id, begin_interval_time, end_interval_time
FROM dba_hist_snapshot
ORDER BY snap_id DESC FETCH FIRST 5 ROWS ONLY;

-- 生成 HTML 格式 AWR 报告
-- 假设 snap_id 分别为 1250 和 1255
SELECT * FROM TABLE(DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML(
    l_dbid     => (SELECT dbid FROM v$database),
    l_inst_num => 1,
    l_bid      => 1250,
    l_eid      => 1255,
    l_options  => 0
));
```

## 步骤 3：ASH 分析 — Top 等待事件

```sql
-- 最近 10 分钟的 Top 等待事件
SELECT event, wait_class, COUNT(*) AS session_seconds,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct
FROM v$active_session_history
WHERE sample_time > SYSTIMESTAMP - INTERVAL '10' MINUTE
GROUP BY event, wait_class
ORDER BY session_seconds DESC;
```

## 步骤 4：定位 Top SQL

```sql
-- 按消耗找 Top SQL
SELECT sql_id,
       ROUND(SUM(elapsed_time)/1000000, 2) AS total_sec,
       COUNT(*) AS executions,
       ROUND(AVG(elapsed_time)/1000, 2) AS avg_ms,
       SUBSTR(MAX(sql_text), 1, 100) AS sql_sample
FROM v$active_session_history ash
JOIN v$sql sq USING (sql_id)
WHERE sample_time > SYSTIMESTAMP - INTERVAL '30' MINUTE
  AND sql_id IS NOT NULL
GROUP BY sql_id
ORDER BY total_sec DESC
FETCH FIRST 5 ROWS ONLY;
```

## 步骤 5：分析特定 SQL 的执行计划

```sql
-- 查看 Top SQL 的执行计划
-- 假设 Top SQL 的 sql_id 为 'abc123xyz4567'
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(sql_id => 'abc123xyz4567', format => 'ALLSTATS LAST'));
```

## 步骤 6：使用 SQL Tuning Advisor

```sql
DECLARE
    v_task VARCHAR2(30);
BEGIN
    v_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(
        sql_id => 'abc123xyz4567',
        scope  => DBMS_SQLTUNE.SCOPE_COMPREHENSIVE,
        time_limit => 300
    );
    DBMS_SQLTUNE.EXECUTE_TUNING_TASK(task_name => v_task);
    DBMS_OUTPUT.PUT_LINE('Task: ' || v_task);
END;
/

-- 查看建议
SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(task_name => 'task_name_here') FROM DUAL;
```

## 分析要点

- `db file sequential read` — 单块读等待，通常是索引扫描
- `log file sync` — 提交等待，检查小事务频繁提交
- `enq: TX - row lock contention` — 行锁争用，检查并发更新相同行
- `read by other session` — 缓存争用，考虑调整 buffer cache
