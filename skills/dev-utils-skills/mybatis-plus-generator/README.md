# MyBatis-Plus Generator Skill

## 概述

这是一个基于 Agent Skills 规范的 MyBatis-Plus 代码生成技能，可以根据数据库表结构自动生成完整的 CRUD 代码，包括 Entity、Mapper、Service、ServiceImpl、Controller、DTO、VO、BO 等对象。

**重要提示**：本技能仅在用户明确提到 **MyBatis-Plus** 或 **mybatis-plus-generator** 时触发，避免与其他代码生成工具产生冲突。

## 功能特点

1. **智能代码生成**：根据表结构和业务需求生成代码，包含智能注释而非简单模板填充
2. **多架构支持**：支持 MVC、DDD（领域驱动设计）、分层架构、整洁架构、六边形架构、COLA V5 等
3. **多语言支持**：支持 Java 和 Kotlin，使用对应的模板文件
4. **智能注释**：生成符合 Java 编程规范的注释，基于业务上下文理解
5. **自定义方法**：根据业务需求自动分析并生成自定义方法
6. **API 文档支持**：支持 Swagger 2 和 OpenAPI 3 注解
7. **DDD 模式支持**：支持聚合根、仓储、领域服务、值对象、领域事件等 DDD 模式
8. **进度跟踪**：实时输出生成进度
9. **统计报告**：生成完成后输出详细统计信息

## 文件结构

```
mybatis-plus-generator/
├── SKILL.md                              # 主技能文档（Agent Skills 规范）
├── LICENSE.txt                           # Apache 2.0 许可证
├── README.md                             # 本文件
├── examples/                             # 示例目录
│   ├── full-workflow-example.md         # 完整工作流程示例
│   ├── mvc-architecture-example.md      # MVC 架构示例
│   ├── ddd-architecture-example.md      # DDD 架构示例
│   ├── architecture-directory-mapping.md # 架构目录映射示例
│   └── swagger-annotations-example.md   # Swagger 注解示例
├── reference/                            # 参考文档目录
│   ├── mybatis-plus-generator-guide.md  # MyBatis-Plus Generator 指南
│   ├── template-variables.md            # 模板变量参考
│   ├── architecture-directory-mapping-guide.md # 架构目录映射详细指南
│   ├── architecture-directory-quick-reference.md # 架构目录映射快速参考
│   ├── code-generation-standards.md     # 代码生成标准
│   ├── progress-and-statistics-formats.md # 进度和统计格式
│   └── swagger-annotations-guide.md     # Swagger 注解指南
└── templates/                            # 代码模板目录（FreeMarker 语法）
    ├── entity.java.ftl / entity.kt.ftl  # Entity 实体类模板
    ├── mapper.java.ftl / mapper.kt.ftl  # Mapper 接口模板
    ├── service.java.ftl / service.kt.ftl # Service 接口模板
    ├── serviceImpl.java.ftl / serviceImpl.kt.ftl # ServiceImpl 实现类模板
    ├── controller.java.ftl / controller.kt.ftl # Controller 控制器模板
    ├── dto.java.ftl / dto.kt.ftl         # DTO 数据传输对象模板
    ├── vo.java.ftl / vo.kt.ftl          # VO 视图对象模板
    ├── bo.java.ftl / bo.kt.ftl          # BO 业务对象模板
    ├── repository.java.ftl / repository.kt.ftl # DDD Repository 接口模板
    ├── aggregate-root.java.ftl / aggregate-root.kt.ftl # DDD 聚合根模板
    ├── domain-service.java.ftl / domain-service.kt.ftl # DDD 领域服务模板
    ├── value-object.java.ftl / value-object.kt.ftl # DDD 值对象模板
    ├── domain-event.java.ftl / domain-event.kt.ftl # DDD 领域事件模板
    ├── application-service.java.ftl / application-service.kt.ftl # DDD 应用服务模板
    └── assembler.java.ftl / assembler.kt.ftl # DDD 装配器模板
```

## 工作流程

技能遵循 8 步系统化工作流程：

1. **收集配置**：数据库信息、全局配置、包配置、策略配置、API 文档类型（Swagger 2 / OpenAPI 3）
2. **确定架构**：MVC、DDD、分层架构、整洁架构、六边形架构、COLA V5 等，并确定目录映射
3. **收集需求**：功能需求分析，自动识别标准方法和自定义方法
4. **确定语言**：Java 或 Kotlin，使用对应的模板文件
5. **创建 Todo**：详细的生成计划，包含表名、对象类型、方法名
6. **生成代码**：使用 FreeMarker 模板生成代码，包含智能注释
7. **进度更新**：实时输出生成进度，更新 Todo 清单
8. **统计信息**：生成完成后的详细统计报告

## 使用方式

**重要提示**：本技能仅在用户明确提到 **MyBatis-Plus** 或 **mybatis-plus-generator** 时触发。

### 触发短语示例

- ✅ "生成 MyBatis-Plus 代码"
- ✅ "使用 MyBatis-Plus 根据表结构生成代码"
- ✅ "MyBatis-Plus 代码生成器"
- ✅ "mybatis-plus-generator"
- ❌ "根据表结构生成代码"（未明确提到 MyBatis-Plus，不会触发）
- ❌ "生成 CRUD 代码"（未明确提到 MyBatis-Plus，不会触发）

### 使用流程

当用户明确提到 MyBatis-Plus 时，技能会自动：

1. **收集配置信息**：数据库连接、表名、包名、作者等
2. **确定架构类型**：MVC、DDD 等，并确定正确的目录结构
3. **分析业务需求**：识别标准 CRUD 方法和自定义业务方法
4. **选择编程语言**：Java 或 Kotlin
5. **生成代码**：使用对应的模板文件生成代码
6. **提供进度更新**：实时显示生成进度
7. **输出统计信息**：生成完成后的详细报告

## 模板说明

### 模板引擎

所有模板文件使用 **FreeMarker** 模板语法（`.ftl` 文件），严格遵循 [MyBatis-Plus 官方模板](https://github.com/baomidou/mybatis-plus/tree/3.0/mybatis-plus-generator/src/main/resources/templates)。

### 模板语法

FreeMarker 模板支持：
- 变量替换（`${variable}`）
- 条件判断（`<#if>`）
- 循环遍历（`<#list>`）
- 字符串操作（`?substring`, `?lower_case` 等）

### 模板分类

#### 标准模板（MVC 架构）

- **Java 模板**：`entity.java.ftl`, `mapper.java.ftl`, `service.java.ftl`, `serviceImpl.java.ftl`, `controller.java.ftl`, `dto.java.ftl`, `vo.java.ftl`, `bo.java.ftl`
- **Kotlin 模板**：`entity.kt.ftl`, `mapper.kt.ftl`, `service.kt.ftl`, `serviceImpl.kt.ftl`, `controller.kt.ftl`, `dto.kt.ftl`, `vo.kt.ftl`, `bo.kt.ftl`

#### DDD 架构模板

- **领域层**：`aggregate-root.*.ftl`, `repository.*.ftl`, `domain-service.*.ftl`, `value-object.*.ftl`, `domain-event.*.ftl`
- **应用层**：`application-service.*.ftl`
- **接口层**：`assembler.*.ftl`

### 模板特性

- ✅ 支持 Swagger 2 和 OpenAPI 3 注解（根据配置自动选择）
- ✅ 智能注释生成（基于表结构和业务上下文）
- ✅ 自定义方法支持
- ✅ Kotlin 特性支持（data class、null safety、companion object 等）
- ✅ DDD 模式支持（聚合根、值对象、领域事件等）

详细模板变量说明请参考 `reference/template-variables.md`。

## 注释规范

生成的代码注释遵循严格的标准：

### JavaDoc 规范

- **类注释**：包含 `<p>` 标签的描述，说明类的业务用途，列出主要字段
- **方法注释**：包含 `<p>` 标签的描述，说明业务逻辑，明确参数类型和返回值类型
- **字段注释**：说明业务含义，包含数据类型和约束信息

### 注释特点

- ✅ **智能理解**：基于表结构和业务上下文生成注释，而非简单复制字段名
- ✅ **符合规范**：遵循 Java 编程规范，使用 `<p>` 标签
- ✅ **类型明确**：`@param`、`@return`、`@exception` 明确声明类型
- ✅ **业务导向**：注释说明业务含义，而非技术实现细节

详细注释规范请参考：
- `reference/code-generation-standards.md` - 代码生成标准
- `java-code-comments` 技能 - Java 代码注释技能

## 架构支持

### MVC 架构

生成标准的 MVC 分层代码：
- Entity（实体类）
- Mapper（数据访问层）
- Service / ServiceImpl（业务逻辑层）
- Controller（控制器层）
- DTO / VO / BO（数据传输对象）

### DDD 架构

支持完整的 DDD 模式：
- **聚合根**（Aggregate Root）：领域对象的核心
- **仓储**（Repository）：领域层的持久化接口
- **领域服务**（Domain Service）：跨聚合的业务逻辑
- **值对象**（Value Object）：不可变的值对象
- **领域事件**（Domain Event）：领域事件定义
- **应用服务**（Application Service）：应用层编排
- **装配器**（Assembler）：DTO 与领域对象转换

### 目录映射

不同架构模式有不同的目录结构，技能会根据架构类型自动确定正确的目录位置。详细说明请参考：
- `reference/architecture-directory-mapping-guide.md` - 完整目录映射指南
- `reference/architecture-directory-quick-reference.md` - 快速参考表
- `examples/architecture-directory-mapping.md` - 目录映射示例

## API 文档支持

### Swagger 2

- 使用注解：`@ApiModel`, `@ApiModelProperty`, `@Api`, `@ApiOperation`, `@ApiParam`
- 依赖：`springfox-swagger2`, `springfox-swagger-ui`
- 适用于：Spring Boot 2.x 项目

### OpenAPI 3

- 使用注解：`@Schema`, `@Tag`, `@Operation`, `@Parameter`
- 依赖：`springdoc-openapi-ui`
- 适用于：Spring Boot 2.2+ 和 Spring Boot 3.x 项目

详细对比请参考 `reference/swagger-annotations-guide.md`。

## 示例文档

- `examples/full-workflow-example.md` - 完整工作流程示例
- `examples/mvc-architecture-example.md` - MVC 架构生成示例
- `examples/ddd-architecture-example.md` - DDD 架构生成示例
- `examples/architecture-directory-mapping.md` - 架构目录映射示例
- `examples/swagger-annotations-example.md` - Swagger 注解使用示例

## 参考文档

### 核心参考

- `reference/mybatis-plus-generator-guide.md` - MyBatis-Plus Generator 使用指南
- `reference/template-variables.md` - 模板变量完整参考
- `reference/code-generation-standards.md` - 代码生成标准和注释规范

### 架构参考

- `reference/architecture-directory-mapping-guide.md` - 架构目录映射详细指南
- `reference/architecture-directory-quick-reference.md` - 架构目录映射快速参考

### 其他参考

- `reference/swagger-annotations-guide.md` - Swagger 2 vs OpenAPI 3 注解对比
- `reference/progress-and-statistics-formats.md` - 进度更新和统计报告格式

## 外部链接

- [MyBatis-Plus 官方文档](https://baomidou.com/)
- [MyBatis-Plus Generator 文档](https://baomidou.com/pages/d357af/)
- [MyBatis-Plus GitHub](https://github.com/baomidou/mybatis-plus)
- [MyBatis-Plus 官方模板](https://github.com/baomidou/mybatis-plus/tree/3.0/mybatis-plus-generator/src/main/resources/templates)
- [Agent Skills 规范](https://agentskills.io/)
- [Agent Skills 入门指南](https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills)

## 许可证

Apache 2.0 License - 详见 `LICENSE.txt`
