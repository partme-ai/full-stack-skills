# 微服务编排 — API Gateway + 3 服务 + Kafka + DB

## compose.yml

```yaml
name: microservices

services:
  gateway:
    image: nginx:1.27-alpine
    ports:
      - "8080:80"
    volumes:
      - ./gateway/nginx.conf:/etc/nginx/nginx.conf:ro
    networks:
      - public
      - internal
    depends_on:
      user-service:
        condition: service_healthy
      order-service:
        condition: service_healthy
      product-service:
        condition: service_healthy
    restart: unless-stopped

  user-service:
    build:
      context: ./services/user
      dockerfile: Dockerfile
    networks:
      - internal
    environment:
      DB_HOST: user-db
      DB_PORT: "5432"
      DB_NAME: users
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      KAFKA_BROKERS: kafka:9092
    depends_on:
      user-db:
        condition: service_healthy
      kafka:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8081/health"]
      interval: 15s
      timeout: 3s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "0.5"

  user-db:
    image: postgres:16-alpine
    volumes:
      - user_db_data:/var/lib/postgresql/data
    networks:
      - internal
    environment:
      POSTGRES_DB: users
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d users"]
      interval: 10s
      timeout: 5s
      retries: 5

  order-service:
    build:
      context: ./services/order
      dockerfile: Dockerfile
    networks:
      - internal
    environment:
      DB_HOST: order-db
      KAFKA_BROKERS: kafka:9092
    depends_on:
      order-db:
        condition: service_healthy
      kafka:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8082/health"]
      interval: 15s
      timeout: 3s
      retries: 3

  order-db:
    image: mysql:8.4
    volumes:
      - order_db_data:/var/lib/mysql
    networks:
      - internal
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MYSQL_DATABASE: orders
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  product-service:
    build:
      context: ./services/product
      dockerfile: Dockerfile
    networks:
      - internal
    environment:
      MONGO_HOST: product-db
      KAFKA_BROKERS: kafka:9092
    depends_on:
      product-db:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8083/health"]
      interval: 15s
      timeout: 3s
      retries: 3

  product-db:
    image: mongo:7
    volumes:
      - product_db_data:/data/db
    networks:
      - internal
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 10s
      timeout: 5s
      retries: 5

  kafka:
    image: bitnami/kafka:3.7
    networks:
      - internal
    environment:
      KAFKA_CFG_NODE_ID: 0
      KAFKA_CFG_PROCESS_ROLES: controller,broker
      KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: 0@kafka:9093
      KAFKA_CFG_LISTENERS: PLAINTEXT://:9092,CONTROLLER://:9093
      KAFKA_CFG_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_CFG_CONTROLLER_LISTENER_NAMES: CONTROLLER
    volumes:
      - kafka_data:/bitnami/kafka
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "kafka-topics.sh", "--bootstrap-server", "localhost:9092", "--list"]
      interval: 30s
      timeout: 10s
      retries: 5

networks:
  public:
    driver: bridge
  internal:
    driver: bridge
    internal: true

volumes:
  user_db_data:
  order_db_data:
  product_db_data:
  kafka_data:
```

## 启动策略

```bash
# 1. 先启动基础设施（DB + Kafka）
docker compose up -d user-db order-db product-db kafka

# 2. 等基础设施就绪后启动服务
docker compose up -d user-service order-service product-service

# 3. 最后启动网关
docker compose up -d gateway
```
```

