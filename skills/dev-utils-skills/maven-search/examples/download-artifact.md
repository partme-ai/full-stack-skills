# Download Maven Artifacts

## Instructions

This example demonstrates how to construct download URLs for Maven artifacts (JAR, POM, sources, Javadoc).

## Key Concepts

- **Repository Base URL**: `https://repo1.maven.org/maven2/`
- **Path Structure**: `{groupId}/{artifactId}/{version}/{artifactId}-{version}.{extension}`
- **GroupId Path**: Replace dots with slashes
- **Artifact Types**: JAR, POM, sources, Javadoc
- **Direct Download**: Construct direct URL for artifact download

## Example

### Download JAR File

**Coordinates**: `com.google.guava:guava:33.0.0`

**URL Construction**:
- GroupId path: `com/google/guava`
- ArtifactId: `guava`
- Version: `33.0.0`
- Extension: `jar`

**Download URL**:
```
https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.jar
```

### Download POM File

**Download URL**:
```
https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.pom
```

### Download Sources

**Download URL**:
```
https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0-sources.jar
```

### Download Javadoc

**Download URL**:
```
https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0-javadoc.jar
```

## Key Points

1. **Path Format**: `{groupId}/{artifactId}/{version}/{artifactId}-{version}.{extension}`
2. **GroupId Conversion**: Replace dots (`.`) with slashes (`/`)
3. **Artifact Naming**: Follows Maven naming conventions
4. **Classifier Support**: Sources and Javadoc use classifiers (`-sources`, `-javadoc`)
5. **URL Validation**: Verify artifact exists before providing download link

## Official Documentation

- **Maven Central Repository**: https://repo1.maven.org/maven2/
- **Maven Repository Layout**: https://maven.apache.org/repository/layout.html
