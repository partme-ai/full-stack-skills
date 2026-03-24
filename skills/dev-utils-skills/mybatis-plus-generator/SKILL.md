---
name: mybatis-plus-generator
description: |
  Provides comprehensive guidance for generating MyBatis-Plus code including Entity, Mapper, Service, ServiceImpl, 
  Controller, DTO, VO, BO and other related objects from database tables. Use ONLY when the user explicitly 
  mentions MyBatis-Plus, mybatis-plus-generator, or wants to generate code using MyBatis-Plus framework. 
  This skill automatically generates standard CRUD methods and custom methods based on user requirements for 
  MyBatis-Plus projects. Supports MVC and DDD architectures, Java and Kotlin languages. Do NOT trigger for 
  generic code generation, JPA/Hibernate, or other ORM frameworks.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**CRITICAL: This skill should ONLY be triggered when the user explicitly mentions MyBatis-Plus or mybatis-plus-generator.**

**ALWAYS use this skill when the user mentions:**
- MyBatis-Plus code generation (explicitly mentions "MyBatis-Plus" or "mybatis-plus")
- Generating MyBatis-Plus code from database tables
- MyBatis-Plus generator or mybatis-plus-generator
- Creating MyBatis-Plus Entity, Mapper, Service, Controller code
- 生成 MyBatis-Plus 代码 (explicitly mentions "MyBatis-Plus")
- MyBatis-Plus 代码生成器 (MyBatis-Plus code generator)
- 使用 MyBatis-Plus 生成代码 (generate code using MyBatis-Plus)

**Trigger phrases include:**
- "生成 MyBatis-Plus 代码" (generate MyBatis-Plus code) - **must include "MyBatis-Plus"**
- "MyBatis-Plus 代码生成" (MyBatis-Plus code generation) - **must include "MyBatis-Plus"**
- "mybatis-plus-generator" (explicitly mentions the generator)
- "使用 MyBatis-Plus 根据表结构生成代码" (use MyBatis-Plus to generate code from table structure)
- "MyBatis-Plus 生成 Entity、Service、Controller" (MyBatis-Plus generate Entity, Service, Controller)
- "MyBatis-Plus 代码生成器" (MyBatis-Plus code generator)

**DO NOT trigger this skill for:**
- Generic code generation without mentioning MyBatis-Plus
- JPA/Hibernate code generation
- Other ORM frameworks (TypeORM, Sequelize, etc.)
- Generic CRUD operations without MyBatis-Plus context
- "根据表结构生成代码" without "MyBatis-Plus" (too generic)
- "生成 CRUD 代码" without "MyBatis-Plus" (too generic)
- "代码生成器" without "MyBatis-Plus" (too generic)

**Supported architectures:**
- Traditional MVC (Model-View-Controller)
- DDD (Domain-Driven Design)
- Layered Architecture
- Clean Architecture

**Supported languages:**
- Java
- Kotlin

**Supported component types:**
- Entity (实体类)
- Mapper (数据访问接口)
- Service (服务接口)
- ServiceImpl (服务实现类)
- Controller (控制器)
- DTO (Data Transfer Object)
- VO (Value Object / View Object)
- BO (Business Object)
- Model (数据模型)

## How to use this skill

**CRITICAL: This skill should ONLY be triggered when the user explicitly mentions MyBatis-Plus or mybatis-plus-generator. Do NOT trigger for generic code generation requests without MyBatis-Plus context.**

### Workflow Overview

This skill follows a systematic 8-step workflow:

1. **Collect Configuration** - Collect database information, global configuration, package configuration, strategy configuration
2. **Determine Architecture** - Ask user about architecture type (MVC, DDD, etc.) to determine which objects to generate
3. **Collect Requirements** - Ask user for functional requirements to analyze and determine methods to generate
4. **Determine Language** - Ask user about programming language (Java or Kotlin)
5. **Create Todo List** - Generate a detailed todo list with table names, object types, and method names
6. **Generate Code** - Generate code files with intelligent comments based on table structure and requirements
7. **Progress Updates** - Provide real-time progress updates during code generation
8. **Statistics** - Output statistics after generation completes

### Step-by-Step Process

#### Step 1: Collect Configuration

**CRITICAL: Before generating any code, you MUST collect the following configuration:**

1. **Database Information:**
   - Database type (MySQL, PostgreSQL, Oracle, etc.)
   - Database connection URL (or ask user to provide table structure)
   - Database name
   - Table names (one or multiple tables)
   - If user cannot provide database connection, ask for table structure (CREATE TABLE statement or table schema)

2. **Global Configuration:**
   - Author name
   - Output directory (default: `src/main/java`)
   - File override strategy (overwrite, skip, ask)
   - Enable Lombok (yes/no)
   - Enable API documentation (yes/no)
   - **API Documentation Type** (if enabled):
     - Swagger 2 (使用 `io.swagger.annotations.*`)
     - OpenAPI 3 (使用 `io.swagger.v3.oas.annotations.*`)
   - Enable validation annotations (yes/no)

3. **Package Configuration:**
   - Parent package name (e.g., `com.example.app`)
   - Entity package (default: `entity`)
   - Mapper package (default: `mapper`)
   - Service package (default: `service`)
   - ServiceImpl package (default: `service.impl`)
   - Controller package (default: `controller`)
   - DTO package (default: `dto`)
   - VO package (default: `vo`)
   - BO package (default: `bo`)

4. **Strategy Configuration:**
   - Naming strategy (camelCase, PascalCase, etc.)
   - Table prefix removal (yes/no, prefix name)
   - Field naming strategy
   - Primary key strategy (AUTO, UUID, etc.)

**IMPORTANT: API Documentation Type Selection:**

When user enables API documentation, you MUST ask:

```
请选择 API 文档类型：
- [ ] Swagger 2
  - 使用注解：@ApiModel, @ApiModelProperty, @Api, @ApiOperation
  - 依赖：springfox-swagger2, springfox-swagger-ui
  - 适用于：Spring Boot 2.x 项目
- [ ] OpenAPI 3
  - 使用注解：@Schema, @Tag, @Operation, @Parameter
  - 依赖：springdoc-openapi-ui
  - 适用于：Spring Boot 2.2+ 和 Spring Boot 3.x 项目
```

**Wait for user confirmation** before proceeding.

**Output**: A configuration summary showing all collected information, including API documentation type.

#### Step 2: Determine Architecture

**CRITICAL: You MUST ask the user about the architecture type to determine which objects to generate.**

Present architecture options:

```
请选择项目架构类型：
- [ ] 传统 MVC (Model-View-Controller)
  - 生成：Entity, Mapper, Service, ServiceImpl, Controller
- [ ] DDD (领域驱动设计)
  - 生成：Entity, Mapper, Service, ServiceImpl, Controller, DTO, VO, BO
- [ ] 分层架构 (Layered Architecture)
  - 生成：Entity, Mapper, Service, ServiceImpl, Controller
- [ ] 整洁架构 (Clean Architecture)
  - 生成：Entity, Repository, UseCase, Controller, DTO
- [ ] 自定义架构
  - 请指定需要生成的对象类型
```

**Wait for user confirmation** before proceeding.

**IMPORTANT: Directory Mapping Based on Architecture**

After determining the architecture type, you MUST identify the correct output directories for each generated object.

**CRITICAL Steps:**

1. **Ask user for base package path** (e.g., `com.example.order`)
2. **Use architecture directory mapping** to determine correct paths:
   - **Quick Reference**: See `reference/architecture-directory-quick-reference.md` for lookup table
   - **Detailed Guide**: See `reference/architecture-directory-mapping-guide.md` for complete mapping rules
3. **Verify directory exists** or create it if needed
4. **Generate files** in the correct location

**Common Path Examples:**

For `user` table with base package `com.example.order`:
- **MVC**: Entity → `com/example/order/entity/User.java`, Controller → `com/example/order/controller/UserController.java`
- **DDD**: Entity → `com/example/order/domain/model/aggregate/user/User.java`, Controller → `com/example/order/interfaces/web/controller/UserController.java`
- **Hexagonal**: Entity → `com/example/order/domain/model/entity/User.java`, Controller → `com/example/order/infrastructure/adapter/inbound/web/controller/UserController.java`
- **Clean**: Entity → `com/example/order/domain/entity/User.java`, Controller → `com/example/order/infrastructure/web/controller/UserController.java`
- **COLA**: Entity → `com/example/order/domain/model/entity/User.java`, Controller → `com/example/order/adapter/web/controller/UserController.java`

**CRITICAL**: Always confirm the exact directory structure with the user if the project structure is unclear. Ask: "请确认项目的目录结构，以便我将生成的代码放在正确的位置。"

#### Step 3: Collect Requirements

**CRITICAL: Ask user for functional requirements to understand what methods need to be generated.**

Ask the user:

```
请描述此次生成代码的功能需求：

例如：
- 用户管理：需要根据邮箱查询用户、根据用户名查询用户、用户登录验证
- 订单管理：需要订单统计、订单分页查询、订单状态更新
- 商品管理：需要商品搜索、商品分类查询、库存管理

请详细描述每个表需要哪些功能，我会根据需求自动分析需要生成的方法。
```

**After user provides requirements:**

1. **Analyze requirements** to identify:
   - Standard CRUD methods (create, read, update, delete)
   - Custom query methods (findByEmail, findByUsername, etc.)
   - Custom business methods (statistics, aggregation, etc.)
   - Custom update methods (updateStatus, updatePassword, etc.)

2. **For each table, identify:**
   - Standard methods needed
   - Custom methods needed based on requirements
   - Method parameters and return types
   - Business logic hints (for method skeletons)

**Output**: A requirements analysis showing:
- Standard methods for each table
- Custom methods for each table
- Method signatures (parameters and return types)

#### Step 4: Determine Language

**CRITICAL: Ask user about programming language.**

```
请选择编程语言：
- [ ] Java
- [ ] Kotlin
```

**Wait for user confirmation** before proceeding.

**Note**: Templates in `templates/` directory support both Java and Kotlin. Use appropriate templates based on user's choice.

#### Step 5: Create Todo List

**CRITICAL: After collecting all information, create a detailed todo list.**

For each table, generate a structured todo list:

```markdown
## Todo List: MyBatis-Plus Code Generation

### Table: user

#### Entity 层
- [ ] User.java - 实体类
  - [ ] 类注释
  - [ ] 字段定义（id, username, email, password, status, createTime, updateTime）
  - [ ] 字段注释

#### Mapper 层
- [ ] UserMapper.java - 数据访问接口
  - [ ] 类注释
  - [ ] 基础 CRUD 方法（继承 BaseMapper）

#### Service 层
- [ ] UserService.java - 服务接口
  - [ ] 类注释
  - [ ] saveUser() - 保存用户
  - [ ] findById() - 根据ID查询
  - [ ] updateUser() - 更新用户
  - [ ] deleteById() - 删除用户
  - [ ] findByEmail() - 根据邮箱查询（自定义方法）
  - [ ] findByUsername() - 根据用户名查询（自定义方法）

#### ServiceImpl 层
- [ ] UserServiceImpl.java - 服务实现类
  - [ ] 类注释
  - [ ] 实现所有 Service 接口方法
  - [ ] 方法注释和实现骨架

#### Controller 层
- [ ] UserController.java - 控制器
  - [ ] 类注释
  - [ ] createUser() - 创建用户
  - [ ] getUserById() - 查询用户
  - [ ] updateUser() - 更新用户
  - [ ] deleteUser() - 删除用户
  - [ ] getUserByEmail() - 根据邮箱查询（自定义接口）

#### DTO 层（如果架构需要）
- [ ] UserCreateDTO.java - 创建用户DTO
- [ ] UserUpdateDTO.java - 更新用户DTO
- [ ] UserQueryDTO.java - 查询用户DTO

#### VO 层（如果架构需要）
- [ ] UserVO.java - 用户视图对象

### Table: order
...
```

**Important**: 
- Organize by table
- List all objects that need to be generated
- Include all methods (standard + custom)
- Use checkboxes for tracking progress

#### Step 6: Generate Code

**CRITICAL: Generate code files with intelligent comments based on table structure and requirements.**

**Order of generation:**
1. **Entity** - First (base for all other objects)
2. **Mapper** - Second (data access layer)
3. **Service** - Third (business interface)
4. **ServiceImpl** - Fourth (business implementation)
5. **Controller** - Fifth (API layer)
6. **DTO/VO/BO** - Sixth (if needed by architecture)

**For each object:**

1. **Load appropriate template** from `templates/` directory based on object type and language
2. **Analyze table structure**: Read columns, types, constraints, primary keys, foreign keys, relationships
3. **Generate intelligent comments**: Based on business context, not just technical names
   - Class comments: Explain purpose, list main fields
   - Method comments: Explain business logic, include all parameters and return types
   - Field comments: Explain business meaning, not just column names
4. **Generate code**: Replace template variables, add annotations, generate method skeletons
5. **For custom methods**: Generate signatures, add business logic comments, add TODO hints
6. **Determine output directory**: Use architecture directory mapping (see Step 2)
7. **Save files** to correct location based on architecture and package configuration

**After generating each object:**
- Update the todo list: mark completed items with `[x]`
- Show progress to the user
- Continue to the next object

**Code Generation Standards**: See `reference/code-generation-standards.md` for detailed requirements on comments, templates, and code quality.

#### Step 7: Progress Updates

**CRITICAL: Provide real-time progress updates during code generation.**

**Update progress after:**
- Each table starts processing
- Each object is generated
- Each method is added
- Each table completes

**Progress Format**: See `reference/progress-and-statistics-formats.md` for detailed progress update format and examples.

#### Step 8: Statistics

**CRITICAL: After all code generation completes, output comprehensive statistics.**

**Statistics Format**: See `reference/progress-and-statistics-formats.md` for detailed statistics format including:
- Overall statistics (tables, objects, methods, files, lines)
- Per-table statistics
- Per-type statistics
- File locations
- Code quality checklist

### Code Generation Standards

**IMPORTANT: Generated code must include intelligent, context-aware comments, not just template placeholders.**

**Key Requirements:**
1. **Class Comments**: Explain purpose based on business context, include table mapping, list main fields
2. **Method Comments**: Explain business logic, include all parameters with types, return value with type, exceptions
3. **Field Comments**: Explain business meaning, include data type and constraints, not just column names

**Detailed Standards**: See `reference/code-generation-standards.md` for:
- Complete comment format requirements
- Template usage guidelines
- Template variables reference
- Swagger annotation selection
- Custom method generation standards
- Code quality requirements

### Best Practices

1. **Intelligent Comments**: Generate comments based on table structure analysis and business requirements, not just template placeholders
2. **Context Awareness**: Understand table relationships and business context to generate meaningful comments
3. **Method Analysis**: Analyze user requirements to determine what methods are needed
4. **Progress Tracking**: Always update todo list and show progress
5. **Code Quality**: Generate production-ready code with proper annotations and validation
6. **Template Enhancement**: Use templates as base, but enhance with intelligent additions
7. **Language Support**: Support both Java and Kotlin with appropriate templates

### Reference Documentation

**CRITICAL: Use these reference documents for detailed guidance:**

#### Architecture & Directory Mapping
- `reference/architecture-directory-mapping-guide.md` - **Complete directory mapping guide for all architectures** (CRITICAL)
- `reference/architecture-directory-quick-reference.md` - Quick lookup table for directory mappings

#### Code Generation Standards
- `reference/code-generation-standards.md` - Detailed comment standards, template usage, and code quality requirements
- `reference/template-variables.md` - Complete list of template variables
- `reference/swagger-annotations-guide.md` - Swagger 2 vs OpenAPI 3 annotation comparison

#### Progress & Statistics
- `reference/progress-and-statistics-formats.md` - Progress update and statistics output formats

#### MyBatis-Plus Reference
- `reference/mybatis-plus-generator-guide.md` - MyBatis-Plus Generator usage guide

### Examples

See the `examples/` directory for complete examples:
- `examples/mvc-architecture-example.md` - MVC architecture generation example
- `examples/ddd-architecture-example.md` - DDD architecture generation example
- `examples/full-workflow-example.md` - Complete workflow example
- `examples/architecture-directory-mapping.md` - Directory mapping examples for different architectures
- `examples/swagger-annotations-example.md` - Swagger 2 vs OpenAPI 3 annotation examples

### Templates

Templates are located in `templates/` directory, using **FreeMarker** syntax (`.ftl` files), strictly following [MyBatis-Plus official templates](https://github.com/baomidou/mybatis-plus/tree/3.0/mybatis-plus-generator/src/main/resources/templates).

#### Standard Templates (MVC Architecture)

**Java Templates:**
- `entity.java.ftl` - Entity class template
- `mapper.java.ftl` - Mapper interface template
- `service.java.ftl` - Service interface template
- `serviceImpl.java.ftl` - Service implementation template
- `controller.java.ftl` - Controller template
- `dto.java.ftl` - DTO template
- `vo.java.ftl` - VO template
- `bo.java.ftl` - BO template

**Kotlin Templates:**
- `entity.kt.ftl` - Entity data class template
- `mapper.kt.ftl` - Mapper interface template
- `service.kt.ftl` - Service interface template
- `serviceImpl.kt.ftl` - Service implementation template
- `controller.kt.ftl` - Controller template
- `dto.kt.ftl` - DTO template
- `vo.kt.ftl` - VO template
- `bo.kt.ftl` - BO template

#### DDD Architecture Templates

All DDD templates are located in `templates/` root directory, supporting both Java and Kotlin:

**Domain Layer:**
- `aggregate-root.java.ftl` / `aggregate-root.kt.ftl` - Aggregate root template
- `repository.java.ftl` / `repository.kt.ftl` - Repository interface template (domain layer)
- `domain-service.java.ftl` / `domain-service.kt.ftl` - Domain service template
- `value-object.java.ftl` / `value-object.kt.ftl` - Value object template
- `domain-event.java.ftl` / `domain-event.kt.ftl` - Domain event template

**Application Layer:**
- `application-service.java.ftl` / `application-service.kt.ftl` - Application service template

**Interface Layer:**
- `assembler.java.ftl` / `assembler.kt.ftl` - DTO assembler template

**Template Features:**
- Support for Swagger 2 and OpenAPI 3 annotations
- Intelligent comments based on table structure
- Custom method generation support
- Kotlin-specific features (data classes, null safety, etc.)
- DDD-specific patterns (aggregate root, value objects, domain events)
- FreeMarker syntax for template engine

**Reference**: See MyBatis-Plus official templates at:
- https://github.com/baomidou/mybatis-plus/tree/3.0/mybatis-plus-generator/src/main/resources/templates

## Keywords

**English keywords:**
mybatis-plus, mybatis-plus-generator, mybatis-plus code generator, mybatis-plus code generation, generate mybatis-plus code, mybatis-plus entity generator, mybatis-plus mapper generator, mybatis-plus service generator, mybatis-plus controller generator, mybatis-plus crud generation, mybatis-plus from table, mybatis-plus code from database

**Chinese keywords (中文关键词):**
MyBatis-Plus, mybatis-plus-generator, MyBatis-Plus 代码生成器, MyBatis-Plus 代码生成, 生成 MyBatis-Plus 代码, MyBatis-Plus 实体类生成, MyBatis-Plus Mapper 生成, MyBatis-Plus Service 生成, MyBatis-Plus Controller 生成, MyBatis-Plus CRUD 生成, MyBatis-Plus 根据表生成代码, MyBatis-Plus 数据库转代码, MyBatis-Plus 表转 Java, 使用 MyBatis-Plus 生成代码

**IMPORTANT**: All keywords must include "MyBatis-Plus" or "mybatis-plus" to avoid false triggers. Generic terms like "代码生成器" (code generator) or "根据表生成代码" (generate code from table) without "MyBatis-Plus" should NOT trigger this skill.
