# Multi-Module Build Configuration for DDD

## Maven Multi-Module Setup

### Parent POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>ddd-project</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>domain</module>
        <module>application</module>
        <module>infrastructure</module>
        <module>adapter</module>
        <module>start</module>
    </modules>

    <properties>
        <java.version>17</java.version>
        <archunit.version>1.3.0</archunit.version>
        <maven-surefire.version>3.2.5</maven-surefire.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>3.2.5</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
```

### Domain Module POM (Zero Framework Dependencies)

```xml
<project>
    <parent>
        <groupId>com.example</groupId>
        <artifactId>ddd-project</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>
    <artifactId>domain</artifactId>

    <dependencies>
        <!-- ⚠️ No Spring, No JPA, No MyBatis -->
        <dependency>
            <groupId>com.tngtech.archunit</groupId>
            <artifactId>archunit-junit5</artifactId>
            <version>${archunit.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <configuration>
                    <includes>
                        <include>**/*Test.java</include>
                    </includes>
                    <forkCount>2</forkCount>
                    <reuseForks>true</reuseForks>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

## Gradle Multi-Module Setup

```kotlin
// settings.gradle.kts
rootProject.name = "ddd-project"
include("domain", "application", "infrastructure", "adapter", "start")

// domain/build.gradle.kts — Zero framework dependencies
plugins {
    id("java-library")
}

dependencies {
    testImplementation("com.tngtech.archunit:archunit-junit5:1.3.0")
}

// application/build.gradle.kts
dependencies {
    implementation(project(":domain"))
    implementation("org.springframework:spring-tx")
}

// infrastructure/build.gradle.kts
dependencies {
    implementation(project(":domain"))
    implementation("org.springframework.boot:spring-boot-starter-data-jpa")
}
```

## Incremental Build Optimization

```bash
# Maven — Build only changed modules
mvn compile -pl domain,application -am

# Gradle — Parallel build
./gradlew build --parallel --max-workers=4

# Maven — Skip domain tests in fast CI
mvn verify -pl '!domain' \
  -Dtest='!ArchitectureComplianceTest'

# Maven — Parallel module builds
mvn -T 4 clean install \
  -DskipTests \
  -pl '!adapter,!start'
```

## CI/CD Build Cache

```yaml
# .github/actions/maven-cache/action.yml
name: "Maven Cache for DDD"
runs:
  using: "composite"
  steps:
    - name: Cache Maven dependencies
      uses: actions/cache@v4
      with:
        path: |
          ~/.m2/repository
          !~/.m2/repository/com/example
        key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
        restore-keys: |
          ${{ runner.os }}-maven-

    - name: Cache module build outputs
      uses: actions/cache@v4
      with:
        path: |
          domain/target/classes
          application/target/classes
          infrastructure/target/classes
        key: ${{ runner.os }}-build-${{ github.sha }}
        restore-keys: |
          ${{ runner.os }}-build-
```

## Dependency Graph Validation

```bash
# Maven — Display dependency tree
mvn dependency:tree -Dverbose | grep "com.example"

# Gradle — Display project dependencies
./gradlew :domain:dependencies --configuration runtimeClasspath

# Check for unintended domain dependencies
mvn dependency:tree -pl domain \
  | grep -E "(spring|hibernate|jackson|mybatis)" \
  && echo "⚠️ Domain has external dependencies!" \
  || echo "✅ Domain is clean"
```

## Module Dependency Rules

```yaml
domain:          # Zero external dependencies (JDK only)
  dependencies: []
  rules:
    - no_spring
    - no_jpa
    - no_mybatis
    - no_infrastructure

application:     # Depends on domain only
  dependencies: [domain]
  rules:
    - no_direct_infrastructure_import
    - no_business_logic_in_app_services

infrastructure:  # Implements domain interfaces
  dependencies: [domain]
  rules:
    - must_implement_all_domain_repositories

adapter:         # Depends on application + domain
  dependencies: [domain, application]
  rules:
    - no_business_logic
    - protocol_conversion_only

start:           # Assembles all modules
  dependencies: [domain, application, infrastructure, adapter]
  rules:
    - no_business_logic
    - minimal_code
```
