# docker run 完整参数速查

## 容器生命周期

| 命令 | 说明 |
|------|------|
| `docker create` | 创建但不启动 |
| `docker start` | 启动已创建的容器 |
| `docker run` | create + start |
| `docker stop` | 优雅停止（SIGTERM→SIGKILL） |
| `docker kill` | 立即停止（SIGKILL） |
| `docker restart` | stop + start |
| `docker pause/unpause` | 暂停/恢复（cgroup freezer） |
| `docker rm` | 删除已停止容器 |
| `docker rm -f` | 强制删除（运行中也删） |

## docker run 完整参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-d, --detach` | 后台运行 | `-d` |
| `--name` | 容器名称 | `--name web` |
| `-p, --publish` | 端口映射 | `-p 8080:80` |
| `-P` | 映射所有 EXPOSE 端口（随机） | `-P` |
| `-v, --volume` | 卷挂载 | `-v /host:/container:ro` |
| `--mount` | 更详细的挂载语法 | `--mount type=bind,src=...` |
| `-e, --env` | 环境变量 | `-e NODE_ENV=prod` |
| `--env-file` | 从文件加载环境变量 | `--env-file .env` |
| `-w, --workdir` | 工作目录 | `-w /app` |
| `-u, --user` | 运行用户 | `-u 1000:1000` |
| `--restart` | 重启策略 | `--restart unless-stopped` |
| `--memory` | 内存限制 | `--memory 512m` |
| `--cpus` | CPU 限制 | `--cpus 1.5` |
| `--network` | 网络 | `--network mynet` |
| `--hostname` | 主机名 | `--hostname app1` |
| `--add-host` | 添加 hosts 条目 | `--add-host db:192.168.1.100` |
| `--dns` | DNS 服务器 | `--dns 8.8.8.8` |
| `--link` | 链接容器（已废弃） | `--link redis:redis` |
| `--rm` | 退出后自动删除 | `--rm` |
| `-i, --interactive` | 保持 STDIN 打开 | `-i` |
| `-t, --tty` | 分配伪终端 | `-t` |
| `--read-only` | 根文件系统只读 | `--read-only` |
| `--tmpfs` | tmpfs 挂载 | `--tmpfs /tmp:rw,size=128M` |
| `--cap-add/--cap-drop` | 添加/移除 Linux capabilities | `--cap-drop=ALL` |
| `--security-opt` | 安全选项 | `--security-opt no-new-privileges` |
| `--label` | 元数据标签 | `--label env=prod` |
| `--log-driver` | 日志驱动 | `--log-driver json-file` |
| `--log-opt` | 日志驱动选项 | `--log-opt max-size=10m` |
| `--health-cmd` | 覆盖 HEALTHCHECK | `--health-cmd "curl -f localhost"` |
| `--health-interval` | 健康检查间隔 | `--health-interval 30s` |
| `--init` | 使用 init 进程（tini） | `--init` |
| `--privileged` | 特权模式（慎用） | `--privileged` |

## 重启策略

| 策略 | 行为 |
|------|------|
| `no` | 不自动重启（默认） |
| `on-failure[:N]` | 仅退出码非 0 时重启，最多 N 次 |
| `always` | 总是重启（包括 daemon 重启后） |
| `unless-stopped` | 除非手动 stop，否则重启 |
```

