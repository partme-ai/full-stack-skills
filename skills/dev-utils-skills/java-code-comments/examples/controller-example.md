# Controller 代码注释示例

## 场景

为 Spring Boot REST Controller 添加完整的 JavaDoc 注释。

## 原始代码

```java
package com.example.controller;

import org.springframework.web.bind.annotation.*;
import com.example.dto.UserDTO;
import com.example.service.UserService;

@RestController
@RequestMapping("/api/users")
public class UserController {
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @PostMapping
    public UserDTO createUser(@RequestBody UserCreateRequest request) {
        return userService.createUser(request);
    }
    
    @GetMapping("/{id}")
    public UserDTO getUserById(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PutMapping("/{id}")
    public UserDTO updateUser(@PathVariable Long id, @RequestBody UserUpdateRequest request) {
        return userService.updateUser(id, request);
    }
    
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteById(id);
    }
}
```

## 添加注释后的代码

```java
package com.example.controller;

import org.springframework.web.bind.annotation.*;
import com.example.dto.UserDTO;
import com.example.service.UserService;

/**
 * 用户管理控制器
 * 
 * <p>提供用户相关的 REST API 接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>创建新用户</li>
 *   <li>根据 ID 查询用户信息</li>
 *   <li>更新用户信息</li>
 *   <li>删除用户</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    /**
     * 用户服务接口
     * 
     * <p>用于处理用户相关的业务逻辑
     */
    private final UserService userService;
    
    /**
     * 构造函数
     * 
     * @param userService 用户服务实例，由 Spring 容器注入
     */
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    /**
     * 创建新用户
     * 
     * <p>接收用户创建请求，验证数据后创建新用户并返回用户信息。
     * 
     * @param request 用户创建请求对象，包含用户名、邮箱、密码等信息
     * @return 创建成功的用户信息 DTO
     * @throws IllegalArgumentException 当请求参数不合法时抛出
     * @throws BusinessException 当用户名或邮箱已存在时抛出
     */
    @PostMapping
    public UserDTO createUser(@RequestBody UserCreateRequest request) {
        return userService.createUser(request);
    }
    
    /**
     * 根据用户 ID 查询用户信息
     * 
     * <p>根据提供的用户 ID 查询对应的用户详细信息。
     * 
     * @param id 用户唯一标识符
     * @return 用户信息 DTO，包含用户的基本信息
     * @throws ResourceNotFoundException 当用户不存在时抛出
     */
    @GetMapping("/{id}")
    public UserDTO getUserById(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    /**
     * 更新用户信息
     * 
     * <p>根据用户 ID 和更新请求，更新用户的指定字段信息。
     * 
     * @param id 用户唯一标识符
     * @param request 用户更新请求对象，包含需要更新的字段信息
     * @return 更新后的用户信息 DTO
     * @throws ResourceNotFoundException 当用户不存在时抛出
     * @throws IllegalArgumentException 当更新参数不合法时抛出
     */
    @PutMapping("/{id}")
    public UserDTO updateUser(@PathVariable Long id, @RequestBody UserUpdateRequest request) {
        return userService.updateUser(id, request);
    }
    
    /**
     * 删除用户
     * 
     * <p>根据用户 ID 删除指定的用户。删除操作会级联删除用户相关的数据。
     * 
     * @param id 用户唯一标识符
     * @throws ResourceNotFoundException 当用户不存在时抛出
     */
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteById(id);
    }
}
```

## 注释要点

1. **类注释**：
   - 描述控制器的职责和功能
   - 说明遵循的设计规范
   - 列出主要功能点
   - 包含 @author 和 @since 标签

2. **字段注释**：
   - 说明字段的用途
   - 解释依赖关系

3. **方法注释**：
   - 清晰描述方法功能
   - 详细说明所有参数
   - 说明返回值
   - 列出可能抛出的异常
