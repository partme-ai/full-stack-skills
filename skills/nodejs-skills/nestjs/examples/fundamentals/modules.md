# Modules | 模块

**官方文档**: https://docs.nestjs.com/modules


## Instructions

This example demonstrates how to create and organize modules in NestJS.

### Key Concepts

- Creating modules with `@Module()`
- Module imports, exports, and providers
- Feature modules
- Shared modules
- Global modules
- Dynamic modules

### Example: Basic Module

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

### Example: Feature Module

```typescript
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
  exports: [CatsService], // Export to make it available to other modules
})
export class CatsModule {}
```

### Example: Importing Modules

```typescript
import { Module } from '@nestjs/common';
import { CatsModule } from './cats/cats.module';
import { DogsModule } from './dogs/dogs.module';

@Module({
  imports: [CatsModule, DogsModule],
})
export class AppModule {}
```

### Example: Shared Module

```typescript
import { Module, Global } from '@nestjs/common';
import { CommonService } from './common.service';

@Global()
@Module({
  providers: [CommonService],
  exports: [CommonService],
})
export class CommonModule {}
```

### Example: Dynamic Module

```typescript
import { Module, DynamicModule } from '@nestjs/common';
import { ConfigModule } from './config.module';

@Module({})
export class DatabaseModule {
  static forRoot(options: DatabaseOptions): DynamicModule {
    return {
      module: DatabaseModule,
      providers: [
        {
          provide: 'DATABASE_OPTIONS',
          useValue: options,
        },
        DatabaseService,
      ],
      exports: [DatabaseService],
    };
  }
}

// Usage
@Module({
  imports: [DatabaseModule.forRoot({ host: 'localhost', port: 5432 })],
})
export class AppModule {}
```

### Example: Module Re-exporting

```typescript
import { Module } from '@nestjs/common';
import { CatsModule } from './cats/cats.module';
import { DogsModule } from './dogs/dogs.module';

@Module({
  imports: [CatsModule, DogsModule],
  exports: [CatsModule, DogsModule], // Re-export modules
})
export class AnimalModule {}
```

### Key Points

- Modules organize application structure
- Use `@Module()` decorator with imports, controllers, providers, exports
- Feature modules encapsulate related functionality
- Shared modules export providers for reuse
- Global modules are available everywhere
- Dynamic modules accept configuration
- Export providers to make them available to other modules
- Import modules to use their exported providers
