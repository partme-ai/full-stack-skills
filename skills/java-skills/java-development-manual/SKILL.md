---
name: java-development-manual
description: |
  Java开发手册规约集合，基于阿里巴巴Java开发手册（嵩山版）。
  涵盖7大维度：编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约。
  当用户需要：(1) 编写或审查Java代码 (2) 检查命名/代码规范 (3) 处理异常和日志 (4) 编写单元测试 (5) 安全编码 (6) 数据库设计 (7) 工程架构设计时使用此skill。
  触发词：Java规范、阿里规约、代码规范、开发手册、编程规约、异常处理、单元测试、安全、MySQL、工程结构、设计模式。
---

# Java开发手册（嵩山版）

## 概述

本手册基于阿里巴巴Java开发手册（嵩山版），将规约分为7个维度。规约按约束力强弱分为：

| 级别 | 含义 | 说明 |
|------|------|------|
| **【强制】** | 必须遵守 | 违反可能导致严重问题 |
| **【推荐】** | 建议遵守 | 提升代码质量和可维护性 |
| **【参考】** | 可选择性采纳 | 根据实际情况判断 |

## 章节导航

根据需求选择对应章节的详细规约：

| 章节 | 适用场景 | 详细文档 |
|------|---------|----------|
| **编程规约** | 命名、格式、OOP、并发、集合处理 | [coding-convention.md](references/coding-convention.md) |
| **异常日志** | 错误码、异常处理、日志规范 | [exception-log.md](references/exception-log.md) |
| **单元测试** | 测试用例、覆盖率、Mock | [unit-test.md](references/unit-test.md) |
| **安全规约** | SQL注入、XSS、CSRF、脱敏 | [security.md](references/security.md) |
| **MySQL数据库** | 建表、索引、SQL、ORM | [mysql.md](references/mysql.md) |
| **工程结构** | 分层架构、依赖管理、服务器 | [project-structure.md](references/project-structure.md) |
| **设计规约** | UML、设计模式、设计原则 | [design.md](references/design.md) |

## 快速参考

### 命名规范速查

```java
// 类名：UpperCamelCase
public class UserService { }
public class UserDO { }      // DO/DTO/VO例外

// 方法名/变量：lowerCamelCase
private String userName;
public void getUserById() { }

// 常量：全大写+下划线
public static final int MAX_RETRY_COUNT = 3;

// 包名：全小写
package com.company.project.service;
```

### 禁止事项速查

| 禁止 | 原因 |
|------|------|
| 拼音命名 | 可读性差 |
| 魔法值 | 难以维护 |
| `SELECT *` | 性能和可维护性 |
| Executors创建线程池 | 可能OOM |
| 字符串拼接SQL | 注入风险 |
| finally中return | 丢失try返回值 |
| foreach中remove | ConcurrentModificationException |

### 必须事项速查

| 必须 | 原因 |
|------|------|
| 覆写方法加@Override | 避免签名错误 |
| 表必备三字段 | id, create_time, update_time |
| 敏感数据脱敏 | 隐私保护 |
| 参数校验 | 安全防护 |
| ThreadLocal回收 | 避免内存泄漏 |
| 日志用占位符 | 性能优化 |

### 异常处理速查

```java
// 正确的异常处理
try {
    // 业务逻辑
} catch (SpecificException e) {
    logger.error("操作失败, 参数: {}", params, e);
    throw new BusinessException("用户友好提示", e);
} finally {
    // 资源关闭（JDK7+ try-with-resources）
}
```

### 数据库速查

```sql
-- 建表必备
CREATE TABLE example (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 索引命名
-- 主键: pk_字段名
-- 唯一: uk_字段名
-- 普通: idx_字段名
```

### 并发处理速查

```java
// 线程池创建
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,
    maximumPoolSize,
    keepAliveTime,
    TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(queueCapacity),
    new ThreadFactory() {
        private AtomicInteger counter = new AtomicInteger(1);
        public Thread newThread(Runnable r) {
            return new Thread(r, "worker-" + counter.getAndIncrement());
        }
    },
    new ThreadPoolExecutor.CallerRunsPolicy()
);

// ThreadLocal使用
try {
    threadLocal.set(value);
    // 业务逻辑
} finally {
    threadLocal.remove();  // 必须回收
}
```

## 使用指南

### 代码审查场景

1. **命名检查** → 查看 [coding-convention.md](references/coding-convention.md) 的"命名风格"章节
2. **并发问题** → 查看 [coding-convention.md](references/coding-convention.md) 的"并发处理"章节
3. **异常处理** → 查看 [exception-log.md](references/exception-log.md)
4. **安全问题** → 查看 [security.md](references/security.md)

### 新项目搭建场景

1. **架构设计** → 查看 [design.md](references/design.md)
2. **分层结构** → 查看 [project-structure.md](references/project-structure.md)
3. **数据库设计** → 查看 [mysql.md](references/mysql.md)
4. **单元测试** → 查看 [unit-test.md](references/unit-test.md)

### 问题排查场景

1. **NPE问题** → 查看 [exception-log.md](references/exception-log.md) 的"NPE防护"
2. **性能问题** → 查看 [mysql.md](references/mysql.md) 的"索引规约"
3. **并发问题** → 查看 [coding-convention.md](references/coding-convention.md) 的"并发处理"
