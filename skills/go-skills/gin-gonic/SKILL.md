---
name: gin-gonic
description: "Guides Go web development with the Gin-Gonic HTTP framework including routing, route groups, middleware, JSON binding, validation, error handling, and graceful shutdown. Use when the user needs to build REST APIs or HTTP services with Gin-Gonic (alias for the Gin framework)."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Go HTTP services or REST APIs with Gin-Gonic
- Configure routing, route groups, and middleware
- Implement request binding, validation, and JSON responses
- Set up authentication, logging, or CORS middleware
- Deploy Gin applications with graceful shutdown

## How to use this skill

### Workflow

1. **Initialize the router** - `gin.Default()` includes Logger and Recovery middleware
2. **Define routes** - Group related routes and attach handlers
3. **Bind and validate** - Use `ShouldBindJSON` or `ShouldBindQuery` with struct tags
4. **Return responses** - Use `c.JSON()` for consistent API responses

### Quick-Start Example: REST API with Middleware

```go
package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type CreateUserRequest struct {
    Name  string `json:"name" binding:"required,min=2"`
    Email string `json:"email" binding:"required,email"`
}

func main() {
    r := gin.Default()

    // Route group with auth middleware
    api := r.Group("/api/v1")
    {
        api.POST("/users", createUser)
        api.GET("/users/:id", getUser)
    }

    r.Run(":8080")
}

func createUser(c *gin.Context) {
    var req CreateUserRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    // ... create user logic
    c.JSON(http.StatusCreated, gin.H{"name": req.Name, "email": req.Email})
}

func getUser(c *gin.Context) {
    id := c.Param("id")
    c.JSON(http.StatusOK, gin.H{"id": id})
}
```

## Best Practices

1. **Use route groups** - Group routes by version or resource (`/api/v1/users`)
2. **Validate with struct tags** - Use `binding:"required,email"` for declarative validation
3. **Centralize error handling** - Use middleware to catch panics and return consistent error JSON
4. **Graceful shutdown** - Use `http.Server` with `srv.Shutdown(ctx)` for clean connection draining
5. **Avoid gin.Default() in production** - Use `gin.New()` and add only the middleware you need

## Resources

- **Official Docs**: https://gin-gonic.com/docs/

## Keywords

gin-gonic, gin, Go, web framework, REST API, routing, middleware, JSON binding, 路由, 中间件
