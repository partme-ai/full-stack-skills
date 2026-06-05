# 示例：PL/SQL 存储过程 — 员工薪资管理包

## 场景

创建一个完整的员工薪资管理包，支持涨薪、查询年收入、批量调整部门薪资。

## 包规范

```sql
CREATE OR REPLACE PACKAGE salary_mgmt AS
    -- 涨薪
    PROCEDURE give_raise(p_emp_id NUMBER, p_percent NUMBER);
    -- 查询年收入
    FUNCTION annual_income(p_emp_id NUMBER) RETURN NUMBER;
    -- 批量调整部门薪资
    PROCEDURE dept_raise(p_dept_id NUMBER, p_percent NUMBER);
    -- 获取部门薪资统计
    FUNCTION dept_stats(p_dept_id NUMBER) RETURN SYS_REFCURSOR;
END salary_mgmt;
/
```

## 包体

```sql
CREATE OR REPLACE PACKAGE BODY salary_mgmt AS

    PROCEDURE give_raise(p_emp_id NUMBER, p_percent NUMBER) AS
        v_old_sal employees.salary%TYPE;
    BEGIN
        SELECT salary INTO v_old_sal FROM employees WHERE employee_id = p_emp_id FOR UPDATE;
        UPDATE employees SET salary = salary * (1 + p_percent/100) WHERE employee_id = p_emp_id;
        DBMS_OUTPUT.PUT_LINE('员工 ' || p_emp_id || ': ' || v_old_sal || ' → ' || ROUND(v_old_sal*(1+p_percent/100),2));
        COMMIT;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, '员工 ' || p_emp_id || ' 不存在');
        WHEN OTHERS THEN ROLLBACK; RAISE;
    END;

    FUNCTION annual_income(p_emp_id NUMBER) RETURN NUMBER AS
        v_sal employees.salary%TYPE;
        v_comm employees.commission_pct%TYPE;
    BEGIN
        SELECT salary, NVL(commission_pct, 0) INTO v_sal, v_comm
        FROM employees WHERE employee_id = p_emp_id;
        RETURN v_sal * 12 + v_sal * NVL(v_comm, 0);
    END;

    PROCEDURE dept_raise(p_dept_id NUMBER, p_percent NUMBER) AS
    BEGIN
        UPDATE employees SET salary = salary * (1 + p_percent/100)
        WHERE department_id = p_dept_id;
        DBMS_OUTPUT.PUT_LINE('部门 ' || p_dept_id || ' 已更新 ' || SQL%ROWCOUNT || ' 行');
        COMMIT;
    END;

    FUNCTION dept_stats(p_dept_id NUMBER) RETURN SYS_REFCURSOR AS
        c SYS_REFCURSOR;
    BEGIN
        OPEN c FOR SELECT employee_id, last_name, salary,
                          annual_income(employee_id) AS annual
                   FROM employees WHERE department_id = p_dept_id
                   ORDER BY salary DESC;
        RETURN c;
    END;

END salary_mgmt;
/
```

## 调用示例

```sql
-- 单员工涨薪 10%
BEGIN salary_mgmt.give_raise(100, 10); END;
/

-- 查询年收入
SELECT salary_mgmt.annual_income(100) FROM DUAL;

-- 部门批量涨薪 5%
BEGIN salary_mgmt.dept_raise(50, 5); END;
/

-- 获取部门薪资统计
VARIABLE c REFCURSOR;
EXEC :c := salary_mgmt.dept_stats(50);
PRINT c;
```
