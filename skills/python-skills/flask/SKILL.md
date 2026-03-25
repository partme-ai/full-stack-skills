---
name: flask
description: "Provides comprehensive guidance for Flask framework including routing, templates, forms, database integration, extensions, and deployment. Use when the user asks about Flask, needs to create web applications, implement routes, or build Python web services."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Python web applications with Flask routing and templates
- Configure WSGI, blueprints, extensions, and deployment
- Integrate Flask-SQLAlchemy, Flask-Login, or other extensions
- Create REST APIs or serve server-rendered pages with Jinja2

## How to use this skill

### Workflow

1. **Create app** — instantiate Flask and define routes
2. **Add templates** — use Jinja2 for HTML rendering
3. **Organize with blueprints** — split features into blueprint modules
4. **Configure and deploy** — set environment config, deploy with Gunicorn

### Quick Start Example

```python
# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-me-in-production'

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/api/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        data = request.get_json()
        # Process and save item
        return jsonify({'status': 'created', 'item': data}), 201
    return jsonify({'items': []})

if __name__ == '__main__':
    app.run(debug=True)
```

### Application Factory Pattern

```python
# __init__.py
from flask import Flask

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
```

```bash
# Development
flask --app app run --debug

# Production
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

### Blueprint Example

```python
# auth/routes.py
from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        return redirect(url_for('main.index'))
    return render_template('auth/login.html')
```

## Best Practices

- Use the application factory pattern with blueprints for modularity
- Keep sensitive configuration out of source code — use environment variables
- Deploy with Gunicorn or uWSGI behind a reverse proxy (nginx)
- Enable CSRF protection with Flask-WTF; set security headers
- Use `flask shell` for interactive debugging with app context

## Reference

- Official documentation: https://flask.palletsprojects.com/

## Keywords

flask, Python web, routing, templates, Jinja2, blueprints, WSGI, REST API, Gunicorn
