# Java Conventions — 注释模板与检查清单

## 注释检查清单（提交前）
- 是否新增/修改了类或方法？若是：类注释与方法注释必须同步更新。
- 方法是否包含非简单 CRUD 的业务逻辑？若是：按逻辑块补充注释（意图、边界、异常路径）。
- Controller/Service/ServiceImpl/Mapper 是否均保持注释一致（职责描述、入参出参、异常/返回约定）？
- 注释是否与当前实现一致（不保留过期说明）？

## 常用 JavaDoc 模板

### Controller

```java
/**
 * XXX 接口控制器。
 *
 * 职责：
 * - 接收 HTTP 请求并完成参数校验
 * - 调用应用/服务层完成业务编排
 * - 组装并返回统一响应
 */
```

### Service / ServiceImpl

```java
/**
 * XXX 领域服务。
 *
 * 职责：
 * - 承载跨聚合/跨实体的业务规则编排
 * - 保持领域逻辑内聚，避免将业务下沉为 CRUD 拼接
 */
```

### Mapper

```java
/**
 * XXX 数据访问层。
 *
 * 约束：
 * - 仅负责数据库读写与对象映射
 * - 不在 Mapper 内堆叠业务规则
 */
```

### 方法（通用）

```java
/**
 * 执行 XXX 业务动作。
 *
 * @param xxx 业务参数含义说明
 * @return 返回值含义说明
 * @throws IllegalArgumentException 参数不合法时抛出
 */
```

## 逻辑块注释示例（非简单 CRUD）

```java
public Result handle(Command cmd) {
  // 1) 参数校验与默认值处理

  // 2) 领域规则校验（状态机/幂等/权限等）

  // 3) 状态变更与持久化（事务边界）

  // 4) 事件发布/异步触发（若有）
  return Result.ok();
}
```
