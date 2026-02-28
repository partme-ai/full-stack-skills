# Custom Decorators | 自定义装饰器

**官方文档**: https://docs.nestjs.com/custom-decorators

## Instructions

This example demonstrates how to create custom decorators in NestJS to improve code readability and reusability.

### Key Concepts

- Creating parameter decorators with `createParamDecorator()`
- Creating method decorators
- Creating class decorators
- Combining decorators
- Using decorators with metadata

### Example: Parameter Decorator

```typescript
import { createParamDecorator, ExecutionContext } from '@nestjs/common';

// User(): 自定义参数装饰器，从请求中提取用户信息
export const User = createParamDecorator(
  (data: unknown, ctx: ExecutionContext) => {
    const request = ctx.switchToHttp().getRequest();
    return request.user;
  },
);

// Usage in controller
@Controller('profile')
export class ProfileController {
  @Get()
  getProfile(@User() user: any) {
    return user;
  }
}
```

### Example: Method Decorator

```typescript
import { SetMetadata } from '@nestjs/common';

// Roles(): 自定义方法装饰器，设置角色元数据
export const Roles = (...roles: string[]) => SetMetadata('roles', roles);

// Usage in controller
@Controller('admin')
export class AdminController {
  @Get('users')
  @Roles('admin', 'moderator')
  getUsers() {
    return [];
  }
}
```

### Example: Combining Decorators

```typescript
import { applyDecorators, UseGuards, SetMetadata } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

// Auth(): 组合装饰器，同时应用守卫和元数据
export function Auth(...roles: string[]) {
  return applyDecorators(
    SetMetadata('roles', roles),
    UseGuards(AuthGuard('jwt')),
  );
}

// Usage
@Controller('protected')
export class ProtectedController {
  @Get('data')
  @Auth('admin')
  getData() {
    return { data: 'protected' };
  }
}
```

### Example: Class Decorator

```typescript
import { SetMetadata } from '@nestjs/common';

// ApiVersion(): 自定义类装饰器，设置 API 版本
export const ApiVersion = (version: string) => SetMetadata('apiVersion', version);

// Usage
@ApiVersion('V1')
@Controller('users')
export class UsersController {
  @Get()
  findAll() {
    return [];
  }
}
```

### Key Points

- Use `createParamDecorator()` for parameter decorators
- Use `SetMetadata()` to attach metadata to handlers
- Use `applyDecorators()` to combine multiple decorators
- Custom decorators improve code readability and reusability
- Decorators can access execution context and request/response objects
