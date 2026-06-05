# Oracle 特有特性 — 分区 / 索引 / 物化视图 / Flashback / AQ

## 表空间与数据文件

```sql
-- 创建表空间
CREATE TABLESPACE tbs_app_data
    DATAFILE '/u01/oradata/orcl/app_data01.dbf' SIZE 10G
    AUTOEXTEND ON NEXT 1G MAXSIZE 32G;

-- 创建临时/撤销表空间
CREATE TEMPORARY TABLESPACE tbs_app_temp TEMPFILE '/u01/oradata/orcl/app_temp01.dbf' SIZE 5G;
CREATE UNDO TABLESPACE tbs_app_undo DATAFILE '/u01/oradata/orcl/app_undo01.dbf' SIZE 10G;

-- 表空间管理
ALTER TABLESPACE tbs_app_data ADD DATAFILE '/u01/oradata/orcl/app_data02.dbf' SIZE 10G;
ALTER TABLESPACE tbs_app_data READ ONLY;
ALTER TABLESPACE tbs_app_data OFFLINE NORMAL;

-- 表空间使用率
SELECT df.tablespace_name,
       ROUND(df.bytes/1024/1024/1024,2) AS total_gb,
       ROUND((1-fs.bytes/df.bytes)*100,2) AS used_pct
FROM (SELECT tablespace_name, SUM(bytes) AS bytes FROM dba_data_files GROUP BY tablespace_name) df
JOIN (SELECT tablespace_name, SUM(bytes) AS bytes FROM dba_free_space GROUP BY tablespace_name) fs
ON df.tablespace_name = fs.tablespace_name;
```

## 分区表

```sql
-- RANGE 分区
CREATE TABLE sales (
    sale_id NUMBER(10), sale_date DATE, amount NUMBER(10,2)
) PARTITION BY RANGE (sale_date) (
    PARTITION p_2023_q1 VALUES LESS THAN (DATE '2023-04-01'),
    PARTITION p_2023_q2 VALUES LESS THAN (DATE '2023-07-01'),
    PARTITION p_future VALUES LESS THAN (MAXVALUE)
);

-- LIST 分区
CREATE TABLE customers PARTITION BY LIST (region) (
    PARTITION p_north VALUES ('北京','天津','河北'),
    PARTITION p_east VALUES ('上海','江苏','浙江'),
    PARTITION p_other VALUES (DEFAULT)
);

-- HASH 分区
CREATE TABLE logs PARTITION BY HASH (log_id) PARTITIONS 8;

-- 复合分区（RANGE-HASH）
CREATE TABLE sales_comp PARTITION BY RANGE (sale_date)
SUBPARTITION BY HASH (region) SUBPARTITIONS 4 (
    PARTITION p_2023_q1 VALUES LESS THAN (DATE '2023-04-01')
);

-- 间隔分区（11g+ 自动建分区）
CREATE TABLE sales_interval PARTITION BY RANGE (sale_date)
INTERVAL(NUMTOYMINTERVAL(1,'MONTH')) (
    PARTITION p_first VALUES LESS THAN (DATE '2023-01-01')
);

-- 分区操作
ALTER TABLE sales ADD PARTITION p_2024_q1 VALUES LESS THAN (DATE '2024-04-01');
ALTER TABLE sales TRUNCATE PARTITION p_future;
ALTER TABLE sales EXCHANGE PARTITION p_2023_q1 WITH TABLE sales_2023_q1;
ALTER TABLE sales MERGE PARTITIONS p_2023_q1, p_2023_q2 INTO PARTITION p_2023_h1;
ALTER TABLE sales SPLIT PARTITION p_future AT (DATE '2024-04-01')
    INTO (PARTITION p_2024_q1, PARTITION p_future);
```

## 索引

```sql
-- B-Tree 索引（默认）
CREATE INDEX idx_emp_dept_id ON employees(department_id);
CREATE INDEX idx_emp_dept_name ON employees(department_id, last_name);  -- 复合
CREATE UNIQUE INDEX idx_emp_email ON employees(email);                 -- 唯一

-- 位图索引（适合低基数、数据仓库）
CREATE BITMAP INDEX idx_sales_region ON sales(region);

-- 函数索引
CREATE INDEX idx_emp_upper_name ON employees(UPPER(last_name));

-- 域索引（Oracle Text 全文）
CREATE INDEX idx_docs_content ON documents(content) INDEXTYPE IS CTXSYS.CONTEXT;

-- 索引监控
ALTER INDEX idx_emp_dept_id MONITORING USAGE;
SELECT * FROM v$object_usage;  -- 查看未被使用的索引
```

## 物化视图

```sql
-- 基本物化视图
CREATE MATERIALIZED VIEW mv_dept_salary_summary
    BUILD IMMEDIATE REFRESH COMPLETE ON DEMAND ENABLE QUERY REWRITE
AS SELECT d.department_id, d.department_name,
          COUNT(e.employee_id) AS emp_count, SUM(e.salary) AS total_salary
FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;

-- 快速刷新物化视图（需物化视图日志）
CREATE MATERIALIZED VIEW LOG ON employees WITH PRIMARY KEY, ROWID (salary, department_id) INCLUDING NEW VALUES;
CREATE MATERIALIZED VIEW mv_emp_fast
    BUILD IMMEDIATE REFRESH FAST ON COMMIT
AS SELECT department_id, COUNT(*) AS cnt, SUM(salary) AS total_sal
FROM employees GROUP BY department_id;

-- 刷新
EXEC DBMS_MVIEW.REFRESH('mv_dept_salary_summary', 'C');  -- C=完全, F=快速
ALTER SESSION SET QUERY_REWRITE_ENABLED = TRUE;
```

## Flashback 技术

```sql
-- Flashback Query — 见 references/09-sql-syntax.md

-- Flashback Table（需启用行移动）
ALTER TABLE employees ENABLE ROW MOVEMENT;
FLASHBACK TABLE employees TO TIMESTAMP (SYSTIMESTAMP - INTERVAL '15' MINUTE);
FLASHBACK TABLE employees TO SCN 1234567;
FLASHBACK TABLE employees TO RESTORE POINT before_batch;

-- Flashback Drop（回收站）
DROP TABLE employees;
SELECT object_name, original_name, droptime FROM recyclebin;
FLASHBACK TABLE employees TO BEFORE DROP;

-- Flashback Database（需启用闪回日志）
-- FLASHBACK DATABASE TO TIMESTAMP (SYSTIMESTAMP - INTERVAL '1' HOUR);
```

## AQ（Advanced Queuing）— 高级队列

```sql
-- 创建类型和队列表
CREATE OR REPLACE TYPE order_msg AS OBJECT (order_id NUMBER, customer_id NUMBER, amount NUMBER);
/
BEGIN
    DBMS_AQADM.CREATE_QUEUE_TABLE(queue_table => 'order_queue_table', queue_payload_type => 'order_msg');
    DBMS_AQADM.CREATE_QUEUE(queue_name => 'order_queue', queue_table => 'order_queue_table');
    DBMS_AQADM.START_QUEUE(queue_name => 'order_queue');
END;
/

-- 发送消息
DECLARE
    enqueue_options    DBMS_AQ.ENQUEUE_OPTIONS_T;
    message_properties DBMS_AQ.MESSAGE_PROPERTIES_T;
    message_handle     RAW(16);
    msg                order_msg := order_msg(1001, 500, 1500.00);
BEGIN
    DBMS_AQ.ENQUEUE('order_queue', enqueue_options, message_properties, msg, message_handle);
    COMMIT;
END;
/

-- 接收消息
DECLARE
    dequeue_options    DBMS_AQ.DEQUEUE_OPTIONS_T;
    message_properties DBMS_AQ.MESSAGE_PROPERTIES_T;
    message_handle     RAW(16);
    msg                order_msg;
BEGIN
    dequeue_options.wait := DBMS_AQ.FOREVER;
    DBMS_AQ.DEQUEUE('order_queue', dequeue_options, message_properties, msg, message_handle);
    COMMIT;
END;
/
```
