# Search Maven Components by Coordinates

## Instructions

This example demonstrates how to search for Maven components using groupId and artifactId coordinates.

## Key Concepts

- **Maven Coordinates**: `groupId:artifactId:version` format
- **GroupId Search**: Use `g:` prefix in query
- **ArtifactId Search**: Use `a:` prefix in query
- **Combined Search**: Use `AND` operator to combine groupId and artifactId
- **Exact Match**: More precise than text search

## Example

### Search by GroupId and ArtifactId

**Request**:
```
GET https://search.maven.org/solrsearch/select?q=g:com.google.guava+AND+a:guava&rows=20&wt=json
```

**Response**:
```json
{
  "response": {
    "numFound": 50,
    "start": 0,
    "docs": [
      {
        "id": "com.google.guava:guava:33.0.0",
        "g": "com.google.guava",
        "a": "guava",
        "v": "33.0.0",
        "p": "jar",
        "timestamp": 1234567890000
      }
    ]
  }
}
```

### Search by GroupId Only

**Request**:
```
GET https://search.maven.org/solrsearch/select?q=g:org.springframework&rows=50&wt=json
```

### Search by ArtifactId Only

**Request**:
```
GET https://search.maven.org/solrsearch/select?q=a:spring-boot-starter-web&rows=20&wt=json
```

## Key Points

1. **Coordinate Format**: Always use `groupId:artifactId:version` format
2. **URL Encoding**: Replace spaces with `+` in query parameters
3. **Exact Matching**: Coordinate search provides exact matches
4. **Multiple Versions**: Results include all available versions
5. **Latest Version**: Sort by timestamp descending to get latest version

## Official Documentation

- **Maven Central Search**: https://search.maven.org/
- **Maven Coordinates Guide**: https://maven.apache.org/guides/mini/guide-naming-conventions.html
