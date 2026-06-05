# 性能调优 — AWR / ASH / ADDM / DBMS_XPLAN

## EXPLAIN PLAN / DBMS_XPLAN

```sql
-- 生成执行计划
EXPLAIN PLAN FOR
SELECT d.department_name, e.last_name, e.salary
FROM departments d JOIN employees e ON d.department_id = e.department_id
WHERE e.salary > 10000;

-- 查看执行计划
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);

-- 查看实际执行计划（带统计信息）
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(sql_id => 'abc123', format => 'ALLSTATS LAST'));

-- 格式化选项
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(format => 'BASIC'));    -- 基本
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(format => 'TYPICAL'));  -- 典型（默认）
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(format => 'ALL'));      -- 全部
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(format => 'ADVANCED')); -- 高级（含提示）

-- 查找高消耗 SQL
SELECT sql_id, ROUND(elapsed_time/1000,2) AS elapsed_ms,
       cpu_time, buffer_gets, executions,
       SUBSTR(sql_text, 1, 200) AS sql_text_short
FROM v$sql
WHERE elapsed_time > 0 AND executions > 0
ORDER BY elapsed_time DESC FETCH FIRST 10 ROWS ONLY;
```

## AWR（Automatic Workload Repository）

```sql
-- 生成 AWR 报告（HTML 格式）
SELECT * FROM TABLE(DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML(
    l_dbid     => (SELECT dbid FROM v$database),
    l_inst_num => 1,
    l_bid      => 100,    -- 起始快照 ID
    l_eid      => 110,    -- 结束快照 ID
    l_options  => 0
));

-- 创建 AWR 快照
EXEC DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();

-- 修改 AWR 保留策略（默认 8 天）
EXEC DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(retention => 14400);   -- 10天
EXEC DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(interval => 60);       -- 间隔 60 分钟
```

## ASH（Active Session History）

```sql
-- 最近 10 分钟的 Top 等待事件
SELECT event, COUNT(*) AS cnt,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct
FROM v$active_session_history
WHERE sample_time > SYSTIMESTAMP - INTERVAL '10' MINUTE
GROUP BY event ORDER BY cnt DESC;

-- Top SQL（基于 ASH）
SELECT sql_id, COUNT(*) AS hits,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct
FROM v$active_session_history
WHERE sample_time > SYSTIMESTAMP - INTERVAL '10' MINUTE AND sql_id IS NOT NULL
GROUP BY sql_id ORDER BY hits DESC FETCH FIRST 5 ROWS ONLY;
```

## ADDM（Automatic Database Diagnostic Monitor）

```sql
DECLARE
    v_task_name VARCHAR2(30);
BEGIN
    v_task_name := 'MY_ADDM_TASK';
    DBMS_ADDM.ANALYZE_DB(
        task_name => v_task_name,
        begin_snapshot => 100,
        end_snapshot => 110
    );
END;
/
```

## SQL Tuning Advisor

```sql
DECLARE
    v_task_name VARCHAR2(30);
BEGIN
    v_task_name := DBMS_SQLTUNE.CREATE_TUNING_TASK(
        sql_id      => 'abc123xyz4567',
        scope       => DBMS_SQLTUNE.SCOPE_COMPREHENSIVE,
        time_limit  => 300,
        task_name   => 'tune_sql_abc123'
    );
    DBMS_SQLTUNE.EXECUTE_TUNING_TASK(task_name => v_task_name);
END;
/

-- 查看调优建议
SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(task_name => 'tune_sql_abc123') FROM DUAL;

-- 接受 SQL Profile
EXEC DBMS_SQLTUNE.ACCEPT_SQL_PROFILE(task_name => 'tune_sql_abc123');
```

## DBMS_STATS — 统计信息

```sql
-- 收集表级统计信息
EXEC DBMS_STATS.GATHER_TABLE_STATS(
    ownname => 'HR', tabname => 'EMPLOYEES',
    estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE,
    cascade => TRUE, degree => DBMS_STATS.AUTO_DEGREE,
    method_opt => 'FOR ALL COLUMNS SIZE AUTO'
);

-- 收集模式级统计信息
EXEC DBMS_STATS.GATHER_SCHEMA_STATS(ownname => 'HR', options => 'GATHER AUTO');

-- 锁定/解锁统计信息
EXEC DBMS_STATS.LOCK_TABLE_STATS('HR', 'EMPLOYEES');
EXEC DBMS_STATS.UNLOCK_TABLE_STATS('HR', 'EMPLOYEES');

-- 恢复历史统计信息
EXEC DBMS_STATS.RESTORE_TABLE_STATS('HR', 'EMPLOYEES', SYSTIMESTAMP - 7);

-- 查看统计信息
SELECT table_name, num_rows, blocks, avg_row_len, last_analyzed
FROM dba_tab_statistics WHERE owner = 'HR' AND table_name = 'EMPLOYEES';
```

## SPM（SQL Plan Management）

```sql
-- 加载执行计划到 SPM
DECLARE v_plans_loaded PLS_INTEGER;
BEGIN
    v_plans_loaded := DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE(sql_id => 'abc123xyz4567');
END;
/

-- 查看 SPM 基线
SELECT sql_handle, plan_name, enabled, accepted, fixed FROM dba_sql_plan_baselines;

-- 演变计划
SELECT DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE(sql_handle => 'SQL_handle_here', verify => 'YES') FROM DUAL;

-- 固定计划
DECLARE v_fixed PLS_INTEGER;
BEGIN
    v_fixed := DBMS_SPM.ALTER_SQL_PLAN_BASELINE(
        sql_handle => 'SQL_handle_here', plan_name => 'SQL_PLAN_xxxxx',
        attribute_name => 'FIXED', attribute_value => 'YES');
END;
/

-- SPM 配置
ALTER SYSTEM SET optimizer_capture_sql_plan_baselines = FALSE;
ALTER SYSTEM SET optimizer_use_sql_plan_baselines = TRUE;
```
