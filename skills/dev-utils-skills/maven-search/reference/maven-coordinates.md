# Maven Coordinates Reference

## Coordinate Format

Maven coordinates follow the format:
```
groupId:artifactId:version
```

## GroupId

- **Format**: Reverse domain notation
- **Examples**: 
  - `com.google.guava`
  - `org.springframework.boot`
  - `io.github.projectlombok`
- **Rules**:
  - Should follow reverse domain notation
  - Use lowercase letters
  - Separate segments with dots (`.`)
  - Should be unique across organizations

## ArtifactId

- **Format**: Lowercase, hyphen-separated
- **Examples**:
  - `guava`
  - `spring-boot-starter-web`
  - `lombok`
- **Rules**:
  - Use lowercase letters
  - Separate words with hyphens (`-`)
  - Should be descriptive of the component

## Version

- **Format**: Semantic versioning preferred
- **Examples**:
  - `33.0.0` (release version)
  - `1.0.0-SNAPSHOT` (snapshot version)
  - `2.5.0-RELEASE` (release version)
- **Rules**:
  - Follow semantic versioning (major.minor.patch)
  - Avoid snapshot versions in production
  - Use release versions for stability

## Complete Coordinate Examples

```
com.google.guava:guava:33.0.0
org.springframework.boot:spring-boot-starter-web:3.2.0
io.projectreactor:reactor-core:3.6.0
```

## Official Documentation

- **Maven Naming Conventions**: https://maven.apache.org/guides/mini/guide-naming-conventions.html
