# ArchUnit Compliance Test Suite

P0/P1/P2 分级门禁的 ArchUnit 测试实现。

## P0 — Block Merge（阻断合并）

```java
@ArchTest
static final ArchRule domain_should_not_depend_on_framework =
    classes().that().resideInAPackage("..domain..")
        .should().onlyDependOnClassesThat()
        .resideInAnyPackage("..domain..", "java..", "org.slf4j..");
```

## P1 — Warning（告警）

```java
@ArchTest
static final ArchRule no_cyclic_dependencies =
    slices().matching("..domain.(*)..")
        .should().beFreeOfCycles();
```

## P2 — Report（报告）

```java
@ArchTest
static final ArchRule naming_convention =
    classes().that().areAnnotatedWith(Service.class)
        .should().haveSimpleNameEndingWith("Service");
```

## 运行方式

将上述规则放在 `src/test/java/architecture/` 下，JUnit 5 + ArchUnit Runner 自动执行。
