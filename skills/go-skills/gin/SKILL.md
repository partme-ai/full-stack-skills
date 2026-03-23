---
name: gin
description: Provides comprehensive guidance for Gin Go framework including routing, middleware, request handling, JSON binding, and API development. Use when the user asks about Gin, needs to create Gin applications, implement REST APIs, or build Go web services.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Gin 编写 Go HTTP 路由、中间件、绑定与渲染
- 配置路由组、 recovery、CORS 与部署

## How to use this skill

1. **核心**：gin.Default()、GET/POST、c.JSON、c.Bind；路由组与中间件。
2. **进阶**：自定义中间件、验证、静态文件；Graceful shutdown。
3. **参考**：https://gin-gonic.com/docs/

## Best Practices

- 中间件顺序与职责清晰；错误统一返回。
- 绑定与校验；生产用 recovery 与日志。

## Keywords

gin, Go Web, 路由, 中间件
