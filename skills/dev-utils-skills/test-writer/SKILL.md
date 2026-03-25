---
name: test-writer
description: "Generates unit, integration, and end-to-end tests using frameworks like pytest, Jest, JUnit, and Playwright. Use when the user needs to write tests for existing code, create test suites for a module, add edge-case coverage, or set up a testing framework from scratch."
---

## When to use this skill

Use this skill whenever the user wants to:
- Write unit tests for functions, classes, or modules
- Create integration tests for API endpoints or database interactions
- Build end-to-end tests for user workflows
- Add test coverage for edge cases and error paths
- Set up a testing framework (pytest, Jest, JUnit, Vitest, Playwright)
- Generate test fixtures and mock data

## How to use this skill

### Workflow

1. **Identify the code under test** - Read the function/class/module to understand its behavior
2. **Choose the test type** - Unit (isolated), integration (multi-component), or E2E (full flow)
3. **Write tests using AAA pattern** - Arrange inputs, Act on the function, Assert expected results
4. **Cover edge cases** - Empty inputs, boundary values, error conditions, concurrent access

### Unit Test Example (pytest)

```python
import pytest
from decimal import Decimal
from orders import calculate_order_total, OrderItem

class TestCalculateOrderTotal:
    def test_single_item_no_discount(self):
        items = [OrderItem(price=Decimal("10.00"), quantity=2)]
        result = calculate_order_total(items, discount_pct=0.0, tax_rate=0.08)
        assert result == Decimal("21.60")

    def test_applies_discount_before_tax(self):
        items = [OrderItem(price=Decimal("100.00"), quantity=1)]
        result = calculate_order_total(items, discount_pct=0.1, tax_rate=0.10)
        assert result == Decimal("99.00")

    def test_empty_items_returns_zero(self):
        result = calculate_order_total([], discount_pct=0.0, tax_rate=0.08)
        assert result == Decimal("0.00")

    def test_invalid_discount_raises_error(self):
        items = [OrderItem(price=Decimal("10.00"), quantity=1)]
        with pytest.raises(ValueError, match="discount_pct must be 0-1"):
            calculate_order_total(items, discount_pct=1.5)
```

### Integration Test Example (Jest + Supertest)

```typescript
import request from 'supertest';
import { app } from '../src/app';
import { db } from '../src/database';

describe('POST /api/users', () => {
  afterEach(async () => { await db.query('DELETE FROM users WHERE email LIKE $1', ['%@test.com']); });

  it('creates a user and returns 201', async () => {
    const res = await request(app)
      .post('/api/users')
      .send({ name: 'Alice', email: 'alice@test.com' })
      .expect(201);
    expect(res.body).toMatchObject({ name: 'Alice', email: 'alice@test.com' });
  });

  it('returns 400 for missing email', async () => {
    await request(app).post('/api/users').send({ name: 'Bob' }).expect(400);
  });
});
```

## Best Practices

1. **One assertion per behavior** - Each test should verify one specific behavior
2. **Descriptive test names** - Name tests as `test_<behavior>_when_<condition>` or `it('should <outcome> when <input>')`
3. **Isolate dependencies** - Use mocks/stubs for external services, databases, and APIs
4. **Test the contract, not the implementation** - Assert on outputs and side effects, not internal state
5. **Run tests in CI** - Ensure tests pass on every commit; aim for 80%+ line coverage on critical paths

## Keywords

测试编写, test writing, unit test, integration test, e2e test, pytest, Jest, JUnit, Vitest, Playwright, mock, fixture, 单元测试, 集成测试, 端到端测试, test coverage
