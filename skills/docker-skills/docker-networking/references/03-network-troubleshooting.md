# 网络排查四步诊断法

## 步骤 1：inspect 收集信息

```bash
# 查看容器网络配置
docker inspect --format='{{json .NetworkSettings.Networks}}' web | jq .

# 查看网关和 IP
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{.Gateway}}{{end}}' web

# 查看 DNS 配置
docker exec web cat /etc/resolv.conf
```

## 步骤 2：连通性测试

```bash
# 容器间 ping
docker exec web ping api

# 端口测试
docker exec web nc -zv db 3306

# DNS 解析
docker exec web nslookup api
docker exec web nslookup api.myapp-net   # 完整域名
```

## 步骤 3：iptables 检查

```bash
# 查看 NAT 规则（端口映射）
sudo iptables -t nat -L DOCKER -n

# 查看 FORWARD 规则
sudo iptables -L DOCKER-USER -n
```

## 步骤 4：抓包分析

```bash
# 抓取容器网卡流量
docker run --rm --net container:web nicolaka/netshoot \
  tcpdump -i eth0 port 80
```

## 常见问题速查

| 症状 | 可能原因 | 解决 |
|------|------|------|
| 容器间 ping 通但端口不通 | 防火墙/应用未监听 0.0.0.0 | `netstat -tlnp` 检查监听地址 |
| 服务名无法解析 | 未加入同一自定义网络 | `docker network connect` |
| `localhost` 访问失败 | 容器中 localhost=本容器 | 使用 `host.docker.internal` 或服务名 |
| 端口映射无效 | 端口已被占用或被防火墙拦截 | `lsof -i :PORT` 检查 |
| 容器无法出网 | IP forwarding 未开启 | `sysctl net.ipv4.ip_forward=1` |
| Docker DNS 失败 | `/etc/resolv.conf` 被覆盖 | 使用 `--dns` 参数指定 |
| 跨主机不通 | overlay 网络未配置 | 检查 Swarm 网络状态 |
```

