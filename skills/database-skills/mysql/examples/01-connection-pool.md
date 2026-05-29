# 示例: 连接池配置 (Java HikariCP)

## 场景

生产环境高并发 Web 应用中，合理配置数据库连接池是保证性能的关键。本例展示 HikariCP（Spring Boot 默认连接池）的最佳实践配置。

## 问题

- 连接数太少 → 请求排队等待，响应变慢
- 连接数太多 → MySQL 连接数耗尽（`max_connections`），系统崩溃
- 连接泄漏 → 连接未正确归还，池逐渐耗尽

## 解决方案

### application.yml 配置

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/shop?useSSL=false&serverTimezone=Asia/Shanghai&characterEncoding=utf8mb4
    username: root
    password: your_password
    driver-class-name: com.mysql.cj.jdbc.Driver
    hikari:
      # 核心配置
      maximum-pool-size: 20           # 最大连接数（核心参数）
      minimum-idle: 5                 # 最小空闲连接数
      connection-timeout: 30000       # 等待连接超时（毫秒）
      idle-timeout: 600000            # 空闲连接最大存活（毫秒，10min）
      max-lifetime: 1800000           # 连接最大寿命（毫秒，30min）
      
      # MySQL 专用优化
      auto-commit: true
      connection-test-query: SELECT 1
      pool-name: ShopHikariPool
      
      # 性能监控
      register-mbeans: true           # 开启 JMX 监控
```

### 常用计算公式

```
最大连接数 = ((核心数 * 2) + 有效磁盘数)

示例:
- 4 核 CPU + 1 SSD → (4 * 2) + 1 = 9
- 8 核 CPU + 1 SSD → (8 * 2) + 1 = 17

通用建议:
- 微服务低并发场景: 5-10
- Web 应用中并发场景: 15-30
- 高并发场景: 分库后每个库 20-50

注意: 不是越大越好。连接池大小 × 并发请求数 = MySQL 实际并发连接。
举例: 10 个实例 × 每个 20 连接 = 200 个 MySQL 连接。
```

### 验证配置

```sql
-- 查看实际连接数
SHOW STATUS LIKE 'Threads_connected';
SHOW STATUS LIKE 'Max_used_connections';

-- 查看连接来源
SELECT * FROM information_schema.processlist;
```

## 关键要点

1. **连接池大小不是越大越好**：过多的连接会导致 MySQL 上下文切换开销和锁争用
2. **max-lifetime 应小于 MySQL 的 wait_timeout**（通常 28800s），避免连接被 MySQL 断开后还留在池中
3. **connection-test-query** 用于心跳检测，`SELECT 1` 性能最好
4. 建议配合 `spring.datasource.hikari.leak-detection-threshold` 检测连接泄漏
