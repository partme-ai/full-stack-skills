# 用户服务完整 API 设计案例

> 用户限界上下文（User BC）的 REST API 设计，展示注册、登录、资料管理等典型 CQRS 场景。

## 领域模型

```
User (Aggregate Root)
├── UserId (ValueObject)
├── Email (ValueObject)
├── PasswordHash (ValueObject)
├── UserProfile (ValueObject)
│   ├── Nickname
│   ├── Avatar
│   └── Phone
└── UserStatus: ACTIVE / SUSPENDED / DELETED
```

## 1. CQRS 端点设计

### 命令端点（写）

```
POST   /api/v1/users/register           → 用户注册
POST   /api/v1/users/login              → 用户登录
PUT    /api/v1/users/profile            → 更新资料
PUT    /api/v1/users/password           → 修改密码
DELETE /api/v1/users/{userId}           → 注销账号
POST   /api/v1/users/password/reset     → 重置密码（发送邮件）
```

### 查询端点（读）

```
GET    /api/v1/users/me                 → 当前用户信息
GET    /api/v1/users/{userId}           → 指定用户信息（公开）
```

## 2. 数据对象转换链

```
UserPO ↔ User(UserDO) ↔ UserDTO ↔ UserProfileVO
```

### PO

```java
@Entity
@Table(name = "users")
public class UserPO {
    @Id
    private Long id;
    private String email;
    private String passwordHash;
    private String nickname;
    private String avatar;
    private String phone;
    private String status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
```

### DO

```java
public class User extends AggregateRoot<UserId> {
    private UserId id;
    private Email email;
    private PasswordHash passwordHash;
    private UserProfile profile;
    private UserStatus status;

    public static User register(Email email, PasswordHash passwordHash) {
        User user = new User(UserId.generate(), email, passwordHash);
        user.addDomainEvent(new UserRegisteredEvent(user.id, user.email));
        return user;
    }

    public void updateProfile(UserProfile newProfile) {
        this.profile = newProfile;
        addDomainEvent(new UserProfileUpdatedEvent(this.id));
    }

    public void changePassword(PasswordHash oldPwd, PasswordHash newPwd) {
        if (!this.passwordHash.matches(oldPwd)) {
            throw new BusinessException(40101, "原密码不正确");
        }
        this.passwordHash = newPwd;
        addDomainEvent(new UserPasswordChangedEvent(this.id));
    }
}
```

### DTO

```java
// 注册命令 DTO
public record RegisterRequest(
    @Email String email,
    @NotBlank @Size(min = 6, max = 32) String password,
    @NotBlank String nickname
) {
    public RegisterCommand toCommand() {
        return new RegisterCommand(Email.of(email), PasswordHash.encode(password), nickname);
    }
}

// 登录命令 DTO
public record LoginRequest(
    @Email String email,
    @NotBlank String password
) {}

// 查询 DTO
public record UserDetailDTO(
    String userId,
    String email,
    String nickname,
    String avatar,
    String status,
    String createdAt
) {}
```

### VO（前端视图）

```json
{
  "userId": "USR-2024-001",
  "nickname": "张三",
  "avatar": "https://cdn.example.com/avatars/001.jpg",
  "isVerified": true,
  "memberSince": "2024-01-15",
  "settings": {
    "notifications": true,
    "language": "zh-CN"
  }
}
```

## 3. 转换器

```java
public class UserAssembler {
    // DO → DTO
    public static UserDetailDTO toDetailDTO(User user) {
        return new UserDetailDTO(
            user.getId().getValue(),
            user.getEmail().getValue(),
            user.getProfile().getNickname(),
            user.getProfile().getAvatar(),
            user.getStatus().name(),
            user.getCreatedAt().toString()
        );
    }

    // DO → 登录响应
    public static LoginResponse toLoginResponse(User user, String token) {
        return new LoginResponse(
            token,
            toDetailDTO(user)
        );
    }
}
```

## 4. 统一响应

```json
// 注册成功
POST /api/v1/users/register → 201
{
  "code": 0,
  "message": "success",
  "data": {
    "userId": "USR-2024-001",
    "email": "zhang@example.com"
  }
}

// 登录成功
POST /api/v1/users/login → 200
{
  "code": 0,
  "message": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "expiresIn": 3600,
    "user": {
      "userId": "USR-2024-001",
      "nickname": "张三",
      "avatar": "https://cdn.example.com/avatars/001.jpg"
    }
  }
}

// 邮箱已注册
POST /api/v1/users/register → 409
{
  "code": 40901,
  "message": "该邮箱已被注册",
  "requestId": "req-xyz789"
}
```

## 5. 安全设计

| 端点 | 认证 | 限流 | 备注 |
|------|------|------|------|
| POST /register | 无 | 5/min/IP | 防恶意注册 |
| POST /login | 无 | 10/min/IP | 防暴力破解 |
| POST /password/reset | 无 | 3/min/IP | 防滥用 |
| PUT /profile | JWT | 30/min/user | — |
| GET /users/me | JWT | 100/min/user | — |
| DELETE /users/{userId} | JWT+资源所有权检查 | 5/min/user | — |
