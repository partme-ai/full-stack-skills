# Architecture Test Examples — DDD 分层架构测试

使用 ArchUnit 验证 DDD 分层架构的依赖方向合规。

## 分层架构依赖检查

```java
@AnalyzeClasses(packages = "com.example.ddd")
class ArchitectureTest {
    @Test void domain_layer_should_not_depend_on_other_layers() {
        JavaClasses classes = new ClassFileImporter()
            .importPackages("com.example.ddd");
        ArchRule rule = layeredArchitecture()
            .layer("Domain").definedBy("..domain..")
            .layer("Application").definedBy("..application..")
            .layer("Adapter").definedBy("..adapter..")
            .layer("Infrastructure").definedBy("..infrastructure..")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers("Application", "Infrastructure")
            .whereLayer("Application").mayNotBeAccessedByLayers("Adapter")
            .whereLayer("Adapter").mayNotBeAccessedByLayers("Infrastructure");
        rule.check(classes);
    }
}
```

## 聚合根不应被外部直接依赖

```java
@Test void aggregate_should_not_expose_internals() {
    ArchRule rule = classes()
        .that().areAnnotatedWith(AggregateRoot.class)
        .should().onlyHaveAccessorsThatAreDeclaredIn("..domain..");
    rule.check(classes);
}
```

## Repository 接口应在 Domain 层

```java
@Test void repository_interfaces_belong_in_domain() {
    ArchRule rule = classes()
        .that().haveSimpleNameEndingWith("Repository")
        .and().areInterfaces()
        .should().resideInAPackage("..domain..");
    rule.check(classes);
}
```

## 领域事件命名规范

```java
@Test void domain_events_should_have_past_tense_names() {
    ArchRule rule = classes()
        .that().areAssignableTo(DomainEvent.class)
        .should().haveSimpleNameEndingWith("Event");
    rule.check(classes);
}
```
