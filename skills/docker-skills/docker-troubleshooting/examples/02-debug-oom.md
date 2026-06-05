# 容器崩溃调试全过程

## 症状：容器启动后立即退出

```bash
docker run -d --name myapp myapp:latest
docker ps -a | grep myapp
# myapp   Exited (1) 2 seconds ago
```

## 诊断流程

```bash
# Step 1: 查看退出码
docker inspect --format='{{.State.ExitCode}}' myapp
# 退出码速查：
# 0    正常退出
# 1    应用错误
# 126  权限不足（CMD 不可执行）
# 127  命令找不到
# 137  SIGKILL（OOM）
# 139  SIGSEGV（段错误）
# 143  SIGTERM（优雅终止）

# Step 2: 查看日志（即使 Exited 也能看到）
docker logs myapp
docker logs --tail 50 myapp

# Step 3: 检查是否 OOM
docker inspect --format='{{.State.OOMKilled}}' myapp
# true → 内存不足，增加 --memory

# Step 4: 覆盖 CMD 进入调试
docker run -it --rm --entrypoint sh myapp:latest
# 进入后手动运行应用，观察输出

# Step 5: 检查文件权限
docker run -it --rm --entrypoint sh myapp:latest
ls -la /app/entrypoint.sh
# 权限不足 → Dockerfile 加 RUN chmod +x

# Step 6: 检查端口绑定
docker inspect --format='{{.NetworkSettings.IPAddress}}' myapp
# 确认应用监听 0.0.0.0 而不是 127.0.0.1
```

## 常见问题速查

| 症状 | 退出码 | 原因 | 修复 |
|------|:--:|------|------|
| 秒退 | 127 | 命令找不到 | 检查 ENTRYPOINT/CMD 路径 |
| 秒退 | 1 | 应用崩溃 | `docker logs` 查堆栈 |
| 30s 后退 | 137 | OOM Kill | `--memory=512m` 增加限制 |
| 运行但不响应 | 0 | 监听 127.0.0.1 | 改为 0.0.0.0 |
| 启动慢 | - | DNS 超时 | `--dns 8.8.8.8` |
```

