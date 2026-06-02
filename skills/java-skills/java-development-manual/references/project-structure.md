# 工程结构规约

## 目录
- [一、应用分层](#一应用分层)
- [二、领域模型](#二领域模型)
- [三、二方库依赖](#三二方库依赖)
- [四、服务器配置](#四服务器配置)

---

## 一、应用分层

### 推荐分层架构

```
┌─────────────────────────────────────────────────────┐
│                   开放API层                          │
│    (RPC接口/HTTP接口/网关控制)                        │
├─────────────────────────────────────────────────────┤
│                   终端显示层                          │
│    (velocity/JS/JSP/移动端)                          │
├─────────────────────────────────────────────────────┤
│                    Web层                             │
│    (Controller/参数校验/简单业务)                     │
├─────────────────────────────────────────────────────┤
│                   Service层                          │
│    (具体业务逻辑)                                     │
├─────────────────────────────────────────────────────┤
│                   Manager层                          │
│    (通用业务/第三方封装/DAO组合)                       │
├─────────────────────────────────────────────────────┤
│                    DAO层                             │
│    (数据访问/MySQL/Oracle/HBase)                     │
└─────────────────────────────────────────────────────┘
```

### 各层职责

| 层级 | 职责 | 说明 |
|------|------|------|
| **开放API层** | 对外暴露 | RPC接口、HTTP接口、网关 |
| **终端显示层** | 渲染展示 | velocity、JS、JSP、移动端 |
| **Web层** | 访问控制转发 | Controller、参数校验 |
| **Service层** | 业务逻辑 | 具体业务处理 |
| **Manager层** | 通用处理 | 第三方封装、缓存、DAO组合 |
| **DAO层** | 数据访问 | MySQL、Oracle、HBase |

### 分层异常处理

| 层级 | 异常处理方式 |
|------|-------------|
| **DAO层** | catch(Exception) + throw DAOException，不打印日志 |
| **Service层** | 必须记录日志到磁盘 |
| **Web层** | 跳转友好错误页面 |
| **开放接口层** | 转化为错误码和错误信息 |

---

## 二、领域模型

| 模型 | 全称 | 说明 |
|------|------|------|
| **DO** | Data Object | 与数据库表一一对应 |
| **DTO** | Data Transfer Object | 数据传输对象 |
| **BO** | Business Object | 业务对象 |
| **Query** | - | 数据查询对象（超过2个参数封装） |
| **VO** | View Object | 显示层对象 |

**注意**：Query禁止使用Map类传输

---

## 三、二方库依赖

### 【强制】规约

1. **GAV命名规范**：
   - **GroupID**：`com.{公司/BU}.业务线[.子业务线]`，最多4级
   - **ArtifactID**：`产品线名-模块名`

2. **版本号格式**：`主版本号.次版本号.修订号`
   - 主版本号：产品方向改变、大规模API不兼容
   - 次版本号：相对兼容、增加主要功能
   - 修订号：完全兼容、修复BUG
   - **起始版本号必须为1.0.0**

3. **线上不依赖SNAPSHOT版本**

4. **依赖群定义统一版本变量**：
   ```xml
   <properties>
       <spring.version>5.3.20</spring.version>
   </properties>
   ```

5. **禁止相同GAV不同Version**

### 【推荐】规约

1. **依赖声明与版本仲裁分离**：
   ```xml
   <!-- 父POM：版本仲裁 -->
   <dependencyManagement>
       <dependencies>...</dependencies>
   </dependencyManagement>

   <!-- 子POM：依赖声明 -->
   <dependencies>...</dependencies>
   ```

2. **二方库不要有配置项**

---

## 四、服务器配置

### 【推荐】规约

1. **调小TCP time_wait超时时间**：
   ```bash
   # /etc/sysctl.conf
   net.ipv4.tcp_fin_timeout = 30
   ```

2. **调大最大文件句柄数**

3. **JVM配置OOM时输出dump**：
   ```bash
   -XX:+HeapDumpOnOutOfMemoryError
   ```

4. **Xms和Xmx设置相同大小**：
   ```bash
   -Xms4g -Xmx4g
   ```

---

## 项目目录结构示例

```
project-name/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/company/project/
│   │   │       ├── controller/        # Web层
│   │   │       ├── service/           # Service层
│   │   │       │   └── impl/
│   │   │       ├── manager/           # Manager层
│   │   │       ├── dao/               # DAO层
│   │   │       ├── model/             # 领域模型
│   │   │       │   ├── dto/
│   │   │       │   ├── vo/
│   │   │       │   └── query/
│   │   │       └── config/
│   │   └── resources/
│   │       ├── mapper/
│   │       └── application.yml
│   └── test/
│       └── java/
```
