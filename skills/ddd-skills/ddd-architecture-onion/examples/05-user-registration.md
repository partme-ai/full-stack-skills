# Example 5: 用户注册 + 邮件验证（User Registration）

展示洋葱架构下用户注册功能的完整实现，包含邮件验证流程。

## 业务场景

用户通过邮箱注册账号，系统发送验证邮件，用户点击链接完成激活。

## 目录结构

```
user-registration/
├── core/domain/                        # Domain 层（零框架依赖）
│   ├── model/
│   │   ├── User.java                   # 聚合根
│   │   ├── UserId.java                 # 值对象
│   │   ├── Email.java                  # 值对象（含格式校验）
│   │   └── Password.java               # 值对象（含强度校验）
│   ├── service/
│   │   └── PasswordEncryption.java     # 领域服务接口
│   ├── repository/
│   │   └── UserRepository.java         # 仓储接口
│   └── event/
│       └── UserRegisteredEvent.java    # 领域事件
├── core/application/                   # Application 层
│   └── service/
│       ├── RegisterUserUseCase.java    # 应用服务接口
│       └── impl/
│           └── RegisterUserService.java # 编排实现
├── infrastructure/                     # Infrastructure 层
│   ├── data/
│   │   ├── entity/
│   │   │   └── UserPO.java            # JPA 持久化对象
│   │   ├── repository/
│   │   │   └── UserRepositoryImpl.java
│   │   └── mapper/
│   │       └── UserMapper.java         # PO ↔ Domain 映射
│   └── email/
│       └── SmtpEmailSender.java        # 邮件发送实现
├── api/                                # API 适配层
│   ├── controller/
│   │   └── RegistrationController.java
│   ├── dto/
│   │   ├── request/
│   │   │   └── RegisterRequest.java
│   │   └── response/
│   │       └── RegisterResponse.java
│   └── assembler/
│       └── UserAssembler.java
└── composition/                        # DI 组装层
    └── config/
        └── UserRegistrationConfig.java
```

## 关键代码

### Domain 层：值对象（不可变）

```java
// core/domain/model/Email.java
public final class Email {
    private final String value;

    public Email(String value) {
        if (value == null || !value.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            throw new IllegalArgumentException("Invalid email format");
        }
        this.value = value;
    }

    public String getValue() { return value; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Email)) return false;
        Email email = (Email) o;
        return value.equals(email.value);
    }

    @Override
    public int hashCode() { return value.hashCode(); }
}
```

### Domain 层：聚合根

```java
// core/domain/model/User.java
public class User {
    private final UserId userId;
    private final Email email;
    private Password password;
    private boolean isActive;
    private final List<DomainEvent> domainEvents = new ArrayList<>();

    public static User register(Email email, Password password, PasswordEncryption encryptor) {
        User user = new User(UserId.generate(), email, encryptor.encode(password));
        user.isActive = false;
        user.addDomainEvent(new UserRegisteredEvent(user.userId, user.email));
        return user;
    }

    public void activate() {
        if (isActive) throw new IllegalStateException("User already active");
        this.isActive = true;
    }

    public void addDomainEvent(DomainEvent event) {
        domainEvents.add(event);
    }

    public List<DomainEvent> getDomainEvents() {
        return Collections.unmodifiableList(domainEvents);
    }

    public void clearDomainEvents() {
        domainEvents.clear();
    }
}
```

### Domain 层：仓储接口

```java
// core/domain/repository/UserRepository.java
public interface UserRepository {
    Optional<User> findByEmail(Email email);
    Optional<User> findById(UserId id);
    void save(User user);
    boolean existsByEmail(Email email);
}
```

### Application 层：编排实现

```java
// core/application/service/impl/RegisterUserService.java
@Service
@Transactional
public class RegisterUserService implements RegisterUserUseCase {
    private final UserRepository userRepo;
    private final PasswordEncryption encryptor;
    private final EmailSender emailSender;

    public RegisterUserService(UserRepository userRepo,
                                PasswordEncryption encryptor,
                                EmailSender emailSender) {
        this.userRepo = userRepo;
        this.encryptor = encryptor;
        this.emailSender = emailSender;
    }

    public RegisterResult execute(RegisterCommand cmd) {
        // Application 层只编排，不包含业务逻辑
        Email email = new Email(cmd.getEmail());
        Password password = new Password(cmd.getPassword());

        if (userRepo.existsByEmail(email)) {
            throw new DuplicateEmailException(email);
        }

        User user = User.register(email, password, encryptor);
        userRepo.save(user);

        // 发布领域事件（由 Infrastructure 的 EventPublisher 处理）
        user.getDomainEvents().forEach(event -> {
            if (event instanceof UserRegisteredEvent) {
                emailSender.sendVerificationEmail(
                    ((UserRegisteredEvent) event).getEmail(),
                    generateVerificationLink(((UserRegisteredEvent) event).getUserId())
                );
            }
        });
        user.clearDomainEvents();

        return new RegisterResult(user.getUserId().getValue(), false);
    }
}
```

### Infrastructure 层：仓储实现

```java
// infrastructure/data/repository/UserRepositoryImpl.java
@Repository
public class UserRepositoryImpl implements UserRepository {
    private final JpaUserRepository jpaRepo;   // Spring Data JPA
    private final UserMapper mapper;

    @Override
    public Optional<User> findByEmail(Email email) {
        return jpaRepo.findByEmail(email.getValue())
            .map(mapper::toDomain);
    }

    @Override
    public void save(User user) {
        UserPO po = mapper.toPO(user);
        jpaRepo.save(po);
    }
}
```

### API 层：Controller

```java
// api/controller/RegistrationController.java
@RestController
@RequestMapping("/api/users")
public class RegistrationController {
    private final RegisterUserUseCase registerUseCase;

    @PostMapping("/register")
    public ResponseEntity<RegisterResponse> register(@Valid @RequestBody RegisterRequest request) {
        RegisterCommand cmd = UserAssembler.toCommand(request);
        RegisterResult result = registerUseCase.execute(cmd);
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(UserAssembler.toResponse(result));
    }

    @PostMapping("/verify")
    public ResponseEntity<Void> verify(@RequestParam String token) {
        verifyUseCase.execute(new VerifyCommand(token));
        return ResponseEntity.ok().build();
    }
}
```

## 洋葱架构合规检查

| 检查项 | 合规状态 |
|--------|---------|
| Domain 层无框架 import | ✅ 合格（纯 Java） |
| Repository 接口定义在 Domain | ✅ 合格（UserRepository 在 domain/repository） |
| Repository 实现在 Infrastructure | ✅ 合格（UserRepositoryImpl 在 infrastructure） |
| Application 层只编排无业务逻辑 | ✅ 合格（RegisterUserService 仅协调） |
| 值对象不可变 | ✅ 合格（Email/Password 均为 final） |
| DTO 在 API 层定义 | ✅ 合格（RegisterRequest/Response 在 api/dto） |
| DI 集中在 composition 模块 | ✅ 合格（UserRegistrationConfig） |
