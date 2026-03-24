# Authenticated Sessions | 认证会话

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to use custom HTTP headers for authentication, skipping login flows.

### Key Concepts

- Authentication via HTTP headers
- Origin-scoped headers (security)
- Skipping login flows
- Multiple origins with different auth tokens
- Global headers vs origin-scoped headers

### Example: Basic Authentication

```bash
# Set headers for specific origin (scoped to api.example.com only)
agent-browser open api.example.com --headers '{"Authorization": "Bearer <token>"}'

# All requests to api.example.com include the auth header
agent-browser snapshot -i --json
agent-browser click @e2

# Navigate to another domain - headers are NOT sent (safe!)
agent-browser open other-site.com  # No auth header sent
```

### Example: Multiple Origins

```bash
# Set headers for first origin
agent-browser open api.example.com --headers '{"Authorization": "Bearer token1"}'
agent-browser snapshot -i

# Set headers for second origin
agent-browser open api.acme.com --headers '{"Authorization": "Bearer token2"}'
agent-browser snapshot -i
```

### Example: Global Headers

```bash
# Set global headers (all domains)
agent-browser set headers '{"X-Custom-Header": "value"}'

# All subsequent requests include the header
agent-browser open example.com
agent-browser open other-site.com  # Header included here too
```

### Example: Use Cases

```bash
# 1. Skip login flows - Authenticate via headers instead of UI
agent-browser open dashboard.example.com --headers '{"Authorization": "Bearer <token>"}'
agent-browser snapshot -i

# 2. Switch users - Start new sessions with different auth tokens
agent-browser --session user1 open api.example.com --headers '{"Authorization": "Bearer token1"}'
agent-browser --session user2 open api.example.com --headers '{"Authorization": "Bearer token2"}'

# 3. API testing - Access protected endpoints directly
agent-browser open api.example.com/protected --headers '{"Authorization": "Bearer <token>"}'
agent-browser get text @e1
```

### Key Points

- Use `--headers` flag to set HTTP headers for specific origin
- Headers are scoped to the origin (security feature)
- Use `set headers` for global headers (all domains)
- Useful for skipping login flows and API testing
- Headers are not leaked to other domains (safe)
