# Search Maven Components by Name

## Instructions

This example demonstrates how to search for Maven components by name or keywords using the Maven Central Search API.

## Key Concepts

- **Search API Endpoint**: `https://search.maven.org/solrsearch/select`
- **Query Parameter**: Use `q` parameter for search query
- **Text Search**: Searches in groupId, artifactId, and description fields
- **Response Format**: JSON (default) or XML
- **Pagination**: Use `rows` and `start` parameters

## Example

### Search by Component Name

**Request**:
```
GET https://search.maven.org/solrsearch/select?q=guava&rows=20&wt=json
```

**Response Structure**:
```json
{
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

### Search with Multiple Keywords

**Request**:
```
GET https://search.maven.org/solrsearch/select?q=spring+boot&rows=20&wt=json
```

### Search with Filters

**Request** (search in specific field):
```
GET https://search.maven.org/solrsearch/select?q=a:guava&rows=20&wt=json
```

## Key Points

1. **Text Search**: Simple text query searches across groupId, artifactId, and description
2. **Field-Specific Search**: Use `g:` for groupId, `a:` for artifactId, `v:` for version
3. **Combined Search**: Use `AND` and `OR` operators for complex queries
4. **Result Formatting**: Extract `g` (groupId), `a` (artifactId), `v` (version) from response
5. **Pagination**: Use `rows` (max 200) and `start` for pagination

## Official Documentation

- **Maven Central Search**: https://search.maven.org/
- **Search API Documentation**: https://central.sonatype.com/search-api/
