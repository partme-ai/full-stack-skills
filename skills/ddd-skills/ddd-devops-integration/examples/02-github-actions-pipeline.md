# GitHub Actions — Full DDD Quality Gate Pipeline

```yaml
name: DDD Quality Gate

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]

env:
  MAVEN_OPTS: -Dmaven.repo.local=${{ github.workspace }}/.m2/repository

jobs:
  # ──── Build & Unit Tests ────
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
          cache: maven
      - name: Build & Unit Tests
        run: mvn test -pl domain,application
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: '**/target/surefire-reports/'

  # ──── Architecture Validation (Critical Gate) ────
  architecture-check:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
          cache: maven
      - name: Domain Purity Check (P0)
        run: mvn test -pl domain -Dtest=DomainPurityTest
      - name: Layering Compliance Check (P0)
        run: mvn test -pl domain -Dtest=LayeringComplianceTest
      - name: Module Dependency Check (P1)
        run: mvn test -pl domain -Dtest=ModuleDependencyTest
      - name: Naming Convention Check (P2)
        run: mvn test -pl domain -Dtest=NamingConventionTest
      - name: Upload ArchUnit report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: archunit-report
          path: domain/target/surefire-reports/

  # ──── Integration Tests ────
  integration-test:
    needs: architecture-check
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: testdb
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
          cache: maven
      - name: Repository Integration Tests
        run: mvn test -pl infrastructure -Dtest='*RepositoryImplTest'
        env:
          SPRING_DATASOURCE_URL: jdbc:postgresql://localhost:5432/testdb
          SPRING_DATASOURCE_USERNAME: postgres
          SPRING_DATASOURCE_PASSWORD: test

  # ──── Build Docker Image ────
  docker-build:
    needs: integration-test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.REGISTRY_URL }}
          username: ${{ secrets.REGISTRY_USER }}
          password: ${{ secrets.REGISTRY_PASS }}
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ secrets.REGISTRY_URL }}/order-service:${{ github.sha }}
            ${{ secrets.REGISTRY_URL }}/order-service:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## Failure Policy Summary

| Check | Severity | CI Behavior | Action Required |
|:----:|:--------:|:-----------:|:---------------:|
| Domain purity | P0 | Block merge | Fix domain layer dependencies |
| Layering | P0 | Block merge | Fix cross-layer imports |
| Module cycles | P1 | Warning + approval | Refactor module structure |
| Naming conventions | P2 | Report only | Log for next sprint |
| Integration tests | P0 | Block merge | Fix broken repository tests |
| Docker build | P0 | Block release | Fix Dockerfile or build config |
