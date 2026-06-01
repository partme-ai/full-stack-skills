# BuildKit 密钥挂载：避免泄露到镜像层

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm install --registry=https://private-registry.com
```

```bash
# 文件挂载
docker buildx build --secret id=npmrc,src=$HOME/.npmrc -t myapp .
# 环境变量
echo "$NPM_TOKEN" | docker buildx build --secret id=npmrc,src=/dev/stdin -t myapp .
```

## 常见场景

| 场景 | 密钥文件 | target |
|------|---------|--------|
| npm 私有仓库 | .npmrc | /root/.npmrc |
| Maven 私有仓库 | settings.xml | /root/.m2/settings.xml |
| pip 私有仓库 | .pypirc 或 PIP_INDEX_URL | env |
| AWS 凭证 | ~/.aws/credentials | /root/.aws/credentials |
| Git 凭证 | .git-credentials | /root/.git-credentials |
```

