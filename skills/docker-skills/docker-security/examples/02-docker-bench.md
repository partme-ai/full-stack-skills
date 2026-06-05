# Docker Bench Security 审计

```bash
# 运行审计
docker run --rm \
  --net host \
  --pid host \
  --userns host \
  --cap-add audit_control \
  -v /etc:/etc:ro \
  -v /usr/bin/docker-containerd:/usr/bin/docker-containerd:ro \
  -v /usr/bin/docker-runc:/usr/bin/docker-runc:ro \
  -v /usr/lib/systemd:/usr/lib/systemd:ro \
  -v /var/lib:/var/lib:ro \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  --label docker_bench_security \
  docker/docker-bench-security
```

## 理解输出

```
[WARN] 1.1  - Ensure a separate partition for containers has been created
[PASS] 1.2  - Ensure only trusted users are allowed to control Docker daemon
[INFO] 2.1  - Restrict network traffic between containers
[WARN] 2.5  - Ensure aufs storage driver is not used (when applicable)
[PASS] 4.1  - Ensure that a user for the container has been created
[WARN] 5.12 - Ensure that the container's root filesystem is mounted as read only
```

## 逐条修复

| 检查项 | 问题 | 修复 |
|------|------|------|
| 1.1 | 无独立分区 | 创建 `/var/lib/docker` 独立分区 |
| 2.1 | 容器间网络未限制 | Compose: `internal: true` / `--icc=false` |
| 2.5 | 使用 aufs | 切换到 `overlay2` |
| 4.1 | 容器未使用非 root 用户 | Dockerfile: `USER 1000` |
| 5.12 | rootfs 非只读 | `--read-only --tmpfs /tmp` |
```

