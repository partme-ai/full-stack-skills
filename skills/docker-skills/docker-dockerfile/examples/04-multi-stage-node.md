# Node.js pnpm 多阶段构建

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS deps
RUN corepack enable && corepack prepare pnpm@latest --activate
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
COPY prisma ./prisma/
RUN pnpm install --frozen-lockfile --prod=false

FROM node:22-alpine AS builder
RUN corepack enable && corepack prepare pnpm@latest --activate
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile --prod=false
COPY tsconfig.json ./
COPY src ./src
RUN pnpm run build

FROM node:22-alpine
RUN addgroup -S nodejs && adduser -S nodejs -G nodejs
WORKDIR /app
COPY --from=deps /app/node_modules/.pnpm ./node_modules/.pnpm
COPY --from=deps /app/node_modules/.modules.yaml ./node_modules/.modules.yaml
COPY package.json pnpm-lock.yaml ./
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules/.prisma ./node_modules/.prisma
COPY prisma ./prisma
USER nodejs
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:3000/health || exit 1
CMD ["node", "dist/main.js"]
```

**.dockerignore**
```
node_modules/ dist/ build/ .next/ .nuxt/ coverage/ .pnpm-store/ *.log .env* Dockerfile* docker-compose*
```

| 方案 | 镜像大小 |
|------|---------|
| 单阶段 node:22 | ~350 MB |
| 多阶段 + pnpm | ~120 MB |
```
