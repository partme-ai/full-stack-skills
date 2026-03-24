# Get Maven Component Version Information

## Instructions

This example demonstrates how to retrieve version information and version history for a Maven component.

## Key Concepts

- **Metadata File**: `maven-metadata.xml` contains version information
- **Latest Version**: Query metadata to get latest release version
- **Version History**: Metadata includes all available versions
- **Release Dates**: Timestamp information available in search results
- **Version Sorting**: Versions are typically sorted by release date

## Example

### Get Version Metadata

**Request**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/maven-metadata.xml
```

**Response**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadata>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <versioning>
    <latest>33.0.0</latest>
    <release>33.0.0</release>
    <versions>
      <version>33.0.0</version>
      <version>32.1.3</version>
      <version>32.1.2</version>
    </versions>
    <lastUpdated>20240101120000</lastUpdated>
  </versioning>
</metadata>
```

### Get Latest Version via Search API

**Request**:
```
GET https://search.maven.org/solrsearch/select?q=g:com.google.guava+AND+a:guava&rows=1&sort=timestamp+desc&wt=json
```

## Key Points

1. **Metadata Location**: `{groupId}/{artifactId}/maven-metadata.xml`
2. **Path Conversion**: Replace dots in groupId with slashes
3. **Latest Version**: Check `latest` or `release` tag in metadata
4. **Version List**: All versions listed in `versions` section
5. **Last Updated**: Timestamp indicates last update time

## Official Documentation

- **Maven Central Repository**: https://repo1.maven.org/maven2/
- **Maven Metadata Guide**: https://maven.apache.org/ref/current/maven-repository-metadata/
