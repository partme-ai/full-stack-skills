# 构建参数与环境区分

## Dockerfile

```dockerfile
ARG NODE_VERSION=22
FROM node:${NODE_VERSION}-alpine

ARG APP_ENV=development
ENV NODE_ENV=${APP_ENV}

WORKDIR /app
COPY package*.json ./

# dev 装全部依赖，prod 仅生产依赖
RUN if [ "$APP_ENV" = "production" ]; then npm ci --production; else npm install; fi

COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

## 构建命令

```bash
# 开发构建
docker build \
  --build-arg NODE_VERSION=22 \
  --build-arg APP_ENV=development \
  -t myapp:dev .

# 生产构建
docker build \
  --build-arg NODE_VERSION=22 \
  --build-arg APP_ENV=production \
  -t myapp:prod .

# CI 中使用 Git SHA 作为标签
docker build \
  --build-arg APP_ENV=production \
  --label "org.opencontainers.image.version=$(git rev-parse --short HEAD)" \
  -t myapp:$(git rev-parse --short HEAD) .
```

## 查看构建参数是否生效

```bash
docker inspect --format='{{.Config.Env}}' myapp:prod | grep NODE_ENV
# [NODE_ENV=production]

docker inspect --format='{{json .Config.Labels}}' myapp:prod | jq .
# {"org.opencontainers.image.version": "abc1234"}
```
```

