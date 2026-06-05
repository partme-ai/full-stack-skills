# docker run 基础使用

```bash
# 基本运行
docker run nginx:alpine                        # 前台运行

# 后台运行 + 命名
docker run -d --name web nginx:alpine          # -d 后台, --name 命名

# 端口映射
docker run -d -p 8080:80 nginx:alpine          # host:container
docker run -d -p 127.0.0.1:8080:80 nginx:alpine # 仅 localhost
docker run -d -p 8080:80/udp nginx:alpine       # UDP

# 卷挂载
docker run -d -v /data:/var/lib/mysql mysql:8.4        # bind mount
docker run -d -v myvolume:/data alpine                  # named volume
docker run -d -v /var/run/docker.sock:/var/run/docker.sock ...

# 环境变量
docker run -d -e NODE_ENV=production -e PORT=3000 node:22-alpine
docker run -d --env-file .env myapp

# 重启策略
docker run -d --restart always nginx:alpine
docker run -d --restart on-failure:5 myapp
docker run -d --restart unless-stopped myapp

# 资源限制
docker run -d --memory 512m --cpus 1.0 myapp
docker run -d --memory 256m --memory-swap 512m myapp

# 常用组合
docker run -d \
  --name myapp \
  --restart unless-stopped \
  -p 8080:8080 \
  -v app_data:/data \
  -e NODE_ENV=production \
  --memory 512m --cpus 0.5 \
  myapp:latest

# 容器管理
docker ps                     # 运行中
docker ps -a                  # 全部
docker logs -f myapp          # 跟踪日志
docker logs --tail 50 myapp   # 最后 50 行
docker exec -it myapp sh      # 进入容器
docker stop myapp             # 停止
docker start myapp            # 启动已停止的
docker restart myapp          # 重启
docker rm myapp               # 删除
docker rm -f myapp            # 强制删除
```
```

