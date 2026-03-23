# Controllers | 控制器

**官方文档**: https://docs.nestjs.com/controllers


## Instructions

This example demonstrates how to create controllers and handle HTTP requests in NestJS.

### Key Concepts

- Creating controllers with `@Controller()`
- Route handlers with `@Get()`, `@Post()`, `@Put()`, `@Delete()`, `@Patch()`
- Route parameters with `@Param()`
- Query parameters with `@Query()`
- Request body with `@Body()`
- Request and response objects

### Example: Basic Controller

```typescript
import { Controller, Get } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(): string {
    return 'This action returns all cats';
  }
}
```

### Example: Route Parameters

```typescript
import { Controller, Get, Param } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get(':id')
  findOne(@Param('id') id: string): string {
    return `This action returns a #${id} cat`;
  }

  @Get(':id/owner/:ownerId')
  findOneWithOwner(
    @Param('id') id: string,
    @Param('ownerId') ownerId: string,
  ): string {
    return `Cat #${id} owned by #${ownerId}`;
  }
}
```

### Example: Query Parameters

```typescript
import { Controller, Get, Query } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(@Query('limit') limit: number): string {
    return `This action returns all cats (limit: ${limit})`;
  }
}
```

### Example: Request Body

```typescript
import { Controller, Post, Body } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Post()
  create(@Body() createCatDto: CreateCatDto): string {
    return 'This action adds a new cat';
  }
}
```

### Example: All HTTP Methods

```typescript
import { Controller, Get, Post, Put, Delete, Patch, Body, Param } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(): string {
    return 'This action returns all cats';
  }

  @Get(':id')
  findOne(@Param('id') id: string): string {
    return `This action returns a #${id} cat`;
  }

  @Post()
  create(@Body() createCatDto: CreateCatDto): string {
    return 'This action adds a new cat';
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateCatDto: UpdateCatDto): string {
    return `This action updates a #${id} cat`;
  }

  @Patch(':id')
  partialUpdate(@Param('id') id: string, @Body() updateCatDto: UpdateCatDto): string {
    return `This action partially updates a #${id} cat`;
  }

  @Delete(':id')
  remove(@Param('id') id: string): string {
    return `This action removes a #${id} cat`;
  }
}
```

### Example: Status Codes

```typescript
import { Controller, Get, HttpCode, HttpStatus, Post } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Post()
  @HttpCode(HttpStatus.CREATED)
  create(): string {
    return 'This action adds a new cat';
  }

  @Get()
  @HttpCode(200)
  findAll(): string {
    return 'This action returns all cats';
  }
}
```

### Example: Headers

```typescript
import { Controller, Get, Header } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  @Header('Cache-Control', 'no-cache')
  findAll(): string {
    return 'This action returns all cats';
  }
}
```

### Example: Redirects

```typescript
import { Controller, Get, Redirect } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  @Redirect('https://nestjs.com', 301)
  redirect() {
    return { url: 'https://nestjs.com' };
  }
}
```

### Key Points

- Controllers handle incoming requests and return responses
- Use `@Controller()` decorator with optional route prefix
- Route handlers use HTTP method decorators (`@Get()`, `@Post()`, etc.)
- Use `@Param()` to extract route parameters
- Use `@Query()` to extract query parameters
- Use `@Body()` to extract request body
- Use `@HttpCode()` to set status codes
- Use `@Header()` to set response headers
- Use `@Redirect()` for redirects
