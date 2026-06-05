# Redis Session 存储示例

## 1. Spring Session + Redis

```xml
<!-- pom.xml 依赖 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.session</groupId>
    <artifactId>spring-session-data-redis</artifactId>
</dependency>
```

```yaml
# application.yml
spring:
  session:
    store-type: redis
    timeout: 1800  # Session 过期时间 (秒)
  redis:
    host: localhost
    port: 6379
    password: your_password
    timeout: 2000ms
    lettuce:
      pool:
        max-active: 50
        max-idle: 20
        min-idle: 5
```

```java
@Configuration
@EnableRedisHttpSession(maxInactiveIntervalInSeconds = 1800)
public class RedisSessionConfig {
    // 自动生效，无需额外代码
}
```

## 2. Flask Session (Python)

```python
from flask import Flask, session
from flask_session import Session
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379/0')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'session:'
app.config['SESSION_PERMANENT_TIMEOUT'] = 1800

Session(app)

@app.route('/login')
def login():
    session['user_id'] = 1001
    session['role'] = 'admin'
    return 'Session stored in Redis'

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    role = session.get('role')
    return f'User {user_id} with role {role}'
```
