# GitLab CI DDD Pipeline Reference

## Full Pipeline Configuration

```yaml
stages:
  - build
  - unit-test
  - architecture-check
  - integration-test
  - security-scan
  - build-image
  - deploy

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"
  MAVEN_CLI_OPTS: "--batch-mode --errors --fail-at-end"

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .m2/repository/
    - domain/target/
    - application/target/

# Stage 1: Build
compile:
  stage: build
  script:
    - mvn $MAVEN_CLI_OPTS compile -pl domain,application -am
  artifacts:
    paths:
      - domain/target/
      - application/target/
    expire_in: 2 hours

# Stage 2: Unit Tests
unit-test:
  stage: unit-test
  script:
    - mvn $MAVEN_CLI_OPTS test -pl domain -Dtest='*ValueObjectTest,*AggregateTest'
  artifacts:
    reports:
      junit: domain/target/surefire-reports/TEST-*.xml

# Stage 3: Architecture Compliance (Quality Gate)
architecture-check:
  stage: architecture-check
  script:
    - mvn $MAVEN_CLI_OPTS test -pl domain -Dtest=ArchitectureComplianceTest
  artifacts:
    paths:
      - domain/target/archunit-report/
    reports:
      junit: domain/target/surefire-reports/TEST-*.xml
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      when: always
    - if: $CI_COMMIT_BRANCH == "main"
      when: always

# Stage 4: Integration Tests
integration-test:
  stage: integration-test
  services:
    - postgres:16-alpine
  variables:
    SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/testdb
    SPRING_DATASOURCE_USERNAME: postgres
    SPRING_DATASOURCE_PASSWORD: test
  script:
    - mvn $MAVEN_CLI_OPTS verify -pl infrastructure
      -Dtest='*RepositoryImplTest'
  needs: [compile, unit-test]

# Stage 5: Security Scan
security-scan:
  stage: security-scan
  script:
    - mvn $MAVEN_CLI_OPTS verify -pl start -DskipTests
    - mvn $MAVEN_CLI_OPTS dependency-check:check
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# Stage 6: Build Docker Image
docker-build:
  stage: build-image
  image: docker:24.0.5
  services:
    - docker:24.0.5-dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# Stage 7: Deploy to K8s
deploy:
  stage: deploy
  image: bitnami/kubectl:1.29
  script:
    - kubectl set image deployment/order-service
      order-service=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
      -n bc-orders
    - kubectl rollout status deployment/order-service -n bc-orders
  environment:
    name: production/bc-orders
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: manual
```

## Merge Request Approval Rules

```yaml
# .gitlab/merge_request_templates/DDD_Quality_Gate.md
## Architecture Compliance Checklist

- [ ] All ArchUnit P0 tests pass ✅
- [ ] No circular dependencies detected ✅
- [ ] Domain layer has zero framework dependencies ✅
- [ ] Layered dependency direction is correct ✅

## Required Approvals

| Role | Required? |
|------|:---------:|
| Developer | ✅ |
| Senior Developer | ✅ (if P0 violation) |
| Architect | ✅ (if architecture change) |
