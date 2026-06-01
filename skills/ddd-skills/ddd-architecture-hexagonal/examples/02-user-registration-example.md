# Example: 用户注册六边形示例

本示例展示用户注册流程，强调值对象设计、领域事件和端口隔离。

## 值对象

```java
// domain/model/user/Email.java
public final class Email {
    private final String value;

    private Email(String value) {
        if (value == null || !value.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            throw new IllegalArgumentException("无效邮箱: " + value);
        }
        this.value = value.toLowerCase();
    }

    public static Email of(String value) { return new Email(value); }
    public String getValue() { return value; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Email email = (Email) o;
        return value.equals(email.value);
    }
    @Override
    public int hashCode() { return value.hashCode(); }
}

// domain/model/user/PhoneNumber.java
public final class PhoneNumber {
    private final String countryCode;
    private final String number;
    // ... 工厂方法、equals/hashCode
}

// domain/model/user/UserId.java
public final class UserId {
    private final String value;
    // ... 工厂方法
}
```

## 聚合根

```java
// domain/model/user/User.java
public class User extends AggregateRoot<UserId> {
    private UserId id;
    private Email email;
    private PhoneNumber phone;
    private UserStatus status;
    private LocalDateTime registeredAt;

    protected User() {}

    public static User register(Email email, PhoneNumber phone) {
        User user = new User();
        user.id = UserId.generate();
        user.email = email;
        user.phone = phone;
        user.status = UserStatus.ACTIVE;
        user.registeredAt = LocalDateTime.now();
        user.addDomainEvent(new UserRegisteredEvent(user.id, user.email));
        return user;
    }

    public void deactivate(String reason) {
        if (status != UserStatus.ACTIVE) throw new UserException("用户已非激活状态");
        this.status = UserStatus.INACTIVE;
        addDomainEvent(new UserDeactivatedEvent(this.id, reason));
    }

    public void changeEmail(Email newEmail) {
        if (newEmail.equals(this.email)) return;
        this.email = newEmail;
        addDomainEvent(new UserEmailChangedEvent(this.id, newEmail));
    }

    public UserId getId() { return id; }
    public Email getEmail() { return email; }
    public UserStatus getStatus() { return status; }
}
```

## 端口定义

```java
// domain/port/inbound/RegisterUserUseCase.java
public interface RegisterUserUseCase {
    UserRegisteredResult execute(RegisterUserCommand command);
}

// domain/port/inbound/GetUserUseCase.java
public interface GetUserUseCase {
    UserDTO execute(GetUserQuery query);
}

// domain/port/outbound/UserRepository.java
public interface UserRepository {
    Optional<User> findById(UserId id);
    Optional<User> findByEmail(Email email);
    void save(User user);
    boolean existsByEmail(Email email);
}

// domain/port/outbound/VerificationCodePort.java
public interface VerificationCodePort {
    void sendCode(Email email, String code);
    boolean verify(Email email, String code);
}

// domain/port/outbound/NotificationPort.java
public interface NotificationPort {
    void sendWelcomeEmail(Email email, String userName);
}
```

## 应用服务

```java
// application/service/RegisterUserService.java
@ApplicationService
public class RegisterUserService implements RegisterUserUseCase {
    private final UserRepository userRepository;
    private final VerificationCodePort verificationCode;
    private final NotificationPort notification;
    private final EventPublisher eventPublisher;

    public RegisterUserService(UserRepository userRepository,
                               VerificationCodePort verificationCode,
                               NotificationPort notification,
                               EventPublisher eventPublisher) {
        this.userRepository = userRepository;
        this.verificationCode = verificationCode;
        this.notification = notification;
        this.eventPublisher = eventPublisher;
    }

    @Override
    @Transactional
    public UserRegisteredResult execute(RegisterUserCommand command) {
        Email email = Email.of(command.getEmail());

        // 1. 校验邮箱唯一性
        if (userRepository.existsByEmail(email)) {
            throw new EmailAlreadyExistsException(email);
        }

        // 2. 校验验证码
        if (!verificationCode.verify(email, command.getCode())) {
            throw new VerificationCodeException("验证码错误或已过期");
        }

        // 3. 创建用户聚合
        User user = User.register(email, PhoneNumber.of(command.getPhone()));

        // 4. 持久化
        userRepository.save(user);

        // 5. 发送欢迎通知
        notification.sendWelcomeEmail(user.getEmail(), email.getValue());

        // 6. 发布事件
        eventPublisher.publishAll(user.getDomainEvents());

        return UserRegisteredResult.from(user);
    }
}
```

## 主适配器

```java
// adapter/inbound/web/UserController.java
@RestController
@RequestMapping("/api/v1/users")
public class UserController {
    private final RegisterUserUseCase registerUser;
    private final GetUserUseCase getUser;

    @PostMapping("/register")
    public ResponseEntity<UserRegisteredResponse> register(
            @RequestBody @Valid RegisterUserRequest request) {
        var result = registerUser.execute(request.toCommand());
        return ResponseEntity.status(201).body(UserRegisteredResponse.from(result));
    }

    @PostMapping("/send-code")
    public ResponseEntity<Void> sendVerificationCode(@RequestBody @Valid SendCodeRequest request) {
        verificationCodePort.sendCode(Email.of(request.getEmail()), generateCode());
        return ResponseEntity.ok().build();
    }

    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> get(@PathVariable String id) {
        var user = getUser.execute(new GetUserQuery(id));
        if (user == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(user);
    }
}
```

## 次适配器

```java
// adapter/outbound/persistence/JpaUserRepository.java
@Repository
public class JpaUserRepository implements UserRepository {
    private final SpringDataUserRepository jpaRepo;
    private final UserMapper mapper;

    @Override
    public Optional<User> findById(UserId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }

    @Override
    public Optional<User> findByEmail(Email email) {
        return jpaRepo.findByEmail(email.getValue()).map(mapper::toDomain);
    }

    @Override
    public boolean existsByEmail(Email email) {
        return jpaRepo.existsByEmail(email.getValue());
    }

    @Override
    public void save(User user) {
        jpaRepo.save(mapper.toPO(user));
    }
}

// adapter/outbound/external/AliyunSmsVerificationCode.java
@Component
public class AliyunSmsVerificationCode implements VerificationCodePort {
    private final RedisTemplate<String, String> redis;

    @Override
    public void sendCode(Email email, String code) {
        redis.opsForValue().set("vc:" + email.getValue(), code, Duration.ofMinutes(5));
        // 实际发送短信...
    }

    @Override
    public boolean verify(Email email, String code) {
        String stored = redis.opsForValue().get("vc:" + email.getValue());
        return code.equals(stored);
    }
}
```

## 测试

```java
// 应用层测试
@Test
void should_register_user_successfully() {
    var userRepo = mock(UserRepository.class);
    var vcPort = mock(VerificationCodePort.class);
    var notif = mock(NotificationPort.class);
    var eventPub = mock(EventPublisher.class);
    var service = new RegisterUserService(userRepo, vcPort, notif, eventPub);

    when(userRepo.existsByEmail(any())).thenReturn(false);
    when(vcPort.verify(any(), any())).thenReturn(true);

    var cmd = new RegisterUserCommand("test@example.com", "13800138000", "123456");
    var result = service.execute(cmd);

    assertNotNull(result.getUserId());
    verify(userRepo).save(any(User.class));
    verify(notif).sendWelcomeEmail(any(), any());
    verify(eventPub).publishAll(anyList());
}
```

## 数据流转

```
POST /api/v1/users/register
  │  JSON → RegisterUserCommand
  ▼
RegisterUserService.execute()       ← 应用服务
  │  userRepository.existsByEmail() ← 出站端口
  │  verificationCode.verify()      ← 出站端口
  │  User.register()                ← 领域模型
  │  userRepository.save()          ← 出站端口
  │  notification.sendWelcomeEmail()← 出站端口
  ▼
JpaUserRepository.save()            ← 次适配器
AliyunSmsVerificationCode.verify()  ← 次适配器
SendGridNotification.send()         ← 次适配器
```
