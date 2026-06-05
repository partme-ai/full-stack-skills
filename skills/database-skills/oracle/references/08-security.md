# 安全与权限 — 用户 / FGA / VPD / TDE / 数据脱敏

## 用户 / 角色 / 权限

```sql
-- 创建用户
CREATE USER app_user IDENTIFIED BY "StrongPassword123!"
    DEFAULT TABLESPACE tbs_app_data
    TEMPORARY TABLESPACE TEMP
    QUOTA UNLIMITED ON tbs_app_data;

-- 创建角色
CREATE ROLE app_read_role;
CREATE ROLE app_write_role;

-- 系统权限
GRANT CREATE SESSION TO app_user;
GRANT CREATE TABLE, CREATE PROCEDURE, CREATE VIEW, CREATE SEQUENCE TO app_user;

-- 对象权限
GRANT SELECT, INSERT, UPDATE, DELETE ON hr.employees TO app_write_role;
GRANT SELECT ON hr.employees TO app_read_role;
GRANT EXECUTE ON hr.emp_mgmt TO app_admin_role;

-- 角色授予用户
GRANT app_read_role TO app_user;

-- 撤销
REVOKE DELETE ON hr.employees FROM app_write_role;

-- 查看用户权限
SELECT * FROM dba_sys_privs WHERE grantee = 'APP_USER';
SELECT * FROM dba_tab_privs WHERE grantee = 'APP_USER';
SELECT * FROM dba_role_privs WHERE grantee = 'APP_USER';

-- 配置文件（Profile）
CREATE PROFILE app_profile LIMIT
    SESSIONS_PER_USER      5
    IDLE_TIME             30
    CONNECT_TIME         480
    FAILED_LOGIN_ATTEMPTS  5
    PASSWORD_LOCK_TIME     1
    PASSWORD_LIFE_TIME    90
    PASSWORD_GRACE_TIME    7;

-- 用户管理
ALTER USER app_user ACCOUNT LOCK;
ALTER USER app_user ACCOUNT UNLOCK;
ALTER USER app_user PASSWORD EXPIRE;
```

## FGA（Fine-Grained Auditing）— 细粒度审计

```sql
-- 创建 FGA 策略（审计高工资访问）
BEGIN
    DBMS_FGA.ADD_POLICY(
        object_schema   => 'HR',
        object_name     => 'EMPLOYEES',
        policy_name     => 'AUDIT_SALARY_ACCESS',
        audit_condition => 'salary > 10000',
        audit_column    => 'SALARY, COMMISSION_PCT',
        enable          => TRUE,
        statement_types => 'SELECT, UPDATE',
        audit_trail     => DBMS_FGA.XML + DBMS_FGA.EXTENDED
    );
END;
/

-- 查看 FGA 审计日志
SELECT timestamp, db_user, object_schema, object_name, sql_text
FROM dba_fga_audit_trail WHERE object_name = 'EMPLOYEES'
ORDER BY timestamp DESC;

-- 管理 FGA 策略
BEGIN
    DBMS_FGA.DISABLE_POLICY('HR', 'EMPLOYEES', 'AUDIT_SALARY_ACCESS');
    DBMS_FGA.ENABLE_POLICY('HR', 'EMPLOYEES', 'AUDIT_SALARY_ACCESS');
    DBMS_FGA.DROP_POLICY('HR', 'EMPLOYEES', 'AUDIT_SALARY_ACCESS');
END;
/
```

## VPD（Virtual Private Database）— 虚拟私有数据库

```sql
-- 1. 创建策略函数
CREATE OR REPLACE FUNCTION dept_access_policy(
    p_schema VARCHAR2, p_object VARCHAR2
) RETURN VARCHAR2 AS
    v_dept_id NUMBER;
BEGIN
    IF SYS_CONTEXT('USERENV', 'ISDBA') = 'TRUE' THEN
        RETURN '1=1';
    END IF;
    v_dept_id := SYS_CONTEXT('USER_CTX', 'DEPARTMENT_ID');
    IF v_dept_id IS NOT NULL THEN
        RETURN 'department_id = ' || v_dept_id;
    ELSE
        RETURN '1=0';
    END IF;
END;
/

-- 2. 应用策略到表
BEGIN
    DBMS_RLS.ADD_POLICY(
        object_schema   => 'HR',
        object_name     => 'EMPLOYEES',
        policy_name     => 'DEPT_ACCESS_POLICY',
        function_schema => 'HR',
        policy_function => 'dept_access_policy',
        statement_types => 'SELECT, INSERT, UPDATE, DELETE',
        update_check    => TRUE,
        enable          => TRUE
    );
END;
/

-- 查看 VPD 策略
SELECT * FROM dba_policies WHERE object_name = 'EMPLOYEES';

-- 移除
EXEC DBMS_RLS.DROP_POLICY('HR', 'EMPLOYEES', 'DEPT_ACCESS_POLICY');
```

## TDE（Transparent Data Encryption）— 透明数据加密

```sql
-- 打开钱包
ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY "wallet_password";
ADMINISTER KEY MANAGEMENT SET KEY IDENTIFIED BY "wallet_password" WITH BACKUP;

-- 创建加密表空间
CREATE TABLESPACE tbs_encrypted
    DATAFILE '/u01/oradata/orcl/encrypted01.dbf' SIZE 5G
    ENCRYPTION USING 'AES256'
    DEFAULT STORAGE(ENCRYPT);

-- 列级加密
CREATE TABLE credit_cards (
    card_id     NUMBER(10) PRIMARY KEY,
    customer_id NUMBER(10),
    card_number VARCHAR2(16) ENCRYPT USING 'AES256',
    cvv         VARCHAR2(4) ENCRYPT,
    expiry_date DATE
);
```

## 数据脱敏（Data Redaction）

```sql
-- 创建 Redaction Policy
BEGIN
    DBMS_REDACT.ADD_POLICY(
        object_schema       => 'HR',
        object_name         => 'CREDIT_CARDS',
        policy_name         => 'REDACT_CC_NUM',
        column_name         => 'CARD_NUMBER',
        function_type       => DBMS_REDACT.PARTIAL,
        function_parameters => 'VVVVVVVVVVVVVVVV,VVVV-XXXX-XXXX-VVVV,*,1,4',
        expression          => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''APP_ADMIN'''
    );
END;
/

-- 查看脱敏策略
SELECT * FROM redaction_policies;
SELECT * FROM redaction_columns;
```
