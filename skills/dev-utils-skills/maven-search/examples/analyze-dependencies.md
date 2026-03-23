# Analyze Maven Dependencies

## Instructions

This example demonstrates how to analyze dependencies by downloading and parsing POM files.

## Key Concepts

- **POM File**: Project Object Model contains dependency information
- **Dependency Tree**: Parse POM to extract direct and transitive dependencies
- **Dependency Coordinates**: Extract groupId, artifactId, version from POM
- **Scope Information**: Dependencies have scopes (compile, test, provided, runtime)
- **Transitive Dependencies**: Dependencies of dependencies

## Example

### Download and Parse POM

**Step 1: Download POM File**

**Request**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.pom
```

**Step 2: Parse Dependencies**

**POM Structure**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <version>33.0.0</version>
  <dependencies>
    <dependency>
      <groupId>com.google.code.findbugs</groupId>
      <artifactId>jsr305</artifactId>
      <version>3.0.2</version>
      <scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

### Extract Dependency Information

**Dependency Format**: `groupId:artifactId:version:scope`

**Example Output**:
```
Direct Dependencies:
- com.google.code.findbugs:jsr305:3.0.2:provided
```

## Key Points

1. **POM Location**: `{groupId}/{artifactId}/{version}/{artifactId}-{version}.pom`
2. **XML Parsing**: Parse XML to extract dependency information
3. **Scope Handling**: Include scope information (compile, test, provided, runtime)
4. **Optional Dependencies**: Check for optional dependencies
5. **Version Ranges**: Handle version ranges in dependency declarations

## Official Documentation

- **Maven POM Reference**: https://maven.apache.org/pom.html
- **Maven Dependency Mechanism**: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html
