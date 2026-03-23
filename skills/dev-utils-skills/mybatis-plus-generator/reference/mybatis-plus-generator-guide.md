# MyBatis-Plus Generator 参考指南

## 概述

本文档提供 MyBatis-Plus Generator 的使用指南和最佳实践，帮助理解代码生成的原理和配置。

## MyBatis-Plus Generator 原理

### 核心组件

1. **代码生成器（CodeGenerator）**
   - 负责读取数据库表结构
   - 根据配置生成代码
   - 使用模板引擎渲染代码

2. **模板引擎**
   - 支持 Velocity、Freemarker、Beetl
   - 使用占位符替换生成代码
   - 官方模板位于：`mybatis-plus-generator/src/main/resources/templates`

3. **配置策略（StrategyConfig）**
   - 控制生成哪些文件
   - 控制命名规则
   - 控制字段映射规则

### 生成流程

```
数据库表结构
    ↓
读取表元数据（列、类型、约束）
    ↓
应用配置策略（命名、包路径等）
    ↓
加载模板文件
    ↓
替换模板变量
    ↓
生成代码文件
```

## 官方模板参考

### 模板位置

MyBatis-Plus 官方模板位于：
- GitHub: https://github.com/baomidou/mybatis-plus/tree/3.0/mybatis-plus-generator/src/main/resources/templates
- 本地路径：`mybatis-plus-generator/src/main/resources/templates`

### 模板文件

1. **entity.java.vm** - Entity 实体类模板
2. **mapper.java.vm** - Mapper 接口模板
3. **mapper.xml.vm** - Mapper XML 模板
4. **service.java.vm** - Service 接口模板
5. **serviceImpl.java.vm** - ServiceImpl 实现类模板
6. **controller.java.vm** - Controller 控制器模板

### 模板变量

常用模板变量：

- `${package.Entity}` - Entity 包路径
- `${package.Mapper}` - Mapper 包路径
- `${package.Service}` - Service 包路径
- `${package.Controller}` - Controller 包路径
- `${author}` - 作者
- `${date}` - 日期
- `${table.name}` - 表名
- `${entity}` - 实体类名
- `${table.comment}` - 表注释
- `${field.name}` - 字段名
- `${field.propertyName}` - 属性名
- `${field.comment}` - 字段注释
- `${field.type}` - 字段类型

## 配置说明

### 全局配置（GlobalConfig）

```java
GlobalConfig globalConfig = new GlobalConfig();
globalConfig.setAuthor("System");              // 作者
globalConfig.setOutputDir("src/main/java");    // 输出目录
globalConfig.setFileOverride(true);            // 是否覆盖文件
globalConfig.setOpen(false);                   // 是否打开输出目录
globalConfig.setSwagger2(true);                // 是否开启 Swagger
```

### 包配置（PackageConfig）

```java
PackageConfig packageConfig = new PackageConfig();
packageConfig.setParent("com.example.app");    // 父包名
packageConfig.setEntity("entity");              // Entity 包名
packageConfig.setMapper("mapper");             // Mapper 包名
packageConfig.setService("service");           // Service 包名
packageConfig.setServiceImpl("service.impl");  // ServiceImpl 包名
packageConfig.setController("controller");     // Controller 包名
```

### 策略配置（StrategyConfig）

```java
StrategyConfig strategyConfig = new StrategyConfig();
strategyConfig.setNaming(NamingStrategy.underline_to_camel);  // 命名策略
strategyConfig.setColumnNaming(NamingStrategy.underline_to_camel);
strategyConfig.setEntityLombokModel(true);      // 使用 Lombok
strategyConfig.setRestControllerStyle(true);    // REST 风格
strategyConfig.setControllerMappingHyphenStyle(true);
strategyConfig.setTablePrefix("t_");            // 表前缀
```

### 模板配置（TemplateConfig）

```java
TemplateConfig templateConfig = new TemplateConfig();
templateConfig.setEntity("/templates/entity.java.vm");
templateConfig.setMapper("/templates/mapper.java.vm");
templateConfig.setService("/templates/service.java.vm");
templateConfig.setServiceImpl("/templates/serviceImpl.java.vm");
templateConfig.setController("/templates/controller.java.vm");
```

## 最佳实践

### 1. 注释生成

- 使用表注释作为类注释
- 使用字段注释作为属性注释
- 根据业务逻辑生成方法注释
- 遵循 Java 编程规范

### 2. 代码质量

- 生成生产就绪的代码
- 包含适当的注解（Lombok、Swagger、Validation）
- 包含完整的 JavaDoc 注释
- 遵循命名规范

### 3. 自定义方法

- 根据业务需求生成自定义方法
- 提供方法骨架和 TODO 注释
- 包含参数验证提示
- 包含异常处理提示

### 4. 架构适配

- 根据架构类型生成不同的对象
- MVC：Entity, Mapper, Service, ServiceImpl, Controller
- DDD：Entity, Mapper, Service, ServiceImpl, Controller, DTO, VO, BO
- Clean Architecture：Entity, Repository, UseCase, Controller, DTO

## 参考资料

- [MyBatis-Plus 官方文档](https://baomidou.com/)
- [MyBatis-Plus Generator 文档](https://baomidou.com/pages/d357af/)
- [MyBatis-Plus GitHub](https://github.com/baomidou/mybatis-plus)
- [MyBatis-Plus Generator UI](https://github.com/Coffee-Tang/mybatis-plus-generator-ui)
