---
name: django
description: "Provides comprehensive guidance for Django framework including models, views, templates, forms, admin, REST framework, and deployment. Use when the user asks about Django, needs to create web applications, implement models and views, or build Django REST APIs."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create Django web applications with models, views, and templates
- Configure projects, apps, migrations, and deployment
- Build REST APIs with Django REST Framework
- Set up Django admin, forms, and authentication

## How to use this skill

### Workflow

1. **Create project** — scaffold with `django-admin startproject`
2. **Add apps** — create feature apps with `python manage.py startapp`
3. **Define models** — write models, create and run migrations
4. **Build views and URLs** — implement views, wire URL patterns
5. **Test and deploy** — run tests, configure production settings

### Quick Start Example

```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
]
```

```bash
# Setup workflow
django-admin startproject myproject
python manage.py startapp articles
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Django REST Framework Example

```python
# serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'published_at']

# views.py
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

## Best Practices

- One app per responsibility; normalize models and add database indexes
- Keep views thin — place business logic in services or model methods
- Always enable CSRF protection and configure security middleware
- Use `select_related` and `prefetch_related` to avoid N+1 queries
- Run tests with `python manage.py test`; use `--parallel` for speed

## Reference

- Official documentation: https://docs.djangoproject.com/

## Keywords

django, ORM, MTV, migrations, Python web, REST framework, admin, views, templates
