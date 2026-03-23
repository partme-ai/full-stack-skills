---
name: api-doc-generator
description: |
  Provides comprehensive guidance for generating API documentation by scanning code interfaces, extracting request/response 
  information, and creating standardized API documentation. Use ONLY when the user explicitly mentions generating API 
  documentation, creating API docs, scanning interfaces, or documenting APIs. The skill scans Controller classes, extracts 
  interface information (URL, method, parameters, response), and generates documentation following standard templates. 
  Do NOT trigger for generic documentation requests without explicit API documentation mention.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**CRITICAL: This skill should ONLY be triggered when the user explicitly mentions generating API documentation, creating API docs, scanning interfaces, or documenting APIs.**

**ALWAYS use this skill when the user mentions:**
- Generating API documentation (explicitly mentions "API documentation" or "API docs")
- Creating API documentation from code
- Scanning interfaces to generate documentation
- Documenting REST APIs
- 生成接口文档 (explicitly mentions "接口文档")
- 扫描接口生成文档 (scan interfaces to generate documentation)
- 创建API文档 (create API documentation)

**Trigger phrases include:**
- "生成接口文档" (generate API documentation) - **must include "接口文档"**
- "扫描接口生成文档" (scan interfaces to generate documentation)
- "创建API文档" (create API documentation)
- "为接口生成文档" (generate documentation for interfaces)
- "接口文档生成" (API documentation generation)

**DO NOT trigger this skill for:**
- Generic documentation requests without mentioning API/interfaces
- Code comments generation
- README file generation
- Other types of documentation (user guides, technical specs, etc.)
- "生成文档" without "接口" or "API" (too generic)

## How to use this skill

**CRITICAL: This skill should ONLY be triggered when the user explicitly mentions generating API documentation. Do NOT trigger for generic documentation requests without API context.**

### Workflow Overview

This skill follows a systematic 4-step workflow:

1. **Scan Code** - Check current project or specified objects for Controller classes and API interfaces
2. **Extract Information** - Scan interfaces to collect request URL, method, parameters, and response information
3. **Generate Documentation** - Create API documentation following the standard template
4. **Save Output** - Save documentation to `./docs` directory in the current project

### Step-by-Step Process

#### Step 1: Scan Code for Interfaces

**CRITICAL: Before generating any documentation, you MUST scan the code to find API interfaces.**

1. **Identify Target**:
   - Ask user if they want to scan the entire project or specific Controller classes
   - If no target specified, scan the entire project for Controller classes
   - Common Controller patterns:
     - Java: `@RestController`, `@Controller` with `@RequestMapping`
     - Spring Boot: Classes in `controller` or `web` package
     - Files ending with `Controller.java` or `Controller.kt`

2. **Scan for Controllers**:
   - Search for Controller classes in the project
   - Identify all classes annotated with `@RestController` or `@Controller`
   - List all found Controller classes

3. **Check for Interfaces**:
   - For each Controller class, scan for methods annotated with:
     - `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`
     - `@RequestMapping` with method specification
   - Count total number of API interfaces found

4. **Validation**:
   - If no interfaces found, **STOP** and inform user:
     ```
     未找到任何接口，无法生成接口文档。请确认：
     1. 项目中是否存在 Controller 类
     2. Controller 类中是否有 @GetMapping、@PostMapping 等注解的方法
     3. 是否指定了正确的扫描路径
     ```
   - If interfaces found, proceed to Step 2

**Output**: List of Controller classes and total number of interfaces found.

#### Step 2: Extract Interface Information

**CRITICAL: For each interface, extract complete information including URL, method, parameters, and response.**

For each API interface found, extract:

1. **Basic Information**:
   - **Interface Name**: Method name or description from annotation
   - **Request Method**: GET, POST, PUT, DELETE, PATCH
   - **Request URL**: Full path including class-level and method-level mappings
   - **Controller Class**: Full class name with package
   - **Method Name**: Java/Kotlin method name

2. **Request Information**:
   - **Path Parameters**: Parameters in URL path (e.g., `/user/{id}`)
     - Parameter name, type, required flag, description
   - **Query Parameters**: Parameters in query string
     - Parameter name, type, required flag, default value, description
   - **Request Body** (for POST/PUT):
     - Body type (JSON, Form-data, etc.)
     - Field definitions: name, type, required flag, description
     - Nested object structures
   - **Request Headers**:
     - Common headers: Authorization, Shop-Id, Tenant-Id
     - Custom headers if any

3. **Response Information**:
   - **Response Type**: Return type of the method
   - **Response Structure**: 
     - Standard response wrapper (e.g., `R<T>`, `ApiResponse<T>`)
     - Data object structure
   - **Response Fields**: 
     - Field name, type, description
     - Nested object fields
   - **Response Examples**: Generate example JSON responses
   - **Error Responses**: Common error codes and messages

4. **Additional Information**:
   - **Description**: From `@ApiOperation`, `@Operation`, or method comments
   - **Tags**: From `@Api`, `@Tag` annotations
   - **Deprecated**: Check for `@Deprecated` annotation
   - **Security**: Authentication/authorization requirements

**Output**: Structured data for each interface with all extracted information.

#### Step 3: Generate Documentation

**CRITICAL: Generate documentation following the standard template format.**

1. **Select Template Language**:
   - Ask user for preferred language: Chinese or English
   - If not specified, detect from project context (code comments, package names, etc.)
   - Available templates:
     - Chinese: `templates/接口文档模板.md`
     - English: `templates/api-documentation-template-en.md`

2. **Load Template**:
   - Load the appropriate template based on language selection
   - Use it as the base structure

2. **Organize by Module**:
   - Group interfaces by Controller class or business module
   - Create sections for each module

3. **Generate Interface List Table**:
   - For Chinese template: Create "接口一览表" with columns:
     - 序号 (Sequence number)
     - 接口地址 (Interface URL)
     - 请求方式 (Request Method)
     - 说明 (Description)
     - 完成情况 (Status)
   - For English template: Create "API Interface List" with columns:
     - No. (Sequence number)
     - Interface URL
     - Method
     - Description
     - Status

4. **Generate Interface Definitions**:
   For each interface, generate:
   - **Interface Name**: Clear, descriptive name
   - **Interface Address**: Full URL with method
   - **Description**: 
     - Corresponding Controller class and method
     - Business functionality description
     - Business rules if any
   - **Request Section**:
     - Method and URL
     - Headers table
     - Path Parameters table
     - Query Parameters table
     - Request Body (if applicable) with field definitions
   - **Response Section**:
     - Response structure description
     - Response fields table
     - Response example (JSON)
     - Error response examples

5. **Add Standard Sections**:
   - For Chinese template:
     - **统一响应结构**: Standard response format
     - **分页响应格式**: Pagination response format
     - **错误码约定**: Error code conventions
     - **请求头规范**: Request header specifications
     - **注意事项**: Important notes
   - For English template:
     - **Standard Response Structure**: Standard response format
     - **Pagination Response Format**: Pagination response format
     - **Error Code Conventions**: Error code conventions
     - **Request Header Specifications**: Request header specifications
     - **Important Notes**: Important notes

6. **Format Documentation**:
   - Use proper Markdown formatting
   - Ensure tables are properly formatted
   - Include code blocks for JSON examples
   - Add proper headings hierarchy

**Output**: Complete API documentation in Markdown format.

#### Step 4: Save Documentation

**CRITICAL: Save documentation to the `./docs` directory in the current project.**

1. **Determine Output Path**:
   - Default: `./docs/api-documentation.md`
   - If multiple modules: `./docs/{module-name}-api-documentation.md`
   - Ask user if they want a custom filename

2. **Create Directory**:
   - Check if `./docs` directory exists
   - If not, create it automatically

3. **Save File**:
   - Write the generated documentation to the file
   - Use UTF-8 encoding
   - Ensure proper line endings

4. **Inform User**:
   - Tell user where the file was saved
   - Show the file path
   - Optionally display a preview of the documentation

**Output**: Documentation file saved to `./docs/api-documentation.md` (or custom path).

### Code Scanning Guidelines

#### Java/Spring Boot Projects

**Controller Identification**:
- Look for classes annotated with `@RestController` or `@Controller`
- Check for `@RequestMapping` at class level
- Common package patterns: `*.controller.*`, `*.web.*`, `*.api.*`

**Method Identification**:
- Methods annotated with:
  - `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, `@PatchMapping`
  - `@RequestMapping(method = RequestMethod.GET)` etc.

**Parameter Extraction**:
- `@PathVariable`: Path parameters
- `@RequestParam`: Query parameters
- `@RequestBody`: Request body
- `@RequestHeader`: Request headers
- Parameter types from method signature

**Response Extraction**:
- Return type from method signature
- `@ResponseBody` annotation
- Generic types (e.g., `R<T>`, `Page<T>`)
- Response entity structure

#### Kotlin/Spring Boot Projects

Similar to Java, but check for:
- Kotlin data classes for request/response
- Nullable types (`String?`, `Int?`)
- Kotlin-specific annotations

### Documentation Template Structure

The generated documentation follows this structure (available in both Chinese and English):

**Chinese Template** (`templates/接口文档模板.md`):
1. **文档概览** (Document Overview)
   - Version history table
   - Responsibility table

2. **接口一览表** (Interface List Table)
   - Summary table of all interfaces

3. **接口定义** (Interface Definitions)
   - Detailed definition for each interface
   - Request and Response sections
   - Field definitions and examples

4. **统一响应结构** (Standard Response Structure)
   - Standard response format
   - Pagination format
   - Error codes

5. **请求头规范** (Request Header Specifications)

6. **注意事项** (Important Notes)

**English Template** (`templates/api-documentation-template-en.md`):
1. **Document Overview**
   - Version history table
   - Responsibility table

2. **API Interface List**
   - Summary table of all interfaces

3. **Interface Definitions**
   - Detailed definition for each interface
   - Request and Response sections
   - Field definitions and examples

4. **Standard Response Structure**
   - Standard response format
   - Pagination format
   - Error codes

5. **Request Header Specifications**

6. **Important Notes**

**Template Selection**:
- Ask user for preferred language (Chinese/English)
- If not specified, detect from project context
- Both templates follow the same structure, only language differs

### Best Practices

1. **Complete Information**: Extract all available information from code, including annotations and comments
2. **Standard Format**: Follow the template structure strictly
3. **Clear Descriptions**: Use meaningful descriptions from code comments or annotations
4. **Examples**: Include realistic response examples
5. **Error Handling**: Document common error scenarios
6. **Grouping**: Organize interfaces by module or Controller class
7. **Validation**: Verify all extracted information is accurate

### Reference Documentation

- **Templates**:
  - `templates/接口文档模板.md` - Standard API documentation template (Chinese)
  - `templates/api-documentation-template-en.md` - Standard API documentation template (English)
- **Example**: `examples/scan-and-generate-example.md` - Complete workflow example showing how to scan and generate API documentation

## Keywords

**English keywords:**
api documentation, api docs, generate api documentation, create api docs, scan interfaces, document apis, rest api documentation, interface documentation, api doc generator, scan controllers, extract api information

**Chinese keywords (中文关键词):**
接口文档, API文档, 生成接口文档, 创建接口文档, 扫描接口, 接口文档生成, API文档生成, 接口文档生成器, 扫描Controller, 提取接口信息, 接口文档模板

**IMPORTANT**: All keywords must include "接口文档" (API documentation) or "API" to avoid false triggers. Generic terms like "生成文档" (generate documentation) without "接口" or "API" should NOT trigger this skill.
