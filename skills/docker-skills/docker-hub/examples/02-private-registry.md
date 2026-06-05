# 私有仓库搭建

## Docker Registry（最简单）

```yaml
# compose.yml
services:
  registry:
    image: registry:2.8
    ports:
      - "5000:5000"
    volumes:
      - registry_data:/var/lib/registry
    environment:
      REGISTRY_STORAGE_DELETE_ENABLED: "true"
    restart: unless-stopped

volumes:
  registry_data:
```

```bash
docker compose up -d
docker tag myapp localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1
```

## Registry + 认证

```bash
# 创建 htpasswd
docker run --rm httpd:alpine htpasswd -Bbn admin password > htpasswd
```

```yaml
services:
  registry:
    image: registry:2.8
    ports:
      - "5000:5000"
    volumes:
      - registry_data:/var/lib/registry
      - ./htpasswd:/auth/htpasswd:ro
      - ./certs:/certs:ro
    environment:
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry Realm
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
      REGISTRY_HTTP_TLS_CERTIFICATE: /certs/registry.crt
      REGISTRY_HTTP_TLS_KEY: /certs/registry.key
```

## Harbor（企业方案）

```bash
# 下载 Harbor
wget https://github.com/goharbor/harbor/releases/download/v2.12.0/harbor-online-installer-v2.12.0.tgz
tar xzf harbor-online-installer-v2.12.0.tgz
cd harbor

# 配置
cp harbor.yml.tmpl harbor.yml
# 编辑 harbor.yml：设置 hostname、密码、证书路径

# 安装
./install.sh --with-trivy    # 含漏洞扫描
```

Harbor 提供：
- Web UI 管理
- 漏洞扫描（Trivy 集成）
- 镜像复制（跨数据中心同步）
- RBAC 权限
- 垃圾回收与配额管理

## 镜像清理策略

```bash
# Docker Registry 垃圾回收
docker exec registry bin/registry garbage-collect /etc/docker/registry/config.yml

# Harbor 清理策略（Web UI 配置）
# Administration → Cleanup → 设置保留策略（保留最近 N 个 tag、保留时间）
```

## Registry Mirror 加速

```json
// /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://mirror.gcr.io",
    "https://hub-mirror.c.163.com"
  ]
}
```
```

