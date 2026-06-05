---
name: java-conventions
description: 统一 Java 项目编码规范与注释规范（SLF4J+Lombok 日志、Bean Lombok 注解选择、判空 Objects/Optional、工具类优先级 Spring→Apache Commons→Hutool→Guava、复杂逻辑用设计模式/简单逻辑不拆分、Controller/Service/ServiceImpl/Mapper 注释一致性）。当需要“按 Java 规范重构/Review/补全注释/统一日志/统一工具类使用/补全 JavaDoc”时使用。
---

# Java Conventions

用于在 Java 项目中统一编码习惯与注释要求，帮助你在不引入过度设计的前提下保证一致性与可维护性。

## 使用流程
- 先判断改动范围：仅改动当前涉及的类/方法，不做无关格式化。
- 先统一基础规范：日志、判空、工具类选择、Bean 注解策略。
- 再做注释检查：对象注释、方法注释、逻辑块注释（非简单 CRUD）。
- 最后验证：编译 + 测试通过后再提交。

## 编码规范

### 日志规范（必选）
- 统一使用 SLF4J，并结合 Lombok 注解（例如 `@Slf4j`）。
- 禁止 `System.out.println`、`printStackTrace()`。
- 日志内容避免敏感信息与大对象全量输出。

示例：

```java
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class UserService {
  public void handle(String userId) {
    log.info("handle userId={}", userId);
  }
}
```

### Bean/Lombok 注解（按场景选择）
- 领域/DTO/VO/BO 等：按需要选 `@Getter`/`@Setter`/`@Builder`/`@Data`。
- 需要可控 equals/hashCode/toString 时：优先显式选择 Lombok 注解组合，避免一把梭。
- 当对象被序列化/日志输出频繁时：注意 `toString` 的敏感字段与大字段。

### 判空与防御式编程
- 判空优先使用 JDK 工具：`Objects.requireNonNull`、`Objects.nonNull`、`Optional`。
- 不要用“全局 try/catch 吞异常”的方式掩盖空指针问题；应在边界处校验输入。

示例：

```java
import java.util.Objects;

public void updateName(String name) {
  Objects.requireNonNull(name, "name must not be null");
}
```

### 工具类优先级（字符串 / 集合等）
- 优先级：Spring → Apache Commons → Hutool → Guava。
- 在已有依赖满足的前提下，避免为了一个小工具方法引入新依赖。
- 当同类工具同时存在时，统一团队选择，避免到处混用。

## 设计与拆分
- 复杂逻辑：优先通过设计模式（策略、模板方法、责任链等）提升可扩展性与可测试性。
- 简单逻辑：避免过度设计与过度拆分，保持可读性优先。
- 领域建模：业务规则尽量收敛到领域对象/领域服务，避免贫血模型堆在 ServiceImpl。

## 注释规范

### 规则（必选）
- 创建或更新任何对象/方法时，进行注释检查并补全/完善对象注释与方法注释。
- 若方法逻辑不是最简单的 CRUD，需要按逻辑块补充注释说明关键意图与边界条件。
- Controller、Service、ServiceImpl、Mapper 均需要注释，保持注释与代码一致（不写过期注释）。

### 建议模板
- 类：说明职责边界、输入输出、关键约束。
- 方法：说明做什么、关键参数含义、异常/返回约定。

更完整的注释模板与检查清单见 [references/api_reference.md](references/api_reference.md)。

## 输出要求（用于 Review/改造时的交付）
- 列出：已调整的规范点（日志/判空/工具类/注释）。
- 附带：受影响文件清单与验证方式（编译/测试）。
