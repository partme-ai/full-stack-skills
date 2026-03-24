# 进度更新和统计格式

本文档提供代码生成过程中的进度更新和最终统计信息的格式标准。

## 进度更新格式

### 基本格式

```markdown
## 代码生成进度

### Table: {tableName}

✅ 已完成：
- [x] {ClassName}.java - {description}（{details}）

🔄 进行中：
- [ ] {ClassName}.java - {description}
  - [x] {completed item}
  - [ ] {pending item}

⏳ 待生成：
- [ ] {ClassName}.java - {description}
```

### 详细示例

```markdown
## 代码生成进度

### Table: user

✅ 已完成：
- [x] User.java - 实体类（包含 8 个字段，完整注释）
- [x] UserMapper.java - 数据访问接口（继承 BaseMapper）
- [x] UserService.java - 服务接口（6 个方法）

🔄 进行中：
- [ ] UserServiceImpl.java - 服务实现类
  - [x] 类注释
  - [x] saveUser() 方法
  - [ ] findById() 方法
  - [ ] updateUser() 方法
  - [ ] deleteById() 方法
  - [ ] findByEmail() 方法
  - [ ] findByUsername() 方法

⏳ 待生成：
- [ ] UserController.java - 控制器
- [ ] UserCreateDTO.java - 创建用户DTO
- [ ] UserUpdateDTO.java - 更新用户DTO
- [ ] UserVO.java - 用户视图对象

### Table: order

✅ 已完成：
- [x] Order.java - 实体类（包含 12 个字段）
- [x] OrderMapper.java - 数据访问接口

🔄 进行中：
- [ ] OrderService.java - 服务接口

⏳ 待生成：
- [ ] OrderServiceImpl.java - 服务实现类
- [ ] OrderController.java - 控制器
- [ ] OrderCreateDTO.java - 创建订单DTO
- [ ] OrderVO.java - 订单视图对象
```

### 更新时机

在以下时机更新进度：
- 每个表开始处理时
- 每个对象生成完成时
- 每个方法添加完成时
- 每个表处理完成时

## 统计信息格式

### 基本格式

```markdown
## 代码生成统计

### 总体统计
- **生成表数量**: {count} 张表（{table names}）
- **生成对象总数**: {count} 个对象
- **生成方法总数**: {count} 个方法
- **生成文件总数**: {count} 个文件
- **代码总行数**: 约 {count} 行

### 按表统计

#### {tableName} 表
- Entity: {count} 个（{fieldCount} 个字段）
- Mapper: {count} 个（继承 BaseMapper，{methodCount} 个基础方法）
- Service: {count} 个（{methodCount} 个方法：{standardCount} 个标准方法 + {customCount} 个自定义方法）
- ServiceImpl: {count} 个（{methodCount} 个方法实现）
- Controller: {count} 个（{endpointCount} 个接口）
- DTO: {count} 个（{dtoNames}）
- VO: {count} 个（{voNames}）
- **小计**: {totalObjects} 个对象，{totalMethods} 个方法

### 按类型统计
- Entity: {count} 个
- Mapper: {count} 个
- Service: {count} 个
- ServiceImpl: {count} 个
- Controller: {count} 个
- DTO: {count} 个
- VO: {count} 个

### 文件位置
所有文件已生成到以下目录：
- Entity: `{path}`
- Mapper: `{path}`
- Service: `{path}`
- ServiceImpl: `{path}`
- Controller: `{path}`
- DTO: `{path}`
- VO: `{path}`

### 代码质量
- ✅ 所有类都有完整的 JavaDoc 注释
- ✅ 所有方法都有参数和返回值说明
- ✅ 所有字段都有业务含义注释
- ✅ 自定义方法都有业务逻辑说明
- ✅ 符合 Java 编程规范
```

### 详细示例

```markdown
## 代码生成统计

### 总体统计
- **生成表数量**: 2 张表（user, order）
- **生成对象总数**: 14 个对象
- **生成方法总数**: 48 个方法
- **生成文件总数**: 14 个文件
- **代码总行数**: 约 2,500 行

### 按表统计

#### user 表
- Entity: 1 个（8 个字段）
- Mapper: 1 个（继承 BaseMapper，5 个基础方法）
- Service: 1 个（6 个方法：4 个标准方法 + 2 个自定义方法）
- ServiceImpl: 1 个（6 个方法实现）
- Controller: 1 个（5 个接口）
- DTO: 2 个（UserCreateDTO, UserUpdateDTO）
- VO: 1 个（UserVO）
- **小计**: 8 个对象，17 个方法

#### order 表
- Entity: 1 个（12 个字段）
- Mapper: 1 个（继承 BaseMapper，5 个基础方法）
- Service: 1 个（8 个方法：4 个标准方法 + 4 个自定义方法）
- ServiceImpl: 1 个（8 个方法实现）
- Controller: 1 个（7 个接口）
- DTO: 3 个（OrderCreateDTO, OrderUpdateDTO, OrderQueryDTO）
- VO: 1 个（OrderVO）
- **小计**: 8 个对象，31 个方法

### 按类型统计
- Entity: 2 个
- Mapper: 2 个
- Service: 2 个
- ServiceImpl: 2 个
- Controller: 2 个
- DTO: 5 个
- VO: 2 个

### 文件位置
所有文件已生成到以下目录：
- Entity: `src/main/java/com/example/app/entity/`
- Mapper: `src/main/java/com/example/app/mapper/`
- Service: `src/main/java/com/example/app/service/`
- ServiceImpl: `src/main/java/com/example/app/service/impl/`
- Controller: `src/main/java/com/example/app/controller/`
- DTO: `src/main/java/com/example/app/dto/`
- VO: `src/main/java/com/example/app/vo/`

### 代码质量
- ✅ 所有类都有完整的 JavaDoc 注释
- ✅ 所有方法都有参数和返回值说明
- ✅ 所有字段都有业务含义注释
- ✅ 自定义方法都有业务逻辑说明
- ✅ 符合 Java 编程规范
```

## 使用说明

### 进度更新

在代码生成过程中，实时更新进度：
1. 每完成一个对象，更新对应的复选框
2. 每完成一个方法，更新方法级别的进度
3. 每完成一个表，标记表为完成状态

### 统计信息

在代码生成完成后，输出完整的统计信息：
1. 统计所有表的生成情况
2. 按对象类型分类统计
3. 列出所有生成文件的路径
4. 说明代码质量情况

## 参考

- 完整工作流程示例：`../examples/full-workflow-example.md`
