---
name: maven-search
description: Provides comprehensive guidance for searching and retrieving Maven components from Maven Central Repository (https://repo1.maven.org/maven2/). This skill enables searching by groupId, artifactId, version, and other coordinates, retrieving component metadata (POM files, JARs, sources, Javadoc), querying version history, and analyzing dependencies. Use when the user needs to find, verify, or retrieve Maven dependencies, check component versions, analyze dependency trees, or work with Maven coordinates.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Searching for Maven dependencies or components
- Finding Maven coordinates (groupId, artifactId, version)
- Checking component versions or version history
- Retrieving Maven artifacts (JAR, POM, sources, Javadoc)
- Verifying Maven dependency coordinates
- Analyzing dependency trees or transitive dependencies
- Working with Maven Central Repository
- Any request related to Maven components, libraries, or dependencies

**Trigger phrases include:**
- "查找 Maven 依赖" (find Maven dependency), "搜索 Maven 组件" (search Maven component)
- "Maven 坐标" (Maven coordinates), "groupId" (groupId), "artifactId" (artifactId)
- "Maven 版本" (Maven version), "最新版本" (latest version), "版本历史" (version history)
- "Maven Central" (Maven Central), "Maven 仓库" (Maven repository)
- "下载 Maven 依赖" (download Maven dependency), "获取 POM 文件" (get POM file)
- "依赖树" (dependency tree), "传递依赖" (transitive dependencies)
- Any mention of "Maven", "dependency", "artifact", "repository", "coordinates"

## How to use this skill

**CRITICAL: This skill should be triggered when the user needs to search, retrieve, or work with Maven components from Maven Central Repository.**

**Trigger this skill when you see:**
- User says "查找 Maven 依赖" (find Maven dependency), "搜索 Maven 组件" (search Maven component)
- User needs Maven coordinates (groupId, artifactId, version)
- User wants to check component versions or retrieve artifacts
- User mentions Maven Central Repository or Maven dependencies
- User needs to analyze dependencies or verify coordinates

To search for Maven components:

1. **Identify the search type** from the user's request:
   - Search by name → Use Maven Central Search API
   - Get specific version → Use direct repository URL
   - Check latest version → Query maven-metadata.xml
   - Analyze dependencies → Parse POM file
   - Download artifact → Use direct download URL

2. **Load the appropriate example file** from the `examples/` directory:
   - `examples/search-by-name.md` - Search components by name or keywords
   - `examples/search-by-coordinates.md` - Search by groupId and artifactId
   - `examples/get-version-info.md` - Get version information and history
   - `examples/download-artifact.md` - Download JAR, POM, sources, or Javadoc
   - `examples/analyze-dependencies.md` - Analyze dependency tree
   - `examples/verify-coordinates.md` - Verify Maven coordinates validity

3. **Follow the specific instructions** in that example file for API endpoints, parameters, and best practices

4. **Use Maven Central Repository API**:
   
   **Search API** (https://search.maven.org/solrsearch/select):
   - Query parameter: `q` - Search query (e.g., `g:com.google.guava AND a:guava`)
   - Rows parameter: `rows` - Number of results (default: 20, max: 200)
   - Start parameter: `start` - Pagination offset
   - Core parameter: `core` - Search core (default: `gav`)
   
   **Direct Repository Access** (https://repo1.maven.org/maven2/):
   - Path format: `{groupId}/{artifactId}/{version}/{artifactId}-{version}.{extension}`
   - GroupId path: Replace dots with slashes (e.g., `com.google.guava` → `com/google/guava`)
   - Metadata: `maven-metadata.xml` for version information
   - POM file: `{artifactId}-{version}.pom`
   - JAR file: `{artifactId}-{version}.jar`
   - Sources: `{artifactId}-{version}-sources.jar`
   - Javadoc: `{artifactId}-{version}-javadoc.jar`

5. **Construct the appropriate URL**:
   
   **Search Example**:
   ```
   https://search.maven.org/solrsearch/select?q=g:com.google.guava+AND+a:guava&rows=20&wt=json
   ```
   
   **Direct Access Example**:
   ```
   https://repo1.maven.org/maven2/com/google/guava/guava/maven-metadata.xml
   https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.pom
   https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.jar
   ```

6. **Parse and format the results**:
   - Extract relevant information (groupId, artifactId, version, description)
   - Format coordinates in standard Maven format: `groupId:artifactId:version`
   - Present results in a clear, structured format
   - Include download links and metadata when relevant

7. **Validate coordinates**:
   - Verify groupId format (should be reverse domain notation)
   - Check artifactId format (should be lowercase, hyphen-separated)
   - Validate version format (semantic versioning preferred)
   - Confirm artifact exists before providing download links

**Output Format Requirements**:
- Always provide Maven coordinates in standard format: `groupId:artifactId:version`
- Include direct download URLs when relevant
- Format search results in a clear, structured table or list
- Provide metadata information (description, repository, last updated) when available
- Include version information and release dates when querying versions

## Maven Central Repository Structure

### Repository Base URL
- **Primary**: https://repo1.maven.org/maven2/
- **Search API**: https://search.maven.org/solrsearch/select
- **Alternative mirrors**: Available for different regions

### Path Structure
```
{groupId}/{artifactId}/{version}/{artifactId}-{version}.{extension}
```

**Example**:
```
com/google/guava/guava/33.0.0/guava-33.0.0.jar
```

### Available Artifacts
- **POM**: `{artifactId}-{version}.pom` - Project Object Model file
- **JAR**: `{artifactId}-{version}.jar` - Compiled Java classes
- **Sources**: `{artifactId}-{version}-sources.jar` - Source code
- **Javadoc**: `{artifactId}-{version}-javadoc.jar` - API documentation
- **Metadata**: `maven-metadata.xml` - Version and release information

## Search API Parameters

### Query Syntax
- **GroupId search**: `g:com.google.guava`
- **ArtifactId search**: `a:guava`
- **Version search**: `v:33.0.0`
- **Combined search**: `g:com.google.guava AND a:guava`
- **Text search**: `guava` (searches in groupId, artifactId, and description)

### Response Format
- **JSON**: `wt=json` (default)
- **XML**: `wt=xml`
- **Java properties**: `wt=javabin`

### Pagination
- **rows**: Number of results per page (default: 20, max: 200)
- **start**: Offset for pagination (default: 0)

## Best Practices

1. **Always verify coordinates**: Check that groupId, artifactId, and version exist before use
2. **Use latest stable versions**: Prefer RELEASE versions over SNAPSHOT versions
3. **Check version metadata**: Query `maven-metadata.xml` for latest version information
4. **Validate before download**: Verify artifact exists before providing download links
5. **Include checksums**: When available, provide SHA-1 and MD5 checksums for verification
6. **Format coordinates correctly**: Always use standard Maven format `groupId:artifactId:version`
7. **Provide context**: Include description, repository information, and last updated date when available

## Common Tasks

### Task 1: Search by Name
Use the Search API with text query to find components by name or keywords.

**Example**:
```
GET https://search.maven.org/solrsearch/select?q=guava&rows=20&wt=json
```

### Task 2: Search by Coordinates
Use the Search API with groupId and artifactId to find specific components.

**Example**:
```
GET https://search.maven.org/solrsearch/select?q=g:com.google.guava+AND+a:guava&rows=20&wt=json
```

### Task 3: Get Version Information
Query `maven-metadata.xml` to get all available versions and latest version.

**Example**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/maven-metadata.xml
```

### Task 4: Download Artifact
Construct direct download URL for specific artifact.

**Example**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.jar
```

### Task 5: Analyze Dependencies
Download and parse POM file to extract dependency information.

**Example**:
```
GET https://repo1.maven.org/maven2/com/google/guava/guava/33.0.0/guava-33.0.0.pom
```

## Keywords

**English keywords:**
maven, maven central, maven repository, maven dependency, maven artifact, maven component, groupId, artifactId, version, coordinates, pom, jar, dependency, repository, search, retrieve, download, metadata, transitive dependencies, dependency tree, maven coordinates, maven search

**Chinese keywords (中文关键词):**
Maven, Maven 中央仓库, Maven 仓库, Maven 依赖, Maven 组件, Maven 坐标, groupId, artifactId, version, 版本, 坐标, POM, JAR, 依赖, 仓库, 搜索, 检索, 下载, 元数据, 传递依赖, 依赖树, 查找依赖, 搜索组件, 获取版本, 下载依赖

## Resources

- **Maven Central Repository**: https://repo1.maven.org/maven2/
- **Maven Central Search**: https://search.maven.org/
- **Maven Central Search API Documentation**: https://central.sonatype.com/search-api/
- **Maven Coordinates Guide**: https://maven.apache.org/guides/mini/guide-naming-conventions.html
