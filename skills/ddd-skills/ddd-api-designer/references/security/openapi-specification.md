# OpenAPI 3.0 Specification for DDD APIs

## Complete OpenAPI Template

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  description: REST API for Order Bounded Context — CQRS-separated commands and queries
  version: 2.0.0
  contact:
    name: Order Team
    email: order-team@company.com
servers:
  - url: https://api.example.com/api/v2
    description: Production
  - url: https://staging-api.example.com/api/v2
    description: Staging

paths:
  # ─── Command Endpoints (Write) ──────────────────────────────────
  /orders:
    post:
      summary: Create a new order
      operationId: createOrder
      tags: [Order Commands]
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
      responses:
        '201':
          description: Order created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderCreatedResponse'
        '400':
          description: Validation or business error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiError'
      x-springdoc-default: "40001"

  /orders/{orderId}/confirm:
    put:
      summary: Confirm an order
      operationId: confirmOrder
      tags: [Order Commands]
      security:
        - BearerAuth: []
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
            pattern: '^ORD-\d{4}-\d{3,6}$'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ConfirmOrderRequest'
      responses:
        '200':
          description: Order confirmed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderCommandResponse'
        '404':
          description: Order not found

  /orders/{orderId}:
    delete:
      summary: Cancel an order
      operationId: cancelOrder
      tags: [Order Commands]
      security:
        - BearerAuth: []
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CancelOrderRequest'
      responses:
        '204':
          description: Order cancelled (no content)

  # ─── Query Endpoints (Read) ────────────────────────────────────
  /orders/{orderId}:
    get:
      summary: Get order details
      operationId: getOrder
      tags: [Order Queries]
      security:
        - BearerAuth: []
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
        - name: include
          in: query
          description: Comma-separated fields to include (items, payments)
          schema:
            type: string
      responses:
        '200':
          description: Order detail
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderDetailResponse'

  /orders:
    get:
      summary: List orders with filtering and pagination
      operationId: listOrders
      tags: [Order Queries]
      security:
        - BearerAuth: []
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [DRAFT, PAID, SHIPPED, CANCELLED]
        - name: customerId
          in: query
          schema:
            type: string
        - name: page
          in: query
          schema:
            type: integer
            default: 1
            minimum: 1
        - name: size
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
        - name: sort
          in: query
          schema:
            type: string
            default: createdAt,desc
      responses:
        '200':
          description: Paginated order list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderListResponse'

  # ─── Sub-resource Endpoints ────────────────────────────────────
  /orders/{orderId}/items:
    get:
      summary: List items in an order
      operationId: listOrderItems
      tags: [Order Items]
      security:
        - BearerAuth: []
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Order items
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/OrderItemDTO'

    post:
      summary: Add item to order
      operationId: addOrderItem
      tags: [Order Items]
      security:
        - BearerAuth: []
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOrderItemRequest'
      responses:
        '201':
          description: Item added

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    # ─── Command DTOs ──────────────────────────────────────────
    CreateOrderRequest:
      type: object
      required: [customerId, items]
      properties:
        customerId:
          type: string
          description: Customer ID
        items:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/OrderItemRequest'
        couponCode:
          type: string
          description: Optional coupon code

    OrderItemRequest:
      type: object
      required: [productId, quantity]
      properties:
        productId:
          type: string
        quantity:
          type: integer
          minimum: 1
          maximum: 999

    ConfirmOrderRequest:
      type: object
      required: [paymentMethodId]
      properties:
        paymentMethodId:
          type: string

    CancelOrderRequest:
      type: object
      required: [reason]
      properties:
        reason:
          type: string
          maxLength: 500

    # ─── Response DTOs ─────────────────────────────────────────
    OrderCreatedResponse:
      type: object
      properties:
        code:
          type: integer
          example: 0
        message:
          type: string
          example: success
        data:
          $ref: '#/components/schemas/OrderCreatedData'

    OrderCreatedData:
      type: object
      properties:
        orderId:
          type: string
          example: ORD-2024-001
        status:
          type: string
          example: DRAFT
        createdAt:
          type: string
          format: date-time

    OrderCommandResponse:
      type: object
      properties:
        code:
          type: integer
          example: 0
        message:
          type: string
          example: success
        data:
          type: object
          properties:
            orderId:
              type: string
            status:
              type: string

    # ─── Query DTOs ────────────────────────────────────────────
    OrderDetailResponse:
      type: object
      properties:
        code:
          type: integer
          example: 0
        message:
          type: string
        data:
          $ref: '#/components/schemas/OrderDetailVO'

    OrderDetailVO:
      type: object
      properties:
        orderId:
          type: string
        status:
          type: string
        totalAmount:
          type: string
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItemDTO'
        customer:
          $ref: '#/components/schemas/CustomerDTO'
        payment:
          $ref: '#/components/schemas/PaymentDTO'
        shipping:
          $ref: '#/components/schemas/ShippingDTO'
        createdAt:
          type: string
          format: date-time

    OrderItemDTO:
      type: object
      properties:
        itemId:
          type: string
        productName:
          type: string
        quantity:
          type: integer
        unitPrice:
          type: string
        subtotal:
          type: string

    CustomerDTO:
      type: object
      properties:
        customerId:
          type: string
        name:
          type: string
        email:
          type: string

    PaymentDTO:
      type: object
      properties:
        paymentId:
          type: string
        method:
          type: string
        amount:
          type: string
        paidAt:
          type: string
          format: date-time

    ShippingDTO:
      type: object
      properties:
        address:
          type: string
        carrier:
          type: string
        trackingNumber:
          type: string
        estimatedDelivery:
          type: string
          format: date

    # ─── Paginated Response ────────────────────────────────────
    OrderListResponse:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        data:
          $ref: '#/components/schemas/PaginatedOrders'

    PaginatedOrders:
      type: object
      properties:
        records:
          type: array
          items:
            $ref: '#/components/schemas/OrderSummaryVO'
        total:
          type: integer
          example: 100
        page:
          type: integer
          example: 1
        pageSize:
          type: integer
          example: 20
        totalPages:
          type: integer
          example: 5

    OrderSummaryVO:
      type: object
      properties:
        orderId:
          type: string
        status:
          type: string
        totalAmount:
          type: string
        itemCount:
          type: integer
        createdAt:
          type: string
          format: date-time

    # ─── Error Schema ──────────────────────────────────────────
    ApiError:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        detail:
          oneOf:
            - type: string
            - type: array
              items:
                $ref: '#/components/schemas/FieldError'
        requestId:
          type: string

    FieldError:
      type: object
      properties:
        field:
          type: string
        message:
          type: string
```

## OpenAPI Code Generation Strategy

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **Code-first** (annotations) | Single source of truth (code) | Spec may drift from reality | Fast-moving projects |
| **Spec-first** (YAML → codegen) | Contract-first, client SDK | Needs codegen tooling | Public APIs |
| **Hybrid** (annotations → spec export) | Both contract + code aligned | Two-step process | Enterprise |

**Recommendation**: Use code-first for DDD services (SpringDoc / swagger-annotations), export to YAML for client SDK generation.

## Collection Format Configuration

```yaml
# SpringDoc configuration
springdoc:
  api-docs:
    path: /api-docs
  swagger-ui:
    path: /swagger-ui.html
  packages-to-scan: com.example.order.adapter.inbound.web
  paths-to-match: /api/v2/**
```

## Generation Rules for DDD APIs

1. **One OpenAPI spec per bounded context** — Order BC has its own spec, Payment BC has its own
2. **Tag endpoints by CQRS** — `Order Commands` tag for writes, `Order Queries` tag for reads
3. **Never expose DO fields** — All exposed models are DTOs/VOs, never domain objects
4. **Document error codes** — Use `x-*` extensions for business error codes
5. **All datetime fields use ISO 8601** — `format: date-time` or `format: date`
6. **Use `$ref` for reusable schemas** — Avoid inline schema duplication
