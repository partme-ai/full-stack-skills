# Middleware | 中间件

**官方文档**: https://docs.nestjs.com/middleware


## Instructions

This example demonstrates how to create and use middleware in NestJS.

### Key Concepts

- Creating middleware classes
- Functional middleware
- Applying middleware
- Global middleware
- Route-specific middleware

### Example: Class-Based Middleware

```typescript
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log(`Request... ${req.method} ${req.url}`);
    next();
  }
}
```

### Example: Functional Middleware

```typescript
import { Request, Response, NextFunction } from 'express';

export function logger(req: Request, res: Response, next: NextFunction) {
  console.log(`Request... ${req.method} ${req.url}`);
  next();
}
```

### Example: Applying Middleware in Module

```typescript
import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes('cats');
  }
}
```

### Example: Multiple Routes

```typescript
configure(consumer: MiddlewareConsumer) {
  consumer
    .apply(LoggerMiddleware)
    .forRoutes({ path: 'cats', method: RequestMethod.GET });
}
```

### Example: Route Exclusions

```typescript
configure(consumer: MiddlewareConsumer) {
  consumer
    .apply(LoggerMiddleware)
    .exclude(
      { path: 'cats', method: RequestMethod.GET },
      { path: 'cats', method: RequestMethod.POST },
      'cats/(.*)',
    )
    .forRoutes(CatsController);
}
```

### Example: Global Middleware

```typescript
// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { logger } from './common/middleware/logger.middleware';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.use(logger);
  await app.listen(3000);
}
bootstrap();
```

### Key Points

- Middleware executes before route handlers
- Can be class-based or functional
- Use `MiddlewareConsumer` to apply middleware
- Can apply to specific routes or exclude routes
- Global middleware applies to all routes
- Middleware has access to request, response, and next function
