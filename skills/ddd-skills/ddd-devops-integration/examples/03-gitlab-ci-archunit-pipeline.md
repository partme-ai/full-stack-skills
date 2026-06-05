# GitLab CI — ArchUnit Architecture Validation Pipeline

```yaml
# .gitlab-ci.yml — DDD Architecture Quality Gate
stages:
  - build
  - architecture-validation
  - test
  - security
  - deploy

variables:
  MAVEN_CLI_OPTS: "--batch-mode --errors --fail-at-end"
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .m2/repository/
    - domain/target/

# ──── Build Stage ────
compile:
  stage: build
  script:
    - mvn $MAVEN_CLI_OPTS compile -pl domain,application,infrastructure -am
  artifacts:
    paths:
      - domain/target/classes/
      - application/target/classes/
      - infrastructure/target/classes/
    expire_in: 2 hours

# ──── Architecture Validation ────
architecture-validation:
  stage: architecture-validation
  script:
    # P0 Checks — Block on failure
    - mvn $MAVEN_CLI_OPTS test -pl domain
      -Dtest=ArchitectureComplianceTest#domain_no_spring
    - mvn $MAVEN_CLI_OPTS test -pl domain
      -Dtest=ArchitectureComplianceTest#domain_no_infrastructure
    # P1 Checks — Warn on failure
    - mvn $MAVEN_CLI_OPTS test -pl domain
      -Dtest=ArchitectureComplianceTest#layered_architecture ||
      echo "⚠️ P1 violation detected, manual review required"
    # P2 Checks — Report only
    - mvn $MAVEN_CLI_OPTS test -pl domain
      -Dtest=ArchitectureComplianceTest#naming_conventions ||
      echo "📋 P2 violation logged for review"
  artifacts:
    when: always
    reports:
      junit: domain/target/surefire-reports/TEST-*.xml
    paths:
      - domain/target/surefire-reports/
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      when: always
    - if: $CI_COMMIT_BRANCH == "main"
      when: always
    - when: manual

# ──── Integration Tests ────
integration-test:
  stage: test
  services:
    - postgres:16-alpine
    - redis:7-alpine
  variables:
    SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/testdb
    SPRING_DATASOURCE_USERNAME: postgres
    SPRING_DATASOURCE_PASSWORD: test
    SPRING_CACHE_REDIS_HOST: redis
  script:
    - mvn $MAVEN_CLI_OPTS verify -pl infrastructure
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"

# ──── OWASP Dependency Check ────
dependency-security:
  stage: security
  script:
    - mvn $MAVEN_CLI_OPTS org.owasp:dependency-check-maven:check
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# ──── Deploy to Staging ────
deploy-staging:
  stage: deploy
  image: bitnami/kubectl:1.29
  script:
    - kubectl set image deployment/$CI_PROJECT_NAME
      app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA -n staging
    - kubectl rollout status deployment/$CI_PROJECT_NAME -n staging
  environment:
    name: staging
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: manual
```

## Pipeline Flow Diagram

```
                     ┌──────────────┐
                     │    Commit    │
                     └──────┬───────┘
                            ▼
                     ┌──────────────┐
                     │    Compile   │
                     └──────┬───────┘
                            ▼
                     ┌──────────────┐
                     │  Architecture│  ← ArchUnit P0 blocks here
                     │  Validation  │
                     └──────┬───────┘
                            ▼
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
      ┌──────────────┐           ┌────────────────┐
      │  Integration │           │  Security Scan  │
      │    Tests     │           │  (parallel)     │
      └──────┬───────┘           └───────┬────────┘
              │                           │
              └─────────────┬─────────────┘
                            ▼
                     ┌──────────────┐
                     │    Deploy    │ (manual gate)
                     │   Staging    │
                     └──────────────┘
```
