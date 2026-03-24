# Project Structure Template | 项目结构模板

## Standard NestJS Project Structure

```
project-name/
├── src/
│   ├── main.ts                    # Application entry point
│   ├── app.module.ts             # Root module
│   ├── app.controller.ts         # Root controller
│   ├── app.service.ts            # Root service
│   ├── common/                   # Shared utilities
│   │   ├── decorators/
│   │   ├── filters/
│   │   ├── guards/
│   │   ├── interceptors/
│   │   └── pipes/
│   ├── config/                   # Configuration
│   │   └── configuration.ts
│   ├── database/                  # Database configuration
│   │   └── database.module.ts
│   └── modules/                   # Feature modules
│       ├── auth/
│       │   ├── auth.module.ts
│       │   ├── auth.controller.ts
│       │   ├── auth.service.ts
│       │   ├── strategies/
│       │   └── guards/
│       ├── users/
│       │   ├── users.module.ts
│       │   ├── users.controller.ts
│       │   ├── users.service.ts
│       │   ├── entities/
│       │   ├── dto/
│       │   └── users.controller.spec.ts
│       └── cats/
│           ├── cats.module.ts
│           ├── cats.controller.ts
│           ├── cats.service.ts
│           ├── entities/
│           ├── dto/
│           └── cats.controller.spec.ts
├── test/                          # E2E tests
│   ├── app.e2e-spec.ts
│   └── jest-e2e.json
├── .env                          # Environment variables
├── .gitignore
├── nest-cli.json                 # NestJS CLI configuration
├── package.json
├── tsconfig.json                 # TypeScript configuration
└── README.md
```

## Module Structure

```
module-name/
├── module-name.module.ts         # Module definition
├── module-name.controller.ts     # Controller
├── module-name.service.ts        # Service
├── entities/                     # Database entities
│   └── entity-name.entity.ts
├── dto/                          # Data Transfer Objects
│   ├── create-dto.dto.ts
│   └── update-dto.dto.ts
├── interfaces/                   # TypeScript interfaces
│   └── interface-name.interface.ts
└── module-name.controller.spec.ts # Unit tests
```
