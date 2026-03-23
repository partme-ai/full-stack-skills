# Maven Central Repository API Reference

## Base URLs

- **Repository**: https://repo1.maven.org/maven2/
- **Search API**: https://search.maven.org/solrsearch/select

## Search API

### Endpoint
```
GET https://search.maven.org/solrsearch/select
```

### Query Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `q` | string | Search query | Required |
| `rows` | integer | Number of results | 20 (max: 200) |
| `start` | integer | Pagination offset | 0 |
| `wt` | string | Response format (json, xml, javabin) | json |
| `core` | string | Search core (gav) | gav |

### Query Syntax

- **Text Search**: `guava` (searches in groupId, artifactId, description)
- **GroupId**: `g:com.google.guava`
- **ArtifactId**: `a:guava`
- **Version**: `v:33.0.0`
- **Combined**: `g:com.google.guava AND a:guava`
- **OR Operator**: `g:com.google.guava OR g:com.google.collections`

### Response Format (JSON)

```json
{
  "responseHeader": {
    "status": 0,
    "QTime": 10
  },
  "response": {
    "numFound": 100,
    "start": 0,
    "docs": [
      {
        "id": "com.google.guava:guava:33.0.0",
        "g": "com.google.guava",
        "a": "guava",
        "v": "33.0.0",
        "p": "jar",
        "timestamp": 1234567890000,
        "ec": ["-sources.jar", "-javadoc.jar", ".jar", ".pom"]
      }
    ]
  }
}
```

## Direct Repository Access

### Path Structure
```
{groupId}/{artifactId}/{version}/{artifactId}-{version}.{extension}
```

### GroupId Path Conversion
Replace dots (`.`) with slashes (`/`)

**Example**:
- GroupId: `com.google.guava`
- Path: `com/google/guava`

### Available Files

- **POM**: `{artifactId}-{version}.pom`
- **JAR**: `{artifactId}-{version}.jar`
- **Sources**: `{artifactId}-{version}-sources.jar`
- **Javadoc**: `{artifactId}-{version}-javadoc.jar`
- **Metadata**: `maven-metadata.xml`

## Official Documentation

- **Maven Central Search**: https://search.maven.org/
- **Search API Documentation**: https://central.sonatype.com/search-api/
- **Maven Central Repository**: https://repo1.maven.org/maven2/
