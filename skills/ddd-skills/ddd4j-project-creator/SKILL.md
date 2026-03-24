---
name: ddd4j-project-creator
description: |
  A comprehensive skill for creating new ddd4j (Domain-Driven Design for Java) projects based on ddd4j-boot framework. 
  Use ONLY when the user explicitly mentions creating a ddd4j project, initializing ddd4j project, or setting up 
  ddd4j-boot project. Supports three project types: single-module monolith, multi-module monolith, and microservices. 
  Generates project scaffolding based on ddd4j-boot architecture with DDD, Hexagonal Architecture, Clean Architecture, 
  and COLA V5 patterns. Do NOT trigger for generic DDD projects, JPA/Hibernate projects, or other ORM frameworks 
  without explicit ddd4j mention.
license: Complete terms in LICENSE.txt
---

# DDD4j Project Creator

## When to use this skill

**CRITICAL: This skill should ONLY be triggered when the user explicitly mentions creating a ddd4j project, initializing ddd4j project, or setting up ddd4j-boot project.**

**ALWAYS use this skill when the user mentions:**
- Creating a ddd4j project (explicitly mentions "ddd4j")
- Initializing ddd4j-boot project
- Setting up ddd4j project structure
- Creating ddd4j project scaffolding
- 创建 ddd4j 项目 (explicitly mentions "ddd4j")
- 初始化 ddd4j 项目 (initialize ddd4j project)
- ddd4j-boot 项目创建 (create ddd4j-boot project)

**Trigger phrases include:**
- "创建 ddd4j 项目" (create ddd4j project) - **must include "ddd4j"**
- "初始化 ddd4j 项目" (initialize ddd4j project) - **must include "ddd4j"**
- "创建 ddd4j-boot 项目" (create ddd4j-boot project) - **must include "ddd4j"**
- "使用 ddd4j 创建项目" (create project using ddd4j)
- "ddd4j 项目脚手架" (ddd4j project scaffolding)

**DO NOT trigger this skill for:**
- Generic DDD projects without mentioning ddd4j
- JPA/Hibernate projects
- Other ORM frameworks
- Generic project initialization without ddd4j context
- "创建 DDD 项目" without "ddd4j" (too generic)
- "初始化项目" without "ddd4j" (too generic)

## About DDD4j Boot

**DDD4j Boot** is a Java microservice development scaffold based on **Domain-Driven Design (DDD)** principles. It is built with Spring Boot 3.5.x and uses lightweight [ddd-4-java](https://github.com/fuinorg/ddd-4-java) and [cqrs-4-java](https://github.com/fuinorg/cqrs-4-java) libraries to implement Domain-Driven Design, Command Query Responsibility Segregation (CQRS), and Event Sourcing.

### Core Design Principles

- **Domain-Driven Design (DDD)**: Strategic design through bounded contexts, tactical design with entities, value objects, aggregates, domain services, repositories, and domain events
- **Command Query Responsibility Segregation (CQRS)**: Separation of read and write models, independent optimization
- **Event Sourcing**: State changes recorded as event sequences, supporting complete history and state reconstruction
- **Diamond Architecture (COLA)**: Adapter → Application → Domain ← Infrastructure four-layer architecture

### Key Features

- Complete DDD layered architecture supporting COLA V5 pattern
- Lightweight DDD implementation based on ddd-4-java and cqrs-4-java
- Technology stack integration: Spring Boot 3.5.x, MyBatis Plus, Jackson, Guava, Swagger, SaToken
- Dual stack support: WebMVC (traditional Servlet) and WebFlux (reactive)
- Domain model base capabilities: BaseEntity, BaseRepository, BaseService
- Domain event support with built-in event publishing mechanism
- Anti-Corruption Layer (ACL) for external service integration
- Unified exception handling mechanism

## Project Types Supported

### 1. Single-Module Monolith (单体单模块)
**适用场景**: 中小型应用，单个业务领域，团队规模 5-15 人

**特点**:
- 单一 Maven 模块
- 所有层（interfaces, application, domain, infrastructure）在同一模块内
- 适合快速开发和部署

### 2. Multi-Module Monolith (单体多模块)
**适用场景**: 中大型应用，多个业务域，团队规模 15-50 人

**特点**:
- 多个 Maven 模块，按业务域划分
- 每个业务域包含完整的 DDD 四层架构
- 共享 common 模块
- 统一 BOM 和依赖管理

### 3. Microservices (单体微服务)
**适用场景**: 大型电商平台，多个业务域，团队规模 50+ 人

**特点**:
- 每个服务独立部署
- 服务间通过 RPC 和消息队列通信
- 每个服务内部按 DDD 四层架构组织
- 独立的数据库和配置

## How to use this skill

**CRITICAL: This skill should ONLY be triggered when the user explicitly mentions creating a ddd4j project. Do NOT trigger for generic DDD project creation requests without ddd4j context.**

### For New DDD4j Project Creation

1. **Identify the project type** from user requirements:
   - Single-module monolith → `single-module`
   - Multi-module monolith → `multi-module`
   - Microservices → `microservices`

2. **Load the appropriate example** from the `examples/` directory:
   - `examples/single-module.md` - Single-module monolith structure
   - `examples/multi-module.md` - Multi-module monolith structure
   - `examples/microservices.md` - Microservices structure
   - `examples/architecture-patterns.md` - DDD, Hexagonal, Clean, COLA V5 patterns

3. **Collect project information**:
   - `groupId`: Maven group ID (e.g., `com.github.hiwepy` or `io.ddd4j.base`)
   - `artifactId`: Maven artifact ID (e.g., `ddd4j-douyin` or `my-ddd4j-service`)
   - `version`: Project version (e.g., `1.0.0-SNAPSHOT`)
   - `parentVersion`: Parent POM version (e.g., `2023.0.x.20251205-SNAPSHOT` or reference to `ddd4j-boot-parent`)
   - `packageBase`: Base package name (e.g., `io.ddd4j.douyin` or `com.example.service`)
   - `modules`: List of business modules (for multi-module/microservices)
   - `architecture`: Architecture pattern (DDD Classic, Hexagonal, Clean, COLA V5)
   - `ddd4jBootVersion`: DDD4j Boot version (if using ddd4j-boot-bom)

4. **Generate project structure**:
   - Create directory structure based on selected type
   - Generate `pom.xml` files (parent and modules)
   - Create `package-info.java` files for each module
   - Generate `.gitignore`, `LICENSE`, `mvnw`, `mvnw.cmd`
   - Create basic directory structure with `src/main/java` and `src/test/java`

5. **Save to project directory**:
   - **Default location**: Save directly to the command execution directory (same level as the command)
   - **Directory creation**: Automatically create the project directory structure if it doesn't exist
   - **File naming**: Use descriptive names based on project type and module names

### For Existing Project Validation

1. **Analyze project structure**:
   - Scan project directory for Maven modules
   - Identify layer structure (interfaces, application, domain, infrastructure)
   - Check package naming conventions
   - Verify directory organization

2. **Identify project type**:
   - **Single-module**: Single `pom.xml` at root, all layers in one module
   - **Multi-module**: Parent `pom.xml` with multiple modules, each module has complete layers
   - **Microservices**: Multiple services, each with independent structure

3. **Validate against standards**:
   - Check DDD layer compliance
   - Verify dependency direction (interfaces → application → domain ← infrastructure)
   - Validate package naming (`{basePackage}.{module}.{layer}`)
   - Check for required directories (`src/main/java`, `src/test/java`)
   - Verify `package-info.java` files exist

4. **Generate validation report**:
   - List identified issues
   - Provide recommendations
   - Suggest fixes for non-compliant structures

## Output Format and File Saving

When generating a project structure, follow this response structure:

1. **Save the files first**: Create the project structure directly in the command execution directory
   - The project will be created at the same level as where the command is executed
   - Generate all required files and directories (pom.xml, src/, etc.)
   - Use the artifactId as the project root directory name

2. **Inform the user**: Tell them where the files were saved

3. **Display the structure**: Show the generated directory structure in a code block

**Example Response Structure**:
- First line: "I've created the DDD project structure and saved it to `./{artifactId}/` in the current directory."
- Then show the structure wrapped in a code block:
  - Start with: three backticks + `text` + newline
  - Then the directory structure
  - End with: three backticks + newline

**Critical Requirements**:
- Always save project files directly to the command execution directory (same level)
- Use artifactId as the project root directory name
- Create the directory structure automatically if it doesn't exist
- Generate complete project structure with all required files
- Follow Maven and DDD conventions strictly

## Project Structure Standards

### Package Naming Convention

For multi-module projects:
```
{basePackage}.{moduleName}.{layerName}
```

Examples:
- `io.ddd4j.douyin.api.domain` - API module, domain layer
- `io.ddd4j.douyin.api.application` - API module, application layer
- `io.ddd4j.douyin.api.interfaces` - API module, interfaces layer
- `io.ddd4j.douyin.api.infrastructure` - API module, infrastructure layer

### Required Files

Every module must have:
- `pom.xml` - Maven configuration
- `src/main/java/{package}/package-info.java` - Package documentation
- `src/test/java/` - Test directory structure
- `.gitignore` - Git ignore rules (at root)
- `LICENSE` - License file (at root)
- `mvnw`, `mvnw.cmd` - Maven wrapper (at root)

### Layer Dependencies

**Correct dependency direction**:
```
interfaces → application → domain ← infrastructure
```

**Rules**:
- Domain layer must not depend on any other layer
- Infrastructure layer implements domain layer interfaces
- Application layer depends on domain layer
- Interfaces layer depends on application layer

## Architecture Patterns

The skill supports four architecture patterns:

1. **DDD Classic Layered Architecture** (DDD 经典分层架构)
   - Layers: interfaces, application, domain, infrastructure
   - Reference: `docs/1、DDD 经典分层架构目录结构.md` and `examples/architecture-patterns.md#ddd-classic`

2. **Hexagonal Architecture** (六边形架构)
   - Ports and Adapters pattern
   - Reference: `docs/2、六边形架构详细目录结构参考.md` and `examples/architecture-patterns.md#hexagonal`

3. **Clean Architecture** (整洁架构)
   - Entities, Use Cases, Interface Adapters
   - Reference: `docs/3、整洁架构详细目录结构参考.md` and `examples/architecture-patterns.md#clean`

4. **COLA V5** (菱形架构)
   - Adapter → App → Domain ← Infrastructure
   - Reference: `docs/4、COLA V5 架构详细目录结构参考.md` and `examples/architecture-patterns.md#cola-v5`

## Validation Rules

When checking existing projects, validate:

1. **Structure Compliance**:
   - ✓ Correct layer organization
   - ✓ Proper module separation
   - ✓ Package naming conventions

2. **Dependency Rules**:
   - ✓ Domain layer has no external dependencies
   - ✓ Infrastructure implements domain interfaces
   - ✓ Correct dependency direction

3. **File Organization**:
   - ✓ Required directories exist
   - ✓ `package-info.java` files present
   - ✓ Maven configuration correct

4. **Naming Conventions**:
   - ✓ Package names follow convention
   - ✓ Module names are descriptive
   - ✓ Layer names are standard

## Examples

See the `examples/` directory for:
- `single-module.md` - Complete single-module monolith example
- `multi-module.md` - Complete multi-module monolith example (based on ddd4j-douyin structure)
- `microservices.md` - Complete microservices example
- `architecture-patterns.md` - All four architecture patterns with detailed structures

## Keywords

**English keywords:**
ddd4j, ddd4j-boot, ddd4j project, create ddd4j project, initialize ddd4j project, ddd4j project creator, ddd4j project scaffolding, ddd4j-boot project, ddd4j project structure, ddd4j-boot initialization, ddd4j microservice, ddd4j monolith

**Chinese keywords (中文关键词):**
ddd4j, ddd4j-boot, ddd4j 项目, 创建 ddd4j 项目, 初始化 ddd4j 项目, ddd4j 项目创建, ddd4j 项目脚手架, ddd4j-boot 项目, ddd4j 项目结构, ddd4j-boot 初始化, ddd4j 微服务, ddd4j 单体应用

**IMPORTANT**: All keywords must include "ddd4j" to avoid false triggers. Generic terms like "DDD 项目" (DDD project) or "创建项目" (create project) without "ddd4j" should NOT trigger this skill.
