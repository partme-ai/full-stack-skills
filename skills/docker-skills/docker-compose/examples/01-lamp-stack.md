# LAMP 全栈部署 — Nginx + PHP-FPM + MySQL + Redis

## compose.yml

```yaml
name: lamp-stack

services:
  web:
    image: nginx:1.27-alpine
    ports:
      - "8080:80"
    volumes:
      - ./app:/var/www/html:ro
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - web_logs:/var/log/nginx
    networks:
      - frontend
    depends_on:
      php:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost/health"]
      interval: 30s
      timeout: 3s
      retries: 3

  php:
    build:
      context: ./php
      dockerfile: Dockerfile
    volumes:
      - ./app:/var/www/html:ro
    networks:
      - frontend
      - backend
    environment:
      PHP_FPM_PM: dynamic
      PHP_FPM_PM_MAX_CHILDREN: "10"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "php-fpm-healthcheck"]
      interval: 30s
      timeout: 3s
      retries: 3

  db:
    image: mysql:8.4
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
      - ./mysql/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${MYSQL_ROOT_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
      - ./redis/redis.conf:/usr/local/etc/redis/redis.conf:ro
    networks:
      - backend
    command: redis-server /usr/local/etc/redis/redis.conf
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true

volumes:
  db_data:
    driver: local
  redis_data:
    driver: local
  web_logs:
    driver: local
```

## .env

```bash
MYSQL_ROOT_PASSWORD=rootpass123
MYSQL_DATABASE=myapp
MYSQL_USER=myuser
MYSQL_PASSWORD=mypass123
```

## 启动

```bash
docker compose up -d
docker compose ps
docker compose logs -f
```
```

