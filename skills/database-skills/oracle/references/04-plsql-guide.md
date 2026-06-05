# PL/SQL 详解

PL/SQL（Procedural Language/SQL）是 Oracle 的扩展 SQL，支持变量、条件、循环、异常处理等过程式编程。

## 块结构

```sql
DECLARE
    v_employee_id employees.employee_id%TYPE;
    v_salary      employees.salary%TYPE := 5000;
BEGIN
    SELECT employee_id, salary INTO v_employee_id, v_salary
    FROM employees WHERE employee_id = 100;
    DBMS_OUTPUT.PUT_LINE('员工 ' || v_employee_id || ' 工资: ' || v_salary);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('未找到员工');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('错误: ' || SQLERRM);
END;
/
```

## 游标 (Cursor)

```sql
-- 隐式游标（SELECT INTO）
DECLARE v_name employees.last_name%TYPE;
BEGIN
    SELECT last_name INTO v_name FROM employees WHERE employee_id = 100;
EXCEPTION WHEN NO_DATA_FOUND THEN NULL;
END;
/

-- 显式游标
DECLARE
    CURSOR emp_cursor IS SELECT employee_id, last_name FROM employees WHERE department_id = 50;
    v_emp emp_cursor%ROWTYPE;
BEGIN
    OPEN emp_cursor;
    LOOP
        FETCH emp_cursor INTO v_emp;
        EXIT WHEN emp_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_emp.last_name);
    END LOOP;
    CLOSE emp_cursor;
END;
/

-- CURSOR FOR LOOP（最简洁）
BEGIN
    FOR rec IN (SELECT last_name, salary FROM employees WHERE department_id = 50)
    LOOP
        DBMS_OUTPUT.PUT_LINE(rec.last_name || ' 工资: ' || rec.salary);
    END LOOP;
END;
/

-- REF CURSOR（动态游标）
DECLARE
    TYPE refcur IS REF CURSOR;
    c_ref refcur;
    v_id   employees.employee_id%TYPE;
    v_name employees.last_name%TYPE;
BEGIN
    OPEN c_ref FOR 'SELECT employee_id, last_name FROM employees WHERE department_id = :d' USING 50;
    LOOP
        FETCH c_ref INTO v_id, v_name;
        EXIT WHEN c_ref%NOTFOUND;
    END LOOP;
    CLOSE c_ref;
END;
/

-- SYS_REFCURSOR 函数返回
CREATE OR REPLACE FUNCTION get_employees(p_dept_id NUMBER) RETURN SYS_REFCURSOR AS
    c SYS_REFCURSOR;
BEGIN
    OPEN c FOR SELECT * FROM employees WHERE department_id = p_dept_id;
    RETURN c;
END;
/
```

## 存储过程与函数

```sql
-- 存储过程
CREATE OR REPLACE PROCEDURE update_salary(
    p_employee_id IN employees.employee_id%TYPE,
    p_percent     IN NUMBER
) AS
    v_old_salary employees.salary%TYPE;
BEGIN
    SELECT salary INTO v_old_salary FROM employees WHERE employee_id = p_employee_id FOR UPDATE;
    UPDATE employees SET salary = salary * (1 + p_percent / 100) WHERE employee_id = p_employee_id;
    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20001, '员工不存在');
    WHEN OTHERS THEN ROLLBACK; RAISE;
END update_salary;
/

-- 函数（必须有返回值）
CREATE OR REPLACE FUNCTION get_annual_salary(p_employee_id NUMBER) RETURN NUMBER AS
    v_salary employees.salary%TYPE;
    v_commission employees.commission_pct%TYPE;
BEGIN
    SELECT salary, NVL(commission_pct, 0) INTO v_salary, v_commission
    FROM employees WHERE employee_id = p_employee_id;
    RETURN v_salary * 12 + v_salary * v_commission;
END get_annual_salary;
/

-- DETERMINISTIC 函数（可用于函数索引）
CREATE OR REPLACE FUNCTION calculate_tax(p_amount NUMBER) RETURN NUMBER DETERMINISTIC AS
BEGIN
    RETURN p_amount * 0.13;
END;
/
```

## 包 (Package)

```sql
-- 包规范（公开接口）
CREATE OR REPLACE PACKAGE emp_mgmt AS
    c_max_salary CONSTANT NUMBER := 50000;
    FUNCTION get_salary(p_emp_id NUMBER) RETURN NUMBER;
    PROCEDURE raise_salary(p_emp_id NUMBER, p_pct NUMBER);
    PROCEDURE hire_employee(p_last_name VARCHAR2, p_email VARCHAR2, p_job_id VARCHAR2, p_salary NUMBER);
    PROCEDURE set_debug(p_mode BOOLEAN);
    PROCEDURE set_debug(p_mode VARCHAR2);  -- 重载
END emp_mgmt;
/

-- 包体（实现）
CREATE OR REPLACE PACKAGE BODY emp_mgmt AS
    v_last_action VARCHAR2(100);  -- 私有变量

    FUNCTION get_salary(p_emp_id NUMBER) RETURN NUMBER IS
        v_sal employees.salary%TYPE;
    BEGIN
        SELECT salary INTO v_sal FROM employees WHERE employee_id = p_emp_id;
        RETURN v_sal;
    EXCEPTION WHEN NO_DATA_FOUND THEN RETURN NULL;
    END;

    PROCEDURE raise_salary(p_emp_id NUMBER, p_pct NUMBER) IS
    BEGIN
        UPDATE employees SET salary = salary * (1 + p_pct/100) WHERE employee_id = p_emp_id;
        v_last_action := 'Raised salary for ' || p_emp_id;
    END;

    PROCEDURE hire_employee(p_last_name VARCHAR2, p_email VARCHAR2, p_job_id VARCHAR2, p_salary NUMBER) IS
    BEGIN
        INSERT INTO employees(employee_id, last_name, email, job_id, salary, hire_date)
        VALUES (employees_seq.NEXTVAL, p_last_name, p_email, p_job_id, p_salary, SYSDATE);
        v_last_action := 'Hired ' || p_last_name;
    END;

    PROCEDURE set_debug(p_mode BOOLEAN) IS BEGIN g_debug_mode := p_mode; END;
    PROCEDURE set_debug(p_mode VARCHAR2) IS BEGIN g_debug_mode := UPPER(p_mode) = 'ON'; END;

    -- 包初始化（首次引用时执行一次）
    BEGIN
        v_last_action := 'Package initialized';
    END;
END emp_mgmt;
/
```

## 触发器 (Trigger)

```sql
-- DML 行级触发器（工资变更审计）
CREATE OR REPLACE TRIGGER trg_emp_salary_audit
    BEFORE UPDATE OF salary ON employees FOR EACH ROW
    WHEN (OLD.salary != NEW.salary)
BEGIN
    INSERT INTO salary_audit_log(employee_id, old_salary, new_salary, changed_by, changed_at)
    VALUES (:OLD.employee_id, :OLD.salary, :NEW.salary, USER, SYSDATE);
END;
/

-- 语句级触发器（非工作时间禁止修改）
CREATE OR REPLACE TRIGGER trg_no_dml_nonbusiness
    BEFORE INSERT OR UPDATE OR DELETE ON employees
BEGIN
    IF TO_CHAR(SYSDATE, 'DY') IN ('SAT', 'SUN') OR
       TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')) NOT BETWEEN 9 AND 18 THEN
        RAISE_APPLICATION_ERROR(-20001, '非工作时间禁止修改');
    END IF;
END;
/

-- INSTEAD OF 触发器（视图 DML）
CREATE OR REPLACE TRIGGER trg_v_emp_dept_ioi
    INSTEAD OF INSERT ON v_emp_dept FOR EACH ROW
BEGIN
    INSERT INTO employees(employee_id, last_name, salary, department_id)
    VALUES (:NEW.employee_id, :NEW.last_name, :NEW.salary,
            (SELECT department_id FROM departments WHERE department_name = :NEW.department_name));
END;
/

-- 登录审计触发器
CREATE OR REPLACE TRIGGER trg_logon_audit
    AFTER LOGON ON DATABASE
BEGIN
    INSERT INTO logon_audit_log(session_id, user_name, logon_time)
    VALUES (SYS_CONTEXT('USERENV', 'SESSIONID'), USER, SYSDATE);
END;
/
```

## 异常处理

```sql
-- 预定义异常
EXCEPTION
    WHEN NO_DATA_FOUND THEN ...
    WHEN TOO_MANY_ROWS THEN ...
    WHEN DUP_VAL_ON_INDEX THEN ...
    WHEN VALUE_ERROR THEN ...
    WHEN ZERO_DIVIDE THEN ...
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM); RAISE;

-- 自定义异常
DECLARE
    e_salary_too_high EXCEPTION;
    PRAGMA EXCEPTION_INIT(e_salary_too_high, -20001);
BEGIN
    IF v_salary > 50000 THEN RAISE e_salary_too_high; END IF;
EXCEPTION WHEN e_salary_too_high THEN ... END;

-- RAISE_APPLICATION_ERROR
RAISE_APPLICATION_ERROR(-20001, '订单已取消', TRUE);
```

## 集合类型

```sql
-- 关联数组（Index-By Table）
DECLARE
    TYPE dept_name_tab IS TABLE OF departments.department_name%TYPE INDEX BY PLS_INTEGER;
    t_dept_names dept_name_tab;
BEGIN
    FOR rec IN (SELECT department_id, department_name FROM departments)
    LOOP t_dept_names(rec.department_id) := rec.department_name; END LOOP;
END;
/

-- 嵌套表
CREATE OR REPLACE TYPE phone_list AS TABLE OF VARCHAR2(20);
/
DECLARE t_phones phone_list := phone_list('13800138000', '13900139000');
BEGIN t_phones.EXTEND(1); t_phones(3) := '13700137000'; END;
/

-- VARRAY（定长数组）
CREATE OR REPLACE TYPE score_list IS VARRAY(10) OF NUMBER;
/

-- 集合方法: EXISTS, COUNT, LIMIT, FIRST/LAST, PRIOR/NEXT, EXTEND, TRIM, DELETE
```

## 动态 SQL

```sql
-- EXECUTE IMMEDIATE（简单动态 SQL）
CREATE OR REPLACE FUNCTION count_rows(p_table_name VARCHAR2) RETURN NUMBER AS
    v_sql VARCHAR2(200); v_cnt NUMBER;
BEGIN
    v_sql := 'SELECT COUNT(*) FROM ' || p_table_name;
    EXECUTE IMMEDIATE v_sql INTO v_cnt;
    RETURN v_cnt;
END;
/

-- 带绑定变量（防 SQL 注入）
EXECUTE IMMEDIATE 'SELECT last_name FROM employees WHERE employee_id = :id' INTO v_name USING 100;

-- FORALL（批量 DML，提升性能）
DECLARE
    TYPE id_list IS TABLE OF employees.employee_id%TYPE;
    t_ids id_list := id_list(100, 101, 102);
BEGIN
    FORALL i IN t_ids.FIRST..t_ids.LAST
        UPDATE employees SET salary = salary * 1.1 WHERE employee_id = t_ids(i);
    COMMIT;
END;
/

-- BULK COLLECT（批量读取）
DECLARE
    TYPE emp_tab IS TABLE OF employees%ROWTYPE;
    t_emps emp_tab;
BEGIN
    SELECT * BULK COLLECT INTO t_emps FROM employees WHERE department_id = 50;
END;
/
```
