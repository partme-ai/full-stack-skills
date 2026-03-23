# First Steps | 快速开始

**官方文档**: https://docs.nestjs.com/first-steps


## Instructions

This example demonstrates how to create a new NestJS application and understand the basic project structure.

### Key Concepts

- Installing NestJS CLI
- Creating a new project
- Project structure
- Running the application
- Basic application setup

### Example: Installation

```bash
# Install NestJS CLI globally
npm i -g @nestjs/cli

# Or using yarn
yarn global add @nestjs/cli
```

### Example: Creating a New Project

```bash
# Create a new project
nest new project-name

# Or using npm
npm i -g @nestjs/cli
nest new project-name
```

### Example: Project Structure

```
project-name/
├── src/
│   ├── app.controller.ts      # Basic controller
│   ├── app.controller.spec.ts  # Controller tests
│   ├── app.service.ts         # Basic service
│   ├── app.module.ts          # Root module
│   └── main.ts                # Application entry point
├── test/                       # E2E tests
├── node_modules/
├── package.json
├── tsconfig.json              # TypeScript configuration
└── nest-cli.json              # NestJS CLI configuration
```

### Example: Basic Application

```typescript
// src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

```typescript
// src/app.module.ts
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

```typescript
// src/app.controller.ts
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
```

```typescript
// src/app.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}
```

### Example: Running the Application

```bash
# Development mode
npm run start

# Watch mode
npm run start:dev

# Production mode
npm run start:prod

# Debug mode
npm run start:debug
```

### Example: Generating Files

```bash
# Generate a controller
nest generate controller cats
# or
nest g controller cats

# Generate a service
nest generate service cats
# or
nest g service cats

# Generate a module
nest generate module cats
# or
nest g module cats
```

### Key Points

- Use NestJS CLI for project generation and file scaffolding
- Application entry point is `main.ts`
- Root module is `AppModule`
- Controllers handle HTTP requests
- Services contain business logic
- Use `@Injectable()` decorator for services
- Use `@Controller()` decorator for controllers
- Use `@Module()` decorator for modules
