# API Documentation Generator Skill

## 概述

这是一个基于 Agent Skills 规范的接口文档生成技能，可以自动扫描项目中的 Controller 类，提取接口信息（请求地址、请求方式、入参、出参），并生成符合标准的接口文档。

**重要提示**：本技能仅在用户明确提到 **接口文档** 或 **API文档** 时触发，避免与其他文档生成工具产生冲突。

## 功能特点

1. **智能扫描**：自动扫描项目中的 Controller 类，识别所有 API 接口
2. **信息提取**：提取接口的完整信息，包括请求地址、请求方式、参数、响应结构
3. **双语模板**：提供中文和英文两种标准接口文档模板，格式统一规范
4. **自动保存**：生成的文档自动保存到项目 `./docs` 目录
5. **多语言支持**：支持 Java 和 Kotlin 项目
6. **框架支持**：支持 Spring Boot、Spring MVC 等框架

## 文件结构

```
api-doc-generator/
├── SKILL.md                              # 主技能文档（Agent Skills 规范）
├── LICENSE.txt                           # Apache 2.0 许可证
├── README.md                             # 本文件
├── templates/                            # 模板目录
│   ├── 接口文档模板.md                   # 标准接口文档模板（中文）
│   └── api-documentation-template-en.md # 标准接口文档模板（英文）
└── examples/                             # 示例目录
    └── scan-and-generate-example.md     # 扫描和生成示例
```

## 工作流程

技能遵循 4 步系统化工作流程：

1. **扫描代码**：检查当前项目或指定对象的代码，扫描 Controller 类和接口方法
2. **提取信息**：为每个接口收集完整信息（请求地址、请求方式、入参、出参）
3. **生成文档**：依据接口模板创建符合当前项目的接口文档
4. **保存输出**：将生成的文档统一保存到当前项目下的 `./docs` 目录中

## 使用方式

**重要提示**：本技能仅在用户明确提到 **接口文档** 或 **API文档** 时触发。

### 触发短语示例

- ✅ "生成接口文档"
- ✅ "扫描接口生成文档"
- ✅ "创建API文档"
- ✅ "为接口生成文档"
- ❌ "生成文档"（未明确提到接口，不会触发）
- ❌ "创建文档"（未明确提到接口，不会触发）

### 使用流程

当用户明确提到生成接口文档时，技能会自动：

1. **选择模板语言**：询问用户偏好语言（中文/英文），或根据项目上下文自动检测
2. **扫描代码**：查找项目中的 Controller 类
3. **验证接口**：检查是否有接口方法，如果没有则提示无法生成
4. **提取信息**：为每个接口提取完整信息
5. **生成文档**：使用选定的模板（中文或英文）生成接口文档
6. **保存文件**：保存到 `./docs` 目录

## 扫描规则

### Controller 识别

- **Java/Spring Boot**：
  - 查找 `@RestController` 或 `@Controller` 注解的类
  - 常见包路径：`*.controller.*`, `*.web.*`, `*.api.*`
  - 文件名模式：`*Controller.java` 或 `*Controller.kt`

### 接口方法识别

- 查找以下注解的方法：
  - `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, `@PatchMapping`
  - `@RequestMapping(method = RequestMethod.*)`

### 参数提取

- **Path Parameters**：`@PathVariable` 注解的参数
- **Query Parameters**：`@RequestParam` 注解的参数
- **Request Body**：`@RequestBody` 注解的参数
- **Request Headers**：`@RequestHeader` 注解的参数

### 响应提取

- 方法返回类型
- `@ResponseBody` 注解
- 泛型类型（如 `R<T>`, `Page<T>`）
- 响应实体结构

## 文档模板

技能提供**中文**和**英文**两种标准模板，结构完全一致，仅语言不同。

### 中文模板 (`templates/接口文档模板.md`)

1. **文档概览**：版本记录、责任人
2. **接口一览表**：所有接口的汇总表格
3. **接口定义**：每个接口的详细定义
   - 接口说明
   - 请求信息（Method、URL、Headers、Parameters、Body）
   - 响应信息（结构、字段、示例）
4. **统一响应结构**：标准响应格式、分页格式、错误码
5. **请求头规范**：请求头说明
6. **注意事项**：重要提示

### 英文模板 (`templates/api-documentation-template-en.md`)

1. **Document Overview**: Version history, responsibilities
2. **API Interface List**: Summary table of all interfaces
3. **Interface Definitions**: Detailed definition for each interface
   - Interface description
   - Request information (Method, URL, Headers, Parameters, Body)
   - Response information (structure, fields, examples)
4. **Standard Response Structure**: Standard response format, pagination format, error codes
5. **Request Header Specifications**: Request header descriptions
6. **Important Notes**: Important reminders

### 模板选择

- 技能会自动询问用户偏好语言（中文/英文）
- 如果未指定，会根据项目上下文（代码注释、包名等）自动检测
- 两种模板结构完全相同，仅语言不同

## 输出位置

- **默认路径**：`./docs/api-documentation.md`
- **多模块**：`./docs/{module-name}-api-documentation.md`
- **自定义**：用户可指定自定义文件名

如果 `./docs` 目录不存在，会自动创建。

## 示例

### 示例 1: 扫描整个项目

**用户**: "生成接口文档"

**AI 执行**:
1. 扫描项目，发现 3 个 Controller 类
2. 提取 19 个接口的完整信息
3. 生成接口文档
4. 保存到 `./docs/api-documentation.md`

### 示例 2: 扫描指定 Controller

**用户**: "为 OrderController 生成接口文档"

**AI 执行**:
1. 定位 `OrderController` 类
2. 提取 5 个接口的完整信息
3. 生成订单模块接口文档
4. 保存到 `./docs/order-api-documentation.md`

详细示例请参考 `examples/scan-and-generate-example.md`。

## 注意事项

1. **接口验证**：如果项目中没有 Controller 类或接口方法，会提示无法生成文档
2. **信息完整性**：尽量从代码注释和注解中提取接口描述信息
3. **格式规范**：生成的文档严格遵循模板格式
4. **编码格式**：文档使用 UTF-8 编码保存

## 参考资料

- **模板文件**：
  - `templates/接口文档模板.md` - 标准接口文档模板（中文）
  - `templates/api-documentation-template-en.md` - 标准接口文档模板（英文）
- **示例文件**：`examples/scan-and-generate-example.md` - 使用示例
- **Agent Skills 规范**：https://agentskills.io/

## 许可证

Apache 2.0 License - 详见 `LICENSE.txt`
