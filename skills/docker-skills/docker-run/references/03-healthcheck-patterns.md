# 健康检查模式库

## 内置 HEALTHCHECK

```dockerfile
# HTTP 检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# TCP 检查
HEALTHCHECK --interval=10s --timeout=3s \
    CMD nc -z localhost 3306 || exit 1

# 进程检查
HEALTHCHECK --interval=30s --timeout=3s \
    CMD pgrep nginx || exit 1

# 自定义脚本
HEALTHCHECK --interval=30s --timeout=3s \
    CMD /app/health-check.sh || exit 1
```

## 运行时覆盖

```bash
docker run -d \
  --health-cmd="curl -f http://localhost:8080/health || exit 1" \
  --health-interval=10s \
  --health-timeout=3s \
  --health-start-period=30s \
  --health-retries=3 \
  myapp
```

## 参数说明

| 参数 | 默认 | 说明 |
|------|:--:|------|
| `--interval` | 30s | 检查间隔 |
| `--timeout` | 30s | 单次检查超时 |
| `--start-period` | 0s | 启动宽限期（不计数失败） |
| `--start-interval` | 5s | 启动期间检查间隔（v25+） |
| `--retries` | 3 | 连续失败次数阈值 |

## 状态查看

```bash
docker inspect --format='{{.State.Health.Status}}' myapp
# healthy / unhealthy / starting

docker inspect --format='{{json .State.Health}}' myapp | jq .
```

## 按场景的推荐配置

| 场景 | interval | timeout | retries | start-period |
|------|:--:|:--:|:--:|:--:|
| Web API | 30s | 3s | 3 | 10s |
| 数据库 | 10s | 5s | 5 | 30s |
| 消息队列 | 15s | 5s | 5 | 20s |
| 批处理 | 60s | 10s | 2 | 5s |
| 缓存 | 10s | 3s | 3 | 5s |

## Compose 中依赖健康检查

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy     # 等待 db 健康再启动
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 15s
      timeout: 3s
      retries: 3
```
```

