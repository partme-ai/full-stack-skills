---
name: junit
description: Provides comprehensive guidance for JUnit testing framework including test annotations, assertions, test lifecycle, and best practices. Use when the user asks about JUnit, needs to write Java unit tests, use JUnit annotations, or configure JUnit for Java projects.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 JUnit 4/5 编写 Java/Kotlin 单元测试与扩展
- 使用断言、生命周期、参数化与 mock（Mockito 等）

## How to use this skill

1. **用例**：@Test、@BeforeEach、@AfterEach；Assertions（assertEquals、assertThrows）；@ParameterizedTest。
2. **生态**：JUnit 5 + Mockito/AssertJ；Maven/Gradle 依赖与 surefire 配置。
3. **运行**：mvn test、gradle test；IDE 运行与覆盖率。

## Best Practices

- 单测独立、可重复；避免依赖顺序与外部服务。
- 用 mock 隔离依赖；命名与结构清晰。
- 覆盖率与速度平衡；CI 中必跑。

## Keywords

junit, JUnit 5, 单元测试, Java, Kotlin
