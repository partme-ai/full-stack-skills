# 用户 CQRS — 命令与查询分离

> 用户注册（Command） + 用户查询（Query），L1 级别

```java
// Command
public class RegisterUserCommand {
    private final String username;
    private final String email;
    private final String password;
}

@Service
public class UserCommandService {
    public UserRegisteredResult register(RegisterUserCommand cmd) {
        User user = User.register(cmd);
        userRepository.save(user);
        return UserRegisteredResult.from(user);
    }
}

// Query
@Service
public class UserQueryService {
    public UserProfileDTO getProfile(String userId) {
        return userReadRepo.findProfileById(userId);
    }
}
```
