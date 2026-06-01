# 自定义网络：多容器 DNS 互通

```bash
# 创建自定义 bridge 网络
docker network create --driver bridge myapp-net

# 运行数据库
docker run -d --name db \
  --network myapp-net \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.4

# 运行应用（通过服务名 db 连接数据库）
docker run -d --name api \
  --network myapp-net \
  -p 8080:8080 \
  -e DB_HOST=db \
  -e DB_PORT=3306 \
  myapp:latest

# 验证 DNS 解析
docker exec api ping db
docker exec api nslookup db   # 返回 db 容器的 IP
```

## 动态连接/断开网络

```bash
# 运行时不指定网络
docker run -d --name redis redis:7-alpine

# 动态连接到网络
docker network connect myapp-net redis

# 断开
docker network disconnect myapp-net redis
```

## 查看网络详情

```bash
docker network ls
docker network inspect myapp-net

# 输出：
# {
#   "Containers": {
#     "abc...": { "Name": "db", "IPv4Address": "172.18.0.2/16" },
#     "def...": { "Name": "api", "IPv4Address": "172.18.0.3/16" }
#   }
# }
```
```

