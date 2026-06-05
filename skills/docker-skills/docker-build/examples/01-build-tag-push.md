# 从零构建并推送镜像

```bash
# 1. 创建项目
mkdir myapp && cd myapp

# 2. 写 Dockerfile
cat > Dockerfile <<'EOF'
FROM nginx:1.27-alpine
COPY index.html /usr/share/nginx/html/
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost/health || exit 1
EOF

echo '<h1>Hello Docker Build</h1>' > index.html

# 3. 构建（多 tag）
docker build -t myapp:v1.0.0 -t myapp:latest .

# 4. 查看
docker images myapp
docker history myapp:v1.0.0
docker inspect --format='{{.Config.Env}}' myapp:v1.0.0

# 5. 运行验证
docker run -d -p 8080:80 --name myapp-test myapp:latest
curl localhost:8080
docker stop myapp-test && docker rm myapp-test

# 6. 推送到仓库
docker login
docker tag myapp:v1.0.0 docker.io/myuser/myapp:v1.0.0
docker push docker.io/myuser/myapp:v1.0.0
docker push docker.io/myuser/myapp:latest
```
```

