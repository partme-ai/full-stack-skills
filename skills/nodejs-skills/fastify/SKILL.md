---
name: fastify
description: "Provides comprehensive guidance for Fastify framework including routing, plugins, JSON schema validation, hooks, serialization, and performance optimization. Use when the user asks about Fastify, needs to create high-performance Node.js applications, implement plugins, or optimize API performance."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build high-performance Node.js HTTP services with Fastify
- Use JSON Schema for request/response validation and serialization
- Create and compose Fastify plugins with encapsulation
- Configure logging, TypeScript, and production deployments

## How to use this skill

### Workflow

1. **Create server** — instantiate Fastify with options (logging, etc.)
2. **Register plugins** — add functionality via the plugin system
3. **Define routes with schemas** — validate requests and serialize responses
4. **Test and deploy** — use `fastify.inject()` for testing, deploy with process manager

### Quick Start Example

```javascript
const fastify = require('fastify')({ logger: true });

// Register plugins
fastify.register(require('@fastify/cors'));
fastify.register(require('@fastify/helmet'));

// Route with JSON Schema validation
fastify.post('/api/items', {
  schema: {
    body: {
      type: 'object',
      required: ['name', 'price'],
      properties: {
        name: { type: 'string', minLength: 1 },
        price: { type: 'number', minimum: 0 },
      },
    },
    response: {
      201: {
        type: 'object',
        properties: {
          id: { type: 'integer' },
          name: { type: 'string' },
          price: { type: 'number' },
        },
      },
    },
  },
  handler: async (request, reply) => {
    const item = await createItem(request.body);
    reply.code(201).send(item);
  },
});

fastify.get('/api/items/:id', async (request, reply) => {
  const item = await getItem(request.params.id);
  if (!item) {
    reply.code(404).send({ error: 'Not found' });
    return;
  }
  return item;
});

fastify.listen({ port: 3000, host: '0.0.0.0' });
```

### Plugin Pattern

```javascript
// plugins/db.js
async function dbPlugin(fastify, options) {
  const pool = createPool(options.connectionString);
  fastify.decorate('db', pool);
  fastify.addHook('onClose', async () => pool.end());
}

module.exports = require('fastify-plugin')(dbPlugin);

// app.js
fastify.register(require('./plugins/db'), {
  connectionString: process.env.DATABASE_URL,
});
```

### Error Handling

```javascript
fastify.setErrorHandler((error, request, reply) => {
  request.log.error(error);
  const statusCode = error.statusCode || 500;
  reply.code(statusCode).send({
    error: error.message,
    statusCode,
  });
});
```

## Best Practices

- Define JSON Schema for all request bodies and responses — enables fast serialization
- Use `fastify-plugin` to break encapsulation when sharing decorators across scopes
- Leverage built-in Pino logger; avoid `console.log` in production
- Use hooks (`onRequest`, `preHandler`) for cross-cutting concerns
- Test routes with `fastify.inject()` without starting a server

## Reference

- Official documentation: https://fastify.dev/docs/latest/

## Keywords

fastify, Node.js, high performance, JSON schema, plugins, serialization, hooks, Pino logger
