# Verify Maven Coordinates

## Instructions

This example demonstrates how to verify that Maven coordinates (groupId, artifactId, version) are valid and the artifact exists.

## Key Concepts

- **Coordinate Validation**: Check format and existence
- **GroupId Format**: Reverse domain notation (e.g., `com.google.guava`)
- **ArtifactId Format**: Lowercase, hyphen-separated (e.g., `guava`, `spring-boot`)
- **Version Format**: Semantic versioning preferred
- **Existence Check**: Verify artifact exists in repository

## Example

### Verify Coordinates Format

**Valid Coordinates**:
- `com.google.guava:guava:33.0.0` ✓
- `org.springframework.boot:spring-boot-starter-web:3.2.0` ✓

**Invalid Coordinates**:
- `com.google.guava:guava` ✗ (missing version)
- `guava:33.0.0` ✗ (missing groupId)
- `com.google.guava::33.0.0` ✗ (missing artifactId)

### Verify Artifact Existence

**Method 1: Check Metadata**

**Request**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/maven-metadata.xml
```

**If 404**: Artifact does not exist
**If 200**: Artifact exists, check version in metadata

**Method 2: Check Specific Version**

**Request**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.pom
```

**If 404**: Version does not exist
**If 200**: Version exists

## Key Points

1. **Format Validation**: Check coordinate format before querying
2. **GroupId Rules**: Should follow reverse domain notation
3. **ArtifactId Rules**: Should be lowercase, hyphen-separated
4. **Version Rules**: Should follow semantic versioning
5. **Existence Check**: Always verify artifact exists before use

## Official Documentation

- **Maven Naming Conventions**: https://maven.apache.org/guides/mini/guide-naming-conventions.html
- **Maven Central Repository**: https://repo1.maven.org/maven2/
