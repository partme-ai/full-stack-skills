---
name: java-code-comments
description: |
  Provides comprehensive guidance for adding Java code comments following industry standards and best practices. 
  This skill helps add class-level comments, method-level comments, and field-level comments to Java code. 
  Use when the user wants to add comments to Java code, needs to document Java classes/methods/fields, 
  wants to improve code documentation, or needs to generate JavaDoc comments. This skill covers Controller, 
  Service, ServiceImpl, Mapper, Model, Entity, BO (Business Object), DTO, VO, and other common Java 
  component types. The skill follows a systematic workflow: scan codebase, identify components, create 
  todo list, and add comments in order (class comments → method comments → field comments).
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Adding comments to Java code
- Documenting Java classes, methods, or fields
- Generating JavaDoc comments
- Improving code documentation
- Code annotation or code commenting
- 给 Java 代码添加注释
- 生成 Java 文档注释
- 代码注释
- 添加注释

**Trigger phrases include:**
- "给这段代码添加注释" (add comments to this code)
- "生成 JavaDoc" (generate JavaDoc)
- "添加类注释" (add class comments)
- "添加方法注释" (add method comments)
- "添加属性注释" (add field comments)
- "代码注释" (code comments)
- "文档注释" (documentation comments)
- "一句话给 Java 代码添加注释" (add comments to Java code with one sentence)

**Component types this skill handles:**
- Controller (REST controllers, Spring MVC controllers)
- Service (business service interfaces)
- ServiceImpl (service implementations)
- Application Service (DDD application services, orchestrating domain logic)
- Domain Service (DDD domain services, domain business logic)
- Feign Service Interface (Feign remote service interfaces)
- Mapper (MyBatis mappers, data access layer)
- Model (data models, domain models)
- Entity (JPA entities, database entities)
- BO (Business Object, business logic objects)
- DTO (Data Transfer Object)
- VO (Value Object, View Object)
- DAO (Data Access Object)
- Repository (Spring Data repositories)
- Configuration (Spring configuration classes)
- Component (Spring components)
- Utility (utility classes)
- Exception (custom exception classes)

## How to use this skill

**CRITICAL: This skill should be triggered when the user wants to add comments to Java code, regardless of the component type or complexity.**

### Workflow Overview

This skill follows a systematic 4-step workflow:

1. **Scan and Understand** - Scan the entire codebase and related documentation to gain comprehensive understanding
2. **Confirm Component Types** - Ask user to confirm which component types need comments
3. **Create Todo List** - Generate a detailed todo list with class names and method names
4. **Execute Commenting** - Add comments in order: class comments → method comments → field comments, updating todo list after each completion

### Step-by-Step Process

#### Step 1: Scan and Understand the Codebase

**CRITICAL: Before adding any comments, you MUST:**

1. **Scan all Java files** in the project:
   - Read all `.java` files in the current directory and subdirectories
   - Understand the project structure and architecture
   - Identify relationships between classes (dependencies, inheritance, composition)

2. **Read related documentation**:
   - README.md files
   - API documentation
   - Architecture documentation
   - Business requirements documents (if available)

3. **Understand the context**:
   - What does each class do?
   - What is the purpose of each method?
   - What do fields represent?
   - How do components interact with each other?

4. **Identify patterns**:
   - Naming conventions used in the project
   - Existing comment styles (if any)
   - Architecture patterns (MVC, DDD, etc.)
   - Framework usage (Spring, MyBatis, etc.)

**Output**: A summary of your understanding of the codebase, including:
- Project structure overview
- Key components identified
- Architecture patterns detected
- Existing documentation status

#### Step 2: Confirm Component Types

**CRITICAL: You MUST ask the user to confirm which component types need comments.**

Present a checklist of common Java component types and ask the user to select:

```
请确认需要进行代码注释的分类（可多选）：
- [ ] Controller（控制器）
- [ ] Service（服务接口）
- [ ] ServiceImpl（服务实现）
- [ ] Application Service（应用服务，DDD架构）
- [ ] Domain Service（领域服务，DDD架构）
- [ ] Feign Service Interface（Feign远程服务接口）
- [ ] Mapper（数据访问层）
- [ ] Model（数据模型）
- [ ] Entity（实体类）
- [ ] BO（业务对象）
- [ ] DTO（数据传输对象）
- [ ] VO（视图对象）
- [ ] DAO（数据访问对象）
- [ ] Repository（仓储）
- [ ] Configuration（配置类）
- [ ] Component（组件类）
- [ ] Utility（工具类）
- [ ] Exception（异常类）
- [ ] 其他（请 specify）
```

**Also ask about comment types:**
- [ ] 类注释（Class-level comments）
- [ ] 方法注释（Method-level comments）
- [ ] 属性注释（Field-level comments）

**Wait for user confirmation** before proceeding to the next step.

#### Step 3: Create Todo List

**CRITICAL: After user confirms component types, create a detailed todo list.**

For each component type selected by the user:

1. **Scan the codebase** to find all matching classes:
   - Use file search to find classes matching the pattern (e.g., `*Controller.java`, `*Service.java`)
   - List all classes that need comments

2. **For each class, identify**:
   - Class name
   - Methods that need comments
   - Fields that need comments

3. **Generate a structured todo list** in the following format:

```markdown
## Todo List: Java Code Comments

### Controller 层
- [ ] UserController
  - [ ] 类注释
  - [ ] createUser() - 方法注释
  - [ ] updateUser() - 方法注释
  - [ ] deleteUser() - 方法注释
  - [ ] userId - 属性注释

### Service 层
- [ ] UserService
  - [ ] 类注释
  - [ ] findUserById() - 方法注释
  - [ ] saveUser() - 方法注释

### ServiceImpl 层
- [ ] UserServiceImpl
  - [ ] 类注释
  - [ ] findUserById() - 方法注释
  - [ ] saveUser() - 方法注释

### Mapper 层
- [ ] UserMapper
  - [ ] 类注释
  - [ ] selectById() - 方法注释

### Model/Entity 层
- [ ] User
  - [ ] 类注释
  - [ ] id - 属性注释
  - [ ] username - 属性注释
  - [ ] email - 属性注释
```

**Important**: 
- Organize by component type
- List all classes that match the selected types
- Include all methods and fields that need comments
- Use checkboxes for tracking progress

#### Step 4: Execute Commenting Work

**CRITICAL: Add comments in the specified order and update todo list after each completion.**

**Order of execution:**
1. **Class-level comments** (类注释) - First
2. **Method-level comments** (方法注释) - Second
3. **Field-level comments** (属性注释) - Third

**For each item in the todo list:**

1. **Process one class at a time**:
   - Start with class-level comment
   - Then process all methods in that class
   - Finally process all fields in that class
   - Update the todo list after completing each class

2. **Class-level comment format** (Standard JavaDoc):
   ```java
   /**
    * [Class description]
    * 
    * <p>This class [purpose and responsibility]
    * 
    * @author [Author name if available]
    * @since [Version or date if available]
    */
   public class UserController {
   ```

   **Class-level comment format** (Java Coding Standards - strict):
   ```java
   /**
    * <p>[Class description]</p>
    * 
    * <p>This class [purpose and responsibility]</p>
    * 
    * @author [Author name if available]
    * @since [Version or date if available]
    */
   public class UserController {
   ```

   **Specialized class comment formats** (Java Coding Standards - strict):

   **Application Service:**
   ```java
   /**
    * {服务名称}应用服务
    *
    * <p>{详细描述服务的业务功能、职责和应用场景}</p>
    * <p>主要功能包括:</p>
    * <ul>
    *   <li>{功能点1}</li>
    *   <li>{功能点2}</li>
    *   <li>{功能点3}</li>
    * </ul>
    *
    * @author system
    * @since 2025-01-21
    */
   public class UserApplicationService {
   ```

   **Domain Service:**
   ```java
   /**
    * {服务名称}领域服务
    *
    * <p>{详细描述服务的领域职责和业务逻辑}</p>
    * <p>主要功能包括:</p>
    * <ul>
    *   <li>{功能点1}</li>
    *   <li>{功能点2}</li>
    * </ul>
    *
    * @author system
    * @since 2025-01-21
    */
   public class UserDomainService {
   ```

   **Feign Service Interface:**
   ```java
   /**
    * {服务名称}Feign远程服务接口
    *
    * <p>通过Feign调用{目标服务}的远程接口</p>
    * <p>主要功能:</p>
    * <ul>
    *   <li>{接口功能1}</li>
    *   <li>{接口功能2}</li>
    * </ul>
    *
    * @author system
    * @since 2025-01-21
    */
   public interface UserFeignService {
   ```

3. **Method-level comment format** (Standard JavaDoc):
   ```java
   /**
    * [Method description]
    * 
    * @param [paramName] [parameter description]
    * @return [return value description]
    * @throws [ExceptionType] [exception description]
    */
   public UserDTO createUser(@RequestBody UserCreateRequest request) {
   ```

   **Method-level comment format** (Java Coding Standards - strict):
   ```java
   /**
    * <p>[Method description]</p>
    * 
    * <p>[Detailed description]</p>
    * 
    * @param [paramName] [paramType] [parameter description]
    * @return [returnType] [return value description]
    * @exception [full.package.ExceptionType] [exception description]
    */
   public UserDTO createUser(@RequestBody UserCreateRequest request) {
   ```

4. **Field-level comment format** (Standard JavaDoc):
   ```java
   /**
    * [Field description]
    */
   private Long userId;
   ```

   **Field-level comment format** (Java Coding Standards - strict):
   ```java
   /**
    * <p>[Field description]</p>
    * 
    * <p>[Detailed description if needed]</p>
    */
   private Long userId;
   ```

5. **After completing each class**:
   - Update the todo list: mark completed items with `[x]`
   - Show progress to the user
   - Continue to the next class

**Example progress update:**
```markdown
## Progress Update

✅ Completed: UserController
  - [x] 类注释
  - [x] createUser() - 方法注释
  - [x] updateUser() - 方法注释
  - [x] deleteUser() - 方法注释
  - [x] userId - 属性注释

🔄 In Progress: UserService
  - [x] 类注释
  - [ ] findUserById() - 方法注释
  - [ ] saveUser() - 方法注释
```

### Comment Quality Guidelines

**IMPORTANT: Comment Format Standards**

This skill follows two standards:
1. **Standard JavaDoc** (default): See [javadoc-standards.md](reference/javadoc-standards.md) (within this skill)
2. **Java Coding Standards** (strict): See [java-coding-standards.md](reference/java-coding-standards.md) (within this skill)

The Java Coding Standards require:
- **Description must be wrapped in `<p>` tags**: `<p>description</p>`
- **Parameter types must be declared**: `@param paramName paramType description`
- **Return types must be declared**: `@return returnType description`
- **Exception types must be declared with full package name**: `@exception java.lang.Exception description`

**Class Comments Should Include:**
- Clear description of the class purpose (wrapped in `<p>` tags if following Java Coding Standards)
- Main responsibilities
- Usage examples (if complex)
- Related classes or components
- Author and version (if available)

**Method Comments Should Include:**
- Clear description of what the method does (wrapped in `<p>` tags if following Java Coding Standards)
- All parameters with descriptions and types
- Return value description with type
- Exceptions that may be thrown (with full package names)
- Usage examples (for complex methods)
- Side effects (if any)

**Field Comments Should Include:**
- Clear description of what the field represents (wrapped in `<p>` tags if following Java Coding Standards)
- Data type and constraints (if applicable)
- Default values (if applicable)
- Relationships to other fields (if applicable)

### Best Practices

1. **Be concise but complete**: Comments should be clear and informative without being verbose
2. **Use JavaDoc format**: Follow standard JavaDoc conventions
3. **Maintain consistency**: Use consistent style across all comments
4. **Update todo list**: Always update the todo list after completing each item
5. **One class at a time**: Process one complete class before moving to the next
6. **Respect existing code**: Don't modify code logic, only add comments
7. **Context-aware**: Comments should reflect the actual code behavior and business context

### Comment Templates

For different component types, use appropriate templates from the `templates/` directory:
- `templates/controller-comment-template.md` - Controller class comments
- `templates/service-comment-template.md` - Service interface comments
- `templates/serviceimpl-comment-template.md` - Service implementation comments
- `templates/application-service-comment-template.md` - Application Service comments (DDD)
- `templates/domain-service-comment-template.md` - Domain Service comments (DDD)
- `templates/feign-service-comment-template.md` - Feign Service Interface comments
- `templates/mapper-comment-template.md` - Mapper comments
- `templates/entity-comment-template.md` - Entity class comments
- `templates/dto-comment-template.md` - DTO class comments

### Comment Standards Reference

**Note**: All reference documents are located within this skill's directory structure.

- **Standard JavaDoc**: See [reference/javadoc-standards.md](reference/javadoc-standards.md) (local reference)
- **Java Coding Standards** (strict format): See [reference/java-coding-standards.md](reference/java-coding-standards.md) (local reference)

**When to use Java Coding Standards format:**
- When the project explicitly follows 《JAVA 编程规范》
- When the project requires strict format with `<p>` tags for descriptions
- When parameter and return types must be explicitly declared in comments

### Examples

See the `examples/` directory for complete examples:
- `examples/controller-example.md` - Controller commenting example
- `examples/service-example.md` - Service commenting example
- `examples/entity-example.md` - Entity commenting example
- `examples/full-workflow-example.md` - Complete workflow example

## Keywords

**English keywords:**
java, code comments, javadoc, documentation, class comments, method comments, field comments, code annotation, code documentation, java documentation, add comments, generate comments, document code, code comments java, java code comments, controller comments, service comments, mapper comments, entity comments, dto comments

**Chinese keywords (中文关键词):**
Java 代码注释, 添加注释, 生成注释, 代码注释, 文档注释, JavaDoc, 类注释, 方法注释, 属性注释, 字段注释, 给代码添加注释, 代码文档, Java 文档, 注释生成, 一句话添加注释, Controller 注释, Service 注释, Mapper 注释, Entity 注释, DTO 注释, 代码注解
