---
name: spring-data-jpa
description: "Provides comprehensive guidance for Spring Data JPA including repositories, entity management, query methods, and database operations. Use when the user asks about Spring Data JPA, needs to work with JPA repositories, implement data access layers, or configure JPA in Spring."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Define JPA entities with annotations (@Entity, @Id, @Column)
- Create Spring Data repositories (JpaRepository, CrudRepository)
- Use derived query methods, @Query with JPQL/native SQL, and Specifications
- Configure data sources, Hibernate dialect, and transaction management
- Handle pagination, sorting, auditing, and entity graphs

## How to use this skill

### Workflow

1. **Define entities** with JPA annotations and relationship mappings
2. **Create repositories** extending JpaRepository with derived or custom query methods
3. **Configure the data source** in `application.yml` or `application.properties`
4. **Use services** to encapsulate business logic with proper transaction boundaries

### 1. Entity Definition

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(unique = true, nullable = false)
    private String email;

    @CreatedDate
    private LocalDateTime createdAt;

    // Getters and setters
}
```

### 2. Repository

```java
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByNameContaining(String name);
    Page<User> findByNameContaining(String name, Pageable pageable);

    @Query("SELECT u FROM User u WHERE u.email = :email")
    Optional<User> findByEmailCustom(@Param("email") String email);
}
```

### 3. Service with Transactions

```java
@Service
@Transactional
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User create(String name, String email) {
        User user = new User();
        user.setName(name);
        user.setEmail(email);
        return userRepository.save(user);
    }

    @Transactional(readOnly = true)
    public Page<User> search(String name, Pageable pageable) {
        return userRepository.findByNameContaining(name, pageable);
    }
}
```

### 4. Configuration

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: postgres
    password: password
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate.format_sql: true
```

## Best Practices

- Watch for N+1 query problems; use `@EntityGraph` or `JOIN FETCH` to control fetch strategy
- Use pagination (`Pageable`) and batch operations for large datasets
- Separate entities from DTOs; never expose JPA entities directly in API responses
- Define clear transaction boundaries; use `@Transactional(readOnly = true)` for read operations
- Use Flyway or Liquibase for schema migrations instead of `ddl-auto: update` in production

## Resources

- Official documentation: https://spring.io/projects/spring-data-jpa
- Reference guide: https://docs.spring.io/spring-data/jpa/reference/

## Keywords

spring data jpa, JPA, Repository, entity, query methods, JPQL, pagination, transactions, Hibernate, Spring Boot, persistence
