# BuildKit SSH 转发：安全访问私有仓库

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.23-alpine
RUN apk add --no-cache git openssh-client
ENV GOPRIVATE=github.com/mycompany/*
RUN --mount=type=ssh \
    mkdir -p ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts && go mod download
```

```bash
eval $(ssh-agent) && ssh-add ~/.ssh/id_rsa
docker buildx build --ssh default -t myapp .
```

## Node.js 私有包
```dockerfile
FROM node:22-alpine
RUN --mount=type=ssh \
    git config --global url."git@github.com:".insteadOf "https://github.com/" && npm install
```
```

