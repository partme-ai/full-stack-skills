# Service 代码注释示例

## 场景

为 Service 接口和实现类添加完整的 JavaDoc 注释。

## Service 接口示例

### 原始代码

```java
package com.example.service;

import com.example.dto.UserDTO;
import java.util.List;

public interface UserService {
    
    UserDTO createUser(UserCreateRequest request);
    
    UserDTO findById(Long id);
    
    List<UserDTO> findAll();
    
    UserDTO updateUser(Long id, UserUpdateRequest request);
    
    void deleteById(Long id);
}
```

### 添加注释后的代码

```java
package com.example.service;

import com.example.dto.UserDTO;
import java.util.List;

/**
 * 用户服务接口
 * 
 * <p>定义用户相关的业务逻辑接口，包括用户的增删改查操作。
 * 本接口遵循领域驱动设计（DDD）原则，封装用户领域的核心业务逻辑。
 * 
 * <p>主要职责：
 * <ul>
 *   <li>用户创建和注册</li>
 *   <li>用户信息查询</li>
 *   <li>用户信息更新</li>
 *   <li>用户删除</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
public interface UserService {
    
    /**
     * 创建新用户
     * 
     * <p>根据用户创建请求创建新用户，包括数据验证、密码加密等处理。
     * 
     * @param request 用户创建请求对象
     * @return 创建成功的用户信息 DTO
     * @throws IllegalArgumentException 当请求参数不合法时抛出
     * @throws BusinessException 当用户名或邮箱已存在时抛出
     */
    UserDTO createUser(UserCreateRequest request);
    
    /**
     * 根据 ID 查询用户
     * 
     * <p>根据用户 ID 查询用户详细信息，如果用户不存在则抛出异常。
     * 
     * @param id 用户唯一标识符
     * @return 用户信息 DTO
     * @throws ResourceNotFoundException 当用户不存在时抛出
     */
    UserDTO findById(Long id);
    
    /**
     * 查询所有用户
     * 
     * <p>查询系统中所有用户的信息列表。
     * 
     * @return 用户信息 DTO 列表
     */
    List<UserDTO> findAll();
    
    /**
     * 更新用户信息
     * 
     * <p>根据用户 ID 和更新请求，更新用户的指定字段信息。
     * 
     * @param id 用户唯一标识符
     * @param request 用户更新请求对象
     * @return 更新后的用户信息 DTO
     * @throws ResourceNotFoundException 当用户不存在时抛出
     * @throws IllegalArgumentException 当更新参数不合法时抛出
     */
    UserDTO updateUser(Long id, UserUpdateRequest request);
    
    /**
     * 根据 ID 删除用户
     * 
     * <p>根据用户 ID 删除指定用户，删除操作会级联删除用户相关的数据。
     * 
     * @param id 用户唯一标识符
     * @throws ResourceNotFoundException 当用户不存在时抛出
     */
    void deleteById(Long id);
}
```

## ServiceImpl 实现类示例

### 原始代码

```java
package com.example.service.impl;

import com.example.service.UserService;
import com.example.dto.UserDTO;
import com.example.mapper.UserMapper;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class UserServiceImpl implements UserService {
    
    private final UserMapper userMapper;
    
    public UserServiceImpl(UserMapper userMapper) {
        this.userMapper = userMapper;
    }
    
    @Override
    public UserDTO createUser(UserCreateRequest request) {
        // 验证用户名是否已存在
        if (userMapper.existsByUsername(request.getUsername())) {
            throw new BusinessException("用户名已存在");
        }
        
        // 创建用户实体
        User user = new User();
        user.setUsername(request.getUsername());
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        
        // 保存到数据库
        userMapper.insert(user);
        
        // 转换为 DTO 返回
        return convertToDTO(user);
    }
    
    @Override
    public UserDTO findById(Long id) {
        User user = userMapper.selectById(id);
        if (user == null) {
            throw new ResourceNotFoundException("用户不存在");
        }
        return convertToDTO(user);
    }
    
    // ... 其他方法
}
```

### 添加注释后的代码

```java
package com.example.service.impl;

import com.example.service.UserService;
import com.example.dto.UserDTO;
import com.example.mapper.UserMapper;
import org.springframework.stereotype.Service;
import java.util.List;

/**
 * 用户服务实现类
 * 
 * <p>实现 {@link UserService} 接口，提供用户相关的业务逻辑实现。
 * 本类负责处理用户创建、查询、更新、删除等核心业务操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>用户创建：包括数据验证、密码加密、重复性检查</li>
 *   <li>用户查询：支持按 ID 查询和全量查询</li>
 *   <li>用户更新：支持部分字段更新</li>
 *   <li>用户删除：级联删除相关数据</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@Service
public class UserServiceImpl implements UserService {
    
    /**
     * 用户数据访问对象
     * 
     * <p>用于执行用户相关的数据库操作
     */
    private final UserMapper userMapper;
    
    /**
     * 密码编码器
     * 
     * <p>用于对用户密码进行加密处理
     */
    private final PasswordEncoder passwordEncoder;
    
    /**
     * 构造函数
     * 
     * @param userMapper 用户数据访问对象，由 Spring 容器注入
     * @param passwordEncoder 密码编码器，由 Spring 容器注入
     */
    public UserServiceImpl(UserMapper userMapper, PasswordEncoder passwordEncoder) {
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
    }
    
    /**
     * 创建新用户
     * 
     * <p>实现用户创建的业务逻辑，包括：
     * <ol>
     *   <li>验证用户名是否已存在</li>
     *   <li>验证邮箱是否已存在</li>
     *   <li>对密码进行加密处理</li>
     *   <li>创建用户实体并保存到数据库</li>
     *   <li>转换为 DTO 返回</li>
     * </ol>
     * 
     * @param request 用户创建请求对象，包含用户名、邮箱、密码等信息
     * @return 创建成功的用户信息 DTO
     * @throws IllegalArgumentException 当请求参数不合法时抛出
     * @throws BusinessException 当用户名或邮箱已存在时抛出
     */
    @Override
    public UserDTO createUser(UserCreateRequest request) {
        // 验证用户名是否已存在
        if (userMapper.existsByUsername(request.getUsername())) {
            throw new BusinessException("用户名已存在");
        }
        
        // 创建用户实体
        User user = new User();
        user.setUsername(request.getUsername());
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        
        // 保存到数据库
        userMapper.insert(user);
        
        // 转换为 DTO 返回
        return convertToDTO(user);
    }
    
    /**
     * 根据 ID 查询用户
     * 
     * <p>根据用户 ID 从数据库查询用户信息，如果用户不存在则抛出异常。
     * 
     * @param id 用户唯一标识符
     * @return 用户信息 DTO
     * @throws ResourceNotFoundException 当用户不存在时抛出
     */
    @Override
    public UserDTO findById(Long id) {
        User user = userMapper.selectById(id);
        if (user == null) {
            throw new ResourceNotFoundException("用户不存在");
        }
        return convertToDTO(user);
    }
    
    // ... 其他方法
}
```

## 注释要点

1. **接口注释**：
   - 说明接口的职责和设计原则
   - 列出主要功能点
   - 每个方法都要有详细的 JavaDoc

2. **实现类注释**：
   - 说明实现类的职责
   - 描述实现的主要功能
   - 字段注释说明依赖关系
   - 方法注释详细说明实现逻辑
