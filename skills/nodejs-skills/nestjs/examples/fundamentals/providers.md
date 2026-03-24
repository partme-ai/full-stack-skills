# Providers | 提供者

**官方文档**: https://docs.nestjs.com/providers


## Instructions

This example demonstrates how to create providers (services) and use dependency injection in NestJS.

### Key Concepts

- Creating providers with `@Injectable()`
- Dependency injection
- Using providers in controllers
- Provider scopes
- Custom providers

### Example: Basic Service

```typescript
import { Injectable } from '@nestjs/common';

@Injectable()
export class CatsService {
  private readonly cats: Cat[] = [];

  findAll(): Cat[] {
    return this.cats;
  }

  create(cat: Cat): Cat {
    this.cats.push(cat);
    return cat;
  }

  findOne(id: number): Cat {
    return this.cats.find(cat => cat.id === id);
  }
}
```

### Example: Using Service in Controller

```typescript
import { Controller, Get, Post, Body } from '@nestjs/common';
import { CatsService } from './cats.service';
import { CreateCatDto } from './dto/create-cat.dto';

@Controller('cats')
export class CatsController {
  constructor(private readonly catsService: CatsService) {}

  @Get()
  findAll() {
    return this.catsService.findAll();
  }

  @Post()
  create(@Body() createCatDto: CreateCatDto) {
    return this.catsService.create(createCatDto);
  }
}
```

### Example: Registering Provider in Module

```typescript
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}
```

### Example: Optional Providers

```typescript
import { Injectable, Optional, Inject } from '@nestjs/common';

@Injectable()
export class HttpService {
  constructor(
    @Optional() @Inject('HTTP_OPTIONS') private httpClient: any,
  ) {}
}
```

### Example: Custom Providers (useValue)

```typescript
import { Module } from '@nestjs/common';

const config = {
  apiKey: 'my-api-key',
  timeout: 5000,
};

@Module({
  providers: [
    {
      provide: 'CONFIG',
      useValue: config,
    },
  ],
})
export class AppModule {}
```

### Example: Custom Providers (useFactory)

```typescript
import { Module } from '@nestjs/common';

@Module({
  providers: [
    {
      provide: 'CONNECTION',
      useFactory: (optionsProvider: OptionsProvider) => {
        const options = optionsProvider.create();
        return new DatabaseConnection(options);
      },
      inject: [OptionsProvider],
    },
  ],
})
export class AppModule {}
```

### Example: Custom Providers (useClass)

```typescript
import { Module } from '@nestjs/common';

@Module({
  providers: [
    {
      provide: 'CONFIG_SERVICE',
      useClass: ConfigService,
    },
  ],
})
export class AppModule {}
```

### Example: Provider Scopes

```typescript
import { Injectable, Scope } from '@nestjs/common';

@Injectable({ scope: Scope.REQUEST })
export class CatsService {
  // Service instance is created for each request
}
```

### Key Points

- Use `@Injectable()` decorator for providers
- Providers are injected via constructor
- Register providers in module's `providers` array
- Use custom providers for advanced scenarios
- Provider scopes: DEFAULT, REQUEST, TRANSIENT
- Use `@Inject()` for custom tokens
- Use `@Optional()` for optional dependencies
