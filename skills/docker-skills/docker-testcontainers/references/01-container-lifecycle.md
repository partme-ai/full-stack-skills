# Testcontainers Lifecycle

```
Singleton (static field — one container for all tests in class):
@Container
static PostgreSQLContainer<?> pg = new PostgreSQLContainer<>();

→ Container starts once before all tests
→ Container shared across all test methods
→ Faster but tests must not conflict on data

Per-test (instance field — new container per test):
@Container
PostgreSQLContainer<?> pg = new PostgreSQLContainer<>();

→ New container for EACH test method
→ Slower but complete isolation
→ Good for tests that modify schema

Manual lifecycle:
try (var pg = new PostgreSQLContainer<>("postgres:16")) {
    pg.start();
    // test...
} // auto-closed

Reuse (local development speed):
static PostgreSQLContainer<?> pg = new PostgreSQLContainer<>()
    .withReuse(true);
→ Container survives JVM exit, reused on next run
→ Requires ~/.testcontainers.properties: testcontainers.reuse.enable=true
```
