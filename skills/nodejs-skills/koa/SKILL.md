---
name: koa
description: "Provides comprehensive guidance for Koa.js framework including middleware composition, context API, async/await patterns, and application structure. Use when the user asks about Koa, needs to create lightweight Node.js web applications, implement middleware, or build APIs with Koa."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Node.js HTTP services with Koa and its onion-model middleware
- Configure routing (koa-router), body parsing, error handling, and static files
- Compose async middleware with `ctx` and `next` patterns
- Create lightweight REST APIs or web applications

## How to use this skill

### Workflow

1. **Create app** — instantiate Koa and add middleware in order
2. **Add routing** — use `@koa/router` for route definitions
3. **Handle errors** — add error middleware at the top of the stack
4. **Deploy** — run behind reverse proxy with HTTPS

### Quick Start Example

```javascript
const Koa = require('koa');
const Router = require('@koa/router');
const bodyParser = require('koa-bodyparser');

const app = new Koa();
const router = new Router();

// Error handling middleware (top of stack)
app.use(async (ctx, next) => {
  try {
    await next();
  } catch (err) {
    ctx.status = err.status || 500;
    ctx.body = { error: err.message };
    ctx.app.emit('error', err, ctx);
  }
});

// Body parser
app.use(bodyParser());

// Routes
router.get('/api/items', async (ctx) => {
  const items = await Item.findAll();
  ctx.body = { items };
});

router.post('/api/items', async (ctx) => {
  const { name, price } = ctx.request.body;
  const item = await Item.create({ name, price });
  ctx.status = 201;
  ctx.body = item;
});

router.get('/api/items/:id', async (ctx) => {
  const item = await Item.findById(ctx.params.id);
  if (!item) {
    ctx.throw(404, 'Item not found');
  }
  ctx.body = item;
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(3000, () => console.log('Server running on port 3000'));
```

### Onion Model Middleware

```javascript
// Logging middleware — demonstrates onion execution order
app.use(async (ctx, next) => {
  const start = Date.now();
  await next(); // <-- downstream
  const ms = Date.now() - start;
  ctx.set('X-Response-Time', `${ms}ms`);
  console.log(`${ctx.method} ${ctx.url} - ${ms}ms`);
});
```

### Custom Middleware Example

```javascript
// Authentication middleware
function requireAuth() {
  return async (ctx, next) => {
    const token = ctx.get('Authorization')?.replace('Bearer ', '');
    if (!token) {
      ctx.throw(401, 'Authentication required');
    }
    ctx.state.user = await verifyToken(token);
    await next();
  };
}

router.get('/api/profile', requireAuth(), async (ctx) => {
  ctx.body = ctx.state.user;
});
```

## Best Practices

- Use `async/await` correctly with `next()` — always `await next()` in middleware
- Place error handling middleware at the top of the middleware stack
- Use `ctx.throw()` for HTTP errors; listen to `app.on('error')` for logging
- Deploy behind a reverse proxy (nginx) with HTTPS in production
- Use `@koa/cors` for CORS configuration; keep middleware chain lean

## Reference

- Official documentation: https://koajs.com/

## Keywords

koa, Node.js, middleware, onion model, async/await, context, routing, REST API
