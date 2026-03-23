---
name: pytest
description: Provides comprehensive guidance for pytest testing framework including test writing, fixtures, parametrization, mocking, and plugins. Use when the user asks about pytest, needs to write Python tests, use pytest fixtures, or configure pytest for Python projects.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 pytest 编写或运行 Python 单元测试与 fixture
- 使用断言、参数化、mock 与插件（覆盖率、并行）

## How to use this skill

1. **用例**：test_ 前缀或 Test 类；assert 语句；@pytest.fixture、conftest.py。
2. **运行**：pytest、pytest -v -k "pattern"、pytest --cov；markers 与 xfail。
3. **插件**：pytest-cov、pytest-xdist、pytest-mock；pytest.ini 或 pyproject.toml 配置。

## Best Practices

- 单测独立、无副作用；用 fixture 准备数据与依赖。
- 命名与目录清晰；避免依赖执行顺序。
- CI 中跑全量；覆盖率与失败即停。

## Keywords

pytest, Python 测试, fixture, 单元测试
