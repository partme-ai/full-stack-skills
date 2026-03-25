---
name: express
description: "Provides comprehensive guidance for Express.js framework including routing, middleware, request handling, error handling, and API development. Use when the user asks about Express, needs to create HTTP servers, set up routes, implement middleware, or build REST APIs."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Node.js HTTP servers with Express routing and middleware
- Configure CORS, body parsing, error handling, and static files
- Create REST APIs with request validation and response formatting
- Set up production-ready Express applications with security headers

## How to use this skill

### Workflow

1. **Create app** — instantiate Express and configure middleware
2. **Define routes** — set up route handlers for each endpoint
3. **Add error handling** — implement error middleware for consistent responses
4. **Deploy** — run behind a reverse proxy with HTTPS

### Quick Start Example

```javascript
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');

const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Routes
app.get('/api/items', async (req, res, next) => {
  try {
    const items = await Item.findAll();
    res.json({ items });
  } catch (err) {
    next(err);
  }
});

app.post('/api/items', async (req, res, next) => {
  try {
    const { name, price } = req.body;
    const item = await Item.create({ name, price });
    res.status(201).json(item);
  } catch (err) {
    next(err);
  }
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});

// Error middleware (must have 4 params)
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message || 'Internal server error',
  });
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

### Async Error Wrapper

```javascript
// Wrap async handlers to catch rejected promises
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

app.get('/api/users', asyncHandler(async (req, res) => {
  const users = await User.findAll();
  res.json(users);
}));
```

### Router Example

```javascript
// routes/items.js
const router = require('express').Router();

router.get('/', asyncHandler(async (req, res) => { /* ... */ }));
router.post('/', asyncHandler(async (req, res) => { /* ... */ }));
router.get('/:id', asyncHandler(async (req, res) => { /* ... */ }));

module.exports = router;

// app.js
app.use('/api/items', require('./routes/items'));
```

## Best Practices

- Separate routes and middleware into modules; use `express.Router()` for organization
- Always wrap async handlers with try/catch or a wrapper to avoid unhandled rejections
- Use `helmet` for security headers and configure CORS for production origins
- Deploy behind a reverse proxy (nginx) with HTTPS in production
- Use `morgan` for request logging and structured error responses

## Reference

- Official documentation: https://expressjs.com/

## Keywords

express, Node.js, middleware, routing, REST API, error handling, async, helmet, cors
