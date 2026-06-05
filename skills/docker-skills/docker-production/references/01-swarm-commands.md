# Docker Swarm 命令速查

## 集群管理

```bash
docker swarm init --advertise-addr eth0
docker swarm join --token SWMTKN-1-xxx 192.168.1.100:2377
docker swarm join-token manager      # 获取 manager token
docker swarm join-token worker       # 获取 worker token
docker swarm leave --force
docker node ls
docker node promote worker-1         # worker 升级为 manager
docker node update --availability drain node-1  # 排空节点
```

## Service 管理

```bash
docker service create --name web --replicas 3 -p 8080:80 nginx:alpine
docker service ls
docker service ps web
docker service logs -f web
docker service scale web=5
docker service update --image nginx:alpine web
docker service update --force web    # 强制重新部署（不换镜像）
docker service rm web
```

## Stack 部署

```bash
docker stack deploy -c compose.yml myapp
docker stack ls
docker stack ps myapp
docker stack services myapp
docker stack rm myapp
```

## 滚动更新

```bash
docker service create \
  --name api \
  --replicas 3 \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-failure-action rollback \
  --update-monitor 30s \
  myapp:v1

docker service update --image myapp:v2 api
```

## 回滚

```bash
docker service rollback api
docker service update --rollback api
```

## 网络

```bash
docker network create --driver overlay mynet
docker service create --network mynet --name api myapp
```

## Secrets & Configs

```bash
echo "secretpass" | docker secret create db_pass -
docker config create nginx_conf ./nginx.conf

docker service create \
  --secret db_pass \
  --config source=nginx_conf,target=/etc/nginx/nginx.conf \
  --name web nginx
```
```

