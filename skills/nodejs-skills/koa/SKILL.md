---
name: koa
description: Provides comprehensive guidance for Koa.js framework including middleware, context, async/await patterns, and application structure. Use when the user asks about Koa, needs to create Koa applications, implement middleware, or build Node.js web applications.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Koa 编写 Node.js HTTP 服务、中间件与洋葱模型
- 配置路由（koa-router）、body 解析、错误处理与部署

## How to use this skill

1. **核心**：Koa()、ctx 与 next；async 中间件与洋葱顺序；ctx.body、ctx.status。
2. **生态**：koa-router、koa-bodyparser、koa-static；错误与日志中间件。
3. **参考**：https://koajs.com/

## Best Practices

- 中间件 async 与 next 正确使用；错误统一捕获。
- 生产用反向代理与 HTTPS；安全与 CORS。

## Keywords

koa, Node.js, 中间件, 洋葱模型
