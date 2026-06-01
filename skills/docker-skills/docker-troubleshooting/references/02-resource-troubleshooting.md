# 磁盘与资源问题排查

## 磁盘满

```bash
# 1. 查看使用量
docker system df
# TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
# Images          25        5         12.5GB    8.2GB (65%)
# Containers      8         3         1.2GB     800MB (66%)
# Local Volumes   12        4         3.5GB     2.1GB (60%)

# 2. 详细分析
docker system df -v

# 3. 清理
docker container prune     # 删除已停止容器
docker image prune -a      # 删除未使用镜像
docker volume prune        # 删除未使用卷
docker builder prune       # 清理构建缓存

# 4. 安全清理（保留 24h 内的）
docker system prune --filter "until=24h"

# 5. 检查大文件
docker run --rm -v /var/lib/docker:/docker:ro alpine du -sh /docker/*
```

## 日志膨胀

```bash
# 检查日志大小
docker inspect --format='{{.LogPath}}' myapp | xargs ls -lh

# 限制日志大小
docker run -d --log-opt max-size=10m --log-opt max-file=3 myapp

# Compose 中限制
services:
  app:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

# 清理日志
truncate -s 0 $(docker inspect --format='{{.LogPath}}' myapp)
```

## 容器 CPU 100%

```bash
# 查看资源使用
docker stats --no-stream
docker top myapp

# 限制 CPU
docker update --cpus 0.5 myapp

# 查看进程
docker exec myapp ps aux --sort=-%cpu | head -5
```

## 网络耗时排查

```bash
# DNS 解析
docker exec myapp nslookup api-service

# 延迟测试
docker exec myapp time curl -s http://api-service:8080/health

# 抓包
docker run --rm --net container:myapp nicolaka/netshoot tcpdump -i eth0 -w /tmp/capture.pcap
```

## inode 耗尽

```bash
# 检查 inode
df -i /var/lib/docker

# docker 产生的 inode 大户：overlay2 层、小文件多
# 清理：docker system prune -a
```
```

