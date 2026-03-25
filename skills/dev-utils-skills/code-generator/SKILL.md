---
name: code-generator
description: "Generates production-ready code scaffolds, functions, classes, and project structures across Python, TypeScript, Java, and Go. Use when the user asks to generate code from templates, scaffold a new project, create boilerplate classes or modules, or automate repetitive code creation tasks."
---

## When to use this skill

Use this skill whenever the user wants to:
- Generate functions, classes, or modules with proper documentation and error handling
- Scaffold a new project with configuration files and directory structure
- Create boilerplate code (CRUD controllers, service layers, data models)
- Refactor or optimize existing code structure
- Generate code from templates or specifications

## How to use this skill

### Workflow

1. **Clarify requirements** - Identify the target language, framework, and coding conventions
2. **Choose the generation type** - Function/class, module/package, or full project scaffold
3. **Generate code** - Produce complete, documented, tested code following the patterns below
4. **Validate output** - Ensure the code compiles/runs and follows project conventions

### Code Generation Patterns

**Function generation (Python example):**
```python
def calculate_order_total(
    items: list[OrderItem],
    discount_pct: float = 0.0,
    tax_rate: float = 0.08,
) -> Decimal:
    """Calculate the total price for an order including tax and discount.

    Args:
        items: List of order items with price and quantity.
        discount_pct: Discount percentage (0.0 to 1.0).
        tax_rate: Tax rate to apply after discount.

    Returns:
        Final order total as a Decimal rounded to 2 places.

    Raises:
        ValueError: If discount_pct is not between 0 and 1.
    """
    if not 0 <= discount_pct <= 1:
        raise ValueError(f"discount_pct must be 0-1, got {discount_pct}")

    subtotal = sum(item.price * item.quantity for item in items)
    discounted = subtotal * Decimal(1 - discount_pct)
    total = discounted * Decimal(1 + tax_rate)
    return total.quantize(Decimal("0.01"))
```

**Project scaffold (TypeScript/Node):**
```
my-service/
├── src/
│   ├── controllers/    # Route handlers
│   ├── services/       # Business logic
│   ├── models/         # Data models / DTOs
│   ├── middleware/      # Auth, logging, error handling
│   └── index.ts        # Entry point
├── tests/
│   ├── unit/
│   └── integration/
├── package.json
├── tsconfig.json
└── README.md
```

### Supported Languages

- Python (with type hints, docstrings, pytest)
- JavaScript / TypeScript (ESM, JSDoc or TSDoc)
- Java (JavaDoc, Maven/Gradle)
- Go (godoc, modules)
- Rust (rustdoc, Cargo)

## Best Practices

1. **Always include error handling** - Validate inputs, use typed exceptions, return meaningful error messages
2. **Add documentation** - Every public function/class gets a docstring with params, returns, and raises
3. **Follow language conventions** - PEP 8 for Python, gofmt for Go, Prettier for TypeScript
4. **Generate tests alongside code** - At minimum, one happy-path and one error-path test per function
5. **Use type annotations** - Catch bugs early with static typing where the language supports it

## Keywords

代码生成, code generation, scaffold, boilerplate, template, 函数, 类, 模块, project structure, code scaffold, 项目脚手架
