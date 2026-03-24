---
name: express
description: Provides comprehensive guidance for Express.js framework including routing, middleware, request handling, templating, and API development. Use when the user asks about Express, needs to create Express applications, set up routes, implement middleware, or build REST APIs.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Express 编写 Node.js HTTP 服务、路由、中间件与静态资源
- 配置 CORS、body 解析、错误处理与部署

## How to use this skill

1. **核心**：express()、app.get/post、req/res、中间件（next）；router 与静态。
2. **常用**：cors、body-parser/json、helmet、morgan；错误中间件与 404。
3. **参考**：https://expressjs.com/

## Best Practices

- 路由与中间件分层；异步错误用 try/catch 或包装。
- 安全头与 CORS；生产用反向代理与 HTTPS。

## Keywords

express, Node.js, 中间件, 路由
