# Framework & Drivers Layer Configuration

## Location: `{project}-framework/config/`

The **Frameworks & Drivers** layer is the outermost layer — it wires everything together using dependency injection (Spring Boot), configures web/server settings, and bootstraps the application.

## DI Configuration — Wiring the Layers

```java
package com.example.framework.config;

import com.example.adapter.repository.JpaOrderRepository;
import com.example.adapter.gateway.StripePaymentGateway;
import com.example.core.entity.Order;
import com.example.usecase.interactor.CreateOrderInteractor;
import com.example.usecase.interactor.PayOrderInteractor;
import com.example.usecase.interactor.GetOrderInteractor;
import com.example.usecase.port.input.CreateOrderUseCase;
import com.example.usecase.port.input.PayOrderUseCase;
import com.example.usecase.port.input.GetOrderUseCase;
import com.example.usecase.port.output.OrderRepository;
import com.example.usecase.port.output.PaymentGateway;
import com.example.usecase.port.output.EventPublisher;
import com.example.usecase.port.output.NotificationPort;
import com.example.adapter.gateway.RabbitMQEventPublisher;
import com.example.adapter.gateway.EmailNotificationAdapter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * ★ Framework Layer — Dependency Injection configuration.
 * This is where the outermost layer wires all inner layers together.
 * The Interactors and Entities know nothing about Spring.
 */
@Configuration
public class UseCaseConfig {

    // ── Output Port implementations (Adapters) ──
    @Bean
    public OrderRepository orderRepository(
            JpaOrderRepository jpaOrderRepository) {
        return jpaOrderRepository;    // Adapter implements Output Port
    }

    @Bean
    public PaymentGateway paymentGateway(
            StripePaymentGateway stripePaymentGateway) {
        return stripePaymentGateway;
    }

    @Bean
    public EventPublisher eventPublisher(
            RabbitMQEventPublisher rabbitMQEventPublisher) {
        return rabbitMQEventPublisher;
    }

    @Bean
    public NotificationPort notificationPort(
            EmailNotificationAdapter emailAdapter) {
        return emailAdapter;
    }

    // ── UseCase Interactors (Application Business Rules) ──
    @Bean
    public CreateOrderUseCase createOrderUseCase(
            OrderRepository orderRepository,
            EventPublisher eventPublisher,
            NotificationPort notificationPort) {
        return new CreateOrderInteractor(
            orderRepository, eventPublisher, notificationPort);
    }

    @Bean
    public PayOrderUseCase payOrderUseCase(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher) {
        return new PayOrderInteractor(
            orderRepository, paymentGateway, eventPublisher);
    }

    @Bean
    public GetOrderUseCase getOrderUseCase(
            OrderRepository orderRepository) {
        return new GetOrderInteractor(orderRepository);
    }
}
```

## Web Configuration

```java
package com.example.framework.config.web;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.web.filter.CorsFilter;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Bean
    public CorsFilter corsFilter() {
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowCredentials(true);
        config.addAllowedOriginPattern("*");
        config.addAllowedHeader("*");
        config.addAllowedMethod("*");

        UrlBasedCorsConfigurationSource source =
            new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", config);
        return new CorsFilter(source);
    }
}
```

## Security Configuration

```java
package com.example.framework.config.security;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    private final JwtAuthenticationFilter jwtFilter;

    public SecurityConfig(JwtAuthenticationFilter jwtFilter) {
        this.jwtFilter = jwtFilter;
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/v1/auth/**").permitAll()
                .requestMatchers("/api/v1/**").authenticated()
                .anyRequest().permitAll()
            )
            .addFilterBefore(jwtFilter,
                UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
}
```

## Persistence Configuration

```java
package com.example.framework.config.persistence;

import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@Configuration
@EnableJpaRepositories(basePackages = "com.example.adapter.repository")
@EntityScan(basePackages = "com.example.adapter.repository.entity")
@EnableTransactionManagement
public class PersistenceConfig {

    // Spring Boot auto-configures DataSource from application.yml
    // Additional JPA tuning can go here.
}
```

## Application Entry Point

```java
package com.example.framework;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

/**
 * ★ Application entry point — Framework Layer.
 * Scans all layers for Spring-managed beans.
 */
@SpringBootApplication
@ComponentScan(basePackages = {
    "com.example.framework.config",
    "com.example.adapter",
    "com.example.usecase.interactor"
})
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## Application Configuration

```yaml
# src/main/resources/application.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/orderdb
    username: ${DB_USERNAME:app}
    password: ${DB_PASSWORD:secret}
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        format_sql: true

server:
  port: 8080

app:
  payment:
    stripe-api-key: ${STRIPE_API_KEY}
  notification:
    email-from: orders@example.com

---

spring:
  config:
    activate:
      on-profile: test

  datasource:
    url: jdbc:h2:mem:testdb
  jpa:
    hibernate:
      ddl-auto: create-drop
```

## Global Exception Handler (Adapter Layer)

```java
package com.example.adapter.presenter;

import com.example.core.exception.DomainException;
import com.example.usecase.exception.UseCaseException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.time.Instant;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(DomainException.class)
    public ResponseEntity<ErrorResponse> handleDomain(DomainException ex) {
        return ResponseEntity
            .status(HttpStatus.UNPROCESSABLE_ENTITY)
            .body(new ErrorResponse("DOMAIN_ERROR", ex.getMessage()));
    }

    @ExceptionHandler(UseCaseException.class)
    public ResponseEntity<ErrorResponse> handleUseCase(UseCaseException ex) {
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body(new ErrorResponse("USE_CASE_ERROR", ex.getMessage()));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneric(Exception ex) {
        return ResponseEntity
            .status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(new ErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
    }

    public record ErrorResponse(
        String code,
        String message,
        Instant timestamp
    ) {
        public ErrorResponse(String code, String message) {
            this(code, message, Instant.now());
        }
    }
}
```

## Multi-Profile Configuration

| Profile | Purpose | Database | External Services |
|---------|---------|----------|-------------------|
| `dev` | Development | H2 in-memory | Mock endpoints |
| `test` | Automated tests | H2 file-based | WireMock stubs |
| `staging` | Pre-production | PostgreSQL staging | Sandbox APIs |
| `prod` | Production | PostgreSQL cluster | Live APIs |

## Layer Diagram with DI Wiring

```
┌─ Framework (Spring Boot) ─────────────────────┐
│  @Configuration beans wire everything together  │
│  Application.java                              │
│                                                  │
│  ┌─ Adapter (Controller/Repository/Gateway) ─┐ │
│  │  @RestController OrderController            │ │
│  │  @Repository JpaOrderRepository           │ │
│  │     ┌─ UseCase (Interactor + Ports) ──┐   │ │
│  │     │  CreateOrderInteractor           │   │ │
│  │     │  OrderRepository (interface)     │   │ │
│  │     │  CreateOrderUseCase (interface)  │   │ │
│  │     │     ┌─ Enterprise (Entity) ─┐   │   │ │
│  │     │     │  Order.java          │   │   │ │
│  │     │     │  Money.java          │   │   │ │
│  │     │     └──────────────────────┘   │   │ │
│  │     └─────────────────────────────────┘   │ │
│  └───────────────────────────────────────────┘ │
└────────────────────────────────────────────────┘
```

## Module Dependencies (Maven/Gradle)

```xml
<!-- pom.xml — multi-module project -->
<modules>
    <module>order-core</module>         <!-- Enterprise layer -->
    <module>order-usecase</module>      <!-- UseCase layer -->
    <module>order-adapter</module>      <!-- Adapter layer -->
    <module>order-framework</module>    <!-- Framework layer -->
</modules>

<!-- order-framework/pom.xml depends on all inner layers -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-usecase</artifactId>
</dependency>
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-adapter</artifactId>
</dependency>
```

## Key Rules

| Rule | Description |
|------|-------------|
| **No circular deps** | Framework can depend on Adapter, UseCase, Enterprise. Never the reverse. |
| **DI Config owns composition** | Only Framework layer knows how all pieces fit together. |
| **Profiles for environments** | Use Spring profiles to swap adapter implementations (e.g., MockPaymentGateway for test). |
| **Secrets externalized** | API keys, DB passwords via env vars, never hardcoded. |
