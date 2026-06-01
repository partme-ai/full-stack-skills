# API Versioning Strategies

## Strategy Comparison

| Strategy | Example | Pros | Cons | Best For |
|----------|---------|------|------|----------|
| **URL Path** | `/api/v1/orders` | Intuitive, CDN-friendly, easy to test | URL pollution | **Most projects** |
| **Request Header** | `Accept: app.vnd.company.v2+json` | Clean URLs, semantic | Hard to test, poor tooling | Mature API platforms |
| **Query Parameter** | `/api/orders?version=2` | Simple to implement | Caching issues, accidental param | Temporary/testing |
| **Content Negotiation** | `Accept: app/json;version=2` | RESTful standard | Poor client adoption | REST purists |

## Recommended: URL Path Versioning

```
/api/v1/orders         → Version 1 endpoints
/api/v2/orders         → Version 2 endpoints
/api/v1/orders/{id}
/api/v2/orders/{id}
```

**Rationale:**
- Most intuitive for API consumers
- Best Swagger/OpenAPI compatibility (each version = separate spec file)
- CDN can cache by URL path
- Easy to test in browser, curl, Postman

## Version Lifecycle Management

```
v1.0 (active)       →  v2.0-alpha  →  v2.0-beta   →  v2.0 (GA)
  [launch]              [coexist]      [coexist]      [stable]
                           ↓                              ↓
                     v1.x (maintenance)             v1 (sunset)
                     Bug fixes only                 Deprecation notice
                                                    Removed after 6 months
```

### Migration Process

```
Phase 1: Dual-run (v1 + v2)
  ├── v1: Existing clients continue
  ├── v2: New clients start
  └── Migration guide: Document all breaking changes

Phase 2: Deprecate v1
  ├── Add "Deprecated" header to v1 responses
  ├── Extend migration deadline via announcement
  └── Monitor v1 traffic decline

Phase 3: Sunset v1
  ├── Return 410 Gone for v1 endpoints
  ├── Remove v1 code and deployment
  └── Archive v1 OpenAPI spec
```

## What Constitutes a Breaking Change (Version Bump)

### Major Version Bump Required (Breaking)

```
- Remove a field from response
- Rename a field
- Change field type (string → number)
- Make required field optional (clients may rely on it)
- Change endpoint URL
- Change error codes or response structure
- Add required field to request
```

### Minor/Patch Version (Non-Breaking)

```
- Add new endpoint (v1 + new endpoint is compatible)
- Add optional field to response (clients ignore unknown fields)
- Add optional field to request (server uses default if absent)
- Change error message text (not code or structure)
- Performance improvement
- Bug fix (no contract change)
```

## API Version OpenAPI Examples

### v1 OpenAPI

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  version: 1.0.0
servers:
  - url: https://api.example.com/api/v1
paths:
  /orders:
    get:
      summary: List orders (v1 - basic)
      parameters:
        - name: status
          in: query
          schema:
            type: string
      responses:
        '200':
          description: Order list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderV1'
components:
  schemas:
    OrderV1:
      type: object
      properties:
        id: { type: integer }
        status: { type: string }
        amount: { type: number }
```

### v2 OpenAPI

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  version: 2.0.0
servers:
  - url: https://api.example.com/api/v2
paths:
  /orders:
    get:
      summary: List orders (v2 - enhanced pagination + filters)
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [DRAFT, PAID, SHIPPED, CANCELLED]
        - name: page
          in: query
          schema: { type: integer, default: 1 }
        - name: size
          in: query
          schema: { type: integer, default: 20 }
      responses:
        '200':
          description: Paginated order list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedOrderV2'
components:
  schemas:
    OrderV2:
      type: object
      properties:
        orderId: { type: string }        # Renamed: id → orderId
        status: { type: string }
        totalAmount: { type: string }     # Changed type: number → string
        currency: { type: string }        # NEW field
        items:                            # NEW field
          type: array
          items:
            $ref: '#/components/schemas/OrderItemV2'
```

## Client Migration Guide Template

```markdown
# Migrating from Order API v1 to v2

## Breaking Changes

1. `id` → `orderId` (field renamed)
2. `amount` → `totalAmount` + `currency` (split into two fields)
3. `amount` type: number → string (precision improvement)
4. Response now `{code, message, data}` wrapped

## Migration Steps

1. Update your client to parse `orderId` instead of `id`
2. Use `totalAmount` (string) instead of `amount` (number)
3. Use `currency` field for currency code
4. Parse response from flat `{id, ...}` to wrapped `{code, message, data}`

## Timeline

- v1 deprecation notice: 2024-Q2
- v1 sunset: 2024-Q4
- v2 mandatory: 2025-Q1
```
