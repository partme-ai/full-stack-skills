# DDD4j 项目脚手架（Project Scaffolding）

ddd4j Boot 是 COLA v5 的 Java 参考实现，提供完整的项目生成和验证工具链。

## 项目生成流程

### Step 1: 确认项目类型

从用户需求中识别项目类型：
- **Single-module monolith** (`single-module`): 中小型应用，单个业务领域，团队规模 5-15 人
- **Multi-module monolith** (`multi-module`): 中大型应用，多个业务域，团队规模 15-50 人
- **Microservices** (`microservices`): 大型电商平台，多个业务域，团队规模 50+ 人

### Step 2: 加载对应的示例

从 `examples/` 目录加载合适的项目结构示例：
- `examples/13-architecture-patterns.md` — DDD、Hexagonal、Clean、COLA V5 四种架构模式
- `examples/14-single-module.md` — 单模块单体结构
- `examples/15-multi-module.md` — 多模块单体结构
- `examples/16-microservices.md` — 微服务结构

### Step 3: 收集项目信息

- `groupId`: Maven group ID（如 `com.github.hiwepy`）
- `artifactId`: Maven artifact ID（如 `ddd4j-douyin`）
- `version`: 项目版本（如 `1.0.0-SNAPSHOT`）
- `packageBase`: 基础包名（如 `io.ddd4j.douyin`）
- `modules`: 业务模块列表（多模块/微服务场景）
- `architecture`: 架构模式（DDD Classic、Hexagonal、Clean、COLA V5）

### Step 4: 生成项目结构

- 根据所选类型创建目录结构
- 生成 `pom.xml` 文件（父模块和子模块）
- 为每个模块创建 `package-info.java` 文件
- 生成 `.gitignore`、`LICENSE`、`mvnw`、`mvnw.cmd`
- 创建基础目录结构 `src/main/java` 和 `src/test/java`

### Step 5: 保存到项目目录

- **默认位置**: 直接保存到命令执行目录（与命令同级）
- **目录创建**: 自动创建项目目录结构（如不存在）
- **文件命名**: 使用 artifactId 作为项目根目录名

## 项目结构标准

### 包命名规范

多模块项目遵循：
```
{basePackage}.{moduleName}.{layerName}
```

示例：
- `io.ddd4j.douyin.api.domain` — API 模块领域层
- `io.ddd4j.douyin.api.application` — API 模块应用层
- `io.ddd4j.douyin.api.interfaces` — API 模块接口层
- `io.ddd4j.douyin.api.infrastructure` — API 模块基础设施层

### 必需文件清单

每个模块必须包含：
- `pom.xml` — Maven 配置
- `src/main/java/{package}/package-info.java` — 包文档
- `src/test/java/` — 测试目录结构
- `.gitignore` — Git 忽略规则（根目录）
- `LICENSE` — 许可证文件（根目录）
- `mvnw`、`mvnw.cmd` — Maven Wrapper（根目录）

### 层依赖关系

正确的依赖方向：
```
interfaces → application → domain ← infrastructure
```

规则：
- **Domain 层**不得依赖任何其他层
- **Infrastructure 层**实现 Domain 层定义的接口
- **Application 层**依赖 Domain 层
- **Interfaces 层**依赖 Application 层

## 验证规则

对已有项目进行合规检查时，验证以下方面：

### 1. 结构合规性
- 分层组织是否正确
- 模块划分是否合理
- 包命名是否符合规范

### 2. 依赖规则
- Domain 层无外部依赖
- Infrastructure 正确实现 Domain 接口
- 依赖方向正确（interfaces → application → domain ← infrastructure）

### 3. 文件组织
- 必需目录是否存在
- `package-info.java` 文件是否存在
- Maven 配置是否正确

### 4. 命名规范
- 包名是否遵循 `{basePackage}.{module}.{layer}` 约定
- 模块名称是否描述性明确
- 层名称是否标准化
