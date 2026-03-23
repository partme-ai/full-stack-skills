---
name: spring-boot
description: Provides comprehensive guidance for Spring Boot development including project creation, auto-configuration, dependency injection, web development, data access, security, testing, and deployment. Use when the user asks about Spring Boot, needs to create Spring Boot applications, configure Spring Boot, or implement Spring Boot features.
---

# Spring Boot 开发指南

## 概述

Spring Boot 是一个基于 Spring 框架的快速开发框架，提供了自动配置、起步依赖等特性，简化了 Spring 应用的开发。

## 核心特性

### 1. 项目创建

**使用 Spring Initializr**：

访问 https://start.spring.io/ 或使用 IDE 插件创建项目。

**使用 CLI**：

```bash
# 安装 Spring Boot CLI
brew install spring-boot

# 创建项目
spring init --dependencies=web,data-jpa,postgresql my-project
```

**Maven 项目结构**：

```
my-project/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/
│   │   │       └── MyApplication.java
│   │   └── resources/
│   │       ├── application.properties
│   │       └── application.yml
│   └── test/
├── pom.xml
└── README.md
```

### 2. 自动配置

Spring Boot 通过自动配置简化了配置工作。

**application.yml**：

```yaml
spring:
  application:
    name: my-app
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: postgres
    password: password
    driver-class-name: org.postgresql.Driver
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
  server:
    port: 8080
```

**application.properties**：

```properties
spring.application.name=my-app
spring.datasource.url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.username=postgres
spring.datasource.password=password
spring.datasource.driver-class-name=org.postgresql.Driver
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
server.port=8080
```

### 3. 依赖注入

**使用 @Component**：

```java
@Component
public class UserService {
    public String getUserName(Long id) {
        return "User " + id;
    }
}
```

**使用 @Service**：

```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public User findById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
}
```

**使用 @Repository**：

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByNameContaining(String name);
}
```

### 4. Web 开发

**REST Controller**：

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping
    public List<User> getAllUsers() {
        return userService.findAll();
    }
    
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.save(user);
    }
    
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        return userService.update(id, user);
    }
    
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.delete(id);
    }
}
```

**异常处理**：

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage()
        );
        return new ResponseEntity<>(error, HttpStatus.NOT_FOUND);
    }
}
```

### 5. 数据访问

**JPA Entity**：

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    // Getters and Setters
}
```

**Repository**：

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByNameContaining(String name);
    
    @Query("SELECT u FROM User u WHERE u.email = :email")
    Optional<User> findByEmailCustom(@Param("email") String email);
}
```

**Service**：

```java
@Service
@Transactional
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public User save(User user) {
        return userRepository.save(user);
    }
    
    public Optional<User> findById(Long id) {
        return userRepository.findById(id);
    }
    
    public List<User> findAll() {
        return userRepository.findAll();
    }
    
    public void delete(Long id) {
        userRepository.deleteById(id);
    }
}
```

### 6. 配置管理

**@ConfigurationProperties**：

```java
@ConfigurationProperties(prefix = "app")
@Data
public class AppProperties {
    private String name;
    private String version;
    private Database database;
    
    @Data
    public static class Database {
        private String host;
        private int port;
        private String name;
    }
}
```

**使用配置**：

```yaml
app:
  name: my-app
  version: 1.0.0
  database:
    host: localhost
    port: 5432
    name: mydb
```

### 7. 安全（Spring Security）

**依赖**：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

**配置**：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated()
            )
            .httpBasic();
        return http.build();
    }
}
```

### 8. 测试

**单元测试**：

```java
@SpringBootTest
class UserServiceTest {
    @Autowired
    private UserService userService;
    
    @Test
    void testFindById() {
        User user = userService.findById(1L)
            .orElseThrow();
        assertNotNull(user);
    }
}
```

**集成测试**：

```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
class UserControllerTest {
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    void testGetUser() throws Exception {
        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("John"));
    }
}
```

## 最佳实践

### 1. 项目结构

```
com.example.myapp/
├── controller/      # 控制器
├── service/        # 服务层
├── repository/     # 数据访问层
├── entity/         # 实体类
├── dto/            # 数据传输对象
├── config/         # 配置类
└── exception/      # 异常类
```

### 2. 依赖注入

- 优先使用构造函数注入
- 避免使用 `@Autowired` 字段注入
- 使用 `@RequiredArgsConstructor` (Lombok)

### 3. 异常处理

- 使用 `@ControllerAdvice` 全局异常处理
- 定义自定义异常类
- 返回统一的错误响应格式

### 4. 配置管理

- 使用 `application.yml` 而非 `application.properties`
- 区分开发、测试、生产环境配置
- 使用 `@ConfigurationProperties` 绑定配置

## 常用依赖

```xml
<!-- Web -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- JPA -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- PostgreSQL -->
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
</dependency>

<!-- Lombok -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
</dependency>
```

## 示例 Prompt

- "使用 Spring Boot 创建一个 REST API 项目"
- "如何在 Spring Boot 中使用 JPA 进行数据访问？"
- "Spring Boot 中如何配置数据库连接？"
- "如何在 Spring Boot 中实现全局异常处理？"
- "Spring Boot 中如何使用 Spring Security？"
