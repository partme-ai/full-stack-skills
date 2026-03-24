# Pipes | 管道

**官方文档**: https://docs.nestjs.com/pipes


## Instructions

This example demonstrates how to create and use pipes for validation and transformation in NestJS.

### Key Concepts

- Built-in pipes
- Custom pipes
- Validation pipes
- Transformation pipes
- Using pipes globally

### Example: Built-in Pipes

```typescript
import { Controller, Get, Param, Query, UsePipes, ParseIntPipe, ParseBoolPipe } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number) {
    return `This action returns a #${id} cat`;
  }

  @Get()
  findAll(@Query('active', ParseBoolPipe) active: boolean) {
    return `This action returns all cats (active: ${active})`;
  }
}
```

### Example: Custom Validation Pipe

```typescript
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';

@Injectable()
export class ValidationPipe implements PipeTransform {
  transform(value: any, metadata: ArgumentMetadata) {
    if (!value) {
      throw new BadRequestException('Value is required');
    }
    return value;
  }
}
```

### Example: Using ValidationPipe

```typescript
import { Controller, Post, Body, UsePipes, ValidationPipe } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';

@Controller('cats')
export class CatsController {
  @Post()
  @UsePipes(ValidationPipe)
  create(@Body() createCatDto: CreateCatDto) {
    return this.catsService.create(createCatDto);
  }
}
```

### Example: Global Validation Pipe

```typescript
// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(new ValidationPipe());
  await app.listen(3000);
}
bootstrap();
```

### Example: Transformation Pipe

```typescript
import { PipeTransform, Injectable, ArgumentMetadata } from '@nestjs/common';

@Injectable()
export class ParseIntPipe implements PipeTransform<string, number> {
  transform(value: string, metadata: ArgumentMetadata): number {
    const val = parseInt(value, 10);
    if (isNaN(val)) {
      throw new BadRequestException('Validation failed');
    }
    return val;
  }
}
```

### Example: Custom Pipe with DTO

```typescript
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';
import { validate } from 'class-validator';
import { plainToClass } from 'class-transformer';

@Injectable()
export class ValidationPipe implements PipeTransform<any> {
  async transform(value: any, { metatype }: ArgumentMetadata) {
    if (!metatype || !this.toValidate(metatype)) {
      return value;
    }
    const object = plainToClass(metatype, value);
    const errors = await validate(object);
    if (errors.length > 0) {
      throw new BadRequestException('Validation failed');
    }
    return value;
  }

  private toValidate(metatype: Function): boolean {
    const types: Function[] = [String, Boolean, Number, Array, Object];
    return !types.includes(metatype);
  }
}
```

### Key Points

- Pipes transform or validate input data
- Built-in pipes: ParseIntPipe, ParseBoolPipe, ParseUUIDPipe, etc.
- Use ValidationPipe for DTO validation
- Pipes can be applied globally or per route
- Custom pipes implement PipeTransform interface
- Pipes execute before route handlers
