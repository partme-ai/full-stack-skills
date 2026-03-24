# Domain Service 类注释模板

## 类注释模板

### Java 编程规范格式（严格）

```java
/**
 * {服务名称}领域服务
 *
 * <p>{详细描述服务的领域职责和业务逻辑}</p>
 * <p>主要功能包括:</p>
 * <ul>
 *   <li>{功能点1}</li>
 *   <li>{功能点2}</li>
 * </ul>
 *
 * @author system
 * @since 2025-01-21
 */
public class [Resource]DomainService {
}
```

### 标准 JavaDoc 格式

```java
/**
 * {服务名称}领域服务
 * 
 * <p>{详细描述服务的领域职责和业务逻辑}
 * 
 * <p>主要功能包括:
 * <ul>
 *   <li>{功能点1}</li>
 *   <li>{功能点2}</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
public class [Resource]DomainService {
}
```

## 字段注释模板

```java
/**
 * <p>[依赖名称]</p>
 * 
 * <p>用于[用途说明]，负责[具体职责]
 */
private final [DependencyType] [dependencyName];
```

## 方法注释模板

### 业务规则验证方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>验证{业务规则名称}</p>
 * 
 * <p>验证{业务规则}是否满足，如果不满足则抛出业务异常。</p>
 * 
 * @param entity [Resource] {资源名称}实体对象
 * @exception com.example.exception.BusinessException 当{业务规则}不满足时抛出
 */
public void validate[BusinessRule]([Resource] entity) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 验证{业务规则名称}
 * 
 * <p>验证{业务规则}是否满足，如果不满足则抛出业务异常。
 * 
 * @param entity {资源名称}实体对象
 * @throws BusinessException 当{业务规则}不满足时抛出
 */
public void validate[BusinessRule]([Resource] entity) {
}
```

### 领域计算方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>计算{计算项名称}</p>
 * 
 * <p>根据{输入参数}计算{计算项}，计算规则包括：
 * <ol>
 *   <li>{计算步骤1}</li>
 *   <li>{计算步骤2}</li>
 *   <li>{计算步骤3}</li>
 * </ol>
 * </p>
 * 
 * @param entity [Resource] {资源名称}实体对象
 * @return java.math.BigDecimal {返回类型} 计算后的{计算项}值
 */
public BigDecimal calculate[CalculationItem]([Resource] entity) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 计算{计算项名称}
 * 
 * <p>根据{输入参数}计算{计算项}，计算规则包括：
 * <ol>
 *   <li>{计算步骤1}</li>
 *   <li>{计算步骤2}</li>
 *   <li>{计算步骤3}</li>
 * </ol>
 * 
 * @param entity {资源名称}实体对象
 * @return 计算后的{计算项}值
 */
public BigDecimal calculate[CalculationItem]([Resource] entity) {
}
```

### 领域转换方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>转换{转换目标}</p>
 * 
 * <p>将{源对象}转换为{目标对象}，转换过程中会进行{转换规则}等处理。</p>
 * 
 * @param source [SourceType] {源对象}，包含{字段列表}
 * @return [TargetType] {返回类型} 转换后的{目标对象}
 */
public [TargetType] convertTo[Target]([SourceType] source) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 转换{转换目标}
 * 
 * <p>将{源对象}转换为{目标对象}，转换过程中会进行{转换规则}等处理。
 * 
 * @param source {源对象}，包含{字段列表}
 * @return 转换后的{目标对象}
 */
public [TargetType] convertTo[Target]([SourceType] source) {
}
```

### 领域聚合方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>聚合{聚合目标}</p>
 * 
 * <p>将多个{资源名称}聚合为{聚合结果}，聚合规则包括：
 * <ul>
 *   <li>{聚合规则1}</li>
 *   <li>{聚合规则2}</li>
 * </ul>
 * </p>
 * 
 * @param entities java.util.List&lt;[Resource]&gt; {资源名称}实体列表
 * @return [AggregateType] {返回类型} 聚合后的{聚合结果}
 */
public [AggregateType] aggregate[Target](List<[Resource]> entities) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 聚合{聚合目标}
 * 
 * <p>将多个{资源名称}聚合为{聚合结果}，聚合规则包括：
 * <ul>
 *   <li>{聚合规则1}</li>
 *   <li>{聚合规则2}</li>
 * </ul>
 * 
 * @param entities {资源名称}实体列表
 * @return 聚合后的{聚合结果}
 */
public [AggregateType] aggregate[Target](List<[Resource]> entities) {
}
```

### 领域事件处理方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>处理{领域事件名称}</p>
 * 
 * <p>当{触发条件}时，处理{领域事件}，执行{处理逻辑}等操作。</p>
 * 
 * @param event [EventType] {领域事件}对象，包含{事件信息}
 */
public void handle[Event]([EventType] event) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 处理{领域事件名称}
 * 
 * <p>当{触发条件}时，处理{领域事件}，执行{处理逻辑}等操作。
 * 
 * @param event {领域事件}对象，包含{事件信息}
 */
public void handle[Event]([EventType] event) {
}
```

## 使用说明

1. **替换占位符**：
   - `{服务名称}` - 替换为实际的服务名称，如"用户"、"订单"等
   - `{资源名称}` - 替换为实际的资源名称，如"用户"、"订单"等
   - `[Resource]` - 替换为实际的类名，如"User"、"Order"等
   - `{功能点}` - 替换为实际的功能点描述
   - `{业务规则}` - 替换为实际的业务规则描述

2. **选择格式**：
   - 如果项目遵循《JAVA 编程规范》，使用"Java 编程规范格式（严格）"
   - 如果项目使用标准 JavaDoc，使用"标准 JavaDoc 格式"

3. **方法注释**：
   - 领域服务方法通常关注业务规则、计算、转换等核心领域逻辑
   - 方法注释应重点描述领域规则和业务逻辑
   - 避免描述技术实现细节，专注于业务语义

4. **领域服务特点**：
   - 领域服务通常是无状态的
   - 方法通常处理跨聚合的业务逻辑
   - 方法名应体现领域概念和业务语义
