# Redis 缓存使用示例

## 1. Cache-Aside 模式 (Java + Spring Boot)

```java
@Service
public class UserService {
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;
    @Autowired
    private UserMapper userMapper;

    public User getUserById(Long id) {
        String key = "user:" + id;
        // 1. 尝试从缓存获取
        User user = (User) redisTemplate.opsForValue().get(key);
        if (user != null) {
            return user;
        }
        // 2. 缓存未命中，查数据库
        user = userMapper.selectById(id);
        if (user != null) {
            // 3. 写入缓存，设置 TTL
            redisTemplate.opsForValue().set(key, user, 1, TimeUnit.HOURS);
        }
        return user;
    }

    public void updateUser(User user) {
        // 1. 更新数据库
        userMapper.updateById(user);
        // 2. 删除缓存 (下次读取时重建)
        redisTemplate.delete("user:" + user.getId());
    }
}
```

## 2. 分布式锁 (Python + redis-py)

```python
import redis
import uuid
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def acquire_lock(lock_name, acquire_timeout=10, lock_timeout=30):
    """获取分布式锁"""
    identifier = str(uuid.uuid4())
    lock_key = f"lock:{lock_name}"
    end = time.time() + acquire_timeout

    while time.time() < end:
        if r.set(lock_key, identifier, nx=True, ex=lock_timeout):
            return identifier  # 成功获取锁
        time.sleep(0.01)  # 短暂休眠后重试
    return None  # 超时未获取

def release_lock(lock_name, identifier):
    """释放分布式锁 (Lua 脚本保证原子性)"""
    lock_key = f"lock:{lock_name}"
    lua_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end
    """
    return r.eval(lua_script, 1, lock_key, identifier)

# 使用示例
lock_id = acquire_lock("order:1001")
if lock_id:
    try:
        print("处理订单 1001...")
        # 执行业务逻辑
    finally:
        release_lock("order:1001", lock_id)
```

## 3. 限流器 (Node.js)

```javascript
const Redis = require('ioredis');
const redis = new Redis();

async function rateLimit(ip, limit = 100, window = 60) {
    const key = `ratelimit:${ip}`;
    const current = await redis.incr(key);
    if (current === 1) {
        await redis.expire(key, window);
    }
    return current <= limit;
}

// 使用: 每个 IP 每分钟最多 100 次请求
app.use(async (req, res, next) => {
    const allowed = await rateLimit(req.ip);
    if (!allowed) {
        return res.status(429).json({ error: '请求过于频繁' });
    }
    next();
});
```
