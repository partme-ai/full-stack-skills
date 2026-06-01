# COLA v5 ArchUnit 架构校验

## 依赖方向校验

```java
import com.tngtech.archunit.junit.AnalyzeClasses;
import com.tngtech.archunit.junit.ArchTest;
import com.tngtech.archunit.lang.ArchRule;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;

@AnalyzeClasses(packages = "com.yourcompany")
public class ArchitectureComplianceTest {

    // 规则 1：Domain 层不能依赖 Infrastructure
    @ArchTest
    static final ArchRule domain_should_not_depend_on_infrastructure =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .because("Domain layer must not depend on infrastructure");

    // 规则 2：Domain 层不能依赖 App
    @ArchTest
    static final ArchRule domain_should_not_depend_on_app =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..app..")
            .because("Domain layer must not depend on application");

    // 规则 3：Domain 层不能依赖 Adapter
    @ArchTest
    static final ArchRule domain_should_not_depend_on_adapter =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..adapter..")
            .because("Domain layer must not depend on adapter");
}
```

## 框架依赖校验

```java
// 规则 4：Domain 层不能有 Spring Framework 依赖
@ArchTest
static final ArchRule domain_should_not_depend_on_spring =
    noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAnyPackage("org.springframework..", "org.springframework.stereotype..")
        .because("Domain layer must have zero framework dependencies");

// 规则 5：Domain 层不能有 JPA 依赖
@ArchTest
static final ArchRule domain_should_not_depend_on_jpa =
    noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAnyPackage("javax.persistence..", "jakarta.persistence..")
        .because("Domain layer must not depend on JPA");

// 规则 6：Domain 层不能有 MyBatis 依赖
@ArchTest
static final ArchRule domain_should_not_depend_on_mybatis =
    noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAnyPackage("org.apache.ibatis..", "org.mybatis..")
        .because("Domain layer must not depend on MyBatis");
```

## 层职责校验

```java
// 规则 7：Adapter 层不能依赖 Infrastructure
@ArchTest
static final ArchRule adapter_should_not_depend_on_infrastructure =
    noClasses()
        .that().resideInAPackage("..adapter..")
        .should().dependOnClassesThat()
        .resideInAPackage("..infrastructure..")
        .because("Adapter must go through App layer");

// 规则 8：App 层可以依赖 Domain 和 Infrastructure
@ArchTest
static final ArchRule app_should_only_depend_on_domain_and_infra =
    classes()
        .that().resideInAPackage("..app..")
        .should().onlyDependOnClassesThat()
        .resideInAnyPackage(
            "..app..", "..domain..", "..infrastructure..",
            "java..", "lombok..", "org.springframework.."
        ).because("App should only depend on domain and infrastructure");
```

## 包命名校验

```java
// 规则 9：Domain 层不应该包含 controller
@ArchTest
static final ArchRule domain_package_should_not_contain_controller =
    noClasses()
        .that().resideInAPackage("..domain..")
        .should().resideInAPackage("..controller..")
        .because("Controller belongs in adapter layer");

// 规则 10：Adapter 层不应该包含 repository
@ArchTest
static final ArchRule adapter_should_not_contain_repository =
    noClasses()
        .that().resideInAPackage("..adapter..")
        .should().resideInAPackage("..repository..")
        .because("Repository belongs in domain or infrastructure");
```

## CI/CD 集成

### GitHub Actions

```yaml
name: COLA Architecture Check
on: [push, pull_request]
jobs:
  architecture-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Run Architecture Tests
        run: mvn test -Dtest=ArchitectureComplianceTest
```

### Python 校验脚本

提供 `scripts/check_cola.py` 进行静态分析：
```bash
python scripts/check_cola.py /path/to/project
```

## 评分模型

| 分级 | 分数 | 含义 |
|------|:----:|------|
| A (Excellent) | ≥ 90 | 合规优秀，无违规或少量 P2 |
| B (Good) | 70-89 | 基本合规，有改进空间 |
| C (Fair) | 50-69 | 存在明显违规，需修复 P0 |
| D (Needs Refactoring) | < 50 | 架构严重违规，建议重建 |

## check_cola.py 校验

`scripts/check_cola.py` 提供以下校验能力：

1. **Domain 纯净度检查**：扫描 Domain 层的 import 语句，检测框架依赖
2. **依赖方向检查**：检测 Domain → Infrastructure/App/Adapter 的反向依赖
3. **包命名规范**：检查包名是否符合 COLA 约定
4. **循环依赖检测**：DFS 遍历模块依赖图，检测环
5. **合规评分**：P0 = 10分，P1 = 5分，P2 = 2分的扣分模型
