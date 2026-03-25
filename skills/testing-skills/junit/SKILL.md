---
name: junit
description: "Provides comprehensive guidance for JUnit testing framework including test annotations, assertions, test lifecycle, and best practices. Use when the user asks about JUnit, needs to write Java unit tests, use JUnit annotations, or configure JUnit for Java projects."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write Java or Kotlin unit tests with JUnit 4 or JUnit 5 (Jupiter)
- Use annotations (@Test, @BeforeEach, @AfterEach, @ParameterizedTest)
- Apply assertions (assertEquals, assertThrows, assertAll)
- Integrate with Mockito or AssertJ for mocking and fluent assertions
- Configure test execution with Maven Surefire or Gradle

## How to use this skill

### Workflow

1. **Write test classes and methods** annotated with `@Test`
2. **Set up and tear down** test state with lifecycle annotations
3. **Use assertions** to verify expected behavior
4. **Mock dependencies** with Mockito for isolated unit tests

### 1. Basic JUnit 5 Test

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    @Test
    void shouldAddTwoNumbers() {
        Calculator calc = new Calculator();
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void shouldThrowOnDivideByZero() {
        Calculator calc = new Calculator();
        assertThrows(ArithmeticException.class, () -> calc.divide(1, 0));
    }
}
```

### 2. Lifecycle Annotations

```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;

class UserServiceTest {
    private UserService userService;

    @BeforeEach
    void setUp() {
        userService = new UserService(new InMemoryUserRepository());
    }

    @AfterEach
    void tearDown() {
        // Clean up resources
    }
}
```

### 3. Parameterized Tests

```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class StringTest {
    @ParameterizedTest
    @CsvSource({"hello,5", "'',0", "junit,5"})
    void shouldReturnCorrectLength(String input, int expected) {
        assertEquals(expected, input.length());
    }
}
```

### 4. Mocking with Mockito

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
    @Mock private OrderRepository orderRepository;
    @InjectMocks private OrderService orderService;

    @Test
    void shouldSaveOrder() {
        Order order = new Order("item-1", 2);
        orderService.placeOrder(order);
        verify(orderRepository).save(order);
    }
}
```

### 5. Running Tests

```bash
# Maven
mvn test

# Gradle
gradle test

# With coverage (JaCoCo)
mvn test jacoco:report
```

## Best Practices

- Keep tests independent and repeatable; avoid dependencies on execution order or external services
- Use Mockito to isolate the unit under test from its dependencies
- Name tests descriptively (e.g., `shouldReturnEmptyListWhenNoUsersExist`)
- Balance coverage with test speed; run full suite in CI
- Use `@Nested` classes to group related test cases

## Resources

- JUnit 5 User Guide: https://junit.org/junit5/docs/current/user-guide/
- Mockito: https://site.mockito.org/
- AssertJ: https://assertj.github.io/doc/

## Keywords

junit, JUnit 5, JUnit Jupiter, unit testing, Java, Kotlin, assertions, Mockito, parameterized tests, BeforeEach, AfterEach, test lifecycle
