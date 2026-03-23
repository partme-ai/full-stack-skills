---
name: flask
description: Provides comprehensive guidance for Flask framework including routing, templates, forms, database integration, extensions, and deployment. Use when the user asks about Flask, needs to create Flask applications, implement web routes, or build Python web applications.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Flask 编写 Python Web 应用、路由、模板与扩展
- 配置 WSGI、蓝图、配置与部署

## How to use this skill

1. **核心**：Flask(__name__)、@app.route、request、render_template；Jinja2。
2. **进阶**：Blueprint、Flask-SQLAlchemy、配置与环境变量；g、session。
3. **参考**：https://flask.palletsprojects.com/

## Best Practices

- 应用工厂与蓝图拆分；敏感配置不入库。
- 生产用 Gunicorn/uWSGI；CSRF 与安全头。

## Keywords

flask, Python Web, 路由, 模板
